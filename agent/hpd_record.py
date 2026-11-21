"""Pull one building's public HPD record from NYC Open Data and print it as JSON.

    python hpd_record.py <10-digit BBL>

Standard library only, no API key, so it runs anywhere (including the case file agent's sandbox).
Everything here is public record published by the city under Admin Code § 23-502.
"""
import json
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, timedelta

BASE = "https://data.cityofnewyork.us/resource/{}.json?"
PLUTO, VIOLATIONS, COMPLAINTS, REGISTRATIONS, CONTACTS = "64uk-42ks", "wvxf-dwi5", "ygpa-z7cr", "tesw-yqqr", "feu5-w2e2"


def get(dataset: str, **params) -> list:
    url = BASE.format(dataset) + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "case-file"}), timeout=40) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 - retry any transport error, then report it in the output
            if attempt == 2:
                return [{"_error": f"{type(e).__name__}: {e}"}]
    return []


def main(bbl: str) -> dict:
    boro, block, lot = bbl[0], int(bbl[1:6]), int(bbl[6:])
    since = (date.today() - timedelta(days=730)).isoformat()
    pluto = get(PLUTO, **{"$where": f"bbl = {int(bbl)}",
                          "$select": "address,yearbuilt,unitsres,unitstotal,bldgclass,numfloors,ownername"})
    viol = get(VIOLATIONS, **{
        "$where": f"bbl = '{bbl}' AND (inspectiondate >= '{since}' OR violationstatus = 'Open')",
        "$limit": 2000, "$order": "inspectiondate DESC",
        "$select": "violationid,class,ordernumber,novdescription,inspectiondate,approveddate,currentstatus,"
                   "currentstatusdate,violationstatus,apartment,story,rentimpairing"})
    comp = get(COMPLAINTS, **{"$where": f"bbl = {int(bbl)} AND received_date >= '{since}'", "$limit": 5000,
                              "$select": "complaint_id,received_date,apartment,major_category,minor_category,"
                                         "problem_status,status_description"})
    reg = get(REGISTRATIONS, boroid=boro, block=block, lot=lot)
    contacts = []
    if reg and "registrationid" in reg[0]:
        contacts = get(CONTACTS, registrationid=reg[0]["registrationid"],
                       **{"$select": "type,corporationname,firstname,lastname,businesshousenumber,businessstreetname,"
                                     "businesscity,businessstate,businesszip"})
    ok = lambda rows: [r for r in rows if "_error" not in r]
    v, c = ok(viol), ok(comp)
    open_v = [x for x in v if x.get("violationstatus") == "Open"]
    by_category: dict[str, dict] = {}
    for x in c:
        k = x.get("major_category", "?")
        d = by_category.setdefault(k, {"complaints": set(), "apartments": set(), "latest": ""})
        d["complaints"].add(x.get("complaint_id"))
        if x.get("apartment"):
            d["apartments"].add(x["apartment"])
        d["latest"] = max(d["latest"], (x.get("received_date") or "")[:10])
    units = int(float((ok(pluto) or [{}])[0].get("unitsres") or 0))
    return {
        "bbl": bbl,
        "retrieved": date.today().isoformat(),
        "building": (ok(pluto) or [{}])[0],
        "registration": {
            "registered": bool(ok(reg)),
            "ends": (ok(reg)[0].get("registrationenddate") or "")[:10] if ok(reg) else None,
            "contacts": ok(contacts),
        },
        "violations": {
            "window": f"inspected since {since}, plus anything still open",
            "open_total": len(open_v),
            "open_by_class": dict(sorted(Counter(x.get("class") for x in open_v).items())),
            "open_by_order": dict(Counter(x.get("ordernumber") for x in open_v).most_common(25)),
            "rent_impairing_open": sum(1 for x in open_v if str(x.get("rentimpairing", "")).upper().startswith("Y")),
            "rows": [{"id": x.get("violationid"), "class": x.get("class"), "order": x.get("ordernumber"),
                      "inspected": (x.get("inspectiondate") or "")[:10], "status": x.get("currentstatus"),
                      "status_date": (x.get("currentstatusdate") or "")[:10], "open": x.get("violationstatus") == "Open",
                      "apartment": x.get("apartment"), "description": (x.get("novdescription") or "").strip()[:300]}
                     for x in v[:400]],
        },
        "complaints_last_two_years": {
            "total": len({x.get("complaint_id") for x in c}),
            "by_category": {k: {"complaints": len(d["complaints"]), "apartments": len(d["apartments"]), "latest": d["latest"]}
                            for k, d in sorted(by_category.items(), key=lambda kv: -len(kv[1]["complaints"]))},
        },
        "one_third_of_units": -(-units // 3) if units else None,
        "errors": [r["_error"] for rows in (pluto, viol, comp, reg, contacts) for r in rows if "_error" in r],
    }


if __name__ == "__main__":
    if len(sys.argv) != 2 or not (sys.argv[1].isdigit() and len(sys.argv[1]) == 10):
        sys.exit("usage: python hpd_record.py <10-digit BBL>")
    print(json.dumps(main(sys.argv[1]), indent=1))
