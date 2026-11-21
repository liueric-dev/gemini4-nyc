# Demo building: rent-stabilized building (built 1965)

- BBL `4017860017`, BIN `4044993`
- Records retrieved 2026-11-21T00:59:47-05:00 from NYC Open Data (raw: `raw/od-demo-3906-114-st-qn.json`; geocode: `raw/od-demo-3906-114-st-qn-geosearch.json`)
- Why chosen: Listed in the DHCR 2025 rent-stabilized building file (Queens). Chosen as the post-1960 rent-stabilized case so it does not overlap the pre-1960 case: PLUTO 1962-1972, elevator rental class D1/D3/D7, single building on the lot, not a co-op, then ranked by HPD problems received since 2026-01-01 (most: 368). Selection queries are logged in checklist.md.

## PLUTO row (64uk-42ks)

| Field | Value |
|---|---|
| `borough` | QN |
| `block` | 1786 |
| `lot` | 17 |
| `cd` | 403 |
| `ct2010` | 399 |
| `cb2010` | 3003 |
| `schooldist` | 24 |
| `council` | 21 |
| `zipcode` | 11368 |
| `firecomp` | L138 |
| `policeprct` | 115 |
| `healtharea` | 1100 |
| `sanitboro` | 4 |
| `sanitsub` | 3C |
| `address` | 39-06 114 STREET |
| `zonedist1` | R6 |
| `zonedist2` | R5A |
| `splitzone` | True |
| `bldgclass` | D3 |
| `landuse` | 3 |
| `easements` | 0 |
| `ownername` | 39-06 114 ST REALTY LLC |
| `lotarea` | 21875 |
| `bldgarea` | 40936 |
| `comarea` | 256 |
| `resarea` | 40680 |
| `officearea` | 0 |
| `retailarea` | 0 |
| `garagearea` | 0 |
| `strgearea` | 0 |
| `factryarea` | 0 |
| `otherarea` | 256 |
| `areasource` | 2 |
| `numbldgs` | 1 |
| `numfloors` | 6.0000000 |
| `unitsres` | 70 |
| `unitstotal` | 70 |
| `lotfront` | 175.0000000 |
| `lotdepth` | 125.0000000 |
| `bldgfront` | 60.0000000 |
| `bldgdepth` | 113.0000000 |
| `ext` | N |
| `proxcode` | 0 |
| `irrlotcode` | False |
| `lottype` | 5 |
| `bsmtcode` | 0 |
| `assessland` | 393750.00000 |
| `assesstot` | 2060100.00000 |
| `exempttot` | 0.00000 |
| `yearbuilt` | 1965 |
| `yearalter1` | 0 |
| `yearalter2` | 0 |
| `builtfar` | 1.87000000000 |
| `residfar` | 2.43000000000 |
| `commfar` | 0.00000000000 |
| `facilfar` | 4.80000000000 |
| `affresfar` | 3.90000000000 |
| `mnffar` | 0.00000000000 |
| `borocode` | 4 |
| `bbl` | 4017860017.00000000 |
| `tract2010` | 399 |
| `xcoord` | 1024896 |
| `ycoord` | 213651 |
| `latitude` | 40.7530057 |
| `longitude` | -73.8532954 |
| `zonemap` | 10b |
| `sanborn` | 419 014 |
| `taxmap` | 41003 |
| `plutomapid` | 1 |
| `version` | 26v2 |
| `sanitdistrict` | 3 |
| `healthcenterdistrict` | 42 |
| `bct2020` | 4039902 |
| `bctcb2020` | 40399021003 |
| `transitzone` | Special 25-241 Parking Provisions |

## Status flags

- On the DHCR 2025 rent-stabilized building list: **yes** (MULTIPLE DWELLING A;  ; od-dhcr-rs-buildings-2025-queens.pdf p.86)
- NYCHA residential address (3ub5-4ph8): **no**
- HPD building record 1012426: management program PVT, DOB class "None", legal stories None, legal class A units None, class B None, status Pending
- HPD building record 1008856: management program PVT, DOB class "None", legal stories None, legal class A units None, class B None, status Inactive
- HPD building record 527226: management program PVT, DOB class "HEREAFTER ERECTED CLASS A", legal stories 6, legal class A units 70, class B 0, status Active
- Alternative Enforcement Program: Aep Round 12 AEP Discharged
- Certification of No Harassment pilot: none
- Heat Sensor Program: none
- HPD vacate orders: none

## HPD registration (tesw-yqqr, feu5-w2e2)

- Registration 420662: last registered 2026-09-08, ends 2027-09-01
- Contacts by type (individual names omitted here; they are in the raw file): CorporateOwner 1, Agent 1, HeadOfficer 1, SiteManager 1
- Corporate names on the registration: 39-06 114 ST REALTY LLC; ALMA REALTY CORP

## HPD violations

Dataset wvxf-dwi5:
- Total 1642; open 17
- By class: A 246, B 1080, C 315, I 1
- Open by class: B 7, C 10
- Inspection dates 1988-02-23 to 2026-10-30
- Most common order numbers: 508 (245) 508 - REPAIR PLASTER; 501 (176) 501 - REPAIR; 550 (125) 550 - TRACE & REPAIR THE SOURCE & ABATE THE…MOLD; 583 (121) 583 - REPAIR THE SOURCE AND ABATE THE WATER LEAK; 502 (116) 502 - REPAIR WITH SIMILAR MATERIAL; 530 (108) 530 - MAKE DOORS SELF-CLOSING; 556 (82) 556 - PAINT; 702 (81) 702 - REPAIR OR REPLACE SMOKE DETECTOR; 1503 (64) 1503 - REPAIR OR REPLACE CO DETECTOR; 507 (62) 507 - LEAKY ROOF
- Rent-impairing: 117

