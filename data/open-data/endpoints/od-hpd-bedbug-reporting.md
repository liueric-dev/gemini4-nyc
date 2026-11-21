# Bedbug Reporting

## Dataset name

Bedbug Reporting (Department of Housing Preservation and Development (HPD)).

Property owners are required to obtain bedbug infestation history from tenants or a dwelling unit owner. This dataset captures the bedbug infestation history as reported by the property owner. Local Law 69 of 2017 requires that all multiple dwelling property owners must attempt to obtain the bed bug infestation history from the tenant or unit owner, including whether eradication measures were employed for a bedbug infestation. The information reported in this file is self-reported information filed annually by property owners. Once the Bed Bug Annual Report has been filed, the property owner is required to either provide the filing receipt to each tenant (upon commencement of a new lease and with each lease renewal) OR post the filing receipt in a prominent location in the building. In addition, the property owner must either distribute to each tenant or post the DOHMH Preventing and Getting Rid of Bedbugs Safely guide, which provides information on the prevention, detection, and removal of bedbugs. Each record in the file represents a filing completed. If a property has submitted two records for the same period, the second filing is the active final submission for the period.

## Dataset ID

`wz6d-d3jb`. Portal page: https://data.cityofnewyork.us/d/wz6d-d3jb

## API URL

`https://data.cityofnewyork.us/resource/wz6d-d3jb.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-15 17:55.
- Metadata saved: `raw/od-hpd-bedbug-reporting-metadata.json`.
- Data dictionary: `raw/od-hpd-bedbug-reporting-dict-bedbug-reporting-data-dictionary.xlsx` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `building_id` | text | Unique identifier of building |
| `registration_id` | text | Unique identifier of valid registration information |
| `bbl` | text | The BBL (Borough, Block, and Lot) is a unique identifier for each tax lot in the City. |
| `bin` | text | The BIN (Building Identification Number) is a unique identifier for each building in the City. |
| `of_dwelling_units` | number | Total unit count in the building on file with HPD. |
| `infested_dwelling_unit_count` | number | Number of units in the building that had bedbugs during the reporting period, as reported by the building owner. |
| `eradicated_unit_count` | number | Number of units in the building where bedbugs had been eradicated but had returned after treatment, as reported by the building owner. |
| `re_infested_dwelling_unit` | number | Number of units in the building where bedbugs had been eradicated, as reported by the building owner. |
| `filing_date` | calendar_date | Filing date of the report. |
| `filing_period_start_date` | calendar_date | Start of the period for which the owner is reporting results. |
| `filling_period_end_date` | calendar_date | End of the period for which the owner is reporting results. |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/wz6d-d3jb.json?%24where=bbl%3D%272023700005%27&%24limit=50000"
```

Decoded: `$where=bbl='2023700005'&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 6 rows, 4.022 s.

## Example response row

```json
{
 "building_id": "119624",
 "registration_id": "210568",
 "borough": "BRONX",
 "house_number": "1048",
 "street_name": "WASHINGTON AVENUE",
 "postcode": "10456",
 "of_dwelling_units": "3",
 "infested_dwelling_unit_count": "0",
 "eradicated_unit_count": "0",
 "re_infested_dwelling_unit": "0",
 "filing_date": "2023-12-04T00:00:00.000",
 "filing_period_start_date": "2022-11-01T00:00:00.000",
 "filling_period_end_date": "2023-10-31T00:00:00.000",
 "latitude": "40.827336",
 "longitude": "-73.909084",
 "community_board": "3",
 "city_council_district": "16",
 "census_tract_2010": "18501",
 "bin": "2001261",
 "bbl": "2023700005",
 "nta": "Morrisania"
}
```

## Caveats

- Self-reported annual filings by owners under Local Law 69 of 2017 (dataset description). Counts are as reported, not inspected.
- Note the misspelt field `filling_period_end_date`.
- Updated monthly (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
