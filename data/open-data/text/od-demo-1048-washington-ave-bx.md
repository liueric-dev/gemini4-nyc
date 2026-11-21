# Demo building: pre-1960 multiple dwelling under a full HPD vacate order (extra case)

- BBL `2023700005`, BIN `2001261`
- Records retrieved 2026-11-21T00:57:13-05:00 from NYC Open Data (raw: `raw/od-demo-1048-washington-ave-bx.json`; geocode: `raw/od-demo-1048-washington-ave-bx-geosearch.json`)
- Why chosen: First pre-1960 candidate (built 1899, 3 units, LLC-owned, not on the DHCR list, order 616 violations). Kept as an extra example because it has an entire-building vacate order (fire damage, effective 2026-04-20, not rescinded) and is in the Alternative Enforcement Program.

## PLUTO row (64uk-42ks)

| Field | Value |
|---|---|
| `borough` | BX |
| `block` | 2370 |
| `lot` | 5 |
| `cd` | 203 |
| `ct2010` | 185 |
| `cb2010` | 1006 |
| `schooldist` | 9 |
| `council` | 16 |
| `zipcode` | 10456 |
| `firecomp` | E050 |
| `policeprct` | 42 |
| `healtharea` | 3500 |
| `sanitboro` | 2 |
| `sanitsub` | 1B |
| `address` | 1048 WASHINGTON AVENUE |
| `zonedist1` | M1-1/R7-2 |
| `spdist1` | MX-7 |
| `splitzone` | False |
| `bldgclass` | C0 |
| `landuse` | 2 |
| `easements` | 0 |
| `ownername` | 1048 WASHINGTON LLC |
| `lotarea` | 1637 |
| `bldgarea` | 2394 |
| `comarea` | 0 |
| `resarea` | 2394 |
| `officearea` | 0 |
| `retailarea` | 0 |
| `garagearea` | 0 |
| `strgearea` | 0 |
| `factryarea` | 0 |
| `otherarea` | 0 |
| `areasource` | 2 |
| `numbldgs` | 1 |
| `numfloors` | 3.0000000 |
| `unitsres` | 3 |
| `unitstotal` | 3 |
| `lotfront` | 19.1700000 |
| `lotdepth` | 85.4200000 |
| `bldgfront` | 19.0000000 |
| `bldgdepth` | 40.0000000 |
| `ext` | E |
| `proxcode` | 2 |
| `irrlotcode` | False |
| `lottype` | 5 |
| `bsmtcode` | 2 |
| `assessland` | 7260.00000 |
| `assesstot` | 45300.00000 |
| `exempttot` | 0.00000 |
| `yearbuilt` | 1899 |
| `yearalter1` | 0 |
| `yearalter2` | 0 |
| `builtfar` | 1.46000000000 |
| `residfar` | 3.44000000000 |
| `commfar` | 1.00000000000 |
| `facilfar` | 6.50000000000 |
| `affresfar` | 5.01000000000 |
| `mnffar` | 1.00000000000 |
| `borocode` | 2 |
| `bbl` | 2023700005.00000000 |
| `tract2010` | 185 |
| `xcoord` | 1009477 |
| `ycoord` | 240678 |
| `latitude` | 40.8272449 |
| `longitude` | -73.9088460 |
| `zonemap` | 3d |
| `sanborn` | 210S049 |
| `taxmap` | 20904 |
| `plutomapid` | 1 |
| `version` | 26v2 |
| `sanitdistrict` | 3 |
| `healthcenterdistrict` | 22 |
| `bct2020` | 2018501 |
| `bctcb2020` | 20185011006 |
| `transitzone` | Outer Transit Zone |

## Status flags

- On the DHCR 2025 rent-stabilized building list: **no**
- NYCHA residential address (3ub5-4ph8): **no**
- HPD building record 119624: management program PVT, DOB class "HERETOFORE CONVERTED CLASS A", legal stories 3, legal class A units 3, class B 0, status Active
- Alternative Enforcement Program: Aep Round 18 AEP Discharged; Aep Round 19 AEP Active
- Certification of No Harassment pilot: none
- Heat Sensor Program: none
- HPD vacate orders: Entire Building (Fire Damage), effective 2026-04-20, rescinded not rescinded, units 3

## HPD registration (tesw-yqqr, feu5-w2e2)

- Registration 210568: last registered 2026-09-20, ends 2027-09-01
- Contacts by type (individual names omitted here; they are in the raw file): CorporateOwner 1, Agent 1, HeadOfficer 1, SiteManager 1
- Corporate names on the registration: 1048 WASHINGTON LLC

## HPD violations

Dataset wvxf-dwi5:
- Total 481; open 38
- By class: A 108, B 193, C 170, I 10
- Open by class: A 16, B 4, C 14, I 4
- Inspection dates 2004-03-09 to 2026-04-17
- Most common order numbers: 501 (73) 501 - REPAIR; 502 (44) 502 - REPAIR WITH SIMILAR MATERIAL; 556 (42) 556 - PAINT; 508 (35) 508 - REPAIR PLASTER; 616 (20) 616 - LEAD-BASED PAINT HAZARD- PRESUMED PAINT; 702 (19) 702 - REPAIR OR REPLACE SMOKE DETECTOR; 530 (19) 530 - MAKE DOORS SELF-CLOSING; 505 (19) 505 - RETIRED; 1503 (17) 1503 - REPAIR OR REPLACE CO DETECTOR; 506 (17) 506 - REPLACE
- Rent-impairing: 28

