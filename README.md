# Tenant advocate for NYC renters

Built at the Gemini 4 NYC Hackathon, November 21, 2026. Problem statement: **5 Sigma**.

A tenant takes a photo of a problem in their apartment and types their address. The app says whether it is a housing violation, quotes the section of NYC law it breaks, gives the violation class and the landlord's deadline to fix it, and drafts the letter to the landlord. A hosted agent then builds a case file from the building's public record.

**The task we picked:** given a tenant's photo, say whether it is a violation, cite the actual section, and give the class and the landlord's deadline, without false alarms or invented citations.

Team: [add names]

## How it works

| Step | Who does it | What happens |
|---|---|---|
| Propose | Gemini 4 **Argon** | Looks at the photo and says which of eight housing problems it shows, with a description of each |
| Confirm | **Decisions API** | Gives a probability for each problem. A problem is reported only if Argon proposed it and the probability clears a cut-off. The same request reads facts from the photo, such as mould size and which pest |
| Photo quality | **Decisions API** | Is the photo sharp, close enough, and showing scale? If not, the tenant is asked for a better one |
| Building facts | Code, NYC Open Data | The address gives year built, units, building type and open HPD violations |
| Decide | Code, no model | The problem type and the facts select a row of a 92-row decision matrix: class, deadline, law sections. If a fact is missing, the app asks the tenant |
| Explain | Gemini 4 **Argon** | Writes the tenant's rights and the landlord's duties from only the law sections for that row |
| Check | Code and the **Decisions API** | A quote is kept only if it appears word for word in the cited section and the Decisions API agrees it supports the claim |
| Letter | Code | Fills in a letter to the landlord and a 311 complaint from the checked results |
| Case file | **Managed Agents**, running Gemini 4 **Hydrogen** | Pulls the building's HPD record, matches the tenant's problems to violations on file, counts neighbours' complaints, and writes a case file |

No model writes the class or the deadline. Code reads them from the decision matrix, using facts from the photo, the building record and the tenant's answers. The matrix was built from the text of the Housing Maintenance Code and HPD's own violation records.

## Does it work? The test

**The test set.** 175 photos from public, licensed sources, chosen by a seeded script. One of us reviewed every label by hand. The labels and scoring rules were frozen with checksums at 08:03 on November 21, before any app code existed (`data/media/review/freeze.json`). It includes 90 photos with no problem or with a look-alike, such as a stain that isn't mould. The test set was run once, after the system stopped changing.

**The baseline.** One call to Gemini 4 Argon with the photo, asked what violations it shows and to cite the law, class and deadline.

| | Baseline: one model call | This system |
|---|---|---|
| Photos answered exactly right | 145 of 175 (83%) | 147 of 175 (84%) |
| Real problems found | 91 of 98 | 85 of 98 |
| Wrong reports | 41 | 27 |
| False alarms on look-alike photos | 7 of 24 | 3 of 24 |
| False alarms on photos with no problem | 3 of 66 | 4 of 66 |

**What this shows.** Overall accuracy is a tie. The system makes a third fewer wrong reports and fewer than half the false alarms on look-alikes. The baseline finds more: it caught six real problems the system missed.

**Mould size**, which sets the violation class (under 10 square feet is Class A, 10 to under 30 is B, 30 or more is C), compared with the reviewer's judgement on 24 photos:

| | Baseline | This system |
|---|---|---|
| Agreed with the reviewer's size | 15 of 24 | 10 of 24 |
| Right, when it gave an answer | 15 of 21 | 10 of 12 |
| Declined to answer when the reviewer could judge | 3 of 24 | 12 of 24 |
| Declined when the reviewer couldn't tell either | 3 of 5 | 5 of 5 |

The baseline agreed with the reviewer more often. The system declines half the time and asks the tenant for the size or a clearer photo; when it does answer it is right more often, and it never guessed on a photo the reviewer couldn't judge.

Full results, with every photo's answer from both sides, are in [`eval/results/`](eval/results/). The scoring rules are in [`data/media/review/scoring-rules.md`](data/media/review/scoring-rules.md).

### What we changed after seeing failures

1. **The first design lost to the baseline.** It used the Decisions API alone to detect problems and scored 110 of 175 (63%). It reported too many secondary problems: a photo of broken plaster was also flagged for a leak, mould and peeling paint. We changed it so a model proposes and the Decisions API confirms, which reached 147 of 175.
2. **A looser proposing prompt made it worse.** Asking the model to list everything visible dropped the score on practice photos from 74% to 69%, so we reverted it.
3. **One cut-off for every problem type was too blunt.** Detectors and pests almost never cause false reports; peeling paint and wall damage often do. A script now picks a cut-off for each problem type from practice photos only (`eval/tune.py`).
4. **The detection probability says nothing about photo quality.** Reports at 0.8 and above were right no more often than reports below 0.6. So the app asks about the photo directly: is it sharp, close enough, and showing scale?
5. **Gemini 4 Carbon was too slow for a live answer on the day** (about 100 seconds for one explanation, against about 10 for Argon, measured on an unreliable network). The explanation step uses Argon.

