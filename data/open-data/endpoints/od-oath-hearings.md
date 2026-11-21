# OATH Hearings Division Case Status

## Dataset name

OATH Hearings Division Case Status (NYC Office of Administrative Trials and Hearings). Summonses filed by city enforcement agencies and adjudicated at OATH, with infraction, decision, payments and penalties (dataset description).

## Dataset ID

`jz4z-kudi`. Portal page: https://data.cityofnewyork.us/d/jz4z-kudi

## API URL

`https://data.cityofnewyork.us/resource/jz4z-kudi.json` (send `X-App-Token`).
- Metadata: `raw/od-oath-hearings-metadata.json`. Data dictionary: `raw/od-oath-hearings-dict-oath-hearings-division-case-status-data-dictionary.xlsx` (text in `text/`).
- Update frequency (metadata): Daily.

## Key fields

- `ticket_number`, `issuing_agency` (e.g. "SANITATION OTHERS", "PCS - DOHMH" seen for a demo lot), `violation_date`
- `violation_location_borough` (borough name in capitals), `violation_location_block_no` (text, 5 digits zero-padded), `violation_location_lot_no` (text, 4 digits zero-padded), `violation_location_house`, `violation_location_street_name`
- `hearing_status`, `hearing_result`, `hearing_date`, `decision_date`
- `charge_1_code`, `charge_1_code_section`, `charge_1_code_description`, `charge_1_infraction_amount` (up to several charges)
- `penalty_imposed`, `paid_amount`, `balance_due`, `compliance_status`
- `respondent_last_name` (often an LLC; can be a person)

## Example query

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/jz4z-kudi.json?\$where=violation_location_borough='BRONX'%20AND%20violation_location_block_no='02514'%20AND%20violation_location_lot_no='0062'&\$limit=5"
```

(Demo lot 122 West 167th Street, Bronx: 3.9 s; 5 rows returned at the limit.)

## Example response row

```json
{"ticket_number":"080111672Y","violation_date":"2026-11-09T00:00:00.000","violation_time":"08:47:00","issuing_agency":"SANITATION OTHERS","respondent_last_name":"[redacted in this doc]","balance_due":"50","violation_location_borough":"BRONX","violation_location_block_no":"02514","violation_location_lot_no":"0062","violation_location_house":"122","violation_location_street_name":"WEST 167 STREET","violation_location_zip_code":"10452","hearing_status":"NEW ISSUANCE","hearing_date":"2027-02-22T00:00:00.000","total_violation_amount":"50","penalty_imposed":"50","paid_amount":"0","compliance_status":"Penalty Due","charge_1_code":"AS26","charge_1_code_section":"A.C.","charge_1_code_description":"FAILURE TO CLEAN 18 INCHES INTO STREET","charge_1_infraction_amount":"50"}
```

## Caveats

- Dataset note: "As of May 4, 2026, the Respondent First Name, Respondent Address (Street Name), Respondent Address (City), and Respondent Address (State Name) fields have been removed from this dataset."
- Block and lot are zero-padded text, unlike most other datasets.
- DOB summonses also appear in DOB ECB Violations (`od-dob-ecb-violations.md`), which has DOB-specific fields.
- HPD Housing Maintenance Code violations are not OATH summonses; they are in `wvxf-dwi5`.
- License and rate limits: as for all NYC Open Data datasets (see `od-hpd-violations.md`, Caveats).
