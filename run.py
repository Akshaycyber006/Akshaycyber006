#!/usr/bin/env python3
"""Local server for the pixel-art portfolio and public GitHub contribution calendar."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen
from urllib.error import URLError
from pathlib import Path
import json, re
from datetime import date, timedelta

ROOT = Path(__file__).resolve().parent
USER = "Akshaycyber006"

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.split("?")[0] == "/api/contributions":
            try:
                url = f"https://github.com/users/{USER}/contributions"
                req = Request(url, headers={"User-Agent": "AkshayPixelPortfolio/1.0"})
                with urlopen(req, timeout=15) as response:
                    svg = response.read().decode("utf-8", "replace")
                days = []
                # GitHub contribution calendar SVG uses data-date and data-count on rects.
                for tag in re.findall(r"<rect\b[^>]*>", svg):
                    dm = re.search(r'data-date="([^"]+)"', tag)
                    cm = re.search(r'data-count="(\d+)"', tag)
                    lm = re.search(r'data-level="(\d+)"', tag)
                    if dm:
                        days.append({
                            "date": dm.group(1),
                            "count": int(cm.group(1)) if cm else 0,
                            "level": int(lm.group(1)) if lm else 0
                        })
                if not days:
                    raise ValueError("GitHub response did not contain contribution day data")
                total = sum(d["count"] for d in days)
                body = json.dumps({"days": days, "total": total}).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except Exception as exc:
                body = json.dumps({"error": str(exc)}).encode()
                self.send_response(502)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            return
        return super().do_GET()

if __name__ == "__main__":
    print("Open http://localhost:8000 in your browser. Press Ctrl+C to stop.")
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
