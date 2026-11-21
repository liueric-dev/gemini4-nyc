# Workstream 2 checklist: NY State and federal law (`law-state/`)

Counts are manifest items. A state law item is one section. A federal regulation item is one eCFR subpart, or a whole part where noted, and lists its sections in `citation`. Status as of 01:05 New York time, Sat Nov 21. The manifest has 763 items:
- 538 official, all `committable: yes` except the DHCR notices and the NYS Register issue (license unknown, kept in `local/`)
- 225 secondary (Cornell LII copies of the RSC and NYC rent control regulations, plus the Westlaw table of contents), all in `local/`

## Do first

| Target (README) | Got | Ids | Status |
|---|---|---|---|
| RPL § 235-b warranty of habitability | yes | `st-rpl-235-b` | done |
| RPL § 223-b retaliation | yes | `st-rpl-223-b` | done |
| Every other tenant-protection section in RPL Article 7 (utility interruption, lease terms, illegal clauses) | all 55 sections of Article 7 (§§ 220 to 238-a, including § 233-b*2) | `st-rpl-220` … `st-rpl-238-a` | done. Article 7 is collected whole, not filtered. Utility: § 235-a (tenant pays the utility and offsets rent), plus Public Service Law §§ 32-35 and 116, which § 235-a cites (`st-psl-*`). Illegal clauses: §§ 234, 235-c, 235-h, 238-a, plus GOL § 5-321 (`st-gol-5-321`). |
| Multiple Dwelling Law, all articles that apply to NYC | all 193 sections in the API tree, Articles 1 to 11 | `st-mdl-*` | done. MDL § 3(1): the chapter applies to all cities of 325,000 or more, so the whole law applies in NYC. |
| RPAPL Article 7 (incl. § 711, § 768) | 32 sections (§§ 701 to 768) | `st-rpapl-7xx` | done |
| RPAPL Article 7-A | 15 sections (§§ 769 to 783) | `st-rpapl-769` … | done. **Applies in NYC**: the article title and § 769(1) cover NYC and the counties of Nassau, Suffolk, Rockland and Westchester. |
| RPAPL Article 7-C | 14 sections (§§ 796 to 796-m) | `st-rpapl-796*` | done. **Does not apply in NYC**: § 796-a(4) excludes NYC and the counties of Nassau, Suffolk, Rockland and Westchester. |
| RPAPL Article 7-D | 11 sections (§§ 797 to 797-j) | `st-rpapl-797*` | done. **Not available in NYC**: § 797(3) bars these proceedings in any court in Nassau, Suffolk, Richmond, New York, Bronx, Kings or Queens counties. |
| NYC Civil Court Act § 110 (Housing Part) | yes | `st-ccact-110` | done |
| GOL § 7-108 and the rest of GOL Article 7 Title 1 | all 7 sections (§§ 7-101 to 7-109) | `st-gol-7-1xx` | done |

All Do-first items were done by 00:43.

## Then

