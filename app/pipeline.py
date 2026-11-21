"""The pipeline: a photo (and optionally an address and answers) to findings.

    analyze(image_bytes, mime_type, address=None, answers=None) -> dict   (shape: docs/sample-response.json)

Steps, each its own function so it can be replaced or scored alone:
  propose   Hydrogen        which of the eight problems the photo shows, with a description of each
  confirm   Decisions API   a probability per problem type; a proposal is kept only if it clears the cut-off.
                            The same request reads the photo facts the rules need (mould size, which pest...)
  facts     code            building lookup + the tenant's answers
  decide    code            pick the row of the decision matrix (app/db.py)
  explain   Carbon          plain-language explanation that quotes only the law text it was given
  check     code            drop any citation whose quote isn't in the cited section

The detection questions restate the problem definitions in data/README.md. The cut-offs are in
app/thresholds.json; they are untuned defaults until the evaluation's dev run sets them.
"""
import base64
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from zoneinfo import ZoneInfo

from google import genai
from google.genai import types

from app import building as building_mod
from app import config
from app import db as dbm

THRESHOLDS = json.loads((config.ROOT / "app/thresholds.json").read_text())

# One line per core problem type, from the labelling definitions in data/README.md.
DEFINITIONS = {
    "leak": "an active leak, water damage, or water stains on a ceiling or wall",
    "mold": "visible mould or mildew on walls, ceilings, windows or fixtures",
    "peeling-paint": "peeling, flaking or chipping paint",
    "wall-ceiling-damage": "holes, cracks, or broken or fallen plaster in a wall or ceiling",
    "pests": "roaches, mice, rats or bedbugs, or signs of them such as droppings, gnaw holes or nests",
    "smoke-co-detector": "a missing, broken, disconnected or painted-over smoke or carbon monoxide detector",
    "window": "a broken window, a window that won't close or lock, or a missing or broken window guard",
    "heat-hot-water": "a thermometer showing a low indoor temperature, or tap water that isn't hot",
}
MOLD_BINS = {"under_10_sqft": 5, "10_to_under_30_sqft": 15, "30_sqft_or_more": 35}
CLASS_MEANING = {"A": "Non-hazardous", "B": "Hazardous", "C": "Immediately hazardous"}
RETAKE_HINTS = {  # what a clearer photo of each problem needs
    "leak": "Take a closer photo of the stain or drip in good light, and one from further back showing where it is in the room.",
    "mold": "Take a closer photo in good light, with something of known size in the frame, such as a sheet of paper or a door.",
    "peeling-paint": "Take a closer photo of the paint in good light, at an angle that shows it lifting from the surface.",
    "wall-ceiling-damage": "Take one photo close to the damage and one from further back showing the whole wall or ceiling.",
    "pests": "Take a closer, sharper photo of the pest or the droppings, with something of known size beside them.",
    "smoke-co-detector": "Take a photo of the detector, or of the ceiling or wall where one should be, with the whole device in frame.",
    "window": "Take a photo of the whole window, and a closer one of the broken part or the missing guard.",
    "heat-hot-water": "Take a photo of a thermometer with the reading sharp enough to read.",
}
TENANT_DUTY_RULES = {"EO-015", "EO-047"}  # the problem map says these are the tenant's own responsibility
FACT_LABELS = {"mold_area_sqft": "Mould area (sq ft)", "building_kind": "Building type", "year_built": "Year built"}

_client: genai.Client | None = None


def client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=config.key("GEMINI_API_KEY"),
                               http_options=types.HttpOptions(timeout=config.MODEL_TIMEOUT_S * 1000))
    return _client


def _retry(fn, attempts: int = 4):
    """The venue network drops requests now and then, more so with many in flight (video frames).
    Retry with a growing pause: 0.5 s, 1 s, 2 s."""
    for i in range(attempts):
        try:
            return fn()
        except Exception:
            if i == attempts - 1:
                raise
            time.sleep(0.5 * 2**i)


# ---------------------------------------------------------------- detect (Decisions API)

