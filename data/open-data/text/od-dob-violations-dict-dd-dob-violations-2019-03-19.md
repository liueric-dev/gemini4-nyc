# Data dictionary: od-dob-violations-dict-dd-dob-violations-2019-03-19.xlsx

Source: https://data.cityofnewyork.us/d/3h2n-5cm9
Extracted from: od-dob-violations-dict-dd-dob-violations-2019-03-19.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | DOB Violations |
| Agency Name | Department of Buildings |
| Update Frequency | Currently says weekdays - is that still an allowable value? |
| Dataset Description | This data set includes older civil penalties (commonly referred to as ‘DOB Violations’) that were issued by the Department of Buildings (DOB) in the Buildings Information System (BIS).  For newer civil penalties, see the DOB Safety Violations data set (note: some violations are duplicated in both data sets).  Separately, summonses that are issued by DOB but adjudicated by OATH/ECB are in the DOB ECB Violations data set. |
| Dataset Keywords | dob, buildings, violation |
| Dataset Category | Housing & Development |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the idiosyncrasies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Term, Acronym, or Code Definitions | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) |
| ISN_DOB_BIS_VIOL | An internal code that serves as a unique value. |
| BORO | Borough code: (1= Manhattan, 2= Bronx, 3 = Brooklyn, 4 = Queens, 5 = Staten Island) |
| BIN | Building Identification Number assigned by Department of City Planning. |
| BLOCK | Tax Block assigned to the location of the proposed work by the Department of Finance. |
| LOT | Tax Lot assigned to the location of the proposed work by the Department of Finance. |
| ISSUE_DATE | Date that the violation was issued. | Format is YYYYMMDD | Example: 20180406 = April 6, 2018 |
| VIOLATION_TYPE_CODE | A code that categorizes the violation. |  | Values are: • AEUHAZ1 • B = Boiler • C = Construction • E = Elevator • EGNCY = Emergency • FISP = Façade Safety Program • HBLVIO = High Pressure Boiler • IMEGNCY = Immediate Emergency • LANDMK = Landmark Building • P = Plumbing • UB = Unsafe Building • Z = Zoning |
| VIOLATION_NUMBER | The number associated with the violation. |
| HOUSE_NUMBER | The house number for the building where the violation was issued. |
| STREET | The street name for the building where the violation was issued. |
| DISPOSITION_DATE | Date that the violation was dispositioned. |  | Format: YYYYMMDD |
| DISPOSITION_COMMENTS | Additional comments by the inspector at disposition. |
| DEVICE_NUMBER | Elevators and High Pressure Boilers are registered with the Department and issued a Device Number. |  | FISP violations may also include a device number. In this case, it is the Façade Control Number. |
| DESCRIPTION | Notes manually entered by the DOB inspector. |
| ECB_NUMBER | The number of an associated ECB violation, if any. |  | If there is an associated ECB Violation, you can use this number to look up the details in the DOB ECB Violations dataset. |
| NUMBER | An ID that combines several values to create a unique ID. |  | Concatenates the following: • V - for violation • the Issue Date in MMDDYY format • VIOLATION_TYPE_CODE • VIOLATION_NUMBER |
| VIOLATION_CATEGORY | A code and description for the current status of the violation. |  | Values are:  • V*-DOB VIOLATION - DISMISSED • V*-DOB VIOLATION - Resolved • V-DOB VIOLATION - ACTIVE • VP*-VIOLATION UNSERVED ECB- DISMISSED • VP-VIOLATION UNSERVED ECB-ACTIVE • VPW*-VIOLATION UNSERVED ECB-WORK WITHOUT PERMIT-DISMISSED • VPW-VIOLATION UNSERVED ECB-WORK WITHOUT PERMIT-ACTIVE • VW*-VIOLATION - WORK W/O PERMIT DISMISSED • VW-VIOLATION WORK WITHOUT PERMIT - ACTIVE |
| VIOLATION_TYPE | A more descriptive version of the VIOLATION_TYPE_CODE field. |  | Values are:  • AEUHAZ1-FAIL TO CERTIFY CLASS 1 • B-BOILER • C-CONSTRUCTION • E-ELEVATOR • EGNCY-EMERGENCY • FISP-FACADE SAFETY PROGRAM • HBLVIO-HIGH PRESSURE BOILER • IMEGNCY-IMMEDIATE EMERGENCY • LANDMK-LANDMARK • P-PLUMBING • UB-UNSAFE BUILDINGS • Z-ZONING |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
| 1 | 2017-10-05 00:00:00 | Created data dictionary |
| 2 | 2019-03-19 00:00:00 | Added example to illustrate date format in ISSUE_DATE field |

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
