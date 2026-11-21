"""The case file agent: a Managed Agents run that builds a tenant's case file from HPD's public record.

    case = build_case(analysis, apartment="4B")     # from an /api/analyze result that has a building
    case_id = start(case)                           # starts the agent in Google's hosted sandbox
    status(case_id)                                 # {'status': 'in_progress' | 'completed' | ..., 'markdown': ...}

The sandbox gets three small files: the case, a script that reads NYC Open Data (no key needed), and the
skill in agent/SKILL.md. No API key or token is sent into the sandbox. The agent drafts; it never sends.
Cases and results are kept in var/runtime.db.
"""
import json
import sqlite3
import time
import uuid
from datetime import date

from app import config, pipeline
from app import db as dbm

AGENT = "antigravity-preview-09-2026"
AGENT_DIR = config.ROOT / "agent"
RUNTIME_DB = config.VAR / "runtime.db"
PROMPT = (
    "Build the tenant's case file. Follow the case-file skill (also saved at case/SKILL.md). "
    "The case is in case/case.json and the record script is case/hpd_record.py. "
    "Reply with the Markdown case file only."
)


def _db() -> sqlite3.Connection:
    config.VAR.mkdir(exist_ok=True)
    db = sqlite3.connect(RUNTIME_DB)
    db.execute("""CREATE TABLE IF NOT EXISTS cases (
        id TEXT PRIMARY KEY, created REAL, bbl TEXT, case_json TEXT, interaction_id TEXT,
        status TEXT, markdown TEXT, usage TEXT, finished REAL)""")
    return db


def build_case(analysis: dict, apartment: str | None = None) -> dict:
    """Turn an analyze() result into the small case record the agent works from."""
    b = analysis.get("building")
    if not b:
        raise ValueError("A case file needs a building. Run the analysis with an address.")
    conn = dbm.connect()
    try:
        steps = {r["code"]: dict(r) for r in conn.execute("SELECT code, path_title, summary, detail FROM escalation_steps")}
    finally:
        conn.close()
    findings, next_steps = [], {}
    for f in analysis.get("findings", []):
        findings.append({
            "problem": f["title"], "what_the_photo_shows": f.get("description"), "where": f.get("where"),
            "outcome": f["outcome"], "class": f.get("class"), "class_options": f.get("class_options"),
            "landlord_deadline": (f.get("deadline") or {}).get("text"),
            "hpd_orders": f.get("hpd_order"), "how_settled": f.get("certainty"),
            "citations": [{"citation": c["citation"], "quote": c["quote"]} for c in f.get("citations", [])],
        })
        for s in f.get("next_steps", []):
            next_steps[s["code"]] = {"code": s["code"], "path": s["path"], "step": s["title"], "detail": s["detail"]}
    b3 = steps.get("B3")
    return {
        "prepared_on": date.today().isoformat(),
        "building": {k: b.get(k) for k in ("address", "bbl", "year_built", "units_res", "building_kind", "rent_stabilized")},
        "apartment": apartment,
        "findings": findings,
        "next_steps": [next_steps[k] for k in sorted(next_steps)],
        "court_evidence": b3["summary"] if b3 else None,
    }


def start(case: dict) -> str:
    sources = [
        {"type": "inline", "target": "case/case.json", "content": json.dumps(case, indent=1)},
        {"type": "inline", "target": "case/hpd_record.py", "content": (AGENT_DIR / "hpd_record.py").read_text()},
        {"type": "inline", "target": "case/SKILL.md", "content": (AGENT_DIR / "SKILL.md").read_text()},
        {"type": "inline", "target": ".agents/skills/case-file/SKILL.md", "content": (AGENT_DIR / "SKILL.md").read_text()},
    ]
    r = pipeline.client().interactions.create(
        agent=AGENT,
        agent_config={"type": "antigravity", "model": config.MODEL_AGENT},
        input=PROMPT,
        environment={"type": "remote", "sources": sources},
        background=True,
        store=True,
        api_version=config.DECISIONS_API_VERSION,
        timeout=60,
    )
    case_id = f"case-{uuid.uuid4().hex[:10]}"
    db = _db()
    try:
        db.execute("INSERT INTO cases VALUES (?,?,?,?,?,?,?,?,?)",
                   (case_id, time.time(), case["building"]["bbl"], json.dumps(case), r.id, str(r.status), None, None, None))
        db.commit()
    finally:
        db.close()
    return case_id


def status(case_id: str) -> dict | None:
    db = _db()
    try:
        row = db.execute("SELECT created, interaction_id, status, markdown, case_json, finished FROM cases WHERE id = ?",
                         (case_id,)).fetchone()
        if not row:
            return None
        created, interaction_id, state, markdown, case_json, finished = row
        if markdown is None and state not in ("failed", "cancelled"):
            r = pipeline.client().interactions.get(id=interaction_id, api_version=config.DECISIONS_API_VERSION)
            state = str(r.status)
            if state == "completed":
                markdown = getattr(r, "output_text", None) or ""
                usage = r.usage.model_dump() if getattr(r, "usage", None) else {}
                finished = time.time()
                db.execute("UPDATE cases SET status = ?, markdown = ?, usage = ?, finished = ? WHERE id = ?",
                           (state, markdown, json.dumps(usage), finished, case_id))
            else:
                db.execute("UPDATE cases SET status = ? WHERE id = ?", (state, case_id))
            db.commit()
        return {"case_id": case_id, "status": state, "markdown": markdown, "case": json.loads(case_json),
                "seconds": round((finished or time.time()) - created, 1)}
    finally:
        db.close()