def _detect_questions() -> dict:
    q: dict = {
        t: {
            "type": "noul",
            "instructions": f"Does this photo show {d}?",
            "criteria": {"true_description": "The problem itself is visible in the photo.",
                         "false_description": "The problem is not visible in the photo."},
        }
        for t, d in DEFINITIONS.items()
    }
    q["f_mold_size"] = {
        "type": "choice",
        "instructions": "If mould is visible, how large is the total area it covers?",
        "criteria": {
            "none": "No mould is visible",
            "under_10_sqft": "Less than 10 square feet",
            "10_to_under_30_sqft": "10 to under 30 square feet",
            "30_sqft_or_more": "30 square feet or more",
            "cannot_tell": "Mould is visible but the photo gives no way to judge its size",
        },
    }
    q["f_mold_tile_only"] = {
        "type": "noul",
        "instructions": "Is the mould only on the surface of tile, grout or caulk, and nowhere else?",
    }
    q["f_pest"] = {
        "type": "choice",
        "instructions": "Which pest, or sign of which pest, is visible?",
        "criteria": {"none": "No pest or sign of one", "roach": "Cockroaches", "mouse": "Mice",
                     "rat": "Rats", "bedbug": "Bedbugs", "other": "Another pest"},
    }
    q["f_device"] = {
        "type": "choice",
        "instructions": "Which kind of detector, or place where one should be, is shown?",
        "criteria": {"none": "No detector or detector mount is shown", "smoke": "A smoke detector",
                     "CO": "A carbon monoxide detector", "cannot_tell": "A detector, but the kind is unclear"},
    }
    q["f_wall"] = {
        "type": "choice",
        "instructions": "If a wall or ceiling is damaged, how severe is it?",
        "criteria": {"none": "No wall or ceiling damage", "hairline": "Only a hairline crack",
                     "collapse": "Part of the wall or ceiling has collapsed or is collapsing",
                     "structural": "The damage looks structural", "other": "Other damage, such as a hole or broken plaster"},
    }
    q["f_cascading"] = {
        "type": "noul",
        "instructions": "Is water actively cascading or soaking an electrical fixture?",
    }
    q["f_fire_escape"] = {"type": "noul", "instructions": "Does the window shown open onto a fire escape?"}
    return q


def detect(image: bytes, mime_type: str) -> dict:
    """One Decisions API request. Returns {'probabilities': {type: p}, 'answers': raw answers}."""
    r = _retry(lambda: client().decisions.create(
        model=config.MODEL_DECIDE,
        api_version=config.DECISIONS_API_VERSION,
        input=[{"type": "image", "data": base64.b64encode(image).decode(), "mime_type": mime_type}],
        questions=_detect_questions(),
        timeout=config.DECISIONS_TIMEOUT_S,
    ))
    answers = {k: v.model_dump() for k, v in (r.answers or {}).items()}
    return {"probabilities": {t: answers[t]["noul"] for t in DEFINITIONS if t in answers}, "answers": answers}


def detected_types(probabilities: dict[str, float]) -> list[str]:
    cut = THRESHOLDS["detect"]
    found = [t for t, p in probabilities.items() if p >= cut.get(t, cut["default"])]
    return sorted(found, key=lambda t: -probabilities[t])


