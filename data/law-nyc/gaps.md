# law-nyc gaps and decisions

Workstream 1 (NYC law). Collected 2026-11-21, New York time.

## Access and method

- **amlegal (codelibrary.amlegal.com) is browser-only.** A plain `curl` of its JSON API was refused by this machine's permission policy, and the README already lists the site as Cloudflare-blocked. All amlegal text was read in Chrome from the site's own `render-section` API (`/api/render-section/newyorkcity/latest/<code>/<chapter doc>/<record index>/`), one record (section or heading) at a time, 1 request per second.
- **No raw originals for amlegal items** (`raw_file` empty). Two ways to save the API JSON to disk were tried and dropped:
  - a POST to a local receiver on 127.0.0.1: Chrome held it behind a Local Network Access permission prompt, which was not accepted;
  - a clipboard write: it hung on a permission prompt too.
  The README says this case isn't a gap, but it means the text files are the only copy.
- **How the text got to disk.** The browser computed a SHA-256 of each record's whitespace-normalized text. Transcription subagents copied the text from `get_page_text` into staging batches (`local/stage/`). `local/tools/check_stage.py` recomputes the hash and only passes exact matches, and `local/tools/build_law.py` writes `text/` and `manifest.jsonl` from hash-matched records only. A whitespace or Unicode-normalization difference wouldn't show in the hash. Any other change in the words, punctuation or quotes would.
- **Paragraph structure:** one line per amlegal paragraph block. Indentation isn't kept. Tables are rows with cells joined by ` | ` (for example 28 RCNY § 18-01, § 18-02, § 18-04).

- **nyc.gov blocked plain fetches from this machine** (HTTP 403 for `www.nyc.gov/site/hpd/index.page` and HPD PDFs, checked at 01:05 and 01:31). The README says plain fetch works for nyc.gov. This workstream needed nyc.gov only for the HPD Tenant Bill of Rights, which workstream 3 already has.
- **The Legistar Web API** (`webapi.legistar.com/v1/nyc`) returned 403 without a token. The Legistar website itself works with a plain fetch.
- **Tool limits** that shaped the method: `get_page_text` truncates at 50,000 characters, so long sections (§ 8-107 at 124k, § 26-405 at 81k, 28 RCNY § 25-174 at 70k, § 27-2115 at 55k) were read in pieces and each piece hash-checked. `javascript_tool` output truncates at about 1,000 characters.

## Source problems copied as they appear (not fixed)

- NYC Admin Code § 27-2115 (civil penalties): the second subdivision (o)(5) stops mid-sentence at "...pursuant to section" on amlegal.
- § 27-2093.1: an editor's note says L.L. 2026/138 amends it effective 4/15/2027. That amendment isn't in the text yet. **Possibly superseded after that date.**
- § 27-2056.6.1 repeats a sentence of § 27-2056.6, run together with no space ("subsurface.The existence ...").
- Headings with stray spaces: "§ 27- 2017.4" and "§ 27- 2017.8". Ids are normalized to `nyc-hmc-27-2017-4` and `nyc-hmc-27-2017-8`.
- Typos on the source in RCNY 28 chapters 55 and 46 (Spanish text), and form blanks with run-together labels in the chapter 54, 55, 56 and 16 appendices.

## Currency flags

- amlegal says it is current through Local Law 2026/164 (README). Every amlegal item is `version: current-consolidated`.
- HMC Article 15 (§§ 27-2056.21 to 27-2056.24, steam radiator inspection) was added by L.L. 2025/151, effective 5/7/2026.
- § 27-2030 (cooling systems) was added by L.L. 2026/023.
- `effective_date` is the latest "eff. M/D/YYYY" in each section's history note. Sections with no amendment history (original 1967 text) say `unknown`. Most RCNY history notes use "City Record ... eff. ..." in the same format.

## README pointers checked

