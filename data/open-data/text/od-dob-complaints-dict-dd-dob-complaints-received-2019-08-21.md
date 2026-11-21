# Data dictionary: od-dob-complaints-dict-dd-dob-complaints-received-2019-08-21.xlsx

Source: https://data.cityofnewyork.us/d/eabe-havv
Extracted from: od-dob-complaints-dict-dd-dob-complaints-received-2019-08-21.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | DOB Complaints Received |
| Agency Name | Department of Buildings |
| Update Frequency | Daily |
| Dataset Description | A list of complaints received with disposition information. |
| Dataset Keywords | complaints, dob, buildings |
| Dataset Category | Housing & Development |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. | This is the universe of complaints received by Department of Buildings (DOB). It includes complaints that come from 311, that are called in to DOB's Customer Service Center, and that are entered into the system by DOB staff. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the idiosyncrasies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Term, Acronym, or Code Definitions | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) |
| Complaint Number | 7-digit complaint number starting with borough code: (1= Manhattan, 2= Bronx, 3 = Brooklyn, 4 = Queens, 5 = Staten Island). This number is assigned by Buildings Information System (BIS) when the complaint is entered into the system. |
| Status | Current status of the complaint. This is based on the Disposition Code. |  | Expected Values: ACTIVE, CLOSED |
| Date Entered | Date that the complaint was entered into BIS. |
| House Number | House number for the address of the building identified in the complaint. |
| ZIP Code | Zip code for the address of the building identified in the complaint. |
| House Street | Street name for the address of the building identified in the complaint. |
| BIN | Building Identification Number, assigned by City Planning, for the address of the building identified in the complaint. |
| Community Board | Community board for the address of the building identified in the complaint. 3-digit identifier: Borough code = first position, last 2 = community board. |
| Special District | Indicates whether or not the building identified in the complaint is located in a Special District. |
| Complaint Category | 2-digit, alphanumeric, DOB Complaint Category Codes. |  | Current list of DOB complaint codes can be found at http://www1.nyc.gov/assets/buildings/pdf/complaint_category.pdf  Historical list can be found on the Categories tab of this document. |
| Unit | The most recent unit that was assigned to this complaint. It may have been initially assigned to one unit, and then referred to another unit for disposition. |
| Disposition Date | Date that the disposition for the complaint was entered into BIS. |
| Disposition Code | 2-digit, alphanumeric, Disposition Code of Complaint. |  | Complete List of codes can be found at http://www1.nyc.gov/assets/buildings/pdf/bis_complaint_disposition_codes.pdf |
| Inspection Date | Date that the inspection was performed. |
| DOBRunDate | Date when query is run and pushed to Open Data. Could be used to differentiate report dates. |

## Sheet: Categories

