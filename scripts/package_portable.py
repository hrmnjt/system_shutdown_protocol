#!/usr/bin/env python3
"""Create a thumb-drive friendly copy of the generated offline handbook."""

from __future__ import annotations

import re
import shutil
import tomllib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
RELEASE = ROOT / "release"


class EntryPointLinks(HTMLParser):
    def __init__(self, entry: Path) -> None:
        super().__init__()
        self.entry = entry
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs_list)
        for attribute in ("href", "src"):
            value = attrs.get(attribute)
            if not value:
                continue
            parsed = urlsplit(value)
            if parsed.scheme in {"mailto", "tel"} or not parsed.path:
                continue
            if parsed.scheme or value.startswith("//") or parsed.path.startswith("/"):
                self.errors.append(f"{attribute} is not portable: {value}")
                continue
            target = (self.entry.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                self.errors.append(f"{attribute} target is missing: {value}")


def validate_entry_point(entry: Path) -> None:
    parser = EntryPointLinks(entry)
    parser.feed(entry.read_text(encoding="utf-8"))
    if parser.errors:
        raise SystemExit("portable entry point validation failed:\n  - " + "\n  - ".join(parser.errors))


def main() -> None:
    if not (DIST / "index.html").is_file():
        raise SystemExit("dist/index.html is missing; build and validate the site first")

    config = tomllib.loads((ROOT / "hugo.toml").read_text(encoding="utf-8"))
    params = config.get("params", {})
    version = str(params.get("protocolVersion", "unversioned"))
    safe_version = re.sub(r"[^A-Za-z0-9._-]+", "-", version).strip("-").lower()
    destination = RELEASE / f"system-shutdown-protocol-{safe_version}-portable"

    if destination.exists():
        shutil.rmtree(destination)
    RELEASE.mkdir(exist_ok=True)
    shutil.copytree(DIST, destination)
    shutil.copy2(destination / "index.html", destination / "START HERE.html")

    instructions = f"""SYSTEM SHUTDOWN PROTOCOL — PORTABLE OFFLINE COPY
Version: {version}
Last reviewed: {params.get('lastReviewed', 'Unknown')}
Classification: {params.get('classification', 'Private')}

ON A MACBOOK
1. Keep this entire folder together on the thumb drive.
2. Double-click “START HERE.html”.
3. It should open in the default browser without internet access.
4. If macOS asks which application to use, choose Safari, Chrome, or Firefox.

IMPORTANT
- Do not move only the START HERE file; it relies on the nearby pages, CSS, and JavaScript.
- Compare the version and “Last reviewed” value with any printed or hosted copy.
- This folder is not encrypted. Keep the thumb drive physically secure.
- The handbook should point to protected credentials; it should not contain passwords or recovery keys.
"""
    (destination / "README.txt").write_text(instructions, encoding="utf-8")
    validate_entry_point(destination / "START HERE.html")
    print(f"Portable copy created and validated at {destination.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