- The HMC is Admin Code Title 27, Chapter 2: confirmed (amlegal doc 0-0-0-60027, §§ 27-2001 to 27-2154, 252 records incl. headings).
- Local Law 55 of 2018 is codified in the HMC: confirmed. The history notes of §§ 27-2017.1 to 27-2017.12 cite L.L. 2018/055.
- Local Law 1 of 2004 is codified in the HMC: confirmed. HMC Article 14 cites L.L. 2004/001 (§§ 27-2056.1 ff.).
- RCNY Title 28 is HPD: confirmed. It has 63 chapters, numbered 1-64 with **no Chapter 23**.
- The FARE Act is Local Law 119 of 2024 (Int. 360-A), codified as Admin Code Title 20 Chapter 4 Subchapter 15 (§ 20-699.20 ff.). The README's "2024" is the year enacted. Per § 2 of the law, it took effect 180 days after it became law; it was returned unsigned on 12/16/2024.
- § 26-521 (unlawful eviction) is in Title 26 Chapter 5: confirmed.
- Right to Counsel § 26-1301 ff. is in Title 26 Chapter 13 "Provision of Legal Services in Eviction Proceedings": confirmed. amlegal has two different chapters both numbered 13 in Title 26 (the other is "Certification of Certain Rent Payment").
- Rent Stabilization Law is Title 26 Chapter 4 and rent control is Title 26 Chapter 3: confirmed from the amlegal table of contents.
- Health Code articles: window guards are Article 131 (Buildings, § 131.15), pests Article 151, and lead Article 173 (Hazardous Substances). All three are collected.
- "Tenant Bill of Rights": no Admin Code section creates a general tenant bill of rights. What exists is § 21-149 (supportive housing bill of rights, L.L. 2022/015), § 27-2009.2 (safe construction bill of rights) and HPD's non-statutory Tenant Bill of Rights guidance, which workstream 3 collected as `proc-hpd-tenant-bill-of-rights*`. Here, plain `curl` of nyc.gov HPD PDFs returned 403, so this workstream didn't re-download them.
- Tenant protection plans are **§ 28-104.7.16**, not § 28-104.8.4. § 28-104.8.4 is "Application to demolish a building after vacate order". The README gave no number; the first guess was ours and was wrong.
- After-hours construction work is governed by Noise Code §§ 24-222 and 24-223. Construction Code § 28-105.12.5 requires compliance with them. No Article 105 permit section covers after-hours work directly.
- Local Law 152 of 2016 gas piping inspections are Title 28 Article 318, plus DOB rule 1 RCNY § 103-10.
- Fire Code Ch. 10 (Means of Egress) is mostly "Reserved" stubs. The substantive text is FC 1001, FC 1025.1, FC 1025.4-1025.5 and FC 1027 (maintenance of the means of egress).
- CCHR rules (47 RCNY) have no separate rules on housing reasonable accommodation, cooperative dialogue or source of income. Those are subdivisions of Admin Code § 8-107.
- Window guards in the HMC are § 27-2043.1, confirmed from the text.

## Pending amendments (law changes not yet in the consolidated text)

- L.L. 2026/138 makes the certification-of-no-harassment pilot permanent and amends § 27-2093.1. Effective 4/15/2027 (the as-enacted PDF is collected as `nyc-ll-2026-138`).
- L.L. 2026/042 amends Construction Code §§ 28-304.6.6.2 and 28-304.8 (elevators), effective 1/1/2027 (`nyc-ll-2026-042`), and parts of the Electrical Code.
- Title 26 Ch. 39 (Rental Assistance Voucher Program, L.L. 2026/126) is in the consolidated code but effective 1/26/2027.
- §§ 26-601 and 26-618 (SCRIE/DRIE) amendments are effective 7/22/2026 (already in force); 47 RCNY §§ 1-11 and 1-23 amendments are effective 10/30/26.
- The as-enacted PDFs of L.L. 2026/138 and 2026/042 come from intro.nyc, an unofficial mirror, and are marked `secondary`. The official Legistar files weren't located in the time spent. L.L. 2024/119 (FARE Act) is from Legistar (official).

## Not collected

- **Raw amlegal JSON or HTML** (see Access and method).
- **RCNY Title 28 chapters outside tenant conditions:** 1, 2, 4-8, 19, 22, 26-35, 37-39, 41, 42, 49-51, 57, 58 and 61-64 (tax exemptions and abatements, loan and finance programs, city-owned property sales, inclusionary housing, campaign finance and similar). They don't govern conditions in an apartment. There is no Chapter 23.
- **NYC Building Code** (Admin Code Title 28 Ch. 7) egress chapter for new construction, which is large. Egress *maintenance* is covered by Fire Code FC 1027 and the HMC.
- **NFPA 70 (National Electrical Code) base text:** amlegal carries only NYC's amendments, and the NEC itself is copyrighted by NFPA. Only the NYC administrative sections (EC 80-87) and a few dwelling-related amendments were collected.
- **Most of Admin Code Title 17 Ch. 1, Title 20 Ch. 4, Title 8 Ch. 1 and Title 28 Ch. 1 and 3:** only the tenant-relevant sections were taken (listed per item in `local/tools/build_report.txt` and `manifest.jsonl`).
- **As-enacted copies of older local laws** (L.L. 2004/001, L.L. 2018/055 and others): intro.nyc serves them, but they are superseded by the consolidated text, so they were skipped.
- **Multiple Dwelling Law, RPL, RPAPL, Rent Stabilization Code:** state law, workstream 2.