| Target | Got | Ids | Status |
|---|---|---|---|
| RPL § 238-a fees and deposits | yes. The section is titled "Limitation on fees" | `st-rpl-238-a` | done |
| Flood history disclosure | RPL § 231-b "Flood history and risk notice in residential leases" | `st-rpl-231-b` | done |
| Good Cause Eviction, RPL Article 6-A | all 9 sections (§§ 210 to 218) | `st-rpl-210` … `st-rpl-218` | done |
| Good Cause as enacted | L.2024 ch. 56 (S8306-C) Part HH. The act expires June 15, 2034 | `st-gce-2024-s8306c-part-hh` | done |
| Yearly Good Cause rent cap (published) | DHCR's annual notices under RPL § 211, with the CPI % change and the FMR exemption tables: 2024, Feb 2025, Apr 2025 (partial text), Jul/Aug 2026 (current) | `st-dhcr-gce-notice-*` | done |
| Rent Stabilization Code (9 NYCRR 2520-2531) | Three sources:<br>(1) DHCR's adopted 2023 amendment text (official, as-enacted, effective 2023-11-08 per the NYS Register)<br>(2) every RSC section, current consolidated text from Cornell LII (**secondary**, in `local/`, `committable: no`)<br>(3) the part and section list read from Westlaw's table of contents (headings only, in `local/`) | (1) `st-9nycrr-rsc-2023-amendments`<br>(2) `st-9nycrr-25xx-y`<br>(3) `st-9nycrr-rsc-toc` | done, but the consolidated text is secondary. No government host publishes it. See gaps.md |
| DHCR NYC rent control regulations (9 NYCRR Parts 2200-2211, Chapter VII Subchapter D) | (1) DHCR amendment text (official). The NYS Register adoption notice says "No changes" from that text and gives the effective date 2023-11-08.<br>(2) all 133 sections, current consolidated text from Cornell LII (**secondary**, in `local/`, `committable: no`) | (1) `st-9nycrr-nyc-rent-eviction-regs-amendments`, `st-nys-register-2023-11-08`<br>(2) `st-9nycrr-22xx-y` | done, but the consolidated text is secondary. See gaps.md |
| Tenant Protection Regulations (ETPA regs, mostly outside NYC) | 2023 amendment text, effective 2023-11-08 | `st-9nycrr-tpr-2023-amendments` | partial (extra item) |
| NYS Register, Nov 8, 2023 (DHCR adoption notices) | whole issue, with filing numbers and effective dates | `st-nys-register-2023-11-08` (`local/`, license unknown) | done |
| ETPA (`ETP`) | all 18 sections (§ 5-a is marked repealed in the API tree) | `st-etpa-*` | done |
| Emergency Housing Rent Control Law (`ERL`) | all 18 sections | `st-ehrcl-*` | done |
| Local Emergency Housing Rent Control Act (`LEH`) | whole act as one document (the API tree has no sections) | `st-lehrca-ch21-1962` | done |
| HSTPA 2019 text and what it changed | bill S6458/A8281 (L.2019 ch. 36): full text, sponsor memo, Senate summary of Parts A to O | `st-hstpa-2019` | done. Plus `st-hstpa-2019-change-index`, an index of every bill section's verbatim opening words by Part, showing what each Part amends, adds or repeals. |
| Spiegel Law, SSL § 143-b | yes ("Avoidance of abuses in connection with rent checks"), plus § 143-c (rent security deposits) | `st-ssl-143-b`, `st-ssl-143-c` | done |
| NYC Civil Court Act small claims article | Article 18, all 16 sections (§§ 1801 to 1815*2) | `st-ccact-18xx` | done |
| NY State Human Rights Law, Executive Law Article 15 | all 17 sections (§§ 290 to 301). Housing: § 296 subdivisions 2-a, 5 and 18 each open "It shall be an unlawful discriminatory practice for the owner…". Not exhaustive | `st-exec-29x` | done. Whole article, not filtered to housing |
| Penal Law § 250 on recording | Article 250, all 16 sections (§§ 250.00 to 250.71). Eavesdropping is §§ 250.00 and 250.05 | `st-penal-250-*` | done |
| Federal lead disclosure, Title X § 1018 | 42 U.S.C. § 4852d (Title X § 1018 is codified here), plus § 4851b definitions | `fed-42usc-4852d`, `fed-42usc-4851b` | done |
| 24 CFR Part 35 | all non-reserved subparts (A, B, C, D, F, G, H, I, J, K, L, M, R) | `fed-24cfr-35-*` | done |
| 40 CFR Part 745 | subparts D, E (renovation), F (disclosure), L, Q | `fed-40cfr-745-*` | done |
| NSPIRE, 24 CFR Part 5 | Subpart G "Physical Inspection of Real Estate" (§§ 5.701 to 5.713). Latest amendment 2026-11-12 | `fed-24cfr-5-g` | done |
| Fair Housing Act | 42 U.S.C. §§ 3601 to 3619 and 3631, plus HUD regulations 24 CFR Part 100 | `fed-42usc-36xx`, `fed-24cfr-100` | done |
| Rent Guidelines Board orders | 2026 Apartment & Loft Order #58 (June 25, 2026): 0% for 1-year and 0% for 2-year leases starting Oct 1, 2026 to Sep 30, 2027. City Record version, with explanatory statements and the other 2026 orders | `st-rgb-order-58-2026` | partial. Earlier years not collected (see gaps.md) |
| NSPIRE standards and notices (Federal Register) | final rule 88 FR 30442 (2023), inspection standards notice 88 FR 40832, compliance extensions (89 FR 55645, 90 FR 46911, 90 FR 46912), CO detector and smoke alarm notices (90 FR 37546, 90 FR 39414), scoring notice 91 FR 61432 (2026) | `fed-fr-*` | done |

Extras collected for coverage:
- 24 CFR 982 Subparts G, I (Housing Quality Standards), J and L (Section 8 vouchers)
- 24 CFR 966 (public housing lease and grievance, relevant to NYCHA)
- 24 CFR 5 Subpart L (VAWA protections)
- GOL §§ 5-321 and 5-331
- Public Service Law §§ 32-35 and 116 (utility shutoffs in multiple dwellings, cited by RPL § 235-a)
- Public Health Law Article 13 Title 10, Control of Lead Poisoning, all 13 sections (`st-pbh-*`). § 1377, the state rental registry and proactive lead inspections, excludes cities of one million or more, so it **does not apply in NYC**.
- NYC Civil Court Act Article 2, jurisdiction, all 14 sections, including § 204 summary proceedings (`st-ccact-2xx`)
- Penal Law Article 241, Harassment of Rent Regulated Tenants, §§ 241.00 to 241.07 (`st-penal-241-*`)
- 24 CFR Part 8, Section 504 nondiscrimination in federally assisted programs, whole part with 33 sections (`fed-24cfr-8`)
- 15 U.S.C. § 9058, the CARES Act 30-day notice to vacate for covered properties (`fed-15usc-9058`)
- 24 CFR Part 245, tenant participation in multifamily housing projects (`fed-24cfr-245`)
- 24 CFR Part 247, evictions from certain subsidized and HUD-owned projects (`fed-24cfr-247`)
- 24 CFR Part 964, tenant participation in public housing (`fed-24cfr-964`)

