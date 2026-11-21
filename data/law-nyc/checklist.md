# law-nyc checklist

Workstream 1 (NYC law). Status as of 2026-11-21 01:50 New York time. Counts come from `manifest.jsonl` (one line per section file; built by `local/tools/build_law.py`).

## Do first

| Target | Source | Status |
|---|---|---|
| NYC Housing Maintenance Code, Admin Code Title 27 Ch. 2, all sections | amlegal NYCadmin 0-0-0-60027 (252 records: chapter, subchapter and article headings plus sections § 27-2001 to § 27-2154) | DONE: 216 section files (`nyc-hmc-*`), every record hash-verified |
| HPD rules, RCNY Title 28, chapters implementing the HMC | amlegal NYCrules, per chapter | DONE for all 23 Do-first chapters: all hash-verified; RCNY 28 total incl. lower-priority chapters: 236 section/appendix files (`nyc-rcny28-*`) (ch. 25 is the largest: 77 records, ~202k chars) |

HMC topics from the README, all inside the HMC files: repairs and maintenance (Subch. 2 Art. 1, § 27-2005 ff.), heat and hot water (Art. 8, § 27-2028 ff.), cooling (§ 27-2030), pests, mold and allergens (Art. 4, §§ 27-2017 to 27-2017.12, L.L. 2018/055), bedbug history (§§ 27-2018.1, 27-2018.2), lead paint (Art. 14, § 27-2056.1 ff., L.L. 2004/001), window guards (§ 27-2043.1), smoke and CO detectors (Art. 11, § 27-2045; the former CO section § 27-2046.1 was repealed by L.L. 2016/157), harassment (§ 27-2004 a 48, § 27-2005 d, § 27-2115 m ff.), the tenant's duties (§ 27-2006 ff.), violation classes, correction periods and penalties (§ 27-2115 and Subch. 5).

RCNY Title 28 chapters chosen as HMC-implementing or tenant-facing (Do first): 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 25, 36, 40, 44, 45, 46, 47, 48, 53, 54, 55, 56, 59. Lower priority, collected afterwards: 3 (Mitchell-Lama: succession, surcharges, carrying-charge increases), 14, 21, 24, 43, 52, 60. Not collected: the tax-exemption, finance and development-program chapters (1, 2, 4-8, 19, 22, 26-35, 37-39, 41, 42, 49-51, 57, 58, 61-64), which don't govern conditions in a tenant's apartment.

## Then

