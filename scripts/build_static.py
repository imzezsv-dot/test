#!/usr/bin/env python3
"""Assemble a static preview build for Vercel / any static host.

Copies app/web/* into public/, rewrites `/static/` paths to `/`, and
switches the interface into a demo-only mode where the upload button is
disabled and pressing "See a finished example" is the only path.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "app" / "web"
DST = ROOT / "public"


def rewrite(text: str) -> str:
    text = text.replace("/static/", "/")
    text = text.replace('id="start" disabled', 'id="start" disabled data-static="true"')
    return text


def main() -> None:
    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)

    for html in DST.rglob("*.html"):
        html.write_text(rewrite(html.read_text()))

    # A one-line preview entry so /preview.html resolves.
    (DST / "preview.html").write_text(rewrite((SRC / "index.html").read_text()))

    # Vercel: static site, no build step needed.
    (ROOT / "vercel.json").write_text(
        '{\n'
        '  "cleanUrls": true,\n'
        '  "rewrites": [\n'
        '    { "source": "/(.*)", "destination": "/$1" }\n'
        '  ],\n'
        '  "headers": [\n'
        '    { "source": "/(.*)\\\\.woff2", "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }] }\n'
        '  ]\n'
        '}\n'
    )
    print(f"Built {DST} with {sum(1 for _ in DST.rglob('*'))} entries.")


if __name__ == "__main__":
    main()
