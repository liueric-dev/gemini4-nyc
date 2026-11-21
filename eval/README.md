# Evaluation

The baseline, the scoring script and the results go here.

- Test items and labels: `data/media/review/review_set.json` and `decisions.json`, with `freeze-addendum.json` applied on top. These are frozen; never edit them.
- Scoring rules: `data/media/review/scoring-rules.md`.
- Tune on dev-split items only (`split == "dev"` in `data/media/manifest.jsonl`). Run the test set once, at the end, for both the system and the baseline.