## HPD complaints (ygpa-z7cr)

- 368 problems in 166 complaints, 2003-09-19 to 2026-04-29; since 2026-01-01: 39
- By major category: DOOR/WINDOW 56; HEAT/HOT WATER 52; PLUMBING 51; UNSANITARY CONDITION 49; HEATING 44; PAINT/PLASTER 36; ELECTRIC 26; FLOORING/STAIRS 17; GENERAL 16; SAFETY 11; WATER LEAK 6; APPLIANCE 2
- Top category / subcategory: HEATING / HEAT RELATED 43; DOOR/WINDOW / DOOR 35; UNSANITARY CONDITION / PESTS 29; HEAT/HOT WATER / ENTIRE BUILDING 27; PAINT/PLASTER / WALL 27; HEAT/HOT WATER / APARTMENT ONLY 25; FLOORING/STAIRS / FLOOR 17; PLUMBING / WATER SUPPLY 15
- Most common outcome text: "The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been" (87) | "The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specifi" (85) | "More than one complaint was received for this building-wide condition. This complaint status is for the initial complaint.The Department of " (41)

## 311 service requests since 2020 (erm2-nwe9)

- 275 requests, 2020-01-09 to 2026-08-28
- By agency: HPD 228, DOB 13, NYPD 12, DSNY 10, DOHMH 8, DEP 4
- Top complaint type / descriptor: DOOR/WINDOW / DOOR 31; UNSANITARY CONDITION / PESTS 23; PAINT/PLASTER / WALL 21; HEAT/HOT WATER / ENTIRE BUILDING 18; HEAT/HOT WATER / APARTMENT ONLY 16; FLOORING/STAIRS / FLOOR 14; DOOR/WINDOW / WINDOW FRAME 11; PLUMBING / WATER SUPPLY 10; UNSANITARY CONDITION / MOLD 8; PLUMBING / RADIATOR 7

## Other records

- HPD litigations: 11 (Tenant Action [CLOSED] 3; Access Warrant - Non-Lead [CLOSED] 2; Tenant Action/Harrassment [CLOSED] 2; Heat and Hot Water [CLOSED] 2; Tenant Action/Harrassment [PENDING] 1; Access Warrant - lead [PENDING] 1)
- Harassment findings: No Harassment (); No Harassment ()
- Bedbug annual filings: 6 (2022-11-01..2023-10-31: infested 0, eradicated 0, re-infested 0; 2023-11-01..2024-10-31: infested 0, eradicated 0, re-infested 0; 2024-11-01..2025-10-31: infested 0, eradicated 0, re-infested 0, latest 3)
- DOB complaints: 13
- DOB violations (BIS): 0
- DOB safety violations (DOB NOW): 0
- DOB ECB violations: 3
- DOB permits (BIS): 0
- DOB NOW approved permits: 0
- Certificates of occupancy (to 2021): 0
- Certificates of occupancy (DOB NOW): 0
- ACRIS documents on this lot: 47
  - ECB by status: ACTIVE 3

## Query timings (this fetch)

| Dataset | ID | HTTP | Seconds | Rows |
|---|---|---|---|---|
| pluto | 64uk-42ks | 200 | 4.269 | 1 |
| hpd_buildings | kj4p-ruqc | 200 | 8.98 | 1 |
| hpd_registrations | tesw-yqqr | 200 | 0.578 | 1 |
| hpd_violations | wvxf-dwi5 | 200 | 11.364 | 481 |
| hpd_violations_nycha | im9z-53hg | 200 | 0.475 | 0 |
| hpd_complaints | ygpa-z7cr | 200 | 7.917 | 368 |
| hpd_litigations | 59kj-x8nc | 200 | 0.433 | 11 |
| hpd_vacate_orders | tb8q-a3ar | 200 | 2.415 | 1 |
| hpd_bedbug_reporting | wz6d-d3jb | 200 | 4.022 | 6 |
| hpd_aep | hcir-3275 | 200 | 0.357 | 2 |
| hpd_conh_pilot | bzxi-2tsw | 200 | 5.647 | 0 |
| hpd_heat_sensor | h4mf-f24e | 200 | 0.719 | 0 |
| sr311 | erm2-nwe9 | 200 | 18.82 | 275 |
| dob_complaints | eabe-havv | 200 | 0.37 | 13 |
| dob_violations | 3h2n-5cm9 | 200 | 0.419 | 0 |
| dob_ecb_violations | 6bgk-3dad | 200 | 2.546 | 3 |
| dob_safety_violations | 855j-jady | 200 | 0.425 | 0 |
| dob_permits | ipu4-2q9a | 200 | 5.06 | 0 |
| dob_now_permits | rbx6-tga4 | 200 | 10.539 | 0 |
| dob_cofo | bs8b-p36w | 200 | 0.376 | 0 |
| dob_now_cofo | pkdm-hqz6 | 200 | 0.448 | 0 |
| acris_legals | 8h5j-fqxa | 200 | 10.236 | 47 |
| nycha_residential_addresses | 3ub5-4ph8 | 200 | 5.827 | 0 |
| hpd_registration_contacts | feu5-w2e2 | 200 | 0.358 | 4 |

Timings were taken while other heavy queries ran on the same app token, so they overstate typical latency; see the Live fetch table in `checklist.md` for quiet-time timings.
