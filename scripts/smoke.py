"""Smoke tests: one call to each Gemini service the app depends on.

Run from the repo root:
    uv run python scripts/smoke.py            # the three fast calls
    uv run python scripts/smoke.py --agent    # also one Managed Agents run (slower, costs more tokens)

Uses two dev-split photos only (never test items). Prints timings and writes var/smoke.json.
The questions here are placeholders to prove the calls work; they are not the app's tuned questions.
"""
import base64
import json
import sys
import time
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from google import genai
from google.genai import types

from app import config

warnings.simplefilter("ignore")

MOULD_PHOTO = config.DATA / "media/images/med-0157.jpg"  # dev split, draft label: mold
CLEAN_PHOTO = config.DATA / "media/images/med-0502.jpg"  # dev split, no problem
AGENT = "antigravity-preview-09-2026"

client = genai.Client(api_key=config.key("GEMINI_API_KEY"))
results: dict[str, dict] = {}


def run(name: str, fn) -> None:
    start = time.perf_counter()
    try:
        out = fn()
        results[name] = {"ok": True, "seconds": round(time.perf_counter() - start, 2), **out}
    except Exception as e:  # noqa: BLE001 - report every failure, don't stop at the first
        results[name] = {
            "ok": False,
            "seconds": round(time.perf_counter() - start, 2),
            "error": f"{type(e).__name__}: {str(e)[:600]}",
        }
    print(f"\n== {name}\n{json.dumps(results[name], indent=1)[:2500]}", flush=True)


def describe() -> dict:
    r = client.models.generate_content(
        model=config.MODEL_DESCRIBE,
        contents=[
            types.Part.from_bytes(data=MOULD_PHOTO.read_bytes(), mime_type="image/jpeg"),
            "In two sentences, describe any housing condition problem visible in this photo and where it is.",
        ],
    )
    return {"model": config.MODEL_DESCRIBE, "text": (r.text or "")[:500], "usage": _usage(r)}


def explain() -> dict:
    r = client.models.generate_content(
        model=config.MODEL_EXPLAIN,
        contents="Reply with exactly: ready",
    )
    return {"model": config.MODEL_EXPLAIN, "text": (r.text or "")[:200], "usage": _usage(r)}


def _usage(r) -> dict:
    u = getattr(r, "usage_metadata", None)
    if not u:
        return {}
    return {
        "input_tokens": getattr(u, "prompt_token_count", None),
        "output_tokens": getattr(u, "candidates_token_count", None),
        "thinking_tokens": getattr(u, "thoughts_token_count", None),
    }


def decide(photo: Path):
    def call() -> dict:
        r = client.decisions.create(
            model=config.MODEL_DECIDE,
            api_version=config.DECISIONS_API_VERSION,
            input=[
                {
                    "type": "image",
                    "data": base64.b64encode(photo.read_bytes()).decode(),
                    "mime_type": "image/jpeg",
                }
            ],
            questions={
                "mold": {"type": "noul", "instructions": "Is mould growth visible on a surface in this photo?"},
                "leak": {
                    "type": "noul",
                    "instructions": "Is there a water leak or water damage visible in this photo?",
                },
                "mold_size": {
                    "type": "choice",
                    "instructions": "How large is the total area of visible mould in this photo?",
                    "criteria": {
                        "none": "No mould is visible",
                        "under_10_sqft": "Less than 10 square feet",
                        "10_to_30_sqft": "10 to under 30 square feet",
                        "30_sqft_or_more": "30 square feet or more",
                        "cannot_tell": "Mould is visible but the photo gives no way to judge its size",
                    },
                },
            },
        )
        answers = {k: v.model_dump() for k, v in (r.answers or {}).items()}
        usage = r.usage.model_dump() if r.usage else {}
        return {"photo": photo.name, "answers": answers, "usage": usage}

    return call


def agent() -> dict:
    r = client.interactions.create(
        agent=AGENT,
        input=(
            "Fetch https://data.cityofnewyork.us/resource/wvxf-dwi5.json?$limit=1 with Python. "
            "Reply with the HTTP status code and the names of the first five fields. Do nothing else."
        ),
        environment={"type": "remote"},  # a fresh hosted sandbox with default (open) network access
        api_version=config.DECISIONS_API_VERSION,  # agent environments are v1beta only too
        timeout=600,
    )
    usage = r.usage.model_dump() if getattr(r, "usage", None) else {}
    return {
        "agent": AGENT,
        "status": str(r.status),
        "id": getattr(r, "id", None),
        "text": (getattr(r, "output_text", None) or "")[:600],
        "usage": usage,
    }


if __name__ == "__main__":
    run("describe (Hydrogen, photo in)", describe)
    run("explain (Carbon, text)", explain)
    run("decide (Decisions API, mould photo)", decide(MOULD_PHOTO))
    run("decide (Decisions API, clean photo)", decide(CLEAN_PHOTO))
    if "--agent" in sys.argv:
        run("managed agent (one run, reaches NYC Open Data)", agent)
    config.VAR.mkdir(exist_ok=True)
    (config.VAR / "smoke.json").write_text(json.dumps(results, indent=1))
    failed = [k for k, v in results.items() if not v["ok"]]
    print("\nFAILED: " + ", ".join(failed) if failed else "\nAll calls returned.")
    sys.exit(1 if failed else 0)
