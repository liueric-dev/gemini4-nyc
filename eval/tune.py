"""Pick the confirmation cut-offs from dev photos by a rule fixed in advance.

    uv run python eval/tune.py                       # print what each rule would pick; change nothing
    uv run python eval/tune.py --rule per-type --write   # write the chosen cut-offs to app/thresholds.json

Two rules, both mechanical:
  global    one cut-off for every problem type: the value with the most exact matches. Ties to the lower value.
  per-type  one cut-off per problem type: the value with the best F1 for that type. Ties to the lower value.
The honest estimate for a rule is its cross-validated score: cut-offs chosen on one half of the dev photos
and scored on the other half, both ways. It reads only cached dev results and never looks at the test set.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import config
from eval.run import CORE, load_dev, score_detection

CACHE = config.VAR / f"eval/dev/system-{config.MODEL_DESCRIBE}-{config.PROPOSE_VERSION}"
GRID = [round(0.05 * i, 2) for i in range(1, 19)]  # 0.05 to 0.90


def load() -> tuple[list[dict], dict]:
    items = [it for it in load_dev(None)[0] if (CACHE / f"{it['id']}.json").exists()]
    cached = {it["id"]: json.loads((CACHE / f"{it['id']}.json").read_text())["result"] for it in items}
    probs = {i: {t: (c["probabilities"].get(t, 0.0) if t in c["proposed"] else 0.0) for t in CORE} for i, c in cached.items()}
    return items, probs


def predict(items, probs, cuts) -> dict:
    return {it["id"]: [t for t in CORE if probs[it["id"]][t] >= cuts[t]] for it in items}


def tune_global(items, probs) -> dict:
    best = max(GRID, key=lambda g: (score_detection(items, predict(items, probs, dict.fromkeys(CORE, g)))["exact_match"][0], -g))
    return dict.fromkeys(CORE, best)


def tune_per_type(items, probs) -> dict:
    cuts = {}
    for t in CORE:
        def f1(g, t=t):
            tp = sum(1 for it in items if probs[it["id"]][t] >= g and t in it["key"])
            fp = sum(1 for it in items if probs[it["id"]][t] >= g and t not in it["key"])
            fn = sum(1 for it in items if probs[it["id"]][t] < g and t in it["key"])
            return 2 * tp / (2 * tp + fp + fn) if tp else 0.0
        cuts[t] = max(GRID, key=lambda g: (f1(g), -g))
    return cuts


RULES = {"global": tune_global, "per-type": tune_per_type}


def line(name, items, preds) -> str:
    d = score_detection(items, preds)
    e, r, fa, la = d["exact_match"], d["recall"], d["false_alarms"]["no-problem"], d["false_alarms"]["look-alike"]
    return (f"{name:34} exact {e[0]}/{e[1]} ({100 * e[0] / e[1]:.0f}%)  found {r[0]}/{r[1]}  "
            f"false alarms: clean {fa[0]}/{fa[1]}, look-alike {la[0]}/{la[1]}")


def main() -> None:
    items, probs = load()
    print(f"{len(items)} dev photos with cached results ({CACHE.name})")
    a, b = items[0::2], items[1::2]
    for name, rule in RULES.items():
        cross = {**predict(b, probs, rule(a, probs)), **predict(a, probs, rule(b, probs))}
        print(line(f"{name}, cross-validated", items, cross))
        print(f"    picks on all dev photos: {rule(items, probs)}")
    if "--write" in sys.argv:
        name = sys.argv[sys.argv.index("--rule") + 1] if "--rule" in sys.argv else "global"
        cuts = RULES[name](items, probs)
        cross = {**predict(b, probs, RULES[name](a, probs)), **predict(a, probs, RULES[name](b, probs))}
        path = config.ROOT / "app/thresholds.json"
        t = json.loads(path.read_text())
        t["confirm"] = {"default": 0.5, **cuts}
        t["_tuned"] = {"rule": name, "dev_photos": len(items), "proposer": CACHE.name,
                       "cross_validated_exact_match": score_detection(items, cross)["exact_match"]}
        path.write_text(json.dumps(t, indent=2) + "\n")
        print(f"wrote {path} using the {name} rule")


if __name__ == "__main__":
    main()
