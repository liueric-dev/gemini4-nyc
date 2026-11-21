"""Write docs/decision-matrix.md from data/problem-map/expected-outcomes.csv.

Run from the repo root:  uv run python scripts/render_decision_matrix.py
The CSV is the source of truth (and is frozen for scoring); this only reformats it for reading.
"""
import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data/problem-map/expected-outcomes.csv"
OUT = ROOT / "docs/decision-matrix.md"

TITLES = {
    "mold": "Mould",
    "peeling-paint": "Peeling paint (and lead)",
    "pests": "Pests",
    "window": "Windows and window guards",
    "heat-hot-water": "Heat and hot water",
    "smoke-co-detector": "Smoke and carbon monoxide detectors",
    "leak": "Leaks",
    "wall-ceiling-damage": "Wall and ceiling damage",
}
CORE = list(TITLES)
STATUS = {
    "settled": "Settled",
    "class-from-data": "From HPD's records",
    "class-unsettled": "Class not settled",
    "unsettled": "Not settled",
}


def status_label(s: str) -> str:
    return "Settled" if s.startswith("settled") else STATUS.get(s, s)


def cell(s: str) -> str:
    s = re.sub(r"\s*\[[^\]]*\]", "", s or "")  # drop the [source-id] references
    s = s.replace("_", " ").replace("|", "/").replace("<=", "≤ ").replace(">=", "≥ ").strip()
    return s or "—"


rows = list(csv.DictReader(line for line in SRC.open() if not line.startswith("#")))
types = CORE + sorted({r["problem_type"] for r in rows} - set(CORE))
out = [
    "# The decision matrix",
    "",
    ("For each problem the app recognises: the situations it can be in, the facts that tell them apart, "
    "and what the law says happens in each. This page is generated from "
    "`data/problem-map/expected-outcomes.csv` by `scripts/render_decision_matrix.py`; don't edit it by hand."),
    "",
    ("**This is a draft.** It was assembled overnight from the law text and HPD's records. "
    "Nobody with legal training has reviewed it."),
    "",
    "## How to read it",
    "",
    "- **Situation:** what the tenant has.",
    ("- **Deciding facts:** what the app needs to know to land on this row. Some come from the photo, "
    "some from the building lookup, some from a question to the tenant."),
    "- **Class:** how serious HPD treats it. A is non-hazardous, B is hazardous, C is immediately hazardous.",
    ("- **Landlord's deadline:** how long the landlord has to fix it. The clock starts when HPD issues "
    "a violation notice after an inspection, not when the tenant reports it."),
    "- **How sure:**",
    "  - *Settled*: the law states the class and deadline.",
    "  - *From HPD's records*: the law doesn't state the class, but HPD has consistently issued this class.",
    ("  - *Class not settled*: it is a violation, but HPD issues it in more than one class and the rule "
    "for choosing isn't published. The inspector decides."),
    "  - *Not settled*: we couldn't establish the outcome from the sources collected.",
    "",
    ("Default deadlines by class: A 90 days, B 30 days, C 24 hours. "
    "Some problems have their own: 21 days for Class C mould, pests, lead paint and window guards; "
    "no grace period at all for heat and hot water."),
    "",
    "## At a glance",
    "",
    "| Problem | Situations | Settled or from HPD's records | Main deciding facts |",
    "|---|---|---|---|",
]
FACTS = {
    "mold": "Area in square feet; where it is; whether an earlier violation went unfixed",
    "peeling-paint": "Year the building was built; whether a child under 6 lives there",
    "pests": "Which pest",
    "window": "Whether a child aged 10 or under lives there; type of window",
    "heat-hot-water": "Indoor, outdoor and water temperature; time of day; time of year",
    "smoke-co-detector": "Which device; why it is missing or not working",
    "leak": "Whether water is cascading; where it comes from",
    "wall-ceiling-damage": "Collapse or structural damage, against hairline cracks",
}
for t in CORE:
    rs = [r for r in rows if r["problem_type"] == t]
    ok = sum(1 for r in rs if status_label(r["status"]) in ("Settled", "From HPD's records"))
    out.append(f"| {TITLES[t]} | {len(rs)} | {ok} | {FACTS[t]} |")
out += ["", "The other 11 problem types (wiring, plumbing, doors and so on) are at the end.", ""]

for i, t in enumerate(types):
    if i == len(CORE):
        out += ["## Other problem types", ""]
    rs = [r for r in rows if r["problem_type"] == t]
    head = "##" if t in TITLES else "###"
    out += [
        f"{head} {TITLES.get(t, t.replace('-', ' ').capitalize())}",
        "",
        "| # | Situation | Building | Deciding facts | Violation? | Class | Landlord's deadline | How sure |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rs:
        out.append(
            "| " + " | ".join(
                [
                    r["row_id"],
                    cell(r["scenario"]),
                    cell(r["building"]),
                    cell(r["facts"]),
                    cell(r["expected_violation"]),
                    cell(r["expected_class"]),
                    cell(r["correction_deadline"]),
                    status_label(r["status"]),
                ]
            ) + " |"
        )
    notes = [(r["row_id"], cell(r["notes"])) for r in rs if r["notes"].strip()]
    if notes:
        out += ["", "Notes:"] + [f"- **{rid}:** {n}" for rid, n in notes]
    out.append("")

OUT.write_text("\n".join(out))
print(f"wrote {OUT.relative_to(ROOT)}: {len(rows)} rows, {len(types)} problem types")
print(Counter(status_label(r["status"]) for r in rows))
