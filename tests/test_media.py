"""Uploads: any photo a phone sends is read, turned upright and kept to a size the models answer quickly."""
import io
import json

import pytest
from PIL import Image

from app import media


def picture(fmt: str, size: tuple[int, int], **save) -> bytes:
    out = io.BytesIO()
    Image.new("RGB", size, (120, 90, 60)).save(out, fmt, **save)
    return out.getvalue()


def test_a_small_upright_photo_is_passed_through_untouched():
    for fmt, mime in (("JPEG", "image/jpeg"), ("PNG", "image/png"), ("WEBP", "image/webp")):
        data = picture(fmt, (800, 600))
        assert media.prepare_image(data) == (data, mime)


def test_a_phone_sized_photo_is_made_smaller():
    data, mime = media.prepare_image(picture("JPEG", (4032, 3024)))
    assert mime == "image/jpeg" and Image.open(io.BytesIO(data)).size == (1600, 1200)


def test_heic_and_gif_are_resaved_as_jpeg():
    for fmt in ("HEIF", "GIF"):
        data, mime = media.prepare_image(picture(fmt, (640, 480)))
        assert mime == "image/jpeg" and Image.open(io.BytesIO(data)).format == "JPEG"


def test_a_sideways_photo_is_turned_upright():
    exif = Image.Exif()
    exif[0x0112] = 6  # the camera was held on its side
    data, _ = media.prepare_image(picture("JPEG", (800, 600), exif=exif))
    assert Image.open(io.BytesIO(data)).size == (600, 800)


def test_a_file_that_is_not_a_picture_is_refused_in_plain_words():
    with pytest.raises(ValueError, match="isn't a photo I can read"):
        media.prepare_image(b"not a picture")


def test_uploads_are_stored_by_what_they_are_not_what_the_client_said(tmp_path, monkeypatch):
    monkeypatch.setattr(media, "UPLOADS", tmp_path)
    photo_id = media.save_upload(picture("HEIF", (640, 480)), "image/heic")
    assert media.load(photo_id)[1] == "image/jpeg"
    clip = media.save_video(b"frames", ".mkv")
    assert clip.suffix == ".mkv" and media.video_path(clip.stem) == clip
    assert media.save_video(b"frames", ".exe").suffix == ".bin"  # the name comes from a short list, never the client
    assert media.video_path("video-../../etc") is None and media.video_path("upload-abc") is None


def test_pinned_photos_come_first_and_the_rest_keep_their_order():
    ids = [it["id"] for it in media.test_items()]
    assert "med-0832" in ids  # committed in data/media/samples, so it is on every machine
    pinned = [p for p in media.PINNED if p in ids]
    assert ids[: len(pinned)] == pinned
    review = [it["id"] for it in json.loads((media.MEDIA / "review/review_set.json").read_text())["items"]]
    rest = set(ids[len(pinned):])
    assert ids[len(pinned):] == [i for i in review if i in rest]
