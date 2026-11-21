# Demo building: pre-1960 multiple dwelling (built 1929, 4 units)

- BBL `2025140062`, BIN `2003271`
- Records retrieved 2026-11-21T01:17:47-05:00 from NYC Open Data (raw: `raw/od-demo-122-w-167-st-bx.json`; geocode: `raw/od-demo-122-w-167-st-bx-geosearch.json`)
- Why chosen: PLUTO year built 1929, 4 residential units, class C3 walk-up, LLC-owned; not on the DHCR 2025 rent-stabilized list, so it isolates the pre-1960 branch from rent stabilization. Found among buildings with HPD order 616 (presumed lead-based paint) violations inspected since 2025-06-01; chosen over 1048 Washington Avenue, which is under a full vacate order, and checked for no HPD vacate order.

## PLUTO row (64uk-42ks)

| Field | Value |
|---|---|
| `borough` | BX |
| `block` | 2514 |
| `lot` | 62 |
| `cd` | 204 |
| `ct2010` | 199 |
| `cb2010` | 4003 |
| `schooldist` | 9 |
| `council` | 16 |
| `zipcode` | 10452 |
| `firecomp` | E068 |
| `policeprct` | 44 |
| `healtharea` | 3310 |
| `sanitboro` | 2 |
| `sanitsub` | 2A |
| `address` | 122 WEST 167TH STREET |
| `zonedist1` | R7-1 |
| `splitzone` | False |
| `bldgclass` | C3 |
| `landuse` | 2 |
| `easements` | 0 |
| `ownername` | 122W 167 LLC |
| `lotarea` | 2500 |
| `bldgarea` | 4476 |
| `comarea` | 0 |
| `resarea` | 4476 |
| `officearea` | 0 |
| `retailarea` | 0 |
| `garagearea` | 0 |
| `strgearea` | 0 |
| `factryarea` | 0 |
| `otherarea` | 0 |
| `areasource` | 2 |
| `numbldgs` | 3 |
| `numfloors` | 3.0000000 |
| `unitsres` | 4 |
| `unitstotal` | 4 |
| `lotfront` | 25.0000000 |
| `lotdepth` | 100.0000000 |
| `bldgfront` | 25.0000000 |
| `bldgdepth` | 40.0000000 |
| `ext` | G |
| `proxcode` | 1 |
| `irrlotcode` | False |
| `lottype` | 5 |
| `bsmtcode` | 0 |
| `assessland` | 56250.00000 |
| `assesstot` | 281250.00000 |
| `exempttot` | 0.00000 |
| `yearbuilt` | 1929 |
| `yearalter1` | 2021 |
| `yearalter2` | 0 |
| `builtfar` | 1.79000000000 |
| `residfar` | 3.44000000000 |
| `commfar` | 0.00000000000 |
| `facilfar` | 4.80000000000 |
| `affresfar` | 5.01000000000 |
| `mnffar` | 0.00000000000 |
| `borocode` | 2 |
| `bbl` | 2025140062.00000000 |
| `tract2010` | 199 |
| `xcoord` | 1004608 |
| `ycoord` | 244043 |
| `latitude` | 40.8364935 |
| `longitude` | -73.9264292 |
| `zonemap` | 3b |
| `sanborn` | 210S041 |
| `taxmap` | 20908 |
| `appbbl` | 2025140062.00000000 |
| `appdate` | 2022-10-14T00:00:00.000 |
| `plutomapid` | 1 |
| `version` | 26v2 |
| `sanitdistrict` | 4 |
| `healthcenterdistrict` | 23 |
| `bct2020` | 2019900 |
| `bctcb2020` | 20199004003 |
| `transitzone` | Outer Transit Zone |

## Status flags

- On the DHCR 2025 rent-stabilized building list: **no**
- NYCHA residential address (3ub5-4ph8): **no**
- HPD building record 120959: management program PVT, DOB class "OLD  LAW TENEMENT", legal stories 3, legal class A units 4, class B 0, status Active
- Alternative Enforcement Program: none
- Certification of No Harassment pilot: none
- Heat Sensor Program: none
- HPD vacate orders: none

## HPD registration (tesw-yqqr, feu5-w2e2)

- Registration 215369: last registered 2025-08-26, ends 2026-09-01
- Contacts by type (individual names omitted here; they are in the raw file): CorporateOwner 1, Agent 1, HeadOfficer 1
- Corporate names on the registration: 122W 167 LLC; FRONTGATE MANAGEMENT

## HPD violations

Dataset wvxf-dwi5:
- Total 396; open 164
- By class: A 62, B 202, C 128, I 4
- Open by class: A 16, B 85, C 62, I 1
- Inspection dates 2004-09-01 to 2026-11-18
- Most common order numbers: 501 (46) 501 - REPAIR; 508 (41) 508 - REPAIR PLASTER; 569 (24) 569 - ABATE THE NUISANCE OF MICE; 502 (24) 502 - REPAIR WITH SIMILAR MATERIAL; 568 (22) 568 - ABATE THE NUISANCE OF ROACHES; 556 (22) 556 - PAINT; 702 (19) 702 - REPAIR OR REPLACE SMOKE DETECTOR; 550 (16) 550 - TRACE & REPAIR THE SOURCE & ABATE THE…MOLD; 510 (14) 510 - ABATE THE NUISANCE; 616 (14) 616 - LEAD-BASED PAINT HAZARD- PRESUMED PAINT
- Rent-impairing: 29

