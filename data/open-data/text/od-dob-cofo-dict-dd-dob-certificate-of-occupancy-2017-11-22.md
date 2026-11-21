# Data dictionary: od-dob-cofo-dict-dd-dob-certificate-of-occupancy-2017-11-22.xlsx

Source: https://data.cityofnewyork.us/d/bs8b-p36w
Extracted from: od-dob-cofo-dict-dd-dob-certificate-of-occupancy-2017-11-22.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | DOB Certificate Of Occupancy |
| Agency Name | Department of Buildings (DOB) |
| Update Frequency | Daily |
| Dataset Description | A Certificate of Occupancy (CO) states a building’s legal use and/or type of permitted occupancy. New buildings must have a CO, and existing buildings must have a current or amended CO when there is a change in use, egress or type of occupancy. No one may legally occupy a building until the Department has issued a Certificate of Occupancy or Temporary Certificate of Occupancy. The Department issues a final Certificate of Occupancy when the completed work matches the submitted plans for new buildings or major alterations. It issues a Letter of Completion for minor alterations to properties. These documents confirm the work complies with all applicable laws, all paperwork has been completed, all fees owed to the Department have been paid, all relevant violations have been resolved and all necessary approvals have been received from other City Agencies. |
| Dataset Keywords | building, occupancy, certificate, C of O, CO |
| Dataset Category | Housing & Development |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. | Data Set Volume and Growth Expectation: Approximately 71600 record for 5 years . Average 55 records per day. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the idiosyncrasies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) | Data Type (Plain Text, Number, Date) | Required |
| JOB_NUMBER | Number assigned by the Department of Buildings to the job application that the Certificate of Occupancy was issued for. | This is a primary key that can be used to find job application details in our other datasets. | varchar(9) | Yes |
| JOB_TYPE | 2-digit code to indicate the overall job type for the application. | A Certificate of Occupancy is issued after a new building is built or after a major alteration that affects the use, egress, or type of occupancy of the building.   Expected values are: • A1 = Alteration Type I, A major alteration that will change the use, egress, or occupancy of the building. • NB = New Building, An application to build a new structure. “NB” cannot be selected if any existing building elements are to remain—for example a part of an old foundation, a portion of a façade that will be incorporated into the construction, etc. | varchar(2) | Yes |
| C_O_ISSUE_DATE | Date the Certificate of Occupancy was issued. |  | Date in MM/DD/YYYY format | Yes |
| BIN_NUMBER | Building Identification Number (BIN) assigned by Department of City Planning. | This BIN Number comes from our BIS database. The second BIN column later in this dataset is added as part of the geocoding process required by law. | varchar(7) | Yes |
| BOROUGH | The name of the NYC borough where the building is located. | Expected values = Manhattan, Bronx, Brooklyn, Queens, Staten Island | varchar(20) | Yes |
| NUMBER | The house number for the building address. | In the address, "280 Broadway", 280 is the house number. This number may contain a dash (-), as in "8-15 27 Avenue". | varchar(12) | Yes |
| STREET | The street name for the building address. | In the address, "1050 Park Place", Park Place is the street name. | varchar(32) | Yes |
| BLOCK | Tax Block assigned to the location of the building by the Department of Finance. | This is the block number issued on the Certificate of Occupancy. It is based on the block number as it was submitted on the job application for the construction work that resulted in the Certificate of Occupancy. Block numbers can change over time, so this may not reflect the current data for the building. | varchar(5) | Yes |
| LOT | Tax Lot assigned to the location of the building by the Department of Finance. | This is the lot number issued on the Certificate of Occupancy. It is based on the lot number as it was submitted on the job application for the construction work that resulted in the Certificate of Occupancy. Lot numbers can change over time, so this may not reflect the current data for the building. | varchar(5) | Yes |
| POSTCODE | The Zip Code for the building address. |
| PR_DWELLING_UNIT | This is the proposed number of dwelling units in the building after the proposed work has been completed, as reported by the applicant. |  | varchar(5) | Yes |
| EX_DWELLING_UNIT | This is the existing number of dwelling units in the building, as reported by the applicant. |  | varchar(5) | Yes |
| APPLICATION_STATUS_RAW | The status of the application for a Certificate of Occupancy. | Expected values = Open, Issued, Withdrawn | varchar(25) | Yes |
| FILING_STATUS_RAW | The filing status of the application for a Certificate of Occupancy. | Expected values = Amended, Final, New, Temporary | varchar(25) | Yes |
| ITEM_NUMBER | aka Issue Number. Number of Partitioned Units of Work for a Job. |  | varchar(3) | Yes |
| ISSUE_TYPE | The type of Certificate of Occupancy that was issued. | Expected values = Temporary, Final | varchar(15) | Yes |
| LATITUDE | Geographical latitude of the building. | Geocoded based on address. |
| LONGITUDE | Geographical longitude of the building. | Geocoded based on address. |
| COMMUNITY_BOARD | Community Board Number for the building’s address. | Geocoded based on address. |
| COUNCIL_DISTRICT | Council district for the building's address. | Geocoded based on address. |
| CENSUS_TRACT | Census tract for the building's address. | Geocoded based on address. |
| BIN | Building Identification Number (BIN) assigned by Department of City Planning. | Geocoded based on address. |
| BBL | A number that is created by concatenating a number for the borough (indicated below), the Block number and the Lot number.   • 1 = Manhattan • 2 = Bronx • 3 = Brooklyn • 4 = Queens • 5 = Staten Island | Geocoded based on address. |
| NTA | Neighborhood Tabulation Area | Geocoded based on address. |
| LOCATION | Latitude and Longitude. Used for mapping purpose | Geocoded based on address. |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
| 1 | 2017-05-15 00:00:00 | New |
| 2 | 2017-11-22 00:00:00 | Updated with more plain language definition and clarification of the provenance of some fields. |

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
