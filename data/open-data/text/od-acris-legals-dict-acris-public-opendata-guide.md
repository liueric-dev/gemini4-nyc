









ACRIS OpenData Extract Guide


I Revision History
The official version of this document will be maintained by the ACRIS Technical Team.
Date
Version
Reason for change(s)
Author(s)
09/15/2013
1.0
Initial Revision
ACRIS Team

Table of Contents

 TOC \o "1-1" \h \z \t "Heading 2,2,CD H1,1,CD H2,2,CD H3,3,CD H4,4"  HYPERLINK \l "_Toc501733375" I Revision History	 PAGEREF _Toc501733375 \h 2
 HYPERLINK \l "_Toc501733376" 1	Introduction	 PAGEREF _Toc501733376 \h 4
 HYPERLINK \l "_Toc501733377" 2	Standard Operating Procedures	 PAGEREF _Toc501733377 \h 5
 HYPERLINK \l "_Toc501733378" 3	Extract Definition	 PAGEREF _Toc501733378 \h 6
 HYPERLINK \l "_Toc501733379" 3.1	REAL PROPERTY RECORDS	 PAGEREF _Toc501733379 \h 6
 HYPERLINK \l "_Toc501733380" 3.1.1	REAL PROPERTY MASTER	 PAGEREF _Toc501733380 \h 6
 HYPERLINK \l "_Toc501733381" 3.1.2	REAL PROPERTY LEGALS	 PAGEREF _Toc501733381 \h 7
 HYPERLINK \l "_Toc501733382" 3.1.3	REAL PROPERTY PARTIES	 PAGEREF _Toc501733382 \h 8
 HYPERLINK \l "_Toc501733383" 3.1.4	REAL PROPERTY REFERENCES	 PAGEREF _Toc501733383 \h 8
 HYPERLINK \l "_Toc501733384" 3.1.5	REAL PROPERTY REMARKS	 PAGEREF _Toc501733384 \h 9
 HYPERLINK \l "_Toc501733385" 3.2	PERSONAL PROPERTY RECORDS	 PAGEREF _Toc501733385 \h 10
 HYPERLINK \l "_Toc501733386" 3.2.1	PERSONAL PROPERTY MASTER	 PAGEREF _Toc501733386 \h 10
 HYPERLINK \l "_Toc501733387" 3.2.2	PERSONAL PROPERTY LEGALS	 PAGEREF _Toc501733387 \h 11
 HYPERLINK \l "_Toc501733388" 3.2.3	PERSONAL PROPERTY PARTIES	 PAGEREF _Toc501733388 \h 12
 HYPERLINK \l "_Toc501733389" 3.2.4	PERSONAL PROPERTY REFERENCES	 PAGEREF _Toc501733389 \h 13
 HYPERLINK \l "_Toc501733390" 3.2.5	PERSONAL PROPERTY REMARKS	 PAGEREF _Toc501733390 \h 14
 HYPERLINK \l "_Toc501733391" 3.3	CODE MAPPINGS	 PAGEREF _Toc501733391 \h 14
 HYPERLINK \l "_Toc501733392" 3.3.1	DOCUMENT CONTROL CODES	 PAGEREF _Toc501733392 \h 14
 HYPERLINK \l "_Toc501733393" 3.3.2	UCC COLLATERAL CODES	 PAGEREF _Toc501733393 \h 15
 HYPERLINK \l "_Toc501733394" 3.3.3	PROPERTY TYPE CODES	 PAGEREF _Toc501733394 \h 15
 HYPERLINK \l "_Toc501733395" 3.3.4	STATE CODES	 PAGEREF _Toc501733395 \h 15
 HYPERLINK \l "_Toc501733396" 3.3.5	COUNTRY CODES	 PAGEREF _Toc501733396 \h 16

INTRODUCTION 
This document provides the layout of data files and procedures for an extract to be sent to the public NYC OpenData portal in support of Local Law 11 of 2012. As changes are made this document will be updated and re-distributed.

An initial extract will be generated containing all documents recorded in ACRIS through the end of a fixed month and will be published on the NYC OpenData portal with this date. A new extract will be generated and published each month. Each monthly extract will contain all records for documents either recorded or corrected in the previous month and will be published with the month identified. The extract first extract will carry a date embedded in each record corresponding to the fixed month reference above while each monthly extract will carry a date embedded in each record corresponding to the month covered. In addition each file will contain a header record to define each field. 
Each extract of recorded documents will be split into ten files corresponding first to a separation into real and personal property recording where personal property recordings are all recording in the UCC and Federal Liens document class and real property recordings are all other documents. Once identified the data for each of the real and personal recordings will be broken into five subsets corresponding to:

