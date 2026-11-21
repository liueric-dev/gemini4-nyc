# Data dictionary: od-dob-ecb-violations-dict-dd-dob-ecb-violations-2019-07-10.xlsx

Source: https://data.cityofnewyork.us/d/6bgk-3dad
Extracted from: od-dob-ecb-violations-dict-dd-dob-ecb-violations-2019-07-10.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | DOB ECB Violations |
| Agency Name | Department of Buildings |
| Update Frequency | Weekdays |
| Dataset Description | This data set includes summonses issued by the Department of Buildings that are adjudicated by OATH/ECB.  Separately, civil penalties (commonly referred to as ‘DOB Violations’) are found in the DOB Safety Violations (for newer issuances) and DOB Violations (for older issuances) data sets. |
| Dataset Keywords | dob, buildings, violation ecb, nov |
| Dataset Category | Housing & Development |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. | Violations by the Department of Buildings that are adjudicated by OATH/ECB. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the idiosyncrasies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Term, Acronym, or Code Definitions | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) |
| ISN_DOB_BIS_EXTRACT | Unique identifier for the record assigned by Department of Buildings. |
| ECB_VIOLATION_NUMBER | Unique identifier for the Environmental Control Board (ECB) violation. |  | This number can be used to check the status on the OATH Hearings Division Case Status dataset. |
| ECB_VIOLATION_STATUS | Indicates whether or not the violation has been corrected. This is the status of the violation with DOB, not the status of the hearing with OATH. |  | Expected values =  • ACTIVE - still needs to be addressed • RESOLVE - the issue was either fixed with DOB or dismissed by OATH |
| DOB_VIOLATION_NUMBER | When an ECB violation is issued, Department of Buildings also issues a violation. This is the unique identifier for the violation issued by the Department of Buildings. See the DOB Violations dataset for more information. |
| BIN | Building Identification Number for the locatoin that received the violation. Assigned by Department of City Planning. |
| BORO | A number to indicate the NYC borough where the violation was issued. |  | Expected values:  • 1 = Manhattan • 2 = Bronx • 3 = Brooklyn • 4 = Queens • 5 = Staten Island |
| BLOCK | Tax Block for the location that received the violation. Assigned by the Department of Finance. |
| LOT | Tax Lot for the location that received the violation. Assigned by the Department of Finance. |
| HEARING_DATE | Date of the latest scheduled hearing for the respondent named on the violation to admit to it or contest the violation. |  | YYYYMMDD format  This date may change if, for example, the hearing is postponed. |
| HEARING_TIME | Time of the scheduled hearing for the respondent named on the violation to admit to it or contest the violation. |
| SERVED_DATE | Date that the violation was served to the respondent. |  | YYYYMMDD format |
| ISSUE_DATE | Date that the violation was issued. |  | YYYYMMDD format |
| SEVERITY | Indicated Violation Severity. |  | Expected values = Hazardous, Non-Hazardous, Unknown |
| VIOLATION_TYPE | Violations are grouped into types based on their infraction code. |  | Expected values = Administrative, Boilers, Construction, Cranes and Derricks, Elevators, HPD, Local Law, Padlock, Plumbing, Public Assembly, Quality of Life, Signs, Site Safety, Unknown, Zoning. |
| RESPONDENT_NAME | Name of the person or entity that the violation was issued to and who is responsible for any penalties. |
| RESPONDENT_HOUSE_NUMBER | House number for the mailing address for the RESPONDENT_NAME. |
| RESPONDENT_STREET | Street name for the mailing address for the RESPONDENT_NAME. |
| RESPONDENT_CITY | City for the mailing address for the RESPONDENT_NAME. |
| RESPONDENT_ZIP | Zip Code for the mailing address for the RESPONDENT_NAME. |
| VIOLATION_DESCRIPTION | Comments from the ECB inspector who issued the violation. | Some Elevator violations issued during a certain timeframe used alphanumeric codes in the description to further describe the violating condition. See the Elevator Codes sheet within this data dictionary document for the code list, which is also printed on the ECB Summons itself. | This field has a limit of 210 characters, which may cut the comment off mid-sentence. |
| PENALITY_IMPOSED | Amount of the penalty imposed by OATH after adjudication. |  | dollar amount |
| AMOUNT_PAID | Amount that was paid toward the penalty. |  | dollar amount |
| BALANCE_DUE | Amount that is left to be paid toward the penalty. |  | dollar amount |
| INFRACTION_CODE1 | The 3-digit code for the first infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION1 | The section of the applicable law for this violation. |
| INFRACTION_CODE2 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION2 | The section of the applicable law for this violation. |
| INFRACTION_CODE3 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION3 | The section of the applicable law for this violation. |
| INFRACTION_CODE4 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION4 | The section of the applicable law for this violation. |
| INFRACTION_CODE5 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION5 | The section of the applicable law for this violation. |
| INFRACTION_CODE6 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION6 | The section of the applicable law for this violation. |
| INFRACTION_CODE7 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION7 | The section of the applicable law for this violation. |
| INFRACTION_CODE8 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION8 | The section of the applicable law for this violation. |
| INFRACTION_CODE9 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION9 | The section of the applicable law for this violation. |
| INFRACTION_CODE10 | The 3-digit code for the next infraction on the violation. |  | Get a complete list of codes and their descriptions at http://www1.nyc.gov/assets/buildings/excel/penalty_schedule_with_codes.xlsx |
| SECTION_LAW_DESCRIPTION10 | The section of the applicable law for this violation. |
| AGGRAVATED_LEVEL | This indicates if the RESPONDENT_NAME has a pattern of ECB violations or that there was a fatality, serious injury or risk thereof at the place of occurrence. |
| HEARING_STATUS | Status of the hearing. |
| CERTIFICATION_STATUS | Indicates whether respondent/owner has certified the violation as corrected with DOB. |

