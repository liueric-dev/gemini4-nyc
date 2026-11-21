# HUD USER Fair Market Rents API

## Dataset name

HUD USER Fair Market Rents (FMR) and Income Limits API: FMR for the New York, NY HUD Metro FMR Area.

## Dataset ID

- NYC metro entity: `METRO35620MM5600` ("New York, NY HUD Metro FMR Area"), from `fmr/listMetroAreas` (`raw/od-hud-fmr-list-metro-areas.json`)
- NYC counties (from `fmr/listCounties/NY`, `raw/od-hud-fmr-list-counties-ny.json`): Bronx `3600599999`, Kings `3604799999`, New York `3606199999`, Queens `3608199999`, Richmond `3608599999`

## API URL

- `https://www.huduser.gov/hudapi/public/fmr/data/{entityid}?year={year}` (default is the latest year)
- `https://www.huduser.gov/hudapi/public/fmr/listMetroAreas`, `.../fmr/listCounties/{state}`, `.../fmr/statedata/{state}`
- Header: `Authorization: Bearer $HUD_API_TOKEN` (free key)
- Docs: https://www.huduser.gov/portal/dataset/fmr-api.html (`raw/od-hud-fmr-api-docs.html`, `text/od-hud-fmr-api-docs.md`)
- Terms: https://www.huduser.gov/portal/dataset/api-terms-of-service.html (`text/od-hud-api-terms.md`)

## Key fields

`data.area_name`, `data.metro_name`, `data.counties_msa` (the counties in the FMR area), `data.basicdata.{Efficiency, One-Bedroom, Two-Bedroom, Three-Bedroom, Four-Bedroom}` (monthly dollars), `data.basicdata.year`.

## Example query

```
curl -H "Authorization: Bearer $HUD_API_TOKEN" "https://www.huduser.gov/hudapi/public/fmr/data/METRO35620MM5600?year=2026"
```

## Example response row

```json
{"data": {"county_name": "", "counties_msa": "Bronx County, NY; Kings County, NY; New York County, NY; Putnam County, NY; Queens County, NY; Richmond County, NY; Rockland County, NY; and Westchester County, NY", "town_name": "", "metro_status": "1.0", "metro_name": "New York-Newark-Jersey City, NY-NJ", "area_name": "New York, NY HUD Metro FMR Area", "basicdata": {"Efficiency": 2593, "One-Bedroom": 2729, "Two-Bedroom": 2971, "Three-Bedroom": 3760, "Four-Bedroom": 4121, "year": "2027"}}}
```

## Collected

`text/od-hud-fmr-nyc.csv`: years 2020 to 2027 for the metro area (raw `raw/od-hud-fmr-nyc-metro-<year>.json`). Latest (default) is 2027. All five NYC county queries return the same metro values (`raw/od-hud-fmr-county-*-latest.json`).

| year | 0BR | 1BR | 2BR | 3BR | 4BR |
|---|---|---|---|---|---|
| 2027 | 2593 | 2729 | 2971 | 3760 | 4121 |
| 2026 | 2529 | 2655 | 2910 | 3644 | 3959 |
| 2025 | 2406 | 2511 | 2780 | 3465 | 3738 |
| 2024 | 2386 | 2451 | 2752 | 3434 | 3700 |

## License and terms

- Terms of service: use is allowed to "search, display, analyze, retrieve, view and otherwise 'get' information". Apps should display: "This product uses the HUD User Data API but is not endorsed or certified by HUD User." Limit: "60 queries a min".
- HUD is a federal agency, so the data is a US government work.

## Caveats

- `year` is the year the API returns. These are HUD fiscal-year FMRs; the API response doesn't state an effective date, so take it from HUD's FMR documentation before using it for the Good Cause test.
- The FMR area is wider than NYC. It also includes Putnam and Rockland, and Westchester since 2025, so the metro FMR is not NYC-only.
- The 2027 figures are present, so the "current" year depends on the date the app checks.
- Response time about 0.26 to 0.40 s.