document and recording details
properties associated with the document
parties associated with the document
cross references associated with the document
remarks associated with the document

The layout for each of the ten files is given in the Real and Personal Property Extract Definition sections below. Each file in the extract will include the maximum date of recordation or correction included in the extract as a good through date. For any document, the records with the latest good through date will be the current records. 

In addition five control table files will be generated and send each month. These control table files will be complete and each month's files are intended to replace the previous month. The layout of the control table files is given in the code mappings section below.
 


EXTRACT DEFINITION
Each document in the extract is identified by a 16 character document id which appears as the first field of each record. The next field in each record identifies the record type. There are ten different records layouts as described below.
REAL PROPERTY RECORDS
Real property records include documents in the Deeds and Other Conveyances, Mortgages & Instruments and Other Documents classes in ACRIS. These documents typically impact rights to real property and as such follow the real property rather than an individual.
REAL PROPERTY MASTER
For each document there is one and only one master record. As such the master record contains attributes for a document that can appear only once for a document like the document type, date and recorded date and time. The first field of the master record is the 16 character ACRIS document id which uniquely identifies a document in ACRIS. This document id is included in each subsequent record type and can be used to link these records back to the master record. This document id can also be used to look up the document in ACRIS Document Search.

Field
Field Name
Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
‘A’ for master record
3
CRFN
Text(13)
City Register File Number in Format YYYYNNNNNNNNN
4
Recorded Borough
Number(1)
Borough where document was recorded
5
Doc Type
Text(8)
Specific type of instrument
6
Document Date
Text(10)
Date Appearing on Document in Format MM/DD/YYYY
7
Document Amount
Number(16,2)
Total Consideration for Transfers and Principal debt or obligation for Mortgages
8
Recorded Date
Text(10)
Legal Date Instrument was Recorded in Format MM/DD/YYYY 
9
Modified Date
Text(10)
Date Document was Recorded or Index Data was Last Corrected in Format MM/DD/YYYY
10
Reel Year
Number(4)
Pre-ACRIS reel year
11
Reel Nbr
Number(5)
Pre-ACRIS reel number
12
Reel Page
Number(5)
Pre-ACRIS reel page
13
Percentage Transferred
Number(9,6)
Reported percentage of interest transferred if the percentage is available; otherwise is null
14
Good Through Date
Text(10)
MM/DD/YYYY – date of latest recording or correction included with this extract





REAL PROPERTY LEGALS
Each document may have zero or more associated properties. If a document has associated properties, there will be one legals record for each property. Legals records can be linked back to the original document by the first 16 character field of the record which is the document id.

Field
Field Name
Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
 ‘L’ for lot record
3
Borough
Number(1)
Borough Code:
1 = Manhattan 2 = Bronx 3 = Brooklyn 4 = Queens
4
Block
Number(5)
Block number of instrument
5
Lot
Number(4)
Lot number of instrument
6
Easement
Text(1)
Y’es or ‘N’o field
7
Partial Lot
Text(1)
‘P’artial, ‘E’ntire or ‘N’ot Applicable
8
Air Rights
Text(1)
‘Y’es or ‘N’o field
9
Subterranean Rights
Text(1)
Y’es or ‘N’o field
10
Property Type
Text(2)
Code defined in property codes record
11
Street Number
Text(12)
Street / House Number for BBL
12
Street Name
Text(32)
Street Name for BBL
13
Unit Address
Text(7)
Unit Number for BBL
14
 Good Through Date
 Text(10)
MM/DD/YYYY – date of latest recording or correction included with this extract

REAL PROPERTY PARTIES
Each document may have zero or more associated parties. If a document has associated properties, there will be one parties record for each party. Parties records can be linked back to the original document by the first 16 character field of the record which is the document id. 

Field
Field Name
Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
‘P’ for party record
3
Party Type
Text(1)
Party type code
4
Name
Text(70)
Name of party. For individual is typically last name, first name middle initial suffix
5
Address Line 1
Text(60)
Name attention/address of party
6
Address Line 2
Text(60)
Street address of party
7
Country
Text(2)
Country location of party
8
City
Text(30)
City location of party
9
State
Text(2)
State location of party
10
Zip
Text(9)
Zip code of party
11
Good Through Date
 Text(10)
MM/DD/YYYY – date of latest recording or correction included with this extract

REAL PROPERTY REFERENCES
Each document may have zero or more associated references to other documents. If a document has associated references, there will be one reference record for each reference.  Reference records can be linked back to the original document by the first 16 character field of the record which is the document id.

