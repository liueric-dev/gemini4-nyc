"""Build the app's SQLite file from data/.

Run from the repo root:  uv run python scripts/build_db.py
Output: var/tenant.db (git-ignored). It is a build output: safe to delete and rebuild at any time.
Nothing under data/ is modified. Runtime data (building lookups, case records) goes in a separate file.
"""
import csv
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import config

PM = config.DATA / "problem-map"
CORE = {
    "mold": "Mould",
    "peeling-paint": "Peeling paint and lead",
    "pests": "Pests",
    "window": "Windows and window guards",
    "heat-hot-water": "Heat and hot water",
    "smoke-co-detector": "Smoke and carbon monoxide detectors",
    "leak": "Leaks",
    "wall-ceiling-damage": "Wall and ceiling damage",
}
BUILDING = {
    "multiple dwelling (3+ units)": "multiple_dwelling",
    "one- or two-family house, tenant-occupied unit": "one_two_family",
    "NYCHA": "nycha",
    "any": "any",
    "Section 8 (private building)": "section_8",
    "condo unit in a multiple dwelling": "condo",
}

SCHEMA = """
CREATE TABLE sections (
  id TEXT PRIMARY KEY, workstream TEXT, citation TEXT, title TEXT, text TEXT, chars INTEGER,
  source_url TEXT, effective_date TEXT, source_type TEXT, version TEXT, retrieved TEXT, in_repo INTEGER);
CREATE TABLE problem_types (id TEXT PRIMARY KEY, title TEXT, is_core INTEGER, rule_count INTEGER);
CREATE TABLE facts (name TEXT PRIMARY KEY, type TEXT, source TEXT, question TEXT, allowed_values TEXT);
CREATE TABLE rules (
  id TEXT PRIMARY KEY, problem_type TEXT REFERENCES problem_types(id), scenario TEXT,
  building_kind TEXT, location TEXT,
  violation TEXT, violation_text TEXT,
  class TEXT, class_options TEXT, class_text TEXT, class_basis TEXT,
  deadline_value INTEGER, deadline_unit TEXT, deadline_text TEXT, deadline_basis TEXT,
  hpd_orders TEXT, certainty TEXT, notes TEXT, facts_text TEXT,
  conditions TEXT, judgement TEXT);
CREATE TABLE rule_sources (
  rule_id TEXT REFERENCES rules(id), source_id TEXT, subsection TEXT, kind TEXT,
  PRIMARY KEY (rule_id, source_id));
CREATE TABLE escalation_steps (code TEXT PRIMARY KEY, path TEXT, path_title TEXT, summary TEXT, detail TEXT);
CREATE TABLE rule_steps (rule_id TEXT REFERENCES rules(id), code TEXT, PRIMARY KEY (rule_id, code));
CREATE TABLE hpd_orders (
  order_number TEXT PRIMARY KEY, description TEXT, category TEXT, cited_section TEXT, total INTEGER,
  class_a INTEGER, class_b INTEGER, class_c INTEGER, class_i INTEGER, most_common_class TEXT, most_common_share REAL);
CREATE TABLE build_info (key TEXT PRIMARY KEY, value TEXT);
CREATE INDEX rules_by_type ON rules(problem_type);
"""


def strip_refs(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s or "")
    s = re.sub(r"\s*\[[^\]]*\]", "", s)
    return re.sub(r"\s+([.,;:])", r"\1", s).strip(" ;")


def load_sections(db: sqlite3.Connection) -> int:
    n = 0
    for ws in ("law-nyc", "law-state"):
        for line in (config.DATA / ws / "manifest.jsonl").open(encoding="utf-8"):
            if not line.strip():
                continue
            o = json.loads(line)
            tf = o.get("text_file")
            path = config.DATA / ws / tf if isinstance(tf, str) and tf else None
            if not path or not path.exists():
                continue  # local-only files are absent from a fresh clone of the repo
            text = path.read_text(encoding="utf-8", errors="replace")
            db.execute(
                "INSERT INTO sections VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (o["id"], ws, o.get("citation"), o.get("title"), text, len(text), o.get("source_url"),
                 o.get("effective_date"), o.get("source_type"), o.get("version"), o.get("retrieved"),
                 0 if "local/" in tf else 1),
            )
            n += 1
    return n


def parse_class(text: str) -> tuple[str | None, str | None]:
    t = text.strip()
    m = re.match(r"^([ABC])(?: \(|$)", t)
    if m:
        return m.group(1), None
    m = re.match(r"^unsettled \(([^)]*)", t)
    if m:
        opts = re.findall(r"\b([ABC])\b", m.group(1))
        return None, ",".join(opts) or None
    return None, None


def parse_deadline(text: str) -> tuple[int | None, str | None]:
    t = text.strip()
    if t.startswith("none"):
        return 0, "none"
    m = re.match(r"^(\d+) (days|hours)\b", t)
    if m and "if" not in t.split(";")[0]:
        return int(m.group(1)), m.group(2)
    return None, None


def parse_violation(text: str) -> str:
    t = text.strip().lower()
    if t == "yes":
        return "yes"
    if t.startswith("no"):
        return "no"
    if t.startswith("unsettled"):
        return "unsettled"
    return "conditional"


def certainty(status: str) -> str:
    return "settled" if status.startswith("settled") else status


