# Data dictionary: od-hpd-litigations-dict-housing-litigations-data-dictionary.pdf

Source: https://data.cityofnewyork.us/d/59kj-x8nc
Extracted from: od-hpd-litigations-dict-housing-litigations-data-dictionary.pdf

## Page 1

HPD Housing Litigation Division Open Data 
 
The Department of Housing Preservation and Development (HPD) Housing Litigation Division 
(HLD) initiates’ actions in the Housing Court against owners of privately-owned buildings to enforce 
compliance with the housing quality standards contained in the New York State Multiple Dwelling 
Law and the New York City Housing Maintenance Code. HLD attorneys also represent HPD when 
tenants initiate actions against private owners. HPD is automatically named as party to such actions. 
The goal of these court proceedings is to obtain enforceable Orders to Correct, Civil Penalties (fines) 
and Contempt Sanctions, compelling owners to comply with the Housing Maintenance Code.  
 
Under local law, the owner of a single room occupancy multiple dwelling must obtain a 
"Certification of No Harassment" from HPD before applying to DOB for a permit to demolish or 
reconfigure the building. This process is intended to ensure that the owner did not further its 
proposed demolition or construction project by harassing tenants into leaving. HLD investigates to 
determine whether harassment occurred during the statutory review period. If HPD determines that 
there is reasonable cause to believe that harassment occurred, an OATH hearing is held at which 
HLD presents the City's case. A finding of harassment prevents the owner from obtaining a 
demolition or alteration permit for three years. HPD also performs this function for the Special 
Zoning Districts which are subject to a similar provision (though not limited to SROs), under the 
Zoning Resolution. These districts are currently Clinton, Hudson Yards, West Chelsea and 
Greenpoint-Williamsburg.  
 
The Judgment Enforcement Unit (JEU) enforces the money judgments obtained by HLD in the 
actions to enforce the Housing Maintenance Code.  
 
This file contains:  
1. All cases commenced by HPD or by tenants (naming HPD as a party) in the Housing Part of New 
York City Civil Court since August 2006 seeking orders directing landlords of residential property to 
correct violations or to comply with the requirements of the Housing Maintenance Code and/or 
awarding HPD civil penalties.  
2. All cases commenced by HPD in the Housing Part of New York City Civil Court since August 
2006 seeking the appointment of an administrator pursuant to Article 7A of the Real Property 
Actions and Proceedings Law.  
3. All applications filed with HPD since August 2006 seeking a certification of no harassment.  
 
 
Some cases and applications filed before August 2006 are also noted. The decision date reflects 
the date of the last decision made in the matter. There may be other earlier relevant decisions.  
 
The information contained in the file will be updated on a monthly basis with a replacement of the 
dataset. 
 
 


## Page 2

Data Dictionary 
 
Column Name 
Column Description 
Litigation ID 
Unique number identifying the case 
Building ID 
Unique identifier of the building 
Boro ID 
A code between 1 and 5 denoting borough value below 
Boro 
A borough is one of five administrative divisions in New York City 
House Number 
The house number in the address of a building 
Street Name 
The street name is a component of the address of a building 
Zip 
The zip field is the ZIP code where the entity is located 
Block 
The block is the NYC Department of Finance (DOF) defined tax 
block of the building 
Lot 
The Lot is used by the NYC Department of Finance to uniquely 
identify a non-overlapping subdivision of a block. Tax Block 
Numbers and Tax Lot Numbers are used to define an area of 
commonality for the purposes of paying taxes. All structures have a 
block and lot number. 
Case Type 
See the descriptions of the case type data below 
Case Open Date 
The date that the case was filed with the Court. 
Case Status 
The current position of the Case. 
Open Judgment 
A “Y” indicates that civil penalties are owed to HPD after the Court 
issued a judgment against the owners of a building awarding civil 
penalties to HPD.
Finding of Harassment 
After Inquest: Judgments entered for an order and/or civil penalties 
upon default where there was no appearance in Court by the named 
respondent(s). If any of these judgments are vacated by the Court, 
they will be removed from this list. 
After Trial: Judgments awarded by the Court at the conclusion of 
trial at which evidence was presented. 
Finding Date 
The date that the decision was made by the Court. 
Penalty 
The penalty awarded by the Court in the case when harassment is 
found. This amount includes all penalties, including harassment 
penalties. 
Respondent Name/Organization The party or parties against whom a case has been commenced. The 
respondent was not necessarily the owner at the time of the case 
and, even if so, may no longer be the owner of the property at the 
time this report is generated. 
 
 
The following are the descriptions of the case type data contained in this file: 
 
 
Value 
Description 
Tenant Action  
Cases commenced by one or more residential tenants against their 
landlords (and naming HPD as a party) seeking an order to correct 


## Page 3

violations and civil penalties for failure to timely correct 
violations.  
Comprehensive  
Cases in which HPD seeks the correction of all outstanding 
violations in a building and/or civil penalties for owners’ failure to 
timely certify correction of violations and/or for failure to file a 
Multiple Dwelling Registration.  
Comprehensive Supplemental  
Cases in which HPD seeks a finding of contempt and/or additional 
civil penalties against landlords who have failed to comply with 
orders to correct violations.  
Heat and Hot Water  
Cases in which HPD seeks an order to restore and maintain heat 
and hot water at a residential building and civil penalties.  
Heat and Hot Water 
Supplemental  
Cases in which HPD seeks a finding of contempt and/or additional 
civil penalties against landlords who have failed to comply with 
orders to provide heat and/or hot water.  
False Certifications  
Cases in which HPD seeks civil penalties against landlords who 
have falsely certified to HPD that violations were corrected when 
they had not been.  
Access Warrant  
HPD commences cases seeking access warrants when HPD 
inspectors and/or contractors and crews sent by HPD have been 
denied access to inspect and/or to repair conditions in a residential 
building.  
7A Proceedings  
Cases in which HPD seeks the appointment of an administrator for 
a building based on conditions or acts dangerous to life, health or 
safety, harassment and/or deprivation of services  
CONH  
Before applying to the Department of Buildings for a permit to 
demolish or reconfigure some buildings, including single room 
occupancy multiple dwellings and some multiple dwellings in 
several zoning districts, the owner must obtain a Certification of 
No Harassment (“CONH”) from HPD. The owner submits an 
application and HPD investigates and determines whether to issue 
a CONH. If HPD determines that there is reasonable cause to 
believe that harassment occurred, a hearing is held before the 
Office of Administrative Trials and Heading (“OATH”). After 
OATH issues its findings and recommendations, HPD determines 
whether to issue a CONH. A finding of harassment prevents the 
owner from obtaining certain types of demolition and alteration 
permits for three years in the case of single room occupancy 
multiple dwelling, or possibly permanently in properties located in 
certain Special Zoning Districts (unless the owner complies with 
an affordable housing requirement). 
 
 

