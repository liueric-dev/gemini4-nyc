# Primary Land Use Tax Lot Output (PLUTO)

## Dataset name

Primary Land Use Tax Lot Output (PLUTO) (Department of City Planning (DCP)).

Extensive land use and geographic data at the tax lot level in comma-separated values (CSV) file format. The PLUTO files contain more than seventy fields derived from data maintained by city agencies. All previously released versions of this data are available on the DCP Website: BYTES of the BIG APPLE . Current version: 26v2

## Dataset ID

`64uk-42ks`. Portal page: https://data.cityofnewyork.us/d/64uk-42ks

## API URL

`https://data.cityofnewyork.us/resource/64uk-42ks.json` (SODA 2; send `X-App-Token: $NYC_OPENDATA_APP_TOKEN`).

- Update frequency (metadata): Quarterly; automated: Yes; rows last updated 2026-08-24 16:48.
- Metadata saved: `raw/od-pluto-metadata.json`.
- Data dictionary: `raw/od-pluto-dict-pluto-datadictionary.pdf`, `raw/od-pluto-dict-pluto-readme.pdf` (text in `text/`).

## Key fields

| Field | Type | Meaning (from the dataset metadata) |
|---|---|---|
| `bbl` | number | A concatenation of the borough code, tax block and tax lot. This field consists of the borough code followed by the tax block followed by the tax lot. The borough code is one numeric digit. The tax block is one to five numeric digits, preceded with leading zeros when the block is less than five digi |
| `address` | text | An address for the tax lot. Tax lots may be assigned a single house number on a street, a range of house numbers on a street, or addresses on multiple streets. ADDRESS contains the address in PTS, using the low number when there is a range of house numbers. Some tax lots, such as vacant lots or park |
| `borough` | text | The borough in which the tax lot is located. This field contains a two-character borough code. Two portions of the city, Marble Hill and Rikers Island, are legally located in one borough but are serviced by a different borough. The BOROUGH codes associated with these areas are the boroughs in which  |
| `zipcode` | number | A ZIP code that is valid for one of the addresses assigned to the tax lot. Note that a tax lot may have multiple addresses and these addresses may not have the same ZIP code. A building with entrances on two streets may have a different ZIP code for each street address. ZIP CODE may not be valid for |
| `yearbuilt` | number | The year construction of the building was completed. In general, YEAR BUILT is accurate for the decade, but not necessarily for the specific year. Between 1910 and 1985, the majority of YEAR BUILT values are in years ending in 5 or 0. Many structures built between 1800s and early 1900s have a YEAR B |
| `unitsres` | number | The sum of residential units in all buildings on the tax lot. If there are no residential units in the tax lot, this field will be zero. Hotels/motels, nursing homes and SROs do not have residential units, but boarding houses do. Basement units for building superintendents are counted as a residenti |
| `unitstotal` | number | The sum of residential and non-residential (offices, retail stores, etc.) units for all buildings on the tax lot. The count of non-residential units is sometimes not available if the building contains residential units. Non-residential units are units with a separate use. If a building has 25 differ |
| `bldgclass` | text | A code describing the major use of structures on the tax lot. Except as described below, BUILDING CLASS is taken from PTS without modification. For condominiums, PTS contains the building class for each unit lot. When merging this data into a single record for the billing lot, DCP creates several mi |
| `landuse` | number | A code for the tax lot's land use category. The Department of City Planning has created 11 land use categories and assigns each BUILDING CLASS to the most appropriate land use category. Appendix D - Land Use Categories details the relationship of building classes to land use categories. |
| `ownername` | text | The name of the owner of the tax lot. For publicly owned tax lots, owner names have been normalized. For example, "NYC PARKS", "PARKS DEPARTMENT", and "PARKS AND RECREATION (GENERAL)" have been changed to "NYC DEPARTMENT OF PARKS AND RECREATION". If OWNER NAME is normalized, DCPEdited is set to "1". |
| `ownertype` | text | A code indicating type of ownership for the tax lot. Only one data source is used per tax lot. The COLP file, which contains more accurate and specific type of city ownership data than PTS, is used when data is available for that lot. Codes C, M, O, P are derived from COLP. If the tax lot is not in  |
| `numbldgs` | number | The number of buildings on the tax lot. The number of buildings on a lot is calculated by taking the Building Identification Number (BIN) for every building in DoITT's Building Footprints dataset, running Geosupport function BN to get the BBL associated with that BIN, and summing the number of build |
| `numfloors` | number | The number of full and partial floors starting from the ground floor, for the tallest building on the tax lot. A partial floor is a floor that does not span the entire building envelope. For example, if a building is 3 stories tall and 2 floors cover the entire footprint of the building and one floo |
| `condono` | number | The condominium number assigned to the complex. Condominium numbers are unique within a borough (see BOROUGH). |
| `histdist` | text | The name of the Historic District that the tax lot is within. Historic Districts are designated by the New York City Landmarks Preservation Commission. |
| `landmark` | text | This value indicates whether the lot contains an individual landmark building, an interior landmark building, or both. |
| `version` | text | The version number for this release of PLUTO. The Version Number is in the format YYv#.# where: YY is the last two digits of the year; v stands for version; \# is the release number for that year; and .# indicates an amendment to the original release, if applicable. |