| Target (README "Then") | Collected | Ids |
|---|---|---|
| FARE Act (broker fees) | Admin Code Title 20 Ch. 4 Subch. 15, §§ 20-699.20 to 20-699.25 (consolidated). Also the as-enacted Local Law 119 of 2024 PDF from Legistar (raw + text) | `nyc-adm-20-699-*`, `nyc-ll-2024-119` |
| Tenant harassment outside the HMC | Unlawful eviction Title 26 Ch. 5 (§ 26-521 ff.); Human Rights Law § 8-107 (harassment based on protected class); Title 26 Ch. 12 (conditioning occupancy on medical treatment); Title 26 Ch. 24 (buyout agreements). The HMC's own harassment rules (§ 27-2004 a 48, § 27-2005 d, § 27-2115 m) and RCNY 28 Ch. 10 and 53 (certification of no harassment) are under Do first | `nyc-adm-26-52*`, `nyc-adm-8-107`, `nyc-adm-26-120*`, `nyc-adm-26-300*` |
| Tenant Bill of Rights | No Admin Code section creates a general "Tenant Bill of Rights" (see gaps.md). Collected: § 21-149 Supportive housing bill of rights, § 27-2009.2 Safe construction bill of rights (in the HMC), Title 26 Ch. 11 Housing Information Guide (§§ 26-1101 to 26-1104) and RCNY 28 Ch. 46. HPD's Tenant Bill of Rights guidance document is in `process/` (`proc-hpd-tenant-bill-of-rights*`) | `nyc-adm-21-149`, `nyc-hmc-27-2009-2`, `nyc-adm-26-110*` |
| Unlawful eviction and lockouts (§ 26-521) | Title 26 Ch. 5, all sections | `nyc-adm-26-521` to `-529` |
| Right to Counsel (§ 26-1301 ff.) | Title 26 Ch. 13 "Provision of Legal Services in Eviction Proceedings", all | `nyc-adm-26-130*` |
| Rent Stabilization Law (Title 26 Ch. 4) | All 26 records (§ 26-501 to § 26-520) | `nyc-adm-26-5**` |
| Rent control law (Title 26 Ch. 3) | All 23 records (§ 26-401 ff.), including the 81k-char § 26-405 | `nyc-adm-26-4**` |
| Human Rights Law housing provisions (Title 8) | §§ 8-101 to 8-107.1 (housing, reasonable accommodation, cooperative dialogue and lawful source of income are subdivisions of § 8-107); complaint and enforcement §§ 8-109 to 8-126, 8-128; § 8-502 (civil action). CCHR procedure rules 47 RCNY §§ 1-11 to 1-71 (selected) | `nyc-adm-8-*`, `nyc-rcny47-*` |
| Construction Codes: Tenant Protection Plans, after-hours work | § 28-104.7.16 Tenant protection plan; § 28-104.8 to 28-104.8.4; § 28-105.12.5 (noise code compliance); Noise Code §§ 24-219 to 24-224.1 (after-hours and weekend construction limits, § 24-222, § 24-223); DEP rules 15 RCNY Ch. 28 (construction noise mitigation, authorized work hours; selected), Ch. 30 (minimal noise impact construction, incl. resident notice) and Ch. 52 (after-hours noise complaint response times) | `nyc-adm-28-104-*`, `nyc-adm-28-105-12-5`, `nyc-adm-24-22*`, `nyc-rcny15-*` |
| Construction Codes: egress, fire escapes | Fire Code Ch. 10 (Means of Egress) in full: mostly "Reserved" stubs, with the real text at FC 1001, 1025 and 1027 (maintenance of means of egress). Building Code Ch. 10 (new construction egress) not collected | `nyc-fc-*` |
| Local Law 152 of 2016 (gas piping) and gas shutoffs | Title 28 Art. 318 (periodic gas piping inspection) and 1 RCNY § 103-10 (DOB rule) | `nyc-adm-28-318-*`, `nyc-rcny01-103-10` |
| Other Construction Code maintenance duties | Title 28 Art. 301 (owner's responsibility to maintain), Art. 304 (elevators, incl. occupant notice), Art. 312 (CO and smoke detectors), Art. 315 retroactive requirements (selected: gas alarms, elevator safety, outside gas shut-off, emergency water for residential occupancies, self-closing doors in R-1/R-2) | `nyc-adm-28-301-*`, `nyc-adm-28-304-*`, `nyc-adm-28-312-*` |
| Fire Code: blocked exits, fire escapes | Fire Code Ch. 10 (see above); FDNY rule 3 RCNY § 401-06 (fire safety notices and guide for residential buildings) | `nyc-fc-*`, `nyc-rcny03-*` |
| Electrical Code: exposed wiring | Electrical Code (Title 28 Ch. 11): enactment, NYC administrative sections EC 80-87 (existing installations, owner maintenance duty, unsafe wiring, disconnection) and a few dwelling-related amendments. The NFPA 70 base text is not on amlegal | `nyc-elec-*` |
| Health Code (DOHMH): window guards, lead, pests | Health Code Art. 131 (Buildings, incl. window guards § 131.15), Art. 151 (pests), Art. 173 (hazardous substances, incl. lead paint); 24 RCNY Ch. 12 (window falls prevention); Admin Code Title 17: repairs and nuisances §§ 17-113, 17-114, 17-142 to 17-145, uninhabitable houses § 17-159, window guards § 17-123, rodents §§ 17-133.1 to 17-133.4, lead §§ 17-181, 17-185, 17-186, 17-186.1, indoor allergens §§ 17-199.5 to 17-199.8, Ch. 9 (lead testing; Subch. 2 covers schools and day care only), Ch. 11 (pesticide neighbor notification) | `nyc-healthcode-*`, `nyc-rcny24-*`, `nyc-adm-17-*` |
| City pre-lease disclosures | Bedbug history § 27-2018.1 and 28 RCNY Ch. 59; lead § 27-2056.x and 28 RCNY Ch. 11; indoor allergen lease notice 28 RCNY Ch. 54 (appendices); window guard lease notice § 17-123 and Health Code Art. 131; stove knob notice 28 RCNY Ch. 55; housing information guide § 26-1103 and 28 RCNY Ch. 46; fire safety guide and notices 3 RCNY § 401-06; tenant data privacy Title 26 Ch. 30; consumer credit history Title 26 Ch. 29. Sprinkler and flood disclosures are state law (workstream 2) | see the rows above |
| Rent help (related) | SCRIE/DRIE Title 26 Ch. 7; Rental Assistance Voucher Program Title 26 Ch. 39 (enacted by L.L. 2026/126, **effective 1/26/2027, not yet in force**); CityFHEPS repair program 28 RCNY Ch. 60 | `nyc-adm-26-6**`, `nyc-adm-26-39**`, `nyc-rcny28-60-*` |
| Other Title 26 | Ch. 22 expiring affordable housing; Ch. 27 Mitchell-Lama development reporting; Ch. 2 relocation services; Ch. 13 certification of certain rent payment; Ch. 25 audits of certifications of correction; Ch. 34 fees on vacating | `nyc-adm-26-*` |


## Live fetch

| Source and endpoint | Access | Response time seen | Rate limits | Updates | Terms on programmatic use | Verdict |
|---|---|---|---|---|---|---|
| amlegal NYC Admin Code and RCNY: `https://codelibrary.amlegal.com/api/render-section/newyorkcity/latest/<NYCadmin\|NYCrules>/<chapter doc id>/<record index>/` (JSON with `title` and `html`); table of contents at `/api/toc-chain/<code uuid>/<doc id>/` | Browser only. Cloudflare challenge for scripts; a plain fetch was refused here | 70-100 ms per record from inside the browser | None stated; we used 1 request/s per tab | amlegal says "current through Local Law 2026/164"; it updates as local laws are codified | Not found (amlegal's terms page wasn't located); the bot check signals scripts aren't welcome | no |
| NYC Council Legistar: `https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=...` and attachments `View.ashx?M=F&ID=...&GUID=...` (local laws as enacted, PDF) | Plain fetch | 0.5 s per page or PDF | None stated | As the Council acts | Not stated on the pages fetched. The Legistar Web API (`webapi.legistar.com/v1/nyc`) returned 403 without a token | possible (HTML scraping, as-enacted text only) |
| intro.nyc (unofficial mirror of Council data): `https://intro.nyc/local-laws/<year>-<number>` returns the as-enacted local law PDF; `https://intro.nyc/<intro>-<year>` is the bill page with its Legistar link | Plain fetch | 0.1-0.3 s | None stated | Follows Legistar | Not checked; secondary source | possible (secondary; for finding Legistar records and pending amendments) |

## Counts

Manifest: 965 items (admin-code-other 297, elec 68, fc 64, healthcode 34, hmc 216, ll 3, rcny01 1, rcny03 5, rcny15 12, rcny24 14, rcny28 236, rcny47 15). Per-source counts are in `local/tools/build_report.txt` (per source: records fetched, files written, missing idx, hash mismatches), which `build_law.py` regenerates.
