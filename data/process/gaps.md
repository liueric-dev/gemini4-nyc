# Workstream 3 (process) gaps

Everything looked for but not obtained, plus decisions taken without the project owner. Updated during collection.

## Open decisions (for the project owner)

- **Licensing put every item in `local/`.** nyc.gov's terms of use (https://www.nyc.gov/main/terms-of-use, read 2026-11-21) say the site's text, graphics and other materials "are the property of the City of New York. All rights are reserved." So HPD, DOHMH, MOPT and 311 pages and PDFs are recorded as `copyrighted (City of New York ...)`, `committable: unsure`. hcr.ny.gov's disclaimer (https://hcr.ny.gov/disclaimer) and ny.gov's website disclaimer have no copyright or licence statement, so DHCR items are recorded as `license: unknown`, `committable: unsure`. nycourts.gov: no licence statement found (the privacy policy page and robots.txt were checked), so court items are also `unknown` / `unsure`. The README files these as `local/` (git-ignored). If the owner decides government forms and guides can be committed, move the files from `local/` to `raw/` and `text/` and update `raw_file`, `text_file` and `committable` in the manifest. No raw or text file outside `local/` has been written.
- The NY Courts DIY Forms page says commercial use of the DIY programs is prohibited and users must accept terms of use. That applies to the interactive DIY programs, which were not used. It is recorded in `proc-court-diy-forms-housing`.

## Not obtained

