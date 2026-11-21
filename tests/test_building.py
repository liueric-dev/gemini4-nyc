import os

import pytest

from app import building


def test_building_kind_from_pluto_facts():
    assert building.building_kind(4, "122W 167 LLC", "C3") == "multiple_dwelling"
    assert building.building_kind(2, "XU, LEE", "B2") == "one_two_family"
    assert building.building_kind(1, "SMITH", "A1") == "one_two_family"
    assert building.building_kind(120, "NYC HOUSING AUTHORITY", "D3") == "nycha"
    assert building.building_kind(40, "SOME CONDO", "R4") == "condo"
    assert building.building_kind(None, None, None) is None
    assert building.building_kind(0, "A STORE LLC", "K1") is None


@pytest.mark.skipif(not os.environ.get("RUN_LIVE"), reason="live network test; run with RUN_LIVE=1")
def test_live_lookup_of_a_demo_building(tmp_path, monkeypatch):
    monkeypatch.setattr(building, "RUNTIME_DB", tmp_path / "runtime.db")  # throwaway cache file
    b = building.lookup("122 West 167th Street, Bronx")
    assert b["bbl"] == "2025140062"
    assert b["year_built"] == 1929 and b["building_kind"] == "multiple_dwelling"
    assert b["open_violations"]["total"] >= 0 and b["cached"] is False
    assert building.lookup("122 West 167th Street, Bronx")["cached"] is True
