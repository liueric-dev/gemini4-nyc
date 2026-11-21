# Data dictionary: od-hpd-violations-dict-hpd-code-violations-data-dictionary.xlsx

Source: https://data.cityofnewyork.us/d/wvxf-dwi5
Extracted from: od-hpd-violations-dict-hpd-code-violations-data-dictionary.xlsx

## Sheet: Dataset Information

| Data Dictionary - Dataset Information |
| Dataset Name | Housing Maintenance Code Violations |
| Dataset URL | https://data.cityofnewyork.us/d/wvxf-dwi5 |
| Data Provided by The name of the NYC agency providing this data to the public. | Department of Housing Preservation and Development (HPD) |
| Each row is a...  The unit of analysis/level of aggregation of the dataset | Each row in this dataset contains discrete information about one violation of the New York City Housing Maintenance Code or New York State Multiple Dwelling Law. Each violation is identified using a unique Violation ID. These Laws are in place to provide requirements for the maintenance of residential dwelling units within New York City. |
| Publishing Frequency How often changed data is published to this dataset. For an automatically updated dataset, this is the frequency of that automation | Daily |
| Data Change Frequency How often the data underlying this dataset is changed | Daily |
| Frequency Details Additional details about the publishing or data change frequency, if needed |
| Dataset Description Overview of the information this dataset contains, including overall context and definitions of key terms. This field may include links to supporting datasets, agency websites, or external resources for additional context. | This dataset displays violations related to several orders issued by Housing Inspectors to privately owned/managed buildings pursuant to the New York City Housing Maintenance Code (HMC) or the New York State Multiple Dwelling Law (MDL). Violations issued to New York City Housing Authority (NYCHA) buildings are contained in a separate dataset. To learn more about HPD Code Enforcement, see https://www.nyc.gov/site/hpd/services-and-information/code-enforcement.page. |
| Why is this data collected? Purpose behind the collection of this data, including any legal or policy requirements for this data by NYC Executive Order, Local Law, or other policy directive. | This data is collected for internal and external reporting purposes. Pursuant to New York City’s Housing Maintenance Code, the Department of Housing Preservation and Development (HPD) issues violations against conditions, in rental dwelling units and buildings, that have been verified to violate the New York City Housing Maintenance Code (HMC) or the New York State Multiple Dwelling Law (MDL). |
| How is this data collected? The methods used to create and update this dataset, including what cleaning or processing was involved prior to dataset publication. If data collection includes interpreting physical information this field includes technical details.  If data collection includes fielding applications, requests, or complaints, this field includes details about the forms, applications, and processes used. | This data is collected through various internal HPD systems. Violations are issued by Housing Inspectors after a physical inspection is conducted (except for class I violations which are generally administratively issued). Violations are issued in four classes: Class A (non-hazardous), Class B (hazardous), Class C (immediately hazardous) and Class I (information orders).  For more information on violations, see https://www1.nyc.gov/site/hpd/owners/compliance-clear-violations.page |
| How can this data be used? Examples of and/or links to projects or agency operations that have used this dataset. Where relevant, includes links to online projects, agency websites, visualizations, maps, or dashboards. What are some questions one might answer using this dataset? | Using other HPD datasets, such as the Building File or the Registration File, a user can link together violations issued for given buildings or for given owners. You can explore a variety of questions like: How many violations did HPD issue in Calendar year 2018 in Manhattan? What types of violations did HPD issue in Calendar year 2018 in Brooklyn? How many violations that HPD issued are currently open in Staten Island? |
| What are the unique characteristics or limitations of this dataset? Unique characteristics of this dataset to be aware of, specifically, constraints or limitations to the use of the data. | The base data for this file is all violations open as of October 1, 2012.  Violation data is updated daily.  The daily update includes both new violations and updates to the status of previously issued violations. An open violation is a violation which is still active on the Department records. See the status table for determining how to filter for open violations versus closed violations, and within open violations for a more detailed current status.  The property owner may or may not have corrected the physical condition if the status is open. The violation status is closed when the violation is observed/verified as corrected by HPD or as certified by the landlord. The processes for having violations dismissed are described at https://www.nyc.gov/site/hpd/services-and-information/clear-violations.page |
| Additional geospatial information For any datasets with geospatial data, specify the coordinate reference system or projection used and other relevant details. |

## Sheet: Column Information

| Data Dictionary - Column Information |
| Column Name | Column Description | Expected/Allowed Values | Field Limitations | Additional Notes |
| Name of the column exactly as it appears in the dataset. | A brief, plain-language explanation of what the data in the column means. | Specifies if there is an expected range and/or format of possible values. For example, if the data type is Date & Time, this field will note whether the timestamp is MM/DD/YYYY or MM/YYYY. If the Column Name is ice cream, this field might note that values can be Chocolate, Vanilla or Strawberry.  If relevant, this field specifies the unit of measurement of the data field, e.g. thousands, millions, $ value, miles, feet, year, etc. | Describes any unique characteristics or potential analytical limitations presented by this field, including:  - the reasoning for any null, zero, or empty values in the data - if the data in the column was integrated from another dataset or organization - if the data covered includes a different time period - the source of the column and how the data in the column was generated.   For example, information on how the data in this column was generated can include  whether the data was self-reported directly by a person, system generated by a database or agency system, derived through analytical manipulation of other fields or records; or obtained from a different agency. | Provides any additional relevant information about the data in the column, including:  - definitions of acronyms, special term or codes, or jargon that appears in the field values; - the meaning of confusing or non-intuitive values in the data;  - how the information in this column relates to information in other columns; - other unique details about this column. |
| Violation ID | Unique identifier of Violation |  | Data Type: Number |
| Building ID | Unique identifier of building |  | Data Type: Number |
| Registration ID | Unique identifier of valid registration information |  | Data Type: Number |
| BoroID | Borough code | 1 = Manhattan, 2 = Bronx, 3 = Brooklyn, 4 = Queens, 5 = Staten Island | Data Type: Number |
| Borough | The borough where the building is located | Bronx, Brooklyn, Manhattan, Queens, Staten Island | Data Type: Plain Text |
| House Number | The street number in the building's address. E.g.: the house number is '100' in '100 Gold Street' |  | Data Type: Number |
| LowHouseNumber | If there is a range for a building, the lowest house number in the building’s address. |  | Data Type: Number |
| HighHouseNumber | If there is a range for a building, the highest house number in the building’s address. |  | Data Type: Number |
| StreetName | The name of the street in the building's address. E.g.: the street name is 'Gold Street' in '100 Gold Street' |  | Data Type: Plain Text |
| StreetCode |  |  | Data Type: Number |
| Postcode | The postcode where the building is located |  | Data Type: Plain Text |
| Apartment | Apartment in violation, if applicable |  | Data Type: Plain Text |
| Story | Floor of violation |  | Data Type: Number |
| Block | Tax block for building |  | Data Type: Number |
| Lot | Tax lot for building |  | Data Type: Number |
| Class | Indicator of seriousness of the violations, where A is the least serious and C is the most serious. Class I violation are informational notices that do not have certification periods associated; they indicate something about the status of the property: that an Order is open against the property (example: Order to Repair/Vacate Order) or that a property is vacant or that a property is not validly registered. | A,B,C,I | Data Type: Plain Text |
| InspectionDate | Date when the violation was observed |  | Data Type: Date & Time |
| ApprovedDate | Date when the violation was approved |  | Data Type: Date & Time |
| OriginalCertifyByDate | Original date by which the owner was to inform HPD that the violation was corrected |  | Data Type: Date & Time |
| OriginalCorrectByDate | Original date by which the owner was to correct the violation |  | Data Type: Date & Time |
| NewCertifyByDate | If a postponement is granted, a new certify by date is established |  | Data Type: Date & Time |
| NewCorrectByDate | If a postponement is granted, a new correct by date is established |  | Data Type: Date & Time |
| CertifiedDate | Date when the violation was certified by the owner |  | Data Type: Date & Time |
| OrderNumber | Reference to the abstract description of the violation condition which cites a specific section of the law which is in violation | See the tab labeled OrderNumber. | Data Type: Number | Here are some examples of groups of order numbers that are often queried together: ●	Lead-based paint hazards: “616”, “617” ●	Heat violations: “666”, “664”, “966”, “964” ●	Hot water violations: “670”, “970” ●	Mold violations: “550” |
| NOVID | Unique identifier of the Notice of Violation sent to the owner |  | Data Type: Number |
| NOVDescription | Description of the violation |  | Data Type: Plain Text |
| NOVIssueDate | Date when the NOV was sent |  | Data Type: Date & Time |
| CurrentStatusID | Unique identifier affiliated with the current violation status | See the tab labeled CurrentStatus | Data Type: Number |
| CurrentStatus | Current violation status | See the tab labeled CurrentStatus | Data Type: Plain Text |
| CurrentStatusDate | Date when the current status went into effect |  | Data Type: Date & Time |
| NovType | Original/Reissued Notice of Violation. | For more information on the reissuance process, see: https://www.nyc.gov/site/hpd/services-and-information/clear-violations.page | Data Type: Plain Text |
| ViolationStatus | Status of Violation | Open, Close | Data Type: Plain Text |
| RentImpairing | A rent-impairing violation is a condition within a multiple dwelling which constitutes, or if not promptly corrected will constitute, a fire hazard or a serious threat to the life, health or safety of occupants thereof (New York State Multiple Dwelling Law Section 302). |
| Latitude | Latitude and longitude specify the location of the property on the earth's surface. The coordinates provided are an estimate of the location based on the street segment and address range. |  | Data Type: Location |
| Longitude |  |  | Data Type: Location |
| CommunityBoard | Community Board indicates the New York City Community District where the building is located |  | Data Type: Number |
| CouncilDistrict | Council District indicates the New York City Council District where the building is located |  | Data Type: Number |
| CensusTract | Geographic area defined by the U.S. Census Bureau for the various decennial censuses. |  | Data Type: Number |
| BIN | The BIN (Building Identification Number) is a unique identifier for each building in the City. |  | Data Type: Number |
| BBL | BBL is a unique identifier for each tax lot in the city. |  | Data Type: Number |
| NTA | Neighborhood Tabulation Area indicates the New York City Neighborhood Tabulation Area where the building is located. |  | Data Type: Plain Text |

## Sheet: Current Status

| Data Dictionary - Current Status |
| SeqNo | ShortName | LongName | Definition | OPEN OR CLOSED? |
| 1 | OPEN | VIOLATION OPEN | The violation is active and still requires action from the owner or the violation has been properly certified and is pending the statutory period for reinspection or dismissal. | OPEN |
| 2 | NOV SENT | NOV SENT OUT | The Notice of Violation was sent to the registered owner or "Owner of the Premises". | OPEN |
| 3 | NOV CERT | NOV CERTIFIED ON TIME | The violation was certified as corrected by the Owner on time and properly. | OPEN |
| 4 | NOV LATE | NOV CERTIFIED LATE | The violation was certified as corrected by the Owner but was not submitted to HPD in a timely manner.  Therefore, the certification was not acceptable. | OPEN |
| 6 | POSTP GRANT | CERTIFICATION POSTPONMENT GRANTED | The property owner applied to HPD to extend the correction date for the violation, and HPD granted the request.  The new correction and certification date is in the columns NEW CORRECT BY DATE and  NEW CERT BY DATE. | OPEN |
| 7 | POSTP DENIED | CERTIFICATION POSTPONMENT DENIED | The property owner applied to HPD to extend the correction date for the violation, and HPD denied the request.  The condition must be corrected by the original correction date. | OPEN |
| 8 | FALSE CERT | FALSE CERTIFICATION | The violation was certified as corrected by the Owner on time and properly.  A subsequent re-inspection of the condition by HPD found that condition had not been properly corrected.  The violation is open and is subject to civil penalties for false certification. | OPEN |
| 11 | OPEN | VIOLATION WILL BE REINSPECTED | HPD will be attempting to reinspect this violation. | OPEN |
| 19 | DISMISSED/CLOSED | VIOLATION CLOSED | The violation has been closed. | CLOSED |
| 20 | DEFECT LETTER | DEFECT LETTER ISSUED | The violation condition was observed corrected by the Department.  However, documentation required to close the violation has not yet been received and the violation remains open. A notice was generated to the owner regarding the documentation required to close the violation. | OPEN |
| 21 | NOT COMPLIED | NOT COMPLIED WITH | A reinspection of the violation found that the condition still exists as of the status date. | OPEN |
| 22 | 1 NO ACCESS | FIRST NO ACCESS TO RE- INSPECT VIOLATION | HPD attempted to reinspect the violation but there was no access.  The violation remains open. | OPEN |
| 23 | 2 NO ACCESS | SECOND NO ACCESS TO RE-INSPECT VIOLATION | HPD made a second attempt to reinspect the violation but there was no access.  The violation remains open. | OPEN |
| 24 | OPEN | VIOLATION REOPEN | The violation was returned to open status from closed. | OPEN |
| 27 | INFO NOV SENT | INFO NOV SENT OUT | Info NOVs are notice that an order has been issued by the Department.  These orders do not have associated certification or correction dates and are used to serve notice upon current and future owners regarding open agency Orders. | OPEN |
| 28 | CERT INVALID | INVALID CERTIFICATION | A certification has been submitted but was not acceptable due to a defect in the certification documentation. | OPEN |
| 36 | PARTIAL ACCESS | COMPLIED IN ACCESS AREA | This status applies only to window guard violations.  An inspection resulted in a finding that some window guards had been installed, but that there was no access to confirm installation in all windows. | OPEN |
| 10 | CIV 14 MAILED | CIV 14 MAILED | This status indicates that a notice was mailed to the tenant indicating that an owner certification of correction has been received. This notice advises the tenant that they can challenge the certification. | OPEN |

## Sheet: Order Number

