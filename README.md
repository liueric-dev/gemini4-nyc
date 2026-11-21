# gemini4-nyc

Tenant advocate for NYC renters, built at the Gemini 4 NYC Hackathon on Nov 21, 2026.

A tenant takes a photo of a problem in their apartment and types their address. The app says whether it is a violation, quotes the section of NYC housing law, gives the severity class and the landlord's deadline, and drafts the letter or complaint.

## Where things are

| Path | What |
|---|---|
| [docs/plan.md](docs/plan.md) | The plan and the system design |
| [docs/team-brief.md](docs/team-brief.md) | A plain-language brief for the team |
| [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md) | Hackathon rules and judging |
| [docs/GEMINI.md](docs/GEMINI.md) | Gemini 4 model and API notes |
| [data/SUMMARY.md](data/SUMMARY.md) | What data was collected |
| [data/media/review/](data/media/review/) | The frozen test labels and scoring rules |

## For anyone (or any agent) working in this repo

- Data collection is finished. Build and commit normally, anywhere in the repo.
- `data/README.md` was written for the overnight collection agents. Its "do not commit" and write rules no longer apply.
- Don't edit the frozen test files: `data/media/review/decisions.json`, `review_set.json` and `scoring-rules.md`.
- Don't commit `.env`, any `local/` folder, or the media files. They are git-ignored.
- Some files that the docs and manifests mention exist only on Eric's machine: everything under `local/`, the media files, and paths starting `~/hackathons/`.
- API keys go in a `.env` file at the repo root. Ask Eric for the values; never commit them.