def photo_facts(problem_type: str, answers: dict) -> dict[str, tuple]:
    """Facts read from the photo for one problem type: {fact: (value, confidence)}."""
    cut = THRESHOLDS["fact"]
    out: dict[str, tuple] = {}

    def choice(key):
        a = answers.get(key) or {}
        return (a.get("choice"), a.get("confidence", 0.0))

    def noul(key):
        a = answers.get(key) or {}
        p = a.get("noul")
        return (None, 0.0) if p is None else (p >= 0.5, max(p, 1 - p))

    if problem_type == "mold":
        c, p = choice("f_mold_size")
        if c in MOLD_BINS and p >= cut:
            out["mold_area_sqft"] = (MOLD_BINS[c], p)
        v, p = noul("f_mold_tile_only")
        if v is not None and p >= cut:
            out["mold_on_tile_grout_caulk_only"] = (v, p)
    elif problem_type == "pests":
        c, p = choice("f_pest")
        if c not in (None, "none") and p >= cut:
            out["pest"] = (c, p)
    elif problem_type == "smoke-co-detector":
        c, p = choice("f_device")
        if c in ("smoke", "CO") and p >= cut:
            out["device"] = (c, p)
    elif problem_type == "wall-ceiling-damage":
        c, p = choice("f_wall")
        if c in ("hairline", "collapse", "structural", "other") and p >= cut:
            for k in ("hairline", "collapse", "structural"):
                out[k] = (c == k, p)
    elif problem_type == "leak":
        v, p = noul("f_cascading")
        if v is not None and p >= cut:
            out["cascading"] = (v, p)
    elif problem_type == "window":
        v, p = noul("f_fire_escape")
        if v is not None and p >= cut:
            out["window_fire_escape_access"] = (v, p)
    return out


# ---------------------------------------------------------------- photo quality (Decisions API)

QUALITY_QUESTIONS = {
    "sharp_and_lit": ("Is the photo in focus and lit well enough that surface details are clearly visible?",
                      "It is blurry or too dark to show detail. Retake it in focus, with the light on or a flash."),
    "close_enough": ("Is the photo taken close enough that the condition of the surfaces can be seen clearly?",
                     "It is taken from too far away. Add a closer photo of the problem."),
    "shows_location": ("Does the photo show enough of the surroundings to tell where in the room it was taken?",
                       "It doesn't show where in the room this is. Add a photo from further back."),
    "has_scale_reference": (("Is there an object of known size in the photo, such as a door, a light switch, an outlet, "
                            "a sheet of paper, a ruler or a hand, that could be used to judge the size of things?"),
                            "Nothing in the photo shows scale. Put a sheet of paper or a ruler beside it and retake."),
}


def photo_quality(image: bytes, mime_type: str) -> dict[str, float]:
    """Is this photo good evidence? A separate Decisions API request, so it can't affect detection.

    The detection probability says whether a problem is present, not whether the picture is a good record
    of it: on dev photos, reports at 0.8 and above were right no more often than those below 0.6.
    """
    r = _retry(lambda: client().decisions.create(
        model=config.MODEL_DECIDE,
        api_version=config.DECISIONS_API_VERSION,
        input=[{"type": "image", "data": base64.b64encode(image).decode(), "mime_type": mime_type}],
        questions={k: {"type": "noul", "instructions": q} for k, (q, _) in QUALITY_QUESTIONS.items()},
        timeout=config.DECISIONS_TIMEOUT_S,
    ))
    return {k: v.model_dump()["noul"] for k, v in (r.answers or {}).items()}


def quality_report(scores: dict[str, float] | None, found: list[str]) -> dict | None:
    """Turn the quality scores into requests. Scale only matters where size sets the outcome (mould)."""
    if not scores or not found:
        return None
    cut = THRESHOLDS["quality"]
    checks = [k for k in QUALITY_QUESTIONS if k != "has_scale_reference" or "mold" in found]
    weak = [k for k in checks if scores.get(k, 1.0) < cut]
    return {"scores": {k: round(scores[k], 2) for k in checks if k in scores},
            "good_for_evidence": not weak,
            "retake_requests": [QUALITY_QUESTIONS[k][1] for k in weak]}


# ---------------------------------------------------------------- describe (Hydrogen)

DESCRIBE_SCHEMA = {
    "type": "object",
    "properties": {
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "problem_type": {"type": "string"},
                    "description": {"type": "string"},
                    "where": {"type": "string"},
                },
                "required": ["problem_type", "description", "where"],
            },
        },
        "other_condition": {
            "type": "object",
            "nullable": True,
            "properties": {
                "description": {"type": "string"},
                "tenant_responsibility": {"type": "boolean"},
            },
            "required": ["description", "tenant_responsibility"],
        },
    },
    "required": ["findings"],
}


