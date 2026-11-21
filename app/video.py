"""Video support by frames: sample still frames, run the photo pipeline on each, and merge.

    analyze_video(path, address=None, answers=None) -> dict   (same shape as pipeline.analyze, plus timestamps)

A problem is reported only if it is confirmed in at least `min_confirming_frames` frames (one frame for a
very short clip), which keeps a single odd frame from raising a false alarm. Each reported problem carries
the times it was seen and the clearest frame, saved as a still so it can be shown and used as evidence.
Sound is ignored. Needs ffmpeg on the machine.
"""
import logging
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from app import building as building_mod
from app import media, pipeline

VIDEO_TYPES = {".mp4": "video/mp4", ".mov": "video/quicktime", ".webm": "video/webm", ".m4v": "video/x-m4v"}
log = logging.getLogger("tenant")


def duration(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, timeout=30, check=False).stdout.strip()
    try:
        return float(out or 0)
    except ValueError:  # a clip recorded in the browser can report "N/A"
        return 0.0


def frame_times(seconds: float) -> list[float]:
    """Evenly spaced times: one about every `seconds_per_frame`, between `min_frames` and `max_frames` of them."""
    v = pipeline.THRESHOLDS["video"]
    n = max(v["min_frames"], min(v["max_frames"], round(seconds / v["seconds_per_frame"])))
    if seconds <= 0:
        return [0.0]
    return [round(seconds * (i + 0.5) / n, 2) for i in range(n)]


def grab(path: Path, t: float) -> bytes | None:
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", str(t), "-i", str(path), "-frames:v", "1",
         "-vf", "scale='min(1280,iw)':-2", "-q:v", "3", "-f", "image2pipe", "-vcodec", "mjpeg", "-"],
        capture_output=True, timeout=60, check=False)
    return r.stdout if r.returncode == 0 and r.stdout else None


def frames(path: Path) -> list[tuple[float, bytes]]:
    times = frame_times(duration(path))
    with ThreadPoolExecutor(max_workers=6) as pool:
        got = list(pool.map(lambda t: grab(path, t), times))
    return [(t, b) for t, b in zip(times, got, strict=True) if b]


def confirming_frames_needed(frame_count: int) -> int:
    need = pipeline.THRESHOLDS["video"]["min_confirming_frames"]
    return 1 if frame_count <= pipeline.THRESHOLDS["video"]["min_frames"] else need


def merge(per_frame: list[tuple[float, dict]]) -> tuple[list[dict], dict]:
    """Group frame findings by problem type. Returns (reported findings, counts of everything seen)."""
    seen: dict[str, list[tuple[float, dict]]] = {}
    for t, res in per_frame:
        for f in res["findings"]:
            seen.setdefault(f["problem_type"], []).append((t, f))
    need = confirming_frames_needed(len(per_frame))
    out = []
    for hits in seen.values():
        if len(hits) < need:
            continue
        t_best, best = max(hits, key=lambda h: h[1]["probability"])
        times = sorted(t for t, _ in hits)
        out.append({**best, "time_s": t_best, "seen_at_s": times, "time_range_s": [times[0], times[-1]],
                    "frames_confirming": len(hits)})
    out.sort(key=lambda f: -f["probability"])
    return out, {k: len(v) for k, v in seen.items()}


def analyze_video(path: Path, address: str | None = None, answers: dict | None = None,
                  with_explanation: bool = True, save_frames: bool = True, note: str | None = None,
                  seen: dict | None = None) -> dict:
    """note: what the tenant typed, read once for facts (never shown to the step that looks at the frames).
    seen: what the models read from each frame on an earlier run of this video, keyed by frame time. Pass the
    same dict back for a follow-up (an answer, an address) and the frames are not looked at again; an empty
    dict is filled in."""
    t0 = time.perf_counter()
    stills = frames(path)
    if not stills:
        raise ValueError("No frames could be read from this video")
    bld, bld_error = None, None
    if address:
        try:
            bld = building_mod.lookup(address)
        except building_mod.AddressNotFound:
            bld_error = f"No NYC address found for: {address}"
        except Exception:  # the city's records being down must not lose the video's answer
            log.warning("building lookup failed", exc_info=True)
            bld_error = "The city's building records could not be reached just now."
    said = {}
    if note and note.strip():
        try:
            said = pipeline.facts_from_note(note)
        except Exception:  # noqa: BLE001 - reading the note is a convenience; the answer doesn't depend on it
            said = {}
    answers = {**said, **(answers or {})}
    seen = {} if seen is None else seen

    def one(item):
        t, data = item
        frame_seen = seen.get(f"{t:.2f}") or {}
        try:
            res = pipeline.analyze(data, "image/jpeg", answers=answers, with_explanation=False, building=bld,
                                   seen=frame_seen)
        except Exception:  # one frame the models didn't answer for must not lose the other fifteen
            log.warning("frame at %.1f s failed", t, exc_info=True)
            return None
        seen[f"{t:.2f}"] = frame_seen
        return t, res

    # Every frame at once (there are at most `max_frames`), so the wait is one frame's time, not two rounds of
    # it. Measured Nov 21 on a 37 s clip of 12 frames: 12 s with 8 at a time, 7 s with all at once.
    with ThreadPoolExecutor(max_workers=len(stills)) as pool:
        per_frame = [r for r in pool.map(one, stills) if r]
    if not per_frame:
        raise RuntimeError("No frame of the video could be analysed")
    findings, counts = merge(per_frame)
    by_time = dict(stills)
    best_frame = dict(per_frame)
    for f in findings:
        if save_frames:
            photo_id = media.save_upload(by_time[f["time_s"]], "image/jpeg")
            f["frame"] = {"photo_id": photo_id, "url": f"/api/photos/{photo_id}", "time_s": f["time_s"]}
        f["photo_quality"] = best_frame[f["time_s"]].get("photo_quality")
    result = {
        "status": "ok",
        "media_type": "video",
        "video": {"duration_s": round(duration(path), 1), "frames_analysed": len(per_frame),
                  "frame_times_s": [t for t, _ in per_frame], "confirming_frames_needed": confirming_frames_needed(len(per_frame)),
                  "seen_in_frames": counts},
        "nothing_found": not findings,
        "building": bld,
        "building_error": bld_error,
        "findings": findings,
        "facts_from_description": said,
        "unclear": [],
        "out_of_scope": None,
        "timings": {"frames_s": round(time.perf_counter() - t0, 2)},
    }
    if with_explanation:
        pipeline.add_explanations(result)
    result["timings"]["total_s"] = round(time.perf_counter() - t0, 2)
    return result