Field Location
Field Name
Field Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNN - Document ID of Document making the Reference
2
Record Type
Text(1)
‘X’ for cross reference record
3
CRFN of Reference
Text(13)
CRFN of Referenced Document
4
Document ID of Reference
Text(16)
Document ID of Referenced Document
5
Reel Year
Number(4)
Year of reel/page reference
6
Reel Borough
Number(1)
Borough of reel/page reference
7
Reel Nbr
Number(5)
Reel of reel/page  reference
8
Reel Page
Number(5)
Page of reel/page reference
9
Good Through Date
 Text(10)
MM/DD/YYYY – date of latest recording or correction included with OpenData update

REAL PROPERTY REMARKS
Each document may have zero or more associated text remarks. If a document has associated remarks, the remark may potentially be split into a number of remarks records dependent on the length of the remark. Following the layout below each remarks record will include up to 232 characters of the remark; remarks longer than 232 characters will be split into separate sequentially identified records each containing 232 characters of the remark. The original remark as displayed in ACRIS Document Search can be composed by concatenating in Sequence order all remarks with the same Document ID. This Document ID can then be used to link back to the original document by the first 16 character document id field.

Field Location
Field Name
Field Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
‘R’ for remarks record
3
Sequence
Number(2)
Number from 1-20 
4
Text
Text(232)
Portion of Remark for Given Sequence
5
Good Through Date
Text(10)
MM/DD/YYYY – date of latest recording or correction included with this extract
PERSONAL PROPERTY RECORDS
Personal property records include documents in the UCC and Federal Liens class in ACRIS. These documents typically impact rights to personal property associated with real property and as such follow the individual party rather than the real property.
PERSONAL PROPERTY MASTER
For each document there is one and only one master record. As such the master record contains attributes for a document that can appear only once for a document like the document type, date and recorded date. The first 16 character field of the master record is the ACRIS document id which uniquely identifies a document in ACRIS. This document id is included in each subsequent record type and can be used to link these records back to the master record. This document id can also be used to look up the document in ACRIS Document Search.

Field
Field Name
Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
‘A’ for master record
3
CRFN
Text(13)
YYYYNNNNNNNNN
4
Recorded Borough
Number(1)
Borough where document was recorded
5
Docoument Type
Text(8)
Specific type of instrument 
6
Document Amount
Number(14,2)
Principal debt or obligation
7
Recorded / Filed Date
Text(10)
MM/DD/YYYY  - Legal date instrument was recorded
8
UCC Collateral
Text(1)
UCC Collateral code 
9
Fedtax Serial / SLID Nbr
Text(12)
IRS Serial Nbr on Federal Tax Lien
10
Fedtax Assessment Date
Text(10)
MM/DD/YYYY - dae of Federal Tax Lien Assessment
11
RPTT Nbr
Number(12)
YYYYNNNNNNNN - Unique RPTT Nbr
12
Modified Date
Text(10)
MM/DD/YYYY - date document recorded or last modified
13
Reel Year
Number(4)
Pre-ACRIS reel year
14
Reel Nbr
Number(5)
Pre-ACRIS reel number
15
Reel Page
Number(5)
Pre-ACRIS reel page
16
File Nbr
Text(12)
Pre-ACRIS file number
27
Good Through Date
Text(10)
MM/DD/YYYY – date of latest recording or correction included with OpenData update

PERSONAL PROPERTY LEGALS
Each document may have zero or more associated properties. If a document has associated properties, there will be one legals record for each property.  Legals records can be linked back to the original document by the first 16 character field of the record which is the document id. 

Field
Field Name
Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
 ‘L’ for lot record
3
Borough
Number(1)
Borough Code:
4
Block
Number(5)
Block number of instrument
5
Lot
Number(4)
Lot number of instrument
6
Easement
Text(1)
‘Y’ or ‘N’ field
7
Partial Lot
Text(1)
P=partial E=entire
8
Air Rights
Text(1)
‘Y’ or ‘N’ field
9
Subterranean Rights
Text(1)
‘Y’ or ‘N’ field
10
Property Type
Text(2)
Code defined in property table
11
Street Number
Text(12)
Street Number for BBL
12
Street Name
Text(32)
Street Name for BBL
13
Unit
Text(7)
Unit Number for BBL
15
Good Through Date
Text(10)
MM/DD/YYYY – date of latest recording or correction included with OpenData update
PERSONAL PROPERTY PARTIES
Each document may have zero or more associated parties. If a document has associated properties, there will be one parties record for each party.  Parties records can be linked back to the original document by the first 16 characters of the record which is the document id. 

