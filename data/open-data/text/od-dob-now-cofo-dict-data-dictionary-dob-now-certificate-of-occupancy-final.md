# Data dictionary: od-dob-now-cofo-dict-data-dictionary-dob-now-certificate-of-occupancy-final.xlsx

Source: https://data.cityofnewyork.us/d/pkdm-hqz6
Extracted from: od-dob-now-cofo-dict-data-dictionary-dob-now-certificate-of-occupancy-final.xlsx

## Sheet: Dataset Information

| Data Dictionary - Dataset Information |
| Dataset Name | DOB NOW: Certificate of Occupancy |
| Dataset URL | Filled in by the Open Data Team prior to publication |
| Data Provided by The name of the NYC agency providing this data to the public. | Department of Buildings (DOB) |
| Each row is a...  The unit of analysis/level of aggregation of the dataset | Issuance of a Certificate of Occupancy |
| Publishing Frequency How often changed data is published to this dataset. For an automatically updated dataset, this is the frequency of that automation | Monthly |
| Data Change Frequency How often the data underlying this dataset is changed | Daily |
| Frequency Details Additional details about the publishing or data change frequency, if needed | The underlying data changes second-to-second in the system of record. This data will initiallly be published on Open Data on a monthly basis. |
| Dataset Description Overview of the information this dataset contains, including overall context and definitions of key terms. This field may include links to supporting datasets, agency websites, or external resources for additional context. | This data set includes certificates of occupancy issued through the New York City Department of Buildings' DOB NOW: Certificate of Occupancy module. This module was released in March of 2021, anbd from that point onward this data set should be utilized instead of the "DOB Certificate of Occupancy" data set. The data is collected because the Department of Buildings tracks Certificates of Occupancies issued. This data include items such as job filing name, job filing label, BIN, Address, and Certificate of Occupancy status, sequence, label, and issuance date. |
| Why is this data collected? Purpose behind the collection of this data, including any legal or policy requirements for this data by NYC Executive Order, Local Law, or other policy directive. | A Certificate of Occupancy (CO) states a legal use and/or type of permitted occupancy of a building. New buildings must have a CO, and existing buildings must have a current or amended CO when there is a change in use, egress or type of occupancy. No one may legally occupy a building until the Department has issued a CO or Temporary Certificate of Occupancy (TCO).  A CO confirms that the completed work complies with all applicable laws, all paperwork has been completed, all fees owed to the Department have been paid, all relevant violations have been resolved, and all necessary approvals have been received from other City Agencies. The Department issues a final CO when the completed work matches the submitted plans for new buildings or major alterations. |
| How is this data collected? The methods used to create and update this dataset, including what cleaning or processing was involved prior to dataset publication. If data collection includes interpreting physical information this field includes technical details.  If data collection includes fielding applications, requests, or complaints, this field includes details about the forms, applications, and processes used. | It is collected through a data intake form with transactional time stamps within the DOB NOW - Certificate of Occupancy module. |
| How can this data be used? Examples of and/or links to projects or agency operations that have used this dataset. Where relevant, includes links to online projects, agency websites, visualizations, maps, or dashboards. What are some questions one might answer using this dataset? | It can be counted. It has not been used yet because it has not been published yet. The legacy system that preceded it was also not widely used in published analyses/means. |
| What are the unique characteristics or limitations of this dataset? Unique characteristics of this dataset to be aware of, specifically, constraints or limitations to the use of the data. | This data set contain any personally identifiable information, information about requests for Certificates of Occupancy, or why any of those requests would be rejected. |
| Additional geospatial information For any datasets with geospatial data, specify the coordinate reference system or projection used and other relevant details. | Address and borough information is entered and selected by the requestor if the Certiicate of Ocupancy. |

## Sheet: Column Information

