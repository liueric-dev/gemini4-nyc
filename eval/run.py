"""Score the system and the single-call baseline on the dev photos or the frozen test set.

    uv run python eval/run.py --set dev --limit 80          # while building; uses dev-split photos only
    uv run python eval/run.py --set test                     # the frozen test set; run once, at the end
    options: --only system|baseline   --law (also score citations on correct detections)   --workers N

Follows data/media/review/scoring-rules.md. The answer key for the test set is decisions.json with
freeze-addendum.json applied on top; neither file is ever written to. Each item's raw result is cached
under var/eval/ so an interrupted run resumes, and every failed call is counted and reported.
"""
import argparse
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from google.genai import types

from app import config, pipeline
from app import db as dbm

MEDIA = config.DATA / "media"
REVIEW = MEDIA / "review"
CORE = list(pipeline.DEFINITIONS)
BIN_ORDER = ["A", "B", "C"]
SYSTEM_BIN = {"under_10_sqft": "A", "10_to_under_30_sqft": "B", "30_sqft_or_more": "C"}
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


# ---------------------------------------------------------------- items and answer keys

def _manifest() -> dict[str, dict]:
    return {o["id"]: o for o in (json.loads(x) for x in (MEDIA / "manifest.jsonl").open(encoding="utf-8") if x.strip())}


def _core(labels) -> list[str]:
    labels = labels if isinstance(labels, list) else [labels]
    return sorted(x for x in labels if x in CORE)


def load_test() -> tuple[list[dict], dict]:
    man = _manifest()
    review = json.loads((REVIEW / "review_set.json").read_text())["items"]
    decisions = json.loads((REVIEW / "decisions.json").read_text())
    add = json.loads((REVIEW / "freeze-addendum.json").read_text())
    dropped = {k for k, v in decisions.items() if v["verdict"] == "drop"} | set(add["drops"])
    pending = set(add["pending_owner_decision"])
    items, skipped = [], {"dropped": len(dropped), "pending": sorted(pending), "videos_not_attempted": 0, "unmapped": []}
    for it in review:
        i = it["id"]
        if i in dropped or i in pending:
            continue
        if it["media_type"] != "image":
            skipped["videos_not_attempted"] += 1
            continue
        d = decisions[i]
        if d["verdict"] == "right":
            labels = it["draft_label"]
        elif i in add["label_codes"]:
            labels = add["label_codes"][i]["codes"]
        else:
            skipped["unmapped"].append(i)
            continue
        items.append({"id": i, "file": MEDIA / man[i]["raw_file"], "key": _core(labels), "category": it["category"],
                      "mold_bin": d.get("mold_bin")})
    return items, skipped


