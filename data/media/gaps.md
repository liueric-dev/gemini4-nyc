# Media test set (workstream 5): gaps

Everything looked for but not obtained, and why. Interim; updated through the run.

## Targets not met or thin

Targets from the README not met by public items (as of 2026-11-21 02:18 EST):

- Downloadable videos: mold: got 2
- Downloadable videos: heat-hot-water: got 0

## Content that public sources don't have (searched, not found)

- **Real tenant footage and phone photos from NYC apartments.** Openly licensed photos of occupied NYC apartments with defects are rare. Most public problem photos show derelict or abandoned buildings, disaster-damaged homes (FEMA, Hurricane Katrina) or polished stock, and `residential` marks these. News videos of NYC apartments exist only on YouTube under standard licences (fallback, link-only).
- **Pests:** no live rat inside an apartment (rats are dead, in attics, or nestlings); no grease or rub marks, gnaw holes or nests in a home; no standalone roach egg cases or shed skins; no close-up of a clean mattress seam; only 5 NYC photos.
- **Heat:** thermometer photos showing a low indoor reading are scarce, and almost none tie the reading to a date and hour (needed for the day/night heat rule). No public photo of a tap-water thermometer showing a low hot-water temperature was found (see checklist counts).
- **Narrated videos and paired clips:** see checklist. One paired photo set was found (a bathroom ceiling before and after mould cleaning, `pair_id` `pair-sermoa-bathroom-ceiling`).
- **Long walkthroughs:** see checklist.

## Sources blocked, refused, or not usable

- **Pexels:** no API keys are issued, and the website returns 403 to scripts. The browser was used. The Pexels Terms of Service (pexels.com/terms-of-service) say "Data mining, extraction, scraping and the use of programs or robots for automatic data collection and/or extraction of digital data on the Service and/or the content available therein is strictly prohibited for all unauthorised purposes". This collection read Pexels search-page data with in-page scripts and downloaded preview images from the Pexels CDN until about 01:55, when the terms were read and all collectors stopped. **Open decision for the project owner:** whether to keep the Pexels items. They're marked `committable: unsure` and stored in `local/`.
- **25 Pexels photos** accepted by the detector/window/heat collector have no caption, title or photographer, because their search-page data wasn't saved before Pexels access stopped. Their `group_id` is per photo, so one photographer's photos could fall in both splits. Each page needs opening by hand.
- **Pixabay:** the photo and video pages return 403 to scripts. The licence summary page was read in the browser (see checklist). Item pages were not opened one by one. The licence is taken from the Pixabay API, whose documentation says results are released under the Pixabay Content License (`license_check: api-only`). The verifier should open these pages.
- **Wikimedia Commons:** image downloads returned HTTP 429 at first. The cause, confirmed in the 429 message and on mediawiki.org "Common thumbnail sizes", was that the collector requested a non-standard 800 px thumbnail. Wikimedia rejects direct requests that aren't a standard size (20, 40, 60, 120, 250, 330, 500, 960, 1280, 1920, 3840 px). The tool was switched to 1280 px and failed downloads were retried. Images saved earlier are Commons thumbnails (800 px rendition), not originals. Some candidates were never downloaded and were skipped.
- **Federal sources:** fema.gov/multimedia-library returns 403 to scripts. DVIDS search returns an empty 202 (bot check) to scripts. CDC PHIL search is a server-side form that plain fetches can't drive (detail pages do show a public-domain notice). hud.gov Healthy Homes has no usable photo library. FEMA, NIST and other federal photos were reached through Wikimedia Commons instead.
- **DVIDS videos** (public domain per each page): the official Download button needs a login, so the video collector saved the stream that the page's own player serves to anonymous visitors. No login was used. **Open decision for the owner:** whether that method is acceptable.
- **EPA Mold Image Library:** the page says the photos "may be used for presentations and educational purposes without contacting EPA". That isn't a public-domain statement, so the 94 EPA images stay in the fallback set.
- **YouTube news videos** (playbook `videos.json`): YouTube blocked downloads. They're recorded link-only in the manifest as fallback items (`link_only: true`), with unverified caption-based time ranges. They can't be scored.
- **Search quality:** Pixabay is poor for housing defects ("mould" returns mouldy bread and fruit; "ceiling stain" returns stained glass; "water damage" gave 2 relevant hits of 79). Openverse full-text search matches unrelated words (molding, hood moulds, the town of Mold in Wales, the band Slumlord) and needed tag filtering. Openverse anonymous limits: 20 requests/min, 200/day.

## Labels and data quality to review

- All labels are drafts by the collector agents (no Gemini). The owner must review every label, especially test-split items, before they're frozen.
- `draft_hpd_orders` lists candidate HPD order numbers per problem type, drawn from `open-data/text/od-hpd-violation-types.csv` (keyword match on order wording, read by the collector). It isn't a verified mapping; the problem map (workstream 6) should settle it.
- Mould area in `draft_facts` is a visual estimate from the photo, with no scale reference, and is unreliable.
- Fallback photo labels were inferred from the playbook caption or dataset class without viewing the images (`label_confidence: low`).
- Several Flickr items are CC BY-NC or BY-NC-ND (`committable: unsure`, in `local/`).
