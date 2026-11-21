# Data dictionary: od-hpd-registrations-dict-hpd-registration-open-data.pdf

Source: https://data.cityofnewyork.us/d/tesw-yqqr
Extracted from: od-hpd-registrations-dict-hpd-registration-open-data.pdf

## Page 1

HPD Open Data 
Registrations 
 
Pursuant to New York City’s Housing Maintenance Code, the Department of Housing 
Preservation and Development (HPD) collects registration information from owners of 
residential rental units. Owners are required to register if they own residential buildings 
with three or more units or if they own one- or two-family homes and neither they nor 
members of their immediate family live there. Registrations are required upon taking 
ownership of a qualifying building, and once a year thereafter. 
 
The registration information in this file is updated quarterly, normally as of April 30, July 
31, October 30 and January 31. Each file will contain the information from the last valid 
registration at the time of the file posting. A valid registration is one in which all of the 
appropriate data is supplied. Each registration will also display an expiration date. If the 
expiration date has passed, the property registration is not current. The law requires 
HPD to mail Notices of Violation to the owner using the last valid registration, even if 
that property registration is not current. A property registration must be valid and current 
for the property to be in compliance with the law. In order to determine which 
registration in a previous file may be replaced by a registration in a new file, the building 
being registered is uniquely identified by an XML element called BuildingID (full XML 
path: //RegistrationOpenData/Registrations/Registration/BuildingID). Use this value to 
link new registrations with any history you are maintaining in your own datastore. 
 
Starting with the September, 2012 release a registration may apply to more than one 
building (so-called Garden Complexes). In such cases, there will be more than one 
Registration element with the same RegistrationID. However, each such element will 
have a different BuildingID and other building-specific information, such as address, 
BBL and BIN. 
 
Data Dictionary 
 
The Registration information is structured as XML. Schema files defining the XML 
format are included in the zip package containing this file. The root schema file is called 
“services.hpd.gov.xsd”. The XML structure is pretty simple, containing the following 
major elements 
 
RegistrationOpenData 
 
Description – a brief description of the data set 
            InformationURL – an url where related information can be found 
            SourceAgency – the agency providing the data (HPD) 
            SourceSystem – the agency’s system for managing the data 
            StartDate – the start date of the period covered by the file 
            EndDate – the end date of the period covered by the file 


## Page 2

 
Registrations 
 
 
Registration (one or more) 
 
 
 
<multiple elements; see below> 
 
 
 
Contacts 
 
 
 
 
RegistrationContact (one or more) 
 
 
 
 
 
<multiple elements; see below> 
 
The RegistrationOpenData element is the root element and contains some descriptive 
elements as well as the Registrations collection, which contains Registration elements. 
Each Registration element contains elements about the building and the registration, as 
well as the Contacts collection, which contains RegistrationContact elements. Each 
RegistrationContact element contains elements about a person or organization identified 
on the registration form. 
 
RegistrationOpenData Element 
 
Element Name 
Data Type 
Description 
Description 
string 
a brief description of the data set 
InformationURL 
string 
a url where related information can be found 
SourceAgency 
string 
the agency providing the data (HPD) 
SourceSystem 
string 
the agency’s system for managing the data 
StartDate 
dateTime 
the start date of the period covered by the file 
EndDate 
dateTime 
the end date of the period covered by the file 
 
Registration Element 
 
Element Name 
Data Type 
Description 
RegistrationID 
long 
Unique identifier of Registration 
BuildingID 
long 
Unique identifier of building being 
registered 
Boro 
LookupValue 
Address information for the registered 
building (see below for Boro) 
HouseNumber 
string 
LowHouseNumber 
string 
HighHouseNumber 
string 
StreetName 
string 
StreetCode 
long 
Zip 
string 
Block 
int 
Tax block for building 
Lot 
int 
Tax lot for building 
BIN 
int 
DCP Building Identification Number for 
building 
CommunityBoard 
int 
Community Board for building 
LastRegistrationDate dateTime 
Date on which the  registration 


## Page 3

information was processed 
RegistrationEndDate dateTime 
Expiration date of registration record 
Contacts 
Array of 
RegistrationContacts 
Registered people and organizations 
 
 
Boro LookupValue Element 
 
Element Name 
Data Type 
Description 
GroupName 
string 
“Boro” 
SeqNo 
long 
Boro code (1 = Manhattan, 2 = Bronx, 3 = Brooklyn, 4 
= Queens, 5 = Staten Island) 
ShortName 
string 
“MN”, “BX”, “BK”, “QN”, “SI” 
LongName 
string 
“Manhattan”, “Bronx”, “Brooklyn”, “Queens, “Staten 
Island” 
Order 
int 
Not applicable 
 
 
RegistrationContact Element 
 
Element Name 
Data Type 
Description 
RegistrationContactI 
long 
Unique identifier of 
RegistrationContact 
RegistrationID 
long 
Unique identifier of owning 
Registration 
Type 
RegistrationContactType "Individual Owner", 
"Corporate Owner", 
"Managing Agent", 
"Head Officer", 
"Officer", 
"Shareholder" 
ContactDescription 
string 
Description of contact 
CorporationName 
string 
If applicable 
Title 
string 
Contact person information 
FirstName 
string 
MiddleInitial 
string 
LastName 
string 
BusinessHouseNumber string 
Contact address information 
BusinessStreetName 
string 
BusinessApartment 
string 
BusinessCity 
string 
BusinessState 
string 
BusinessZip 
string 


## Page 4

 

