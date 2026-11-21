# Data dictionary: od-dob-now-permits-dict-dob-now-build-approved-permits-data-dictionary.xlsx

Source: https://data.cityofnewyork.us/d/rbx6-tga4
Extracted from: od-dob-now-permits-dict-dob-now-build-approved-permits-data-dictionary.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | DOB NOW: Build – Approved Permits |
| Agency Name | Department of Buildings (DOB) |
| Update Frequency | Daily |
| Dataset Description | List of all approved construction permits in DOB NOW except for Electrical, Elevator, and Limited Alteration Application (LAA) which have their own datasets |
| Dataset Keywords | dob, buildings, permits, construction |
| Dataset Category | Housing & Development |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the idiosyncrasies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) | Data Type (Plain Text, Number, Date) | Required |
| Job Filing Number | The DOB Job Filing Number assigned when the applicant begins the application. | This is the unique identifier for the filing submitted through DOB NOW.   The first character is a letter representing the NYC Borough where the building is located. (B=Brooklyn, M=Manhattan, Q=Queens, S=Staten Island, X=Bronx)  The next 8 characters are numbers that make the Job Filing Number unique.  The last three characters are a dash, a letter, and a number. The letter is either I=Initial, P=Post Approval Amendment, or S=Subsequent. The number indicates the sequence of the filing when you can have multiple of that type. You should always have I1 because there can only be one initial filing. But you can have multiple Subsequent filings, and the number indicates the order in which they were filed.   Note: A Post Approval Amendment is filed to indicate a change in the application and/or plans after they have already been approved by the Department of Buildings. |
| Filing Reason | The reason the permit was applied for. | Expected values include: Initial Permit No Work Permit Renewal Permit Without Changes |
| House No | The house number for the building where the proposed work will take place. | In the address, "280 Broadway", 280 is the house number. This number may contain a dash (-), as in "8-15 27 Avenue". |
| Street Name | The street name for the building where the proposed work will take place. | In the address, "1050 Park Place", Park Place is the street name. |
| Borough | The name of the NYC borough where the proposed work will take place. | Expected values = MANHATTAN, BRONX, BROOKLYN, QUEENS, STATEN ISLAND. |
| LOT | Tax Lot assigned to the location of the proposed work by the Department of Finance. |
| Bin | Building Identification Number assigned by Department of City Planning. | This BIN comes from the DOB database. |
| Block | Tax Block assigned to the location of the proposed work by the Department of Finance. |
| C B NO | Community Board Number for the building’s address. |
| Apt/Condo No(s) | The apartment number for the location where the proposed work will take place if the work is restricted to only certain apartments or condos within the building. |
| Work on Floor | The name or number of the floor(s) of the building where the work will be performed. |
| Work Type | The type of work that will be performed under this permit. | Expected values include, but are not limited to: • Antenna - An antenna is a device that transfers electrical signals across air or wires and can receive, transmit, or broadcast signals to a singular or multiple locations.  • Construction Fence - A fence that encloses the construction work and protects the site.  • Curb Cut - An angled drop cut to the curb in the roadway, street, public right of way, or similar, which provides access to the zoning or tax lot. • Plumbing - The installation, maintenance, extension, and alteration of all piping, fixtures, appliances, and equipment in connection with: sanitary drainage, storm drainage facilities, the venting system and the public or private water supply system. • Sidewalk Shed - A sidewalk shed protects pedestrians from potential debris when construction work on higher floors occurs above the sidewalk. • Sign - To install a sign, a construction permit is required from the Department. Signs that are painted or smaller than six square feet and not illuminated do not require a permit.  • Sprinkler - The installation, modification, repair, or removal of the system of piping and sprinkler heads connected to one or more sources of water supply. • Standpipe -  Installation and/or modifications to piping installed for Standpipe system in a building or structure that serves to transfer water from a water supply to hose connections at one or more locations in a building or structure for fire-fighting purposes. • Supported Scaffold - Scaffold is a temporary elevated platform, including its supporting structure, erected at a construction site during construction to support workers and/or materials and providing aboveground access to the building’s exterior. |
| Permittee's License Type | The type of professional license that the person applying for the permit holds. | Expected values include, but are not limited to: F =  GC = General Contractor P =  PE = Professional Engineer RA = Registered Architect S = Sign Hanger PR = Preparer  (This is not actually a license type. It is the default if someone does not connect a license type to their DOB NOW account.) |
| Applicant License # | The applicant's license number on file with the Department. |
| Applicant First Name | First name of the person who filed the application. |
| Applicant Middle Name | Middle name of the person who filed the application. |
| Applicant Last Name | Last name of the person who filed the application. |
| Applicant Business Name | The business name of the applicant. |
| Applicant Business Address | The business address for the applicant. |
| Filing Representative First Name | First name of the filing representative, if any. A filing representative is someone who fills out Department of Buildings paperwork on behalf of a building owner or licensed professional. |
| Filing Representative Middle Initial | Middle initial of the name of the person who filed the application. |
| Filing Representative Last Name | Last name of the person who filed the application. |
| Filing Representative Business Name | The business name of the filing representative. |
| Work Permit | The DOB Permit Number assigned to this permit. | This is the unique identifier for the permit assigned by DOB NOW.   The first character is a letter representing the NYC Borough where the building is located. (B=Brooklyn, M=Manhattan, Q=Queens, S=Staten Island, X=Bronx)  The next 8 characters are numbers that make the Permit Number unique.  The next three characters are a dash, a letter, and a number. The letter is either EW=, I=Initial, P=Post Approval Amendment, or S=Subsequent. The number indicates the sequence of the filing when you can have multiple of that type. You should always have I1 because there can only be one initial filing. But you can have multiple Subsequent filings, and the number indicates the order in which they were filed.   Note: A Post Approval Amendment is filed to indicate a change in the application and/or plans after they have already been approved by the Department of Buildings.  The last two characters indicate the type of work that the permit covers: AN = Antenna CC = Curb Cut FN = Fence PL = Plumbing SD = Standpipe SF = Scaffold SG = Sign SH = Shed SP = Sprinkler |
| Approved Date | This is the date that the entire job was approved by the Plan Examiner. The applicant can now pull a permit. |
| Issued Date | This is the date that the permit was issued. |
| Expired Date | This is the date that the permit expires. |
| Job Description | The general description of the work being applied for. This field is free text, and is filled out by the applicant. |
| Estimated Job Costs | This is a dollar amount that indicates the applicant's estimate for how much the job will cost. |
| Owner Business Name | The business name of the building owner. |
| Owner Name | The name of the building owner. |
| Owner Street Address | The street name for the building owner's address. |
| Owner City | The city for the building owner's address. |
| Owner State | The state for the building owner's address. |
| Owner Zip Code | The Zip Code for the building owner's address. |
| Permit Status | The most recent status of the permit |
| Tracking Number | Unique identifier of the permit |
| Sequence Number | The numeric order of permit issuance |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
| 1 | 2018-06-29 00:00:00 | Migrated DD to standard template |
|  |  | Added columns Permit Status, Tracking Number, Sequence Number |

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
