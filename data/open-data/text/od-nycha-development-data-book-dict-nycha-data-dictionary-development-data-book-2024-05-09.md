# Data dictionary: od-nycha-development-data-book-dict-nycha-data-dictionary-development-data-book-2024-05-09.xlsx

Source: https://data.cityofnewyork.us/d/evjd-dqpz
Extracted from: od-nycha-development-data-book-dict-nycha-data-dictionary-development-data-book-2024-05-09.xlsx

## Sheet: Dataset Information

| Data Dictionary - Dataset Information |
| Dataset Name | NYCHA Development Data Book |
| Dataset URL | https://data.cityofnewyork.us/Housing-Development/NYCHA-Development-Data-Book/evjd-dqpz |
| Data Provided by The name of the NYC agency providing this data to the public. | New York City Housing Authority (NYCHA) |
| Each row is a...  The unit of analysis/level of aggregation of the dataset | NYCHA development. |
| Publishing Frequency How often changed data is published to this dataset. For an automatically updated dataset, this is the frequency of that automation | As needed |
| Data Change Frequency How often the data underlying this dataset is changed | As needed |
| Frequency Details Additional details about the publishing or data change frequency, if needed |
| Dataset Description Overview of the information this dataset contains, including overall context and definitions of key terms. This field may include links to supporting datasets, agency websites, or external resources for additional context. | Contains the main body of the "Development Data Book". The Development Data Book lists all of the Authority's Developments alphabetically and includes information on the development identification numbers, program and construction type, number of apartments and rental rooms, population, number of buildings and stories, street boundaries, and political districts. |
| Why is this data collected? Purpose behind the collection of this data, including any legal or policy requirements for this data by NYC Executive Order, Local Law, or other policy directive. |
| How is this data collected? The methods used to create and update this dataset, including what cleaning or processing was involved prior to dataset publication. If data collection includes interpreting physical information this field includes technical details.  If data collection includes fielding applications, requests, or complaints, this field includes details about the forms, applications, and processes used. |
| How can this data be used? Examples of and/or links to projects or agency operations that have used this dataset. Where relevant, includes links to online projects, agency websites, visualizations, maps, or dashboards. What are some questions one might answer using this dataset? |
| What are the unique characteristics or limitations of this dataset? Unique characteristics of this dataset to be aware of, specifically, constraints or limitations to the use of the data. |
| Additional geospatial information For any datasets with geospatial data, specify the coordinate reference system or projection used and other relevant details. |

## Sheet: Column Information