def step_codes(text: str) -> list[str]:
    codes: list[str] = []
    for m in re.finditer(r"\b([A-F])(\d)(?:-\1?(\d))?\b", text):
        lo, hi = int(m.group(2)), int(m.group(3) or m.group(2))
        codes += [f"{m.group(1)}{i}" for i in range(lo, hi + 1)]
    return sorted(set(codes))


def load_rules(db: sqlite3.Connection, section_ids: set[str]) -> int:
    cond = json.loads((config.ROOT / "app/rule_conditions.json").read_text())
    for name, f in cond["facts"].items():
        db.execute("INSERT INTO facts VALUES (?,?,?,?,?)",
                   (name, f["type"], f["source"], f["ask"], json.dumps(f.get("values")) if f.get("values") else None))
    rows = list(csv.DictReader(ln for ln in (PM / "expected-outcomes.csv").open(encoding="utf-8")
                               if not ln.startswith("#")))
    unknown = set(cond["rows"]) - {r["row_id"] for r in rows}
    if unknown:
        raise SystemExit(f"rule_conditions.json names rows that aren't in the CSV: {sorted(unknown)}")
    types: dict[str, int] = {}
    for r in rows:
        types[r["problem_type"]] = types.get(r["problem_type"], 0) + 1
    for t, n in types.items():
        db.execute("INSERT INTO problem_types VALUES (?,?,?,?)",
                   (t, CORE.get(t, t.replace("-", " ").capitalize()), int(t in CORE), n))
    for r in rows:
        klass, options = parse_class(r["expected_class"])
        dval, dunit = parse_deadline(r["correction_deadline"])
        c = cond["rows"].get(r["row_id"], {})
        db.execute(
            "INSERT INTO rules VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (r["row_id"], r["problem_type"], strip_refs(r["scenario"]),
             BUILDING.get(r["building"].strip(), "other"), r["location"].strip(),
             parse_violation(r["expected_violation"]), strip_refs(r["expected_violation"]),
             klass, options, strip_refs(r["expected_class"]), r["class_basis"],
             dval, dunit, strip_refs(r["correction_deadline"]), r["deadline_basis"],
             strip_refs(r["hpd_orders"]), certainty(r["status"]), strip_refs(r["notes"]), r["facts"],
             json.dumps(c.get("when", [[]])), c.get("judgement")),
        )
        for src in r["sources"].split(";"):
            src = src.strip()
            if not src:
                continue
            sid, _, sub = src.partition(" ")
            kind = "law" if sid in section_ids else ("open-data" if sid.startswith("od-") else "process")
            db.execute("INSERT OR IGNORE INTO rule_sources VALUES (?,?,?,?)", (r["row_id"], sid, sub or None, kind))
        for code in step_codes(r["escalation"]):
            db.execute("INSERT OR IGNORE INTO rule_steps VALUES (?,?)", (r["row_id"], code))
    return len(rows)


def load_escalation(db: sqlite3.Connection) -> int:
    lines = (PM / "escalation.md").read_text(encoding="utf-8").splitlines()
    path = title = None
    n, i = 0, 0
    while i < len(lines):
        m = re.match(r"^### ([A-F])\. (.+)$", lines[i])
        if m:
            path, title = m.group(1), m.group(2)
        elif lines[i].startswith("## Part 2"):
            path = None
        elif path and lines[i].startswith("|"):
            table = []
            while i < len(lines) and lines[i].startswith("|"):
                table.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            header = table[0]
            for row in table[2:]:
                cm = re.match(rf"^({path}\d)\b\s*(.*)$", row[0])
                if not cm:
                    continue
                detail = {h: strip_refs(v) for h, v in zip(header[1:], row[1:]) if h.lower() != "source"}
                summary = strip_refs(cm.group(2)) or next(iter(detail.values()), "")
                db.execute("INSERT OR REPLACE INTO escalation_steps VALUES (?,?,?,?,?)",
                           (cm.group(1), path, title, summary, json.dumps(detail)))
                n += 1
            continue
        i += 1
    return n


def load_hpd_orders(db: sqlite3.Connection) -> int:
    n = 0
    with (config.DATA / "open-data/text/od-hpd-order-class-map.csv").open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            db.execute(
                "INSERT INTO hpd_orders VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (r["ordernumber"], r["dict_short_description"], r["dict_category"], r["cited_section"],
                 int(r["total_excluding_upgraded"] or 0), int(r["class_A"] or 0), int(r["class_B"] or 0),
                 int(r["class_C"] or 0), int(r["class_I"] or 0), r["most_common_class"],
                 float(r["most_common_share"] or 0)),
            )
            n += 1
    return n


def build(out: Path) -> dict[str, int]:
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp")
    tmp.unlink(missing_ok=True)
    db = sqlite3.connect(tmp)
    db.executescript(SCHEMA)
    counts = {"sections": load_sections(db)}
    section_ids = {row[0] for row in db.execute("SELECT id FROM sections")}
    counts["rules"] = load_rules(db, section_ids)
    counts["escalation_steps"] = load_escalation(db)
    counts["hpd_orders"] = load_hpd_orders(db)
    for k, v in counts.items():
        db.execute("INSERT INTO build_info VALUES (?,?)", (k, str(v)))
    db.commit()
    db.close()
    tmp.replace(out)
    return counts


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else config.DB_PATH
    print(f"built {target}: {build(target)}")
