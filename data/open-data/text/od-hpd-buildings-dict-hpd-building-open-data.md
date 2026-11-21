# Data dictionary: od-hpd-buildings-dict-hpd-building-open-data.pdf

Source: https://data.cityofnewyork.us/d/kj4p-ruqc
Extracted from: od-hpd-buildings-dict-hpd-building-open-data.pdf

## Page 1

HPD Open Data 
Buildings 
 
Pursuant to New York City’s Housing Maintenance Code, the Department of Housing 
Preservation and Development (HPD) collects information on multiple dwellings in New York 
City, and other buildings that fall under its jurisdiction. HPD’s Buildings Open Data covers all 
buildings which meet any of the following criteria: 
 
a. HPD has required the owner to register the building under the Housing Maintenance 
Code (HMC) 
b. HPD has initiated a litigation action under the HMC 
c. HPD has received a complaint for the building 
d. HPD has initiated a work order for the purposes of emergency repair, demolition, or 
the Alternative Enforcement Program (AEP) for the building 
e. HPD has added the property to the AEP program 
 
This building information in this file will be updated monthly. The first file is being published in 
March 2013. 
 
A change was implemented starting with the file available on August 1, 2014. The format of the 
pipe-delimited files was changed to include the numeric value assigned to LookupValue 
elements. For more details, see the description of the pipe-delimited files at the end of this 
document. 
 
Buildings are identified by a BuildingID. 
 
Data Dictionary 
 
The Building information is provided in two formats: XML and pipe-delimited values text.  
XML File Format 
The XML file is named Buildingsyyyymmdd.xml, where the date indicates the last day of the 
quarter covered by the file. Schema files defining the XML format are included in the zip 
package containing this file. The root schema file is called “services.hpd.gov.xsd”. The XML 
structure is pretty simple, containing the following major elements 
 
BuildingOpenData 
 
Description – a brief description of the data set 
            InformationURL – an url where related information can be found 
            SourceAgency – the agency providing the data (HPD) 
            SourceSystem – the agency’s system for managing the data 
            StartDate – the last day of the quarter covered by the file 
            EndDate – empty 


## Page 2

 
Buildings 
 
 
Building (one or more) 
 
 
 
<multiple elements; see below> 
 
 
 
The BuildingOpenData element is the root element and contains some descriptive elements as 
well as the Buildings collection, which contains Building elements. Each Building element 
contains elements about the building. 
 
BuildingOpenData Element 
 
Element Name 
Data Type 
Description 
Description 
String 
a brief description of the data set 
InformationURL 
String 
a URL where related information can be found 
SourceAgency 
String 
the agency providing the data (HPD) 
SourceSystem 
String 
the agency’s system for managing the data 
StartDate 
dateTime 
the date the file was generated 
EndDate 
dateTime 
empty 
 
Building Element 
 
Element Name 
Data Type 
Description 
BuildingID        
long        
Unique identifier of building 
Boro              
LookupValue 
Address information for the building (see 
below for Boro) 
HouseNumber       
String      
LowHouseNumber    
String      
HighHouseNumber   
String      
StreetName        
String      
Zip               
String      
Block             
int         
Tax block for building 
Lot               
int         
Tax lot for building 
BIN               
long        
DCP Building Identification Number for 
building                                                              
CommunityBoard    
long        
Unique number identifying a Community 
District/Board, which is a political 
geographical area within a borough of the 
City of NY                                                         
CensusTract       
String      
Geographic area defined by the U.S. Census 
Bureau for the various decennial censuses        
ManagementProgram 
String      
Contains the current active management 
program which determines who is 
responsible for the management of this 
building                                                              


## Page 3

DoBBuildingClass  
LookupValue 
Stores DoB building classification codes as 
augmented by HPD for other than Multiple 
Dwellings (see DoBBuildingClass below)        
LegalStories      
int         
Number of legal stories in building                   
LegalClassA       
int         
The number of apartments in a multiple 
dwelling                                                             
LegalClassB       
int         
The number of rooms in a multiple dwelling 
without individual baths and kitchens  
RegistrationID    
long        
Multiple dwelling registration number, used 
by HPD in the master building file to identify 
a building                                                           
LifeCycle         
BuildingLifeC
ycle enum 
The stage in the building life cycle (see 
BuildingLifeCycle below)                                 
RecordStatus      
LookupValue 
The numeric value of the status of this 
building (see REC_STTS below)                      
 
 
Boro LookupValue Element 
 
Element Name 
Data Type 
Description 
GroupName 
String 
“Boro” 
SeqNo 
Long 
Boro code (1 = Manhattan, 2 = Bronx, 3 = Brooklyn, 4 
= Queens, 5 = Staten Island) 
ShortName 
String 
“MN”, “BX”, “BK”, “QN”, “SI” 
LongName 
String 
“Manhattan”, “Bronx”, “Brooklyn”, “Queens, “Staten 
Island” 
Order 
Int 
Not applicable 
 
DoBBuildingClass LookupValue Element 
 
Element Name 
Data Type 
Description 
GroupName 
String 
“DoBBuildingClass” 
SeqNo 
Long 
Building Class code 
ShortName 
String 
Building class abbreviated name 
LongName 
String 
Building class full name 
Order 
Int 
Not applicable 
 
REC_STTS LookupValue Element 
 
Element Name 
Data Type 
Description 
GroupName 
String 
“REC_STTS” 
SeqNo 
Long 
code (1 = Active, 2 = Inactive, 3 = Pending 


## Page 4

ShortName 
String 
“Active”, “Inactive”, “Pending” 
LongName 
String 
“Active”, “Inactive”, “Pending” 
Order 
Int 
Not applicable 
 
BuildingLifeCycle Enum 
 
Land 
Planned 
Building 
Demolished 
Under Construction 
 
Pipe-Delimited Values File Format 
The pipe-delimited values text file is named Buildingsyyyymmdd.txt, where the date indicates 
the last day of the quarter covered by the file. The pipe-delimited values text file contains as 
columns the elements of the Building element listed above. The only difference in the column 
contents is that for elements defined as LookupValues, only the numeric value (starting with the 
August 1, 2014 release) and the long name appear in the file. The first record in each file has the 
column headers. For elements defined as LookupValues there will be two columns. The first 
contains the numeric value (SeqNo in the XML file); its column header is the element name 
concatenated with “ID”. The second contains the long name; its column header is the element 
name. Note that the BuildingOpenData element does NOT appear in the pipe-delimited values 
text file. 
 

