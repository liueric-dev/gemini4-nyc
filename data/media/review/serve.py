"""Local review server for the media test set.

Usage: python3 -I data/media/review/serve.py [port]
Then open http://127.0.0.1:<port>/review/index.html
Decisions save to data/media/review/decisions.json as you go (never into manifest.jsonl).
"Freeze" writes data/media/review/freeze.json: the time, plus sha256 of decisions.json and review_set.json.
Adapted from gemini4-playbook/testset/serve.py (Nov 20 prep).
"""

import datetime
import hashlib
import json
import os
import pathlib
import re
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

REVIEW = pathlib.Path(__file__).resolve().parent
ROOT = REVIEW.parent  # data/media, so media files resolve as /images/... and /videos/...
DECISIONS = REVIEW / "decisions.json"
FREEZE = REVIEW / "freeze.json"
SET = REVIEW / "review_set.json"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path == "/api/decisions":
            return self._send(200, DECISIONS.read_bytes() if DECISIONS.exists() else b"{}", "application/json")
        if self.path == "/api/freeze":
            return self._send(200, FREEZE.read_bytes() if FREEZE.exists() else b"{}", "application/json")
        rng = self.headers.get("Range")
        path = pathlib.Path(self.translate_path(self.path))
        if rng and path.is_file():  # byte ranges so video seeking works
            return self._send_range(path, rng)
        return super().do_GET()

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)) or 0)
        if self.path == "/api/decisions":
            if FREEZE.exists():
                return self._send(409, b'{"error":"frozen"}', "application/json")
            data = json.loads(body)
            tmp = DECISIONS.with_suffix(".tmp")
            tmp.write_text(json.dumps(data, indent=1, sort_keys=True))
            os.replace(tmp, DECISIONS)
            return self._send(200, b'{"ok":true}', "application/json")
        if self.path == "/api/freeze":
            info = {
                "frozen_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
                "decisions_sha256": sha(DECISIONS),
                "review_set_sha256": sha(SET),
                "decisions_count": len(json.loads(DECISIONS.read_text())) if DECISIONS.exists() else 0,
            }
            FREEZE.write_text(json.dumps(info, indent=1))
            return self._send(200, json.dumps(info).encode(), "application/json")
        return self._send(404, b"not found", "text/plain")

    def _send(self, code, body, ctype):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_range(self, path, rng):
        size = path.stat().st_size
        m = re.match(r"bytes=(\d*)-(\d*)", rng)
        start = int(m.group(1)) if m and m.group(1) else 0
        end = int(m.group(2)) if m and m.group(2) else size - 1
        end = min(end, size - 1)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(str(path)))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()
        with path.open("rb") as f:
            f.seek(start)
            self.wfile.write(f.read(end - start + 1))

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8770
    print(f"Review: http://127.0.0.1:{port}/review/index.html  (decisions saved to {DECISIONS})")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
