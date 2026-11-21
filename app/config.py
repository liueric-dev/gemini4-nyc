"""Settings and paths. Keys are read from the repo-root .env and never logged."""
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
VAR = ROOT / "var"  # build outputs (SQLite file, caches, results); git-ignored
DB_PATH = VAR / "tenant.db"

load_dotenv(ROOT / ".env")

# Model ids, from docs/GEMINI.md. Each has one job (see docs/plan.md, System design).
# Proposes which problems a photo shows and describes them. On 220 dev photos, confirmed by the Decisions
# API: Hydrogen as proposer matched the key on 74%; Argon's proposals projected to about 80%.
MODEL_DESCRIBE = "gemini-4-argon"
# Bump when the proposing prompt changes, so cached evaluation results are not reused.
# p1: "list only the problems that are clearly visible" (74% exact on 220 dev photos). p2: "list every problem
# that is visible" scored 69%, with more false reports, so p1 was kept.
PROPOSE_VERSION = "p1"
MODEL_AGENT = "gemini-4-hydrogen"  # the case file agent (Managed Agents) runs on Hydrogen
# Step 6: explain the law and draft. Measured Nov 21 on one finding: Argon 10.6 s, Hydrogen 17.2 s,
# Carbon 103.8 s, all with every quote verified. Carbon is too slow for a live answer today.
MODEL_EXPLAIN = "gemini-4-argon"
MODEL_BASELINE = "gemini-4-argon"  # the single-call baseline uses the same model the system reasons with
DECISIONS_TIMEOUT_S = 15  # normally about 1 second
MODEL_TIMEOUT_S = 60
DESCRIBE_THINKING = "LOW"
EXPLAIN_THINKING = "LOW"
MODEL_DECIDE = "gemini-decision-1"  # step 2: yes/no and choice verdicts with probabilities
# The Decisions API and Managed Agents environments exist only on v1beta; the SDK's default
# version returns 404 (decisions) or 400 (agent environment) for them.
DECISIONS_API_VERSION = "v1beta"

REQUIRED_KEYS = ["GEMINI_API_KEY", "NYC_OPENDATA_APP_TOKEN"]


def key(name: str) -> str:
    value = os.environ.get(name, "")
    if not value:
        raise RuntimeError(f"{name} is not set. Add it to {ROOT / '.env'} (see .env.example).")
    return value


def missing_keys() -> list[str]:
    return [k for k in REQUIRED_KEYS if not os.environ.get(k)]
