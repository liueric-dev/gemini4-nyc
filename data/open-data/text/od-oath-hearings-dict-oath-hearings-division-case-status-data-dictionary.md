# Data dictionary: od-oath-hearings-dict-oath-hearings-division-case-status-data-dictionary.xlsx

Source: https://data.cityofnewyork.us/d/jz4z-kudi
Extracted from: od-oath-hearings-dict-oath-hearings-division-case-status-data-dictionary.xlsx

## Sheet: Dataset Info

| Data Dictionary - Dataset Information |
| General |
| Dataset Name | OATH Hearings Division Case Status |
| Agency Name | Office of Administrative Trials and Hearings (OATH) |
| Update Frequency | Daily |
| Dataset Description | The OATH Hearings Division Case Status dataset contains information about alleged public safety and quality of life violations that are filed and adjudicated through the City’s administrative law court, the NYC Office of Administrative Trials and Hearings (OATH) and provides information about the infraction charged, decision outcome, payments, amounts and fees relating to the case. The summonses listed in this dataset are issued and filed at the OATH Hearings Division by City enforcement agencies. |
| Dataset Keywords | oath, moda, ecb violations, violations, charges, environmental control board, tribunal, alj, administrative law judge, ticket, ticket finder, quality of life, business integrity commission, bic, department of buildings, dob, department of consumer affairs, dca, department of environmental protection, dep, fire department, fdny, department of health and mental hygiene, dohmh, department of information technology and telecommunications, doitt, landmarks preservation commission, lpc, department of parks and recreation, dpr, police department, nypd, department of sanitation, dsny, department of small business services, sbs, department of transportation, dot |
| Dataset Category | City Government |
| Detailed Description |
| List any additional information in order to provide context to the data for someone not familiar with your agency's operations. | DCA, DOHMH and TLC summonses may contain alphanumeric values. Because NYCServ does not contain a borough field, “NOT NYC” in Borough column appears for all TLC summonses. For TLC summonses, the Violation Details Column lists the most recent “Event Description” recorded in the TLC summons processing software (NYCServ): Document Printed: the decision was not picked up by the respondent, it was printed and mailed to the address on file. Decision Printed: respondent signed out for the decision following the hearing. Batch Insert: summons was entered into NYCServ. |
| Why is this data collected?  How is this data collected?  What does each record represent?  How can this data be used?  What are the ideosyncracies or limitations of the data to be aware of? |
| Form V 1.0 |

## Sheet: Column Info

