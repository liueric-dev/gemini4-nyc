# Data dictionary: od-acris-master-dict-acris-real-property-master-data-dictionary.xlsx

Source: https://data.cityofnewyork.us/d/bnx9-e6tj
Extracted from: od-acris-master-dict-acris-real-property-master-data-dictionary.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | ACRIS - Real Property Master |
| Agency Name | Department of Finance |
| Update Frequency | Monthly |
| Dataset Description | Document level details for Personal Property documents recorded in ACRIS. |
| Dataset Keywords | dof, acris land records |
| Dataset Category | City Government |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. | The ACRIS Real Property Master dataset includes document level details for deed, mortgages and other real property related documents recorded in ACRIS against properties in the four boroughs of Manhattan, Bronx, Brooklyn and Queens. In addtional the dataset also includes index details for stand-alone NYC and NYS transfer tax returns submitted to ACRIS (like returns related to the sale of cooperative shares) and NYC transfer tax returns submitted to the Richmond County Clerk.  Documents in this dataset are uniquely identified by both the document id and CRFN fields; however to find the most current version of the index data for the document, one must find the record with the most recent good through date. The good through date roughly corresponds to when a specific version of index data for a document was published in OpenData.  Most document will only have one good through date and for many documents that good through date corresponds to the initial date ACRIS data was published in OpenData; however some documents may have more than one.  After documents are recorded, they are included in the next monthly OpenData update with a good through date corresponding to the month of recording. If the index data for a document is subsequently updated in another month, all index data for the document is re-published to OpenData with a new good through date corresponding to the month of correction. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the ideosyncracies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Term, Acronym, or Code Definitions | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) |
| Document ID | CCCNNNNNNNNNNNNN |
| Record Type | ‘A’ for master record |
| CRFN | YYYYNNNNNNNNN |
| Recorded Borough | Borough where document was recorded |  | 1 = Manhattan 2 = Bronx 3 = Brooklyn 4 = Queens |
| Docoument Type | Specific type of instrument |  | see ACRIS Document Control Codes dataset for a list of document types |
| Document Date | MM/DD/YYYY - date that appears on document |
| Document Amount | Total Consideration for Transfers and Principal debt or obligation for Mortgages |
| Recorded  Date | MM/DD/YYYY  - Legal date instrument was recorded |
| Modified Date | MM/DD/YYYY - date document recorded or last modified |
| Reel Year | Pre-ACRIS reel year |
| Reel Nbr | Pre-ACRIS reel number |
| Reel Page | Pre-ACRIS reel page |
| Percentage Transferred | Reported percentage of interest transferred. |
| Good Through Date | MM/DD/YYYY – date of latest recording or correction included with OpenData update |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |

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
|  | Transportaion |
