"""The web API. Run with `make dev`."""
import hashlib
import json
import logging
import mimetypes
import os
import time
from collections import deque
from pathlib import Path
from typing import Annotated

from fastapi import Body, FastAPI, File, Form, HTTPException, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app import building, case_agent, config, letter, media, pipeline, shop, video

app = FastAPI(title="Tenant advocate")
log = logging.getLogger("tenant")  # failures are written here with their cause; the tenant sees a plain sentence
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
        # which commit is running: Render sets RENDER_GIT_COMMIT; on a laptop this says "local"
        "commit": os.environ.get("RENDER_GIT_COMMIT", "")[:7] or "local",
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
    except Exception:
        log.exception("building lookup failed")
        raise HTTPException(503, "The city's building records did not respond. Try again.") from None


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


def is_video(f: UploadFile) -> bool:
    """Is the upload a video? Goes by the declared type, then the file name, because some clients send no
    type or a generic one. Anything that isn't a video is read as a photo, and media.prepare_image says so
    if it isn't one either."""
    declared = (f.content_type or "").split(";")[0].strip().lower()
    if declared.startswith(("image/", "video/")):
        return declared.startswith("video/")
    name = f.filename or ""
    return (mimetypes.guess_type(name)[0] or "").startswith("video/") or Path(name).suffix.lower() in media.VIDEO_SUFFIXES


MAX_UPLOAD = 20 * 1024 * 1024
MAX_VIDEO = 100 * 1024 * 1024
SEEN_SECONDS = 30 * 60


def _seen_file(media_id: str) -> Path:
    return config.VAR / "cache" / "vision" / f"{media_id}.json"


def load_seen(media_id: str) -> dict:
    """What the models read from this photo or video in the last half hour, or {}. A follow-up on the same
    picture (an answer to a question, an address added later) reuses it; see pipeline.look."""
    try:
        f = _seen_file(media_id)
        if time.time() - f.stat().st_mtime < SEEN_SECONDS:
            return json.loads(f.read_text())
    except (OSError, ValueError):
        pass
    return {}


def save_seen(media_id: str, seen: dict) -> None:
    if seen and not _seen_file(media_id).exists():
        _seen_file(media_id).parent.mkdir(parents=True, exist_ok=True)
        _seen_file(media_id).write_text(json.dumps(seen))


@app.post("/api/analyze")
def analyze(
    photo: Annotated[UploadFile | None, File()] = None,
    photo_id: Annotated[str | None, Form()] = None,
    address: Annotated[str | None, Form()] = None,
    answers: Annotated[str | None, Form()] = None,
    explain: Annotated[bool, Form()] = True,
    note: Annotated[str | None, Form()] = None,
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
    clip = None  # the saved video, when this request is about one
    if photo is not None and is_video(photo):
        data = photo.file.read(MAX_VIDEO + 1)
        if len(data) > MAX_VIDEO:
            raise HTTPException(413, "Video is larger than 100 MB")
        clip = media.save_video(data, Path(photo.filename or "").suffix.lower())
    elif photo is None and photo_id and photo_id.startswith("video-"):
        clip = media.video_path(photo_id)  # a follow-up on a video sent earlier: no second upload
        if not clip:
            raise HTTPException(404, "No such video on this machine")
    if clip:
        seen = load_seen(clip.stem)
        try:
            result = video.analyze_video(clip, address=address or None, answers=parsed, with_explanation=explain,
                                         note=note, seen=seen)
        except ValueError as e:
            raise HTTPException(415, str(e)) from None
        except Exception as e:
            log.exception("video analysis failed")
            raise HTTPException(503, f"The video could not be analysed ({type(e).__name__}). Try again.") from None
        save_seen(clip.stem, seen)
        result["photo"] = {"id": clip.stem}  # send this back as photo_id with answers, in place of the file
        return result
    if photo is not None:
        data = photo.file.read(MAX_UPLOAD + 1)
        if len(data) > MAX_UPLOAD:
            raise HTTPException(413, "Photo is larger than 20 MB")
        try:
            photo_id = media.save_upload(data)
        except ValueError as e:
            raise HTTPException(415, str(e)) from None
    if not photo_id:
        raise HTTPException(400, "Send a photo or a photo_id")
    found = media.load(photo_id)
    if not found:
        raise HTTPException(404, "No such photo on this machine")
    key = hashlib.sha256(json.dumps([photo_id, address or "", parsed, explain, note or ""], sort_keys=True).encode()).hexdigest()[:16]
    saved = config.VAR / "cache" / "analyze" / f"{key}.json"
    seen = load_seen(photo_id)
    try:
        result = pipeline.analyze(found[0], found[1], address=address or None, answers=parsed, with_explanation=explain,
                                  note=note, seen=seen)
    except Exception as e:  # the venue network drops calls; fall back to the last good answer if there is one
        log.exception("photo analysis failed")
        if saved.exists():
            return {**json.loads(saved.read_text()), "from_cache": True,
                    "cache_note": "The live call failed, so this is the answer saved from the last successful run."}
        raise HTTPException(503, f"The model service did not respond ({type(e).__name__}). Try again.") from None
    save_seen(photo_id, seen)
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
    except Exception as e:
        log.exception("explanation failed")
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


@app.post("/api/ask")
def ask_question(
    question: Annotated[str, Body(embed=True)],
    analysis: Annotated[dict | None, Body(embed=True)] = None,
    history: Annotated[list[dict] | None, Body(embed=True)] = None,
) -> dict:
    """Answer a question typed into the chat, using only the case, the rules and law for the kind of problem it
    mentions, and the escalation steps. history is the earlier exchange, [{"q": ..., "a": ...}].
    Returns answer, citations (quotes checked against the law) and covered (false when there is no source)."""
    if not question.strip():
        raise HTTPException(400, "Ask a question")
    spend("analyze")
    try:
        return pipeline.ask(question, analysis, history)
    except Exception as e:
        log.exception("question failed")
        raise HTTPException(503, f"The model service did not respond ({type(e).__name__}). Try again.") from None
