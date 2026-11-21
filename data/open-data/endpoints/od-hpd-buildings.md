# Buildings Subject to HPD Jurisdiction

## Dataset name

Buildings Subject to HPD Jurisdiction (Department of Housing Preservation and Development (HPD)).

Pursuant to New York City’s Housing Maintenance Code, the Department of Housing Preservation and Development (HPD) collects information on multiple dwellings in New York City, and other buildings that fall under its jurisdiction. HPD’s Buildings Open Data covers all buildings which meet any of the following criteria: a. HPD has required the owner to register the building under the Housing Maintenance Code (HMC) b. HPD has initiated a litigation action under the HMC c. HPD has received a complaint for the building d. HPD has initiated a work order for the purposes of emergency repair, demolition, or the Alternative Enforcement Program (AEP) for the building e. HPD has added the property to the AEP program Buildings are identified by a BuildingID.

## Dataset ID

`kj4p-ruqc`. Portal page: https://data.cityofnewyork.us/d/kj4p-ruqc

## API URL

`https://data.cityofnewyork.us/resource/kj4p-ruqc.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-05 15:21.
- Metadata saved: `raw/od-hpd-buildings-metadata.json`.
- Data dictionary: `raw/od-hpd-buildings-dict-hpd-building-open-data.pdf` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `buildingid` | number | Unique identifier of building |
| `boroid` | number | Unique number identifying a borough |
| `block` | number | Tax block for building |
| `lot` | number | Tax lot for building |
| `bin` | number | DCP Building Identification Number for building |
| `housenumber` | text | Address information for the building |
| `streetname` | text | Address information for the building |
| `managementprogram` | text | Contains the current active management program which determines who is responsible for the management of this building |
| `dobbuildingclass` | text | Stores DoB building classification codes as augmented by HPD for other than Multiple Dwellings (see DoBBuildingClass below) |
| `legalstories` | number | Number of legal stories in building |
| `legalclassa` | number | The number of apartments in a multiple dwelling |
| `legalclassb` | number | The number of rooms in a multiple dwelling without individual baths and kitchens |
| `registrationid` | number | Multiple dwelling registration number, used by HPD in the master building file to identify a building |
| `lifecycle` | text | The stage in the building life cycle |
| `recordstatus` | text | "The numeric value of the status of this building code (1 = Active, 2 = Inactive, 3 = Pending)" |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/kj4p-ruqc.json?%24where=boroid%3D2+AND+block%3D2370+AND+lot%3D5&%24limit=50000"
```

Decoded: `$where=boroid=2 AND block=2370 AND lot=5&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 1 rows, 8.98 s.

## Example response row

```json
{
 "buildingid": "119624",
 "boroid": "2",
 "boro": "BRONX",
 "housenumber": "1048",
 "lowhousenumber": "1048",
 "highhousenumber": "1048",
 "streetname": "WASHINGTON AVENUE",
 "zip": "10456",
 "block": "2370",
 "lot": "5",
 "bin": "2001261",
 "communityboard": "3",
 "censustract": "18501",
 "managementprogram": "PVT",
 "dobbuildingclassid": "7",
 "dobbuildingclass": "HERETOFORE CONVERTED CLASS A",
 "legalstories": "3",
 "legalclassa": "3",
 "legalclassb": "0",
 "registrationid": "210568",
 "lifecycle": "Building",
 "recordstatusid": "1",
 "recordstatus": "Active"
}
```

## Caveats

- Covers buildings HPD has a reason to track: registration required, litigation, a complaint, a work order or AEP (dataset description). It is not a list of all buildings.
- One BBL can have several HPD building records (the rent-stabilized demo building returned 3).
- `managementprogram` was `PVT` for the private demo buildings (see the NYCHA demo for the NYCHA value); `legalclassa` is the legal count of class A units.
- No `bbl` column; query by `boroid`, `block`, `lot` (all numbers) or by `bin`.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