| Data Dictionary - Order Number |
| Order Number | Full Description | Category | Short Description | MD/PD |
| 4 | § 213, SUBD. 5 M/D LAW  DISCONTINUE USE OF INTERIOR ROOM FOR LIVING OR PROVIDE A SINGLE OPENING OF AT LEAST 60 PERCENT OF AREA OF THE PARTITION TO ROOM HAVING WINDOW OPENING DIRECTLY TO STREET OR YARD | LIGHTS AND VENTILATION ROOMS AND PUBLIC HALLS | 4 - INTERIOR ROOM IN OLD LAW TENEMENT | MD/PD |
| 6 | § 36, 66, 67, 178, 217 M/D LAW  MAINTAIN PROPER VENTILATION BY REMOVING WRAPPINGS AND/OR OBSTRUCTIONS FROM THE LOUVRES OR VENTILATORS OR WINDOWS OR SKYLIGHT | LIGHTS AND VENTILATION ROOMS AND PUBLIC HALLS | 6 - VENTILATION OBSTRUCTED | MD/PD |
| 7 | § 178, 217 M/D LAW  PROVIDE FIXED VENTILATION OF AT LEAST 40 SQ.IN. DIRECTLY OVER STAIRWELL | LIGHTS AND VENTILATION ROOMS AND PUBLIC HALLS | 7- PROVIDE 40 SQ.IN OF VENTILATION | MD/PD |
| 8 | § 178, 217 M/D LAW  PROVIDE A VENTILATING SKYLIGHT DIRECTLY OVER THE STAIRWELL | LIGHTS AND VENTILATION ROOMS AND PUBLIC HALLS | 8 - PROVIDE A VENTILATION SKYLIGHT OVER STAIRWELL | MD/PD |
| 10 | § 178, 217 M/D LAW  PROVIDE SKYLIGHT VENTILATION OF AT LEAST 40 SQ.IN. OR FIXED OR MOVABLE LOUVRES, OR MOVABLE SASH | LIGHTS AND VENTILATION ROOMS AND PUBLIC HALLS | 10 - PROVIDE 40 SQ.IN. OF VENTILATION OF SKYLIGHT | MD/PD |
| 11 | § 178, 217 M/D LAW  MAKE EFFECTIVE THE LIGHT AND VENTILATION OF SKYLIGHT BY REMOVING FROM BENEATH SAME THE DOMELIGHT LOCATED IN CEILING | LIGHTS AND VENTILATION ROOMS AND PUBLIC HALLS | 11 - REMOVE DOME LIGHT IN CEILING | MD/PD |
| 30 | § 78 M/D LAW  PROPERLY PAVE THE FLOOR WITH 4 INCHES OF CONCRETE | LIGHTS AND VENTILATION ROOMS AND PUBLIC HALLS | 30 - CONCRETE FLOOR | MD/PD |
| 51 | § 12 M/D LAW  DISCONTINUE THE STORAGE OF COMBUSTIBLE MATERIAL | UNLAWFUL USE | 51 - DISCONTINUE STORAGE OF COMBUSTIBLES | MD/PD |
| 57 | § 12 M/D LAW  DISCONTINUE THE UNLAWFUL KEEPING OF | UNLAWFUL USE | 57 - PIGEONS, ETC. | MD/PD |
| 65 | § 66 M/D LAW  DISCONTINUE THE UNLAWFUL USE AS A LODGING HOUSE UNLESS AND UNTIL A CERTIFICATE OF OCCUPANCY IS OBTAINED FOR SUCH USE. | UNLAWFUL USE | 65 - DISCONTINUE LODGING HOUSE | MD/PD |
| 69 | § 61 M/D LAW  DISCONTINUE USE UNLESS AND UNTIL AN APPROVED APPLICATION IS FILED AND A CERTIFICATE OF OCCUPANCY IS OBTAINED | UNLAWFUL USE | 69 - MANUFACTURING BUSINESS, ETC. | MD/PD |
| 72 | § 61 M/D LAW  DISCONTINUE THE MANUFACTURING BUSINESS | UNLAWFUL USE | 72 - MANUFACTURING BUSINESS | MD/PD |
| 80 | § 231 M/D LAW  PROVIDE LEGAL SECOND MEANS OF EGRESS AND FILE APPLICATION FOR APPROVAL BEFORE DOING THE WORK | FIRE EGRESS AND PROTECTION | 80 - NO LEGAL SECOND MEANS OF EGRESS | MD |
| 81 | § 187 M/D LAW  PROVIDE A SPRINKLER SYSTEM OR A LEGAL SECOND MEANS OF EGRESS AND FILE APPLICATION FOR APPROVAL BEFORE DOING THIS WORK | FIRE EGRESS AND PROTECTION | 81 - NO SPRINKLER OR FIRE ESCAPE | MD |
| 84 | §  67 M/D LAW  POST A PRINTED SCALE FLOOR PLAN SHOWING MEANS OF EGRESS, AT | FIRE EGRESS AND PROTECTION | 84 - POST MEANS OF EGRESS PLAN | MD |
| 106 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  PROVIDE A SHOE PROPERLY SECURED TO BOTTOM OF STRING OF DROPLADDER | FIRE EGRESS AND PROTECTION | 106 - PROVIDE SHOE FOR DROP LADDER | MD |
| 109 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  PROVIDE A STOP AT TOP OF GUIDE RODS SO AS TO PREVENT REMOVAL OF DROPLADDER | FIRE EGRESS AND PROTECTION | 109 - PROVIDE  STOP FOR GUIDE RODS | MD |
| 118 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  PROPERLY BRACE | FIRE EGRESS AND PROTECTION | 118 - BRACE | MD |
| 121 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  SPLICE WITH ADEQUATE SPLICE PLATE | FIRE EGRESS AND PROTECTION | 121 - SPLICE WITH SPLICE PLATE | MD |
| 135 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  CLOSE THE UNNECESSARY OPENING | FIRE EGRESS AND PROTECTION | 135 - CLOSE OPENINGS | MD |
| 142 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  BRACE AND SUPPORT BALCONY WITH SUITABLE TIE RODS OR SUSPENSION RODS | FIRE EGRESS AND PROTECTION | 142 - BRACE BALCONY WITH TIE RODS | MD |
| 159 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  SAFEGUARD EGRESS BY PROVIDING IRON GUARD RAILS 3 FT 6 IN HIGH AROUND SKYLIGHT | FIRE EGRESS AND PROTECTION | 159 - SAFEGUARD EGRESS | MD |
| 160 | § 62, 187, 231 M/D LAW AND DEPT. RULES AND REGS.  SAFEGUARD EGRESS BY PROVIDING IRON GUARD RAILS OR PARAPET WALLS 3 FT 6 IN HIGH AND EXTENDING A MINIMUM OF 4 FT 0 IN BEYOND EITHER SIDE OF BULKHEAD/SCUTTLE OPENING AT ROOF | FIRE EGRESS AND PROTECTION | 160 - SAFEGUARD ROOF EGRESS | MD |
| 176 | § 53,187,231 M/D LAW & DEPT RULES & REG. PROVIDE MEANS OF EGRESS FROM YARD TO STREET BY FIREPROOF PASSAGEWAY FOR WHICH APPLICATION MUST BE FILED FOR APPROVAL,OR BY UNLOCKED DOOR OR GATE IN FENCE TO ADJOINING PREMISES WITH CONSENT OF ADJACENT OWNER. | FIRE EGRESS AND PROTECTION | 176 - PROVIDE FIREPROOF PASSAGE OR GATE IN FENCE | MD |
| 181 | § 53, 187, 231 M/D LAW AND DEPARTMENT RULES AND REGULATIONS.  PROVIDE A FIREPROOF PASSAGEWAY FROM FIRE ESCAPES AT REAR TO STREET AND FILE APPLICATION FOR APPROVAL BEFORE DOING THIS WORK. | FIRE EGRESS AND PROTECTION | 181 - PROVIDE FIREPROOF PASSAGE | MD |
| 188 | § 185, 240  M/D LAW  PROPERLY FIRE RETARD IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT THE CELLAR CEILING | FIRE EGRESS AND PROTECTION | 188 - FIRE RETARD CELLAR CEILING | MD |
| 208 | § 66, 67, 104, 147, 188, 233 M/D LAW  PROVIDE WITH PROPER HINGES THE SCUTTLE COVER AT ROOF. | FIRE EGRESS AND PROTECTION | 208 - PROVIDE HINGES | MD |
| 209 | § 233 M/D LAW  REMOVE DOOR FROM CLOSET LEADING TO SCUTTLE OPENING IN ROOF AT | FIRE EGRESS AND PROTECTION | 209- DOOR ON SCUTTLE CLOSET | MD |
| 213 | § 61 MDL: SEAL WITH FIRE RETARDING MATERIAL OR PROVIDE WITH FIREPROOF SELF-CLOSING DOOR AND ASSEMBLY THE OPENING LEADING FROM STORE TO PUBLIC HALL | FIRE EGRESS AND PROTECTION | 213 - SEAL UP OR PROVIDE FIREPROOF SELF-CLOSING DOOR | MD |
| 214 | § 189, SUBD. 5 M/D LAW  REMOVE SASH IN PARTITION BETWEEN ROOM AND PUBLIC HALL AND SEAL OPENING WITH MATERIAL SIMILAR TO ADJACENT WALL | FIRE EGRESS AND PROTECTION | 214 - REMOVE SASH | MD |
| 219 | § 190 M/D LAW  SOLIDLY CLOSE THE SPACE BETWEEN THE TREADS OF INSIDE STAIRS | FIRE EGRESS AND PROTECTION | 219 - OPEN TREADS | MD |
| 222 | § 242 M/D LAW PROVIDE UNDER COMPLETED PERMIT,A PROPER ENCLOSURE WITH FIREPROOF SELFCLOSING DOORS AND ASSEMBLIES,AT THE TOP AND THE BOTTOM OF THE CELLAR STAIRS, | FIRE EGRESS AND PROTECTION | 222 - PROVIDE CELLAR STAIR ENCLOSURE | MD |
| 225 | § 51 M/D LAW  PROVIDE UNDER COMPLETED PERMIT, A PROPER ENCLOSURE FOR THE ELEVATOR SHAFT, | FIRE EGRESS AND PROTECTION | 225 - PROVIDE ENCLOSURE | MD |
| 226 | § 65 M/D LAW  PROVIDE UNDER COMPLETED PERMIT, A PROPER ENCLOSURE FOR THE CENTRAL HEATING PLANT, | FIRE EGRESS AND PROTECTION | 226 - PROVIDE ENCLOSURE AT | MD |
| 230 | § 192 M/D LAW  PROVIDE AN INDEPENDENT ENTRANCE FROM OUTSIDE THE DWELLING TO CELLAR AND FILE APPLICATION FOR APPROVAL BEFORE DOING THE WORK | FIRE EGRESS AND PROTECTION | 230 - OUTSIDE ENTRANCE TO CELLAR | MD |
| 462 | § 212 M/D LAW  ARRANGE THE DOOR OR WINDOW SO THAT IT MAY BE READILY OPENED AND PROPER ACCESS AFFORDED TO THE BOTTOM OF | SHAFTS AND COURTS | 462 - PROVIDE FREE ACCESS TO BOTTOM OF SHAFT OR COURTS | MD |
| 463 | § 212 M/D LAW  PROVIDE A STATIONARY IRON LADDER EXTENDING FROM THE SILL OF THE LOWERS WINDOW TO THE BOTTOM OF | SHAFTS AND COURTS | 463 - PROVIDE STATIONARY IRON LADDER | MD |
| 483 | § 62 M/D LAW  REARRANGE TELEVISION AND/OR RADIO ANTENNA TO BE AT LEAST 10 FEET ABOVE ROOF AND NOT ATTACHED TO ANY FIRE ESCAPE OR SOIL OR VENT LINE | MISCELLANEOUS | 483 - TELEVISION OR RADIO ANTENNA | MD/PD |
| 484 | § 329, M/D LAW AND DEPT. RULES AND REGS.  PROVIDE A COMPLETED CERTIFICATE OF INSPECTION VISITS IN A PROPER FRAME AT OR NEAR MAILBOXES, BOTTOM EDGE OF FRAME BETWEEN 48-62 INCHES ABOVE FLOOR | POSTING/SIGNAGE | 484 - IV-1. MAILBOXES PRESENT | MD/PD |
| 485 | § 329, M/D LAW AND DEPT. RULES AND REGS.  PROVIDE A COMPLETED CERTIFICATE OF INSPECTION VISITS IN A PROPER FRAME READILY ACCESSIBLE FOR SIGNATURE, BOTTOM EDGE OF FRAME BETWEEN 48-62 INCHES ABOVE FLOOR AT | POSTING/SIGNAGE | 485 - IV-1. NO MAILBOXES PRESENT | MD/PD |
| 491 | § 300 M/D LAW  FILE PLANS AND APPLICATION AND LEGALIZE THE FOLLOWING ALTERATION OR RESTORE TO THE LEGAL CONDITION EXISTING PRIOR TO THE MAKING OF SAID ALTERATION | ALTERATIONS | 491 - FILE PLANS OR RESTORE | MD/PD |
| 494 | § 4, 8, 25, 67 M/D LAW  THE PREMISES IS CLASSIFIED AS A MULTIPLE DWELLING AND IS BEING MAINTAINED IN VIOLATION OF THE ABOVE SECTIONS. FILE AN ALTERATION APPLICATION AND PLANS 1/8 INCH SCALE AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE SUCH USE. | HOTEL AND CERTAIN OTHER CLASS A & CLASS B DWELLINGS | 494 - FILE PLANS TO LEGALIZE | MD |
| 495 | § 300, 301, 302, M/D LAW  FILE PLANS AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE THE FOLLOWING ALTERATION OR RESTORE PREMISES TO PRIOR LEGAL CONDITION | HOTEL AND CERTAIN OTHER CLASS A & CLASS B DWELLINGS | 495 - FILE PLANS & OBTAIN CERTIFICATE OF OCCUPANCY OR RESTORE | MD |
| 496 | §27-2033.3(A) CORRECT FAILURE TO COMPLY WITH TENANT NOTIFICATION REQUIREMENTS REGARDING INTERNET CAPABLE TEMPERATURE REPORTING DEVICES. | HEAT SENSOR PROGRAM | 496 - CORRECT FAILURE TO COMPLY WITH TENANT NOTIFICATION | MD |
| 497 | §27-2033.3(B) CORRECT FAILURE TO INSTALL AN INTERNET CAPABLE TEMPERATURE REPORTING DEVICE IN ONE LIVING ROOM IN APARTMENT | HEAT SENSOR PROGRAM | 497 - CORRECT FAILURE TO INSTALL TEMPERATURE REPORTING DEVICE | MD |
| 498 | § 27-2033.3(C); (D) CORRECT FAILURE TO PROPERLY MAINTAIN A REQUIRED INTERNET CAPABLE TEMPERATURE REPORTING DEVICE IN APARTMENT. | HEAT SENSOR PROGRAM | 498 -CORRECT FAILURE TO PROPERLY MAINTAIN A REPORTING DEVICE | MD |
| 499 | § 27-2033.3(E) CORRECT FAILURE TO MAINTAIN REQUIRED RECORDS REGARDING INTERNET CAPABLE TEMPERATURE REPORTING DEVICES AND SUBMIT SUCH RECORDS TO THE DEPARTMENT UPON REQUEST. | HEAT SENSOR PROGRAM | 499 - CORRECT FAILURE TO MAINTAIN R RECORDS REGARDING T DEVICES | MD |
| 500 | § 26-1103 ADMIN. CODE: POST AND MAINTAIN A PROPER NOTICE ON WALL OF THE ENTRANCE STORY IN ENGLISH AND SPANISH ON THE AVAILABILITY OF THE AGENCY’S HOUSING INFORMATION GUIDE. A SAMPLE NOTICE CAN BE FOUND AT WWW.NYC.GOV/HPD. | POSTING/SIGNAGE | 500 - POST HOUSING INFORMATION GUIDE NOTICE | MD |
| 501 | § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE | MAINTENANCE | 501 - REPAIR | MD |
| 502 | § 27-2005 ADM CODE  PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE | MAINTENANCE | 502 - REPAIR WITH SIMILAR MATERIAL | MD |
| 503 | § 27-2005 ADM CODE  MAKE SAFE BY PROPERLY REPAIRING THE STRUCTURAL DEFECT | MAINTENANCE | 503 - STRUCTURAL DEFECT | MD |
| 504 | § 27-2005 ADM CODE  PROVIDE | MAINTENANCE | 504 - PROVIDE | MD |
| 505 | § 27-2005 ADM CODE  REPLACE WITH NEW THE BROKEN OR DEFECTIVE | RETIRED | 505 - RETIRED | MD |
| 506 | § 27-2005 ADM CODE  REPLACE WITH NEW THE MISSING | MAINTENANCE | 506 - REPLACE | MD |
| 507 | § 27-2005 ADM CODE  REPAIR THE ROOF SO THAT IT WILL NOT LEAK | MAINTENANCE | 507 - LEAKY ROOF | MD |
| 508 | § 27-2005 ADM CODE  REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN A UNIFORM COLOR | MAINTENANCE | 508 - REPAIR PLASTER | MD |
| 509 | § 27-2005 ADM CODE  PROPERLY SECURE THE LOOSE | MAINTENANCE | 509 - SECURE LOOSE MATTER | MD |
| 510 | § 27-2005 ADM CODE & 309 M/D LAW  ABATE THE NUISANCE CONSISTING OF | MAINTENANCE | 510 - ABATE THE NUISANCE | MD |
| 511 | § 27-2005 ADM CODE  REPAIR AND OPERATE THE GAS APPLIANCE SO AS TO PREVENT CARBON MONOXIDE | MAINTENANCE | 511 - REPAIR THE GAS APPLIANCE TO PREVENT CARBON MONOXIDE | MD |
| 512 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. REPLACE WITH NEW THE BROKEN, DEFECTIVE AND/OR MISSING | EGRESS | 512 - FIRE ESCAPE DEFECTIVE.  REPLACE WITH NEW THE BROKEN | MD |
| 513 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. ADJUST THE DROPLADDER SO THAT IT WILL SLIDE EASILY IN THE GUIDE RODS | EGRESS | 513 - F/E ADJUST THE DROP LADDER | MD |
| 514 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. PROPERLY SECURE | EGRESS | 514 - F/E DEFECTIVE:  PROPERLY SECURE | MD |
| 515 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. FILL IN HOLES IN WALL AROUND BRACKETS AND/OR RAILS | EGRESS | 515- F/E DEFECTIVE.  FILL IN HOLES IN WALL AROUND BRACKETS AND/OR RAILS | MD |
| 516 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. RESET THE BRACES OF THE BRACKETS SO THAT THEY SHALL BEAR AGAINST WALL | EGRESS | 516 - FIRE ESCAPE DEFECTIVE.  RESET THE BRACES OF THE BRACKETS | MD |
| 517 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. REMOVE AND REPLACE WITH NEW THE BROKEN AND DEFECTIVE BRACKET AND LEAVE ALL ANCHORAGES UNCOVERED FOR INSPECTION | EGRESS | 517 - F/E.  REMOVE AND REPLACE WITH NEW THE BRACKET | MD |
| 518 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. REPLACE WITH 2 X 1/2 INCH IRON BAR EXTENDING ACROSS AND SECURED TO 2 BRACKETS, THE BROKEN OR DEFECTIVE ANGLE IRON OR BAR AT FOOT OF GOOSENECK LADDER | EGRESS | 518 - F/E   REPLACE WITH 2" X 1/2" IRON BAR EXTENDING ACROSS | MD |
| 519 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE.  REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES | EGRESS | 519 - F/E.  REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES | MD |
| 520 | § 27-2005 ADM CODE  FIRE ESCAPE DEFECTIVE. REMOVE THE ADDITIONAL, DANGEROUS, INADEQUATE FIRE ESCAPE | EGRESS | 520 - F/E DEFECTIVE REMOVE THE ADDITIONAL, DANGER | MD |
| 521 | § 27-2005, 2007 ADM CODE  FIRE EGRESS DEFECTIVE. REMOVE OBSTRUCTING BARS OR UNLAWFUL GATES FROM WINDOW TO FIRE ESCAPE OR PROVIDE APPROVED TYPE GATE | EGRESS | 521 - REMOVE BARS OR GATES FROM FIRE ESCAPE WINDOW | MD |
| 522 | § 27-2005, 2007 ADM CODE  FIRE EGRESS DEFECTIVE. REMOVE OBSTRUCTING BARS OR UNLAWFUL GATES FROM AT LEAST 1 WINDOW OR PROVIDE APPROVED TYPE GATE | EGRESS | 522 - REMOVE BARS OR GATES FROM NON FIRE ESCAPE WINDOW | MD |
| 523 | § 27-2005, 2007 ADM CODE  FIRE EGRESS DEFECTIVE. RESTORE EGRESS BY REMOVING LOCKING DEVICE AND ARRANGE TO OPEN READILY THE GATE IN FENCE AT LOT LINE | EGRESS | 523 - MAKE GATE IN FENCE OPENABLE | MD |
| 524 | § 27-2005, 2007 ADM CODE  FIRE EGRESS DEFECTIVE. REMOVE THE OBSTRUCTION IN FIREPROOF PASSAGEWAY | EGRESS | 524 - FIRE PASSAGEWAY OBSTRUCTED | MD |
| 525 | § 27-2005, 2007 ADM CODE  FIRE EGRESS DEFECTIVE. MAKE STATIONARY THE IRON LADDER LEADING TO SCUTTLE OPENING IN ROOF | EGRESS | 525 - SCUTTLE LADDER NOT STATIONARY | MD |
| 526 | § 27-2005, 2007 ADM CODE  REMOVE THE ILLEGAL FASTENING | EGRESS | 526 - REMOVE ILLEGAL FASTENING | MD |
| 527 | § 27-2005, 2007 ADM CODE  EGRESS OBSTRUCTED. PROVIDE PROPER MEANS OF EGRESS BY REMOVING PARTITIONS FORMING CLOSET ENCLOSING SCUTTLE LADDER TO ROOF | EGRESS | 527 - REMOVE PARTITIONS | MD |
| 528 | § 27-2005 ADM CODE  REPLACE WITH STANDARD WIRE GLASS THE PRESENT GLASS | EGRESS | 528 - REPLACE WITH WIRE GLASS | MD |
| 529 | § 27-2005 HMC: REFIT… | EGRESS | 529 - REFIT DOORS ETC. | MD |
| 530 | § 27-2005, 27-2007, 27-2041.1 HMC, §238, § 309; § 107 (2) ( C) MDL AND 28 RCNY §25-171: REPLACE OR REPAIR THE SELF-CLOSING DOORS THAT IS MISSING OR DEFECTIVE | EGRESS | 530 - MAKE DOORS SELF-CLOSING | MD |
| 531 | § 27-2005 ADM CODE  MAKE STATIONARY THE TRANSOM OVER DOOR | EGRESS | 531 - TRANSOM NOT STATIONARY | MD |
| 532 | § 27-2005 ADM CODE  PROVIDE A STATIONARY IRON LADDER OR FIREPROOF STAIR FOR THE OUTSIDE CELLAR ENTRANCE | EGRESS | 532 - STATIONARY LADDER TO CELLAR | MD |
| 533 | § 27-2005 ADM CODE  REMOVE ILLEGAL FASTENINGS FROM GRATING DOOR TO OUTSIDE CELLAR ENTRANCE | EGRESS | 533 - GRATINGS SECURED | MD |
| 534 | § 27-2005 ADM CODE  PROVIDE A PROPER SEAT FOR WATER CLOSET | MAINTENANCE | 534 - PROVIDE A SEAT FOR WATER CLOSET | MD |
| 535 | § 27-2005 ADM CODE  REMOVE THE TORN AND/OR LOOSE FLOOR COVERING | MAINTENANCE | 535 - REMOVE FLOOR COVERING | MD |
| 536 | § 27-2005, 2007 ADM CODE  REMOVE DEVICE PREVENTING DOOR FROM BEING SELF-CLOSING | EGRESS | 536 - DOOR NOT SELF-CLOSING | MD |
| 537 | § 27-2005, 2007 ADM CODE  REMOVE UNLAWFUL WOOD OR METAL LOUVRED OR SCREEN DOORS AND ASSEMBLIES FROM ENTRANCE TO | EGRESS | 537 - REMOVE UNLAWFUL DOORS | MD |
| 538 | § 27-2005, 2007 ADM CODE  REMOVE ALL ENCUMBRANCES CONSISTING OF | EGRESS | 538 - REMOVE ENCUMBRANCES | MD |
| 539 | § 27-2005, 2007 ADM CODE  AND DEPT. RULES AND REGULATIONS. REMOVE THE ENCUMBRANCE OBSTRUCTING EGRESS FROM FIRE ESCAPES | EGRESS | 539 - REMOVE ENCUMBRANCE | MD |
| 540 | § 27-848 ADMIN CODE & DEPT. RULES AND REGS.  REPLACE REFUSE CHUTE WARNING SIGN PUBLIC HALL DOOR TO SERVICE CLOSET OR ON WALL OVER HOPPER DOOR AT | MAINTENANCE | 540 - NO REFUSE CHUTE WARNING SIGN | MD |
| 541 | § 27-2009.2  FAILURE TO DISTRIBUTE AND POST SAFE CONSTRUCTION BILL OF RIGHTS AND/OR NOTICE OF THE TENANT PROTECTION PLAN.  SUCH NOTICES SHALL REMAIN POSTED UNTIL THE COMPLETION OF THE DESCRIBED PERMITTED WORK. | EGRESS | 541 - POST SAFE CONSTRUCTION BILL OF RIGHTS | MD |
| 542 | 28 RCNY § 25-171; & 67 (7)(B) MDL; NYC FIRE CODE § 703.1.3; NYC FIRE CODE § 703.2: ADJUST DOOR TO PREVENT GAPS BETWEEN THE TOP AND SIDE EDGES OF DOOR AND DOOR JAMB EXCEEDING THE MAXIMUM ALLOWABLE CLEARANCE OF 1/8 OF AN INCH AND MAXIMUM ALLOWABLE CLEARANCE | EGRESS | 542 - ADJUST DOOR TO PREVENT GAP - FIRE CODE/EGRESS | MD |
| 546 | § 27-2005, 2007 HMC: REMOVE THE ILLEGAL DOUBLE CYLINDER KEY OPERATED LOCKING DEVICE AT DOOR | EGRESS | 546 - REMOVE DOUBLE CYLINDER LOCK | MD |
| 549 | § 27-2005, 2012 HMC & § 309 MDL: ABATE THE NUISANCE CONSISTING OF EXCESSIVE STORAGE OF MATERIAL | EGRESS | 549 - REMOVE EXCESSIVE STORAGE | MD |
| 550 | § 27-2017.3 HMC: TRACE AND REPAIR THE SOURCE AND ABATE THE VISIBLE MOLD CONDITION... | CLEANING | 550 - TRACE & REPAIR THE SOURCE & ABATE THE…MOLD | MD |
| 551 | § 27-2010, 2011, 2012 ADM CODE  CLEANSE AND DISINFECT TO THE SATISFACTION OF THIS DEPARTMENT AFTER REMOVING THE | CLEANING | 551 - REMOVE ACCUMULATION OF RUBBISH, WATER & DISINFECT | MD |
| 552 | § 27-2010, 2011, 2012 ADM CODE  REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE | CLEANING | 552 - REMOVE ACCUMULATION OR RUBBISH | MD |
| 553 | § 27-2011 ADM CODE  CLEANSE TO THE SATISFACTION OF THIS DEPARTMENT THE | CLEANING | 553 - CLEANSE | MD |
| 554 | §  27-2005 ADM CODE  PAINT METAL IN ACCORDANCE WITH DEPT. REGULATION | PAINTING | 554 - PAINT METAL | MD |
| 555 | §  27-2013 ADM CODE  REMOVE OR COVER IN A MANNER APPROVED BY THE DEPARTMENT THE PEELING LEAD PAINT | PAINTING - RETIRED | 555 - REPEALED: LEAD - BASED PAINT | MD |
| 556 | § 27-2013 ADM CODE  PAINT WITH LIGHT COLORED PAINT TO THE SATISFACTION OF THIS DEPARTMENT | PAINTING | 556 - PAINT | MD |
| 557 | § 27-2013 ADM CODE  REMOVE THE DIRTY AND/OR LOOSE PAPER AND REPAPER OR PAINT TO THE SATISFACTION OF THIS DEPARTMENT | PAINTING | 557 - REMOVE OLD PAPER AND REPAPER OR PAINT | MD |
| 558 | § 27-2013 ADM CODE  NO DECORATING IN 3 YEARS. PAINT WITH LIGHT COLORED PAINT TO THE SATISFACTION OF THIS DEPARTMENT | PAINTING | 558 - PAINT | MD/PD |
| 559 | § 27-2013 ADM CODE  NO DECORATING IN 3 YEARS. REMOVE THE DIRTY AND/OR LOOSE PAPER AND REPAPER OR PAINT TO THE SATISFACTION OF THIS DEPARTMENT | PAINTING | 559 - REMOVE OLD PAPER AND REPAPER OR PAINT | MD/PD |
| 560 | § 27-2013 ADM CODE  MAINTAIN AND KEEP ON PREMISES SUCH RECORDS RELATING TO TIME WHEN WINDOW FRAMES AND SASHES AND DWELLING UNITS WERE LAST PAINTED. | PAINTING | 560 - NO RECORD OF PAINTING ON PREMISES | MD |
| 561 | § 27-2014 ADM CODE  AND DEPT. RULES AND REGULATIONS. SCRAPE AND REMOVE RUST SCALES AND PAINT WITH 2 COATS OF PAINT | PAINTING | 561 - PAINT METAL | MD |
| 562 | § 27-2014 ADM CODE  PAINT TO THE SATISFACTION OF THIS DEPARTMENT THE EXTERIOR WINDOW FRAMES AND SASHES | PAINTING | 562 - PAINT WINDOW FRAMES AND SASHES | MD |
| 563 | § 27-2015 ADM CODE  THOROUGHLY WHITEWASH OR PAINT WITH A LIGHT COLOR THE SURFACES | PAINTING | 563 - WHITEWASH PAINT WITH A LIGHT COLOR  (COURTS & SHAFTS) | MD |
| 564 | § 27-2081 ADM CODE  THOROUGHLY WHITEWASH OR PAINT WITH A LIGHT COLOR THE SURFACES | PAINTING | 564 - WHITEWASH OR PAINT (CELLAR) | MD |
| 565 | § 27-2015 ADM CODE  THOROUGHLY CLEANSE TO THE SATISFACTION OF THIS DEPARTMENT THE DIRTY AND UNSANITARY EXTERIOR WALLS AT | PAINTING | 565 - CLEANSE TO THE SATISFACTION OF THIS DEPARTMENT | MD |
| 566 | HMC ADM CODE: § 27-2021.4 HMC: ABATE THE NUISANCE CONSISTING OF PESTS. EVIDENCE OF | EXTERMINATION & RODENT ERADICATION | 566 - REMOVE VERMIN | MD |
| 567 | HMC ADM CODE: § 27-2017, 27-2017.1, 27-2017.4, 27-2017.5,  27-2017.8, 27-2019, 27-2021 HMC: ABATE THE NUISANCE CONSISTING OF EVIDENCE OF RATS AND ALL UNDERLYING CAUSES CREATING THE PEST INFESTATIONS, BY USING INTEGRATED PEST MANAGEMENT (IPM), ELIMINATE ALL BURROW ENTRY AND PASSAGEWAYS, PEST NESTS, HOLES, GAPS OR CRACKS IN WALLS, CEILINGS, FLOORS, FIXING LEAKS AND MANAGING GARBAGE IN PUBLIC AREAS. EVIDENCE FOUND AT | EXTERMINATION & RODENT ERADICATION | 567 - REMOVE RODENT | MD |
| 568 | HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF ROACHES | EXTERMINATION & RODENT ERADICATION | 568 - ABATE THE NUISANCE OF ROACHES | MD |
| 569 | HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF MICE | EXTERMINATION & RODENT ERADICATION | 569 - ABATE THE NUISANCE OF MICE | MD |
| 570 | HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF BEDBUGS | EXTERMINATION & RODENT ERADICATION | 570 - ABATE THE NUISANCE OF BEDBUGS | MD |
| 571 | § 27-2021 ADM CODE  PROVIDE SUFFICIENT, PROPER AND SEPARATE METAL RECEPTACLES FOR THE DEPOSIT OF GARBAGE, RUBBISH AND OTHER WASTE MATERIAL AND ARRANGE FOR COLLECTION AND DISPOSAL OF SUCH MATERIAL. | COLLECTION OF WASTE | 571 - PROVIDE GARGABE CANS | MD |
| 572 | § 27-2021 ADM CODE  PROVIDE PLACE WITHIN THE BUILDING FOR THE STORAGE OF WASTE RECEPTACLES AND DISINFECT SAME REGULARLY. | COLLECTION OF WASTE | 572 - STORAGE OF GARBAGE CANS | MD |
| 573 | § 27-2022 ADM CODE  POST A SIGN INDICATING HOURS OF COLLECTION AND METHOD OF COLLECTION OF WASTE MATERIAL WHERE DUMBWAITER SERVICE IS NOT PROVIDED. | POSTING/SIGNAGE | 573 - POST A SIGN | MD |
| 576 | § 27-2024 ADM CODE  PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES | WATER SUPPLY | 576 - INADEQUATE COLD WATER | MD |
| 577 | § 27-2024 ADM CODE  PROVIDE ADEQUATE SUPPLY OF HOT WATER FOR THE FIXTURES | WATER SUPPLY | 577 - INADEQUATE HOT WATER SUPPLY (VOLUME) | MD |
| 578 | § 27-2026 ADM CODE  REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE | WATER SUPPLY | 578 - REPAIR LEAKY PIPES | MD |
| 579 | § 27-2026 ADM CODE  REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS | WATER SUPPLY | 579 - REPAIR LEAKY FAUCETS | MD |
| 580 | § 27-2024 ADM CODE  PROVIDE SUITABLE TIGHT COVER MADE OF METAL OR WOOD COVERED WITH METAL FOR WATER SUPPLY TANK ON ROOF. | WATER SUPPLY | 580 - PROVIDE COVER FOR ROOF TANK | MD |
| 581 | § 27-2024 ADM CODE  EMPTY AND THOROUGHLY CLEANSE THE INTERIOR SIDES AND BOTTOM OF WATER SUPPLY TANK ON ROOF. | WATER SUPPLY | 581 - CLEAN INSIDE ROOF TANK | MD |
| 582 | § 27-2024 ADM CODE  PROVIDE A BALL COCK FOR THE WATER SUPPLY TANK ON ROOF. | WATER SUPPLY | 582 - PROVIDE BALL COCK FOR ROOF TANK | MD |
| 583 | § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK | WATER SUPPLY | 583 - REPAIR THE SOURCE AND ABATE THE WATER LEAK | MD |
| 584 | HMC- §27–2024 PROVIDE AND MAINTAIN A PURE AND WHOLESOME WATER SUPPLY THAT WAS FOUND DISCOLORED AT | WATER SUPPLY | 584- DISCOLORED WATER | MD |
| 586 | § 27-2026 ADM CODE  PROVIDE A SEPARATE HOUSE SEWER AND HOUSE DRAIN PROPERLY CONNECTED TO PLUMBING SYSTEM OF THE BUILDING AND TO MAIN SEWER AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING THIS WORK. | SEWERS AND DRAINAGE | 586 - PROVIDE SEPARATE HOUSE SEWER | MD |
| 587 | § 27-2026 ADM CODE  REMOVE CESSPOOL AND ALL SEWAGE SATURATED EARTH, DISINFECT SITE AND FILL WITH FRESH EARTH. CONNECT PLUMBING SYSTEM OF BUILDING TO MAIN SEWER BY INSTALLING HOUSE SEWER AND DRAIN. FILE APPLICATION FOR APPROVAL BEFORE DOING WORK. | SEWERS AND DRAINAGE | 587 - REMOVE CESSPOOL | MD |
| 588 | § 27-2026 ADM CODE  PROVIDE A SUITABLE STRAINER FOR THE DRAIN | SEWERS AND DRAINAGE | 588 - PROVIDE STRAINER | MD |
| 589 | § 27-2026 ADM CODE  PROVIDE SUITABLE TIGHT COVER FOR THE HANDHOLE OPENING OF TRAP | SEWERS AND DRAINAGE | 589 - HAND HOLD COVER MISSING | MD |
| 590 | § 27-2066 ADM CODE  PROVIDE A WATER CLOSET FOR EACH FAMILY WITHIN THE BUILDING AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING THIS WORK | SEWERS AND DRAINAGE | 590 - ADDITIONAL WATER CLOSET | MD |
| 591 | § 27-2026 ADM CODE  RESET, SO AS TO SECURE A PROPER AND TIGHT CONNECTION, THE WATER CLOSET BOWL | SEWERS AND DRAINAGE | 591 - RESET WATER CLOSET BOWL | MD |
| 592 | § 27-2026 ADM CODE  REPLACE WITH NEW THE DEFECTIVE FLUSH PIPE OF WATER CLOSET | SEWERS AND DRAINAGE | 592 - DEFECTIVE FLUSH PIPE OF WATER CLOSET | MD |
| 593 | § 27-2026 ADM CODE  REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET | SEWERS AND DRAINAGE | 593 - REPAIR FLUSHING APPARATUS OF WATER CLOSET | MD |
| 594 | § 27-2026 ADM CODE  REPAIR LEAKY WATER CLOSET FLUSH PIPE CONNECTION | SEWERS AND DRAINAGE | 594 - LEAKY FLUSH PIPE CONNECTION | MD |
| 595 | § 27-2026 ADM CODE  REMOVE ALL OBSTRUCTIONS FROM WATER CLOSET | SEWERS AND DRAINAGE | 595 - REMOVE OBSTUCTION FROM WATER CLOSET | MD |
| 596 | § 27-2026 ADM CODE  REPLACE THE BROKEN OR DEFECTIVE | SEWERS AND DRAINAGE | 596 - REPLACE DEFECTIVE SINK, WATER CLOSET, WASH TUB | MD |
| 597 | § 27-2026 ADM CODE  REMOVE DISUSED PLUMBING FIXTURES AND PROPERLY SEAL PIPE CONNECTIONS | SEWERS AND DRAINAGE | 597 - REMOVE DISUSED PLUMBING | MD |
| 598 | § 27-2026 ADM CODE  REPAIR THE BROKEN OR DEFECTIVE CONNECTION | SEWERS AND DRAINAGE | 598 - REPAIR BROKEN, LOOSE CONNECTION | MD |
| 599 | § 27-2026 ADM CODE  REPAIR BY CLOSING SO AS TO BE GAS TIGHT ALL OPENINGS IN THE | SEWERS AND DRAINAGE | 599 - MAKE GAS TIGHT | MD |
| 600 | § 27-2026 ADM CODE  PROVIDE A PROPER SCREW CAP FOR THE CLEANOUT OF TRAP | SEWERS AND DRAINAGE | 600 - PROVIDE SCREW CAP FOR TRAP | MD |
| 604 | § 27-2026 ADM CODE  REMOVE OR COVER IN A MANNER APPROVED BY THE DEPARTMENT THE PEELING POSSIBLE LEAD PAINT - POST-60 BUILDING - REFER FOR XRF TESTING | RETIRED | REPEALED: LEAD - BASED PAINT | MD |
| 606 | § 27-2056.5 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD - PAINT THAT TESTED POSITIVE FOR LEAD CONTENT AND THAT IS PEELING OR ON A DETERIORATED SUBSURFACE - USING EXCLUSIVE INTERIM CONTROLS. | RETIRED | REPEALED: LEAD - BASED PAINT | MD |
| 607 | § 27-2056.5 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD - PAINT THAT TESTED POSITIVE FOR LEAD CONTENT AND THAT IS PEELING OR IS ON A DETERIORATED SUBSURFACE ON WOOD TRIM, DOORS, OR  WINDOWS - USING EXCLUSIVE INTERIM CONTROLS, WHICH INCLUDE A SURFACE DU | RETIRED | REPEALED: LEAD - BASED PAINT | MD |
| 610 | § 27-2056.5 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD - PRESUMED LEAD PAINT THAT IS PEELING OR IS ON A DETERIORATED SUBSURFACE - USING EXCLUSIVE INTERIM CONTROLS. | RETIRED | REPEALED: LEAD - BASED PAINT | MD |
| 611 | § 27-2056.5 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD - PRESUMED LEAD PAINT THAT IS PEELING OR ON A DETERIORATED SUBSURFACE ON WOOD TRIM, DOORS, OR  WINDOWS - USING EXCLUSIVE INTERIM CONTROLS, WHICH INCLUDE A SURFACE DUST TEST IN ACCORDANCE WITH STAT | RETIRED | REPEALED: LEAD - BASED PAINT | MD |
| 612 | § 27-2056.5 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD - PRESUMED LEAD PAINT THAT IS ON A DETERIORATED SUBSURFACE THAT IS UNSTABLE OR UNSOUND USING EXCLUSIVE INTERIM CONTROLS. | RETIRED | REPEALED: LEAD - BASED PAINT | MD |
| 614 | § 27-2056.8 ADM CODE -CERTIFY COMPLIANCE WITH LEAD-BASED PAINT HAZARD CONTROL REQUIREMENTS DURING PERIOD OF UNIT VACANCY BY SUBMITTING REQUIRED SUPPORTING DOCUMENTATION AND AFFIDAVITS FOR APARTMENT | RETIRED | REPEALED: LEAD - BASED PAINT | MD |
| 616 | § 27-2056.6 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD - PRESUMED LEAD PAINT THAT IS PEELING OR ON A DETERIORATED SUBSURFACE USING WORK PRACTICES SET FORTH IN 28 RCNY §11-06(B)(2) | LEAD-BASED PAINT | 616 - LEAD-BASED PAINT HAZARD- PRESUMED PAINT | MD/PD |
| 617 | § 27-2056.6 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD - PAINT THAT TESTED POSITIVE FOR LEAD CONTENT AND THAT IS PEELING OR ON A DETERIORATED SUBSURFACE - USING WORK PRACTICES SET FORTH IN 28 RCNY §11-06(B)(2) | LEAD-BASED PAINT | 617 -  LEAD-BASED PAINT HAZARD- POSITIVE | MD/PD |
| 618 | § 27-2056.7 ADM CODE: CORRECT FAILURE TO PROVIDE TO THE DEPARTMENT WITHIN 45 DAYS OF DEMAND ALL RECORDS REQUIRED TO BE MAINTAINED BY OWNER PURSUANT TO LOCAL LAW 1 OF 2004 RELATED TO LEAD-BASED PAINT NOTICES, INSPECTIONS AND REMEDIATION/ABATEMENT ACTIVITIE | LEAD-BASED PAINT | 618 - PROVIDE DEPARTMENT ALL RECORDS | MD/PD |
| 619 | § 27-2056.4 ADM CODE- CORRECT FAILURE TO NOTIFY OCCUPANTS AND/OR TO INVESTIGATE LEAD-BASED PAINT HAZARDS. | LEAD-BASED PAINT | 619 - CORRECT FAILURE TO NOTIFY OCCUPANTS | MD/PD |
| 620 | § 27-2056.4(H) AND 27-2056.17 ADM CODE -CORRECT FAILURE TO PROVIDE TO THE DEPARTMENT WITHIN 45 DAYS OF DEMAND ALL RECORDS REQUIRED TO BE MAINTAINED BY OWNER PURSUANT TO LOCAL LAW 1 OF 2004 RELATED TO LEAD-BASED PAINT NOTICES, INSPECTIONS AND REMEDIATION/A | LEAD-BASED PAINT | 620 -  FAILURE TO PROVIDE TO THE DEPT.  WITHIN 45 DAYS | MD/PD |
| 621 | § 27-2056.7, 27-2056.8, 27-2056.9 ADM CODE -CERTIFY COMPLIANCE WITH LEAD-BASED PAINT HAZARD CONTROL REQUIREMENTS DURING PERIOD OF UNIT VACANCY BY PERFORMING ACTIVITIES NECESSARY TO ABATE PRESUMED LEAD-BASED PAINT FROM REQUIRED WINDOW AND/OR DOOR FRICTION | LEAD-BASED PAINT | 621 - CERTIFY COMPLIANCE WITH LEAD-BASED PAINT HAZARD | MD/PD |
| 622 | § 27-2056.7, 27-2056.8, 27-2056.9 ADM CODE -CERTIFY COMPLIANCE WITH LEAD-BASED PAINT HAZARD CONTROL REQUIREMENTS DURING PERIOD OF UNIT VACANCY BY PERFORMING ACTIVITIES NECESSARY TO ABATE TESTED LEAD-BASED PAINT FROM REQUIRED WINDOW AND/OR DOOR FRICTION SU | LEAD-BASED PAINT | 622 - LEAD-BASED PAINT HAZARD - DURING UNIT VACANCY | MD/PD |
| 623 | § 27-2056.7, 27-2056.17 AND 27-2056.8 ADM CODE - CERTIFY COMPLIANCE WITH LEAD-BASED PAINT HAZARD CONTROL REQUIREMENTS DURING PERIOD OF UNIT VACANCY BY SUBMITTING REQUIRED SUPPORTING DOCUMENTATION AND AFFIDAVITS FOR APARTMENT | LEAD-BASED PAINT | 623 - CERTIFY COMPLIANCE WITH LEAD-BASED PAINT HAZARD | MD/PD |
| 624 | § 27-2056.6 ADM CODE - CORRECT THE LEAD-BASED PAINT HAZARD-PAINT THAT IS PEELING OR ON A DETERIORATED SUBSURFACE AND EITHER TESTED INCONCLUSIVE FOR LEAD CONTENT AT 0.5MG/CM2 OR TESTED POSITIVE FOR LEAD CONTENT ON A METAL OR CERAMIC SUBSTRATE AS SET FORTH IN (28 RCNY §11-07(b)) USING WORK PRACTICES SET FORTH IN 28 RCNY §11-06(b)(2) | LEAD-BASED PAINT | 624 - CORRECT THE LEAD-BASED PAINT TESTED INCONCLUSIVE OR POSTIVE FOR METAL/CERAMIC SUBSTRATE | MD/PD |
| 625 | § 27-2056.7, 27-2056.8, 27-2056.9 ADM CODE - CERTIFY COMPLIANCE WITH LEAD-BASED PAINT HAZARD CONTROL REQUIREMENTS DURING PERIOD OF UNIT VACANCY BY PERFORMING ACTIVITIES NECESSARY TO ABATE PRESUMED LEAD PAINT THAT IS XRF TESTED INCONCLUSIVE AT 0.5 MG/CM2 ( | LEAD-BASED PAINT | 625 - COMPLIANCE WITH LEAD, REQUIREMENT DURING VACANCY | MD/PD |
| 626 | § 27-2056.4(A-1) - CERTIFY COMPLIANCE WITH THE REQUIREMENT TO PERFORM ONE INVESTIGATION FOR THE PRESENCE OF LEAD-BASED PAINT THROUGH XRF TESTING IN A DWELLING UNIT WITHIN ONE YEAR AFTER A CHILD UNDER AGE SIX HAS COME TO RESIDE AFTER AUGUST 9, 2020 BY SUBM | LEAD-BASED PAINT | 626 - LEAD  REQUIREMENT TO PERFORM  INVESTIGATION | MD/PD |
| 630 | (C) 27-2142(A) HMC: THE FOLLOWING DWELLING UNITS WERE REOCCUPIED WHILE BEING SUBJECT TO AN ORDER TO REPAIR/VACATE ORDER ISSUED BY THE DEPARTMENT; ORDER CONDITIONS OBSERVED EXISTING. | ORDER TO REPAIR/VACATE ORDER | 630 - VACATE ORDER REOCCUPIED - NOT HABITABLE | MD |
| 631 | (B) 27-2142(A) HMC: THE FOLLOWING DWELLING UNITS WERE REOCCUPIED WHILE BEING SUBJECT TO AN ORDER TO REPAIR/VACATE ORDER ISSUED BY THE DEPARTMENT; FILE FOR A DISMISSAL REQUEST RELATED TO THE ISSUED ORDER (SEE WWW.NYC.GOV/HPD). | ORDER TO REPAIR/VACATE ORDER | 631 - VACATE ORDER REOCCUPIED - HABITABLE | MD |
| 632 | (B) 27-2141(C) HMC: ORDER TO REPAIR/VACATE ORDER MUST REMAIN POSTED UNTIL SUCH TIME AS THE ORDER IS RESCINDED.  A COPY FOR POSTING CAN BE FOUND THROUGH HPDONLINE (WWW.NYC.GOV/HPD). | POSTING/SIGNAGE | 632 - VACATE ORDER REOCCUPIED - POSTING MISSING | MD |
| 646 | § 27-2026 ADM CODE  PROPERLY CLOSE AND SEAL OPENING AS DESCRIBED BELOW | SEWERS AND DRAINAGE | 646 - PROPERLY CLOSE AND SEAL THE HUB OPENING | MD |
| 647 | § 27-2026 ADM CODE  PROPERLY CLOSE AND SEAL THE HUB OPENING AFTER REMOVING THE DISUSED, BROKEN OR DEFECTIVE | SEWERS AND DRAINAGE | 647 - PROPERLY CLOSE AND SEAL THE HUB OPENING | MD |
| 648 | § 27-2026 ADM CODE  PROPERLY REAM OUT, TAP AND PLUG, WITH SCREW PLUGS, THE HOLES IN | SEWERS AND DRAINAGE | 648 - PROPERLY REAM OUT, TAP AND PLUG | MD |
| 649 | § 27-2026 ADM CODE  REMOVE ALL OBSTRUCTIONS AND REPAIR ALL DEFECTS IN | SEWERS AND DRAINAGE | 649 - REMOVE OBSTRUCTIONS | MD |
| 650 | § 27-2027 ADM CODE  PROVIDE PROPERLY TRAPPED, SEWER CONNECTED, RAIN LEADER SO AS TO PROVIDE PROPER DRAINAGE AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING THE WORK | SEWERS AND DRAINAGE | 650 - PROVIDE RAIN LEADER | MD |
| 652 | § 27-2027 ADM CODE  REPAIR THE BROKEN OR DEFECTIVE RAIN LEADER | SEWERS AND DRAINAGE | 652 - REPAIR RAIN LEADER | MD |
| 653 | § 27-2027 ADM CODE  PROVIDE A GUTTER, PROPERLY CONNECTED TO DRAINAGE SYSTEM, FOR PROPER DRAINAGE | SEWERS AND DRAINAGE | 653 - PROVIDE A GUTTER | MD |
| 654 | § 27-2027 ADM CODE  REPAIR THE BROKEN OR DEFECTIVE GUTTER | SEWERS AND DRAINAGE | 654 - REPAIR GUTTER | MD |
| 655 | § 27-2027 ADM CODE  READJUST AND GRADE WITH A PROPER SLOPE TOWARD THE RAIN LEADER, THE GUTTER | SEWERS AND DRAINAGE | 655 - PROVIDE PROPER SLOPE, GUTTER TO RAIN LEADER | MD |
| 657 | § 27-2005 ADM CODE  REMOVE THE BROKEN OR DEFECTIVE FLOORING AND PAVE THE FLOOR WITH 4 INCHES OF CONCRETE | PAVING AND GRADING | 657 - BROKEN FLOOR, PAVE WITH CONCRETE | MD |
| 658 | § 27-2005 ADM CODE  PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING | PAVING AND GRADING | 658 - REPAIR BROKEN PAYING | MD |
| 659 | § 27-2027 ADM CODE  GRADE WITH PROPER SLOPE TO EXISTING DRAIN AND PAVE WITH 4 INCHES OF CONCRETE THE SURFACE | PAVING AND GRADING | 659 - GRADE AND PAVE TO DRAIN | MD |
| 660 | § 27-2027 ADM CODE  REGRADE WITH THE PROPER SLOPE TO EXISTING DRAIN THE SURFACE | PAVING AND GRADING | 660 - REGRADE TO DRAIN | MD |
| 664 | § 27-2028, 2032 ADM CODE  PROVIDE AN ADEQUATE SUPPLY OF HEAT FROM AN APPROVED CENTRAL HEATING SYSTEM, OR AN APPROVED SYSTEM OF GAS OR ELECTRICAL HEATING IN GOOD OPERATING CONDITION FOR THE DWELLING UNIT | HEAT AND HOT WATER | 664 - PROVIDE ADEQUATE HEAT | MD |
| 665 | § 27-2028 ADM CODE  INSTALL CENTRAL HEATING SYSTEM OR, IF LAWFULLY FEASIBLE, INDIVIDUAL SPACE HEATERS, AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING WORK | HEAT AND HOT WATER | 665 - INSTALL CENTRAL HEATING SYSTEM | MD |
| 666 | § 27-2029 ADM CODE  PROVIDE AN ADEQUATE SUPPLY OF HEAT FOR THE APARTMENT | HEAT AND HOT WATER | 666 - INADEQUATE HEAT | MD |
| 667 | § 27-2030 HMC: DO NOT USE LAW REPEALED File with this department an inspection report of the central heating plant and hot water system for the current year | RETIRED | 667 - HEATING PLAN - LAW REPEALED | MD |
| 668 | § 27-2028 ADM CODE  REPAIR AND OPERATE THE HEATING APPLIANCE SO AS TO PREVENT COAL GAS | RETIRED | 668 - HEATING PLAN - LAW REPEALED | MD |
| 669 | § 27-2031 ADM CODE  INSTALL CENTRAL HOT WATER SYSTEM OR, IF FEASIBLE, INDIVIDUAL HOT WATER HEATERS, AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING WORK | HEAT AND HOT WATER | 669 - PROVIDE HOT WATER | MD |
| 670 | § 27-2031 ADM CODE  PROVIDE HOT WATER AT ALL HOT WATER FIXTURES | HEAT AND HOT WATER | 670 - INADEQUATE HOT WATER | MD |
| 671 | §  27-2033 ADM CODE  POST NOTICE, IN FORM APPROVED BY THE DEPARTMENT, STATING THE NAME AND LOCATION OF THE PERSON DESIGNATED BY THE OWNER TO HAVE KEY TO BUILDINGS HEATING SYSTEM | HEAT AND HOT WATER | 671 - POST BOILER ROOM ACCESS NOTICE | MD |
| 672 | §  27-2033 ADM CODE  PROVIDE READY ACCESS TO BUILDINGS HEATING SYSTEM | HEAT AND HOT WATER | 672 - PROVIDE ACCESS TO BOILER ROOM | MD |
| 673 | §  27-2030 ADM CODE  REPAIR AND OPERATE THE APPLIANCE SO AS TO PREVENT CARBON MONOXIDE | RETIRED | 673 - REPAIR APPLIANCE TO PREVENT CO - LAW REPEALED | MD |
| 674 | §  27-2029 ADM CODE  DEVICE PRESENT ON CENTRAL HEATING SYSTEM WHICH IS CAPABLE OF CAUSING AN OTHERWISE OPERABLE SYSTEM TO BECOME INOPERABLE | HEAT AND HOT WATER | 674 - ILLEGAL DEVICE | MD |
| 675 | § 27-2032, 2034 ADM CODE  DISCONTINUE USE OF ILLEGAL SPACE AND/OR HOT WATER HEATER AND PROVIDE FILED FOR & APPROVED HEATER WHICH OBTAINS COMBUSTION AIR DIRECTLY FROM OUTSIDE THE BUILDING OR APPROVED CENTRAL SYSTEM | GAS APPLIANCES | 675 - ILLEGAL HEATER | MD |
| 677 | § 27-2035 ADM CODE  DISCONTINUE THE USE OF THE GAS FIRED REFRIGERATOR | GAS APPLIANCES | 677 - DISCONTINUE GAS REFRIGERATOR | MD |
| 678 | § 27-2036 ADM CODE  MAINTAIN ON THE REEMISES A SELF INSPECTION REPORT OF EACH GAS FUELED SPACE HEATER AND EACH GAS APPLIANCE FOR THE CURRENT YEAR. SUCH REPORT SHALL BE SUBMITTED TO THE DEPARTMENT UPON REQUEST. | GAS APPLIANCES | 678 - NO SELF INSPECTION REPORT | MD |
| 679 | 27-2037, 2039 HMC: Provide adequate lighting for the laundry room | RETIRED | 679 - LIGHT FOR LAUNDRY ROOM - NO LONGER IN USE, REPLACED BY 680 | MD |
| 680 | § 27-2037, 2039 ADM CODE  PROVIDE ADEQUATE LIGHTING FOR THE LAUNDRY ROOM | ARTIFICIAL LIGHTING | 680 -LIGHTING FOR THE LAUNDRY ROOM | MD |
| 681 | § 27-2037 ADM CODE  PROVIDE A PROPER MEANS OF LIGHTING FOR WATER CLOSET COMPARTMENT | ARTIFICIAL LIGHTING | 681 - NO LIGHT FOR WATER CLOSET | MD |
| 682 | § 27-2038 ADM CODE  PROVIDE ADEQUATE LIGHTING FOR | ARTIFICIAL LIGHTING | 682 - INADEQUATE LIGHTING | MD |
| 683 | § 27-2039 ADM CODE  PROVIDE ADEQUATE LIGHT OF NOT LESS THAN 60 WATTS INCANDESCENT OR EQUIVALENT ILLUMINATION | ARTIFICIAL LIGHTING | 683 - PROVIDE LIGHT - Not Less that 60 Watt incadescent | MD |
| 684 | § 27-2037 ADM CODE  PROVIDE ADEQUATE LIGHTING | ARTIFICIAL LIGHTING | 684 - PROVIDE Adequate LIGHT | MD |
| 685 | § 27-2039 ADM CODE  PROVIDE AND MAINTAIN A LIGHT DIRECTLY OVER THE MAIL BOXES IN PUBLIC HALL | ARTIFICIAL LIGHTING | 685 -  NO LIGHT OVER MAIL BOX | MD |
| 686 | § 27-2040 ADM CODE  PROVIDE ADEQUATE LIGHTING AT OR NEAR THE OUTSIDE OF THE FRONT ENTRANCEWAY OF THE BUILDING AND KEEP SAME BURNING FROM SUNSET EVERY DAY TO SUNRISE ON THE DAY FOLLOWING | ARTIFICIAL LIGHTING | 686 -  NO LIGHT AT ENTRANCE TO BUILDING | MD |
| 687 | § 27-2040 ADM CODE  INSTALL AND MAINTAIN SUFFICIENT LIGHT OR LIGHTS OF AT LEAST 100 WATTS INCANDESCENT OR EQUIVALENT EACH, TO LIGHT ADEQUATELY FROM SUNSET TO SUNRISE THE | ARTIFICIAL LIGHTING | 687 - INADEQUATE LIGHTING IN YARD OR COURT | MD |
| 688 | § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES | ARTIFICIAL LIGHTING | 688 - PROVIDE SUPPLY OF ELECTRICTY TO FIXTURES | MD |
| 689 | § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF | ARTIFICIAL LIGHTING | 689 - REPAIR/ABATE UNSAFE WIRES | MD |
| 690 | § 27-2041 ADM CODE  PROVIDE A PEEP HOLE IN ENTRANCE DOOR OF THE DWELLING UNIT SO LOCATED SO AS TO PERMIT A PERSON INSIDE THE DWELLING TO VIEW ANY PERSON OUTSIDE ENTRANCE DOOR | PROTECTIVE DEVICES AND FIRE PROTECTION | 690 - NO PEEP HOLE | MD |
| 691 | § 27-2042 ADM CODE  PROVIDE A MIRROR IN SELF-SERVICE ELEVATOR ARRANGED SO AS TO ENABLE A PERSON ENTERING, TO VIEW INSIDE OF ELEVATOR NUMBER | PROTECTIVE DEVICES AND FIRE PROTECTION | 691 - NO MIRROR IN ELEVATOR | MD |
| 692 | § 27-2043 ADM CODE  PROVIDE A LOCK AND KEY TO THE ENTRANCE DOOR OF DWELLING UNIT AND, IF A CL A MULTIPLE DWELLING, ALSO | PROTECTIVE DEVICES AND FIRE PROTECTION | 692 - NO LOCK AND KEY TO APARTMENT | MD |
| 693 | § 27-2044, 2041.1 HMC: §238 MDL and 28 RCNY §25-171: REPLACE OR REPAIR THE SELF-CLOSING THE DOORS THAT IS MISSING OR DEFECTIVE | PROTECTIVE DEVICES AND FIRE PROTECTION | 693 - SELF-CLOSING DOORS | MD |
| 694 | § 27-2044 ADM CODE  REPLACE WITH WIRE GLASS THE PRESENT GLASS IN DOORS AND/OR TRANSOMS | PROTECTIVE DEVICES AND FIRE PROTECTION | 694 - WIRE GLASS IN DOOR , TRANSOMS | MD |
| 695 | § 27-2044 ADM CODE  REMOVE UNLAWFUL SASH IN PARTITION SEPARATING APARTMENT FROM PUBLIC HALL AND SEAL OPENING WITH FIRE RETARDED MATERIAL | PROTECTIVE DEVICES AND FIRE PROTECTION | 695 - UNLAWFUL SASH, BETWEEN APARTMENT AND PUBLIC HALL | MD |
| 696 | § 27-2044 ADM CODE  PROPERLY FIRE-RETARD, IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT, THE CEILING | PROTECTIVE DEVICES AND FIRE PROTECTION | 696 - FIRE RETARD CEILING | MD |
| 697 | § 27-2005, 2044 HMC: PROVIDE APPROVED ONE-HOUR FIRE RESISTANCE RATED SELF-CLOSING DOOR WITH KEY-OPERATED DEAD BOLT & LATCH SET PEEPHOLE & CHAIN GUARD AT MAIN ENTRANCE | PROTECTIVE DEVICES AND FIRE PROTECTION | 697 - OLT, RATED APARTMENT DOOR | MD |
| 698 | § 27-2005, 2044 HMC:PROVIDE APPROVED ONE-HOUR FIRE RESISTANCE RATED SELF-CLOSING DOOR AT ALL OPENINGS TO PUBLIC HALL, OTHER THAN APARTMENT MAIN ENTRANCE DOOR | PROTECTIVE DEVICES AND FIRE PROTECTION | 698 - OLT, RATED DOOR, NOT MAIN ENTRANCE DOOR | MD |
| 699 | § 27-2044 ADM CODE  PROVIDE SEAL OF ONE-HOUR FIRE RETARDING MATERIAL FOR TRANSOMS OVER ALL DOOR OPENINGS TO PUBLIC HALL FROM | PROTECTIVE DEVICES AND FIRE PROTECTION | 699 - OLT, SEAL TRANSOMS | MD |
| 700 | §27-2045(B)(5) HMC, § 12-01 RCNY POST A PROPER NOTICE OF SMOKE DETECTOR REQUIREMENTS, IN A FORM APPROVED BY THE COMMISSIONER, AT OR NEAR THE MAILBOX | POSTING/SIGNAGE | 700 - POST SMOKE DETECTOR NOTICE | MD |
| 701 | § 27-2045, 2046 ADM CODE  PROVIDE AN APPROVED AND OPERATIONAL SMOKE DETECTING DEVICE, INSTALLED IN ACCORDANCE WITH DEPARTMENT OF BUILDINGS RULES AND REGULATIONS | SMOKE DETECTING DEVICES | 701 - LAW REPEALED | MD |
| 702 | § 27-2045(B)(1)(A) HMC, § 12-01, § 12-03 RCNY REPAIR, REPLACE OR PROVIDE AN APPROVED AND OPERATIONAL SMOKE DETECTING DEVICE, INSTALLED IN ACCORDANCE WITH DEPARTMENT OF BUILDINGS RULES AND REGULATIONS | SMOKE DETECTING DEVICES | 702 - REPAIR OR REPLACE SMOKE DETECTOR | MD |
| 703 | § 27-2045, 2046 ADM CODE  FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF SMOKE DETECTING DEVICE IN ACCORDANCE WITH H.P.D. RULES AND REGULATIONS. | RETIRED | 703 - FILE CERTIFICATION SMOKE DETECTOR - DO NOT USE, RULE REVISED | MD |
| 704 | § 27-2045, 2046 ADM CODE  MAINTAIN ON THE PREMISES AND MAKE AVAILABLE TO THE DEPARTMENT UPON REQUEST RECORDS OF INSTALLATION AND MAINTENANCE OF SMOKE DETECTORS IN THE BUILDING. | SMOKE DETECTING DEVICES | 704 - PROVIDE SMOKE DECTOR RECORDS. | MD |
| 706 | § 27-2047 ADM CODE  ARRANGE FOR MAIL TO BE DELIVERED TO OWNER, HIS AGENT OR EMPLOYEES FOR PROMPT DISTRIBUTION TO OCCUPANTS. | MISCELLANEOUS SERVICES AND FACILITIES | 706 - NO MAIL RECEPTACLES | MD |
| 707 | § 27-2047 ADM CODE  PROVIDE AND MAINTAIN APPROVED MAIL RECEPTACLES AND DIRECTORIES FOR THE PERSONS RESIDING IN THE DWELLING AS PROVIDED IN THE U.S. POSTAL REGULATIONS. | MISCELLANEOUS SERVICES AND FACILITIES | 707 - NO MAIL RECEPTACLES | MD |
| 708 | § 27-2048 ADM CODE  PAINT OR POST A SIGN INDICATING FLOORS | POSTING/SIGNAGE | 708 - POST FLOOR SIGN | MD |
| 709 | § 27-2049 ADM CODE  POST AND MAINTAIN A STREET NUMBER ON THE FRONT OF THE DWELLING PLAINLY VISIBLE FROM THE SIDEWALK. | POSTING/SIGNAGE | 709 - NO NUMBER IDENTIFYING BUILDING | MD |
| 710 | § 27-2050 ADM CODE  FILE WITH THE BOROUGH CHIEF INSPECTOR OF THIS DEPARTMENT A SPRINKLER TEST REPORT FOR THE CURRENT YEAR. | RETIRED | 710- LAW AMENDED: NOT REQUIRED | MD |
| 711 | § 27-2050 ADM CODE  MAINTAIN ON THE PREMISES A COPY OF THE SPRINKLER TEST FOR THE CURRENT YEAR. | RETIRED | 711 - MAINTAIN SPRINKLER REPORT | MD |
| 712 | § 27-2050 ADM CODE  PROVIDE AN ANGLE HOSE VALVE OR SILL COCK AT EXTREME END OF HIGHEST LINE OF SPRINKLERS. | SPRINKLER SYSTEM | 712 - PROVIDE HOSE VALVE OR SILL COCK | MD |
| 713 | § 27-2050 ADM CODE  PROVIDE A PIECE OF GARDEN HOSE 10 FEET IN LENGTH WITH FEMALE COUPLING AND A 10 QUART PAIL ON PREMISES TO TEST SPRINKLER SYSTEM. | SPRINKLER SYSTEM | 713 - PROVIDE HOSE AND PAIL | MD |
| 714 | § 27-2050 ADM CODE  SEAL IN OPEN POSITION THE O.S.Y. VALVE OF THE SPRINKLER SYSTEM IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT | SPRINKLER SYSTEM | 714 - O.S.Y. VALVE NOT SEALED IN OPEN POSITION | MD |
| 715 | § 27-2050 ADM CODE  PROVIDE 3 EXTRA SPRINKLER HEADS AND SUITABLE WRENCH FOR EMERGENCY PURPOSES AT O.S.Y. VALVE OF SPRINKLER IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT | SPRINKLER SYSTEM | 715 - WRENCH AND 3 SPRINKLER HEADS NOT PROVIDED | MD |
| 716 | § 27-2051 ADM CODE  PROVIDE A MANAGER WHO SHALL BE RESPONSIBLE FOR THE CONDUCT, OPERATION AND MAINTENANCE OF PREMISES AND WHO SHALL LIVE ON PREMISES OR BE REGULARLY PRESENT THEREIN. | MISCELLANEOUS SERVICES AND FACILITIES | 716 - PROVIDE A MANAGER | MD |
| 717 | § 27-2005, 2050 HMC: PROVIDE AN ADEQUATE SUPPLY OF WATER FOR THE WET SPRINKLER AND/OR STANDPIPE SYSTEM AT | SPRINKLER SYSTEM | 717 - PROVIDE AN ADEQUATE SUPPLY OF WATER FOR  SPRINKLER | MD |
| 718 | § 27-2005 HMC: REPAIR OR REPLACE DEFECTIVE DIGITAL SIGN | POSTING/SIGNAGE | 718-DIGITAL SIGN NOT WORKING OR DEFECTIVE. | MD |
| 719 | § 27-2005 HMC: REQUIRED NOTICE MISSING FROM DIGITAL SIGN AT ENTRY STORY PUBLIC HALL.  ADD NOTICE(S) REGARDING | POSTING/SIGNAGE | 719-REQUIRED NOTICE MISSING | MD |
| 721 | § 27-2053 ADM CODE  PROVIDE DWELLING WITH A JANITOR OR RESPONSIBLE PERSON OR JANITORIAL SERVICE. | JANITORIAL SERVICES | 721 - PROVIDE A JANITOR | MD |
| 722 | § 27-2053 ADM CODE  POST SIGN ON WALL OF ENTRANCE STORY BEARING NAME, ADDRESS INCLUDING APARTMENT NUMBER IF ANY, AND TELEPHONE NUMBER OF SUPERINTENDENT, JANITOR OR HOUSEKEEPER. | POSTING/SIGNAGE | 722 - POST SIGN INDICATING NAME AND ADDRESS OF JANITOR, ETC. | MD |
| 724 | § 27-2055 ADM CODE  FILE WITH THIS DEPARTMENT A CERTIFICATION THAT THE PERSON DOING JANITORIAL SERVICES IS COMPETENT TO PERFORM SAME. | JANITORIAL SERVICES | 724 - NO CERTIFICATION OF JANITOR | MD |
| 726 | § 27-2059 ADM CODE  DISCONTINUE USE OF INTERIOR ROOM FOR LIVING OR PROVIDE AN ALCOVE OPENING OF AT LEAST 32# SQ FT TO ROOM HAVING A WINDOW OPENING DIRECTLY TO STREET OR YARD | UNLAWFUL USE | 726 - DISCONTINUE FOR LIVING DUE TO LIGHTING/VENTILATION | MD |
| 727 | § 27-2061 ADM CODE  DISCONTINUE USE OF INTERIOR ROOM FOR LIVING | UNLAWFUL USE | 727 - INTERIOR ROOM, CANNOT BE MADE LEGAL | MD |
| 728 | §27-2153 ADM CODE POST AND MAINTAIN A NOTICE, WRITTEN IN ENGLISH AND IN SPANISH, ON THE BUILDING ENTRANCE DOOR OR OTHER CONSPICUOUS LOCATION IN THE BUILDING COMMON AREA, STATING THAT: (1) THE BUILDING IS IN THE ALTERNATIVE ENFORCEMENT PROGRAM, (2) THAT OCCUPANTS MAY CALL 311 OR THE AEP AT 212-863-8262 | POSTING/SIGNAGE | 728 - POST AND MAINTAIN A NOTICE | MD |
| 729 | §27-2153 ADM CODE THE PREMISES HAS BEEN SELECTED TO PARTICIPATE IN THE ALTERNATIVE ENFORCEMENT PROGRAM WHICH MAY RESULT IN BUILDING-WIDE INSPECTIONS, FEES, AND EXTENSIVE REPAIR WORK TO CORRECT VIOLATIONS AND UNDERLYING CONDITIONS. CHARGES FOR REPAIR WORK DONE PURSUANT TO THIS ORDER, IF NOT PAID, WILL | ALTERNATIVE ENFORCEMENT PROGRAM | 729 - SELECTED TO PARTICIPATE IN THE AEP PROGRAM | MD |
| 730 | § 27-2091(C) ADM CODE   THE PROPERTY HAS BEEN ISSUED AN ORDER TO IDENTIFY AND ADDRESS  UNDERLYING CONDITIONS AND VIOLATIONS RELATED TO THE ORDER. FAILURE TO COMPLY MAY RESULT IN EXTENSIVE REPAIR WORK TO CORRECT UNDERLYING CONDITIONS AND RELATED VIOLATIONS | UNDERLYING CONDITIONS PROGRAM ORDER | 730 - USED FOR BUILDINGS SELECTED FOR UCP ONLY | MD |
| 731 | § 27-2064 ADM CODE  PROVIDE PROPER PLASTERED PARTITIONS EXTENDING FROM FLOOR TO CEILING FOR WATER CLOSET COMPARTMENT AND/OR BATHROOM | SANITARY FACILITIES | 731 - PLASTERED PARTITIONS | MD |
| 732 | § 27-2064 ADM CODE  PROVIDE IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT A WATERPROOF FLOOR AND BASE FOR THE WATER CLOSET | SANITARY FACILITIES | 732 - WATERPROOF FLOOR OF WATER CLOSET | MD |
| 733 | § 27-2065 ADM CODE  PROVIDE VENTILATION FOR WATER CLOSET COMPARTMENT AND/OR BATHROOM AND FILE APPLICATION FOR APPROVAL BEFORE DOING WORK | SANITARY FACILITIES | 733 - PROVIDE VENTILATION | MD |
| 734 | § 27-2067 ADM CODE  PROVIDE AT LEAST ONE WATER CLOSET ON THE SAME FLOOR FOR THE ROOMS USED FOR CLASS B OCCUPANCY. WORK MUST BE COMPLETED UNDER PERMIT | SANITARY FACILITIES | 734 - NO WATER CLOSET FOR CLASS "B" ROOMS. | MD |
| 735 | § 27-2067 ADM CODE  PROVIDE A WATER CLOSET, WASH BASIN, BATHTUB OR SHOWER FOR EACH SIX PERSONS OR REMAINDER THEREOF FOR ANY ROOM USED FOR CLASS B OCCUPANCY. WORK MUST BE COMPLETED UNDER PERMIT. | SANITARY FACILITIES | 735 - INADEQUATE SANITARY FACILITIES | MD |
| 736 | § 27-2067 ADM CODE  PROVIDE UNDER COMPLETED PERMIT SANITARY FACILITIES FOR EACH 6 PERSONS OR REMAINDER THEREOF FOR CLASS B ROOMS BY INSTALLING | SANITARY FACILITIES | 736 - INADEQUATE SANITARY FACILITIES | MD |
| 737 | § 27-2067 ADM CODE  PROVIDE UNDER COMPLETED PERMIT, WATER CLOSET, WASHBASIN, BATHTUB OR SHOWER FOR EACH 6 PERSONS OR REMAINDER THEREOF FOR SINGLE ROOM OCCUPANCY APTS. AT | SANITARY FACILITIES | 737 - INADEQUATE SANITARY FACILITIES | MD |
| 738 | § 27-2067 ADM CODE  PROVIDE UNDER COMPLETED PERMIT, SANITARY FACILITIES FOR EACH 6 PERSONS OR REMAINDER THEREOF FOR SINGLE ROOM OCCUPANCY APT., BY INSTALLING | SANITARY FACILITIES | 738 - INADEQUATE SANITARY FACILITIES | MD |
| 739 | § 27-2068 ADM CODE  PROVIDE ADDITIONAL WATER CLOSET AND WASH BASIN SO THERE SHALL BE NOT LESS THAN 1 WATER CLOSET AND WASH BASIN FOR EVERY 7 SLEEPING ROOMS AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING THIS WORK. | SANITARY FACILITIES | 739 - INADEQUATE  WATER CLOSET AND WASHBASIN RATIO | MD |
| 741 | § 27-2070 ADM CODE  DISCONTINUE UNLAWFUL COOKING SPACE OR FILE PLANS AND APPLICATION WITH THIS DEPARTMENT TO LEGALIZE SAME, IF LAWFULLY FEASIBLE, | KITCHEN AND KITCHENETTES | 741 - DISCONTINUE COOKING OR LEGALIZE | MD |
| 742 | § 27-2070 ADM CODE  PROVIDE AN ADEQUATE SUPPLY OF GAS TO THE FIXTURES | KITCHEN AND KITCHENETTES | 742 - NO GAS | MD |
| 744 | § 27-2046.4 HMC: PROVIDE STOVE KNOB SAFETY COVERS OR PERMANENT STOVE SAFETY KNOBS WITH INTEGRATED LOCKING MECHANISMS FOR THE GAS STOVE TOP | KITCHEN AND KITCHENETTES | 744 - PROVIDE CONTROL KNOB SAFETY COVERS | MD |
| 745 | § 27-2074 ADM CODE  DISCONTINUE USE OF ROOMS LESS THAN 6 FEET WIDE FOR LIVING | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 745 - DISCONTINUE ROOMS | MD |
| 746 | § 27-2075 ADM CODE  DISCONTINUE UNLAWFUL OVERCROWDING | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 746 - OVERCROWDING | MD |
| 748 | § 27-2075 ADM CODE  POST A SIGN IN ROOMING UNIT SHOWING MAXIMUM LAWFUL OCCUPANCY FOR SLEEPING PURPOSES | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 748 - OCCUPANCY SIGN FOR ROOMS | MD |
| 749 | § 27-2076 ADM CODE  DISCONTUNUE UNLAWFUL USE OF KITCHEN FOR SLEEPING PURPOSES | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 749 - KITCHEN USED FOR SLEEPING PURPOSES | MD |
| 750 | § 27-2076 ADM CODE  DISCONTINUE UNLAWFUL OCCUPANCY FOR LIVING PURPOSES BY CHILD OR CHILDREN UNDER 16 YEARS OF AGE | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 750 - UNLAWFUL OCCUPANCY OF CHILD OR CHILDREN UNDER 16 | MD |
| 751 | § 27-2077 ADM CODE  DISCONTINUE THE ROOMING UNIT | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 751 - DISCONTINUE  ROOMING UNIT | MD |
| 752 | § 27-2078 ADM CODE  DISCONTINUE USE FOR SINGLE ROOM OCCUPANCY PURPOSES THE APARTMENTS WHICH ARE OCCUPIED BY MORE THAN 2 BOARDERS, ROOMERS OR LODGERS | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 752 - DISCONTINUE SINGLE ROOM OCCUPANCY | MD |
| 753 | § 27-2077, 2078 ADM CODE  DISCONTINUE UNLAWFUL USE FOR SINGLE ROOM OCCUPANCY PURPOSES | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 753 - DISCONTINUE SINGLE ROOM OCCUPANCY | MD |
| 754 | § 27-2078 ADM CODE  DISCONTINUE THE UNLAWFUL USE AS SEPARATELY OCCUPIED SLEEPING ROOMS OR, PROVIDE UNOBSTRUCTED ACCESS TO EACH REQUIRED MEANS OF EGRESS | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 754 - DISCONTINUE ROOMS OR PROVIDE EGRESS | MD |
| 755 | § 27-2079 ADM CODE  DISCONTINUE THE USE OF THE PREMISES FOR SINGLE ROOM OCCUPANCY | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 755 - DISCONTINUE SRO | MD |
| 756 | § 27-2080 ADM CODE  PROVIDE TENANT REGISTER ON PREMISES PURSUANT TO RULES AND REGULATIONS OF THIS DEPARTMENT. | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 756 - PROVIDE REGISTER | MD |
| 759 | § 27-2091 HMC, § 302 MDL : APARTMENTS HAVE BEEN ISSUED A COMMISSIONER'S ORDER AND OCCUPANTS ARE IN NEED OF RELOCATION SERVICES. APARTMENTS CANNOT BE RE-OCCUPIED UNITL THE COMMISSIONER'S ORDER IS REVOKED AFTER HPD INSPECTION OF APARTMENTS. | COMMISSIONER'S ORDER | 759 - APARTMENTS HAVE BEEN ISSUED A COMMISSIONER’S ORDER | MD/PD |
| 760 | § 27-2091 HMC, § 302 MDL: THE PREMISES HAVE BEEN ISSUED A COMMISSIONER'S ORDER AND OCCUPANTS ARE IN NEED OF RELOCATION SERIVICES. APARTMENTS CANNOT BE REOCCUPIED UNTIL THE COMMISSIONER'S ORDER IS REVOKED AFTER HPD INSPECTION OF APARTMENTS. | COMMISSIONER'S ORDER | 760 - BUILDING HAVE BEEN ISSUED A COMMISSIONER’S ORDER | MD/PD |
| 761 | § 27-2081 ADM CODE  DISCONTINUE USE OF ROOMS FOR LIVING, DISCONNECT PLUMBING FIXTURES AND PROPERLY SEAL PIPE CONNECTIONS | ILLEGAL OCCUPANCY OF BASEMENT AND CELLARS | 761 - DISCONTINUE ROOMS AT CELLAR | MD |
| 762 | § 27-2081 ADM CODE  DISCONTINUE USE OF ROOMS FOR LIVING PURPOSES | ILLEGAL OCCUPANCY OF BASEMENT AND CELLARS | 762 - DISCONTINUE ROOMS | MD |
| 764 | § 27-2081 ADM CODE  DISCONTINUE USE FOR LIVING | ILLEGAL OCCUPANCY OF BASEMENT AND CELLARS | 764 - DISCONTINUE ROOMS  AT CELLAR | MD |
| 765 | § 27-2142 ADM CODE  APTS HAVE BEEN VACATED BY THIS DEPARTMENT AND CANNOT BE REOCCUPIED UNTIL SO ORDERED AFTER PROOF OF COMPLIANCE FOR APTS | ORDER TO REPAIR/VACATE ORDER | 765 - VACATED APARTMENT(S) | MD |
| 766 | § 27-2089 ADM CODE  ABOVE PREMISES HAVE BEEN VACANT AND UNTENANTED EXCEPT FOR CARETAKER FOR 60 DAYS OR MORE, AND CANNOT BE REOCCUPIED UNTIL A NEW CERTIFICATE OF OCCUPANCY HAS BEEN OBTAINED. PREMISES HAVE BEEN VACANT SINCE | VACANT MULTIPLE DWELLINGS | 766 - VACANT BUILDING | MD |
| 767 | § 27-2089 ADM CODE  THE PREMISES HAVE BEEN VACATED BY AN ORDER OF THIS DEPARTMENT AND CANNOT BE REOCCUPIED EXCEPT FOR CARETAKER, UNTIL (1) AN APPLICATION AND PLAN FOR THE WORK REQUIRED BY THIS ARTICLE HAVE BEEN FILED WITH AND APPROVED BY THE DEPARTMENT OF BUILDINGS, WHERE REQUIRED, (2) SUCH WORK HAS BEEN COMPLETED BY THE OWNER AND APPROVED BY THE DEPARTMENT OR THE DEPARTMENT OF BUILDINGS WHERE REQUIRED, (3) WHERE REQUIRED BY THE DEPARTMENT OF BUILDINGS, A NEW CERTIFICATE OF OCCUPANCY HAS BEEN OBTAINED AND (4) THE DEPARTMENT HAS INSPECTED AND DETERMINED THAT SUCH DWELLING IS HABITABLE. | ORDER TO REPAIR/VACATE ORDER | 767 - VACATED BUILDING | MD |
| 768 | § 27-2089 ADM CODE  THE PREMISES FORMERLY A VACANT BUILDING ARE NOW OCCUPIED BY OTHER THAN A CARETAKER WITHOUT OBTAINING A CERTIFICATE OF OCCUPANCY | VACANT MULTIPLE DWELLINGS | 768 - VACANT BUILDING NOW OCCUPIED | MD |
| 769 | § 27-2004 ADM CODE  DISCONTINUE THE YEAR-ROUND USE OF THESE PREMISES, CLASSFIED FOR SUMMER RESORT OCCUPANCY EXCEPT BY OWNER OR CARETAKER | ORDER TO REPAIR/VACATE ORDER | 769 - SUMMER OCCUPANCY USED FOR YEAR-ROUND OCCUPANCY | MD |
| 771 | §27-2096 HMC: PROPERTY REGISTRATION WAS FILED WITH FALSE OR INCOMPLETE INFORMATION RELATED TO THE PROPERTY CONTACTS. FILE WITH THIS DEPARTMENT A TRUE REGISTRATION STATEMENT FOR THE BUILDING. | ANNUAL PROPERTY REGISTRATION | 771 - REGISTRATION STATEMENT IS FALSE | MD |
| 772 | § 27-2098 ADM CODE  FILE WITH THIS DEPARTMENT A REGISTRATION STATEMENT FOR BUILDING. | ANNUAL PROPERTY REGISTRATION | 772 - NO REGISTRATION | MD |
| 773 | § 27-2098 ADM CODE  FILE WITH THIS DEPARTMENT A TELEPHONE NUMBER AT WHICH THE OWNER OR A RESPONSIBLE PERSON CAN BE REACHED AT ALL HOURS IN THE EVENT OF AN EMERGENCY. | ANNUAL PROPERTY REGISTRATION | 773 - PROVIDE a 24hr TELEPHONE NUMBER | MD |
| 774 | § 27-2101 ADM CODE  FILE WITH THIS DEPARTMENT A WRITTEN DESIGNATION FOR CHANGE IN MANAGING AGENT OF BUILDING. | ANNUAL PROPERTY REGISTRATION | 774 - CHANGE IN MANAGING AGENT | MD |
| 775 | § 27-2099 ADM CODE  FILE WITH THIS DEPARTMENT REGISTRATION STATEMENT FOR CHANGE OF OWNERSHIP OF BUILDING. | ANNUAL PROPERTY REGISTRATION | 775 - CHANGE IN REGISTRATION | MD |
| 776 | § 27-2100 ADM CODE  FILE WITH THIS DEPARTMENT A REGISTRATION STATEMENT WITH A PROPER ADDRESS FOR REGISTERED PARTY. | ANNUAL PROPERTY REGISTRATION | 776 - ADDRESS OF OWNER INCORRECT | MD |
| 777 | § 27-2102 ADM CODE  FILE WITH THIS DEPARTMENT A REGISTRATION STATEMENT FOR LESSEE. | ANNUAL PROPERTY REGISTRATION | 777 - LEASE NOT REGISTERED | MD |
| 778 | § 27-2104 ADM CODE  POST AND MAINTAIN A PROPER SIGN ON WALL OF ENTRANCE STORY SHOWING THE REGISTRATION NUMBER ASSIGNED BY THE DEPARTMENT AND THE ADDRESS OF THE BUILDING. | ANNUAL PROPERTY REGISTRATION | 778 - POST REGISTRATION SIGN | MD |
| 779 | § 27-2105 ADM CODE  RENT BILL OR RECEIPT NOT PROVIDED FOR TENANT WITH NAME AND ADDRESS OF INDIVIDUAL ACTING AS MANAGING AGENT OR NAME AND ADDRESS OF OWNER PRINTED OR STAMPED THEREON | ANNUAL PROPERTY REGISTRATION | 779 - RENT RECEIPT NOT PROVIDED | MD |
| 780 | §27-2107 ADM CODE   OWNER FAILED TO FILE A VALID REGISTRATION STATEMENT WITH THE DEPARTMENT AS REQUIRED BY ADM CODE §27-2097 AND IS THEREFORE SUBJECT TO CIVIL PENALTIES, PROHIBITED FROM CERTIFYING VIOLATIONS, AND DENIED THE RIGHT TO RECOVER POSSESSION OF | ANNUAL PROPERTY REGISTRATION | 780 - FILE A VALID REGISTRATION | MD |
| 790 | § 27-2043.1 HMC INSTALL THE MISSING OR REPAIR/REPLACE THE DEFECTIVE WINDOW GUARD(S) IN ACCORDANCE WITH THE SPECIFICATIONS OF THE NEW YORK CITY HEALTH CODE SECTION 24 RCNY CHAPTER 12. | WINDOW GUARDS | 790 - INSTALL/REPLACE/REPAIR WINDOW GUARDS (APT) | MD |
| 791 | § 27-2043.1 HMC INSTALL THE MISSING OR REPAIR/REPLACE THE DEFECTIVE WINDOW GUARD(S) THROUGHOUT THE PUBLIC AREAS IN ACCORDANCE WITH THE SPECIFICATIONS OF THE NEW YORK CITY HEALTH CODE SECTION 24 RCNY CHAPTER 12. | WINDOW GUARDS | 791 - INSTALL/REPLACE/REPAIR WINDOW GUARDS (PUBLIC AREA) | MD |
| 801 | § 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE | MAINTENANCE | 801 - REPAIR | PD |
| 802 | § 27-2005 ADMIN. CODE:  PROPERLY REPAIR WITH SIMILAR MATERIAL THE BROKEN OR DEFECTIVE | MAINTENANCE | 802 - REPAIR WITH SIMILAR MATERIAL | PD |
| 803 | § 27-2005 ADMIN. CODE:  MAKE SAFE BY PROPERLY REPAIRING THE STRUCTURAL DEFECT. | MAINTENANCE | 803 - STRUCTURAL DEFECT | PD |
| 804 | § 27-2005 ADMIN. CODE: PROVIDE | MAINTENANCE | 804 - PROVIDE | PD |
| 805 | § 27-2005 HMC:  DO NOT USE ORDER NUMBER RETIRED | MAINTENANCE | 805 - RETIRED | PD |
| 806 | § 27-2005 ADMIN. CODE:  REPLACE WITH NEW THE MISSING | MAINTENANCE | 806 - REPLACE | PD |
| 807 | § 27-2005 ADMIN. CODE: REPAIR THE ROOF SO THAT IT WILL NOT LEAK | MAINTENANCE | 807 - LEAKY ROOF | PD |
| 808 | § 27-2005 ADMIN. CODE:  REPAIR THE BROKEN OR DEFECTIVE PLASTERED SURFACES AND PAINT IN UNIFORM COLOR | MAINTENANCE | 808 - REPAIR PLASTER | PD |
| 809 | § 27-2005 ADMIN. CODE:  PROPERLY SECURE THE LOOSE | MAINTENANCE | 809 - SECURE LOOSE MATTER | PD |
| 810 | § 27-2005 ADMIN. CODE:  ABATE THE NUISANCE  CONSISTING OF | MAINTENANCE | 810 - ABATE THE NUISANCE | PD |
| 811 | § 27-2005 ADMIN. CODE:  REPAIR AND OPERATE THE GAS APPLIANCE SO AS TO PREVENT CARBON MONOXIDE | MAINTENANCE | 811 - REPAIR THE GAS APPLIANCE TO PREVENT CARBON MONOXIDE | PD |
| 812 | § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE.  REPLACE WITH NEW THE BROKEN, DEFECTIVE AND/OR MISSING | EGRESS | 812 - FIRE ESCAPE DEFECTIVE.  REPLACE WITH NEW THE BROKEN | PD |
| 813 | § 27-2005 ADMIN. CODE:  FIRE ESCAPE DEFECTIVE. ADJUST THE DROPLADDER SO THAT IT WILL SLIDE EASILY IN THE GUIDE RODS | EGRESS | 813 - F/E ADJUST THE DROP LADDER | PD |
| 814 | § 27-2005 ADMIN. CODE:  FIRE ESCAPE DEFECTIVE.  PROPERLY SECURE | EGRESS | 814 - F/E DEFECTIVE:  PROPERLY SECURE | PD |
| 815 | § 27-2005 ADMIN. CODE:  FIRE ESCAPE DEFECTIVE. FILL IN HOLES IN WALL AROUND BRACKETS AND/OR RAILS | EGRESS | 815- F/E DEFECTIVE.  FILL IN HOLES IN WALL AROUND BRACKETS AND/OR RAILS | PD |
| 816 | § 27-2005 ADMIN. CODE:  FIRE ESCAPR DEFECTIVE. RESET THE BRACES OF THE BRACKETS SO THAT THEY SHALL BE AGAINST WALL | EGRESS | 816 - FIRE ESCAPE DEFECTIVE.  RESET THE BRACES OF THE BRACKETS | PD |
| 817 | § 27-2005 ADMIN. CODE: FIRE ESCAPE DEFECTIVE.  REMOVE AND REPLACE WITH NEW THE BROKEN AND DEFECTIVE BRACKET AND LEAVE ALL ANCHORAGES UNCOVERED FOR INSPECTION | EGRESS | 817 - F/E.  REMOVE AND REPLACE WITH NEW THE BRACKET | PD |
| 818 | § 27-2005 ADMIN. CODE:  FIRE ESCAPE DEFECTIVE. REPLACE WITH 2" X1/2" IRON BAR EXTENDING ACROSS AND SECURED TO TWO BRACKETS, THE BROKEN OR DEFECTIVE ANGLE IRON OR BAR AT FOOT OF GOOSENECK LADDER | EGRESS | 818 - F/E   REPLACE WITH 2" X 1/2" IRON BAR EXTENDING ACROSS | PD |
| 819 | § 27-2005 ADMIN. CODE:  FIRE ESCAPE DEFECTIVE.  REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES | EGRESS | 819 - F/E.  REMOVE OR MAKE SAFE THE ADDITIONAL FIRE ESCAPES | PD |
| 820 | § 27-2005 ADMIN. CODE:  FIRE ESCAPE DEFECTIVE.  REMOVE THE ADDITIONAL, DANGEROUS, INADEQUATE FIRE ESCAPE | EGRESS | 820 - F/E DEFECTIVE REMOVE THE ADDITIONAL, DANGER | PD |
| 821 | § 27-2005,2007 ADMIN. CODE:  FIRE EGRESS DEFECTIVE. REMOVE OBSTRUCTING BARS OR GATES FROM WINDOW TO FIRE ESCAPE | EGRESS | 821 - REMOVE BARS OR GATES FROM FIRE ESCAPE WINDOW | PD |
| 822 | § 27-2005,2007 ADMON. CODE:  FIRE EGRESS DEFECTIVE.  REMOVE OBSTRUCTING BARS OR GATES FROM AT LEAST 1 WINDOW. | EGRESS | 822 - REMOVE BARS OR GATES FROM NON FIRE ESCAPE WINDOW | PD |
| 826 | § 27-2005 ADMIN. CODE:  REMOVE THE ILLEGAL FASTENING | EGRESS | 826 - REMOVE ILLEGAL FASTENING | PD |
| 829 | § 27-2005 ADMIN. CODE: REFIT | EGRESS | 829 - REFIT DOORS ETC. | PD |
| 834 | § 27-2005 ADMIN. CODE: PROVIDE A PROPER SEAT FOR WATER CLOSET | MAINTENANCE | 834 - PROVIDE A SEAT FOR WATER CLOSET | PD |
| 835 | § 27-2005 ADMIN. CODE:  REMOVE THE TORN AND/OR LOOSE FLOOR COVERING | MAINTENANCE | 835 - REMOVE THE TORN AND/OR LOOSE FLOOR COVERING | PD |
| 838 | § 27-2005, 2007 ADMIN. CODE:  REMOVE ALL ENCUMBRANCES CONSISTING OF | EGRESS | 838 - REMOVE ENCUMBRANCES | PD |
| 839 | § 27-2005,2007 ADMIN. CODE AND DEPARTMENT RULES AND REGULATIONS: REMOVE THE ENCUMBRANCE OBSTRUCTING EGRESS FROM FIRE ESCAPES | EGRESS | 839 - REMOVE ENCUMBRANCE OBSTRUCTING EGRESS | PD |
| 846 | § 27-2005, 2007 HMC: REMOVE THE ILLEGAL DOUBLE CYLINDER KEY OPERATED LOCKING DEVICE AT DOOR | EGRESS | 846 - REMOVE DOUBLE CYLINDER LOCK | PD |
| 849 | § 27-2005, 2012 HMC & § 309 MDL: ABATE THE NUISANCE CONSISTING OF EXCESSIVE STORAGE OF MATERIAL | EGRESS | 849 - REMOVE EXCESSIVE STORAGE | PD |
| 851 | § 27-2010,2011,2012  ADMIN. CODE:  CLEANSE AND DISINFECT TO THE SATISFACTION OF THIS DEPARTMENT AFTER REMOVING THE | CLEANING | 851 - REMOVE ACCUMULATION OF RUBBISH, WATER & DISINFECT | PD |
| 852 | § 27-2010, 2011, 2012  ADMIN. CODE:  REMOVE THE ACCUMULATION OF REFUSE AND/OR RUBBISH AND MAINTAIN IN A CLEAN CONDITION THE | CLEANING | 852 - REMOVE ACCUMULATION OR RUBBISH | PD |
| 853 | § 27-2010, 2011, 2012 ADMIN CODE: CLEANSE TO THE SATISFACTION OF THIS DEPARTMENT THE | CLEANING | 853 - CLEANSE | PD |
| 856 | § 27-2013 ADMIN. CODE:  PAINT WITH LIGHT COLORED PAINT TO THE SATISFACTION OF THIS DEPARTMENT | PAINTING | 856 - PAINT | PD |
| 857 | § 27-2013 ADMIN. CODE:  REMOVE THE DIRTY AND/OR LOOSE PAPER AND REPAPER OR PAINT TO THE SATISFACTION OF THIS DEPARTMENT | PAINTING | 857 - REMOVE OLD PAPER AND REPAPER OR PAINT | PD |
| 861 | § 27-2014  ADMIN. CODE AND DEPARTMENT RULES AND REGULATIONS:  SCRAPE AND REMOVE RUST SCALES AND PAINT WITH TWO COATS OF PAINT THE | PAINTING | 861 - PAINT METAL | PD |
| 862 | § 27-2014 ADMIN. CODE:  PAINT TO THE SATISFACTION OF THIS DEPARTMENT THE EXTERIOR WINDOW FRAMES AND SASHES | PAINTING | 862 - PAINT WINDOW FRAMES AND SASHES | PD |
| 866 | HMC ADM CODE: § 27-2021.4 HMC: ABATE THE NUISANCE CONSISTING OF PESTS. EVIDENCE OF | EXTERMINATION & RODENT ERADICATION | 866 - REMOVE VERMIN | PD |
| 867 | 867 (C) § 27-2017, 27-2017.1, 27-2017.4, 27-2017.5,  27-2017.8, 27-2019, 27-2021 HMC: ABATE THE NUISANCE CONSISTING OF EVIDENCE OF RATS AND ALL UNDERLYING CAUSES CONDUCIVE TO PEST INFESTATIONS, BY USING INTEGRATED PEST MANAGEMENT (IPM), ELIMINATE ALL BURROW ENTRY AND PASSAGEWAYS, PEST NESTS, HOLES, GAPS OR CRACKS IN WALLS,CEILINGS, FLOORS, FIXING LEAKS AND MANAGE GARBAGE IN PUBLIC AREAS. EVIDENCE FOUND AT | EXTERMINATION & RODENT ERADICATION | 867 - REMOVE RODENT | PD |
| 868 | HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF ROACHES | EXTERMINATION & RODENT ERADICATION | 868 - ABATE THE NUISANCE OF ROACHES | PD |
| 869 | HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF MICE | EXTERMINATION & RODENT ERADICATION | 869 - ABATE THE NUISANCE OF MICE | PD |
| 870 | HMC ADM CODE: § 27-2017.4 ABATE THE INFESTATION CONSISTING OF BEDBUGS | EXTERMINATION & RODENT ERADICATION | 870 - ABATE THE NUISANCE OF BEDBUGS | PD |
| 871 | § 27-2023 ADMIN. CODE:  PROVIDE SUFFICIENT,PROPER AND SEPARATE METAL RECEPTACLES FOR THE DEPOSIT OF GARBAGE, RUBBISH AND OTHER WASTE MATERIAL AND ARRANGE FOR COLLECTION AND DISPOSAL OF SUCH MATERIAL. | COLLECTION OF WASTE | 871 - PROVIDE GARGABE CANS | PD |
| 872 | § 27-2023 ADMIN. CODE:  PROVIDE PLACE WITHIN THE BUILDING FOR THE STORAGE OF WASTE RECEPTACLES AND DISINFECT SAME REGULARLY. | COLLECTION OF WASTE | 872 - STORAGE OF GARBAGE CANS | PD |
| 876 | § 27-2024  ADMIN. CODE:  PROVIDE ADEQUATE SUPPLY OF COLD WATER FOR THE FIXTURES | WATER SUPPLY | 876 - INADEQUATE COLD WATER | PD |
| 877 | § 27-2024 ADMIN. CODE:  PROVIDE ADEQUATE SUPPLY OF HOT WATER FOR THE FIXTURES | WATER SUPPLY | 877 - INADEQUATE HOT WATER SUPPLY (VOLUME) | PD |
| 878 | § 27-2026 ADMIN. CODE:  REPAIR THE LEAKY AND/OR DEFECTIVE WATER SUPPLY PIPE | WATER SUPPLY | 878 - REPAIR LEAKY PIPES | PD |
| 879 | § 27-2026 ADMIN. CODE:  REPAIR THE LEAKY AND/OR DEFECTIVE FAUCETS | WATER SUPPLY | 879 - REPAIR LEAKY FAUCETS | PD |
| 883 | § 27-2026, 2027 HMC: PROPERLY REPAIR THE SOURCE AND ABATE THE EVIDENCE OF A WATER LEAK | WATER SUPPLY | 883 - REPAIR THE SOURCE AND ABATE THE WATER LEAK | PD |
| 884 | HMC- §27–2024 PROVIDE AND MAINTAIN A PURE AND WHOLESOME WATER SUPPLY THAT WAS FOUND DISCOLORED AT | WATER SUPPLY | 884- DISCOLORED WATER | PD |
| 888 | § 27-2026 ADMIN. CODE:  PROVIDE SUITABLE STRAINER FOR THE DRAIN | SEWERS AND DRAINAGE | 888 - PROVIDE STRAINER | PD |
| 889 | § 27-2026 ADMIN. CODE: PROVIDE SUITABLE TIGHT COVER FOR HANDHOLE OPENING OF TRAP | SEWERS AND DRAINAGE | 889 - HAND HOLD COVER MISSING | PD |
| 891 | § 27-2026 ADMIN. CODE:  RESET, SO AS TO SECURE A PROPER AND TIGHT CONNECTION, THE WATER CLOSET BOWL | SEWERS AND DRAINAGE | 891 - RESET WATER CLOSET BOWL | PD |
| 892 | § 27-2026 ADMIN. CODE:  REPLACE WITH NEW THE DEFECTIVE FLUSH PIPE OF WATER CLOSET | SEWERS AND DRAINAGE | 892 - DEFECTIVE FLUSH PIPE OF WATER CLOSET | PD |
| 893 | § 27-2026  ADMIN. CODE:  REPAIR THE FLUSHING APPARATUS AND MAINTAIN SAME SO AS TO FLUSH EFFECTIVELY THE WATER CLOSET | SEWERS AND DRAINAGE | 893 - REPAIR FLUSHING APPARATUS OF WATER CLOSET | PD |
| 894 | § 27-2026 ADMIN. CODE:  REPAIR LEAKY WATER CLOSET FLUSH PIPE CONNECTION | SEWERS AND DRAINAGE | 894 - LEAKY FLUSH PIPE CONNECTION | PD |
| 895 | § 27-2026 ADMIN. CODE:  REMOVE ALL OBSTRUCTIONS FROM WATER CLOSET | SEWERS AND DRAINAGE | 895 - REMOVE OBSTUCTION FROM WATER CLOSET | PD |
| 896 | § 27-2026 ADMIN. CODE:  REPLACE THE BROKEN OR DEFECTIVE | SEWERS AND DRAINAGE | 896 - REPLACE DEFECTIVE SINK, WATER CLOSET, WASH TUB | PD |
| 897 | § 27-2026  ADMIN. CODE:  REMOVE DISUSED PLUMBING FIXTURES AND PROPERLY SEAL PIPE CONNECTIONS | SEWERS AND DRAINAGE | 897 - REMOVE DISUSED PLUMBING | PD |
| 898 | § 27-2026 ADMIN. CODE:  REPAIR THE BROKEN OR DEFECTIVE CONNECTION | SEWERS AND DRAINAGE | 898 - REPAIR BROKEN, LOOSE CONNECTION | PD |
| 899 | § 27-2026 ADMIN. CODE:  REPAIR BY CLOSING SO AS TO BE GAS TIGHT ALL OPENINGS IN THE | SEWERS AND DRAINAGE | 899 - MAKE GAS TIGHT | PD |
| 900 | § 27-2026  ADMIN. CODE:  PROVIDE A PROPER SCREW CAP FOR THE CLEANOUT OF TRAP | SEWERS AND DRAINAGE | 900 - PROVIDE SCREW CAP FOR TRAP | PD |
| 946 | § 27-2026 ADMIN. CODE: PROPERLY CLOSE AND SEAL OPENING AS DESCRIBED BELOW | SEWERS AND DRAINAGE | 946 - PROPERLY CLOSE AND SEAL THE HUB OPENING | PD |
| 947 | § 27-2026  ADMIN. CODE:  PROPERLY  CLOSE AND SEAL THE HUB OPENING AFTER REMOVING THE DISUSED, BROKEN OR DEFECTIVE | SEWERS AND DRAINAGE | 947 - PROPERLY CLOSE AND SEAL THE HUB OPENING | PD |
| 948 | § 27-2026 ADMIN. CODE:  PROPERLY REAM OUT, TAP AND PLUG, WITH SCREW PLUGS, THE HOLES IN | SEWERS AND DRAINAGE | 948 - PROPERLY REAM OUT, TAP AND PLUG | PD |
| 949 | § 27-2026 ADMIN. CODE:  REMOVE ALL OBSTRUCTIONS AND REPAIR ALL DEFECTS IN | SEWERS AND DRAINAGE | 949 - REMOVE OBSTRUCTIONS | PD |
| 950 | § 27-2027 ADMIN. CODE: PROVIDE PROPERLY TRAPPED, SEWER CONNECTED, RAIN LEADER SO AS TO PROVIDE PROPER DRAINAGE AND FILE AN APPLICATION FOR APPROVAL BEFORE DOING THE WORK | SEWERS AND DRAINAGE | 950 - PROVIDE RAIN LEADER | PD |
| 952 | § 27-2027 ADMIN. CODE:  REPAIR THE BROKEN OR DEFECTIVE RAIN LEADER | SEWERS AND DRAINAGE | 952 - REPAIR RAIN LEADER | PD |
| 953 | § 27-2027 ADMIN. CODE:  PROVIDE A GUTTER, PROPERLY CONNECTED TO DRAINAGE SYSTEM, FOR PROPER DRAINAGE | SEWERS AND DRAINAGE | 953 - PROVIDE A GUTTER | PD |
| 954 | § 27-2027 ADMIN. CODE:  REPAIR THE BROKEN OR DEFECTIVE GUTTER | SEWERS AND DRAINAGE | 954 - REPAIR GUTTER | PD |
| 955 | § 27-2027 ADMIN. CODE:  READJUST AND GRADE WITH A PROPER SLOPE TOWARD THE RAIN LEADER THE GUTTER | SEWERS AND DRAINAGE | 955 - PROVIDE PROPER SLOPE, GUTTER TO RAIN LEADER | PD |
| 958 | § 27-2027 ADMIN. CODE:  PROPERLY REPAIR THE BROKEN OR DEFECTIVE PAVING | PAVING AND GRADING | 958 - REPAIR BROKEN PAYING | PD |
| 959 | § 27-2027 ADMIN. CODE:  GRADE WITH PROPER SLOPE TO EXISTING DRAIN AND PAVE WITH 4 INCHES OF CONCRETE THE SURFACE | PAVING AND GRADING | 959 - GRADE AND PAVE TO DRAIN | PD |
| 960 | § 27-2027 ADMIN. CODE:  REGRADE WITH PROPER SLOPE TO EXISTING DRAIN THE SURFACE | PAVING AND GRADING | 960 - REGRADE TO DRAIN | PD |
| 964 | § 27-2028, 2032 ADMIN.CODE:  PROVIDE AN ADEQUATE SUPPLY OF HEAT FROM AN APPROVED CENTRAL HEATING SYSTEM OR AN APPROVED SYSTEM OF GAS OR ELECTRICAL HEATING IN GOOD OPERATING CONDITION FOR THE DWELLING UNIT | HEAT AND HOT WATER | 964 - PROVIDE ADEQUATE HEAT | PD |
| 965 | § 27-2028  ADMIN. CODE:  INSTALL CENTRAL HEATING SYSTEM OR, IF LAWFULLY FEASIBLE, INDIVIDUAL SPACE HEATERS, AND FILE APPLICATION FOR APPROVAL BEFORE DOING WORK | HEAT AND HOT WATER | 965 - INSTALL CENTRAL HEATING SYSTEM | PD |
| 966 | § 27-2029  ADMIN. CODE:  PROVIDE AN ADEQUATE SUPPLY OF HEAT FOR THE APARTMENT | HEAT AND HOT WATER | 966 - INADEQUATE HEAT | PD |
| 967 | 27-2030 HMC: DO NOT USE LAW REPEALED File with this department an inspection report of the central heating plant and hot water system for the current year. | RETIRED | 967 - HEATING PLANT & HOT WATER - LAW REPEALED | PD |
| 968 | § 27-2038  ADMIN. CODE:  REPAIR AND OPERATE THE HEATING APPLICANCE SO AS TO PREVENT COAL GAS | RETIRED | 968 - REPAIR HEATING/PREVENT COAL GAS - LAW REPEALED | PD |
| 969 | § 27-2031  ADMIN. CODE:  INSTALL CENTRAL HOT WATER SYSTEM OR, IF FEASIBLE, INDIVIDUAL HOT WATER HEATERS, AND FILE AN APPLICATION FORAPPROVAL BEFORE DOING WORK | HEAT AND HOT WATER | 969 - PROVIDE HOT WATER | PD |
| 970 | § 27-2031  ADMIN. CODE:  PROVIDE HOT WATER AT ALL HOT WATER FIXTURES | HEAT AND HOT WATER | 970 - INADEQUATE HOT WATER | PD |
| 975 | § 27-2032, 2034  ADNIM. CODE:  DISCONTINUE USE OF ILLEGAL SPACE AND/OR HOT WATER HEATER AND PROVIDE FILED FOR & APPROVED HEATER WHICH OBTAINS COMBUSTION AIR DIRECTLY FROM OUTSIDE THE BUILDING OR APPROVED CENTRAL SYSTEM | GAS APPLIANCES | 975 - ILLEGAL HEATER - DISCONTINUE USE | PD |
| 976 | § 27-2032, 2034  ADMIN. CODE: EITHER DISCONTINUE USE OF ILLEGAL SPACE AND/OR HOT WATER HEATER OR PROVIDE FILED FOR & APPROVED HEATER WHICH OBTAINS COMBUSTION AIR DIRICTLY FROM OUTSIDE THE BUILDING OR APPROVED CENTRAL SYSTEM | GAS APPLIANCES | 976 - ILLEGAL HEATER - DISCONTINUE USE OR FILE | PD |
| 977 | § 27-2035  ADMIN. CODE:  DISCONTINUE THE USE OF THE ILLEGAL GAS FIRED REFRIGERATOR | GAS APPLIANCES | 977 - DISCONTINUE GAS REFRIGERATOR | PD |
| 981 | § 27-2037  ADMIN. CODE:  PROVIDE PROPER MEANS OF LIGHTING FOR WATER CLOSET COMPARTMENT | ARTIFICIAL LIGHTING | 981 - NO LIGHT FOR WATER CLOSET | PD |
| 982 | § 27-2038 ADMIN CODE:  PROVIDE ADEQUATE LIGHTING FOR | ARTIFICIAL LIGHTING | 982 - INADEQUATE LIGHTING | PD |
| 988 | § 27-2037, 2038 HMC: PROVIDE A SAFE AND ADEQUATE SUPPLY OF ELECTRIC SERVICE TO THE FIXTURES | ARTIFICIAL LIGHTING | 988 - PROVIDE SUPPLY OF ELECTRICTY TO FIXTURES | PD |
| 989 | § 27-2005, 2006, 2037 HMC: PROPERLY REPAIR AND ABATE UNSAFE ELECTRIC WIRING CONDITION CONSISTING OF | ARTIFICIAL LIGHTING | 989 - REPAIR/ABATE UNSAFE WIRES | PD |
| 990 | § 27-2041  ADMIN. CODE:  PROVIDE A PEEP HOLE IN ENTRANCE DOOR OF THE DWELLING UNIT SO LOCATED AS TO PERMIT A PERSON INSIDE THE DWELLING UNIT TO VIEW ANY PERSON OUTSIDE ENTRANCE DOOR | PROTECTIVE DEVICES AND FIRE PROTECTION | 990 - NO PEEP HOLE | PD |
| 992 | § 27-2043  ADMIN. CODE:  PROVIDE A LOCK AND KEY TO THE ENTRANCE DOOR OF DWELLING UNIT | PROTECTIVE DEVICES AND FIRE PROTECTION | 992 - NO LOCK AND KEY TO APARTMENT | PD |
| 1000 | § 27-2045 ADM CODE - POST A PROPER NOTICE OF SMOKE DETECTOR REQUIREMENTS, IN A FORM APPROVED BY THE COMMISSIONER , AT OR NEAR THE MAILBOX | SMOKE DETECTING DEVICES | 1000 - POST SMOKE DETECTOR NOTICE | PD |
| 1001 | § 27-2045 ADM CODE - PROVIDE AN APPROVED AND OPERATIONAL SMOKE DETECTING DEVICE, INSTALLED IN ACCORDANCE WITH DEPARTMENT OF BUILDINGS RULES AND REGULATIONS | SMOKE DETECTING DEVICES | 1001 - NO SMOKE DETECTOR OR SMOKE DECTOR NOT OPERATIONAL | PD |
| 1002 | § 27-2044 ADM CODE - REPAIR OR REPLACE SMOKE DETECTOR | SMOKE DETECTING DEVICES | 1002 - REPAIR OR REPLACE SMOKE DETECTOR | PD |
| 1003 | § 27-2045 ADM CODE - FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF SMOKE DETECTING DEVICE IN ACCORDANCE WITH HPD RULES AND REGULATIONS | SMOKE DETECTING DEVICES | 1003 - FILE CERTIFICATE OF INSTALLATION - REMOVE? | PD |
| 1004 | § 27-2045 ADM CODE - MAINTAIN ON THE PREMISES AND MAKE AVAILABLE TO THE DEPARTMENT UPON REQUEST RECORDS OF INSTALLATION AND MAINTENANCE OF SMOKE DETECTORS IN THE BUILDING | SMOKE DETECTING DEVICES | 1004 - PROVIDE SMOKE DECTOR RECORDS. | PD |
| 1009 | § 27-2049 ADM CODE - POST AND MAINTAIN A STREET NUMBER ON THE FRONT OF THE DWELLING PLAINLY VISIBLE FROM THE SIDEWALK | MISCELLANEOUS SERVICES AND FACILITIES | 1009 - NO NUMBER IDENTIFYING BUILDING | PD |
| 1017 | § 27-2005, 2050 HMC: PROVIDE AN ADEQUATE SUPPLY OF WATER FOR THE WET SPRINKLER AND/OR STANDPIPE SYSTEM AT | MISCELLANEOUS SERVICES AND FACILITIES | 1017 - PROVIDE AN ADEQUATE SUPPLY OF WATER FOR  SPRINKLER | PD |
| 1026 | § 27-2062 ADM CODE - DISCONTINUE USE OF INTERIOR ROOM FOR LIVING OR PROVIDE AN ALCOVE OPENING OF AT LEAST 32 1/2 SQ.FT. TO ROOM HAVING A WINDOW OPENING DIRECTLY TO STREET OR YARD | JANITORIAL SERVICES | 1026 - DISCONTINUE FOR LIVING DUE TO LIGHTING/VENTILATION | PD |
| 1027 | § 27-2062 ADM CODE - DISCONTINUE USE OF INTERIOR ROOM FOR LIVING | JANITORIAL SERVICES | 1027 - INTERIOR ROOM, CANNOT BE MADE LEGAL | PD |
| 1028 | § 27-2062 ADM CODE - DISCONTINUE THE USE OF THE INTERIOR ROOM FOR LIVING OR PROVIDE AN ALCOVE OPENING OF 60 SQ.FT. TO A ROOM HAVING A WINDOW OPENING DIRECTLY TO STREET OR YARD | JANITORIAL SERVICES | 1028 - DISCONTINUE FOR LIVING OR PROVIDE 60 SQ. FT. OPENING | PD |
| 1030 | § 27-2069 ADM CODE - PROVIDE UNDER COMPLETED PERMIT, A WATER CLOSET, WASH BASIN AND BATH OR SHOWER ON THE SAME STORY FOR APARTMENT | SANITARY FACILITIES | 1030 - PROVIDE A WATER CLOSET UNDER PERMIT | PD |
| 1031 | § 27-2064 ADM CODE - PROVIDE PROPER PLASTERED PARTITIONS EXTENDING FROM FLOOR TO CEILING FOR WATER CLOSET COMPARTMENT AND/ OR BATHROOM | SANITARY FACILITIES | 1031 - PROVIDE A WATER CLOSET | PD |
| 1032 | § 27-2064 ADM CODE - PROVIDE IN ACCORDANCE WITH THE RULES AND REGULATIONS OF THIS DEPARTMENT A WATERPROOF FLOOR AND BASE FOR THE WATER CLOSET | SANITARY FACILITIES | 1032 - PROVIDE WATERPROOF FLOOR FOR WATER CLOSET | PD |
| 1033 | § 27-2065 ADM CODE - PROVIDE VENTILATION FOR WATER CLOSET COMPARTMENT AND/ OR BATHROOM AND FILE APPLICATION FOR APPROVAL BEFORE DOING WORK | SANITARY FACILITIES | 1033 - PROVIDE VENTILATION FOR WATER CLOSET | PD |
| 1041 | § 27-2073 ADM CODE - DISCONTINUE UNLAWFUL COOKING SPACE OR FILE PLANS AND APPLICATION WITH THIS DEPARTMENT TO LEGALIZE SAME, IF LAWFULLY FEASIBLE | KITCHEN AND KITCHENETTES | 1041 - DISCONTINUE COOKING OR LEGALIZE | PD |
| 1042 | § 27-2073 ADM CODE - PROVIDE AN ADEQUATE SUPPLY OF GAS TO THE FIXTURES | KITCHEN AND KITCHENETTES | 1042 - NO GAS | PD |
| 1046 | § 27-2075 ADM CODE - DISCONTINUE UNLAWFUL OVERCROWDING | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 1046 - OVERCROWDING | PD |
| 1049 | § 27-2076 ADM CODE - DISCONTINUE UNLAWFUL USE OF KITCHEN FOR SLEEPING PURPOSES | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 1049 - KITCHEN USED FOR SLEEPING PURPOSES | PD |
| 1051 | § 27-2077 ADM CODE - DISCONTINUE THE ROOMING UNIT | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 1051 - DISCONTINUE  ROOMING UNIT | PD |
| 1054 | § 27-2078-ADM CODE - DISCONTINUE THE UNLAWFUL OCCUPANCY BY MORE THAN TWO ROOMERS, BOARDERS OR LODGERS | MINIMUM ROOM SIZES AND OCCUPANCY REGULATIONS | 1054 - DISCONTINUE SINGLE ROOM OCCUPANCY - 2 LODGERS | PD |
| 1061 | § 27-2087 ADM CODE - DISCONTINUE USE OF ROOMS FOR LIVING, DISCONNECT PLUMBING FIXTURES WHERE ILLEGAL AND PROPERLY SEAL PIPE CONNECTIONS | OCCUPANY OF BASEMENT AND CELLARS | 1061 - DISCONTINUE ROOMS AT CELLAR | PD |
| 1062 | § 27-2087 ADM CODE - DISCONTINUE USE OF ROOMS FOR LIVING PURPOSES OR OBTAIN A CERTIFICATE OF OCCUPANCY | OCCUPANY OF BASEMENT AND CELLARS | 1062 - DISCONTINUE ROOMS AT BSMT OR OBTAIN C/O | PD |
| 1067 | § 27-2142 ADM CODE - THE PREMISES OR APTS. HAVE BEEN VACATED BY THE DEPARTMENT AND CANNOT BE REOCCUPIED UNTIL SO ORDERED AFTER PROOF OF COMPLIANCE FOR | RESIDENTIAL BUILDINGS  UNDER VACATE ORDER | 1067 - VACATE ORDER REOCCUPIED - NOT HABITABLE | PD |
| 1068 | § 27-2142 ADM CODE - THE PREMISES VACATED BY THIS DEPARTMENT, HAVE BEEN REOCCUPIED WITHOUT OBTAINING REQUIRED APPROVAL | RESIDENTIAL BUILDINGS  UNDER VACATE ORDER | 1068 - VACATE ORDER REOCCUPIED - HABITABLE | PD |
| 1071 | § 27-2096 ADM CODE - FILE WITH THIS DEPARTMENT A TRUE REGISTRATION STATEMENT FOR BUILDING | ANNUAL PROPERTY REGISTRATION | 1071 - REGISTRATION STATEMENT IS FALSE | PD |
| 1072 | § 27-2098 ADM CODE - FILE WITH THIS DEPARTMENT A REGISTRATION STATEMENT FOR BUILDING | ANNUAL PROPERTY REGISTRATION | 1072 - NO REGISTRATION | PD |
| 1074 | § 27-2098 ADM CODE - FILE WITH THIS DEPARTMENT A WRITTEN DESIGNATION OF MANAGING AGENT OF BUILDING | ANNUAL PROPERTY REGISTRATION | 1074 - CHANGE IN MANAGING AGENT | PD |
| 1075 | § 27-2099 ADM CODE - FILE WITH THIS DEPARTMENT A REGISTRATION STATEMENT FOR CHANGE OF OWNERSHIP OF BUILDING | ANNUAL PROPERTY REGISTRATION | 1075 - CHANGE IN REGISTRATION | PD |
| 1076 | § 27-2100 ADM CODE - FILE WITH THIS  DEPARTMENT A REGISTRATION STATEMENT WITH A PROPER ADDRESS FOR REGISTERED PARTY | ANNUAL PROPERTY REGISTRATION | 1076 - ADDRESS OF OWNER INCORRECT | PD |
| 1079 | § 27-2105 ADM CODE - RENT BILL OR RECIEPT NOT PROVIDED FOR TENANT WITH NAME AND ADDRESS OF INDIVIDUAL ACTING AS MANAGING AGENT OR NAME AND ADDRESS OF OWNER PRINTED OR STAMPED THEREON | ANNUAL PROPERTY REGISTRATION | 1079 - RENT RECEIPT NOT PROVIDED | PD |
| 1492 | § 9, 170, 171, 300, 301, 302 M.D.LAW-FILE PLANS AND APPLICATION AND OBTAIN A CERTIFICATE OF OCCUPANCY TO LEGALIZE THE CONVERSION FROM A PRIVATE DWELLING TO MULTIPLE DWELLING USE IF LAWFULLY FEASIBLE OR RESTORE TO LAWFUL OCCUPANCY | CONVERSIONS | 1492 - FILE PLANS & OBTAIN C/O TO LEGALIZE CONVERSION FROM PD TO MD | PD |
| 1493 | § 9, 56, 193, 300, 302 M.D. LAW- ABOVE FRAME BUILDING HAS BEEN CONVERTED FROM A PRIVATE DWELLING TO A MULTIPLE DWELLING AND IS NOW OCCUPIED AND MAINTAINED AS SUCH CONTRARY TO LAW.RESTORE PREMISES TO LAWFUL OCCUPANCY | CONVERSIONS | 1493 - CONVERTED FROM PD TO MD - RESTORE TO LAWFUL OCCUPANCY | PD |
| 1499 | § 27-2005 HMC: IMMEDIATELY PROVIDE A FIRE GUARD AS DIRECTED BY THE NYC DEPT. OF HOUSING PRESERVATION & DEVELOPMENT (HPD) AND/OR THE NYC DEPT. OF BUILDINGS (DOB) TO PROTECT AGAINST FIRE HAZARDS OBSERVED BY HPD AND/OR DOB. FIRE HAZARDS OBSERVED BY HPD HAVE | FIREGUARD | 1499 - PROVIDE FIRE GUARD | MD/PD |
| 1501 | §27-2045(B)(5) HMC, § 12-06, 12-10 RCNY POST A PROPER NOTICE OF CARBON MONOXIDE DETECTING DEVICE REQUIREMENTS, IN A FORM APPROVED BY COMMISSIONER, IN A COMMON AREA OF A CLASS A MULTIPLE DWELLING NEAR INSPECTION CERTIFICATE OR PROVIDE NOTICE TO TENANTS IN PRIVATE DWELLINGS | CARBON MONOXIDE DETECTING DEVICES | 1501 - POST CO DETECTOR NOTICE | MD/PD |
| 1502 | § 27-2046.1, 2046.2 HMC: PROVIDE AN APPROVED AND OPERATIONAL CARBON MONOXIDE DETECTING DEVICE, INSTALLED IN ACCORDANCE WITH APPLICABLE LAW AND RULES. | CARBON MONOXIDE DETECTING DEVICES | 1502 - NO CO DETECTOR OR DETECTOR NOT OPERATIONAL | MD/PD |
| 1503 | § 27-2045(B)(1)(B) HMC, § 12-06, § 12-07, § 12-09 RCNY REPAIR, REPLACE OR PROVIDE AN APPROVED AND OPERATIONAL CARBON MONOXIDE DETECTING DEVICE, INSTALLED IN ACCORDANCE WITH APPLICABLE LAW AND RULES | CARBON MONOXIDE DETECTING DEVICES | 1503 - REPAIR OR REPLACE CO DETECTOR | MD/PD |
| 1504 | § 27-2046.1, 2046.2 HMC: FILE CERTIFICATION OF SATISFACTORY INSTALLATION OF CARBON MONOXIDE DETECTING DEVICE(S) IN ACCORDANCE WITH HPD RULE. | RETIRED | 1504 - FILE CERTIFICATION FOR CO DETECTOR | MD/PD |
| 1505 | § 27-2046.1, 2046.2 HMC: MAINTAIN ON THE PREMISES AND MAKE AVAILABLE TO THE DEPARTMENT UPON REQUEST RECORDS OF INSTALLATION AND MAINTENANCE OF CARBON MONOXIDE DETECTING DEVICE(S) IN THE BUILDING. | RECORD-KEEPING: CARBON MONOXIDE DETECTING DEVICES | 1505 - PROVIDE CO DETECTOR RECORDS | MD/PD |
| 1506 | § 27-2005 HMC: POST, IN A FORM APPROVED BY THE COMMISSIONER, AND MAINTAIN A NOTICE IN A COMMON AREA OF THE BUILDING REGARDING THE PROCEDURES THAT SHOULD BE FOLLOWED WHEN A GAS LEAK IS SUSPECTED | POSTING/SIGNAGE | 1506 - POST GAS LEAK NOTICE | MD/PD |
| 1507 | (A) § HMC:FILE ANNUAL BEDBUG REPORT IN ACCORDANCE WITH HPD RULE AS DESCRIBED ON THE BACK OF THIS NOTICE OF VIOLATION OR AS DESCRIBED ON HPD’S WEBSITE, WWW.NYC.GOV\HPD, SEARCH BED BUGS. | FILING: BEDBUGS | 1507 - FILE ANNUAL BEDBUG REPORT | MD |
| 1508 | (A) § HMC: POST AT OR NEAR THE MAILBOXES OR DISTRIBUTE TO EACH TENANT UPON COMMENCEMENT OF NEW LEASE OR UPON LEASE RENEWAL, IN THE FORM APPROVED BY THE COMMISSIONER, THE ANNUAL BEDBUG REPORT AND A COPY OF THE DOHMH PREVENTING AND GETTING RID OF BEDBUGS SA | POSTING/SIGNAGE | 1508 - POST, THE ANNUAL BEDBUG REPORT | MD |
| 1509 | §27-2018.1  HMC: POST, IN THE FORM APPROVED BY THE COMMISSIONER, AND MAINTAIN THE NOTICE ABOUT PREVENTION, DETECTION AND REMOVAL OF BEDBUG INFESTATION REQUIRED BY §27-2018.1 IN COMMON AREA OF THE BUILDING OR PROVIDE TO EACH TENANT, ACCORDING TO THE CERTIF | POSTING/SIGNAGE | 1509 - POST, NOTICE ABOUT PREVENTION | MD |
| 1511 | § 28-315.2.4 PROVIDE AND INSTALL NATURAL GAS ALARM(S) IN ACCORDANCE WITH SECTION 908.10 OF THE NEW YORK CITY BUILDING CODE | NATURAL GAS DETECTING DEVICES | EFFECTIVE JAN 1, 2027: PROVIDE GAS ALARM/DETECTOR | MD |
| 1520 | §27-2104(b) HMC: POST A PROPER NOTICE REGARDING RENT STABILIZATION LAW, IN A FORM APPROVED BY THE COMMISSIONER, IN A CONSPICUOUS LOCATION WITHIN THE COMMON AREA AT THE BUILDING’S ENTRANCE. | POSTING/SIGNAGE | 1520 - RENT STABILIZATION LAW INFORMATION SIGN | MD |
| 1524 | §27-2005 (E) HMC: PROVIDE WRITTEN NOTICE TO THE TENANTS AT LEAST TWENTY-FOUR HOURS PRIOR TO ESSENTIAL SERVICE INTERRUPTION BY POSTING A NOTICE IN A PROMINENT PLACE WITHIN THE PUBLIC PART OF THE BUILDING AND ON EACH FLOOR OF SUCH BUILDING, WHERE AN OWNER M | NOTIFICATION: INTERRUPTION OF SERVICE | 1524 - PROVIDE NOTICE - ESSENTIAL SERVICE INTERRUPTION | MD/PD |
| 81B | § 194 M/D LAW  PROVIDE SPRINKLER HEADS IN ALL CLASS B ROOMS AND FILE APPLICATION FOR APPROVAL BEFORE DOING THIS WORK | FIRE EGRESS AND PROTECTION | 81B - NO SPRINGKLER HEADS IN CLASS B ROOMS | MD |

## Sheet: FAQs

| Data Dictionary - Frequently Asked Questions |
| Do all violations require property owners provide a certification by the certification deadline for all violation types? If not, is there a list of violation types by order number that require different conditions for property owner follow up? | Failure to certify the correction of a violation subjects the property owner to potential civil penalties should HPD seek to enforce the correction in Housing Court. Violations such as lead-based paint hazard violations and mold violations under certain circumstances require that an owner also provide evidence of having used appropriate certified or licensed firms or workers.  Violations such as property registration and for failure to file a bedbug annual report only require the owner to submit valid documents. If owners fail to timely certify, there is another process called the Dismissal Request process for the owner to request reinspections of open violation. |
| Under what conditions does HPD do a reinspection or conduct additional follow-up? Is it just for cases when either a violation does not receive a certification from the property owner or a tenant is contacted after a violation and informs hpd that the issue hasn't been addressed? | HPD’s Division of Code Enforce can reinspect a violation at any time. However, there are some general categories that account for the a large percentage of attempted violation reinspections: —Audit reinspection of a certified violation or tenant challenge of a certified violation —Owner request (see Dismissal Request process information OHO/DCE FORM- DR-1 (nyc.gov)) —Proactive reinspection initiated by the agency —Pursuant to court action |
| What happens if a tenant provides follow-up on a violation after the 70 day window? | If the violation has already been closed the tenant will have to file a new complaint and start the process again. |
| Why are certain violations with a current status listed as "will be reinspected" listed as open while others are closed? | The status “will be reinspected” indicates that the violation may have been associated with a reinspection type of record created in HPD’s database.  It does not indicate that a reinspection of the violation will necessarily be attempted or completed. |
| What order numbers are for lead violations? | You can find more information under the "Order Number" tab in this spreadsheet by filtering for "LEAD-BASED PAINT" in the Category column. |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History |
| Description of all major changes to the format including what specific fields were added or removed, data calculation method, or method of collection of the data that have taken place since the initial version. Adding or updating new data values does not necessitate a new version entry. |
| Date | Change Highlights | Comments |
| 2014-02-14 00:00:00 | Creation of dataset |
| 2025-12-18 00:00:00 | FAQ Addition |

## Sheet: Primer Page & InternaI Info.

| Data Dictionary - Open Data Team Internal Information |
| This section is used for internal purposes by the Open Data Team and can be ignored by external data users. |
| Information shared in this section may be publicly displayed on the dataset’s primer page on NYC Open Data. |
| Dataset Tags | housing, housing violations, hpd |
| A list of comma-separated terms, based on the topic of the dataset, that will link to other datasets with that same tag. |
| Tags are used along with the dataset name and description to search NYC Open Data. |
| Are rows removed from this dataset when the data is updated? | No |
| Can this dataset be feasibly automated? | Yes |
| Is this data also present on a website maintained by or on behalf of the agency? | Yes: https://hpdonline.nyc.gov/hpdonline/ |
| If so, please provide the website URL. |
| What is the update frequency of the data on the agency's website? | Daily |
| Only applicable if the data is also present on a website maintained by or on behalf of the agency |
| Is the data on the agency's website updated automatically? | Yes |
| Only applicable if the data is also present on a website maintained by or on behalf of the agency |

## Sheet: Hidden_Frequencies

| Hourly | Hourly |
| Daily | Daily |
| Weekly | Weekly |
| Every weekday | Every weekday |
| Every 2 weeks | Every 2 weeks |
| Monthly | Monthly |
| Every 2 months | Every 2 months |
| Quarterly | Quarterly |
| Every 4 months | Every 4 months |
| Every 6 months | Every 6 months |
| Annually | Annually |
| Every 2 years | Every 2 years |
| Every 3 years | Every 3 years |
| Every 4 years | Every 4 years |
| Every 5 years | Every 5 years |
| Every 10 years | Every 10 years |
| Historical data | Historical data |
| As needed | As needed |
| Other | Other |

## Sheet: Hidden_Agencies

| 311 |
| Administration for Children's Services (ACS) |
| Banking Commission |
| Board of Correction (BOC) |
| Board of Elections (BOENY) |
| Board of Standards and Appeals (BSA) |
| Bronx Borough President (BPBX) |
| Brooklyn Borough President (BPBK) |
| Brooklyn Public Library (BPL) |
| Business Integrity Commission (BIC) |
| Campaign Finance Board (CFB) |
| Children's Cabinet |
| City Clerk & Clerk of the Council (OCC) |
| City Council (NYCC) |
| City Employees' Retirement System (NYCERS) |
| City University of New York (CUNY) |
| Civic Engagement Commission (CEC) |
| Civil Service Commission (CSC) |
| Civilian Complaint Review Board (CCRB) |
| Commission on Human Rights (CCHR) |
| Commission to Combat Police Corruption (CCPC) |
| Conflicts of Interest Board (COIB) |
| Department for the Aging (DFTA) |
| Department of Buildings (DOB) |
| Department of City Planning (DCP) |
| Department of Citywide Administrative Services (DCAS) |
| Department of Consumer and Worker Protection (DCWP) |
| Department of Correction (DOC) |
| Department of Cultural Affairs (DCLA) |
| Department of Design and Construction (DDC) |
| Department of Education (DOE) |
| Department of Environmental Protection (DEP) |
| Department of Finance (DOF) |
| Department of Health and Mental Hygiene (DOHMH) |
| Department of Homeless Services (DHS) |
| Department of Housing Preservation and Development (HPD) |
| Department of Investigation (DOI) |
| Department of Parks and Recreation (DPR) |
| Department of Probation (DOP) |
| Department of Records and Information Services (DORIS) |
| Department of Sanitation (DSNY) |
| Department of Small Business Services (SBS) |
| Department of Social Services (DSS) |
| Department of Transportation (DOT) |
| Department of Veterans' Services (DVS) |
| Department of Youth and Community Development (DYCD) |
| Environmental Control Board (ECB) |
| Equal Employment Practices Commission (EEPC) |
| Financial Information Services Agency (FISA) & Office of Payroll Administration (OPA) |
| Fire Department of New York City (FDNY) |
| Human Resources Administration (HRA) |
| Independent Budget Office (IBO) |
| Landmarks Preservation Commission (LPC) |
| Law Department (LAW) |
| Manhattan Borough President (MBPO) |
| Mayor's Community Affairs Unit (CAU) |
| Mayor's Office Counsel |
| Mayor's Office for Economic Opportunity |
| Mayor's Office for International Affairs |
| Mayor's Office for People with Disabilities (MOPD) |
| Mayor's Office for Strategic Partnerships (OSP) |
| Mayor's Office of Citywide Event Coordination and Management (CECM) |
| Mayor's Office of Climate and Environmental Justice (MOCEJ) |
| Mayor's Office of Community Mental Health (OCMH) |
| Mayor's Office of Contract Services (MOCS) |
| Mayor's Office of Criminal Justice (MOCJ) |
| Mayor's Office of Food Policy (MOFP) |
| Mayor's Office of Housing Recovery Operations (HRO) |
| Mayor's Office of Immigrant Affairs (MOIA) |
| Mayor's Office of Media and Entertainment (MOME) |
| Mayor's Office of Minority and Women Owned Businesses (MWBE) |
| Mayor's Office of Operations (OPS) |
| Mayor's Office of Special Enforcement |
| Mayor's Office of Special Projects and Community Events (MOSPCE) |
| Mayor's Office to End Domestic and Gender-Based Violence (ENDGBV) |
| Mayor's Office to Protect Tenants (MOPT) |
| Mayor’s Office of Workforce Development (WKDEV) |
| Metropolitan Transportation Authority (MTA) |
| New York City Housing Authority (NYCHA) |
| New York Public Library (NYPL) |
| NYC & Company (NYCGO) |
| NYC Advisory Committee on the Judiciary |
| NYC Center for Innovation through Data Intelligence (CIDI) |
| NYC Emergency Management (NYCEM) |
| NYC Health + Hospitals |
| NYC Office of the Administrative Justice Coordinator |
| NYC Service |
| Office of Administrative Tax Appeals (OATA) / (Tax Commission & Tax Appeals Tribunal) |
| Office of Administrative Trials and Hearings (OATH) |
| Office of Chief Medical Examiner (OCME) |
| Office of Collective Bargaining (OCB) |
| Office of Labor Relations (OLR) |
| Office of Management and Budget (OMB) |
| Office of Technology and Innovation (OTI) |
| Office of the Actuary |
| Office of the Comptroller (COMPTROLLER) |
| Police Department (NYPD) |
| Police Pension Fund (NYCPPF) |
| Procurement Policy Board (PPB) |
| Public Design Commission (formerly Art Commission (ARTCOM) and Design Commission) |
| Queens Borough President (QBP) |
| Queens Library (QBPL) |
| School Construction Authority (SCA) |
| Staten Island Borough President (BPSI) |
| Taxi and Limousine Commission (TLC) |
| Young Men's Initiative (YMI) |

## Sheet: Hidden_DataTypes

| Date & Time |
| Location/Point/Line/Polygon |
| Number |
| Text |
| True-False/Checkbox/Binary |
| URL/Website |