def _generate_json(model: str, contents: list, schema: dict, level: str) -> dict:
    r = _retry(lambda: client().models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=schema,
            thinking_config=types.ThinkingConfig(thinking_level=level),
        ),
    ))
    return json.loads(r.text)


def propose(image: bytes, mime_type: str) -> dict:
    """Hydrogen looks at the photo and proposes which of the eight problems it shows, describing each.

    The Decisions API then has to confirm each proposal (see confirmed_types). The first version used
    the Decisions API alone and reported too many secondary problems; on 220 dev photos it matched the
    answer key on 64% against 79% for a single model call. Proposing with a model and confirming with
    the Decisions API matched the single call and halved false alarms on look-alike photos.
    """
    listed = "\n".join(f"- {t}: {d}" for t, d in DEFINITIONS.items())
    ask = (
        "This is a photo from a rented apartment. Which of these housing problems does it show?\n"
        f"{listed}\n\nList only the problems that are clearly visible; most photos show one or none. For each, "
        "write one or two plain sentences describing what is visible, and say where in the photo it is. Use the "
        "problem_type ids exactly as given. If the photo shows none of them, return an empty findings list; then, "
        "if it shows some other household problem, describe it in other_condition and say whether fixing it "
        "would ordinarily be the tenant's own responsibility (for example cleaning, a light bulb, or the "
        "tenant's own belongings). Otherwise leave other_condition null."
    )
    out = _generate_json(config.MODEL_DESCRIBE, [types.Part.from_bytes(data=image, mime_type=mime_type), ask],
                         DESCRIBE_SCHEMA, config.DESCRIBE_THINKING)
    out["findings"] = [f for f in out.get("findings", []) if f.get("problem_type") in DEFINITIONS]
    return out


def confirmed_types(proposed: list[str], probabilities: dict[str, float]) -> list[str]:
    """A problem is reported only if the model proposed it and the Decisions API's probability clears the cut-off."""
    cut = THRESHOLDS["confirm"]
    kept = {t for t in proposed if probabilities.get(t, 0.0) >= cut.get(t, cut["default"])}
    return sorted(kept, key=lambda t: -probabilities.get(t, 0.0))


# ---------------------------------------------------------------- decide (code)

def _signature(rule: dict) -> tuple:
    """What the tenant would be told. Two rows with the same signature aren't worth a question."""
    return (rule["violation"], rule["class"], rule["deadline_value"], rule["deadline_unit"])


ASKABLE = ("ask", "photo")  # facts a tenant can supply; records, weather and derived facts are looked up


def _outcome(rule: dict) -> str:
    if rule["violation"] == "no":
        return "not_landlord_responsibility" if rule["id"] in TENANT_DUTY_RULES else "no_violation"
    if rule["class"]:
        return "violation"
    if rule["class_options"]:
        return "inspector_decides"
    return "not_settled"


def decide(conn, problem_type: str, facts: dict, building_kind: str, location: str = "dwelling unit",
           fact_sources: dict[str, str] | None = None) -> dict:
    """Pick the row of the decision matrix, or say which questions would settle it.

    Returns {'rule': row | None, 'questions': [fact names], 'possible': [rows], 'tie': [rows]}.
    A question is asked only when its answer could change the outcome.
    """
    rows = dbm.candidate_rules(conn, problem_type, facts, building_kind, location)
    sources = fact_sources or {}
    matched = [r for r in rows if r["match"] == "matched"]
    # A row that hinges on a fact the tenant can't supply (such as an earlier violation on HPD's record)
    # stays out unless that fact was looked up.
    possible = [r for r in rows if r["match"] == "possible"
                and all(sources.get(f, "ask") in ASKABLE for f in r["missing_facts"])]
    rows = matched + possible
    specific = [r for r in matched if r["specificity"] > 0]
    if specific:
        return {"rule": specific[0], "questions": [], "possible": [], "tie": []}
    if not rows:
        return {"rule": None, "questions": [], "possible": [], "tie": []}
    if len({_signature(r) for r in rows}) == 1:
        return {"rule": (matched or possible)[0], "questions": [], "possible": [], "tie": []}
    if possible:
        counts: dict[str, int] = {}
        for r in possible:
            for f in r["missing_facts"]:
                counts[f] = counts.get(f, 0) + 1
        questions = sorted(counts, key=lambda f: (-counts[f], f))[: THRESHOLDS["max_questions"]]
        return {"rule": None, "questions": questions, "possible": possible + matched, "tie": []}
    return {"rule": matched[0], "questions": [], "possible": [], "tie": matched if len(matched) > 1 else []}


