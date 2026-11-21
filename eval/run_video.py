"""Score video: the system (by frames) and the single-call baseline (the whole clip given to the model).

    uv run python eval/run_video.py --set dev --limit 20     # practice clips
    uv run python eval/run_video.py --set test               # the reviewed test clips; run once

Per scoring-rules.md rule 8: detection is scored as for photos, a timestamp is correct if it falls inside
the reviewer's range widened by 3 seconds each side, and video is reported separately from photos.
"""
import argparse
import ast
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import config, pipeline, video
from eval.run import BASELINE_PROMPT, CORE, MEDIA, REVIEW, _core, _manifest, pct, run_all, score_detection


def _ranges(locations) -> list[tuple[float, float]]:
    if isinstance(locations, str):
        try:
            locations = ast.literal_eval(locations)
        except (ValueError, SyntaxError):
            return []
    out = []
    for loc in locations or []:
        if isinstance(loc, dict) and "start_s" in loc and "end_s" in loc:
            out.append((float(loc["start_s"]), float(loc["end_s"])))
    return out


def load(which: str, limit: int | None) -> tuple[list[dict], dict]:
    man = _manifest()
    items, skipped = [], {}
    if which == "test":
        review = json.loads((REVIEW / "review_set.json").read_text())["items"]
        decisions = json.loads((REVIEW / "decisions.json").read_text())
        add = json.loads((REVIEW / "freeze-addendum.json").read_text())
        out = {k for k, v in decisions.items() if v["verdict"] == "drop"} | set(add["drops"]) | set(add["pending_owner_decision"])
        for it in review:
            if it["media_type"] != "video" or it["id"] in out:
                continue
            labels = it["draft_label"] if decisions[it["id"]]["verdict"] == "right" else add["label_codes"].get(it["id"], {}).get("codes")
            if labels is None:
                continue
            items.append({"id": it["id"], "file": MEDIA / man[it["id"]]["raw_file"], "key": _core(labels),
                          "category": it["category"], "ranges": _ranges(it.get("problem_locations")), "mold_bin": None})
        skipped = {"dropped_or_pending": sorted(i["id"] for i in review if i["media_type"] == "video" and i["id"] in out)}
    else:
        for o in man.values():
            f = MEDIA / str(o.get("raw_file"))
            if (o.get("split") != "dev" or o.get("media_type") != "video" or o.get("license") == "copyrighted"
                    or f.suffix.lower() not in video.VIDEO_TYPES or not f.exists()):
                continue
            labels = o["draft_label"] if isinstance(o["draft_label"], list) else [o["draft_label"]]
            if o.get("category") == "problem" and not _core(labels):
                continue
            items.append({"id": o["id"], "file": f, "key": _core(labels), "category": o.get("category"),
                          "ranges": _ranges(o.get("problem_locations")), "mold_bin": None})
        items.sort(key=lambda x: x["id"])
        if limit:
            items = items[:: max(1, len(items) // limit)][:limit]
    return items, skipped


def system_predict(item: dict) -> dict:
    stills = video.frames(item["file"])

    def one(still):
        t, data = still
        with ThreadPoolExecutor(max_workers=2) as pool:
            det, prop = pool.submit(pipeline.detect, data, "image/jpeg"), pool.submit(pipeline.propose, data, "image/jpeg")
            det, prop = det.result(), prop.result()
        return {"t": t, "probabilities": det["probabilities"], "proposed": [f["problem_type"] for f in prop["findings"]]}

    with ThreadPoolExecutor(max_workers=4) as pool:
        return {"frames": list(pool.map(one, stills))}


def system_labels(res: dict, need: int | None = None) -> tuple[list[str], dict[str, float]]:
    """Problems confirmed in enough frames, and for each the time of its clearest frame."""
    frames = res["frames"]
    need = need or video.confirming_frames_needed(len(frames))
    hits: dict[str, list[tuple[float, float]]] = {}
    for f in frames:
        for t in pipeline.confirmed_types(f["proposed"], f["probabilities"]):
            hits.setdefault(t, []).append((f["probabilities"][t], f["t"]))
    kept = {t: max(h)[1] for t, h in hits.items() if len(h) >= need}
    return sorted(kept), kept


VIDEO_SCHEMA = {
    "type": "object",
    "properties": {"problems": {"type": "array", "items": {
        "type": "object",
        "properties": {"problem_type": {"type": "string", "enum": [*CORE, "other"]},
                       "time_s": {"type": "number"}, "law_citation": {"type": "string"},
                       "violation_class": {"type": "string", "enum": ["A", "B", "C", "unknown"]}},
        "required": ["problem_type", "time_s", "law_citation", "violation_class"]}}},
    "required": ["problems"],
}


def baseline_predict(item: dict) -> dict:
    c = pipeline.client()
    f = c.files.upload(file=str(item["file"]))
    for _ in range(90):
        if str(f.state).endswith("ACTIVE"):
            break
        if str(f.state).endswith("FAILED"):
            raise RuntimeError("file processing failed")
        time.sleep(2)
        f = c.files.get(name=f.name)
    prompt = BASELINE_PROMPT.replace("This is a photo", "This is a video").replace("does it show", "does it show at any point") \
        .replace(" Also say how large any visible mould is.", " For each, give the time in seconds where it is clearest.")
    return pipeline._generate_json(config.MODEL_BASELINE, [f, prompt], VIDEO_SCHEMA, "LOW")


def score_times(items: list[dict], times: dict[str, dict[str, float]]) -> list[int]:
    """For correctly detected problems in clips with a reviewed range: is the reported time inside it (±3 s)?"""
    right = total = 0
    for it in items:
        for t, when in (times.get(it["id"]) or {}).items():
            if t in it["key"] and it["ranges"]:
                total += 1
                right += any(a - 3 <= when <= b + 3 for a, b in it["ranges"])
    return [right, total]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", choices=["dev", "test"], required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only", choices=["system", "baseline"])
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    items, skipped = load(args.set, args.limit)
    root = config.VAR / "eval" / f"{args.set}-video"
    report: dict = {"set": f"{args.set}-video", "items": len(items), "skipped": skipped,
                    "run_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "video_settings": pipeline.THRESHOLDS["video"]}
    print(f"{args.set} video: {len(items)} clips", skipped or "")
    if args.only != "baseline":
        res = run_all(items, "system", system_predict, root / f"system-{config.MODEL_DESCRIBE}-{config.PROPOSE_VERSION}", args.workers)
        ok = {i: r["result"] for i, r in res.items() if r["ok"]}
        labelled = {i: system_labels(r) for i, r in ok.items()}
        report["system"] = {
            "detection": score_detection(items, {i: v[0] for i, v in labelled.items()}),
            "timestamps": score_times(items, {i: v[1] for i, v in labelled.items()}),
            "any_one_frame_variant": score_detection(items, {i: system_labels(r, need=1)[0] for i, r in ok.items()}),
            "errors": {i: r["error"] for i, r in res.items() if not r["ok"]}}
    if args.only != "system":
        res = run_all(items, "baseline", baseline_predict, root / "baseline", args.workers)
        ok = {i: r["result"] for i, r in res.items() if r["ok"]}
        report["baseline"] = {
            "detection": score_detection(items, {i: sorted({p["problem_type"] for p in r["problems"] if p["problem_type"] in CORE}) for i, r in ok.items()}),
            "timestamps": score_times(items, {i: {p["problem_type"]: p["time_s"] for p in r["problems"]} for i, r in ok.items()}),
            "errors": {i: r["error"] for i, r in res.items() if not r["ok"]}}
    out = config.VAR / "eval" / f"{args.set}-video-results.json"
    out.write_text(json.dumps(report, indent=1))
    for name in ("system", "baseline"):
        if name in report:
            d = report[name]["detection"]
            print(f"\n== {name} ({d['items_scored']} scored, {d['calls_failed']} failed)")
            print(f"   exact match {pct(d['exact_match'])} | found {pct(d['recall'])} | reports right {pct(d['precision'])}")
            print("   false alarms: " + ", ".join(f"{k} {pct(v)}" for k, v in d["false_alarms"].items()))
            print(f"   time inside the reviewer's range: {pct(report[name]['timestamps'])}")
            if "any_one_frame_variant" in report[name]:
                v = report[name]["any_one_frame_variant"]
                print(f"   (if one confirming frame were enough: exact {pct(v['exact_match'])}, found {pct(v['recall'])}, "
                      f"false alarms {', '.join(f'{k} {pct(x)}' for k, x in v['false_alarms'].items())})")
            if report[name]["errors"]:
                print("   errors:", list(report[name]["errors"].items())[:3])
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
