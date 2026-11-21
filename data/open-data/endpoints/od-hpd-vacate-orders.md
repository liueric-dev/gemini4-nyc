# Order to Repair/Vacate Orders

## Dataset name

Order to Repair/Vacate Orders (Department of Housing Preservation & Development (HPD)).

Order to Repair/Vacate Orders

## Dataset ID

`tb8q-a3ar`. Portal page: https://data.cityofnewyork.us/d/tb8q-a3ar

## API URL

`https://data.cityofnewyork.us/resource/tb8q-a3ar.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Daily; automated: Yes; rows last updated 2026-11-20 16:50.
- Metadata saved: `raw/od-hpd-vacate-orders-metadata.json`.
- Data dictionary: `raw/od-hpd-vacate-orders-dict-hpd-vacate-orders-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `building_id` | number | The Building ID is a unique numeric identifier assigned to each building by HPD |
| `registration_id` | text | The Registration ID is a number assigned to residential buildings as per the Housing Maintenance Code. All multiple dwellings (3 units or more) are required to have a registration number (the first digit of the number is the borough in which the building is located). Private dwellings are assigned a |
| `bbl` | number | The BBL (Borough, Block, and Lot) is a unique identifier for each tax lot in the City. |
| `bin` | number | The BIN (Building Identification Number) is a unique identifier for each building in the City. |
| `vacate_order_number` | number | Unique number to identify each Vacate Order |
| `primary_vacate_reason` | text | Primary reason the unit/building is vacated. |
| `vacate_type` | text | Area affected by the vacate. |
| `vacate_effective_date` | calendar_date | The date the Order to Repair/Vacate Order was made effective. |
| `actual_rescind_date` | calendar_date | The date the Order to Repair/Vacate Order was rescinded. |
| `number_of_vacated_units` | number | Number of units vacated. |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/tb8q-a3ar.json?%24where=bbl%3D2023700005&%24limit=50000"
```

Decoded: `$where=bbl=2023700005&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 1 rows, 2.415 s.

## Example response row

```json
{
 "building_id": "119624",
 "registration_id": "210568",
 "boro_short_name": "BX",
 "house_number": "1048",
 "street_name": "WASHINGTON AVENUE",
 "vacate_order_number": "260643",
 "primary_vacate_reason": "Fire Damage",
 "vacate_type": "Entire Building",
 "vacate_effective_date": "2026-04-20T00:00:00.000",
 "number_of_vacated_units": "3",
 "postoce": "10456",
 "latitude": "40.827336000000003",
 "longitude": "-73.909083999999993",
 "community_board": "3",
 "council_district": "16",
 "census_tract": "18501",
 "bin": "2001261",
 "bbl": "2023700005",
 "nta": "Morrisania"
}
```

## Caveats

- HPD vacate orders only. FDNY has its own vacate list (n5xc-7jfa) and DOB vacates are not here.
- Dataset title is "Order to Repair/Vacate Orders"; updated daily (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