## HPD violation classification list (HMC § 27-2115(d)): not found

Searched 2026-11-21, 06:00-06:20 New York time. The problem map can't settle the class for orders such as 501, 506, 507, 508, 583 and 689, which HPD issues as A, B or C.

**What § 27-2115(d) requires** (read from `nyc-hmc-27-2115`): by 1 Sep 1972, HPD was to classify all MDL and HMC violations as non-hazardous, hazardous or immediately hazardous, get approval from the advisory council to the Housing Part of Civil Court, and publish the list in the **City Record**. It may modify the list later after publication and a hearing. The list is therefore a City Record publication, not a codified rule.

**Searches, none of which found the list:**
- **amlegal RCNY Title 28.** All 23 Do-first chapters and chapters 3, 14, 21, 24, 43, 52 and 60 are collected; their texts contain no classification list. The remaining 33 chapters were also scanned in the browser for "27-2115", "classification of violation", "non-hazardous", "immediately hazardous" and "class A/B/C violation". The scan was stopped partway, when the coordinator limited the search to 20 minutes. Chapters 1, 2, 4-8, 19, 22 and 26-28 and part of 29 (133 records) were covered; 29-64 were not finished, and only passing mentions turned up (§§ 5-05, 8-01, 8-03, about tax and loan programs). No RCNY section implementing § 27-2115(d) was found.
- **HPD website, read in Chrome** (plain fetch returns 403):
  - `code-enforcement.page` lists the 9 conditions always cited on inspection.
  - `report-a-maintenance-issue.page` and `penalties-and-fees.page` give correction periods by class: A 90 days; B 30 days; C 21 days for lead, window guards, mold, mice/cockroaches and rats; 14 days for self-closing doors; immediate for heat and hot water; 24 hours for all other C. `penalties-and-fees.page` also gives civil penalties by class.
  - `clear-violations.page` gives the class definitions A/B/C/I.
  - `html/hpd/downloads/pdf/code-enfor-booklet-single-pg-10-25-06-blue-ver.pdf` is a 2-page printout of the Clear Violations page, not a list.
  - None of these has a condition-by-class or order-by-class list. All four pages are already in `process/` (`proc-hpd-code-enforcement`, `proc-hpd-report-maintenance-issue`, `proc-hpd-penalties-and-fees`, `proc-hpd-clear-violations`).
- **HPD Open Data violations data dictionary** (`open-data/raw/od-hpd-violations-dict-hpd-code-violations-data-dictionary.xlsx`). The "Order Number" sheet has the columns Order Number, Full Description, Category, Short Description and MD/PD, with **no class column**. Orders 501, 506, 507, 508, 583 and 689 are all listed without a class. The "Column Information" sheet defines Class only generally: A non-hazardous, B hazardous, C immediately hazardous, I information.
- **Web search** for "classification of violations", "27-2115", "City Record" HPD and order-number-to-class tables found only secondary summaries.
- **City Record:** the 1972 publication and any later modifications weren't located online in the time allowed. The City Record Online (CROL) archive and the Government Publications Portal (a860-gpp.nyc.gov) weren't searched; they are the next places to look.

**Official class rules that do exist in collected files (use these in the problem map):**
- HMC sections that fix the class in the text: § 27-2017.3 (mold, class set by area and unit count), § 27-2017.4 (pests), § 27-2030, § 27-2041.1, § 27-2043.1 (window guards), §§ 27-2046.3 and 27-2046.4, the lead sections (§§ 27-2056.2, 27-2056.6, 27-2056.6.1, 27-2056.7, 27-2056.8, 27-2056.17), and § 27-2115 (harassment under § 27-2005 d is class C; heat; correction periods).
- RCNY 28: §§ 11-01, 17-03, 25-101, 36-03, 44-01 and 44-02.
- Rent-impairing violations (MDL § 302-a) have an official HPD list in **28 RCNY § 25-191** (`nyc-rcny28-25-191`).
- For everything else, the empirical order-and-class distribution from the HPD violations dataset (workstream 4, `od-hpd-violation-types-*`) is the only source. Treat class as fact-dependent, noting that one order number can be issued as A, B or C.
