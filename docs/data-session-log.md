# Data session log (Nov 20–21, 2026)

What the data session ("gemini-data") did, what was decided, and what is still open. For the data itself, see [../data/SUMMARY.md](../data/SUMMARY.md). For the collection spec, see [../data/README.md](../data/README.md).

## Timeline

| Time (NY) | What happened |
|---|---|
| Nov 20, evening | Reviewed `data/README.md` against `plan.md`. Added priority order, building data, NYCHA, forms, media split and labels, and fixed citation errors. Merged proposals from the planning session and the reviewer session. |
| Nov 20, late | Added API keys (`.env`, git-ignored: Senate, NOAA, HUD, NYC Open Data, Pixabay; Pexels issues none). Eric allowed Chrome for sites that block scripts (Cloudflare on amlegal, nycourts, Westlaw, the rules site). Tested both. |
| Nov 21, 00:35 | Five collector agents launched, one per workstream. The reviewer session `gemini-data-fable` checked output about every 30 minutes, and its corrections were applied. |
| 00:43–02:20 | State law, NYC law, process and open data finished their first-tier items. The problem map agent drafted from them. |
| 02:20–06:00 | The account usage limit stopped everything. |
| 06:00–06:30 | Wrap-up only, to save quota. Last follow-ups: § 23-502 and the HPD classification list (not found); CIV-LT-25 (not found); HP fee. |
| 06:20 | Ran `media/split.py`. Wrote `data/SUMMARY.md`. Timed the live fetches. |
| 06:45–07:00 | Agreed the review set with Eric and the reviewer. `media/select_review.py` picked 203 items. Built the review page (`media/review/`). |
| 07:00–08:03 | Eric reviewed all 203 items. The caulk question was researched and decided. **Labels frozen at 08:03:23.** |

## Decisions Eric made

- **Collection:** collect fresh. The October projects (`~/hackathons/tenant-advocate`, `~/hackathons/daytona-hackathon-tenant-advocate`) were not used, and can be compared afterwards.
- **Media sources:**
  - Public and licensed first. Copyrighted fallback (the playbook test set) is local only, kept out of the headline number, and doesn't count toward targets.
  - Pexels items are kept, even though they were gathered through the website.
- **Test set:**
  - Built licence-first, then residential-first, with no confidence filter.
  - 10 photos per core type, with mould raised to 30 (Eric's main metric) and heat at 6.
  - All 92 test negatives (no-problem photos and look-alikes).
  - The 24 test videos are test data for "can it handle video". They're not shown in the demo.
- **Review page:** shows the draft label. On mould photos, the size hints stay hidden until a bin is picked.
- **Caulk:** surface mould on intact tile, grout or caulk is the tenant's cleaning duty (HMC § 27-2012(a)), not an owner mould violation. Damaged caulk is owner repair (HPD order 502). Mould from behind, or recurring, is a mould hazard (550, sized by area). HPD's data shows about 1,900 Class A "cleanse" orders (553) for these cases. Applied in `media/review/scoring-rules.md` (rule 6) and in `problem-map/expected-outcomes.csv` (row EO-015).
- **Representativeness:** the public media is mostly renovations, abandoned buildings and stock photos, not NYC tenant photos. That's acceptable for the evaluation if the write-up states it. For the demo, use real NYC apartment footage, ideally filmed live.

## What exists now

| Where | What |
|---|---|
| `data/law-nyc/`, `law-state/`, `process/`, `open-data/` | 967 / 763 / 468 / 276 items, each with `manifest.jsonl`, `checklist.md` (including a Live fetch table) and `gaps.md` |
| `data/problem-map/` | DRAFT: `problem-types.md`, `expected-outcomes.csv` (92 rows; only EO-015 has been decided by Eric), `escalation.md`, `gaps.md` |
| `data/media/manifest.jsonl` | 1,319 items: 829 public (739 photos, 90 videos) and 490 fallback. Split by group: 474 test and 845 dev from `split.py`. `select_review.py` then moved 8 dev groups (13 items) to test, giving 487 test and 832 dev (public: 258 test, 571 dev) |
| `data/media/review/` | `review_set.json` (203 items), `decisions.json` (Eric's labels), `freeze.json` (08:03:23, with checksums), `scoring-rules.md` (10 rules), `serve.py` and `index.html` (the review page) |
| `data/media/local/` | Backups of the manifest before the split and before the selection, plus backups of decisions and expected outcomes |

**Review results:**
- **Frozen `decisions.json`:** 194 right, 5 wrong, 4 dropped (two watermarks, an unplayable video, a short-clip video). Mould bins: A 11, B 6, C 7, can't tell 6, surface only 1.
- **`freeze-addendum.json` (08:20):** holds decisions the owner confirmed before the freeze that a stale review tab overwrote. It adds label codes for the 5 wrong items (med-0188 leak, med-0309 peeling-paint, med-0526 none, med-0749 window) and drops med-0672 (cause not visible). It also records the hashes of `scoring-rules.md` and `expected-outcomes.csv`.
- **Pending owner decision:** med-0820 is marked right with mould bin A, but carries the drop reason "very ambiguous". It's excluded until decided.
- **Result:** 197 scored, 5 dropped, 1 pending. The scoring script reads `decisions.json` and then the addendum.

## Findings that shape the design

- **The law is too large for the prompt.** It's about 6 million characters (about 1.5 million tokens). Use the problem map to look up the 20–50 relevant sections by id, put only those in the prompt, and reject any citation outside that set.
- **The camera suits some problems far better than others.** Strong: mould (class set by area), leaks, peeling paint and plaster, pests, windows and window guards, detectors. Weak: heat (34% of HPD complaints, but the camera only reads a thermometer; it needs the time plus the outdoor temperature).
- **Live fetch is fine for** the Senate API, eCFR, GeoSearch, HPD violations, complaints and registrations by BBL (0.2–3.8 s), PLUTO, HUD FMR, and NWS (last 7 days only). Not for amlegal, nycourts or Westlaw (browser only), so use the collected copies.
- **Demo buildings:** five buildings in `open-data/text/od-demo-*.md` (pre-1960, rent-stabilized, NYCHA, a 1–2 family house, and one under a vacate order).

## Still open

1. **Commit:** not done yet. Plan: commit the manifests, checklists, gaps files, the problem map, the review set and decisions, the freeze record, the scoring rules and the scripts. Add `data/media/images/` and `data/media/videos/` to `.gitignore` first. Never commit `local/` or `fallback/`.
2. **Problem map review:** 20 rows have the class unsettled and 13 are unsettled overall. The big unknown is HPD's violation classification list (HMC § 27-2115(d)), published in the City Record in 1972 and not yet found; check City Record Online or a860-gpp.nyc.gov.
3. **Other gaps:**
   - no official full copy of the Rent Stabilization Code (only Cornell LII, secondary)
   - the HP Order to Show Cause and Verified Petition aren't online
   - the HP fee ($45 in older sources) isn't confirmed current
   - 183 media items have unchecked licences
   - there's no narrated video
4. **Demo footage:** real NYC apartment footage, ideally filmed live at the event.
5. **Running processes:** the review server on port 8770 and `caffeinate` (10 hours, started about 01:00). Stop both when they're no longer needed.
6. **Quota:** the shared usage limit ran out in under 2 hours overnight. Keep subagents few.