| Data Dictionary - Column Information |
| Column Name | Column Description | Expected/Allowed Values | Field Limitations | Additional Notes |
| Name of the column exactly as it appears in the dataset. | A brief, plain-language explanation of what the data in the column means. | Specifies if there is an expected range and/or format of possible values. For example, if the data type is Date & Time, this field will note whether the timestamp is MM/DD/YYYY or MM/YYYY. If the Column Name is ice cream, this field might note that values can be Chocolate, Vanilla or Strawberry.  If relevant, this field specifies the unit of measurement of the data field, e.g. thousands, millions, $ value, miles, feet, year, etc. | Describes any unique characteristics or potential analytical limitations presented by this field, including:  - the reasoning for any null, zero, or empty values in the data - if the data in the column was integrated from another dataset or organization - if the data covered includes a different time period - the source of the column and how the data in the column was generated.   For example, information on how the data in this column was generated can include  whether the data was self-reported directly by a person, system generated by a database or agency system, derived through analytical manipulation of other fields or records; or obtained from a different agency. | Provides any additional relevant information about the data in the column, including:  - definitions of acronyms, special term or codes, or jargon that appears in the field values; - the meaning of confusing or non-intuitive values in the data;  - how the information in this column relates to information in other columns; - other unique details about this column. |
| Job Filing Name | The filing sequence indicator | I1, S1, P2; not G4 | Created by DOB NOW module, and should not be null | Text |
| Job Type | Overall job type for the application | Alteration CO, New Building, not A1, A2, or A3 | Created by DOB NOW module, and should not be null | Text |
| BIN | Building Identification Number assigned by Department of City Planning | 1000003, 1000016 | Created by DOB NOW module, and should not be null | Number |
| Borough | A name to indicate the NYC borough where the proposed work will take place | Manhattan, Queens; any location not in a New York City borough would be unexpected | Supplied by DOB NOW applicant, and should not be null | Number |
| House No | The house number for the building owner's address. | 123, 45, 67 | Supplied by DOB NOW applicant, and should not be null | Text |
| Street Name | The street name for the building owner's address. | Broadway, First Avenue; a street not in New York City would be unexpected | Supplied by DOB NOW applicant, and should not be null | Text |
| Block | Tax Block assigned to the location of the proposed work by the Department of Finance. | 5652, 176, 2417 | Supplied by DOB NOW applicant, and should not be null | Number |
| Lot | Tax Lot assigned to the location of the proposed work by the Department of Finance. | 67, 36, 8 | Supplied by DOB NOW applicant, and should not be null | Number |
| Zip Code | The Zip Code for the filing representative's address. | 11219, 11201, 11249 | Supplied by DOB NOW applicant, and should not be null | Number |
| Submitted Date | The date the Certificate of Ocupancy request is submitted to the Department of Buildings | 1/31/2022, 4/19/2022; dates before March 2021 would be unexpected | Created by DOB NOW module, and should not be null | Date |
| C of O Status | The status of the Certificate of Ocupancy | Certificate of Ocupancy (CO) Issued; anything else would be unexpected | Created by DOB NOW module, and should not be null | Text |
| C of O Sequence # | The nominal ordering of Certificate of Ocupancy requests in a series | 6141, 14510, 14531,15107 | Created by DOB NOW module, and should not be null | Number |
| C of O Filing Type | The type of Certificate of Ocupancy requested | Initial, Final, Renewal With Change; anything else would be unexpected | Created by DOB NOW module, and should not be null | Text |
| Community Board | NYC Community Board | 302, 312, 318; anything with a decimal point would be unexpected | Created by DOB NOW module, and should not be null | Number |
| C of O Issuance Date | The date the Certificate of Ocupancy is issued | 3/2/2022 3:11:09 PM, 2/4/2022 1:10:14 PM; dates before March 2021 would be unexpeted | Created by DOB NOW module, and should not be null | Date |
| Application Number | The Certificate of Ocupancy number | CO-000014510, CO-00004531, CO-00006141; anything not following this structure would be unexpected | Created by DOB NOW module, and should not be null | Text |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History |
| Description of all major changes to the format including what specific fields were added or removed, data calculation method, or method of collection of the data that have taken place since the initial version. Adding or updating new data values does not necessitate a new version entry. |
| Date | Change Highlights | Comments |
| 4.26.2022 | N/A | Initital Release |

## Sheet: Primer Page & InternaI Informat

| Data Dictionary - Open Data Team Internal Information |
| This section is used for internal purposes only by the Open Data Team and can be ignored by external data users.   Information shared in this section may be publicly displayed on the dataset’s primer page on NYC Open Data. |
| Dataset Tags A list of comma-separated terms, based on the topic of the dataset, that will link to other datasets with that same tag.   Tags are used along with the dataset name and description to search NYC Open Data. | dob, Certificate, occupancy, C of O |
| Are rows removed from this dataset when the data is updated? | No |
| Can this dataset be feasibly automated? | Yes |
| Is this data also present on a website maintained by or on behalf of the agency? If so, please provide the website URL. | https://a810-dobnow.nyc.gov/publish/Index.html#!/ |
| What is the update frequency of the data on the agency's website? Only applicable if the data is also present on a website maintained by or on behalf of the agency | Daily |
| Is the data on the agency's website updated automatically? Only applicable if the data is also present on a website maintained by or on behalf of the agency | Yes |

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
| To be determined | Not Applicable |
| Not Applicable |

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
| Department of Information Technology & Telecommunications (DoITT) |
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