## Example query

Demo building `1048-washington-ave-bx` (BBL 2023700005, BIN 2001261):

```
curl -H "X-App-Token: $NYC_OPENDATA_APP_TOKEN" "https://data.cityofnewyork.us/resource/64uk-42ks.json?%24where=bbl%3D2023700005&%24limit=50000"
```

Decoded: `$where=bbl=2023700005&$limit=50000`

Result on 2026-11-21T00:57: HTTP 200, 1 rows, 4.269 s.

## Example response row

```json
{
 "borough": "BX",
 "block": "2370",
 "lot": "5",
 "cd": "203",
 "ct2010": "185",
 "cb2010": "1006",
 "schooldist": "9",
 "council": "16",
 "zipcode": "10456",
 "firecomp": "E050",
 "policeprct": "42",
 "healtharea": "3500",
 "sanitboro": "2",
 "sanitsub": "1B",
 "address": "1048 WASHINGTON AVENUE",
 "zonedist1": "M1-1/R7-2",
 "spdist1": "MX-7",
 "splitzone": false,
 "bldgclass": "C0",
 "landuse": "2",
 "easements": "0",
 "ownername": "1048 WASHINGTON LLC",
 "lotarea": "1637",
 "bldgarea": "2394",
 "comarea": "0",
 "resarea": "2394",
 "officearea": "0",
 "retailarea": "0",
 "garagearea": "0",
 "strgearea": "0",
 "factryarea": "0",
 "otherarea": "0",
 "areasource": "2",
 "numbldgs": "1",
 "numfloors": "3.0000000",
 "unitsres": "3",
 "unitstotal": "3",
 "lotfront": "19.1700000",
 "lotdepth": "85.4200000",
 "bldgfront": "19.0000000",
 "bldgdepth": "40.0000000",
 "ext": "E",
 "proxcode": "2",
 "irrlotcode": false,
 "lottype": "5",
 "bsmtcode": "2",
 "assessland": "7260.00000",
 "assesstot": "45300.00000",
 "exempttot": "0.00000",
 "yearbuilt": "1899",
 "yearalter1": "0",
 "yearalter2": "0",
 "builtfar": "1.46000000000",
 "residfar": "3.44000000000",
 "commfar": "1.00000000000",
 "facilfar": "6.50000000000",
 "affresfar": "5.01000000000",
 "mnffar": "1.00000000000",
 "borocode": "2",
 "bbl": "2023700005.00000000",
 "tract2010": "185",
 "xcoord": "1009477",
 "ycoord": "240678",
 "latitude": "40.8272449",
 "longitude": "-73.9088460",
 "zonemap": "3d",
 "sanborn": "210S049",
 "taxmap": "20904",
 "plutomapid": "1",
 "version": "26v2",
 "sanitdistrict": "3",
 "healthcenterdistrict": "22",
 "bct2020": "2018501",
 "bctcb2020": "20185011006",
 "transitzone": "Outer Transit Zone"
}
```

## Caveats

- Field `bbl` is a number in the API (`bbl=2023700005`, no quotes) and comes back as `"2023700005.00000000"`.
- Quarterly release (metadata); the current version is in `version` (26v2 on 2026-11-21, per the dataset description).
- `yearbuilt` is "accurate for the decade, but not necessarily for the specific year" (column description). Treat a 1955 to 1965 value as uncertain for the pre-1960 lead rule.
- Condominiums: PLUTO has one record per billing lot (75xx); unit lots are merged (column descriptions of `lot` and `bldgclass`).
- `ownername` is the Department of Finance owner of record, often a single-purpose LLC. Use HPD Registration Contacts for the managing agent and head officer.
- Rent stabilization and NYCHA status are not in PLUTO. Use the DHCR list (`od-dhcr-rs-buildings.md`) and NYCHA Residential Addresses (`od-nycha-residential-addresses.md`).
- License: NYC Open Data. NYC Admin Code § 23-502(d) says public data sets are available "without any registration requirement, license requirement or restrictions on their use", though the city may require apps to identify the source and version (`text/od-nyc-open-data-law-mirror.md`, an unofficial mirror). Dataset metadata has no license field.
- Rate limits: with an app token Socrata "do[es] not throttle API requests ... unless those requests are determined to be abusive"; without one, requests share an IP-based pool with "a much lower throttling limit" (`local/od-socrata-app-tokens.md`). Default page size is 1,000 rows (`local/od-nyc-opendata-api-guide.md`); set `$limit`.
