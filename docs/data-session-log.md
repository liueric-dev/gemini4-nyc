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

## Handoff to gemini-data-fable (11:24)

Additions since about 08:18. It doesn't repeat the sections above, `data/SUMMARY.md`, `scoring-rules.md`, `freeze.json` or `freeze-addendum.json`.

### 1. Decisions and events since 08:18

- **med-0820:** still undecided (keep as A, or drop). It's excluded until Eric answers.
- **med-0188:** Eric confirmed `leak` at about 07:57 ("yea sounds good" to the whole mapping table: 0188 leak, 0309 peeling-paint, 0526 none, 0749 window, 0672 drop). It's recorded in the addendum.
- **Commits:**
  - Eric asked that nothing be marked "pre-event", so that wording was removed from the commit messages.
  - He then asked for every timestamp inside the data to be changed to the submission time. I declined: it would falsify the `retrieved` provenance and the freeze proof, and conflicts with the rule that judges must be able to tell what was made at the event. He agreed to squash instead.
  - Result: one commit, `2305aaa` (11:09), pushed to **https://github.com/liueric-dev/gemini4-nyc**. It's public; Eric created it. Then `ad2acc0` (the team brief). No timestamps inside the files were changed.
- **Team:** two teammates joined, both non-technical.
  - `docs/team-brief.md` was written for them, Notion-importable, deliberately long at Eric's request.
  - Only `liueric-dev` is a collaborator. The teammates aren't added yet; I offered to add them if Eric gives their usernames.
  - They need their own `.env` (key names below), shared privately.
- **Teammate's agent says it's "restricted to docs and data":**
  - Diagnosed: nothing in the repo restricts it (no CLAUDE.md, no `.claude/`, no settings). The cause is that `data/README.md` reads as instructions to agents (line 3 "Instructions for the sessions and agents that gather the data", line 21 "Do not commit anything", plus the workstream write rules), and it never says collection is over. On top of that, the docs reference `~/hackathons/...` paths and uncommitted files.
  - **Proposed and awaiting Eric's OK:** a "Collection is finished; these rules were for the overnight agents; build and commit normally; `local/`, media and `~/hackathons/` paths exist only on Eric's machine" note at the top of `data/README.md` and the root `README.md`.
- **Discord #rules:** never read in this session.
- **Demo and design:** I gave Eric a next-steps list:
  1. baseline plus scoring script first
  2. the pipeline (observe, then Decisions API, then problem map lookup, then cited answer)
  3. the demo UI
  4. building lookup (optional)
  5. the full evaluation and failure write-up
  6. a one-minute video with real NYC footage, README, public repo, rehearsal

  No design decisions were made. Eric plans to do the roadmap and system design with you.

### 2. Repo and commit state

- **Committed:** `.gitignore`, `README.md` (one line: `# gemini4-nyc`), `docs/` (5 files including `team-brief.md`), and `data/` (2,401 files): everything not ignored.
- **The `.gitignore` already contains:**
  - `.env`
  - `data/*/local/`
  - `data/media/fallback/`
  - `data/.venv/`
  - `data/media/images/`
  - `data/media/videos/`
  - `data/open-data/raw/od-ncei-ghcnh-usw00094728-2026.psv` (36 MB, can be re-downloaded)
  - `.claude-transfer/`
- **Never add:**
  - `.env`
  - any `local/` folder
  - `data/media/fallback/` (copyrighted)
  - `data/media/images/` and `videos/` (1.2 GB; Pexels, Pixabay and NC/ND licences unsure)
  - `.claude-transfer/`: created 08:50, not by this session; it holds `images.tgz` at 113 MB, over GitHub's 100 MB file limit, and `text.tgz`
- **Uncommitted right now:** only this handoff section in `docs/data-session-log.md`.
- **Key scan before the push:** none of the five key values appears in any committed file. Key names in `.env`: `NYSENATE_API_KEY`, `NOAA_CDO_TOKEN`, `HUD_API_TOKEN`, `NYC_OPENDATA_APP_TOKEN`, `PIXABAY_API_KEY`.

### 3. Scripts

| Script | Command (from the repo root) | Effect | Safe to re-run? |
|---|---|---|---|
| `data/media/split.py` | `python3 -I data/media/split.py [--dry-run]` | Rewrites `split` in `media/manifest.jsonl` (seed 20261121, by `group_id`, about 30% test; public and fallback split separately) | **No.** It would undo the 8 groups moved by `select_review.py` and change test membership. `--dry-run` only prints. |
| `data/media/select_review.py` | `python3 -I data/media/select_review.py` | Moves dev groups to test in the manifest, and **overwrites `media/review/review_set.json`** | **Never.** It would break the frozen `review_set.json` hash. |
| `data/media/review/serve.py` | `python3 -I data/media/review/serve.py 8770`, then open `http://127.0.0.1:8770/review/index.html` | Local review page. Decisions go to `review/decisions.json`; Freeze writes `freeze.json` | Yes. Since `freeze.json` exists, it rejects writes with 409, so it's read-only now. |
| `data/law-nyc/local/tools/*` (`build_law.py`, `amlegal_extract.js`, `check_stage.py`, `pdf2txt.py`, `add_extra.py`) | Workstream 1 agent's tools; see `local/tools/AGENT_BRIEF.md` | Rebuild the law-nyc text from staged browser extracts | Not needed. Not committed (they're in `local/`). |

