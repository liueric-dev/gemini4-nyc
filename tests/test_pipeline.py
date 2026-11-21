"""The pipeline's decision logic and citation check. No network calls."""
from app import db as dbm
from app import pipeline as p

MD = "multiple_dwelling"


def sources(db):
    return {k: v["source"] for k, v in dbm.fact_defs(db).items()}


def test_known_area_picks_the_rule(db):
    d = p.decide(db, "mold", {"mold_area_sqft": 15}, MD, fact_sources=sources(db))
    assert d["rule"]["id"] == "EO-008" and d["questions"] == []
    assert p._outcome(d["rule"]) == "violation"


def test_unknown_area_asks_for_it_and_not_for_city_records(db):
    d = p.decide(db, "mold", {}, MD, fact_sources=sources(db))
    assert d["rule"] is None
    assert "mold_area_sqft" in d["questions"]
    assert "prior_class" not in d["questions"]  # that comes from HPD's record, not the tenant


def test_leak_needs_no_question_because_no_answer_changes_the_outcome(db):
    d = p.decide(db, "leak", {}, MD, fact_sources=sources(db))
    assert d["rule"]["id"] == "EO-001" and d["questions"] == []
    assert p._outcome(d["rule"]) == "inspector_decides"


def test_paint_asks_about_a_child_under_six(db):
    d = p.decide(db, "peeling-paint", {"year_built": 1950}, MD, fact_sources=sources(db))
    assert d["rule"] is None and "child_under_6_resides" in d["questions"]
    answered = p.decide(db, "peeling-paint", {"year_built": 1950, "child_under_6_resides": True}, MD,
                        fact_sources=sources(db))
    assert answered["rule"]["id"] == "EO-018" and answered["rule"]["class"] == "C"


def test_surface_mould_on_grout_is_the_tenants_duty(db):
    facts = {"mold_area_sqft": 5, "mold_on_tile_grout_caulk_only": True}
    d = p.decide(db, "mold", facts, MD, fact_sources=sources(db))
    assert d["rule"]["id"] == "EO-015" and p._outcome(d["rule"]) == "not_landlord_responsibility"


def test_citation_check_keeps_real_quotes_and_drops_the_rest(db):
    s = dbm.get_section(db, "nyc-hmc-27-2017-3")
    real = s["text"][s["text"].index("The presence of visible mold"):][:120]
    kept, dropped = p.check_citations(
        [
            {"section_id": s["id"], "quote": real, "supports": "x"},
            {"section_id": s["id"], "quote": "The landlord must repaint every wall within seven days.", "supports": "x"},
            {"section_id": "nyc-hmc-99-9999", "quote": real, "supports": "x"},
            {"section_id": s["id"], "quote": "mold", "supports": "too short to count"},
        ],
        {s["id"]: s},
    )
    assert len(kept) == 1 and dropped == 3
    assert kept[0]["checked"] and kept[0]["citation"] == s["citation"]


def test_long_penalty_section_is_cut_to_the_relevant_parts(db):
    s = dbm.get_section(db, "nyc-hmc-27-2115")
    general = p.excerpt(s, "mold")
    heat = p.excerpt(s, "heat-hot-water")
    assert len(general) < 6000 and general.startswith("(c) ")
    assert "(k) (1)" in heat and len(heat) > len(general)


def test_detection_cut_off_and_photo_facts(monkeypatch):
    # fixed cut-offs for the test, so retuning app/thresholds.json doesn't change what is checked here
    monkeypatch.setitem(p.THRESHOLDS, "confirm", {"default": 0.5})
    monkeypatch.setitem(p.THRESHOLDS, "detect", {"default": 0.5})
    monkeypatch.setitem(p.THRESHOLDS, "fact", 0.5)
    probs = {"mold": 0.91, "leak": 0.77, "pests": 0.12}
    assert p.detected_types(probs) == ["mold", "leak"]
    # a problem is reported only if the model proposed it and the Decisions API confirms it
    assert p.confirmed_types(["mold", "pests"], probs) == ["mold"]
    assert p.confirmed_types([], probs) == []
    answers = {"f_mold_size": {"choice": "10_to_under_30_sqft", "confidence": 0.7},
               "f_mold_tile_only": {"noul": 0.1}}
    facts = p.photo_facts("mold", answers)
    assert facts["mold_area_sqft"][0] == 15 and facts["mold_on_tile_grout_caulk_only"][0] is False
    unsure = p.photo_facts("mold", {"f_mold_size": {"choice": "under_10_sqft", "confidence": 0.4}})
    assert "mold_area_sqft" not in unsure  # below the cut-off: ask the tenant instead of guessing


