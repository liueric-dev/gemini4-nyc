# DOB Violations

## Dataset name

DOB Violations (Department of Buildings (DOB)).

This data set includes older civil penalties (commonly referred to as ‘DOB Violations’) that were issued by the Department of Buildings (DOB) in the Buildings Information System (BIS). For newer civil penalties, see the DOB Safety Violations data set (note: some violations are duplicated in both data sets). Separately, summonses that are issued by DOB but adjudicated by OATH/ECB are in the DOB ECB Violations data set.

## Dataset ID

`3h2n-5cm9`. Portal page: https://data.cityofnewyork.us/d/3h2n-5cm9

## API URL

`https://data.cityofnewyork.us/resource/3h2n-5cm9.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Every weekday; automated: Yes; rows last updated 2026-11-20 13:43.
- Metadata saved: `raw/od-dob-violations-metadata.json`.
- Data dictionary: `raw/od-dob-violations-dict-dd-dob-violations-2019-03-19.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `isn_dob_bis_viol` | text |  |
| `boro` | text |  |
| `bin` | text |  |
| `block` | text |  |
| `lot` | text |  |
| `issue_date` | text |  |
| `violation_type_code` | text |  |
| `violation_number` | text |  |
| `violation_category` | text |  |
| `violation_type` | text |  |
| `description` | text |  |
| `disposition_date` | text |  |
| `disposition_comments` | text |  |
| `ecb_number` | text |  |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/3h2n-5cm9.json?%24where=bin%3D%272001261%27&%24limit=50000"
```

Decoded: `$where=bin='2001261'&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 0 rows, 0.419 s.

## Example response row

(From demo building `3906-114-st-qn`.)

```json
{
 "isn_dob_bis_viol": "22253",
 "boro": "4",
 "bin": "4044993",
 "block": "01786",
 "lot": "00017",
 "issue_date": "19881115",
 "violation_type_code": "E",
 "violation_number": "1161D/07",
 "house_number": "39-06",
 "street": "114 ST",
 "disposition_date": "19900907",
 "device_number": "4P4399",
 "description": "11)PROPERLY SECURE ALARM BUTTON IN BUTTON PANEL 51)PROVIDE LIGHT                ON TOP OF CAR 52)REPLACE SPLICE BOX COVERS ON TOP OF CAR 53)FILE A BN           FOR CAR 53)FILE A BN FOR NEW BRAKE INSTALLED AND HAVE SAME TESTED BY            THIS DEPT",
 "number": "V*111588E1161D/07",
 "violation_category": "V*-DOB VIOLATION - Resolved",
 "violation_type": "E-ELEVATOR                                                        ELEVATORREQUIRED"
}
```

## Caveats

- Older civil penalties issued in BIS; newer ones are in DOB Safety Violations (855j-jady), and some appear in both (dataset description).
- `issue_date` is text; check the format in the example row.
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
