# Handoff: where the build stands (Nov 21, 15:40)

Written by the session that built the backend, the evaluation and the live front end, for whoever continues. Submission is due at 17:00.

## State in one paragraph

The app works end to end, locally and hosted. A tenant gives an address and a photo or video; the app reports the problem, the violation class, the landlord's deadline and the quoted law; it answers typed questions, drafts the letter and 311 text, offers a Shopify fix-it kit for tenant-duty problems, and builds a case file with a hosted agent. Everything is committed and pushed. Hosted at https://gemini4-nyc.onrender.com (auto-deploys on every push; `/api/health` shows the running commit).

## Do not change (the test results depend on these)

The frozen test set was run once. Changing any of the following makes the numbers in the README and on `/proof.html` untrue:
- the proposing prompt in `app/pipeline.py` (`propose`), and `PROPOSE_VERSION` in `app/config.py`
- the detection questions (`_detect_questions`) and `DEFINITIONS`
- `confirm`, `fact` and `video` in `app/thresholds.json`
- `MODEL_DESCRIBE` in `app/config.py`
- anything under `data/media/review/` and `data/problem-map/expected-outcomes.csv`

Safe to change: the screens, wording, the explanation and question-answering prompts, the letter, the agent's skill, the photo-quality check.

## Still to do before 17:00

1. **README:** add the team's names (placeholder near the top) and the hosted link.
2. **Rehearse the demo** end to end on Eric's laptop. Not done yet.
3. **One-minute captioned video.** Not started, as far as this session knows.
4. **Try a video upload through the page's + button.** Tested through the API and the page's rendering separately, never in one go. Sample: `data/media/samples/med-0422.webm` (takes about 35 s).
5. **Decide `med-0820`** (keep as mould bin A, or drop). It is excluded from scoring until decided.
6. **Discord `#rules`** has never been read by any session.
7. **Don't push during judging.** A push redeploys the hosted site and can interrupt it for a minute.

## Demo advice

- Present from the laptop (`make dev`, then http://localhost:5173). It is faster, has all 179 test photos and shows rent-stabilized status. The hosted site has 76 sample photos, can't show rent-stabilized, and on the free plan sleeps after about 15 idle minutes.
- A good path: type a problem, give an address (a judge's own works), "Pick a test photo", answer the question, open "See the rule", ask a typed question, "What do I do now?", then "Build my case file" (about 80 s, so start it early and come back).
- Demo with a photo. Video works but takes 35 s or more.
- The results page is `/proof.html`.

## What the numbers say (frozen test set)

- **Photos (175):** system 147 exactly right, baseline 145. System 27 wrong reports against 41, and 3 false alarms on 24 look-alikes against 7. Baseline finds more real problems (91 of 98 against 85).
- **Video (22):** system 17 exactly right with no wrong reports; baseline 14 with 5.
- **Mould size (24):** baseline agrees with the reviewer more (15 against 10); the system declines half the time, and is right 10 of 12 when it answers.
- **First design:** 110 of 175. The change to "a model proposes, the Decisions API confirms" is the main "what we changed" story.

Honest pitch: the same accuracy, far fewer false alarms, it says when it can't tell, and every quote is checked.

## How the front end is put together

The screens are the team's prototype (github.com/hey-niia/tenard) with the scripted chat replaced by live calls.
- **Edit:** `web/live/live.js` (all logic and views) and `web/live/extra.css`.
- **Never edit:** `web/index.html` and `web/public/app.js`. They are generated.
- **Rebuild:** `python3 web/assemble.py /path/to/tenard/index.html <their-commit>`.
- **When the design changes:** pull their repo, read `git diff` on `index.html`, run the assemble script (their CSS and icons come across by themselves), then port changes to views or cards by hand into `live.js`. Currently built from their commit `0a313b5`.
- `web/proof.html` is hand-written and standalone.

Deliberately left out of their mock-up because nothing is behind them: the microphone button, "Edit" on the letter, "Add" in the evidence checklist, two made-up cases in "Your cases", their six sample images.

Still scripted (the team's walk-through, not data): the Dec 5 / Dec 18 / January time-skips, the evidence checklist's item list, the opening prompt for each problem type.

## Where things are

| Path | What |
|---|---|
| `app/pipeline.py` | propose, confirm, decide, explain, check; `ask` (typed questions); `facts_from_note` |
| `app/db.py`, `app/rule_conditions.json` | decision matrix lookups; hand-written conditions for the 92 rules |
| `app/building.py` | address to building facts (NYC Open Data) |
| `app/video.py` | video by frames |
| `app/letter.py` | letter and 311 text, filled in by code |
| `app/case_agent.py`, `agent/` | Managed Agents case file run, its skill and record script |
| `app/shop.py`, `app/diy_kits.json` | Shopify fix-it kits (built by the `shopify-fix-it-kits` session) |
| `app/main.py` | every endpoint, the static pages, the hourly caps |
| `eval/` | `run.py`, `run_video.py`, `tune.py`, `report.py`, `results/` |
| `docs/api.md` | what each endpoint takes and returns |
| `Dockerfile` | the hosted build |

Commands: `make setup`, `make db`, `make dev`, `make test` (31 tests), `make lint`.

## Things that will trip you up

- **The Decisions API and agent environments need `api_version="v1beta"`.** The SDK default fails.
- **Vite listens on `localhost` (IPv6).** `curl http://127.0.0.1:5173` fails; use `http://localhost:5173`.
- **Media files aren't in the repo,** except `data/media/samples/`. The evaluation only runs on Eric's laptop.
- **The venue network drops calls.** Model calls retry four times. Don't trust any latency measurement taken today.
- **Gemini 4 Carbon took about 100 s per explanation** when measured, so Argon does proposing and explaining and Hydrogen runs the agent. That measurement was on a bad network; `MODEL_EXPLAIN` is one line if someone re-times it.
- **Commit only your own files by name** when more than one session shares the folder.
- **The tenant's typed description must not reach the proposing step.** Several problem types confirm at a 0.05 cut-off, which is safe only while proposals come from the photo alone.
- **The decision matrix is a draft** with no legal review. Leaks and wall damage have no predicted class by design.
- **Keys:** `.env` holds `GEMINI_API_KEY` and `NYC_OPENDATA_APP_TOKEN` (plus collection keys). Never print or commit them. Render has its own copies in its settings.
