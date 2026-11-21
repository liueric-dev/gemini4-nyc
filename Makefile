.PHONY: setup dev api web test lint build

setup:        ## install Python and web dependencies
	uv sync
	cd web && npm install

dev:          ## run the API (port 8000) and the web page (port 5173) together
	@trap 'kill 0' INT TERM EXIT; \
	uv run uvicorn app.main:app --reload --port 8000 & \
	(cd web && npm run dev) & \
	wait

api:
	uv run uvicorn app.main:app --reload --port 8000

web:
	cd web && npm run dev

test:
	uv run pytest -q

lint:
	uv run ruff check .
	cd web && npm run lint

build:
	cd web && npm run build