Other workstream agents left helpers in their own `local/` folders. None are needed.

**Python:**
- system `python3` (always run with `-I`)
- `data/.venv/` (Python 3.14, `pymupdf`), git-ignored, used only for PDF text

**Backups in `data/media/local/`:**
- `manifest.pre-split.jsonl`
- `manifest.pre-review-select.jsonl`
- `decisions.backup-0757.json` (202 entries, includes the label codes before the overwrite)
- `expected-outcomes.backup.csv` (EO-015 before the caulk change)

### 4. Processes

**Nothing started by this session is running.**
- Review server: stopped.
- My 10-hour `caffeinate`: stopped.
- All subagents: finished or stopped.
- All Chrome tabs: closed.

Two `caffeinate -i -t 300` processes seen at about 08:35 weren't started by this session; I left them alone.

### 5. Unfinished work

- **med-0820:** keep or drop.
- **The README note** for teammates' agents: awaiting Eric's OK.
- **Collaborators:** add the teammates, once Eric gives their usernames.
- **183 public media items** still have `license_check` "not yet checked". This only matters if media files are ever committed; they aren't.
- **Problem map review:** 20 rows with the class unsettled. HPD's § 27-2115(d) classification list is likely in the City Record from 1972 (City Record Online or a860-gpp.nyc.gov); not searched.
- **Other gaps:** no official Rent Stabilization Code; the HP OSC and petition aren't online; the HP fee isn't confirmed; RGB orders before 2026 (the plain download was denied by the session's permission check; not routed around).
- **Nothing promised to Eric is outstanding** beyond the items above.

### 6. Traps

- **`data/README.md` is written as orders to collection agents.** Agents reading it today will think they can't commit or can't touch the app (see section 1).
- **Manifests list files that aren't in the repo:**

  | Folder | Missing from the repo |
  |---|---|
  | `media/` | all 1,306 |
  | `process/` | all 936 |
  | `law-state/` | 459 |
  | `open-data/` | 31 |
  | `law-nyc/` | 0 |

  That's expected (licences and size). Each line keeps `source_url` and `sha256`.
- **Frozen files:** never edit `media/review/decisions.json` or `review_set.json`, or their hashes break.
  - Corrections go in a new addendum.
  - `scoring-rules.md` still says "DRAFT" in its title, but it's the frozen version (hashed in the addendum). Don't edit it.
  - `problem-map/expected-outcomes.csv` is hashed too. Change it only with a note, because rule 9 scores against it.
- **The stale-tab overwrite:**
  - The review page keeps an in-memory copy and POSTs the whole object on each save.
  - Any edit to `decisions.json` made while a review tab is open gets overwritten.
  - It's harmless now, because the server refuses writes after the freeze.
- **`expected-outcomes.csv` starts with a `#` comment line.** Skip it when parsing.
- **Ids starting `med-f`** are fallback items: copyrighted, local only, never in the headline.
- **Fetching:**
  - nyc.gov plain fetches are intermittently 403 (use the browser).
  - hcr.ny.gov works only with curl's default user agent.
  - nycourts PDFs come only through a same-site fetch plus download in Chrome.
  - amlegal and Westlaw are browser-only. Westlaw labels itself "Unofficial", so don't copy it in bulk.
- **Usage limit:** the shared account limit ran out from 02:20 to 06:00. Each collector agent used 340,000–530,000 tokens. Keep subagents few.

### 7. Eric's preferences (not recorded elsewhere)

- **Writing:** be verbose in documents for the team; they can trim them. The teammates are non-technical, and one uses Notion.
- **Data:** be persistent about getting it. But pause and check whether it's needed when token use balloons.
- **Evaluation:** whether a photo shows a home matters less than whether the model identifies the problem. Use home photos first and backfill from others.
- **Mould size class agreement** is his main metric of interest.
- **Videos** are test data for "can it handle video"; there's no time to show video in the demo.
- **Representativeness:** the public media isn't representative of NYC tenants. That's OK for the evaluation, but the demo should use real NYC apartment footage.
- **Pexels:** keep it ("it's a small amount").
- **Commits:** no "pre-event" labels.
- **Reviewer:** he likes running plans past you before building.