def test_quality_report_asks_for_scale_only_when_size_matters(monkeypatch):
    monkeypatch.setitem(p.THRESHOLDS, "quality", 0.5)
    scores = {"sharp_and_lit": 0.9, "close_enough": 0.8, "shows_location": 0.7, "has_scale_reference": 0.1}
    mould = p.quality_report(scores, ["mold"])
    assert mould["good_for_evidence"] is False and len(mould["retake_requests"]) == 1
    assert "scale" in mould["retake_requests"][0]
    pests = p.quality_report(scores, ["pests"])
    assert pests["good_for_evidence"] is True and "has_scale_reference" not in pests["scores"]
    dark = p.quality_report({**scores, "sharp_and_lit": 0.2}, ["pests"])
    assert dark["good_for_evidence"] is False and "blurry or too dark" in dark["retake_requests"][0]
    assert p.quality_report(scores, []) is None  # nothing reported, nothing to document


def test_video_frames_are_spread_and_a_single_odd_frame_is_not_reported(monkeypatch):
    from app import video

    monkeypatch.setitem(p.THRESHOLDS, "video", {"seconds_per_frame": 3, "max_frames": 16, "min_frames": 4,
                                                 "min_confirming_frames": 2})
    assert len(video.frame_times(9)) == 4          # short clip: the minimum
    assert len(video.frame_times(30)) == 10        # one about every 3 seconds
    assert len(video.frame_times(385)) == 16       # long clip: capped
    assert video.frame_times(30)[0] == 1.5 and video.frame_times(30)[-1] == 28.5

    def frame(t, found):
        return t, {"findings": [{"problem_type": k, "probability": v} for k, v in found.items()]}

    per_frame = [frame(1.5, {"mold": 0.7}), frame(4.5, {"mold": 0.9, "leak": 0.6}), frame(7.5, {}), frame(10.5, {"mold": 0.8}),
                 frame(13.5, {})]
    findings, seen = video.merge(per_frame)
    assert [f["problem_type"] for f in findings] == ["mold"]          # the leak was seen in one frame only
    assert findings[0]["time_s"] == 4.5 and findings[0]["seen_at_s"] == [1.5, 4.5, 10.5]
    assert findings[0]["time_range_s"] == [1.5, 10.5] and seen == {"mold": 3, "leak": 1}
    short, _ = video.merge(per_frame[:4][1:2] + per_frame[2:4])        # a 3-frame clip: one frame is enough
    assert sorted(f["problem_type"] for f in short) == ["leak", "mold"]


def own_connection(db, monkeypatch):
    """analyze() and ask() open and close their own connection; point them at the test database."""
    from pathlib import Path

    path, connect = Path(db.execute("PRAGMA database_list").fetchone()[2]), dbm.connect
    monkeypatch.setattr(dbm, "connect", lambda: connect(path))


def looked(problem_type):
    """What look() returns for a photo that plainly shows one problem."""
    return {"det": {"probabilities": {problem_type: 0.95}, "answers": {}},
            "desc": {"findings": [{"problem_type": problem_type, "description": "seen", "where": "wall"}]}, "quality": None}


def test_a_follow_up_reuses_what_was_read_from_the_photo(db, monkeypatch):
    own_connection(db, monkeypatch)
    monkeypatch.setitem(p.THRESHOLDS, "confirm", {"default": 0.5})
    calls = []
    monkeypatch.setattr(p, "look", lambda *a: calls.append(1) or looked("mold"))
    seen: dict = {}
    first = p.analyze(b"jpeg", seen=seen, with_explanation=False)
    assert first["findings"][0]["outcome"] == "needs_answer" and seen["det"] and calls == [1]
    # the tenant answers the question: same picture, so the models are not asked again
    second = p.analyze(b"jpeg", seen=seen, answers={"mold_area_sqft": 15}, with_explanation=False)
    assert second["findings"][0]["rule_id"] == "EO-008" and calls == [1]


def test_without_a_building_record_the_year_built_is_asked(db, monkeypatch):
    own_connection(db, monkeypatch)
    monkeypatch.setitem(p.THRESHOLDS, "confirm", {"default": 0.5})
    told = {"child_under_6_resides": True, "lead_presumption_rebutted": False, "owner_occupied_unit": False}
    asked = p.analyze(b"jpeg", seen=looked("peeling-paint"), answers=told, with_explanation=False)["findings"][0]
    assert asked["outcome"] == "needs_answer" and asked["questions"][0]["fact"] == "year_built"
    settled = p.analyze(b"jpeg", seen=looked("peeling-paint"), answers={**told, "year_built": 1929},
                        with_explanation=False)["findings"][0]
    assert settled["rule_id"] == "EO-018" and settled["class"] == "C"


