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


class Reply:
    def __init__(self, properties):
        self._p = properties

    def raise_for_status(self):
        pass

    def json(self):
        return {"features": [{"properties": self._p}] if self._p else []}


def geocoder_says(monkeypatch, label, housenumber, bbl="2025140062"):
    p = {"label": label, "housenumber": housenumber, "addendum": {"pad": {"bbl": bbl}}}
    monkeypatch.setattr(building.httpx, "get", lambda *a, **k: Reply(p))


def test_a_match_is_kept_only_if_it_is_the_house_number_that_was_typed(monkeypatch):
    geocoder_says(monkeypatch, "122 WEST 167 STREET, Bronx, NY, USA", "122")
    assert building.geocode("122 West 167th Street, Bronx")["bbl"] == "2025140062"
    geocoder_says(monkeypatch, "39-06 114 STREET, North Corona, NY, USA", "39-06")
    assert building.geocode("3906 114th Street Queens")["address"].startswith("39-06")  # with or without the hyphen
    # the geocoder always returns its nearest guess; these are what it gave for text that isn't that address
    geocoder_says(monkeypatch, "218 PENNSYLVANIA AVENUE, Brooklyn, NY, USA", "218")
    with pytest.raises(building.AddressNotFound):
        building.geocode("1600 Pennsylvania Avenue, Washington DC")
    geocoder_says(monkeypatch, "PS/IS 217 ROOSEVELT ISLAND, New York, NY, USA", None)
    with pytest.raises(building.AddressNotFound):
        building.geocode("is my landlord allowed to do this")
