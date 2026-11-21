"""Video support by frames: sample still frames, run the photo pipeline on each, and merge.

    analyze_video(path, address=None, answers=None) -> dict   (same shape as pipeline.analyze, plus timestamps)

A problem is reported only if it is confirmed in at least `min_confirming_frames` frames (one frame for a
very short clip), which keeps a single odd frame from raising a false alarm. Each reported problem carries
the times it was seen and the clearest frame, saved as a still so it can be shown and used as evidence.
Sound is ignored. Needs ffmpeg on the machine.
"""
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from app import building as building_mod
from app import media, pipeline

VIDEO_TYPES = {".mp4": "video/mp4", ".mov": "video/quicktime", ".webm": "video/webm", ".m4v": "video/x-m4v"}


def duration(path: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, timeout=30, check=False).stdout.strip()
    return float(out or 0)


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
                  with_explanation: bool = True, save_frames: bool = True) -> dict:
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

    def one(item):
        t, data = item
        return t, pipeline.analyze(data, "image/jpeg", answers=answers, with_explanation=False, building=bld)

    # Every frame at once (there are at most `max_frames`), so the wait is one frame's time, not two rounds of
    # it. Measured Nov 21 on a 37 s clip of 12 frames: 12 s with 8 at a time, 7 s with all at once.
    with ThreadPoolExecutor(max_workers=len(stills)) as pool:
        per_frame = list(pool.map(one, stills))
    findings, seen = merge(per_frame)
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
                  "seen_in_frames": seen},
        "nothing_found": not findings,
        "building": bld,
        "building_error": bld_error,
        "findings": findings,
        "unclear": [],
        "out_of_scope": None,
        "timings": {"frames_s": round(time.perf_counter() - t0, 2)},
    }
    if with_explanation:
        pipeline.add_explanations(result)
    result["timings"]["total_s"] = round(time.perf_counter() - t0, 2)
    return result