Field
Field Name
Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
‘P’ for party record
3
Party Type
Text(1)
Party type code
4
Name
Text(70)
Name of party
5
Address Line 1
Text(60)
Name attention/address of party
6
Address Line 2
Text(60)
Street address of party
7
Country
Text(2)
Country location of party
8
City
Text(30)
City location of party
9
State
Text(2)
State location of party
10
Zip
Text(9)
Zip code of party
11
Good Through Date
Text(10)
MM/DD/YYYY – date of latest recording or correction included with OpenData update
PERSONAL PROPERTY REFERENCES
Each document may have zero or more associated references to other documents. If a document has associated references, there will be one reference record for each reference.  Reference records can be linked back to the original document by the first 16 character field of the record which is the document id.

Field Location
Field Name
Field Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNN
2
Record Type
Text(1)
‘X’ for cross reference record
3
CRFN of Reference
Text(13)
CRFN of Referenced Document
4
Document ID of Reference
Text(16)
Document ID of Referenced Document
5
File Nbr
Text(12)
File number of reference
6
Good Through Date
Text(10)
MM/DD/YYYY – date of latest recording or correction included with this extract
PERSONAL PROPERTY REMARKS
Each document may have zero or more associated text remarks. If a document has associated remarks, the remark may potentially be split into a number of remarks records dependent on the length of the remark. Following the layout below each remarks record will include up to 232 characters of the remark; remarks longer than 232 characters will be split into separate sequentially identified records each containing 232 characters of the remark. The original remark as displayed in ACRIS Document Search can be composed by concatenating in Sequence order all remarks with the same Document ID. This Document ID can then be used to link back to the original document using the first 16 character document id field. 

Field Location
Field Name
Field Definition
Description
1
Document ID
Text(16)
CCCNNNNNNNNNNNNN
2
Record Type
Text(1)
‘R’ for remarks record
3
Sequence
Number(2)
Number from 1-20 
4
Text
Text(232)
Remarks
5
Good Through Date
Text(10)
MM/DD/YYYY – date of latest recording or correction included with this extract

CODE MAPPINGS
In ACRIS documents are stored with codes representing longer descriptions that are displayed on images generated by ACRIS and in Document Search. The translation from these codes is done via lookup tables. This section defines records for those lookup tables. The code lookup records will be fully replaced each month with new lookup records, but as ACRIS never deletes from its lookup tables, the net effect will be to publish new codes as they are added to ACRIS.
DOCUMENT CONTROL CODES
The Document Control Codes record maps the short codes stored in ACRIS to descriptive names as displayed in ACRIS Document Search.

Field
Field Name
Definition
Description
1
Record Type
Text(1)
‘D’ for Document control type record












2
Doc Type
Text(8)
Doc type code
3
Doc Type Description
Text(30)
Document type description 




4
Class Code Description
Text(30)
Document class description
5
Party1 Type
Text(20)
Party type 1 name for this document type
6
Party2 Type
Text(20)
Party type 2 name for this document type
7
Party3 Type
Text(20)
Party type 3 name for this document type

UCC COLLATERAL CODES
The UCC Collateral Codes record maps the short codes stored in ACRIS to descriptive collateral types as displayed in ACRIS Document Search. 

Field
Field Name
Definition
Description
1
Record Type
Text(1)
‘U’ for Collateral codes record












2
UCC Collateral Code
Text(1)
UCC Collateral code 
3
Description
Text(50)
UCC Collateral description 

















PROPERTY TYPE CODES
The Property Type Codes record maps the short codes stored in ACRIS to descriptive property types as displayed in ACRIS Document Search. 

Field
Field Name
Definition
Description
1
Record Type
Text(1)
‘G’ for Property type record












2
Property Type
Text(2)
Property type code 
3
Description
Text(40)
Property type description 





STATE CODES
The State Codes record maps the short codes stored in ACRIS to descriptive state names as displayed in ACRIS Document Search. 

Field
Field Name
Definition
Description
1
Record Type
Text(1)
‘S’ for State codes type record












2
State Code
Text(2)
State code 
3
Description
Text(20)
State name 










COUNTRY CODES
The Country Codes record maps the short codes stored in ACRIS to descriptive country names as displayed in ACRIS Document Search. 

Field
Field Name
Definition
Description
1
Record Type
Text(1)
‘T’ for Collateral type record












2
Country Code
Text(2)
Country code 
3
Description
Text(20)
Country name 















ACRIS OpenData Extract Guide



Ver. 1.0 PAGE  \* Arabic 15
Last Updated: 09/15/2013




ACRIS OpenData Extract Guide