### HP action (Housing Part)
- **HP action Order to Show Cause and Verified Petition (blank forms): not online.** The NYC Housing Court page "Starting a HP Proceeding" (`proc-court-hp-starting`) says the clerk hands out the "Order to Show Cause Directing the Correction of Violations (HP Action)" and the "Verified Petition". Searched: the nycourts.gov forms index filtered by Landlord Tenant (20 forms), NYC Housing court type (32 forms), NYC Civil Court case type (70 forms), the DIY Forms page for NYC Housing Court (no HP program), the HP Cases index and all its subpages, and the Civil Court publications page. The HP materials that are online were collected: Tenant's Request for Inspection, CIV-LT-66 (serving the HP OSC and petition), CIV-LT-22 (restore for compliance hearing and civil penalties), and the fee waiver forms. Possible follow-ups: HPD's Housing Litigation Division pages, or nonprofit copies (Housing Court Answers), which would be `secondary` and `committable: no`.
- **HP index-number fee: no current official statement found.** The current NYC Housing Court fees page (`proc-court-fees`) has no HP line; its "Issue a notice of petition" fee is $45. The HP page sends readers to that fees page, and the current NYC Civil Court fees page was also checked. Older official court sources all say $45:
  - `proc-court-legacy-tenantsguide` (Civil Court tenants' Q&A, Nov 2016) says "pay the $45 court fee" for an HP case.
  - `proc-court-seminar-tenants-rights-transcript` (Civil Court seminar, 2007-04-25, given by a court clerk) says starting the case costs $45.00.
  - `proc-court-seminar-need-repairs-transcript` (Civil Court seminar, 2008-10-29, given by a Legal Aid lawyer) says "a $45 fee".
  - The current Getting Repairs video transcript (`proc-court-video-getting-repairs-transcript`) mentions the index-number fee and the fee waiver but gives no amount.
  - Treat $45 as stated by the court in 2007 to 2016, not confirmed current. The fee statute is workstream 2's.
- **CIV-LT-25 (requested 2026-11-21 06:00): not found.** No form page slug among the 954 `/forms/` pages in the nycourts.gov sitemap matched HP, repair or LT-25 terms (slugs are titles, not form numbers, so this is not conclusive). It is also not among the NYC Housing or NYC Civil Court forms listings, and not in the Internet Archive listing of the retired `/courts/nyc/housing/forms/` folder. The "Affirmation of Service" link on the Starting an HP Proceeding page leads to a listing of 6 generic service forms. Three were collected: CIV-RC-94 (personal delivery), CIV-RC-95 (other than personal delivery), CIV-GP-11 (by mail). A full scan of all 954 form pages for form numbers was started and then stopped to save time.
- Not searched (deprioritised by the coordinator on 2026-11-21 at about 06:10): official court or HPD pages on constructive eviction, and on whether RPL § 223-b retaliation protection covers NYCHA tenants.
- "Getting Repairs and Services" video and transcript (Civil Court publications page) not downloaded. The transcripts are `/media/NNNN` links that redirect to webfiles.nycourts.gov, and it isn't recorded which transcript belongs to which video.

### RPAPL Article 7-A, 7-C, 7-D
- Per the workstream 2 (state law) collector, RPAPL § 796-a(4) excludes Article 7-C in NYC and § 797(3) bars Article 7-D cases in the five boroughs. The 7-C forms (UCS-LT11A to C) and 7-D forms (UCS-LT12A to E) were downloaded before that correction. They are kept, and their manifest notes say "NOT USABLE IN NYC".
- **RPAPL Article 7-A forms: none found online.** The NYC Housing Court "Article 7A Proceedings" page (`proc-court-7a`) is a short summary with no form links. The forms indexes above list no 7-A or administrator form usable in NYC. HPD's 7A Program page (`proc-hpd-7a-program`) was collected.

### DHCR
- No separate "rent history request" form was found. The forms page lists REC-1 "Request for Records Access" (collected). The rent-increases page says tenants "can request a rent history". The online route is NYS Rent Connect (rent.hcr.ny.gov), which needs a login and was not used.
- Online complaint filing through Rent Connect (RA-89, RA-81, RA-90, HHW-1 online versions): sign-in required, not used. The PDF versions were collected.
- hcr.ny.gov's robots.txt disallows `/search/`. The fact-sheet list was read from `/search/rental_housing_documents_by_type` (4 pages, 1 request per second) before robots.txt was checked. Only the fact sheets themselves (`/fact-sheet-N`, which are not disallowed) were saved. Logged for transparency.

### HP action: more alternatives tried
- An Internet Archive CDX search of the retired court directory `nycourts.gov/courts/nyc/housing/*` (about 2,500 archived URLs, 2004 to 2024) shows no HP Order to Show Cause or Verified Petition form either. The archived forms folder held only answer, service, OSC-instruction, poor-person and similar forms. This supports the court's statement that the clerk issues the HP papers.
- The same search found the retired `/courts/nyc/housing/pdfs/` folder. Its files are still served live at `www.nycourts.gov/legacyPDFs/courts/nyc/housing/pdfs/<name>.pdf`. 25 were fetched in Chrome (`proc-court-legacy-*`): the "Answer in Person" defense fact sheets, repairs and essential services, warranty of habitability, Section 8, Spiegel law, and the NYC tenants' Q&A guide (Nov 2016). They are dated 2004 to 2017, aren't linked from current pages, and are marked as possibly outdated. Also tried: two old court URLs linked from current HPD and HRA pages (`courts.state.ny.us/courts/nyc/housing/procedural_housing.shtml`, `nycourts.gov/COURTS/nyc/housing/welcome.shtml`). Both now give "Page not found".

### Other
- MOPT pages (`nyc.gov/content/tenantprotection/pages/...`) and the Tenant Resource Portal are empty JavaScript shells to a plain fetch. Their content was taken from the open NYC content API they load from (`apps.nyc.gov/content-api/v1/content/<site>/<slug>`), saved as JSON. That is the original source; the HTML shells were not kept.
- National Grid: the "Report a Gas Emergency" and "More Time to Pay" URLs (`nationalgridus.com/regionalized/...`) returned the same generic regional landing page to a plain fetch, so nothing was kept. Getting the NYC pages would need choosing a region in the browser. Not done (secondary source, low priority). Con Edison pages were collected.
- Dead links found on official pages: the HUD NSPIRE smoke alarm standard PDF linked from HPD's Section 8 Inspections page (hud.gov, 404), and a NYCHA HQS program update notice PDF (404). Not collected.
- HPD heat season magnet (`proc-hpd-heat-season-magnet`) and the HPD Underlying Conditions rule PDF (`proc-hpd-underlying-conditions-rule`) are image-only PDFs with almost no extractable text. No OCR tool is installed, so they were not transcribed.
- Two links on the HPD Clear Violations page point to a private HPD SharePoint (`nyco365-my.sharepoint.com/...Clearing-HPD-Violations_revised.pdf`, `violation-reissuance.pdf`). Not public, not fetched.

## README corrections

- **hcr.ny.gov is not reachable with a browser user agent.** With a Chrome user-agent string curl gets a Cloudflare 403 "Just a moment..." page. With curl's default user agent, plain fetch works (200). nyc.gov is the opposite: curl's default user agent gets a 403, and a browser user-agent string works.
- **nycourts.gov PDFs cannot be fetched with curl.** `www.nycourts.gov/media/NNNN` redirects to `webfiles.nycourts.gov/public/<yyyy-mm>/<file>.pdf`, and both hosts return the Cloudflare 403 page to curl. What worked: in the Chrome tab, `fetch()` the file from the same origin, bundle the bytes as base64 JSON, and save them with one `<a download>` per fresh tab. Chrome blocks a second automatic download in the same tab. Files are byte-for-byte originals. `www.nycourts.gov/legacyPDFs/...` PDFs worked the same way.
- The court forms pages are not "subpages of landlord-and-tenant-forms". That page links to the shared forms search (`nycourts.gov/forms?...field_case_type[1511]=1511`, 20 Landlord Tenant forms). Each form has a `/forms/<slug>` page whose PDF link is `/media/NNNN`.
- The README lists RPAPL 7-C and 7-D among the Housing Court forms to collect. Per workstream 2 they don't apply in NYC (see above).