def load_dev(limit: int | None) -> tuple[list[dict], dict]:
    """Dev-split public photos. Their labels are unreviewed drafts, so dev numbers guide building only."""
    items = []
    for o in _manifest().values():
        f = MEDIA / str(o.get("raw_file"))
        if (o.get("split") != "dev" or o.get("media_type") != "image" or o.get("license") == "copyrighted"
                or "fallback" in str(o.get("raw_file")) or f.suffix.lower() not in MIME or not f.exists()):
            continue
        labels = o["draft_label"] if isinstance(o["draft_label"], list) else [o["draft_label"]]
        if o.get("category") == "problem" and not _core(labels):
            continue  # a problem outside the eight core types; not scored
        items.append({"id": o["id"], "file": f, "key": _core(labels), "category": o.get("category"), "mold_bin": None})
    items.sort(key=lambda x: x["id"])
    if limit:
        step = max(1, len(items) // limit)  # an even spread across the id range, fixed for a given limit
        items = items[::step][:limit]
    return items, {}


# ---------------------------------------------------------------- the two predictors

def system_predict(item: dict) -> dict:
    data, mime = item["file"].read_bytes(), MIME[item["file"].suffix.lower()]
    with ThreadPoolExecutor(max_workers=2) as pool:
        det, prop = pool.submit(pipeline.detect, data, mime), pool.submit(pipeline.propose, data, mime)
        det, prop = det.result(), prop.result()
    return {"probabilities": det["probabilities"], "answers": det["answers"],
            "proposed": [f["problem_type"] for f in prop["findings"]]}


BASELINE_SCHEMA = {
    "type": "object",
    "properties": {
        "problems": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "problem_type": {"type": "string", "enum": [*CORE, "other"]},
                    "law_citation": {"type": "string"},
                    "violation_class": {"type": "string", "enum": ["A", "B", "C", "unknown"]},
                    "landlord_deadline": {"type": "string"},
                },
                "required": ["problem_type", "law_citation", "violation_class", "landlord_deadline"],
            },
        },
        "mold_size": {"type": "string", "enum": ["no_mould", "under_10_sqft", "10_to_under_30_sqft", "30_sqft_or_more",
                                                 "tile_grout_only", "cannot_tell"]},
    },
    "required": ["problems", "mold_size"],
}
BASELINE_PROMPT = (
    "This is a photo from a rented apartment in New York City. What housing violations does it show? For each one, "
    "give the problem type, the law it breaks, the HPD violation class, and the landlord's deadline to fix it. "
    "If it shows no violation, return an empty list. Problem types: "
    + "; ".join(f"{t} ({d})" for t, d in pipeline.DEFINITIONS.items())
    + ". Also say how large any visible mould is."
)


def baseline_predict(item: dict) -> dict:
    data = item["file"].read_bytes()
    part = types.Part.from_bytes(data=data, mime_type=MIME[item["file"].suffix.lower()])
    return pipeline._generate_json(config.MODEL_BASELINE, [part, BASELINE_PROMPT], BASELINE_SCHEMA, "LOW")


def run_all(items: list[dict], name: str, fn, out_dir: Path, workers: int) -> dict[str, dict]:
    out_dir.mkdir(parents=True, exist_ok=True)

    def one(item):
        cache = out_dir / f"{item['id']}.json"
        if cache.exists():
            return item["id"], json.loads(cache.read_text())
        t = time.perf_counter()
        try:
            res = {"ok": True, "result": fn(item)}
        except Exception as e:  # noqa: BLE001 - every failed call is recorded and reported, never hidden
            res = {"ok": False, "error": f"{type(e).__name__}: {str(e)[:300]}"}
        res["seconds"] = round(time.perf_counter() - t, 2)
        if res["ok"]:
            cache.write_text(json.dumps(res))
        return item["id"], res

    results, done = {}, 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for i, res in pool.map(one, items):
            results[i] = res
            done += 1
            if done % 20 == 0 or done == len(items):
                print(f"  {name}: {done}/{len(items)}", flush=True)
    return results


# ---------------------------------------------------------------- scoring

def system_labels(res: dict) -> list[str]:
    return sorted(pipeline.confirmed_types(res["proposed"], res["probabilities"]))


def detector_only_labels(res: dict) -> list[str]:
    """The first design, kept so the report can show what changed: the Decisions API alone."""
    return sorted(pipeline.detected_types(res["probabilities"]))


def system_bin(res: dict) -> str:
    a, cut = res["answers"], pipeline.THRESHOLDS["fact"]
    tile = (a.get("f_mold_tile_only") or {}).get("noul", 0)
    if tile >= max(cut, 0.5):
        return "tile-grout"
    size = a.get("f_mold_size") or {}
    return SYSTEM_BIN.get(size.get("choice"), "cant-tell") if size.get("confidence", 0) >= cut else "cant-tell"


def baseline_labels(res: dict) -> list[str]:
    return sorted({p["problem_type"] for p in res.get("problems", []) if p["problem_type"] in CORE})


def baseline_bin(res: dict) -> str:
    m = res.get("mold_size")
    return "tile-grout" if m == "tile_grout_only" else SYSTEM_BIN.get(m, "cant-tell")