## Sheet: Elevator Codes

| Elevator ECB Violation Codes |
| During a certain period of time, DOB inspectors were using the codes below to provide additional information about elevator violations. In the description of an ECB Violation, you might see a code like 05A10. |
| Using the below tables, you can see that this would indicate an issue with the "Car door/gate" (05) being "Altered" (A)  and that it should be "Repaired" (10). |
| I. Elevator Parts |  |  |  | II. Violating Conditions |  |  |  | III. Suggested Remedy |
| Inside Car | Code | Description |  |  | Code | Description |  |  | Code | Description |
|  | 1 | Emergency stop switch |  |  | A | Altered |  |  | 1 | Adjust |
|  | 2 | Alarm system/Outside Comm. |  |  | B | Insufficient |  |  | 2 | Clean |
|  | 3 | Car enclosure/Toe guard |  |  | C | Padlocked |  |  | 3 | Install Guards |
|  | 4 | Side emergency exit |  |  | D | Unsecured |  |  | 4 | Patch |
|  | 5 | Car door/gate |  |  | E | Rubbing |  |  | 5 | Perform & file test |
|  | 6 | Car door/gate contact |  |  | F | Lost motion |  |  | 6 | Properly secure |
|  | 7 | Door reopening device |  |  | G | Improper Fuses |  |  | 7 | Provide |
|  | 8 | Car floor to landing sill |  |  | H | Worn |  |  | 8 | Regroove |
|  | 9 | Car floor |  |  | I | Damaged |  |  | 9 | Remove |
|  | 10 | Car door gibs |  |  | J | Misaligned |  |  | 10 | Repair |
|  | 11 | Car button station |  |  | K | Rusted |  |  | 11 | Replace |
|  | 12 | Car lighting |  |  | L | Defective |  |  | 12 | Reshackle |
|  | 13 | Emergency lighting |  |  | M | Missing |  |  | 13 | Seal |
|  | 14 | Car mirror |  |  | N | By-passed |  |  | 14 | Shorten |
|  | 15 | Certificate frame/Capacity plate |  |  | O | Dirty |  |  | 15 | Tag Device |
| Outside Hoistway | Code | Description |  |  | P | No means of access |  |  | 16 | Provide means of access |
|  | 16 | Hoistway doors |  |  | Q | Unguarded |  |  | 17 | Re-Inspection required |
|  | 17 | Hoistway door gibs |  |  | R | Illegal |
|  | 18 | Hoistway door reinforcements |  |  | S | Not fire retardant |
|  | 19 | Hoistway door safety retainer |  |  | T | Unlabeled |
|  | 20 | Vision panel |  |  | U | Device not tagged |
|  | 21 | Interlocks |  |  | V | Not level |
|  | 22 | Parking device |  |  | W | Unlocked |
|  | 23 | Hall button station |  |  | X | Inoperative |
|  | 24 | Indicators |  |  | Y | Oil leak |
|  | 25 | Required signage |  |  | Z | Water leak |
| Top of Car | Code | Description |  |  | AA | Carbon buildup |
|  | 26 | Top emergency exit cover |  |  | BB | Expired tag |
|  | 27 | Governor release carrier |
|  | 28 | Door hangers & connectors |
|  | 29 | Door operator |
|  | 30 | Normal/Final limits |
|  | 31 | Leveling unit |
|  | 32 | Guide shoes/Roller guides |
|  | 33 | Counterweight |
|  | 34 | Hoistway/Safety operated switch |
|  | 35 | Electric wiring |
|  | 36 | Pipes and ducts |
|  | 37 | Overhead & Deflector sheave |
|  | 38 | Traveling cable & junction |
|  | 39 | Car top/out rigger |
| Machine Room | Code | Description |
|  | 40 | Machine room/Control room space |
|  | 41 | Machine room door |
|  | 42 | Controller - selector |
|  | 43 | Reverse phase relay |
|  | 44 | Traction sheave |
|  | 45 | Governor/Governor switch |
|  | 46 | Ventilation/Ambient temp |
|  | 47 | Drum |
|  | 48 | Pump unit/Tank |
|  | 49 | Drum machine limit switch |
|  | 50 | Generator |
|  | 51 | Slack rope switch |
|  | 52 | Hoist ropes/Suspension means |
|  | 53 | Governor ropes |
|  | 54 | Car counterweight rope |
|  | 55 | Drum counterweight rope |
|  | 56 | Hoist machine/Hoist motor |
|  | 57 | Fire extinguisher |
|  | 58 | Worm/Gear/Bearings |
|  | 59 | Machine brake |
|  | 60 | Lighting machine space |
|  | 61 | Machine disconnect switch |
|  | 62 | Commutator |
|  | 63 | Motor brushes |
|  | 64 | NYC Device # |
|  | 65 | Unintended car movement |
|  | 66 | Emergency brakes/rope gripper |
|  | 67 | Communication |
|  | 68 | Maintenance log/MCP |
|  | 69 | Code data place |
| Pit | Code | Description |
|  | 70 | Pit/Access |
|  | 71 | Pit light |
|  | 72 | Pit stop switch |
|  | 73 | Car guide-rails & brackets |
|  | 74 | Cwt. Guide-rails & brackets |
|  | 75 | Buffers |
|  | 76 | Car safety & tail rope |
|  | 77 | Underside platform |
|  | 78 | Tension Weight |
|  | 79 | Comp/chains/rope/switch |
|  | 80 | Counterweight runby/Signage |
|  | 81 | Cylinder piston |
|  | 82 | Plunger gripper |
| Escalator/Moving Walk | Code | Description |
|  | 83 | Fire shutters |
|  | 84 | Skirt switch/Skirt deflector |
|  | 85 | Step and skirt clearance |
|  | 86 | Comb plate/Comb plate teeth |
|  | 87 | Landing plate/Impact switches |
|  | 88 | Handrails/Handrail safeties |
|  | 89 | Step/thread |
|  | 90 | Starting switches |
|  | 91 | Emergency stop button |
|  | 92 | Decking and ballistrades |
|  | 93 | Ceiling guards/Anti slide device |
|  | 94 | Deck barricades |
|  | 95 | Internal safeties |
|  | 96 | Safety Signage |
| All Types | Code | Description |
|  | 97 | Entire device |
|  | 98 | Current five year test |
|  | 99 | Current one year test |
|  | 100 | Miscellaneous |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
| 1 | 2017-10-05 00:00:00 | Data dictionary created |
| 2 | 2019-07-10 00:00:00 | Added Elevator Codes sheet |

## Sheet: Dropdown Options

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
|  | Transportation |
