"""The web API. Run with `make dev`."""
import hashlib
import json
import os
import time
from collections import deque
from typing import Annotated

from fastapi import Body, FastAPI, File, Form, HTTPException, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app import building, case_agent, config, letter, media, pipeline, shop, video

app = FastAPI(title="Tenant advocate")
# The chat prototype (hey-niia/tenard) is served from another origin and calls this API from the browser.
app.add_middleware(CORSMiddleware, allow_origins=["https://hey-niia.github.io", "http://localhost:5180"],
                   allow_methods=["GET", "POST"], allow_headers=["*"])


# ---- a cap on the calls that cost money, so a public link can't drain the Gemini quota
LIMITS = {"analyze": int(os.environ.get("LIMIT_ANALYZE_PER_HOUR", "300")),
          "case": int(os.environ.get("LIMIT_CASE_FILES_PER_HOUR", "30"))}
_calls: dict[str, deque] = {"analyze": deque(), "case": deque()}


def spend(kind: str) -> None:
    now, q = time.time(), _calls[kind]
    while q and now - q[0] > 3600:
        q.popleft()
    if len(q) >= LIMITS[kind]:
        raise HTTPException(429, "This demo has reached its hourly limit. Try again later.")
    q.append(now)


# ---- the screens: plain files, served by this process so one container is the whole app
WEB = config.ROOT / "web"


@app.get("/", include_in_schema=False)
def page_index() -> FileResponse:
    return FileResponse(WEB / "index.html")


@app.get("/proof.html", include_in_schema=False)
def page_proof() -> FileResponse:
    return FileResponse(WEB / "proof.html")


@app.get("/app.js", include_in_schema=False)
def page_script() -> FileResponse:
    return FileResponse(WEB / "public" / "app.js", media_type="text/javascript")


@app.get("/api/health")
def health() -> dict:
    return {
        "ok": True,
        "missing_keys": config.missing_keys(),
        "database_built": config.DB_PATH.exists(),
    }


@app.get("/api/building")
def get_building(address: str) -> dict:
    """Address to building facts: year built, units, building kind, open HPD violations."""
    try:
        return building.lookup(address)
    except building.AddressNotFound:
        raise HTTPException(404, f"No NYC address found for: {address}") from None


@app.get("/api/test-items")
def get_test_items() -> dict:
    """The held-out test photos, for the pick-a-photo grid. Labels are not included."""
    return {"items": media.test_items()}


@app.get("/api/photos/{photo_id}")
def get_photo(photo_id: str) -> Response:
    found = media.load(photo_id)
    if not found:
        raise HTTPException(404, "No such photo on this machine")
    return Response(content=found[0], media_type=found[1], headers={"Cache-Control": "max-age=3600"})


MAX_UPLOAD = 20 * 1024 * 1024
MAX_VIDEO = 100 * 1024 * 1024