| Data Dictionary - Column Information |
| Column Name | Column Description | Term, Acronym, or Code Definitions | Additional Notes  (where applicable, include the  range of possible values, units of measure, how to interpret null/zero values, whether there are specific relationships between columns, and information on column source) |
| Ticket Number | A unique identifier for the summons |
| Violation Date | The date on which the alleged violation indicated on the summons occurred |
| Violation Time | The time of day at which the alleged violation indicated on the summons occurred |
| Issuing Agency | A governmental agency authorized to issue summonses for violations of City rules and regulations |
| Respondent Last Name | The last name of the person to whom the summons was issued |
| Balance Due | The balance of the monetary penalty owed by the respondent |
| Violation Location (Borough) | One of the five boroughs of New York City (Brooklyn, Bronx, Manhattan, Queens and Staten Island) in which the alleged violation occurred |
| Violation Location (Block No.) | The block number of the location where the alleged violation occurred |
| Violation Location (Lot No.) | The lot number of the location where the alleged violation occurred |
| Violation Location (House #) | The number of the house, building or structure where the alleged violation occurred |
| Violation Location (Street Name) | The name of the street on which the alleged violation occurred |
| Violation Location (Floor) | The floor of the house, building or structure where the alleged violation occurrred |
| Violation Location (City) | Name of the City, town or community where the alleged violation occurred |
| Violation Location (Zip Code) | The zip code of the address where the alleged violation occurred |
| Violation Location (State Name) | The State in which the alleged violation occurred |
| Respondent Address (Borough) | The borough in which the respondent lives or is located |
| Respondent Address (House #) | The house number of the address at which the respondent lives or is located |
| Respondent Address (Zip Code) | The zip code of the address where the respondent lives or is located |
| Hearing Status | Hearing status |
| Hearing Result | Outcome or result of the hearing |
| Scheduled Hearing Location | The location or address at which the hearing will occur |
| Hearing Date | The date on which the hearing will occur |
| Hearing Time | The time at which the hearing will occur |
| Decision Location (Borough) | The borough in which the decision was rendered |
| Decision Date | The date on which the decision was rendered |
| Total Violation Amount | The monetary amount associated with the violation |
| Violation Details | Violation details include: section/rule of law, OATH code, penalty amount and idenfifying information of the employee of the enforcement agency |
| Date Judgment Docketed | The date on which the judgment was docketed |
| Respondent Address or Facility Number(For FDNY and DOB Tickets) | The address of the respondent |
| Penalty Imposed | The actual penalty the respondent is required to pay |
| Paid Amount | The total amount paid by the respondent |
| Additional Penalties or Late Fees | Monetary penalties which are levied in addition to the original penalty amount and which may include a fee for payments made after the payment due date. |
| Compliance Status | Indicates whether the respondent has taken measures to address the summons |
| Premises Type | Premises where the violation allegedly occurred |
| Charge #1: Code | The OATH Code for the first charge noted |
| Charge #1: Code Section | The law or City regulations for the first charge noted |
| Charge #1: Code Description | A short categorical description for the first charge noted |
| Charge #1: Infraction Amount | The monetary amount associated with the first charge noted |
| Charge #2: Code | The OATH Code for the second charge noted |
| Charge #2: Code Section | The law or City regulations for the second charge noted |
| Charge #2: Code Description | A short categorical description for the second charge noted |
| Charge #2: Infraction Amount | The monetary amount associated with the second charge noted |
| Charge #3: Code | The OATH Code for the third charge noted |
| Charge #3: Code Section | The law or City regulations for the third charge noted |
| Charge #3: Code Description | A short categorical description for the third charge noted |
| Charge #3: Infraction Amount | The monetary amount associated with the third charge noted |
| Charge #4: Code | The OATH Code for the fourth charge noted |
| Charge #4: Code Section | The law or City regulations for the fourth charge noted |
| Charge #4: Code Description | A short categorical description for the fourth charge noted |
| Charge #4: Infraction Amount | The monetary amount associated with the fourth charge noted |
| Charge #5: Code | The OATH Code for the fifth charge noted |
| Charge #5: Code Section | The law or City regulations for the fifth charge noted |
| Charge #5: Code Description | A short categorical description for the fifth charge noted |
| Charge #5: Infraction Amount | The monetary amount associated with the fifth charge noted |
| Charge #6: Code | The OATH Code for the sixth charge noted |
| Charge #6: Code Section | The law or City regulations for the sixth charge noted |
| Charge #6: Code Description | A short categorical description for the sixth charge noted |
| Charge #6: Infraction Amount | The monetary amount associated with the sixth charge noted |
| Charge #7: Code | The OATH Code for the seventh charge noted |
| Charge #7: Code Section | The law or City regulations for the seventh charge noted |
| Charge #7: Code Description | A short categorical description for the seventh charge noted |
| Charge #7: Infraction Amount | The monetary amount associated with the seventh charge noted |
| Charge #8: Code | The OATH Code for the eighth charge noted |
| Charge #8: Code Section | The law or City regulations for the eighth charge noted |
| Charge #8: Code Description | A short categorical description for the eighth charge noted |
| Charge #8: Infraction Amount | The monetary amount associated with the eighth charge noted |
| Charge #9: Code | The OATH Code for the ninth charge noted |
| Charge #9: Code Section | The law or City regulations for the ninth charge noted |
| Charge #9: Code Description | A short categorical description for the ninth charge noted |
| Charge #9: Infraction Amount | The monetary amount associated with the ninth charge noted |
| Charge #10: Code | The OATH Code for the tenth charge noted |
| Charge #10: Code Section | The law or City regulations for the tenth charge noted |
| Charge #10: Code Description | A short categorical description for the tenth charge noted |
| Charge #10: Infraction Amount | The monetary amount associated with the tenth charge noted |

## Sheet: Dataset Revision History

| Data Dictionary - Revision History Description of all changes to the format, data, or method of collection of the dataset that have taken place since the initial release. |
| Version | Date | Change Highlights | Comments |
|  | 2016-03-02 00:00:00 | Dataset published |
|  | 2018-09-11 00:00:00 | Added additional information |
|  | 2026-03-04 00:00:00 | The Respondent First Name, Respondent Address (Street Name), Respondent Address (City), and Respondent Address (State Name) fields have been removed from this dataset. |

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
