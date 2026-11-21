# DOB ECB Violations

## Dataset name

DOB ECB Violations (Department of Buildings (DOB)).

This data set includes summonses issued by the Department of Buildings that are adjudicated by OATH/ECB. Separately, civil penalties (commonly referred to as ‘DOB Violations’) are found in the DOB Safety Violations (for newer issuances) and DOB Violations (for older issuances) data sets.

## Dataset ID

`6bgk-3dad`. Portal page: https://data.cityofnewyork.us/d/6bgk-3dad

## API URL

`https://data.cityofnewyork.us/resource/6bgk-3dad.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Every weekday; automated: Yes; rows last updated 2026-11-20 13:18.
- Metadata saved: `raw/od-dob-ecb-violations-metadata.json`.
- Data dictionary: `raw/od-dob-ecb-violations-dict-dd-dob-ecb-violations-2019-07-10.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `ecb_violation_number` | text |  |
| `ecb_violation_status` | text |  |
| `dob_violation_number` | text |  |
| `bin` | text |  |
| `issue_date` | text |  |
| `severity` | text |  |
| `violation_type` | text |  |
| `violation_description` | text |  |
| `penality_imposed` | number |  |
| `balance_due` | number |  |
| `infraction_code1` | text |  |
| `section_law_description1` | text |  |
| `hearing_status` | text |  |
| `certification_status` | text |  |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/6bgk-3dad.json?%24where=bin%3D%272001261%27&%24limit=50000&%24select=ecb_violation_number%2Cecb_violation_status%2Cdob_violation_number%2Cbin%2Cboro%2Cblock%2Clot%2Cissue_date%2Cseverity%2Cviolation_type%2Cviolation_description%2Cpenality_imposed%2Cbalance_due%2Cinfraction_code1%2Csection_law_description1%2Chearing_status%2Ccertification_status"
```

Decoded: `$where=bin='2001261'&$limit=50000&$select=ecb_violation_number,ecb_violation_status,dob_violation_number,bin,boro,block,lot,issue_date,severity,violation_type,violation_description,penality_imposed,balance_due,infraction_code1,section_law_description1,hearing_status,certification_status`

Result on 2026-11-21T00:57: HTTP 200, 3 rows, 2.546 s.

## Example response row

```json
{
 "ecb_violation_number": "39202893P",
 "ecb_violation_status": "ACTIVE",
 "bin": "2001261",
 "boro": "2",
 "block": "02370",
 "lot": "0005",
 "issue_date": "20260902",
 "severity": "CLASS - 2",
 "violation_type": "Construction",
 "violation_description": "CONTRARY TO C-OF-O # 89 WHICH INDICATES PREMISES AS 3 STORY, 2 FAMILY & STORE DWELLING: AT TIME OF INSPECTION BUILDING WAS OBSERVED CREATED & OCCUPIED AS A 3 FAMILY NFP DWELLING WITH CLASS 'A' APTS AT 1ST, 2ND,",
 "penality_imposed": "1250",
 "balance_due": "1250",
 "infraction_code1": "203",
 "section_law_description1": "28-118.3.2                                                                  OCC CONTRARY TO THAT ALLOWED BY THE C OF O OR DOB RECORDS",
 "hearing_status": "PENDING"
}
```

## Caveats

- DOB summonses adjudicated by OATH/ECB (dataset description). Summonses from other agencies (e.g. Sanitation, DOHMH) are in OATH Hearings (jz4z-kudi, `od-oath-hearings.md`).
- `issue_date` is text in YYYYMMDD form (e.g. `20260902`).
- `respondent_name` and respondent address fields name owners; the demo query selected only non-name fields.
- Updated every weekday (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