@app.post("/api/analyze")
def analyze(
    photo: Annotated[UploadFile | None, File()] = None,
    photo_id: Annotated[str | None, Form()] = None,
    address: Annotated[str | None, Form()] = None,
    answers: Annotated[str | None, Form()] = None,
    explain: Annotated[bool, Form()] = True,
) -> dict:
    """A photo to findings. Send an uploaded photo or the id of a test photo, plus an optional address
    and answers (a JSON object of fact name to value) to questions from an earlier response."""
    spend("analyze")
    try:
        parsed = json.loads(answers) if answers else {}
    except json.JSONDecodeError:
        raise HTTPException(400, "answers must be a JSON object") from None
    if not isinstance(parsed, dict):
        raise HTTPException(400, "answers must be a JSON object")
    if photo is not None and (photo.content_type or "").startswith("video/"):
        data = photo.file.read(MAX_VIDEO + 1)
        if len(data) > MAX_VIDEO:
            raise HTTPException(413, "Video is larger than 100 MB")
        try:
            path = media.save_video(data, photo.content_type)
            return video.analyze_video(path, address=address or None, answers=parsed, with_explanation=explain)
        except ValueError as e:
            raise HTTPException(415, str(e)) from None
        except Exception as e:  # noqa: BLE001
            raise HTTPException(503, f"The video could not be analysed ({type(e).__name__}). Try again.") from None
    if photo is not None:
        data = photo.file.read(MAX_UPLOAD + 1)
        if len(data) > MAX_UPLOAD:
            raise HTTPException(413, "Photo is larger than 20 MB")
        try:
            photo_id = media.save_upload(data, photo.content_type or "")
        except ValueError as e:
            raise HTTPException(415, str(e)) from None
    if not photo_id:
        raise HTTPException(400, "Send a photo or a photo_id")
    found = media.load(photo_id)
    if not found:
        raise HTTPException(404, "No such photo on this machine")
    key = hashlib.sha256(json.dumps([photo_id, address or "", parsed, explain], sort_keys=True).encode()).hexdigest()[:16]
    saved = config.VAR / "cache" / "analyze" / f"{key}.json"
    try:
        result = pipeline.analyze(found[0], found[1], address=address or None, answers=parsed, with_explanation=explain)
    except Exception as e:  # noqa: BLE001 - the venue network drops calls; fall back to the last good answer if there is one
        if saved.exists():
            return {**json.loads(saved.read_text()), "from_cache": True,
                    "cache_note": "The live call failed, so this is the answer saved from the last successful run."}
        raise HTTPException(503, f"The model service did not respond ({type(e).__name__}). Try again.") from None
    result["photo"] = {"id": photo_id, "url": f"/api/photos/{photo_id}"}
    result["from_cache"] = False
    saved.parent.mkdir(parents=True, exist_ok=True)
    saved.write_text(json.dumps(result))
    return result


@app.post("/api/explain")
def explain_findings(analysis: Annotated[dict, Body(embed=True)]) -> dict:
    """Add the written explanation and checked citations to an analysis made with explain=false.
    Lets a screen show the class and deadline first, then fill this in when it arrives."""
    try:
        return pipeline.add_explanations(analysis)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(503, f"The model service did not respond ({type(e).__name__}). Try again.") from None


@app.post("/api/case-file")
def start_case_file(
    analysis: Annotated[dict, Body(embed=True)],
    apartment: Annotated[str | None, Body(embed=True)] = None,
) -> dict:
    """Start the case file agent. Send the response from /api/analyze (it must include a building).
    Returns a case_id straight away; the agent takes a minute or two. Poll GET /api/case-file/{case_id}."""
    try:
        case = case_agent.build_case(analysis, apartment)
    except ValueError as e:
        raise HTTPException(400, str(e)) from None
    spend("case")
    return {"case_id": case_agent.start(case), "status": "in_progress"}


@app.get("/api/case-file/{case_id}")
def get_case_file(case_id: str) -> dict:
    """status is in_progress until the agent finishes; then markdown holds the case file."""
    found = case_agent.status(case_id)
    if not found:
        raise HTTPException(404, "No such case")
    return found


@app.get("/api/results")
def get_results() -> dict:
    """The evaluation numbers for the proof screen: the frozen test set if it has been run, else the dev run."""
    out = {}
    for name, key in (("test-results.json", "photos"), ("test-video-results.json", "video"), ("test-items.json", "items")):
        path = config.ROOT / "eval/results" / name
        if path.exists():
            out[key] = json.loads(path.read_text())
    if not out:
        raise HTTPException(404, "No evaluation has been run yet")
    return out


@app.post("/api/letter")
def draft_letter(
    analysis: Annotated[dict, Body(embed=True)],
    tenant_name: Annotated[str | None, Body(embed=True)] = None,
    apartment: Annotated[str | None, Body(embed=True)] = None,
) -> dict:
    """Draft the letter to the landlord and the 311 complaint text from an /api/analyze response."""
    try:
        return letter.draft(analysis, tenant_name, apartment)
    except ValueError as e:
        raise HTTPException(400, str(e)) from None


@app.get("/api/diy/{rule_id}")
def diy_kit(rule_id: str) -> dict:
    """For a problem that is the tenant's own job: what to buy (one Shopify product per item) and the steps.
    Only tenant-duty rules have a kit, so products never appear on a landlord's violation."""
    if rule_id not in shop.KITS:
        raise HTTPException(404, "There is no fix-it-yourself kit for this rule")
    return shop.kit(rule_id)