def score_detection(items: list[dict], preds: dict[str, list[str] | None]) -> dict:
    per = {t: {"tp": 0, "fp": 0, "fn": 0} for t in CORE}
    exact = scored = failed = 0
    alarms = {"no-problem": [0, 0], "look-alike": [0, 0]}
    for it in items:
        p = preds.get(it["id"])
        if p is None:
            failed += 1
            continue
        scored += 1
        key = set(it["key"])
        exact += set(p) == key
        for t in CORE:
            per[t]["tp"] += t in p and t in key
            per[t]["fp"] += t in p and t not in key
            per[t]["fn"] += t not in p and t in key
        if it["category"] in alarms:
            alarms[it["category"]][1] += 1
            alarms[it["category"]][0] += bool(p)
    tp, fp, fn = (sum(v[k] for v in per.values()) for k in ("tp", "fp", "fn"))
    return {
        "items_scored": scored, "calls_failed": failed,
        "exact_match": [exact, scored],
        "precision": [tp, tp + fp], "recall": [tp, tp + fn],
        "false_alarms": {k: v for k, v in alarms.items()},
        "per_type": {t: {"found": [v["tp"], v["tp"] + v["fn"]], "false_reports": v["fp"]} for t, v in per.items()},
    }


def score_mold(items: list[dict], bins: dict[str, str | None]) -> dict:
    table: dict[str, dict[str, int]] = {}
    exact = within = judged = abst_when_cant = cant = abst_when_judged = 0
    for it in items:
        ref, got = it["mold_bin"], bins.get(it["id"])
        if not ref or got is None:
            continue
        ref = {"cant-tell": "cant-tell", "tile-grout": "tile-grout"}.get(ref, ref)
        table.setdefault(ref, {}).setdefault(got, 0)
        table[ref][got] += 1
        if ref == "cant-tell":
            cant += 1
            abst_when_cant += got == "cant-tell"
        else:
            judged += 1
            abst_when_judged += got == "cant-tell"
            exact += got == ref
            within += got == ref or (got in BIN_ORDER and ref in BIN_ORDER
                                     and abs(BIN_ORDER.index(got) - BIN_ORDER.index(ref)) <= 1)
    return {"reviewer_bin_by_system_bin": table, "exact_agreement": [exact, judged], "within_one_bin": [within, judged],
            "abstained_when_reviewer_could_not_tell": [abst_when_cant, cant],
            "abstained_when_reviewer_judged": [abst_when_judged, judged]}


def resolve_citation(text: str, section_ids: set[str]) -> str | None:
    """Map a citation as written ('Admin Code § 27-2017.3(b)') to a section id in our law base, if it exists."""
    t = text.lower()
    m = re.search(r"27-(\d{4})(?:\.(\d+))?", t)
    if m:
        sid = f"nyc-hmc-27-{m.group(1)}" + (f"-{m.group(2)}" if m.group(2) else "")
        return sid if sid in section_ids else None
    for law, prefix in (("multiple dwelling law", "st-mdl-"), ("mdl", "st-mdl-"), ("real property law", "st-rpl-"),
                        ("rpl", "st-rpl-"), ("rpapl", "st-rpapl-")):
        m = re.search(law + r"[^0-9]{0,12}(\d+(?:-[a-z])?)", t)
        if m:
            sid = prefix + m.group(1)
            return sid if sid in section_ids else None
    return None


def score_baseline_citations(items: list[dict], results: dict[str, dict]) -> dict:
    """For problems the baseline detected correctly: is the cited law real, and is it law for that problem type?"""
    conn = dbm.connect()
    section_ids = {r[0] for r in conn.execute("SELECT id FROM sections")}
    by_type = {t: {r[0] for r in conn.execute(
        "SELECT rs.source_id FROM rule_sources rs JOIN rules r ON r.id = rs.rule_id WHERE r.problem_type = ? AND rs.kind = 'law'", (t,))}
        for t in CORE}
    conn.close()
    total = real = right = 0
    for it in items:
        res = results.get(it["id"])
        if not res or not res["ok"]:
            continue
        for p in res["result"].get("problems", []):
            if p["problem_type"] not in it["key"]:
                continue
            total += 1
            sid = resolve_citation(p["law_citation"], section_ids)
            real += sid is not None
            right += sid is not None and sid in by_type[p["problem_type"]]
    return {"correct_detections_with_a_citation": total, "citation_is_a_real_section": [real, total],
            "citation_is_law_for_that_problem": [right, total]}


