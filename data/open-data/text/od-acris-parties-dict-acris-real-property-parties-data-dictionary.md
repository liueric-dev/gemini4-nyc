# Data dictionary: od-acris-parties-dict-acris-real-property-parties-data-dictionary.xlsx

Source: https://data.cityofnewyork.us/d/636b-3b5g
Extracted from: od-acris-parties-dict-acris-real-property-parties-data-dictionary.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | ACRIS - Real Property Parties |
| Agency Name | Department of Finance |
| Update Frequency | Monthly |
| Dataset Description | The parties under which real property documents recorded in ACRIS are indexed. |
| Dataset Keywords | dof, acris land records |
| Dataset Category | City Government |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. | The ACRIS Real Property Parties dataset lists all parties (individuals and companies) associated with real property documents recorded in ACRIS. The parties in this dataset can be linked back to the document details in the ACRIS Real Property Master dataset using the document id and good through date fields common to both datasets. If there is no matching document id, good through date combination in the ACRIS Personal Real Master dataset, then the record for this document was corrected in ACRIS after publication in OpenData and the document is no longer indexed against this party. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the ideosyncracies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Term, Acronym, or Code Definitions | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) |
| Document ID | CCCNNNNNNNNNNNNN |
| Record Type | ‘P’ for party record |
| Party Type | Party type code |
| Name | Name of party |  | generally last name, first name middle initial suffix  for individuals |
| Address Line 1 | Name attention/address of party |
| Address Line 2 | Street address of party |
| Country | Country location of party |  | see ACRIS Country Codes dataset for values |
| City | City location of party |
| State | State location of party |  | see ACRIS State Codes dataset for values |
| Zip | Zip code of party |
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