## HPD complaints (ygpa-z7cr)

- 2363 problems in 1258 complaints, 2003-02-24 to 2026-11-16; since 2026-01-01: 368
- By major category: HEAT/HOT WATER 557; PAINT/PLASTER 311; HEATING 268; UNSANITARY CONDITION 258; PLUMBING 206; GENERAL 185; DOOR/WINDOW 156; WATER LEAK 123; FLOORING/STAIRS 72; ELECTRIC 68; SAFETY 63; APPLIANCE 61
- Top category / subcategory: HEAT/HOT WATER / ENTIRE BUILDING 415; HEATING / HEAT RELATED 266; PAINT/PLASTER / CEILING 155; HEAT/HOT WATER / APARTMENT ONLY 142; UNSANITARY CONDITION / PESTS 132; PAINT/PLASTER / WALL 124; UNSANITARY CONDITION / MOLD 100; PLUMBING / WATER-LEAKS 84
- Most common outcome text: "The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been" (501) | "The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specifi" (421) | "More than one complaint was received for this building-wide condition. This complaint status is for the initial complaint.The Department of " (328)

## 311 service requests since 2020 (erm2-nwe9)

- 609 requests, 2020-01-03 to 2026-11-16
- By agency: HPD 507, DOB 49, NYPD 32, DOHMH 13, DEP 4, DSNY 3, TLC 1
- Top complaint type / descriptor: HEAT/HOT WATER / ENTIRE BUILDING 205; HEAT/HOT WATER / APARTMENT ONLY 49; Elevator / Elevator - Single Device On Property/No Alternate Service 44; PAINT/PLASTER / CEILING 27; WATER LEAK / HEAVY FLOW 25; WATER LEAK / SLOW LEAK 21; UNSANITARY CONDITION / MOLD 21; GENERAL / BELL/BUZZER/INTERCOM 17; UNSANITARY CONDITION / PESTS 14; APPLIANCE / ELECTRIC/GAS RANGE 14

## Other records

- HPD litigations: 35 (Heat and Hot Water [CLOSED] 9; Tenant Action [CLOSED] 9; Access Warrant - Non-Lead [CLOSED] 8; False Certification Non-Lead [CLOSED] 4; Comprehensive [CLOSED] 3; Comp Supplemental Cases [CLOSED] 2)
- Bedbug annual filings: 9 (2022-11-01..2023-10-31: infested 0, eradicated 0, re-infested 0; 2023-11-01..2024-10-31: infested 0, eradicated 0, re-infested 0; 2024-11-01..2025-10-31: infested 0, eradicated 0, re-infested 0, latest 3)
- DOB complaints: 96
- DOB violations (BIS): 25
- DOB safety violations (DOB NOW): 14
- DOB ECB violations: 38
- DOB permits (BIS): 27
- DOB NOW approved permits: 8
- Certificates of occupancy (to 2021): 0
- Certificates of occupancy (DOB NOW): 0
- ACRIS documents on this lot: 36
  - ECB by status: RESOLVE 35, ACTIVE 3

## Query timings (this fetch)

| Dataset | ID | HTTP | Seconds | Rows |
|---|---|---|---|---|
| pluto | 64uk-42ks | 200 | 0.283 | 1 |
| hpd_buildings | kj4p-ruqc | 200 | 0.374 | 3 |
| hpd_registrations | tesw-yqqr | 200 | 11.398 | 1 |
| hpd_violations | wvxf-dwi5 | 200 | 12.445 | 1642 |
| hpd_violations_nycha | im9z-53hg | 200 | 0.664 | 0 |
| hpd_complaints | ygpa-z7cr | 200 | 6.552 | 2363 |
| hpd_litigations | 59kj-x8nc | 200 | 5.794 | 35 |
| hpd_vacate_orders | tb8q-a3ar | 200 | 11.276 | 0 |
| hpd_bedbug_reporting | wz6d-d3jb | 200 | 8.582 | 9 |
| hpd_aep | hcir-3275 | 200 | 10.83 | 1 |
| hpd_conh_pilot | bzxi-2tsw | 200 | 24.927 | 0 |
| hpd_heat_sensor | h4mf-f24e | 200 | 0.36 | 0 |
| sr311 | erm2-nwe9 | 200 | 7.456 | 609 |
| dob_complaints | eabe-havv | 200 | 3.686 | 96 |
| dob_violations | 3h2n-5cm9 | 200 | 6.105 | 25 |
| dob_ecb_violations | 6bgk-3dad | 200 | 1.951 | 38 |
| dob_safety_violations | 855j-jady | 200 | 20.719 | 14 |
| dob_permits | ipu4-2q9a | 200 | 138.633 | 27 |
| dob_now_permits | rbx6-tga4 | 200 | 2.17 | 8 |
| dob_cofo | bs8b-p36w | 200 | 16.37 | 0 |
| dob_now_cofo | pkdm-hqz6 | 200 | 2.73 | 0 |
| acris_legals | 8h5j-fqxa | 200 | 12.847 | 36 |
| nycha_residential_addresses | 3ub5-4ph8 | 200 | 14.421 | 0 |
| hpd_registration_contacts | feu5-w2e2 | 200 | 30.869 | 4 |

Timings were taken while other heavy queries ran on the same app token, so they overstate typical latency; see the Live fetch table in `checklist.md` for quiet-time timings.
