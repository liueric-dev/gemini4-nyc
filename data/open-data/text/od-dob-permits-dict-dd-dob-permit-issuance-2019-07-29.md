# Data dictionary: od-dob-permits-dict-dd-dob-permit-issuance-2019-07-29.xlsx

Source: https://data.cityofnewyork.us/d/ipu4-2q9a
Extracted from: od-dob-permits-dict-dd-dob-permit-issuance-2019-07-29.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | DOB Permit Issuance |
| Agency Name | Department of Buildings (DOB) |
| Update Frequency | Daily |
| Dataset Description | A list of permits issued by the Department of Buildings since 1989. |
| Dataset Keywords | permit, dob, buildings |
| Dataset Category | Housing & Development |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the idiosyncrasies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) | Data Type (Plain Text, Number, Date) | Required |
| BOROUGH | The name of the NYC borough where the proposed work will take place. | Expected values = Manhattan, Bronx, Brooklyn, Queens, Staten Island. | Text | Yes |
| Bin # | Building Identification Number assigned by Department of City Planning. |  | Number | Yes |
| House # | The house number for the building where the proposed work will take place. | In the address, "280 Broadway", 280 is the house number. This number may contain a dash (-), as in "8-15 27 Avenue". | Text |
| Street Name | The street name for the building where the proposed work will take place. | In the address, "1050 Park Place", Park Place is the street name. | Text | Yes |
| Job # | The DOB Job Application Number assigned when the applicant begins the application. | This is the unique identifier for the application submitted to the Department. It may contain several work types, and more work types may be added as the application review and the work continues. It is a 9-digit number where the first digit indicates the borough where the building is located.  • 1 = Manhattan • 2 = Bronx • 3 = Brooklyn • 4 = Queens • 5 = Staten Island | Number | Yes |
| Job doc. # | A sequential number assigned to each of the documents that make up a job application. | Every job application should have a 01 document. Every additional document receives a number that increases by 1 (ex: 02, 03, 04) | Text | Yes |
| Job Type | 2-digit code to indicate the overall job type for the application.  Note: You should also look at the Permit Type field to find out what this specific permit has been issued for. An NB job, for example, can have several different Work/Permit Types such as PL, SP, EQ, etc. And each Work/Permit Type will be issued a seperate permit. | Expected values are: • A1 = Alteration Type I, A major alteration that will change the use, egress, or occupancy of the building. • A2 = Alteration Type II, An application with multiple types of work that do not affect the use, egress, or occupancy of the building. • A3 = Alteration Type III, One type of minor work that doesn't affect the use, egress, or occupancy of the building. • NB = New Building, An application to build a new structure. “NB” cannot be selected if any existing building elements are to remain—for example a part of an old foundation, a portion of a façade that will be incorporated into the construction, etc. • DM = Demolition, An application to fully or partially demolish an existing building. • SG = Sign, An application to install or remove an outdoor sign. | Text | Yes |
| Self_Cert | Indicates whether or not the application was submitted as Professionally Certified. A Professional Engineer (PE) or Registered Architect (RA) can certify compliance with applicable laws and codes on applications filed by him/her as applicant. | Expected values are:  • Y = Yes.  • N = No. • blank = No information for this record. | Text | No |
| Block | Tax Block assigned to the location of the proposed work by the Department of Finance. |  | Text | Yes |
| Lot | Tax Lot assigned to the location of the proposed work by the Department of Finance. | Note: NYC Tax Lots are 4 digits. This dataset reports them in 5 digits with a leading zero. If you are concatenating fields to create the BBL, you will need to adjust for this. | Text | Yes |
| Community Board | Community Board Number for the building’s address. |  | Text | Yes |
| Zip Code | ZIP Code for the building's address. |  | Text | No |
| Bldg Type | Legal occupancy classification. | Expected values are: • 1 = 1-2-3 Family • 2 = Other  DOF classification has 36 types - this field just simplifies it for DOB purposes. Anything above 3 family we consider multiple dwelling and is regulated more heavily. Other agencies might have different cutoffs. | Text | No |
| Residential |  | Expected values are:  • Y = Yes.  • blank = No information for this record. | Text | No |
| Special District 1 |  |  | Text | No |
| Special District 2 |  |  | Text | No |
| Work Type | The specific type of work covered by the permit. | This is a two character code to indicate the type of work. Check the Type Values sheet in this document for expected values and definitions. If the Work Type is blank, check the Permit Type. | Text | No |
| Permit Status | The current status of the permit application. | Expected values are  • IN PROCESS = The applicant submitted the PW-2 appliction for a permit and it is being processed • ISSUED = The permit has been issued • RE-ISSUED = The permit has been reissued • REVOKED = The permit has been revoked | Text | Yes |
| Filing Status | Indicates if this is the first time the permit is being applied for or if the permit is being renewed. | Expected values are INITIAL or RENEWAL. | Text | Yes |
| Permit Type | The specific type of work covered by the permit. | This is a two character code to indicate the type of work. Check the Type Values sheet in this document for expected values and definitions. | Text | Yes |
| Permit Sequence # | A sequential number assigned to each issuance of the particular permit from initial issuance to each subsequent renewal. | Every initial permit should have a 01 sequence number. Every additional renewal receives a number that increases by 1 (ex: 02, 03, 04) | Text | Yes |
| Permit Subtype | A more specific designation for the type of work indicated in the Permit Type. | This is a two character code to indicate the type of work. Check the Type Values sheet in this document for expected values and definitions. | Text | No |
| Oil Gas | If the permit is for work on fuel burning equipment, this indicates whether it burns oil or gas. | Expected values are OIL, GAS, or blank. | Text | No |
| Site Fill | This indicates the source of any fill dirt that will be used on the construction site. When over 300 cubic yards of fill is being used, the Department is required to inform Sanitation of where the fill is coming from and the amount. | Expected Values are: • USE UNDER 300 CU.YD = Less than 300 cubic yards (on-site or off-site) is being used.  • NOT APPLICABLE = Not applicable to proposed work. • ON-SITE = 300 or more cubic yards of fill is being used from on-site. • OFF-SITE = 300 or more cubic yards of fill will be transplanted from an off-site location. • blank | Text | No |
| Filing Date | The date the permit application was filed with DOB. |  | Date | Yes |
| Issuance Date | The date the permit was issued. |  | Date | Yes |
| Expiration Date | The date that the permit expires. |  | Date | Yes |
| Job Start Date | The date that the initial permit was issued for this Permit Type. |  | Date | Yes |
| Permittee's First Name | First name of the person that the permit was issued to. |  | Text | Yes |
| Permittee's Last Name | Last name of the person that the permit was issued to. |  | Text | Yes |
| Permittee's Business Name | Business name of the person that the permit was issued to. |  | Text | Yes |
| Permittee's Phone # | Phone number of the person that the permit was issued to. |  | Text | Yes |
| Permittee's License Type | Professional license type of the person that the permit was issued to. | Expected values are: DM =  FS = Fire Suppression Contractor GC = General Contractor HI =  MP = Master Plumber NW =  OB = Oil Burner Installer OW =  PE = Professional Engineer RA = Registered Architect SI = Sign Hanger | Text | Yes |
| Permittee's License # | Professional license number of the person that the permit was issued to. |  | Text | No |
| Act as Superintendent | Indicates if the permittee acts as the Construction Superintendent for the work site. | Expected values are Y, blank. | Text | No |
| Permittee's Other Title | Another license number for the person that the permit was issued to, if any. |  | Text | No |
| HIC License | NYC-Registered Home Improvement Contractors (HIC)  need a license for all alteration work in 1-, 2-, 3- , 4-family homes or individual apartments in condos/co-ops. HIC licenses are issued by the NYC Department of Consumer Affairs. |  | Text | No |
| Site Safety Mgr's First Name | The Site Safety Manager's first name. | A certified Site Safety Manager is required on new construction or demolition sites 15 stories and above or 100,000 square feet or greater. | Text | No |
| Site Safety Mgr's Last Name | The Site Safety Manager's last name. |  | Text | No |
| Site Safety Mgr Business Name | The Site Safety Manager's business name. |  | Text | No |
| Superintendent First & Last Name | The Construction Superintendent's first and last name. | A registered Construction Superintendent is required at new buildings and buildings under demolition nine stories and below. | Text | No |
| Superintendent Business Name | The Construction Superintendent's business name. |  | Text | No |
| Owner's Business Type | Indicates the type of entity that owns the building where the work will be performed. |  | Text | No |
| Non-Profit | Indicates if the building is owned by a non-profit. | Expected values are Y, N, blank. | Text | No |
| Owner's Business Name | Business name for the owner of the building where the work will be performed. |  | Text | No |
| Owner's First Name | First name of the owner of the building where the work will be performed. |  | Text | Yes |
| Owner's Last Name | Last name of the owner of the building where the work will be performed. |  | Text | Yes |
| Owner's House # | House number for the address of the owner of the building where the work will be performed. |  | Text | Yes |
| Owner's House Street Name | Street for the address of the owner of the building where the work will be performed. |  | Text | Yes |
| Owner's House City | City for the address of the owner of the building where the work will be performed. |  | Text | Yes |
| Owner's House State | State for the address of the owner of the building where the work will be performed. |  | Text | No |
| Owner's House Zip Code | ZIP Code for the address of the owner of the building where the work will be performed. |  | Text | Yes |
| Owner's Phone # | Phone number of the owner of the building where the work will be performed. |  | Text | Yes |
| DOBRunDate | Date when query is run and pushed to Open Data. Could be used to differentiate report dates. |  | Date | Yes |
| PERMIT_SI_NO |  |  | Text | Yes |
| LATITUDE | Latitude for the building where the proposed work will take place. |  | Text | Yes |
| LONGITUDE | Longitude for the building where the proposed work will take place. |  | Text | Yes |
| COUNCIL_DISTRICT | Council District for the building where the proposed work will take place. |  | Text | Yes |
| CENSUS_TRACT | Census Tract for the building where the proposed work will take place. |  | Text | Yes |
| NTA_NAME | Neighborhood Tabulation Area for the building where the proposed work will take place. | Neighborhood Tabulation Areas (NTAs) were created to project populations at a small area level, from 2000 to 2030 for PlaNYC, the long-term sustainability plan for New York City. For more info, go to https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-nynta.page. | Text | Yes |

