"""Photos the app can show: the held-out test items, and uploads kept for the session.

Media files are not in the repo. They exist only where data collection ran, so on any other machine
the test grid is empty and uploads still work.
"""
import io
import json
import uuid
from functools import lru_cache
from pathlib import Path

import pillow_heif
from PIL import Image, ImageOps

from app import config

pillow_heif.register_heif_opener()  # iPhones save HEIC; Pillow reads it once this is registered

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


VIDEO_SUFFIXES = {".mp4", ".mov", ".webm", ".m4v", ".3gp", ".mkv", ".avi"}  # ffmpeg reads the content, not the name
MAX_SIDE = 1600  # pixels on the long side. The test photos and video frames are this size or smaller
SENT_AS_IS = {"JPEG": "image/jpeg", "PNG": "image/png", "WEBP": "image/webp"}


def prepare_image(data: bytes) -> tuple[bytes, str]:
    """Any photo a phone or browser sends, as (bytes, mime type) the models take and answer quickly.

    A phone photo is 3 to 12 MB. Sent whole, the detection request took 10 to 15 seconds against a 15-second
    limit; a photo no wider than MAX_SIDE takes 1 to 2. HEIC (the iPhone's own format), GIF and the rest are
    re-saved as JPEG, upright. A JPEG, PNG or WebP that is already small and upright is passed through untouched.
    Raises ValueError if the bytes aren't a picture.
    """
    try:
        im = Image.open(io.BytesIO(data))
        if im.format in SENT_AS_IS and max(im.size) <= MAX_SIDE and im.getexif().get(0x0112, 1) == 1:
            return data, SENT_AS_IS[im.format]
        im = ImageOps.exif_transpose(im).convert("RGB")
        im.thumbnail((MAX_SIDE, MAX_SIDE))
        out = io.BytesIO()
        im.save(out, "JPEG", quality=88)
    except Exception:  # noqa: BLE001 - Pillow raises several kinds of error for a file it can't read
        raise ValueError("That file isn't a photo I can read. Try a JPEG, PNG or HEIC photo, or an MP4 or MOV video.") from None
    return out.getvalue(), "image/jpeg"


def save_upload(data: bytes, content_type: str | None = None) -> str:
    """Keep an uploaded photo for the session and return its id. The declared type is not trusted: the bytes
    are read, and prepare_image decides what is stored."""
    data, mime = prepare_image(data)
    ext = next(e for e, m in MIME.items() if m == mime)
    UPLOADS.mkdir(parents=True, exist_ok=True)
    photo_id = f"upload-{uuid.uuid4().hex[:12]}"
    (UPLOADS / f"{photo_id}{ext}").write_bytes(data)
    return photo_id


def save_video(data: bytes, suffix: str) -> Path:
    """Keep an uploaded video for the session and return where it is. The name is generated, never the client's."""
    UPLOADS.mkdir(parents=True, exist_ok=True)
    path = UPLOADS / f"video-{uuid.uuid4().hex[:12]}{suffix if suffix in VIDEO_SUFFIXES else '.bin'}"
    path.write_bytes(data)
    return path


def video_path(video_id: str) -> Path | None:
    """Where an uploaded video is, from the id an earlier answer returned. The id is looked up, never used as a path."""
    if video_id.startswith("video-") and video_id[6:].isalnum():
        return next(iter(UPLOADS.glob(f"{video_id}.*")), None)
    return None
