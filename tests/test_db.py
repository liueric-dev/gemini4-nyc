"""The data layer, checked against answers read straight from the problem map.

Builds a throwaway database in a temp folder; never touches var/tenant.db.
"""
from app import db as dbm

MD = "multiple_dwelling"


def ids(rows, match="matched"):
    return [r["id"] for r in rows if r["match"] == match]


def test_counts(db):
    assert len(dbm.problem_types(db)) == 19
    assert len(dbm.problem_types(db, core_only=True)) == 8
    assert db.execute("SELECT count(*) FROM escalation_steps").fetchone()[0] >= 30


def test_mould_class_follows_area(db):
    def top(area):
        facts = {"mold_area_sqft": area, "mold_on_tile_grout_caulk_only": False}
        return dbm.candidate_rules(db, "mold", facts, MD, "dwelling unit")

    small, mid, large = top(5), top(12), top(40)
    assert ids(small) == ["EO-007"] and small[0]["class"] == "A" and small[0]["deadline_value"] == 90
    assert ids(mid) == ["EO-008"] and mid[0]["class"] == "B" and mid[0]["deadline_value"] == 30
    assert ids(large) == ["EO-010"] and large[0]["class"] == "C" and large[0]["deadline_value"] == 21
    assert set(ids(top(10))) == {"EO-008", "EO-009"}


def test_surface_mould_on_grout_is_not_a_violation(db):
    rows = dbm.candidate_rules(db, "mold", {"mold_area_sqft": 2, "mold_on_tile_grout_caulk_only": True}, MD, "dwelling unit")
    assert ids(rows) == ["EO-015"]
    assert rows[0]["violation"] == "no" and rows[0]["needs_judgement"]


def test_paint_depends_on_year_and_child(db):
    lead = dbm.candidate_rules(db, "peeling-paint", {"year_built": 1950, "child_under_6_resides": True}, MD, "dwelling unit")
    assert ids(lead) == ["EO-018"] and lead[0]["class"] == "C" and lead[0]["deadline_value"] == 21
    no_child = dbm.candidate_rules(db, "peeling-paint", {"year_built": 1950, "child_under_6_resides": False}, MD, "dwelling unit")
    assert ids(no_child) == ["EO-021"] and no_child[0]["class"] == "A" and no_child[0]["deadline_value"] == 90


def test_missing_facts_say_what_to_ask(db):
    rows = dbm.candidate_rules(db, "peeling-paint", {"year_built": 1950}, MD, "dwelling unit")
    assert ids(rows) == []
    asked = {f for r in rows for f in r["missing_facts"]}
    assert "child_under_6_resides" in asked
    assert "EO-022" not in [r["id"] for r in rows]  # built 1978 or later is ruled out


def test_pests_differ_by_building(db):
    md = dbm.candidate_rules(db, "pests", {"pest": "roach"}, MD, "dwelling unit")
    house = dbm.candidate_rules(db, "pests", {"pest": "roach"}, "one_two_family", "dwelling unit")
    assert ids(md) == ["EO-033"] and md[0]["class"] == "C" and md[0]["deadline_value"] == 21
    assert ids(house) == ["EO-039"] and house[0]["class"] == "B" and house[0]["deadline_value"] == 30


def test_heat_has_no_grace_period(db):
    facts = {"heat_season": True, "hour": 10, "outside_temp_f": 40, "indoor_temp_f": 60}
    rows = dbm.candidate_rules(db, "heat-hot-water", facts, MD, "dwelling unit")
    top = next(r for r in rows if r["id"] == "EO-059")
    assert top["match"] == "matched" and top["class"] == "C" and top["deadline_unit"] == "none"
    assert "EO-060" not in [r["id"] for r in rows]  # warm outside is ruled out


def test_leak_class_is_left_to_the_inspector(db):
    rows = dbm.candidate_rules(db, "leak", {}, MD, "dwelling unit")
    base = next(r for r in rows if r["id"] == "EO-001")
    assert base["class"] is None and base["class_options"] == "A,B,C" and base["certainty"] == "class-unsettled"


def test_sections_and_steps(db):
    secs = dbm.sections_for(db, "EO-008")
    assert "nyc-hmc-27-2017-3" in [s["id"] for s in secs]
    assert all(s["text"] and s["source_type"] == "official" for s in secs)
    codes = [s["code"] for s in dbm.steps_for(db, "EO-001")]
    assert {"A1", "A2", "A3", "A4", "A6"} <= set(codes)
    assert dbm.hpd_order(db, "550") is not None


def test_steps_have_plain_action_titles(db):
    steps = dbm.steps_for(db, "EO-008")
    by_code = {s["code"]: s for s in steps}
    assert by_code["A1"]["action"] == "Tell your landlord in writing"
    assert by_code["A1"]["who"] == "Landlord or managing agent"
    assert by_code["A2"]["when"] and "30 days" in by_code["A2"]["when"]
    assert all(s["action"] and not s["action"].startswith(s["code"]) for s in steps)
    assert [s["code"] for s in dbm.general_steps(db, "A")] == [f"A{i}" for i in range(1, 9)]
