# Workstream 2 gaps and corrections (`law-state/`)

## Gaps

### Rent Stabilization Code (9 NYCRR Parts 2520-2531), consolidated text: only from a secondary source

**Decision (logged for the owner).** Every RSC section was collected from Cornell LII (law.cornell.edu/regulations/new-york/9-NYCRR-25xx.y) as `source_type: secondary`, `committable: no`, in `local/`.
- LII's notes show amendments from the NYS Register of November 8, 2023, so it reflects the HSTPA-era code.
- Westlaw's page for § 2523.4 showed "Current through September 15, 2021".
- The section list came from Westlaw's table of contents (`st-9nycrr-rsc-toc`).
- Before citing any of this in the public repo, check it against an official copy, or use the DHCR amendment text plus the NYS Register.

How each host was tried:
- **DHCR, hcr.ny.gov:** no consolidated code on the site.
  - Searched the 8-page sitemap (14,801 URLs) and the regulatory-information page.
  - Tried paths `/rent-stabilization-code`, `/rsc`, `/rent-laws-and-regulations` and `/laws-and-regulations`. All 404.
  - DHCR hosts only amendment documents:
    - `rsc-rule-text`: the 2023 adopted amendment text, collected as `st-9nycrr-rsc-2023-amendments`
    - `rent-stabilization-code-amendments-hstpa-revisions`: a 2022-08-30 PDF of the same title, most likely the proposed version. Not collected, because the 2023 text replaces it.
- **Westlaw (govt.westlaw.com/nycrr):** per the coordinator's instruction (Nov 21), use it only to confirm section numbers and dates, not to copy text. It labels itself "Unofficial".
- **Cornell LII (law.cornell.edu/regulations/new-york/...):** has section pages. It is a secondary mirror, so not used for text.
- **NYC Rent Guidelines Board site:** not tried for the code. A search result says it lists the code among its downloads (see the Rent Guidelines Board section below).
- **NY Department of State:** publishes the NYS Register. The Nov 8, 2023 issue was collected (`st-nys-register-2023-11-08`). It has the adoption notices and their effective dates, but only a summary of the RSC changes, because the full text was "available on DHCR's website".

### NYC rent control regulations (9 NYCRR Parts 2200-2211) and other DHCR rules, consolidated text
Same situation as the RSC. DHCR hosts only the amendment PDF, collected as `st-9nycrr-nyc-rent-eviction-regs-amendments`. The NYS Register adoption notice (I.D. No. HCR-35-22-00004-A, effective 2023-11-08) says the final rule had no changes from the published text, so the 2022 PDF is the adopted text.

LII files these regulations under Chapter VII Subchapter D, "Rent And Eviction Regulations-new York City (Part 2200 to 2211)". All 133 sections listed there were collected from LII as secondary sources (`local/`, `committable: no`), on the same terms as the RSC.

### Rent Guidelines Board orders: only 2026 collected
- **Collected:** Order #58 (2026), the City Record version, from rules.cityofnewyork.us (`st-rgb-order-58-2026`).
- **Earlier orders not collected** (#57 for 2025-26 and earlier):
  - rentguidelinesboard.cityofnewyork.us returned 403 to a plain curl of its intro page.
  - A search found `rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2025/07/Apt-Order-57.pdf`. My attempt to download it was denied by the session's permission classifier ("Unauthorized Access").
  - I did not work around that denial, through the browser or otherwise.
  - The project owner can decide whether to fetch the earlier orders, for example in the browser.

### HSTPA change list: index only
`st-hstpa-2019-change-index` lists each bill section's verbatim opening words by Part. It is extracted by script, not hand-written. It was not turned into a normalized citation table: some lines are nested headings from the quoted amended text, and the bill amends unconsolidated chapters by chapter number, so mapping them to the current sections needs a human check.

### April 2025 Good Cause notice: partial text
In `st-dhcr-gce-notice-2025-04`, pages 1, 3, 5 and 7 are images with no text layer. No OCR was done.

### Local Emergency Housing Rent Control Act: no section breakdown
The API law tree for `LEH` is empty at every date tried (2019-06-28, 2020-04-17, 2021-11-12, current). The whole act's text sits on the chapter document `-CH21-1962`, so it was collected as a single item.

### Dates

**Open Legislation `activeDate`.**
- 2014-09-22 is the API's baseline. For sections at that date, `effective_date` is `unknown`, with a note "unchanged since at least 2014-09-22 (API baseline)". This was corrected after a reviewer flagged it.
- Later dates are the publication dates of the current version.
- Sections with `* NB` annotations have more than one version, or delayed or expiring effect. They are flagged in `notes`.

**eCFR.** `effective_date` is the latest `amendment_date` among the unit's sections, from the eCFR versions API. 24 CFR 5 Subpart G (NSPIRE) shows 2026-11-12, a very recent amendment.

## Corrections to README pointers

**RPAPL Articles 7-A, 7-C and 7-D, described in the README as "administrator for rents", "administrator for dangerous conditions" and "judgment directing repairs".**
- Article 7-A is the NYC article. Its title is "Special Proceedings By Tenants of Dwellings In the City of New York and the Counties of Nassau, Suffolk, Rockland and Westchester For Judgment Directing Deposit of Rents and the Use Thereof For the Purpose of Remedying Conditions Dangerous to Life, Health or Safety".
- Article 7-C is the same remedy for the rest of the state. § 796-a(4) says it does **not** apply in NYC or in Nassau, Suffolk, Rockland and Westchester.
- Article 7-D (repairs) **cannot be brought in NYC**. § 797(3) bars it in Nassau, Suffolk, Richmond, New York, Bronx, Kings and Queens counties.
- So the README's workstream 3 pointer to nycourts "RPAPL 7-C administrator" and "RPAPL 7-D repairs" forms likely names articles that NYC tenants can't use. Worth checking which article those forms actually cite. A browser tab opened by another agent showed a nycourts form named `-ucs-lt12a-noticeofpetitionart7drepairs.pdf`, so the courts do publish an Article 7-D form. Whether NYC Housing Court accepts it needs checking against § 797(3).

**Smaller corrections:**
- RPL § 238-a is titled "Limitation on fees", not "fees and deposits". Deposits are in GOL Article 7 Title 1.
- "Penal Law § 250" is Article 250. Eavesdropping is §§ 250.00 and 250.05.
- The Social Services law id is `SOS`, as the README guessed. § 143-b is confirmed as "Avoidance of abuses in connection with rent checks".
- "Title X § 1018" is codified at 42 U.S.C. § 4852d. Its regulations are 24 CFR 35 Subpart A and 40 CFR 745 Subpart F.
- NSPIRE is 24 CFR Part 5 Subpart G, "Physical Inspection of Real Estate".
- NYC Civil Court Act § 110 is confirmed as "Housing part". The small claims article is Article 18.
- GOL § 7-108 is confirmed, titled "Deposits made by tenants of non-rent stabilized dwelling units".
- Good Cause Eviction is confirmed as RPL Article 6-A (§§ 210 to 218), enacted as L.2024 ch. 56 Part HH. Part HH says the act expires June 15, 2034.
- Utility interruption: RPL Article 7 has no section with that name. § 235-a covers tenant payments to utilities and cites Public Service Law §§ 33, 34 and 116, which were collected.