### Where it still fails

- **Leaks.** 13 wrong leak reports, more than the baseline's 9. Water stains are often reported alongside the real problem.
- **Mid-sized mould.** Of six photos the reviewer put at 10 to under 30 square feet, the system got none right (two called smaller, four declined). The baseline got one.
- **Missed problems.** It found 85 of 98 real problems. The confirm step that removes false alarms also removes some real ones, mostly detectors and leaks.
- **Leaks and wall damage have no predicted class.** HPD issues them in more than one class and the rule for choosing is not published online, so the app says the inspector decides.
- **Video is not supported.** The 22 test videos were not attempted.

### Limits of the test

- The photos are public images, not NYC tenants' own photos.
- 175 photos is a small set. Differences of a few photos are noise.
- The law step was scored for the baseline (its citations were a real section 90 of 91 times, and law for that problem 84 of 91). The system's citations were not scored the same way; they are constrained by code to the sections for the matched rule and checked word for word.
- The decision matrix is a draft. Nobody with legal training has reviewed it.

## What was built when

- **Before hacking began (overnight, November 20 to 21):** data collection only. The law text, HPD's public records, the test photos, and a draft decision matrix (`data/`). The test labels were reviewed and frozen at 08:03. This is logged in [`docs/data-session-log.md`](docs/data-session-log.md).
- **During the hackathon (from 10:30 on November 21):** all of the app. Everything in `app/`, `agent/`, `eval/`, `scripts/`, `tests/` and `web/`, and the system design in `docs/plan.md`. The commit history shows the order.

## Run it

Needs Python 3.12 with [uv](https://docs.astral.sh/uv/), and Node 22 or later.

```
make setup          # install dependencies
cp .env.example .env    # then add GEMINI_API_KEY and NYC_OPENDATA_APP_TOKEN
make db             # build the database from data/
make dev            # API on port 8000, web page on port 5173
make test           # 23 tests, no network needed
```

The evaluation:

```
uv run python eval/run.py --set dev --limit 220    # practice photos
uv run python eval/tune.py                         # show the cut-offs each rule would pick
uv run python eval/run.py --set test               # the frozen test set
uv run python eval/report.py                       # write eval/results/
```

The test photos are not in this repository (licences and size), so the evaluation and the photo grid only run where the photos are on disk. Each photo's source URL and checksum are in `data/media/manifest.jsonl`.

## Where things are

| Path | What |
|---|---|
| `app/pipeline.py` | The pipeline: propose, confirm, decide, explain, check |
| `app/db.py`, `app/rule_conditions.json` | The decision matrix lookups and the conditions that select a row |
| `app/building.py` | Address to building facts |
| `app/letter.py` | The letter and 311 drafts |
| `app/case_agent.py`, `agent/` | The case file agent and its skill |
| `eval/` | Baseline, scoring, cut-off tuning, results |
| `docs/api.md` | What the backend returns |
| `docs/decision-matrix.md` | The 92 situations, readable |
| `docs/plan.md` | The plan and system design |
| `data/` | The law, the public records, the decision matrix and the frozen test labels |

## Working in this repo

- Data collection is finished. Build and commit normally. `data/README.md` was written for the overnight collection agents; its "do not commit" rules no longer apply.
- Don't edit the frozen test files: `data/media/review/decisions.json`, `review_set.json`, `scoring-rules.md` and `data/problem-map/expected-outcomes.csv`.
- Don't commit `.env`, any `local/` folder, or media files. They are git-ignored.
- The screens live in `web/`. The backend contract is `docs/api.md`, with a filled-in example in `docs/sample-response.json`.
- API keys go in `.env` at the repo root. Never commit them.

## Sources and credits

- Law text: NYC Administrative Code and Rules (American Legal Publishing), New York State law (NY Senate Open Legislation), federal regulations (eCFR). Public law, collected November 21, 2026.
- Building and violation data: NYC Open Data (HPD, Department of City Planning), NYC GeoSearch. Free to use under NYC Administrative Code § 23-502.
- Rent-stabilized buildings: NYS Homes and Community Renewal 2025 building registration file, published by the NYC Rent Guidelines Board.
- Test photos: Wikimedia Commons, Flickr, iNaturalist, Pexels and others, each under its own licence. Credits and source links for every photo are in `data/media/manifest.jsonl`.

This app helps a tenant organise evidence and understand the law. It is not legal advice, and it never sends anything on the tenant's behalf.
