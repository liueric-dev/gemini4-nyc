"""Drafts for the tenant: a letter to the landlord and the text of a 311 complaint.

Both are filled in by code from an /api/analyze response. No model writes them, so every legal statement
is one the pipeline already produced: the class and deadline from the decision matrix, and quotes that
were checked against the cited section. The tenant reviews and sends them; the app never sends anything.
"""
from datetime import date

from app import db as dbm

REPORTABLE = ("violation", "inspector_decides", "not_settled")
RETALIATION = "st-rpl-223-b"


def _class_sentence(f: dict) -> str:
    d = (f.get("deadline") or {}).get("text")
    if f["outcome"] == "violation" and f.get("class"):
        s = f"HPD classifies this as a Class {f['class']} ({(f.get('class_meaning') or '').lower()}) violation."
        if (f.get("deadline") or {}).get("unit") == "none":
            return s + " The law gives no grace period to correct it."
        return s + (f" Once HPD issues a notice of violation, the owner has {d.split(' from ')[0].split(' after ')[0]} to correct it." if d else "")
    if f["outcome"] == "inspector_decides":
        o = f.get("class_options") or []
        opts = o[0] if len(o) == 1 else ", ".join(o[:-1]) + " or " + o[-1] if o else ""
        return f"HPD treats this as a violation. Its inspector assigns the class ({opts}), which sets the time to correct it."
    return ""


def draft(analysis: dict, tenant_name: str | None = None, apartment: str | None = None) -> dict:
    findings = [f for f in analysis.get("findings", []) if f.get("outcome") in REPORTABLE]
    if not findings:
        raise ValueError("There is nothing to put in a letter: no finding is a condition the landlord must repair.")
    b = analysis.get("building") or {}
    address = b.get("address") or "[building address]"
    owner = b.get("owner") or "[Landlord or managing agent]"
    apt = apartment or "[apartment number]"
    name = tenant_name or "[Your name]"
    today = date.today().strftime("%B %-d, %Y")

    conn = dbm.connect()
    try:
        protected = any(RETALIATION in [s["id"] for s in dbm.sections_for(conn, f["rule_id"])]
                        for f in findings if f.get("rule_id"))
    finally:
        conn.close()

    items = []
    for i, f in enumerate(findings, 1):
        lines = [f"{i}. {f['title']}. {f.get('description') or ''}".rstrip()]
        if f.get("where"):
            lines.append(f"   Location: {f['where']}.".replace("..", "."))
        for c in f.get("citations", [])[:2]:
            if c["section_id"] != RETALIATION:
                lines.append(f"   {c['citation']} says: \"{c['quote']}\"")
        cs = _class_sentence(f)
        if cs:
            lines.append(f"   {cs}")
        items.append("\n".join(lines))

    plural = len(findings) > 1
    letter = "\n\n".join([
        today,
        f"To: {owner}\nRe: {'Conditions' if plural else 'A condition'} needing repair at {address}, Apartment {apt}",
        f"Dear {owner},",
        (f"I am the tenant of the apartment above. I am writing to tell you about the following "
        f"{'conditions' if plural else 'condition'} and to ask that you repair {'them' if plural else 'it'}."),
        "\n\n".join(items),
        "Please contact me to arrange access for the repair. I am available [days and times].",
        ("If this is not repaired, I may file a complaint with 311, which refers it to the Department of Housing "
        "Preservation and Development (HPD) for inspection."),
        *(["State law protects tenants from retaliation for making a complaint like this one (Real Property Law § 223-b)."]
          if protected else []),
        "I am keeping a copy of this letter and proof that it was delivered.",
        f"Sincerely,\n{name}\nApartment {apt}, {address}",
    ])
    complaint = "\n".join(
        f"{f['title']} in apartment {apt} at {address}. {f.get('description') or ''} {('Location: ' + f['where'] + '.') if f.get('where') else ''}".strip()
        for f in findings)
    return {
        "letter": letter,
        "complaint_311": complaint,
        "notes": [
            "This is a draft. Check every detail and fill in the parts in square brackets before you send it.",
            "Send the letter in a way that gives you proof of delivery, such as certified mail, and keep a copy.",
            "For 311, call 311 or use the 311 website or app, and keep the service request number.",
        ],
        "findings_included": [f["problem_type"] for f in findings],
    }
