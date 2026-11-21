# One container is the whole app: the API, the screens, and the database built from data/.
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir uv

WORKDIR /srv
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-dev

COPY app ./app
COPY agent ./agent
COPY scripts ./scripts
COPY eval ./eval
COPY web ./web
COPY data ./data
RUN uv run python scripts/build_db.py

# Set GEMINI_API_KEY and NYC_OPENDATA_APP_TOKEN in the host's settings; never bake them into the image.
ENV PORT=8000
EXPOSE 8000
CMD ["sh", "-c", "uv run --no-sync uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