def pick_by_scenario(image: bytes, mime_type: str, rows: list[dict]) -> dict:
    """Several rows fit and code can't tell them apart: the Decisions API picks by scenario text."""
    r = client().decisions.create(
        model=config.MODEL_DECIDE,
        api_version=config.DECISIONS_API_VERSION,
        input=[{"type": "image", "data": base64.b64encode(image).decode(), "mime_type": mime_type}],
        questions={"row": {"type": "choice", "instructions": "Which description best fits what this photo shows?",
                           "criteria": {x["id"]: x["scenario"] for x in rows}}},
    )
    choice = r.answers["row"].model_dump()["choice"]
    return next((x for x in rows if x["id"] == choice), rows[0])


# ---------------------------------------------------------------- explain (Carbon) and check (code)

LONG_SECTION = 8000
PENALTY_SECTION_PARTS = {  # § 27-2115 is about 55,000 characters; pass only the parts a problem type needs
    "always": (r"^\(c\) ", r"^\(d\) "),
    "heat-hot-water": (r"^\(k\) \(1\)", r"^\(l\) \(1\)"),
    "peeling-paint": (r"^\(l\) \(1\)", r"^\(m\) \(1\)"),
}


def _between(text: str, start: str, end: str) -> str:
    s = re.search(start, text, re.MULTILINE)
    if not s:
        return ""
    e = re.search(end, text[s.start() + 1:], re.MULTILINE)
    return text[s.start(): s.start() + 1 + e.start()] if e else text[s.start(): s.start() + 6000]


def excerpt(section: dict, problem_type: str) -> str:
    text = section["text"]
    if len(text) <= LONG_SECTION:
        return text
    if section["id"] == "nyc-hmc-27-2115":
        parts = [_between(text, *PENALTY_SECTION_PARTS["always"])]
        if problem_type in PENALTY_SECTION_PARTS:
            parts.append(_between(text, *PENALTY_SECTION_PARTS[problem_type]))
        return "\n[...]\n".join(p for p in parts if p)
    return text[:LONG_SECTION] + "\n[...]"


def _norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def check_citations(citations: list[dict], sections: dict[str, dict]) -> tuple[list[dict], int]:
    """Keep a citation only if it names a section we supplied and its quote is in that section's text."""
    kept, dropped = [], 0
    for c in citations:
        s = sections.get(c.get("section_id"))
        quote = _norm(c.get("quote", "")).strip('". ')
        if s and len(quote) >= 20 and quote in _norm(s["text"]):
            kept.append({"section_id": s["id"], "citation": s["citation"], "quote": c["quote"].strip(),
                         "supports": c.get("supports", ""), "checked": True, "source_url": s["source_url"]})
        else:
            dropped += 1
    return kept, dropped