## Live fetch

| Source and endpoint | Access | Response time seen | Rate limits | Update frequency | Terms allow programmatic use? | Verdict |
|---|---|---|---|---|---|---|
| NY Senate Open Legislation API: `GET https://legislation.nysenate.gov/api/3/laws/{lawId}/{locationId}?key=…` (section); `/api/3/laws/{lawId}` (tree, add `full=true` to get all text in one call); `/api/3/bills/{session}/{printNo}`; `/api/3/laws/search?term=` | free key | section about 0.06 to 0.10 s; RPP tree (334 KB) 0.15 s; bill 0.4 s; full RPP tree with text (1.6 MB) one call. 650+ calls at 1/s with no errors | docs: "Requests made with an API key are limited to 10 requests per second and 4 concurrent requests per key." | Laws republish when amended. Each doc carries `activeDate` and `publishedDates` (RPP updates in 2026: Jun 5, Jun 12, Sep 4). Bills are "near-real time" per docs | Yes. It is the Senate's public API, and a free key is required | **good** |
| eCFR Versioner API: `https://www.ecfr.gov/api/versioner/v1/full/{date}/title-{n}.xml?part=&subpart=`; `/structure/…json`; `/versions/title-{n}.json?part=` (per-section amendment dates); `/titles.json` | open, no key. Must send `Accept-Encoding: gzip` or `full` returns an error | 0.2 to 0.3 s typical, some 2.7 to 4 s | none stated in responses. The developer docs page redirected to unblock.federalregister.gov for the fetch tool, so its terms were not read | titles.json showed Title 24 up to date as of 2026-11-19 (2 days before retrieval), so roughly daily | US government work, public domain. Formal terms page not read (blocked) | **good** |
| govinfo US Code link service: `https://www.govinfo.gov/link/uscode/42/{section}?link-type=html` | open, no key | 0.13 to 0.21 s | none seen | annual US Code edition (2024 edition served) | public domain, official GPO | **good** (for static statute text; rarely changes) |
| DHCR hcr.ny.gov (Good Cause notices, rule text PDFs) | plain fetch | 0.1 to 0.6 s | none stated | Good Cause notice yearly (on or before Aug 1, per RPL § 211); rule texts rarely | public government site; no API | **possible** (stable URLs per notice, but new notices get new URLs, e.g. `good-cause-eviction-law-notice-august-2026`) |
| Federal Register API: `https://www.federalregister.gov/api/v1/documents.json?conditions[term]=…`; `/api/v1/documents/{doc}.json` (metadata, including `raw_text_url`, `effective_on`, `dates`) | open, no key | 0.08 to 0.3 s | none stated in responses | new documents appear with each issue; each document has a `publication_date` | US government work, public domain | **good** (for finding new HUD notices such as NSPIRE updates) |
| Cornell LII NYCRR pages: `https://www.law.cornell.edu/regulations/new-york/9-NYCRR-{section}` | plain fetch | about 0.2 s | none seen; throttled to about 1 request per 1.2 s | LII says "State regulations are updated quarterly" | LII terms not read. Secondary mirror | **possible** for lookups, but secondary, so not for the public repo |
| Westlaw NYCRR (govt.westlaw.com/nycrr) | browser only (blocks scripts) | page loads about 2 to 3 s in Chrome | — | sections show "Current through" dates (§ 2523.4: September 15, 2021) | self-labelled "Unofficial". Coordinator: confirm numbers and dates only, do not copy text | **no** |
| NY Department of State, NYS Register PDFs: `https://dos.ny.gov/system/files/documents/{yyyy}/{mm}/{mmddyy}.pdf` | plain fetch | 0.5 s | — | per issue (only the Nov 8, 2023 issue was checked) | state publication; license not stated | **possible** (to track new DHCR rule adoptions) |
| rules.cityofnewyork.us PDF uploads (RGB orders as published) | plain fetch worked for a PDF URL | 0.15 s | — | yearly (Order #58 adopted June 25, 2026; City Record PDF created Sep 1, 2026) | city publication | **possible** |
| uscode.house.gov | plain fetch | — | — | — | — | not used: the URL tried returned 404; govinfo used instead |
| rentguidelinesboard.cityofnewyork.us | 403 to curl on the HTML. Later PDF requests were denied by the session's permission classifier | — | — | yearly orders | — | **no** for live fetch |