## Sheet: Type Values

| Work Type |
| Acronym | Stands for |
| BL | Boiler |
| CC | Curb Cut |
| EQ | Construction Equipment |
| FA | Fire Alarm |
| FB | Fuel Burning |
| FP | Fire Suppression |
| FS | Fuel Storage |
| MH | Mechanical/HVAC |
| NB | New Building |
| OT | Other |
| PL | Plumbing |
| SD | Standpipe |
| SP | Sprinkler |
| Permit Type |
| Acronym | Stands for |
| AL | Alteration |
| DM | Demolition |
| EQ | Construction Equipment |
| EW | Equipment Work |
| FO | Foundation |
| NB | New Building |
| PL | Plumbing |
| SG | Sign |
| Permit SubType |
| Acronym | Stands for |
| BL | Boiler |
| CH | Chute |
| EA | Earthwork |
| FA | Fire Alarm |
| FB | Fuel Burning |
| FN | Fence |
| FP | Fire Suppression |
| FS | Fuel Storage |
| MH | Mechanical/HVAC |
| OT | Other |
| SC | Scaffold (only one job in 1991 - this is likely a typo) |
| SD | Standpipe |
| SF | Scaffold |
| SH | Sidewalk Shed |
| SP | Sprinkler |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
| 1 | 2016-08-09 00:00:00 | Created |
| 2 | 2018-02-12 00:00:00 | Updated with more plain language explanation. |
| 3 | 2018-03-07 00:00:00 | Added 2 expected values to Permittee's License Type. | There are now 4 expected values for this field that need definition. We are researching them. |
| 4 | 2018-08-13 00:00:00 | Clarified an issue with Lot - dataset reports 5 digits with leading zero even though it should just be 4 digits. |
| 5 | 2018-08-23 00:00:00 | Clarified expected values in Building Type |
| 6 | 2018-11-02 00:00:00 | Clarified Permit Status |
| 7 | 2019-07-29 00:00:00 | Added Type Values sheet |

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
