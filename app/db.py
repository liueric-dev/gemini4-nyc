"""Read-only lookups over the built database (var/tenant.db; build it with scripts/build_db.py).

The three calls the pipeline needs:
  candidate_rules(problem_type, facts, ...)  -> the rows of the decision matrix that still fit
  sections_for(rule_id)                      -> the law sections that rule points to, with full text
  steps_for(rule_id)                         -> the escalation steps that apply to that rule
"""
import json
import sqlite3
from pathlib import Path
from typing import Any

from app import config

OPS = {
    "lt": lambda a, b: a < b,
    "le": lambda a, b: a <= b,
    "gt": lambda a, b: a > b,
    "ge": lambda a, b: a >= b,
    "eq": lambda a, b: a == b,
    "in": lambda a, b: a in b,
}


# What each escalation step asks the tenant to do, in plain words. Codes are from data/problem-map/escalation.md.
STEP_ACTIONS = {
    "A1": "Tell your landlord in writing",
    "A2": "File a 311 complaint so HPD inspects",
    "A3": "HPD inspects and issues a violation",
    "A4": "HPD's Emergency Repair Program makes the repair",
    "A5": "Challenge a false certification that it was fixed",
    "A6": "Start an HP action in Housing Court",
    "A7": "Join with neighbours for a 7-A proceeding",
    "A8": "File a DHCR complaint (rent-regulated apartments)",
    "B1": "Keep proof that you notified the landlord",
    "B2": "Keep your 311 number and the inspection result",
    "B3": "Gather evidence for court",
    "B4": "Know the rule on recording conversations",
    "B5": "Know why the violation record matters later",
    "C1": "Raise the warranty of habitability in court",
    "C2": "Ask DHCR for a rent reduction (rent-regulated apartments)",
    "C3": "Rent-impairing violations",
    "C4": "Ask the court for a 7-A administrator",
    "C5": "Spiegel law, for tenants on public assistance",
    "C6": "Deduct a utility bill you had to pay",
    "C7": "Section 8 payment abatement",
}


def connect(path: Path | None = None) -> sqlite3.Connection:
    p = path or config.DB_PATH
    if not p.exists():
        raise FileNotFoundError(f"{p} not found. Build it with: uv run python scripts/build_db.py")
    db = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    return db


def problem_types(db: sqlite3.Connection, core_only: bool = False) -> list[dict]:
    q = "SELECT * FROM problem_types" + (" WHERE is_core = 1" if core_only else "") + " ORDER BY is_core DESC, id"
    return [dict(r) for r in db.execute(q)]


def fact_defs(db: sqlite3.Connection) -> dict[str, dict]:
    return {r["name"]: dict(r) for r in db.execute("SELECT * FROM facts")}


def _check(alternative: list, facts: dict[str, Any]) -> tuple[str, list[str]]:
    """One AND-list of clauses. Returns ('fail' | 'pass' | 'unknown', missing fact names)."""
    missing: list[str] = []
    for fact, op, value in alternative:
        if facts.get(fact) is None:
            missing.append(fact)
        elif not OPS[op](facts[fact], value):
            return "fail", []
    return ("unknown" if missing else "pass"), missing


