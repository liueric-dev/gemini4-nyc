# NOAA Climate Data Online (CDO) web services v2

## Dataset name

NOAA NCEI Climate Data Online API v2.

## Dataset ID

Central Park as GHCND station `GHCND:USW00094728`.

## API URL

- `https://www.ncei.noaa.gov/cdo-web/api/v2/datasets` (also `/data`, `/stations`, `/datatypes`)
- Header `token: $NOAA_CDO_TOKEN` (free key)
- Docs: https://www.ncdc.noaa.gov/cdo-web/webservices/v2 (`text/od-noaa-cdo-v2-docs.md`)

## Key fields

`/datasets` results: `id`, `name`, `mindate`, `maxdate`, `datacoverage`.

## Example query

```
curl -H "token: $NOAA_CDO_TOKEN" "https://www.ncei.noaa.gov/cdo-web/api/v2/datasets?stationid=GHCND:USW00094728&limit=100"
```

Saved: `raw/od-noaa-cdo-datasets.json` (all datasets), `raw/od-noaa-cdo-datasets-knyc.json` (datasets for Central Park).

## Example response row

```
GHCND | Daily Summaries | 1763-01-01 -> 2026-11-15
NORMAL_HLY | Normals Hourly | 2010-01-01 -> 2010-12-31
```

## How far back and how recent

Datasets the API lists (2026-11-21): `GHCND` Daily Summaries to 2026-11-15, `GSOM`, `GSOY`, `NEXRAD2`/`NEXRAD3` radar, `NORMAL_*` (2010 normals only), `PRECIP_15` and `PRECIP_HLY` (to 2014). Central Park has GHCND, GSOM, GSOY and the 2010 normals (no hourly normals listed for this station).

## License

US government work; no licence statement found in the docs page fetched. The docs page fetched did not state the request limits.

## Caveats

- **No hourly observed temperature**, which confirms the README. It is useful only for daily max/min (GHCND), if that is ever needed.
- Response time about 0.24 s.
