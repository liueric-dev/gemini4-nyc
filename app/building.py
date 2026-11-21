"""Building lookup: a typed NYC address to the facts the decision rules need.

    lookup("122 West 167th Street, Bronx") -> {bbl, address, year_built, units_res, building_kind,
                                               rent_stabilized, open_violations, ...}

Sources, all live and free to use (NYC Open Data, Admin Code § 23-502(d)): NYC GeoSearch for the address,
PLUTO for year built and units, HPD for open violations and registration. The rent-stabilized list is a
local file that exists only where data collection ran; without it the answer is "unknown".
Results are cached for a day in var/runtime.db, which is separate from the rebuilt var/tenant.db.
"""
import csv
import json
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

import httpx

from app import config

GEOSEARCH = "https://geosearch.planninglabs.nyc/v2/search"
SODA = "https://data.cityofnewyork.us/resource/{}.json"
PLUTO, VIOLATIONS, REGISTRATIONS = "64uk-42ks", "wvxf-dwi5", "tesw-yqqr"
RS_LIST = config.DATA / "open-data/local/od-dhcr-rs-buildings-2025.csv"
RUNTIME_DB = config.VAR / "runtime.db"
CACHE_SECONDS = 24 * 3600
ATTRIBUTION = (
    "Building data: NYC GeoSearch and PLUTO (Department of City Planning), HPD violations and registrations "
    "(NYC Open Data), DHCR 2025 building registration file via the Rent Guidelines Board."
)


class AddressNotFound(Exception):
    pass


def _soda(dataset: str, params: dict) -> list[dict]:
    r = httpx.get(SODA.format(dataset), params=params, timeout=30,
                  headers={"X-App-Token": config.key("NYC_OPENDATA_APP_TOKEN")})
    r.raise_for_status()
    return r.json()


def geocode(address: str) -> dict:
    r = httpx.get(GEOSEARCH, params={"text": address, "size": 1}, timeout=15)
    r.raise_for_status()
    features = r.json().get("features") or []
    if not features:
        raise AddressNotFound(address)
    p = features[0]["properties"]
    pad = (p.get("addendum") or {}).get("pad") or {}
    if not pad.get("bbl"):
        raise AddressNotFound(address)
    return {"bbl": pad["bbl"], "bin": pad.get("bin"), "address": p.get("label"), "borough": p.get("borough"),
            "match_confidence": p.get("confidence")}


def building_kind(units_res: int | None, owner: str | None, building_class: str | None) -> str | None:
    """Map PLUTO facts to the building kinds the decision rules use. None means unknown."""
    if owner and "HOUSING AUTHORITY" in owner.upper():
        return "nycha"
    if building_class and building_class.upper().startswith("R") and building_class.upper() not in ("RR",):
        return "condo"
    if units_res is None:
        return None
    if units_res >= 3:
        return "multiple_dwelling"
    if units_res >= 1:
        return "one_two_family"
    return None


@lru_cache(maxsize=1)
def _rent_stabilized_bbls() -> frozenset[str] | None:
    if not RS_LIST.exists():
        return None
    with RS_LIST.open(encoding="utf-8") as fh:
        return frozenset(row["bbl"] for row in csv.DictReader(fh))


def _int(v) -> int | None:
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _fetch(bbl: str) -> dict:
    boro, block, lot = bbl[0], int(bbl[1:6]), int(bbl[6:])
    with ThreadPoolExecutor(max_workers=3) as pool:
        pluto = pool.submit(_soda, PLUTO, {
            "$where": f"bbl = {int(bbl)}",
            "$select": "address,yearbuilt,unitsres,unitstotal,bldgclass,numfloors,ownername,numbldgs"})
        viols = pool.submit(_soda, VIOLATIONS, {
            "bbl": bbl, "violationstatus": "Open", "$limit": 1000, "$order": "inspectiondate DESC",
            "$select": "violationid,class,ordernumber,novdescription,inspectiondate,currentstatus,apartment,story,rentimpairing"})
        reg = pool.submit(_soda, REGISTRATIONS, {"boroid": boro, "block": block, "lot": lot})
        p = (pluto.result() or [{}])[0]
        v, r = viols.result(), reg.result()
    units = _int(p.get("unitsres"))
    year = _int(p.get("yearbuilt")) or None
    by_class: dict[str, int] = {}
    for x in v:
        by_class[x.get("class", "?")] = by_class.get(x.get("class", "?"), 0) + 1
    rs = _rent_stabilized_bbls()
    return {
        "bbl": bbl,
        "year_built": year,
        "units_res": units,
        "units_total": _int(p.get("unitstotal")),
        "floors": _int(p.get("numfloors")),
        "building_class": p.get("bldgclass"),
        "owner": p.get("ownername"),
        "building_kind": building_kind(units, p.get("ownername"), p.get("bldgclass")),
        "rent_stabilized": None if rs is None else bbl in rs,
        "hpd_registered": bool(r),
        "hpd_registration_ends": (r[0].get("registrationenddate") or "")[:10] or None if r else None,
        "open_violations": {
            "total": len(v),
            "by_class": dict(sorted(by_class.items())),
            "rent_impairing": sum(1 for x in v if str(x.get("rentimpairing", "")).upper().startswith("Y")),
            "recent": [
                {"class": x.get("class"), "order": x.get("ordernumber"), "date": (x.get("inspectiondate") or "")[:10],
                 "apartment": x.get("apartment"), "status": x.get("currentstatus"),
                 "description": (x.get("novdescription") or "").strip()}
                for x in v[:25]
            ],
        },
        "facts": {"year_built": year},
        "attribution": ATTRIBUTION,
    }


def _cache() -> sqlite3.Connection:
    config.VAR.mkdir(exist_ok=True)
    db = sqlite3.connect(RUNTIME_DB)
    db.execute("CREATE TABLE IF NOT EXISTS building_cache (bbl TEXT PRIMARY KEY, fetched_at REAL, body TEXT)")
    return db


def lookup(address: str, use_cache: bool = True) -> dict:
    """Address to building facts. Raises AddressNotFound if GeoSearch has no match."""
    start = time.perf_counter()
    geo = geocode(address)
    db = _cache()
    try:
        row = db.execute("SELECT fetched_at, body FROM building_cache WHERE bbl = ?", (geo["bbl"],)).fetchone()
        if use_cache and row and time.time() - row[0] < CACHE_SECONDS:
            body, cached = json.loads(row[1]), True
        else:
            body, cached = _fetch(geo["bbl"]), False
            db.execute("INSERT OR REPLACE INTO building_cache VALUES (?,?,?)",
                       (geo["bbl"], time.time(), json.dumps(body)))
            db.commit()
    finally:
        db.close()
    return {**geo, **body, "cached": cached, "seconds": round(time.perf_counter() - start, 2)}
