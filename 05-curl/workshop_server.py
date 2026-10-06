#!/usr/bin/env python3
"""Local HTTP exercise server for HackSeries Day 1.

Run from any directory: python3 05-curl/workshop_server.py
No third-party packages are required.
"""

from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit


CLUE = (
    "The server is running. Try curl -I to inspect headers, -o to save "
    "this text, and -L to follow /old.\n"
)
FINAL_ANSWER = "192.0.2.42"
FINAL_MESSAGE = (
    "ACCESS GRANTED\n"
    "Final clue: the shell is strongest when small commands work together.\n"
    "Submit this clue and the commands you used.\n"
)
WRONG_ANSWER = (
    "That IP is not the most frequent one on ERROR lines. "
    "Check the pipeline and try again.\n"
)


class WorkshopHandler(BaseHTTPRequestHandler):
    server_version = "HackSeriesWorkshop/1.0"

    def do_GET(self) -> None:
        self._respond(include_body=True)

    def do_HEAD(self) -> None:
        self._respond(include_body=False)

    def _respond(self, *, include_body: bool) -> None:
        request = urlsplit(self.path)
        params = parse_qs(request.query)

        if request.path == "/clue.txt":
            status, body = 200, CLUE
        elif request.path == "/old":
            self.send_response(302)
            self.send_header("Location", "/clue.txt")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        elif request.path == "/final":
            answer = params.get("ip", [""])[0]
            status, body = (
                (200, FINAL_MESSAGE)
                if answer == FINAL_ANSWER
                else (400, WRONG_ANSWER)
            )
        else:
            status, body = 404, "File not found\n"

        payload = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if include_body:
            self.wfile.write(payload)


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the workshop curl exercises")
    parser.add_argument("--host", default="127.0.0.1", help="address to bind (default: localhost)")
    parser.add_argument("--port", type=int, default=8000, help="port (default: 8000)")
    args = parser.parse_args()

    try:
        server = ThreadingHTTPServer((args.host, args.port), WorkshopHandler)
    except OSError as exc:
        parser.exit(1, f"Could not start server: {exc}\n")

    print(f"Workshop server: http://{args.host}:{args.port}", flush=True)
    print("Press Ctrl+C to stop.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