| Data Dictionary - Column Information |
| Column Name | Column Description | Expected/Allowed Values | Field Limitations | Additional Notes |
| DATA AS OF |
| DEVELOPMENT | Development name. |
| HUD AMP# | Asset Management Project (AMP) numbers. |
| TDS# | The number used by numerous computer applications to identify NYCHA Developments. |
| CONSOLIDATED TDS# | Consolidated Tenant Data Systems number. |
| DEVELOPMENT EDP# | Assigned to a development during the development (construction) period. |
| OPERATING EDP# | A number that each development utilize for Operating Costs. |
| HUD # | The U.S. Department of Housing and Urban Development (HUD) identification number. |
| PROGRAM | The Programs designations are: Federal, MHOP, Mixed Finance, Mixed Finance/LLC1, Mixed Finance LLC2, Mixed Finance/Non-NYCHA Development. |
| METHOD | Two items in this field Conventional and Turnkey. |
| TYPE | 5 items in this field: Gut Rehab, New Const, New Const (Eld), Rehab, and Rehab (Eld). |
| NUMBER OF SECTION 8 TRANSITION APARTMENTS | The total number of apartments transitioned to the Section 8 Program in the LLC1 developments. |
| NUMBER OF CURRENT APARTMENTS | The number of units available for occupancy in the development as per the January 1, 2024 Dwelling Unit Inventory which is used to track the number of units on the rent roll. |
| TOTAL NUMBER OF APARTMENTS | The total number of apartments at the development including the Section 8 Transition apartments at the LLC1 developments. |
| NUMBER OF RENTAL ROOMS | Rental room count per unit is equal to 2 1/2 plus the number of bedrooms. The number of rental rooms includes balconies and half-bath as half-rooms. |
| AVG NO R/R PER APARTMENT | The average number of rental rooms per apartment is the number of rental rooms divided by the number of current units. The Section 8 units in the LLC1 Developments are included. |
| POPULATION SECTION 8 TRANSITION | The number of persons living in the Section 8 Transition units in the LLC1 developments. |
| POPULATION PUBLIC HOUSING | The number of persons living in all public housing units. The residents living in the Section 8 Transition units in the LLC1 developments are not included in this population count. |
| TOTAL POPULATION | The total number of persons living at the developments, including the Section 8 Transition apartments in the LLC1 developments. |
| TOTAL # OF FIXED INCOME HOUSEHOLDS | Number of households on fixed income (households with income from Social Security, Supplementary Security Income (SSI), Survivors Insurance, Veterans Benefits, or Pension (as well as other Public or Non Public Benefits), while not earning employment income or receiving Public Assistance. |
| PERCENT FIXED INCOME HOUSEHOLDS | Number of households on fixed income divided by the total number of households. |
| NUMBER OF RESIDENTIAL BLDGS | The number of residential buildings on the grounds that are used for dwelling units. |
| NUMBER OF NON-RESIDENTIAL BLDGS | The number of non-residential buildings at a development. |
| NUMBER OF STAIRHALLS | The number of individual entrances in each development. |
| NUMBER OF STORIES | The number of floors in each building. |
| TOTAL AREA SQ FT | This number includes land acquired and developed as part of the development for a park or playground to be operated and manintained by the NYC Department of Parks. At State and City Developments, the park or playground is owned by the City of New York. At federal Developments, parks and playgrounds are leased to the City. |
| ACRES | The land area of the development including buildings and grounds is shown in acres (one acre equals 43,560 square feet). |
| NET DEV AREA SQ FT | This is Square Feet at a Development less the land set aside for a park or playground. For the majority of developments this figure is the same acreage. |
| EXCLUDING PARK ACRES | This is the number of acres at a development less the land set aside for a park or playground. For the majority of developments this figure is the same as "acres". |
| BLDG COVERAGE SQ FT | The total ground floor area of the building footprints of a development. |
| CUBAGE CU FT | Cubic Space (height x length x width of residential buildings) in all the buildings at a development, expressed as cubic feet. |
| BLDG COVERAGE % | This is the building coverage, divided by a development’s total area in square feet. This figure is presented as a percentage. |
| DENSITY | Measure of development density as represented by the number of persons per acre. |
| DEVELOPMENT COST | The sum of the land cost, construction cost and site improvement cost, including fees for architects and engineers at the time of original construction. |
| PER RENTAL ROOM | Cost to develop the property divided by the number of rental rooms at the time of original construction. |
| AVG MONTHLY GROSS RENT | This is the average gross monthly rent of the households in each development. The average tenant share of rent for the Section 8 households in the LLC1 developments is included. |
| LOCATION STREET A | For NYCHA Developments that fit into a relatively neat rectangular block or two, these fields should be the four border streets (north, south, east, and west) of the Development. For Developments that are spread over some distance such as West Farms Road Rehab, the streets that best define the location of the development are provided. |
| LOCATION STREET B |
| LOCATION STREET C |
| LOCATION STREET D |
| BOROUGH | Bronx, Brooklyn, Manhattan, Queens, or Staten Island. |
| COMMUNITY DISTIRCT | Community District Number. |
| US CONGRESSIONAL DISTRICT | Congressional District Number. |
| NY STATE SENATE DISTRICT | New York State Senate District Number. |
| NY STATE ASSEMBLY DISTRICT | New York State Assembly District Number. |
| NY CITY COUNCIL DISTRICT | New York City Council District Number. |
| COMPLETION DATE | The Initial Occupancy Completion Date: The date when the development was at least 95% occupied. |
| FEDERALIZED DEVELOPMENT | Date on which City and / or State Developments were transferred to the Federal Program. There are 11 items in this field. They are: 1968/08/29-Fed Tran; 1971/06/29-Fed Tran; 1972/06/29-Fed Tran; 1977/07/01-ATP 1 (abbreviation for Authority Transfer Program); 1978/02/01-ATP 2; 1978/07/01-ATP 3; 1979/08/01-ATP 4; 1980/07/01-ATP 5; 1980/10/01-ATP 7; and 1995/07/13-PTA (abbreviation for Physical Transfer of Assets). |
| SENIOR DEVELOPMENT | A senior development where all residents are senior, aged 62 or older, is denoted as "Exclusively". A development where only some buildings are designated for senior residents is denoted as "Partially". |
| ELECTRICITY PAID BY RESIDENTS | A "Yes" indicates developments where residents pay for their electricity. |
| PRIVATE MANAGEMENT | A "Yes" indicates developments managed by a private management company. |
| RAD TRANSFERRED DATE | The date when the development underwent a Rental Assistance (RAD) / Permanent Affordability Commitment Together (PACT) conversion. |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History |
| Description of all major changes to the format including what specific fields were added or removed, data calculation method, or method of collection of the data that have taken place since the initial version. Adding or updating new data values does not necessitate a new version entry. |
| Date | Change Highlights | Comments |
| 2013-03-29 00:00:00 | Creation of dataset |

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
