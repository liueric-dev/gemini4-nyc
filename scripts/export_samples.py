"""Copy the test photos that may be redistributed into data/media/samples/, with credits.

    uv run python scripts/export_samples.py

Rule, not a hand pick: every reviewed test photo whose manifest says `committable: yes` and whose licence
was checked against its source and matched. Plus a few small videos chosen the same way, for trying video
upload. The full media set stays out of the repo (size, and licences that don't allow redistribution).
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import config

MEDIA = config.DATA / "media"
OUT = MEDIA / "samples"
VIDEOS = ["med-0420", "med-0418", "med-0422", "med-0421", "med-0621"]  # small, verified, one per kind of content


def ok(m: dict) -> bool:
    c = m.get("license_check")
    return m.get("committable") == "yes" and isinstance(c, dict) and c.get("result") == "match"


def main() -> None:
    man = {o["id"]: o for o in (json.loads(x) for x in (MEDIA / "manifest.jsonl").open(encoding="utf-8") if x.strip())}
    review = json.loads((MEDIA / "review/review_set.json").read_text())["items"]
    decisions = json.loads((MEDIA / "review/decisions.json").read_text())
    add = json.loads((MEDIA / "review/freeze-addendum.json").read_text())
    out = {k for k, v in decisions.items() if v["verdict"] == "drop"} | set(add["drops"]) | set(add["pending_owner_decision"])
    ids = [it["id"] for it in review if it["media_type"] == "image" and it["id"] not in out and ok(man[it["id"]])]
    ids += [v for v in VIDEOS if ok(man[v])]
    OUT.mkdir(exist_ok=True)
    rows = []
    for i in ids:
        m = man[i]
        src = MEDIA / m["raw_file"]
        if not src.exists():
            continue
        shutil.copy2(src, OUT / src.name)
        rows.append(m)
    lines = ["# Sample media: credits", "",
             ("These files are in the repository so the app can be tried without the full media set. Each one's licence "
             "allows redistribution and was checked against its source. They are unmodified."), "",
             "| File | Credit and licence | Source |", "|---|---|---|"]
    for m in rows:
        lines.append(f"| `{Path(m['raw_file']).name}` | {str(m.get('attribution') or m.get('license')).replace('|', '/')} | {m.get('source_url')} |")
    (OUT / "CREDITS.md").write_text("\n".join(lines) + "\n")
    size = sum((OUT / Path(m["raw_file"]).name).stat().st_size for m in rows)
    print(f"{len(rows)} files, {size / 1e6:.1f} MB, in {OUT}")


if __name__ == "__main__":
    main()
