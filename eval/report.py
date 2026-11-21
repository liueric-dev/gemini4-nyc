"""Copy the test run into eval/results/ (committed) and list every photo either side got wrong.

    uv run python eval/report.py

Reads the cached per-photo outputs of `eval/run.py --set test`; makes no model calls.
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import config
from eval.run import baseline_bin, baseline_labels, load_test, system_bin, system_labels

SRC = config.VAR / "eval"
OUT = config.ROOT / "eval" / "results"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copy(SRC / "test-results.json", OUT / "test-results.json")
    items, _ = load_test()
    sys_dir = SRC / "test" / f"system-{config.MODEL_DESCRIBE}-{config.PROPOSE_VERSION}"
    rows = []
    for it in items:
        s = json.loads((sys_dir / f"{it['id']}.json").read_text())["result"]
        b = json.loads((SRC / "test" / "baseline" / f"{it['id']}.json").read_text())["result"]
        sl, bl = system_labels(s), baseline_labels(b)
        rows.append({
            "id": it["id"], "category": it["category"], "answer": it["key"],
            "system": sl, "system_right": sl == it["key"],
            "baseline": bl, "baseline_right": bl == it["key"],
            "proposed_by_model": s["proposed"],
            "probabilities": {k: round(v, 2) for k, v in s["probabilities"].items()},
            "mold_bin": {"reviewer": it["mold_bin"], "system": system_bin(s), "baseline": baseline_bin(b)} if it["mold_bin"] else None,
            "baseline_citations": [{"problem": p["problem_type"], "law": p["law_citation"], "class": p["violation_class"],
                                    "deadline": p["landlord_deadline"]} for p in b.get("problems", [])],
        })
    (OUT / "test-items.json").write_text(json.dumps(rows, indent=1))
    both = sum(r["system_right"] and r["baseline_right"] for r in rows)
    only_s = sum(r["system_right"] and not r["baseline_right"] for r in rows)
    only_b = sum(r["baseline_right"] and not r["system_right"] for r in rows)
    neither = sum(not r["system_right"] and not r["baseline_right"] for r in rows)
    print(f"{len(rows)} photos: both right {both}, only system {only_s}, only baseline {only_b}, neither {neither}")
    print(f"wrote {OUT / 'test-results.json'} and {OUT / 'test-items.json'}")


if __name__ == "__main__":
    main()