def explain(items: list[dict]) -> dict[str, dict]:
    """One Carbon call for every finding that has a rule. items: [{problem_type, description, rule, sections}]."""
    if not items:
        return {}
    blocks, ids = [], set()
    for it in items:
        r = it["rule"]
        law = "\n\n".join(f"<section id=\"{s['id']}\" citation=\"{s['citation']}\">\n{excerpt(s, it['problem_type'])}\n</section>"
                          for s in it["sections"])
        ids |= {s["id"] for s in it["sections"]}
        deadline = r["deadline_text"] or "not settled"
        blocks.append(
            f"<finding problem_type=\"{it['problem_type']}\">\nWhat the photo shows: {it['description']}\n"
            f"Situation: {r['scenario']}\nIs it a violation: {r['violation_text']}\n"
            f"Class: {r['class'] or r['class_text']}\nLandlord's deadline: {deadline}\n"
            f"Notes: {r['notes'] or 'none'}\n{law}\n</finding>"
        )
    schema = {
        "type": "object",
        "properties": {
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "problem_type": {"type": "string"},
                        "summary": {"type": "string"},
                        "landlord_duties": {"type": "string"},
                        "tenant_rights": {"type": "string"},
                        "tenant_responsibilities": {"type": "string"},
                        "citations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "section_id": {"type": "string", "enum": sorted(ids)},
                                    "quote": {"type": "string"},
                                    "supports": {"type": "string"},
                                },
                                "required": ["section_id", "quote", "supports"],
                            },
                        },
                    },
                    "required": ["problem_type", "summary", "landlord_duties", "tenant_rights",
                                 "tenant_responsibilities", "citations"],
                },
            }
        },
        "required": ["findings"],
    }
    prompt = (
        "You are helping a New York City tenant understand a housing problem. For each finding below, the "
        "situation, class and deadline have already been decided from the law; do not change them or add others.\n\n"
        "Write for a tenant, in plain language, two or three sentences per field:\n"
        "- summary: what this is and what it means for them\n"
        "- landlord_duties: what the landlord must do\n"
        "- tenant_rights: what the tenant is entitled to\n"
        "- tenant_responsibilities: what the tenant must do themselves, such as giving access for repairs\n"
        "- citations: one to three. Each quote must be copied word for word from one of the sections supplied "
        "for that finding, at least one full clause long, and section_id must be that section's id. In supports, "
        "say in a few words what the quote establishes.\n\n"
        "Use only the supplied sections. If they don't cover a point, leave it out. Don't cite anything else and "
        "don't give legal advice beyond what the sections say.\n\n" + "\n\n".join(blocks)
    )
    out = _generate_json(config.MODEL_EXPLAIN, [prompt], schema, config.EXPLAIN_THINKING)
    return {f["problem_type"]: f for f in out.get("findings", [])}


# ---------------------------------------------------------------- the whole thing

def _confidence(p: float) -> str:
    c = THRESHOLDS["confidence"]
    return "high" if p >= c["high"] else "medium" if p >= c["medium"] else "low"


def _now_facts() -> dict:
    now = datetime.now(ZoneInfo("America/New_York"))
    return {"hour": now.hour + now.minute / 60, "heat_season": now.month >= 10 or now.month <= 5}


