"""Photos the app can show: the held-out test items, and uploads kept for the session.

Media files are not in the repo. They exist only where data collection ran, so on any other machine
the test grid is empty and uploads still work.
"""
import json
import uuid
from functools import lru_cache
from pathlib import Path

from app import config

MEDIA = config.DATA / "media"
UPLOADS = config.VAR / "uploads"
SAMPLES = MEDIA / "samples"
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


@lru_cache(maxsize=1)
def _manifest() -> dict[str, dict]:
    out = {}
    for line in (MEDIA / "manifest.jsonl").open(encoding="utf-8"):
        if line.strip():
            o = json.loads(line)
            out[o["id"]] = o
    return out


def _path(item: dict) -> Path | None:
    raw = item.get("raw_file")
    if not isinstance(raw, str) or not raw:
        return None
    p = MEDIA / raw
    if not p.exists():
        p = SAMPLES / Path(raw).name  # the redistributable subset that is committed to the repo
    return p if p.exists() and p.suffix.lower() in MIME else None


@lru_cache(maxsize=1)
def test_items() -> list[dict]:
    """The reviewed, frozen test photos that are on this machine. No labels are returned."""
    review = json.loads((MEDIA / "review/review_set.json").read_text())
    items = []
    for it in review["items"]:
        m = _manifest().get(it["id"])
        if m and m.get("media_type") == "image" and _path(m):
            items.append({"id": it["id"], "url": f"/api/photos/{it['id']}", "license": m.get("license"),
                          "attribution": m.get("attribution"), "source_url": m.get("source_url")})
    return items


def load(photo_id: str) -> tuple[bytes, str] | None:
    """Bytes and mime type for a manifest id or an upload id. The id is looked up, never used as a path."""
    m = _manifest().get(photo_id)
    if m:
        p = _path(m)
        return (p.read_bytes(), MIME[p.suffix.lower()]) if p else None
    if photo_id.startswith("upload-") and photo_id[7:].isalnum():
        for p in UPLOADS.glob(f"{photo_id}.*"):
            if p.suffix.lower() in MIME:
                return p.read_bytes(), MIME[p.suffix.lower()]
    return None


VIDEO_MIME = {".mp4": "video/mp4", ".mov": "video/quicktime", ".webm": "video/webm", ".m4v": "video/x-m4v"}


def save_upload(data: bytes, content_type: str) -> str:
    ext = next((e for e, m in MIME.items() if m == content_type), None)
    if not ext:
        raise ValueError(f"Unsupported image type: {content_type}")
    UPLOADS.mkdir(parents=True, exist_ok=True)
    photo_id = f"upload-{uuid.uuid4().hex[:12]}"
    (UPLOADS / f"{photo_id}{ext}").write_bytes(data)
    return photo_id


def save_video(data: bytes, content_type: str) -> Path:
    """Keep an uploaded video for the session and return where it is. The name is generated, never the client's."""
    ext = next((e for e, m in VIDEO_MIME.items() if m == content_type), None)
    if not ext:
        raise ValueError(f"Unsupported video type: {content_type}")
    UPLOADS.mkdir(parents=True, exist_ok=True)
    path = UPLOADS / f"video-{uuid.uuid4().hex[:12]}{ext}"
    path.write_bytes(data)
    return path
