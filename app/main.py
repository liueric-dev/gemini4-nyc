"""The web API. Run with `make dev`."""
import hashlib
import json
from typing import Annotated

from fastapi import Body, FastAPI, File, Form, HTTPException, Response, UploadFile

from app import building, case_agent, config, letter, media, pipeline, video

app = FastAPI(title="Tenant advocate")


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
    for path in (config.ROOT / "eval/results/test-results.json", config.VAR / "eval/test-results.json",
                 config.VAR / "eval/dev-results.json"):
        if path.exists():
            return json.loads(path.read_text())
    raise HTTPException(404, "No evaluation has been run yet")


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