| num | Complaint..Category.Description |
| 01 | ACCIDENT - CONSTRUCTION/PLUMBING |
| 02 | ACCIDENT - TO PUBLIC |
| 03 | ADJACENT BUILDINGS - NOT PROTECTED |
| 04 | AFTER HOURS WORK - ILLEGAL |
| 05 | PERMIT - NONE (BUILDING/ PA/ DEMO ETC.) |
| 06 | CONSTRUCTION - CHANGE GRADE / CHANGE WATERCOURSE |
| 07 | CONSTRUCTION - CHANGE WATERCOURSE |
| 08 | CONTRACTOR'S SIGN - NONE |
| 09 | DEBRIS - EXCESSIVE |
| 10 | DEBRIS/BUILDING -FALLING OR IN DANGER OF FALLING |
| 11 | DEMOLITION - NO PERMIT |
| 12 | DEMOLITION-UNSAFE/ILLEGAL/MECHANICAL DEMO |
| 13 | ELEVATOR IN (FDNY) READINESS-NONE |
| 14 | EXCAVATION - UNDERMINING ADJACENT BUILDING |
| 15 | FENCE - NONE/INADEQUATE/ILLEGAL |
| 16 | INADEQUATE SUPPORT/SHORING |
| 17 | MATERIAL/PERSONNEL HOIST - NO PERMIT |
| 18 | MATERIAL STORAGE - UNSAFE |
| 19 | MECHANICAL DEMOLITION - ILLEGAL |
| 1A | ILLEGAL CONVERSION COMMERCIAL BLDG/SPACE TO DWELLING UNITS |
| 1B | ILLEGAL TREE REMOVAL/TOPO. CHANGE IN SNAD |
| 1C | DAMAGE ASSESSMENT REQUEST OR REPORT (DISASTER) |
| 1D | CON EDISON REFERRAL |
| 1E | SUSPENDED (HANGING) SCAFFOLDS- NO PMT/LIC/DANGEROUS/ACCIDENT |
| 1F | FAILURE TO COMPLY WITH ANNUAL CRANE INSPECTION |
| 1G | STALLED CONSTRUCTION SITE |
| 1H | EMERGENCY ASBESTOS RESPONSE INSPECTION |
| 1J | JEWELRY/DENTISTRY TORCH: GAS PIPING REMOVED W/O PERMIT |
| 1K | BOWSTRING TRUSS TRACKING COMPLAINT |
| 1L | GAS UTILITY REFERRAL |
| 1U | SPECIAL OPERATIONS COMPLIANCE INSPECTION |
| 1V | ELECTRICAL ENFORCEMENT WORK ORDER (DOB) |
| 1W | PLUMBING ENFORCEMENT WORK ORDER (DOB) |
| 1X | CONSTRUCTION ENFORCEMENT WORK ORDER (DOB) |
| 1Y | ENFORCEMENT WORK ORDER (DOB) |
| 1Z | ENFORCEMENT WORK ORDER (DOB) |
| 20 | LANDMARK BUILDING - ILLEGAL WORK |
| 21 | SAFETY NET/GUARD RAIL-DAM/INADEQ/NONE(OVER 6 STY/75 FT) |
| 22 | SAFETY NETTING - NONE |
| 23 | SIDEWALK SHED/SUPPORTED SCAFFOLD/INADEQUATE/DEFECT/NONE/NO PMT/NO CERT |
| 24 | SIDEWALK SHED - NONE |
| 25 | WARNING SIGNS/LIGHTS - NONE |
| 26 | WATCHMAN - NONE |
| 27 | AUTO REPAIR - ILLEGAL |
| 28 | BUILDING - IN DANGER OF COLLAPSE |
| 29 | BUILDING - VACANT, OPEN AND UNGUARDED |
| 2A | POSTED NOTICE OR ORDER REMOVED/TAMPERED WITH |
| 2B | FAILURE TO COMPLY WITH VACATE ORDER |
| 2C | SMOKING BAN- SMOKING ON CONSTRUCTION SITE |
| 2D | SMOKING SIGNS- "NO SMOKING SIGNS" NOT OBSERVED ON CONSTRUCTION SITE |
| 2E | TRACKING COMPLAINT FOR FULL DEMOLITION NOTIFICATION |
| 2F | BUILDING UNDER STRUCTURAL MONITORING |
| 2G | ADVERTISING SIGN/BILLBOARD/POSTERS/FLEXIBLE FABRIC - ILLEGAL |
| 2H | SECOND AVENUE SUBWAY CONSTRUCTION |
| 2J | SANDY: BUILDING DESTROYED |
| 2K | STRUCTURALLY COMPROMISED BUILDING (LL33/08) |
| 2L | FACADE (LL11/98)- UNSAFE NOTIFICATION |
| 2M | MONOPOLE TRACKING COMPLAINT |
| 30 | BUILDING SHAKING/VIBRATING/STRUCT STABILITY AFFECTED |
| 31 | CERTIFICATE OF OCCUPANCY - NONE/ILLEGAL/CONTRARY TO CO |
| 32 | C OF O - NOT BEING COMPLIED WITH |
| 33 | COMMERCIAL USE - ILLEGAL |
| 34 | COMPACTOR ROOM/REFUSE CHUTE - ILLEGAL |
| 35 | CURB CUT/DRIVEWAY/CARPORT - ILLEGAL |
| 36 | DRIVEWAY/CARPORT - ILLEGAL |
| 37 | EGRESS - LOCKED/BLOCKED/IMPROPER/NO SECONDARY MEANS |
| 38 | EGRESS - EXIT DOOR NOT PROPER |
| 39 | EGRESS - NO SECONDARY MEANS |
| 3A | UNLICENSED/ILLEGAL/IMPROPER ELECTRICAL WORK IN PROGRESS |
| 3B | ROUTINE INSPECTION |
| 3C | PLAN COMPLIANCE INSPECTION |
| 3D | BICYCLE ACCESS WAIVER REQUEST - ELEVATOR SAFETY |
| 3E | BICYCLE ACCESS WAIVER REQUEST - ALTERNATE PARKING |
| 3G | RESTROOM NON-COMPLIANCE WITH LOCAL LAW 79/16 |
| 3H | DCP/BSA COMPLIANCE INSPECTION |
| 40 | FALLING - PART OF BUILDING |
| 41 | FALLING - PART OF BUILDING IN DANGER OF |
| 42 | FENCE - ILLEGAL |
| 43 | STRUCTURAL STABILITY AFFECTED |
| 44 | FIREPLACE/WOOD STOVE - ILLEGAL |
| 45 | ILLEGAL CONVERSION                                                        + |
| 46 | PA PERMIT - NONE |
| 47 | PA PERMIT - NOT BEING COMPLIED WITH |
| 48 | RESIDENTIAL USE - ILLEGAL |
| 49 | STOREFRONT OR BUSINESS SIGN/AWNING/MARQUEE/CANOPY - ILLEGAL |
| 4A | ILLEGAL HOTEL ROOMS IN RESIDENTIAL BUILDINGS |
| 4B | SEP - PROFESSIONAL CERTIFICATION COMPLIANCE AUDIT |
| 4C | EXCAVATION TRACKING COMPLAINT |
| 4D | INTERIOR DEMO TRACKING COMPLAINT |
| 4E | STALLED SITES TRACKING COMPLAINT |
| 4F | SST TRACKING COMPLAINT |
| 4G | ILLEGAL CONVERSION NO ACCESS FOLLOW-UP |
| 4H | V.E.S.T. PROGRAM (DOB & NYPD) |
| 4J | M.A.R.C.H. PROGRAM (INTERAGENCY) |
| 4K | BEST - DM TRACKING COMPLAINT |
| 4L | BEST - HIGH-RISE TRACKING COMPLAINT |
| 4M | BEST - LOW-RISE TRACKING COMPLAINT |
| 4N | RETAINING WALL TRACKING COMPLAINT |
| 4P | LEGAL/PADLOCK TRACKING COMPLAINT |
| 4S | SUSTAINABILITY ENFORCEMENT WORK ORDER |
| 4W | WOODSIDE SETTLEMENT PROJECT |
| 50 | SIGN FALLING - DANGER/SIGN ERECTION OR DISPLAY IN PROGRESS - ILLEGAL |
| 51 | ILLEGAL SOCIAL CLUB |
| 52 | SPRINKLER SYSTEM - INADEQUATE |
| 53 | VENT/EXHAUST - ILLEGAL/IMPROPER |
| 54 | WALL/RETAINING WALL - BULGING/CRACKED |
| 55 | ZONING - NON-CONFORMING |
| 56 | BOILER - FUMES/SMOKE/CARBON MONOXIDE |
| 57 | BOILER - ILLEGAL |
| 58 | BOILER - DEFECTIVE / INOPERATIVE / NO PERMIT |
| 59 | ELECTRICAL WIRING - DEFECTIVE/EXPOSED, IN PROGRESS |
| 5A | REQUEST FOR JOINT FDNY/DOB INSPECTION |
| 5B | NON-COMPLIANCE W/LIGHTWEIGHT MATERIALS |
| 5C | STRUCTURAL STABILITY IMPACTED - NEW BUILDING UNDER CONSTRUCTION |
| 5D | NON-COMPLIANCE W/TPPN 1/00 - VERTICAL ENLARGEMENTS |
| 5E | AMUSEMENT RIDE ACCIDENT/INCIDENT |
| 5F | COMPLIANCE INSPECTION |
| 5G | UNLICENSED/ILLEGAL/IMPROPER WORK IN PROGRESS |
| 5H | ILLEGAL ACTIVITY |
| 5J | MULTI AGENCY JOINT INSPECTION |
| 60 | ELECTRICAL WORK - IMPROPER |
| 61 | ELECTRICAL WORK - UNLICENSED, IN PROGRESS |
| 62 | ELEVATOR-DANGER CONDITION/SHAFT OPEN/UNGUARDED |
| 63 | ELEVATOR - DEFECTIVE / INOPERATIVE |
| 64 | ELEVATOR SHAFT - OPEN AND UNGUARDED |
| 65 | GAS HOOK-UP/PIPING - ILLEGAL OR DEFECTIVE |
| 66 | PLUMBING WORK - ILLEGAL/NO PERMIT(ALSO SPRINKLER/STANDPIPE) |
| 67 | CRANE - NO PERMIT/LICENSE/CERT/UNSAFE/ILLEGAL |
| 68 | CRANE/SCAFFOLD - UNSAFE/ILLEGAL OPERATIONS |
| 69 | CRANE/SCAFFOLD - UNSAFE INSTALLATION/EQUIPMENT |
| 6A | VESTING INSPECTION |
| 6B | SEMI-ANNUAL HOMELESS SHELTER INSPECTION: PLUMBING |
| 6C | SEMI-ANNUAL HOMELESS SHELTER INSPECTION: CONSTRUCTION |
| 6D | SEMI-ANNUAL HOMELESS SHELTER INSPECTION: ELECTRICAL |
| 6M | ELEVATOR - MULTIPLE DEVICES ON PROPERTY |
| 6S | ELEVATOR - SINGLE DEVICE ON PROPERTY/NO ALTERNATE SERVICE |
| 70 | SUSPENSION SCAFFOLD HANGING - NO WORK IN PROGRESS |
| 71 | SRO - ILLEGAL WORK/NO PERMIT/CHANGE IN OCCUP-USE                          + |
| 72 | SRO - CHANGE IN OCCUPANCY/USE |
| 73 | FAILURE TO MAINTAIN |
| 74 | ILLEGAL COMMERCIAL/MANUFACTURING USE IN RESIDENTIAL ZONE |
| 75 | ADULT ESTABLISHMENT |
| 76 | UNLICENSED/ILLEGAL/IMPROPER PLUMBING WORK IN PROGRESS |
| 77 | CONTRARY TO LL58/87 (HANDICAP ACCESS) |
| 78 | PRIVATELY OWNED PUBLIC SPACE/NON-COMPLIANCE |
| 79 | LIGHTS FROM PARKING LOT SHINING ON BUILDING |
| 7F | CSE - TRACKING COMPLIANCE |
| 7G | CSE - SWEEP |
| 80 | ELEVATOR NOT INSPECTED/ILLEGAL/NO PERMIT |
| 81 | ELEVATOR - ACCIDENT |
| 82 | BOILER - ACCIDENT/EXPLOSION |
| 83 | CONSTRUCTION -CONTRARY/BEYOND APPROVED PLANS/PERMITS                      + |
| 84 | FACADE - DEFECTIVE/CRACKING |
| 85 | FAILURE TO RETAIN WATER / IMPROPER DRAINAGE (LL103/89) |
| 86 | WORK CONTRARY TO STOP WORK ORDER |
| 87 | REQUEST FOR DECK SAFETY INSPECTION |
| 88 | SAFETY NET/GUARD RAIL-DAM/INADEQ/NONE(6FL.75 FT OR LESS) |
| 89 | ACCIDENT-CRANES/DERRICKS/SUSPENSION |
| 8A | CONSTRUCTION SAFETY COMPLIANCE ACTION |
| 90 | UNLICENSED/ILLEGAL ACTIVITY |
| 91 | SITE CONDITIONS ENDANGERING WORKERS |
| 92 | ILLEGAL CONVERSION OF MANUFACTURING/INDUSTRIAL SPACE |
| 93 | REQUEST FOR RETAINING WALL SAFETY INSPECTION |
| 94 | PLUMBING-DEFECTIVE/LEAKING/NOT MAINTAINED |
| 95 | BRONX 2ND OFFENSE PILOT PROJECT |
| 96 | UNLICENSED BOILER,ELECTRICAL,PLUMBING OR SIGN WORK COMPLETED |
| 97 | OTHER AGENCY JURISDICTION |
| 98 | REFER TO OPERATIONS FOR DETERMINATION |
| 99 | OTHER |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
| 1 | 2017-07-27 00:00:00 | Data Dictionary created |
| 2 | 2019-08-21 00:00:00 | Added category descriptions |

## Sheet: Sheet2

| Dropdown Options |
| Update Frequency | Annually |
|  | Biannually |
|  | Triannually |
|  | Quarterly |
|  | Monthly |
|  | Bimonthly |
|  | Weekly |
|  | Biweekly |
|  | Daily |
|  | Several times per day |
|  | As needed |
|  | Historical |
| Dataset Category | Business |
|  | City Government |
|  | Education |
|  | Environment |
|  | Health |
|  | Housing & Development |
|  | Public Safety |
|  | Recreation |
|  | Social Services |
|  | Transportaion |
