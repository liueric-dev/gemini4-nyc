"""Shared fixture: a throwaway copy of the database, built once per test run."""
import importlib.util
from pathlib import Path

import pytest

from app import db as dbm

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    spec = importlib.util.spec_from_file_location("build_db", ROOT / "scripts/build_db.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    path = tmp_path_factory.mktemp("db") / "tenant.db"
    counts = mod.build(path)
    assert counts["rules"] == 92
    assert counts["sections"] > 1000
    assert counts["hpd_orders"] == 400
    conn = dbm.connect(path)
    yield conn
    conn.close()
