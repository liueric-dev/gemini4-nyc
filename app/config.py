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
MODEL_DESCRIBE = "gemini-4-hydrogen"  # step 3: describe each detected problem
MODEL_EXPLAIN = "gemini-4-carbon"  # step 6: apply the law and draft
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
