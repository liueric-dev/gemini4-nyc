# Data dictionary: od-hpd-conh-pilot-dict-conh-pilot-building-list-data-dictionary.xlsx

Source: https://data.cityofnewyork.us/d/bzxi-2tsw
Extracted from: od-hpd-conh-pilot-dict-conh-pilot-building-list-data-dictionary.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | Certification of No Harassment (CONH) Pilot Building List |
| Agency Name | Housing Preservation and Development |
| Update Frequency | Monthly |
| Dataset Description | List of buildings subject to Certification of No Harassment (CONH) Pilot Program. Data is current as of the update date shown below. To see the latest status of a building, visit HPD Online at https://www1.nyc.gov/site/hpd/about/hpdonline.page. |
| Dataset Keywords | CONH harassment |
| Dataset Category | Housing & Development |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. | Buildings on this list are subject to the Certification of No Harassment (CONH) Pilot Program. HPD promulgates this list pursuant to criteria set forth in Local Law 140 of 2021. Each record represents a building and is uniquely identified by a Building ID or BIN. All other location or address information is provided for informational purposes only. For more information on the program, see https://www1.nyc.gov/site/hpd/owners/certification-of-no-harassment.page |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the idiosyncrasies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Term, Acronym, or Code Definitions | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) |
| Building ID | Unique identifier of building (HPD) |
| BIN | Unique identifier of building (DOB) |
| Street Address | Building address |
| Borough | Borough where the building is located | 1: Manhattan 2: Bronx 3: Brooklyn 4: Queens 5: Staten Island |
| Block | Tax block |
| Lot | Tax lot |
| BQI | Building Qualification Index; building meets threshold of calculated BQI |  | Values: Yes, No |
| Discharged AEP | Building was discharged from the HPD Alternative Enforcement Program (AEP) |  | Values: Yes, No |
| Discharged 7A | Building was discharged from the HPD 7A program |  | Values: Yes, No |
| HPD Vacate Order | Building was issued HPD Order to Vacate |  | Values: Yes, No |
| DOB Vacate Order | Building was issued Department of Buildings (DOB) Order to Vacate |  | Values: Yes, No |
| Harassment Finding | Building was the subject of a finding of harassment by a court or by New York State Homes and Community Renewal |  | Values: Yes, No |
| Date Added | Date added to CONH Pilot Program List |
| BBL | Borough, block, lot - the unique identifier for each tax lot in NYC |
| Community Board | New York City Community District where building is located |
| Council District | New York City Council District where building is located |
| Latitude | Estimated location based on the street segment and address range. |
| Longitude |
| Census Tract | The 2010 US Census Tract where building is located |
| NTA - Neighborhood Tabulation Area | New York City Neighborhood Tabulation Area where the building is located |
| Zipcode | Zipcode where the building is located |
| Latitude (Internal) | Internal centroid derived from the tax lot |
| Longitude (Internal) |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
| 1 | 2018-11-27 00:00:00 | Original list |
| 2 | 2019-11-22 00:00:00 | Addition of fields: BQI, AEP Order, HPD Vacate Order, DOB Vacate Order, Harassment Finding, Date Added |
| 3 | 2022-06-27 00:00:00 | New list. Addition of fields: Discharged AEP, Discharged 7A. Removal of fields: AEP Order. |

## Sheet: Dropdown Options

| Dropdown Options |
| Update Frequency | Annually |
|  | Biannually |
|  | Triannually |
|  | Quarterly |
| X | Monthly |
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
| X | Housing & Development |
|  | Public Safety |
|  | Recreation |
|  | Social Services |
|  | Transportation |
