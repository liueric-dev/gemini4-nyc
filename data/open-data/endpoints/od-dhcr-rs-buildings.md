# DHCR rent-stabilized building lists (2025 registration file, hosted by the Rent Guidelines Board)

## Dataset name

"List of <Borough> Buildings Containing Stabilized Units", source line on each page: "NYS Homes and Community Renewal 2025 Building Registration File". Published as PDFs by the NYC Rent Guidelines Board.

## Dataset ID

No dataset ID. Five PDFs, uploaded 2026-11 (from the URL path):
- `https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2026/11/2025-DHCR-Bldg-File-{Bronx,Brooklyn,Manhattan,Queens,Staten-Island}.pdf`
- Index page: https://rentguidelinesboard.cityofnewyork.us/resources/rent-stabilized-building-lists/ (`local/od-rgb-rent-stabilized-building-lists.html`, `local/od-rgb-rent-stabilized-building-lists.md`)

Saved as `local/od-dhcr-rs-buildings-2025-<borough>.pdf`.

## API URL

None; plain PDF download. Not on NYC Open Data. The catalog search for "rent stabilized" found only Local Law 44 and 485-x datasets.

## Key fields

Converted CSV `local/od-dhcr-rs-buildings-2025.csv` (51,592 rows, 48,021 distinct BBLs):
- `zip`, `bldgno1`, `street1`, `stsufx1`: primary address (`bldgno1` can be a range, e.g. `303 TO 309`)
- `bldgno2`, `street2`, `stsufx2`: second address, if any
- `city`, `county` (DHCR county code: 60 Bronx, 61 Brooklyn, 62 Manhattan, 63 Queens, 64 Staten Island, as observed per file)
- `status1`: `MULTIPLE DWELLING A` or `MULTIPLE DWELLING B`
- `status2`, `status3`: programme flags such as `421-A (1-15)`, `GARDEN COMPLEX`, `HOTEL`, `NON-EVICT COOP/CONDO`, `SECTION 610 OF PHFL`
- `block`, `lot`, plus `bbl` computed as borough code + 5-digit block + 4-digit lot (the borough code comes from which file the row is in)
- `source_file`, `page`: where the row came from in the PDF

## Example query

Look up a BBL in the CSV, e.g. `grep ',1007220003,' local/od-dhcr-rs-buildings-2025.csv`.

## Example response row

```
1,1007220003,10001,246,10TH,AVE,,,,NEW YORK,62,MULTIPLE DWELLING A,,,722,3,od-dhcr-rs-buildings-2025-manhattan.pdf,1
```

## Caveats

- The RGB page: "The lists do not indicate which apartments in these buildings are rent stabilized, but rather, only those buildings that contain at least one rent stabilized unit." A building missing from the list is not proof that no unit is stabilized (unregistered buildings, deregulated units, newer tax-benefit buildings).
- Converted by script (`pymupdf` word positions bucketed under the header columns). Every page of every PDF yielded rows. Rows per page range from 49 to 59, apart from the last pages. Spot-check against the PDF before relying on a row.
- Some BBLs repeat (multiple addresses per lot, or condo billing lots 75xx).
- Condo lots (75xx) are billing BBLs and won't match a PLUTO tax lot directly.
- Licence: no licence statement was found for these NY State (HCR) lists, so the PDFs and the CSV are marked `committable: unsure` and kept in `local/` (git-ignored). Facts about which buildings are registered may be reusable, but that is the project owner's call.
- Live use: the app would ship this CSV and refresh it yearly. There is no API.