def test_a_building_lookup_that_fails_does_not_lose_the_photo(db, monkeypatch):
    own_connection(db, monkeypatch)
    monkeypatch.setitem(p.THRESHOLDS, "confirm", {"default": 0.5})

    def down(address):
        raise OSError("the city's site is down")

    monkeypatch.setattr(p.building_mod, "lookup", down)
    result = p.analyze(b"jpeg", seen=looked("leak"), address="122 West 167th Street, Bronx", with_explanation=False)
    assert result["findings"][0]["problem_type"] == "leak" and "could not be reached" in result["building_error"]


def test_heat_uses_the_outdoor_temperature(db, monkeypatch):
    own_connection(db, monkeypatch)
    monkeypatch.setitem(p.THRESHOLDS, "confirm", {"default": 0.5})
    monkeypatch.setattr(p, "_now_facts", lambda: {"hour": 15.0, "heat_season": True})
    monkeypatch.setattr(p.weather, "outside_temp_f", lambda: 40.0)
    cold = p.analyze(b"jpeg", seen=looked("heat-hot-water"), answers={"indoor_temp_f": 60}, with_explanation=False)
    f = cold["findings"][0]
    assert f["rule_id"] == "EO-059" and f["class"] == "C"
    assert {"name": "outside_temp_f", "value": 40.0} == {k: u[k] for u in f["facts_used"] if u["name"] == "outside_temp_f"
                                                        for k in ("name", "value")}


def test_a_question_gets_the_rules_and_law_for_what_it_is_about(db, monkeypatch):
    own_connection(db, monkeypatch)
    assert p.topics("There are roaches in my kitchen") == ["pests"]
    assert p.topics("Can my landlord raise my rent?") == []  # "landlord" is not "lead"
    sent = {}

    def model(model_id, contents, schema, level):
        sent["prompt"], sent["ids"] = contents[0], schema["properties"]["citations"]["items"]["properties"]["section_id"]["enum"]
        return {"covered": False, "answer": "x", "citations": []}

    monkeypatch.setattr(p, "_generate_json", model)
    p.ask("And what about bedbugs?", None, [{"q": "Is mould a violation?", "a": "It depends on the size."}])
    assert '<rules topic="Pests">' in sent["prompt"] and "bedbugs" in sent["prompt"]
    assert '<rules topic="Mould">' in sent["prompt"] and "Tenant: Is mould a violation?" in sent["prompt"]
    assert "nyc-hmc-27-2017-3" in sent["ids"]  # the mould section can now be quoted


def test_a_frame_that_fails_does_not_lose_the_video_and_the_note_is_read_once(monkeypatch, tmp_path):
    from app import video

    stills = [(1.5, b"a"), (4.5, b"b"), (7.5, b"c"), (10.5, b"d"), (13.5, b"e")]
    notes = []

    def analyze(data, mime_type, seen=None, answers=None, **kwargs):
        if data == b"c":
            raise TimeoutError("the model did not answer")
        seen.update({"det": data.decode()})
        return {"findings": [{"problem_type": "leak", "probability": 0.9, "said": answers}], "photo_quality": None}

    monkeypatch.setattr(video, "frames", lambda path: stills)
    monkeypatch.setattr(video, "duration", lambda path: 15.0)
    monkeypatch.setattr(p, "analyze", analyze)
    monkeypatch.setattr(p, "facts_from_note", lambda note: notes.append(note) or {"leak_source": "roof"})
    seen: dict = {}
    result = video.analyze_video(tmp_path / "clip.mp4", with_explanation=False, save_frames=False,
                                 note="it comes from the roof", seen=seen)
    assert result["video"]["frames_analysed"] == 4 and result["findings"][0]["frames_confirming"] == 4
    assert notes == ["it comes from the roof"] and result["facts_from_description"] == {"leak_source": "roof"}
    assert result["findings"][0]["said"] == {"leak_source": "roof"}
    assert sorted(seen) == ["1.50", "10.50", "13.50", "4.50"]  # kept for a follow-up; the failed frame is not


def test_video_frames_are_all_analysed_at_the_same_time(monkeypatch, tmp_path):
    import threading

    from app import video

    stills = [(float(t), b"jpeg") for t in range(16)]  # the most frames a video is cut into
    together = threading.Barrier(len(stills), timeout=5)  # breaks unless every frame is in flight at once

    def analyze(data, mime_type, **kwargs):
        together.wait()
        return {"findings": [], "photo_quality": None}

    monkeypatch.setattr(video, "frames", lambda path: stills)
    monkeypatch.setattr(video, "duration", lambda path: 48.0)
    monkeypatch.setattr(p, "analyze", analyze)
    result = video.analyze_video(tmp_path / "clip.mp4", with_explanation=False, save_frames=False)
    assert result["video"]["frames_analysed"] == 16 and result["nothing_found"] is True