## HPD complaints (ygpa-z7cr)

- 463 problems in 155 complaints, 2004-01-23 to 2026-11-17; since 2026-01-01: 78
- By major category: GENERAL 105; PLUMBING 76; PAINT/PLASTER 60; HEAT/HOT WATER 58; UNSANITARY CONDITION 44; NONCONST 34; DOOR/WINDOW 20; HEATING 19; APPLIANCE 17; WATER LEAK 10; ELECTRIC 10; FLOORING/STAIRS 6
- Top category / subcategory: HEAT/HOT WATER / APARTMENT ONLY 46; PAINT/PLASTER / WALL 43; UNSANITARY CONDITION / PESTS 30; PLUMBING / BASIN/SINK 29; GENERAL / DOORS 27; NONCONST / VERMIN 26; HEATING / HEAT RELATED 19; PAINT/PLASTER / CEILING 17
- Most common outcome text: "The Department of Housing Preservation and Development inspected the following conditions. No violations were issued. The complaint has been" (128) | "The Department of Housing Preservation and Development inspected the following conditions. Violations were issued. Information about specifi" (98) | "The Department of Housing Preservation and Development was not able to gain access to inspect the following conditions. The complaint has be" (64)

## 311 service requests since 2020 (erm2-nwe9)

- 231 requests, 2020-01-02 to 2026-11-17
- By agency: HPD 174, NYPD 32, DSNY 8, DEP 6, DOHMH 4, DOB 4, DCWP 2, DPR 1
- Top complaint type / descriptor: HEAT/HOT WATER / APARTMENT ONLY 45; UNSANITARY CONDITION / PESTS 24; PAINT/PLASTER / WALL 16; Noise - Residential / Loud Music/Party 15; PLUMBING / BASIN/SINK 14; DOOR/WINDOW / WINDOW FRAME 7; GENERAL / CABINET 6; DOOR/WINDOW / DOOR FRAME 5; UNSANITARY CONDITION / MOLD 5; WATER LEAK / SLOW LEAK 5

## Other records

- HPD litigations: 3 (Heat and Hot Water [CLOSED] 2; Tenant Action/Harrassment [PENDING] 1)
- Bedbug annual filings: 5 (2022-11-01..2023-10-31: infested 0, eradicated 0, re-infested 0; 2023-11-01..2024-10-31: infested 0, eradicated 0, re-infested 0; 2024-11-01..2025-10-31: infested 0, eradicated 0, re-infested 0, latest 3)
- DOB complaints: 12
- DOB violations (BIS): 3
- DOB safety violations (DOB NOW): 1
- DOB ECB violations: 4
- DOB permits (BIS): 4
- DOB NOW approved permits: 1
- Certificates of occupancy (to 2021): 0
- Certificates of occupancy (DOB NOW): 0
- ACRIS documents on this lot: 52
  - ECB by status: RESOLVE 4

## Query timings (this fetch)

| Dataset | ID | HTTP | Seconds | Rows |
|---|---|---|---|---|
| pluto | 64uk-42ks | 200 | 1.51 | 1 |
| hpd_buildings | kj4p-ruqc | 200 | 14.633 | 1 |
| hpd_registrations | tesw-yqqr | 200 | 20.593 | 1 |
| hpd_violations | wvxf-dwi5 | 200 | 6.546 | 396 |
| hpd_violations_nycha | im9z-53hg | 503 | 30.843 | error |
| hpd_complaints | ygpa-z7cr | 200 | 24.184 | 463 |
| hpd_litigations | 59kj-x8nc | 200 | 11.1 | 3 |
| hpd_vacate_orders | tb8q-a3ar | 200 | 4.083 | 0 |
| hpd_bedbug_reporting | wz6d-d3jb | 200 | 8.563 | 5 |
| hpd_aep | hcir-3275 | 200 | 1.078 | 0 |
| hpd_conh_pilot | bzxi-2tsw | 200 | 4.597 | 0 |
| hpd_heat_sensor | h4mf-f24e | 200 | 14.572 | 0 |
| sr311 | erm2-nwe9 | 200 | 5.741 | 231 |
| dob_complaints | eabe-havv | 200 | 2.62 | 12 |
| dob_violations | 3h2n-5cm9 | 200 | 6.164 | 3 |
| dob_ecb_violations | 6bgk-3dad | 200 | 2.547 | 4 |
| dob_safety_violations | 855j-jady | 200 | 4.589 | 1 |
| dob_permits | ipu4-2q9a | 200 | 15.183 | 4 |
| dob_now_permits | rbx6-tga4 | 200 | 11.08 | 1 |
| dob_cofo | bs8b-p36w | 200 | 7.951 | 0 |
| dob_now_cofo | pkdm-hqz6 | 200 | 11.922 | 0 |
| acris_legals | 8h5j-fqxa | 200 | 6.305 | 52 |
| nycha_residential_addresses | 3ub5-4ph8 | 200 | 4.2 | 0 |
| hpd_registration_contacts | feu5-w2e2 | 200 | 2.897 | 3 |

Timings were taken while other heavy queries ran on the same app token, so they overstate typical latency; see the Live fetch table in `checklist.md` for quiet-time timings.
