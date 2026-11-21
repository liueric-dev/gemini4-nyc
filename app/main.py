"""The web API. Run with `make dev`."""
from fastapi import FastAPI

from app import config

app = FastAPI(title="Tenant advocate")


@app.get("/api/health")
def health() -> dict:
    return {
        "ok": True,
        "missing_keys": config.missing_keys(),
        "database_built": config.DB_PATH.exists(),
    }