def candidate_rules(
    db: sqlite3.Connection,
    problem_type: str,
    facts: dict[str, Any] | None = None,
    building_kind: str | None = None,
    location: str | None = None,
) -> list[dict]:
    """Rows of the decision matrix that the known facts don't rule out, best matches first.

    Each row gets:
      match: 'matched'  every testable condition holds
             'possible' nothing contradicts it, but some facts are still unknown (see missing_facts)
      missing_facts: the facts to get next, from the photo, the building lookup or a question
      needs_judgement: the row has a condition code can't test (see judgement)
    Rows a known fact contradicts are left out. building_kind is one of multiple_dwelling,
    one_two_family, nycha, section_8, condo; location is 'dwelling unit' or 'common area'.
    """
    facts = facts or {}
    out = []
    for r in db.execute("SELECT * FROM rules WHERE problem_type = ? ORDER BY id", (problem_type,)):
        row = dict(r)
        if building_kind and row["building_kind"] not in ("any", building_kind):
            continue
        loc = row["location"]
        if location and {loc, location} == {"dwelling unit", "common area"}:
            continue
        results = [_check(alt, facts) for alt in json.loads(row["conditions"])]
        if all(state == "fail" for state, _ in results):
            continue
        passed = any(state == "pass" for state, _ in results)
        missing = [] if passed else sorted({m for state, ms in results if state == "unknown" for m in ms})
        row["conditions"] = json.loads(row["conditions"])
        row["match"] = "matched" if passed else "possible"
        row["missing_facts"] = missing
        row["needs_judgement"] = bool(row["judgement"])
        row["specificity"] = max((len(alt) for alt in row["conditions"]), default=0)
        out.append(row)
    out.sort(key=lambda x: (x["match"] != "matched", -x["specificity"], x["id"]))
    return out


def get_rule(db: sqlite3.Connection, rule_id: str) -> dict | None:
    r = db.execute("SELECT * FROM rules WHERE id = ?", (rule_id,)).fetchone()
    return dict(r) if r else None


def rules_for_type(db: sqlite3.Connection, problem_type: str) -> list[dict]:
    """Every row of the decision matrix for one problem type, for answering a general question about it."""
    return [dict(r) for r in db.execute("SELECT * FROM rules WHERE problem_type = ? ORDER BY id", (problem_type,))]


def get_section(db: sqlite3.Connection, section_id: str) -> dict | None:
    r = db.execute("SELECT * FROM sections WHERE id = ?", (section_id,)).fetchone()
    return dict(r) if r else None


def sections_for(db: sqlite3.Connection, rule_id: str, official_only: bool = True) -> list[dict]:
    """The law sections a rule points to, with their full text and the subsection it names."""
    q = """SELECT s.*, rs.subsection FROM rule_sources rs JOIN sections s ON s.id = rs.source_id
           WHERE rs.rule_id = ? AND rs.kind = 'law'"""
    if official_only:
        q += " AND s.source_type = 'official'"
    return [dict(r) for r in db.execute(q + " ORDER BY s.id", (rule_id,))]


def steps_for(db: sqlite3.Connection, rule_id: str) -> list[dict]:
    """The escalation steps that apply to a rule, in order."""
    q = """SELECT e.* FROM rule_steps rs JOIN escalation_steps e ON e.code = rs.code
           WHERE rs.rule_id = ? ORDER BY e.code"""
    rows = [dict(r) for r in db.execute(q, (rule_id,))]
    for r in rows:
        d = r["detail"] = json.loads(r["detail"])
        # The source tables are laid out for reading, with "who" in the first column. Give each step a plain
        # action title and named fields, so a screen or an agent doesn't have to guess what a code means.
        r["action"] = STEP_ACTIONS.get(r["code"], r["summary"])
        r["who"] = d.get("Who") or d.get("Who qualifies")
        r["how"] = d.get("Form or letter") or d.get("How") or d.get("What") or d.get("When")
        r["when"] = d.get("Timeline")
    return rows


def general_steps(db: sqlite3.Connection, path: str = "A") -> list[dict]:
    """Every step of one path (A is 'get it fixed'), for questions asked before a photo has been checked."""
    rows = [dict(r) for r in db.execute("SELECT * FROM escalation_steps WHERE path = ? ORDER BY code", (path,))]
    for r in rows:
        d = r["detail"] = json.loads(r["detail"])
        r["action"] = STEP_ACTIONS.get(r["code"], r["summary"])
        r["who"] = d.get("Who") or d.get("Who qualifies")
        r["how"] = d.get("Form or letter") or d.get("How") or d.get("What") or d.get("When")
        r["when"] = d.get("Timeline")
    return rows


def hpd_order(db: sqlite3.Connection, order_number: str) -> dict | None:
    r = db.execute("SELECT * FROM hpd_orders WHERE order_number = ?", (str(order_number),)).fetchone()
    return dict(r) if r else None
