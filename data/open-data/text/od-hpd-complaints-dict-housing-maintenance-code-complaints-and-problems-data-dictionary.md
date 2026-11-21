# Data dictionary: od-hpd-complaints-dict-housing-maintenance-code-complaints-and-problems-data-dictionary.xlsx

Source: https://data.cityofnewyork.us/d/ygpa-z7cr
Extracted from: od-hpd-complaints-dict-housing-maintenance-code-complaints-and-problems-data-dictionary.xlsx

## Sheet: Dataset Information

| Data Dictionary - Dataset Information |
| Dataset Name | Housing Maintenance Code Complaints and Problems |
| Dataset URL | https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Complaints-and-Problems/ygpa-z7cr |
| Data Provided by The name of the NYC agency providing this data to the public. | Department of Housing Preservation & Development (HPD) |
| Each row is a...  The unit of analysis/level of aggregation of the dataset | problems reported by the complainant. |
| Publishing Frequency How often changed data is published to this dataset. For an automatically updated dataset, this is the frequency of that automation | Daily |
| Data Change Frequency How often the data underlying this dataset is changed | Daily |
| Frequency Details Additional details about the publishing or data change frequency, if needed |
| Dataset Description Overview of the information this dataset contains, including overall context and definitions of key terms. This field may include links to supporting datasets, agency websites, or external resources for additional context. | The Department of Housing Preservation and Development (HPD) records complaints that are made by the public for conditions which violate the New York City Housing Maintenance Code (HMC) or the New York State Multiple Dwelling Law (MDL). |
| Why is this data collected? Purpose behind the collection of this data, including any legal or policy requirements for this data by NYC Executive Order, Local Law, or other policy directive. | This data is collected to allow the public to more easily identify complaints and complaint problems that have been issued in their buildings. |
| How is this data collected? The methods used to create and update this dataset, including what cleaning or processing was involved prior to dataset publication. If data collection includes interpreting physical information this field includes technical details.  If data collection includes fielding applications, requests, or complaints, this field includes details about the forms, applications, and processes used. | The data is collected by 311 and the Department of Housing Preservation and Development. HPD records complaints that are made by the public through the 311 Citizen Services Center, Code Enforcement Borough Offices or the internet. |
| How can this data be used? Examples of and/or links to projects or agency operations that have used this dataset. Where relevant, includes links to online projects, agency websites, visualizations, maps, or dashboards. What are some questions one might answer using this dataset? | For more information please see the 'About Code Enforcement' page on the NYC Housing Preservation & Development website: https://www.nyc.gov/site/hpd/services-and-information/code-enforcement.page. |
| What are the unique characteristics or limitations of this dataset? Unique characteristics of this dataset to be aware of, specifically, constraints or limitations to the use of the data. | Unique keys that link back to the to the open dataset '311 Service Requests from 2010 to Present' are include if applicable. Problems are closed if a tenant verifies that the condition was corrected or an inspection result is entered by an HPD inspector. A complaint is closed when all associated problems are closed. |
| Additional geospatial information For any datasets with geospatial data, specify the coordinate reference system or projection used and other relevant details. | Geographic indicators including (Latitude, Longitude, Council District, Census Tract, BIN, BBL and NTA may not be populated for certain buildings if geographic indicators are not found for the address. |

## Sheet: Column Information

| Data Dictionary - Column Information |
| Column Name | Column Description | Expected/Allowed Values | Field Limitations | Additional Notes |
| Name of the column exactly as it appears in the dataset. | A brief, plain-language explanation of what the data in the column means. | Specifies if there is an expected range and/or format of possible values. For example, if the data type is Date & Time, this field will note whether the timestamp is MM/DD/YYYY or MM/YYYY. If the Column Name is ice cream, this field might note that values can be Chocolate, Vanilla or Strawberry.  If relevant, this field specifies the unit of measurement of the data field, e.g. thousands, millions, $ value, miles, feet, year, etc. | Describes any unique characteristics or potential analytical limitations presented by this field, including:  - the reasoning for any null, zero, or empty values in the data - if the data in the column was integrated from another dataset or organization - if the data covered includes a different time period - the source of the column and how the data in the column was generated.   For example, information on how the data in this column was generated can include  whether the data was self-reported directly by a person, system generated by a database or agency system, derived through analytical manipulation of other fields or records; or obtained from a different agency. | Provides any additional relevant information about the data in the column, including:  - definitions of acronyms, special term or codes, or jargon that appears in the field values; - the meaning of confusing or non-intuitive values in the data;  - how the information in this column relates to information in other columns; - other unique details about this column. |
| ReceivedDate | Date when the complaint was received |
| ProblemID | Unique identifier of this problem |
| ComplaintID | Unique identifier of the complaint this problem is associated with |
| BuildingID | Unique identifier given to a building record |
| Borough | Complaint borough | Manhattan, Bronx, Brooklyn, Queens, Staten Island |
| HouseNumber | Complaint house number |
| StreetName | Complaint street name |
| Zip | Complaint zip code |
| Block | Number assigned by the NYC Dept of Finance identifying the tax block the lot is on |
| Lot | Unique number assigned by the NYC Dept of Finance within a Block identifying a lot |
| Apartment | Number of the unit or apartment in a building |
| CommunityBoard | Unique number identifying a Community District/Board, which is a political geographical area within a borough of the City of NY | 1-18 |
| UnitType | Type of space where the problem was reported | Apartment, Building, Building-Wide, Public area |
| SpaceType | Type of space where the problem was reported |
| Type | Code indicating the problem type | Emergency, Hazardous, Immediate Emergency, Non emergency |
| MajorCategory | The major category of the problem |
| MinorCategory | The minor category of the problem |
| ProblemCode | The problem code |
| ComplaintStatus | The status of the complaint | Close, Open |
| ComplaintStatusDate | Date when the complaint status was updated |
| ProblemStatus | The status of the problem | Close, Open |
| ProblemStatusDate | Date when the problem status was updated |
| StatusDescription | Status description |
| ProblemDuplicateFlag | Dupliate complaint Indicator | N, Y |
| ComplaintAnonymousFlag | Anonymous complaint Indicator | N, Y |
| Unique Key | Unique identifier of a Service Request (SR) in the open data set. Links to the to the open dataset '311 Service Requests from 2010 to Present' |  |  | The 311 dataset is found at https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9 |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History |
| Description of all major changes to the format including what specific fields were added or removed, data calculation method, or method of collection of the data that have taken place since the initial version. Adding or updating new data values does not necessitate a new version entry. |
| Date | Change Highlights | Comments |
| 2023-08-07 00:00:00 | Creation of dataset |

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