def pct(pair) -> str:
    return f"{pair[0]}/{pair[1]}" + (f" ({100 * pair[0] / pair[1]:.0f}%)" if pair[1] else "")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", choices=["dev", "test"], required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only", choices=["system", "baseline"])
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    items, skipped = load_test() if args.set == "test" else load_dev(args.limit)
    root = config.VAR / "eval" / args.set
    report: dict = {"set": args.set, "items": len(items), "skipped": skipped,
                    "run_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                    "thresholds": pipeline.THRESHOLDS,
                    "models": {"detect": config.MODEL_DECIDE, "baseline": config.MODEL_BASELINE}}
    print(f"{args.set}: {len(items)} photos", skipped or "")

    if args.only != "baseline":
        res = run_all(items, "system", system_predict, root / f"system-{config.MODEL_DESCRIBE}-{config.PROPOSE_VERSION}", args.workers)
        ok = {i: r["result"] for i, r in res.items() if r["ok"]}
        report["detector_only_v1"] = {"detection": score_detection(items, {i: detector_only_labels(r) for i, r in ok.items()})}
        report["system"] = {
            "detection": score_detection(items, {i: system_labels(r) for i, r in ok.items()}),
            "mold": score_mold(items, {i: system_bin(r) for i, r in ok.items()}),
            "errors": {i: r["error"] for i, r in res.items() if not r["ok"]},
            "median_seconds": sorted(r["seconds"] for r in res.values())[len(res) // 2] if res else None,
        }
    if args.only != "system":
        res = run_all(items, "baseline", baseline_predict, root / "baseline", args.workers)
        ok = {i: r["result"] for i, r in res.items() if r["ok"]}
        report["baseline"] = {
            "detection": score_detection(items, {i: baseline_labels(r) for i, r in ok.items()}),
            "mold": score_mold(items, {i: baseline_bin(r) for i, r in ok.items()}),
            "citations": score_baseline_citations(items, res),
            "errors": {i: r["error"] for i, r in res.items() if not r["ok"]},
            "median_seconds": sorted(r["seconds"] for r in res.values())[len(res) // 2] if res else None,
        }

    out = config.VAR / "eval" / f"{args.set}-results.json"
    out.write_text(json.dumps(report, indent=1))
    for name in ("system", "baseline"):
        if name not in report:
            continue
        d = report[name]["detection"]
        print(f"\n== {name}  ({d['items_scored']} scored, {d['calls_failed']} failed calls, median {report[name]['median_seconds']} s)")
        print(f"   exact match {pct(d['exact_match'])} | found {pct(d['recall'])} of real problems | "
              f"{pct(d['precision'])} of reports were right")
        print("   false alarms: " + ", ".join(f"{k} {pct(v)}" for k, v in d["false_alarms"].items()))
        print("   per type (found, false reports): " + "; ".join(
            f"{t} {v['found'][0]}/{v['found'][1]}, {v['false_reports']}" for t, v in d["per_type"].items()))
        m = report[name]["mold"]
        if m["exact_agreement"][1] or m["abstained_when_reviewer_could_not_tell"][1]:
            print(f"   mould size: exact {pct(m['exact_agreement'])}, within one bin {pct(m['within_one_bin'])}, "
                  f"abstained when reviewer couldn't tell {pct(m['abstained_when_reviewer_could_not_tell'])}, "
                  f"abstained when reviewer judged {pct(m['abstained_when_reviewer_judged'])}")
        if "citations" in report[name]:
            c = report[name]["citations"]
            print(f"   citations on correct detections: real section {pct(c['citation_is_a_real_section'])}, "
                  f"law for that problem {pct(c['citation_is_law_for_that_problem'])}")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