def analyze(image: bytes, mime_type: str = "image/jpeg", address: str | None = None,
            answers: dict | None = None, with_explanation: bool = True, building: dict | None = None) -> dict:
    """building: facts already looked up (video analysis looks the address up once, not once per frame)."""
    t0 = time.perf_counter()
    timings: dict[str, float] = {}
    answers = answers or {}

    def timed(name, fn, *a):
        t = time.perf_counter()
        try:
            return fn(*a)
        finally:
            timings[name] = round(time.perf_counter() - t, 2)

    bld, bld_error = None, None
    with ThreadPoolExecutor(max_workers=4) as pool:  # detection, description, quality and building side by side
        f_qual = pool.submit(photo_quality, image, mime_type)
        f_det = pool.submit(timed, "detect_s", detect, image, mime_type)
        f_desc = pool.submit(timed, "describe_s", propose, image, mime_type)
        f_bld = pool.submit(timed, "building_s", building_mod.lookup, address) if address and not building else None
        det, desc = f_det.result(), f_desc.result()
        if f_bld:
            try:
                bld = f_bld.result()
            except building_mod.AddressNotFound:
                bld_error = f"No NYC address found for: {address}"
        try:
            quality = f_qual.result()
        except Exception:  # noqa: BLE001 - the quality note is optional; never fail an answer over it
            quality = None
    proposed = [f["problem_type"] for f in desc.get("findings", [])]
    found = confirmed_types(proposed, det["probabilities"])
    # Proposed by the model but not confirmed: not reported as a problem. The tenant is asked for a clearer photo.
    unclear = [{"problem_type": f["problem_type"], "probability": round(det["probabilities"].get(f["problem_type"], 0.0), 3),
                "what_was_seen": f.get("description", ""), "request": RETAKE_HINTS[f["problem_type"]]}
               for f in desc.get("findings", []) if f["problem_type"] not in found]

    descriptions = {f["problem_type"]: f for f in desc.get("findings", [])}
    bld = bld or building
    kind = (bld or {}).get("building_kind") or "multiple_dwelling"
    kind_source = "building" if (bld or {}).get("building_kind") else "assumed"
    conn = dbm.connect()
    defs = dbm.fact_defs(conn)
    findings, to_explain = [], []
    try:
        for t in found:
            from_photo = photo_facts(t, det["answers"])
            facts = {k: v for k, (v, _) in from_photo.items()}
            if bld and bld.get("year_built"):
                facts["year_built"] = bld["year_built"]
            if t == "heat-hot-water":
                facts.update(_now_facts())
            facts.update({k: v for k, v in answers.items() if k in defs})
            d = decide(conn, t, facts, kind, fact_sources={k: v["source"] for k, v in defs.items()})
            rule = d["rule"]
            if d["tie"]:
                rule = pick_by_scenario(image, mime_type, d["tie"])
            used = [{"name": k, "label": FACT_LABELS.get(k, k.replace("_", " ").capitalize()), "value": facts[k],
                     "source": "answer" if k in answers else "photo" if k in from_photo else defs.get(k, {}).get("source", "building"),
                     **({"confidence": round(from_photo[k][1], 2)} if k in from_photo and k not in answers else {})}
                    for k in facts if rule and any(k == c[0] for alt in rule["conditions"] for c in alt)]
            used.append({"name": "building_kind", "label": "Building type", "value": kind, "source": kind_source})
            p = det["probabilities"][t]
            f = {
                "problem_type": t,
                "title": dbm.problem_types(conn)[[x["id"] for x in dbm.problem_types(conn)].index(t)]["title"],
                "probability": round(p, 3),
                "confidence": _confidence(p),
                "description": descriptions.get(t, {}).get("description", ""),
                "where": descriptions.get(t, {}).get("where", ""),
                "facts_used": used,
                "questions": [{"fact": q, "question": defs[q]["question"], "type": defs[q]["type"],
                               "options": json.loads(defs[q]["allowed_values"]) if defs[q]["allowed_values"] else None}
                              for q in d["questions"]],
                "possible_outcomes": [
                    {"rule_id": r["id"], "scenario": r["scenario"], "class": r["class"], "class_options": r["class_options"],
                     "deadline_text": r["deadline_text"]} for r in d["possible"]],
                # when the missing fact is one a photo could settle (such as mould size), offer a retake as well
                "retake_request": RETAKE_HINTS[t] if any(defs[q]["source"] == "photo" for q in d["questions"]) else None,
                "citations": [], "explanation": None, "next_steps": [],
            }
            if rule:
                f.update({
                    "outcome": _outcome(rule), "rule_id": rule["id"], "scenario": rule["scenario"],
                    "class": rule["class"],
                    "class_options": rule["class_options"].split(",") if rule["class_options"] else None,
                    "class_meaning": CLASS_MEANING.get(rule["class"]),
                    "deadline": {"value": rule["deadline_value"], "unit": rule["deadline_unit"], "text": rule["deadline_text"],
                                 "starts": "When HPD issues a violation notice after inspecting"},
                    "certainty": rule["certainty"], "hpd_order": rule["hpd_orders"],
                    "needs_judgement": rule["judgement"],
                    "next_steps": [{"code": s["code"], "path": s["path_title"], "title": s["summary"], "detail": s["detail"]}
                                   for s in dbm.steps_for(conn, rule["id"])],
                })
                sections = dbm.sections_for(conn, rule["id"])
                to_explain.append({"problem_type": t, "description": f["description"] or DEFINITIONS[t],
                                   "rule": rule, "sections": sections, "finding": f})
            else:
                f.update({"outcome": "needs_answer" if d["questions"] else "not_settled", "rule_id": None})
            findings.append(f)
    finally:
        conn.close()

    timings["total_s"] = round(time.perf_counter() - t0, 2)
    result = {
        "status": "ok",
        "timings": timings,
        "nothing_found": not findings,
        "probabilities": {k: round(v, 3) for k, v in det["probabilities"].items()},
        "proposed": proposed,
        "unclear": unclear,
        "photo_quality": quality_report(quality, found),
        "building": bld,
        "building_error": bld_error,
        "findings": findings,
        "out_of_scope": desc.get("other_condition") if not findings else None,
    }
    if with_explanation:
        add_explanations(result)
        result["timings"]["total_s"] = round(time.perf_counter() - t0, 2)
    return result


