# Registration Contacts

## Dataset name

Registration Contacts (Department of Housing Preservation and Development (HPD)).

Contains information about organizations or individuals listed on a Multiple Dwelling Registration form.

## Dataset ID

`feu5-w2e2`. Portal page: https://data.cityofnewyork.us/d/feu5-w2e2

## API URL

`https://data.cityofnewyork.us/resource/feu5-w2e2.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Monthly; automated: Yes; rows last updated 2026-11-04 13:50.
- Metadata saved: `raw/od-hpd-registration-contacts-metadata.json`.
- Data dictionary: `raw/od-hpd-registration-contacts-dict-registration-data-dictionary.pdf` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `registrationcontactid` | number | Unique identifier of RegistrationContact |
| `registrationid` | number | Unique identifier of owning Registration |
| `type` | text | "Individual Owner", "Corporate Owner", "Managing Agent", "Head Officer", "Officer", "Shareholder" |
| `contactdescription` | text | Description of contact |
| `corporationname` | text | If applicable |
| `title` | text | Contact person information |
| `firstname` | text | Contact person information |
| `lastname` | text | Contact person information |
| `businesshousenumber` | text | Contact address information |
| `businessstreetname` | text | Contact address information |
| `businesscity` | text | Contact address information |
| `businessstate` | text | Contact address information |
| `businesszip` | text | Contact address information |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/feu5-w2e2.json?%24where=registrationid+in+%28210568%29&%24limit=5000"
```

Decoded: `$where=registrationid in (210568)&$limit=5000`

Result on 2026-11-21T00:57: HTTP 200, 4 rows, 0.358 s.

## Example response row

```json
{
 "registrationcontactid": "21056803",
 "registrationid": "210568",
 "type": "CorporateOwner",
 "contactdescription": "GEN.PART",
 "corporationname": "[redacted in this doc]",
 "businesshousenumber": "1702",
 "businessstreetname": "EAST 5TH STREET",
 "businessapartment": "3RD FL",
 "businesscity": "Brooklyn",
 "businessstate": "NY",
 "businesszip": "11223"
}
```

## Caveats

- `type` values seen for demo building 1048 Washington Ave: Agent, CorporateOwner, HeadOfficer, SiteManager. Building a landlord portfolio means grouping registrations by `corporationname` or by the business address of the head officer or agent; names are free text and inconsistently spelled.
- Contains names of individual owners and officers (not tenants). The example row below is redacted in this doc.
- Updated monthly (metadata).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
