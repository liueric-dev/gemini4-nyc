# NWS API: station observations, KNYC (Central Park)

## Dataset name

National Weather Service API, station observations for KNYC ("New York City, Central Park", ASOS).

## Dataset ID

Station `KNYC`. Station metadata: `raw/od-nws-station-knyc.json` (coordinates -73.96667, 40.78333; elevation 46.9 m; time zone America/New_York).

## API URL

- `https://api.weather.gov/stations/KNYC/observations?start=<ISO8601>&end=<ISO8601>`
- `https://api.weather.gov/stations/KNYC/observations/latest`
- Docs: https://www.weather.gov/documentation/services-web-api (saved as `raw/od-nws-api-docs.html`, `text/od-nws-api-docs.md`)

No key. The docs ask for a `User-Agent` header that identifies the application (`text/od-nws-api-docs.md`, Authentication section). Send `Accept: application/geo+json`.

## Key fields

Each feature's `properties`:
- `timestamp`: observation time, ISO 8601 with UTC offset (UTC in practice)
- `temperature.value`: air temperature, unit in `temperature.unitCode` (`wmoUnit:degC`)
- `temperature.qualityControl`: QC flag (`V` seen)
- `dewpoint`, `relativeHumidity`, `windChill`, `heatIndex`, `windSpeed`, `textDescription`, `rawMessage` (the METAR)
- `maxTemperatureLast24Hours`, `minTemperatureLast24Hours`

## Example query

```
curl -A "tenant-app (contact)" -H "Accept: application/geo+json" \
  "https://api.weather.gov/stations/KNYC/observations?start=2026-11-20T00:00:00-05:00&end=2026-11-21T00:00:00-05:00"
```

Saved: `raw/od-nws-knyc-observations-2026-11-20.json` (19 observations), `raw/od-nws-knyc-observations-latest.json`, `raw/od-nws-knyc-observations-all-available.json` (`?limit=500`, 130 observations).

## Example response row

```json
{"stationId": "KNYC", "timestamp": "2026-11-21T03:51:00+00:00", "textDescription": "", "temperature": {"unitCode": "wmoUnit:degC", "value": 13.9, "qualityControl": "V"}, "dewpoint": {"unitCode": "wmoUnit:degC", "value": 3.9, "qualityControl": "V"}, "relativeHumidity": {"unitCode": "wmoUnit:percent", "value": 50.90931533382, "qualityControl": "V"}, "windChill": {"unitCode": "wmoUnit:degC", "value": null, "qualityControl": "V"}, "heatIndex": {"unitCode": "wmoUnit:degC", "value": null, "qualityControl": "V"}}
```

## How far back and how recent

- **Only about the last 7 days.** Tested 2026-11-21 00:45 New York time: the unfiltered list (`?limit=500`) returned 130 observations from 2026-11-14T05:29Z to 2026-11-21T03:51Z. Queries for 2026-11-10, 2026-11-07, 2026-11-01, 2026-10-25, 2026-08-01 and 2026-01-15 returned 0 features (HTTP 200, empty list).
- Most recent observation was under an hour old.
- Roughly hourly (the :51 routine report), with some extra special reports.

## License and terms

Docs (Pricing section): "All of the information presented via the API is intended to be open data, free to use for any purpose." Rate limit "is not public information, but allows a generous amount for typical use"; when exceeded, retry "typically within 5 seconds".

## Caveats

- Not usable for clips older than about a week. For older dates use NCEI GHCNh (`od-weather-ncei-ghcnh.md`) or Open-Meteo (`od-weather-open-meteo.md`).
- Values are Celsius; convert for the heat rule.
- Times are UTC; convert to America/New_York before comparing with the time of a clip.