def check_support(citations: list[dict]) -> list[float]:
    """Does each quote support the statement it is attached to? One Decisions API request for all of them.

    A quote can be real and still not support the claim; that is the failure legal research tools show most.
    Returns one probability per citation.
    """
    if not citations:
        return []
    text = "\n\n".join(f"Quote {i + 1} (from {c['citation']}): \"{c['quote']}\"" for i, c in enumerate(citations))
    r = _retry(lambda: client().decisions.create(
        model=config.MODEL_DECIDE,
        api_version=config.DECISIONS_API_VERSION,
        input=text,
        questions={f"q{i + 1}": {"type": "noul",
                                 "instructions": f"Does quote {i + 1} support this statement: {c['supports']}"}
                   for i, c in enumerate(citations)},
        timeout=config.DECISIONS_TIMEOUT_S,
    ))
    answers = {k: v.model_dump() for k, v in (r.answers or {}).items()}
    return [answers.get(f"q{i + 1}", {}).get("noul", 0.0) for i in range(len(citations))]


def add_explanations(result: dict) -> dict:
    """Fill in the explanation and citations for every finding that has a rule. Changes result in place.

    Split from analyze() so a screen can show the class and deadline first and fetch this part after.
    A citation is kept only if its quote is in the cited section (check_citations) and the Decisions API
    agrees the quote supports the statement (check_support).
    """
    t = time.perf_counter()
    conn = dbm.connect()
    try:
        items = []
        for f in result.get("findings", []):
            if f.get("rule_id") and not f.get("explanation"):
                items.append({"problem_type": f["problem_type"],
                              "description": f.get("description") or DEFINITIONS[f["problem_type"]],
                              "rule": dbm.get_rule(conn, f["rule_id"]),
                              "sections": dbm.sections_for(conn, f["rule_id"]), "finding": f})
    finally:
        conn.close()
    if not items:
        return result

    def one(it):
        w = explain([it]).get(it["problem_type"])
        if not w:
            return
        kept, dropped = check_citations(w.get("citations", []), {s["id"]: s for s in it["sections"]})
        try:
            support = check_support(kept)
        except Exception:  # noqa: BLE001 - if the support check itself fails, say so instead of dropping quotes
            support = [None] * len(kept)
        for c, p in zip(kept, support, strict=True):
            c["support"] = None if p is None else round(p, 2)
        cut = THRESHOLDS["support"]
        f = it["finding"]
        f["citations"] = [c for c in kept if c["support"] is None or c["support"] >= cut]
        f["citations_dropped"] = dropped
        f["citations_unsupported"] = len(kept) - len(f["citations"])
        f["explanation"] = {k: w.get(k, "") for k in ("summary", "landlord_duties", "tenant_rights", "tenant_responsibilities")}

    with ThreadPoolExecutor(max_workers=4) as pool:  # one finding per thread, side by side
        list(pool.map(one, items))
    result.setdefault("timings", {})["explain_s"] = round(time.perf_counter() - t, 2)
    return result
