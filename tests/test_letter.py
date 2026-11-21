"""The letter draft, built from a saved analysis shape. No network calls."""
from pathlib import Path

import pytest

from app import db as dbm
from app import letter

ANALYSIS = {
    "building": {"address": "39-06 114 STREET, North Corona, NY, USA", "owner": "39-06 114 ST REALTY LLC"},
    "findings": [
        {"problem_type": "mold", "title": "Mould", "outcome": "violation", "rule_id": "EO-008", "class": "B",
         "class_meaning": "Hazardous", "deadline": {"value": 30, "unit": "days", "text": "30 days from mailing of notice"},
         "description": "Dark mould across the lower wall.", "where": "Lower half of the wall",
         "citations": [{"section_id": "nyc-hmc-27-2017-3", "citation": "NYC Admin Code § 27-2017.3",
                        "quote": "shall constitute a hazardous violation"}]},
        {"problem_type": "leak", "title": "Leaks", "outcome": "inspector_decides", "rule_id": "EO-001", "class": None,
         "class_options": ["A", "B", "C"], "deadline": {"value": None, "unit": None, "text": "by assigned class"},
         "description": "Water staining at the baseboard.", "where": "", "citations": []},
        {"problem_type": "mold", "title": "Mould", "outcome": "not_landlord_responsibility", "rule_id": "EO-015",
         "description": "Surface mould on grout.", "citations": []},
    ],
}


@pytest.fixture(autouse=True)
def use_test_db(db, monkeypatch):
    """Point the letter code at the throwaway test database instead of var/tenant.db."""
    test_file = Path(db.execute("PRAGMA database_list").fetchone()[2])
    real_connect = dbm.connect
    monkeypatch.setattr(dbm, "connect", lambda path=None: real_connect(test_file))


def test_letter_states_only_what_the_analysis_found():
    out = letter.draft(ANALYSIS, tenant_name="A. Tenant", apartment="4B")
    text = out["letter"]
    assert "39-06 114 ST REALTY LLC" in text and "Apartment 4B" in text and "A. Tenant" in text
    assert "Class B (hazardous) violation" in text and "the owner has 30 days to correct it" in text
    assert '"shall constitute a hazardous violation"' in text
    assert "inspector assigns the class (A, B or C)" in text
    assert "grout" not in text  # the tenant's own duty is not put to the landlord
    assert "Real Property Law § 223-b" in text
    assert out["findings_included"] == ["mold", "leak"]
    assert "apartment 4B" in out["complaint_311"]


def test_letter_leaves_blanks_for_what_it_does_not_know():
    out = letter.draft({"findings": ANALYSIS["findings"][:1]})
    assert "[apartment number]" in out["letter"] and "[Your name]" in out["letter"] and "[building address]" in out["letter"]


def test_no_letter_when_nothing_is_the_landlords_to_fix():
    with pytest.raises(ValueError):
        letter.draft({"findings": ANALYSIS["findings"][2:]})
