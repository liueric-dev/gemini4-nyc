# Media test set (workstream 5): checklist

Updated 2026-11-21 02:18 EST. Counts are generated from `manifest.jsonl`. Labels are drafts and need the project owner's review.

## What this folder holds

- `manifest.jsonl`: one line per item, public items first (`med-0001`…), then fallback items (`med-f0001`… photos, `med-fv01`… link-only news videos).
- `images/`, `videos/`: public items whose licence allows a public repo (`committable: yes`).
- `local/images/`, `local/videos/`: public items with `committable: unsure` (Pexels, Pixabay, CC NC/ND, GFDL) and any file over 50 MB. Git-ignored.
- `fallback/`: copyrighted playbook items, local evaluation only, git-ignored, in the playbook's source folders.
- `split.py`: dev/test split by `group_id`, fixed seed, about 30% of groups in test.

Extra manifest fields beyond the README: `license_url`, `author`, `search_query`, `candidate_id` (collector's working id), `license_check` (result of checking the licence against the source page), and for fallback items `fallback`, `link_only`, `playbook_flags`, `playbook_section`, `playbook_context`.

## Do first: status

Core-type photos, no-problem photos and look-alikes from public, openly licensed sources were collected first. Smoke/CO detector, window and heat photos started later and came from scarcer sources (see the counts below).

## Targets versus what we got (public items only; fallback items don't count)

"Committable yes only" counts what survives if the `unsure` items (Pexels, Pixabay, CC NC/ND, GFDL, unconfirmed) are dropped. "Residential yes" counts items whose `residential` is `yes`: clearly a home, an apartment, or an apartment building's common area.

| Target (README) | Wanted | Got (public, all licences) | Met? | Residential yes (all) | Committable yes only | Committable yes, residential yes |
|---|---|---|---|---|---|---|
| Core-type photos: leak | 12 | 42 | yes | 30 | 28 | 21 |
| Core-type photos: mold | 12 | 38 | yes | 19 | 27 | 18 |
| Core-type photos: peeling-paint | 12 | 52 | yes | 17 | 25 | 13 |
| Core-type photos: wall-ceiling-damage | 12 | 55 | yes | 30 | 35 | 24 |
| Core-type photos: pests | 12 | 39 | yes | 31 | 12 | 9 |
| Core-type photos: smoke-co-detector | 12 | 22 | yes | 8 | 13 | 4 |
| Core-type photos: window | 12 | 37 | yes | 2 | 10 | 0 |
| Core-type photos: heat-hot-water | 12 | 17 | yes | 13 | 12 | 9 |
| No-problem photos | at least 25% of 555 photos = 139 | 170 (31%) | yes | - | 54 of 212 committable photos (25%) | - |
| Look-alike photos: leak | 3 | 8 | yes | - | 0 | - |
| Look-alike photos: mold | 3 | 15 | yes | - | 2 | - |
| Look-alike photos: peeling-paint | 3 | 3 | yes | - | 0 | - |
| Look-alike photos: wall-ceiling-damage | 3 | 10 | yes | - | 4 | - |
| Look-alike photos: pests | 3 | 14 | yes | - | 4 | - |
| Look-alike photos: smoke-co-detector | 3 | 3 | yes | - | 2 | - |
| Look-alike photos: window | 3 | 6 | yes | - | 1 | - |
| Look-alike photos: heat-hot-water | 3 | 19 | yes | - | 7 | - |
| Extended-type photos: exposed-wiring | 3 | 10 | yes | 6 | 2 | 2 |
| Extended-type photos: plumbing-fixture | 3 | 14 | yes | 8 | 2 | 1 |
| Extended-type photos: radiator | 3 | 4 | yes | 2 | 2 | 2 |
| Extended-type photos: flooring | 3 | 6 | yes | 1 | 0 | 0 |
| Extended-type photos: blocked-exit | 3 | 5 | yes | 1 | 0 | 0 |
| Extended-type photos: door-lock | 3 | 5 | yes | 1 | 1 | 0 |
| Extended-type photos: garbage | 3 | 5 | yes | 0 | 0 | 0 |
| Extended-type photos: appliance | 3 | 8 | yes | 4 | 4 | 3 |
| Extended-type photos: elevator | 3 | 6 | yes | 0 | 4 | 0 |
| Extended-type photos: stairs | 3 | 7 | yes | 0 | 2 | 0 |
| Extended-type photos: no-water-sewage | 3 | 7 | yes | 7 | 0 | 0 |
| Downloadable videos: leak | 3 where any exist | 7 | yes | 1 | 4 | 0 |
| Downloadable videos: mold | 3 where any exist | 2 | no | 0 | 2 | 0 |
| Downloadable videos: peeling-paint | 3 where any exist | 3 | yes | 0 | 2 | 0 |
| Downloadable videos: wall-ceiling-damage | 3 where any exist | 10 | yes | 1 | 5 | 0 |
| Downloadable videos: pests | 3 where any exist | 8 | yes | 2 | 4 | 2 |
| Downloadable videos: smoke-co-detector | 3 where any exist | 6 | yes | 0 | 6 | 0 |
| Downloadable videos: window | 3 where any exist | 4 | yes | 1 | 0 | 0 |
| Downloadable videos: heat-hot-water | 3 where any exist | 0 | no | 0 | 0 | 0 |
| No-problem videos | some | 28 | yes | - | - | - |
| Look-alike videos | some | 10 | yes | - | - | - |
| Long walkthroughs (stress set, >= 2 min) | a few | 3 | yes | - | - | - |
| Narrated videos | any that exist | 11 | - | - | - | - |
| Paired items (same spot, different dates) | any that exist | 1 pair(s) | - | - | - | - |

## Counts

## Problem items per type (problem category; an item with two labels counts under both)

| Type | Target (photos) | Public photos | of which residential yes | of which confidence high/medium | Public photos dev/test | Public videos | Fallback photos | Fallback link-only videos |
|---|---|---|---|---|---|---|---|---|
| leak | 12 | 42 | 30 | 38 | 0 / 0 | 7 | 57 | 8 |
| mold | 12 | 38 | 19 | 37 | 0 / 0 | 2 | 262 | 6 |
| peeling-paint | 12 | 52 | 17 | 50 | 0 / 0 | 3 | 21 | 1 |
| wall-ceiling-damage | 12 | 55 | 30 | 53 | 0 / 0 | 10 | 47 | 4 |
| pests | 12 | 39 | 31 | 39 | 0 / 0 | 8 | 51 | 5 |
| smoke-co-detector | 12 | 22 | 8 | 19 | 0 / 0 | 6 | 0 | 0 |
| window | 12 | 37 | 2 | 35 | 0 / 0 | 4 | 0 | 0 |
| heat-hot-water | 12 | 17 | 13 | 12 | 0 / 0 | 0 | 0 | 4 |
| exposed-wiring | 3 | 10 | 6 | 10 | 0 / 0 | 0 | 0 | 0 |
| plumbing-fixture | 3 | 14 | 8 | 14 | 0 / 0 | 8 | 0 | 0 |
| radiator | 3 | 4 | 2 | 2 | 0 / 0 | 0 | 0 | 0 |
| flooring | 3 | 6 | 1 | 5 | 0 / 0 | 0 | 0 | 0 |
| blocked-exit | 3 | 5 | 1 | 4 | 0 / 0 | 0 | 0 | 0 |
| door-lock | 3 | 5 | 1 | 3 | 0 / 0 | 0 | 0 | 0 |
| garbage | 3 | 5 | 0 | 5 | 0 / 0 | 0 | 0 | 0 |
| appliance | 3 | 8 | 4 | 7 | 0 / 0 | 0 | 0 | 0 |
| elevator | 3 | 6 | 0 | 6 | 0 / 0 | 0 | 0 | 0 |
| stairs | 3 | 7 | 0 | 7 | 0 / 0 | 0 | 0 | 0 |
| no-water-sewage | 3 | 7 | 7 | 7 | 0 / 0 | 0 | 0 | 0 |

## Items by category, media type and split (public)

| Category | Photos dev | Photos test | Videos dev | Videos test | Link-only |
|---|---|---|---|---|---|
| problem | 0 | 0 | 0 | 0 | 0 |
| no-problem | 0 | 0 | 0 | 0 | 0 |
| look-alike | 0 | 0 | 0 | 0 | 0 |

Public photos: 555; no-problem photos: 170 (31%)
Public videos: 78 downloadable, total duration 3043 s
Fallback: 477 photos, 13 link-only videos

## Look-alikes by resembled type (from draft_facts text)

- leak: 8 photos, 2 videos
- mold: 15 photos, 0 videos
- peeling-paint: 3 photos, 4 videos
- wall-ceiling-damage: 10 photos, 2 videos
- pests: 14 photos, 3 videos
- smoke-co-detector: 3 photos, 0 videos
- window: 6 photos, 2 videos
- heat-hot-water: 19 photos, 0 videos
- appliance: 1 photos, 0 videos

## Sources (public)

- pexels, Pexels license: 234
- openverse-flickr, CC BY 2.0: 86
- openverse-flickr, CC BY-NC-SA 2.0: 50
- openverse-flickr, CC BY-SA 2.0: 41
- openverse-flickr, CC BY-NC 2.0: 34
- inaturalist, CC BY-NC: 29
- openverse-flickr, CC BY-NC-ND 2.0: 27
- commons, CC BY-SA 4.0: 22
- pixabay, Pixabay license: 19
- commons, public-domain: 17
- dvids, public-domain: 12
- commons, CC0: 9
- openverse-flickr, CC BY-ND 2.0: 8
- commons, CC BY 4.0: 7
- commons, CC BY-SA 3.0: 6
- commons, CC BY 2.0: 5
- commons, CC BY-SA 2.0: 5
- openverse-flickr, CC0 1.0: 3
- inaturalist, CC BY: 3
- commons, CC BY 2.5: 3
- inaturalist, CC BY-SA: 2
- commons, CC BY 3.0: 2
- commons, GFDL 1.2: 1
- commons, GFDL: 1
- commons, CC BY-SA 3.0 de: 1
- inaturalist, CC0: 1
- internet-archive, CC BY-NC-ND 4.0: 1
- internet-archive, CC0 1.0: 1
- internet-archive, CC BY-NC-SA 4.0: 1
- internet-archive, CC BY-NC-ND 3.0: 1
- internet-archive, CC BY 2.0: 1

committable: {'yes': 235, 'unsure': 398}
license_check: {'match': 290, 'not yet checked': 323, 'api-only': 19, 'unverified': 1}
conditions phone-quality: 292, polished-stock: 219
residential: {'unclear': 188, 'no': 30, 'yes': 359, 'other/derelict': 56}
groups: 469 public, 43 fallback


## Licences

Licences were checked against the source pages:
- Flickr pages (CC licence link), Commons (`LicenseShortName` from the file page's metadata), iNaturalist (photo `license_code`) and Internet Archive (`licenseurl`) were checked by script. Results are in each item's `license_check`.
- Pexels items: licence from the Pexels search-page data (`attributes.license` = "Pexels").
- Pixabay items: licence from the API. Item pages weren't opened (see gaps.md).

Can Pexels and Pixabay files go in a public repo unaltered? Both licences were read in the browser on 2026-11-21:
- **Pexels** (https://www.pexels.com/license/): "Don't redistribute or sell the photos and videos on other stock photo or wallpaper platforms." It also says "Don't sell unaltered copies of a photo or video, e.g. as a poster, print or on a physical product without modifying it first." Separately, the Pexels Terms of Service prohibit automated data collection for unauthorised purposes (see gaps.md).
- **Pixabay** (https://pixabay.com/service/license-summary/): "You cannot sell or distribute Content (either in digital or physical form) on a Standalone basis. Standalone means where no creative effort has been applied to the Content and it remains in substantially the same form as it exists on our website."
- **Decision:** a public repo of unaltered files is plausibly "distribution on a Standalone basis" (Pixabay) and close to redistribution as a collection (Pexels). So all Pexels and Pixabay items are `committable: unsure` and stored in `local/`. They remain usable for local evaluation. CC BY-NC / BY-NC-ND / BY-NC-SA Flickr items and GFDL items are also `unsure` (non-commercial terms versus a public hackathon repo; GFDL requires shipping the licence text). CC BY, CC BY-SA, CC0, public-domain and US-federal items are `committable: yes`, with the credit line in `attribution`.

## Dev/test split

`split.py` (seed 20261121) shuffles the `group_id`s and puts the first 30% in test. It retries with the same random generator until every core type has at least 3 test items and at least one dev item, and no-problem and look-alike items appear in both splits. Public and fallback items are split separately. The script prints the accepted attempt number. `group_id` is `<platform>:<photographer or uploader>` for public items, and the playbook source plus subfolder for fallback items. Exceptions: 25 Pexels items with no photographer recorded are grouped per photo (see gaps.md).

## Live fetch

Media is unlikely to be fetched live; brief notes from what this collection saw on 2026-11-21.

| Source and endpoint | Access | Response time seen | Rate limits | Updates | Terms for programmatic use | Verdict |
|---|---|---|---|---|---|---|
| Pixabay API `pixabay.com/api/` and `/api/videos/` | free key (`PIXABAY_API_KEY`) | search 0.3-1 s | 100 requests per 60 s per key (docs); results must be cached 24 h | continuous uploads | allowed, but the docs say the API is "made for real human requests", forbid systematic mass downloads and permanent hotlinking (download first) | possible (poor relevance for housing defects) |
| Pexels website `pexels.com/search/...` | browser only (no new API keys; site returns 403 to scripts); image CDN `images.pexels.com` works with curl | CDN 0.07-0.3 s | not stated for the website | continuous | no API access available; scraping the site is not an offered interface | no |
| Openverse API `api.openverse.org/v1/images/` | open API, no key | search 0.07-0.3 s; image download from the original host (Flickr) 1-250 s | anonymous: 20 requests/min burst, 200/day sustained (response headers); shared by everything on one IP | index refreshed from providers | open API intended for reuse; each item keeps its own CC license | possible |
| Wikimedia Commons API `commons.wikimedia.org/w/api.php` + `upload.wikimedia.org` | open API, no key | API 0.2-0.35 s | image downloads at non-standard thumbnail widths are rejected with HTTP 429; standard widths are listed at mediawiki.org "Common thumbnail sizes" (e.g. 960, 1280 px) | continuous | allowed with a descriptive User-Agent; per-file licenses | possible |
| iNaturalist API `api.inaturalist.org/v1/observations` | open API, no key | taxa 0.35 s; observations + downloads 3-30 s | none hit in ~45 calls | continuous | allowed; per-photo CC license codes | possible (pests only) |
