#!/usr/bin/env python3
"""Validate the generated handbook using only the Python standard library."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PLACEHOLDER_RE = re.compile(r"\[[A-Za-z][^\[\]]*\]")


class Document(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.links: list[tuple[str, str]] = []
        self.ids: list[str] = []
        self.errors: list[str] = []
        self.title_depth = 0
        self.title_text: list[str] = []
        self.h1_count = 0
        self.main_count = 0
        self.has_lang = False
        self.has_viewport = False
        self.placeholder_count = 0
        self.placeholder_alert_count = 0
        self.source_pages: list[str] = []
        self.stack: list[str] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {key: value or "" for key, value in attrs_list}
        self.stack.append(tag)
        if tag == "html":
            self.has_lang = bool(attrs.get("lang", "").strip())
        elif tag == "title":
            self.title_depth += 1
        elif tag == "meta" and attrs.get("name", "").lower() == "viewport":
            self.has_viewport = bool(attrs.get("content", "").strip())
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "main":
            self.main_count += 1
        elif tag == "img" and "alt" not in attrs:
            self.errors.append("image is missing an alt attribute")

        if "id" in attrs:
            self.ids.append(attrs["id"])
        if "data-source-page" in attrs:
            self.source_pages.append(attrs["data-source-page"])
        classes = set(attrs.get("class", "").split())
        if tag == "mark" and "placeholder" in classes:
            self.placeholder_count += 1
        if "placeholder-alert" in classes:
            self.placeholder_alert_count += 1
        for attribute in ("href", "src"):
            if attrs.get(attribute):
                self.links.append((attribute, attrs[attribute]))
        for attribute in attrs:
            if attribute.lower().startswith("on"):
                self.errors.append(f"inline event handler is not allowed: {attribute}")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if self.stack:
            # Be tolerant of void elements and HTML's optional closing tags.
            for index in range(len(self.stack) - 1, -1, -1):
                if self.stack[index] == tag:
                    del self.stack[index:]
                    break

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)

    def finish(self) -> None:
        if not "".join(self.title_text).strip():
            self.errors.append("missing document title")
        if not self.has_lang:
            self.errors.append("html element is missing a language")
        if not self.has_viewport:
            self.errors.append("missing viewport metadata")
        if self.h1_count != 1:
            self.errors.append(f"expected exactly one h1, found {self.h1_count}")
        if self.main_count != 1:
            self.errors.append(f"expected exactly one main, found {self.main_count}")
        duplicates = sorted({value for value in self.ids if self.ids.count(value) > 1})
        if duplicates:
            self.errors.append(f"duplicate IDs: {', '.join(duplicates)}")
        if self.placeholder_count and not self.placeholder_alert_count:
            self.errors.append("highlighted placeholders exist without a visible alert")


def resolve_local(source: Path, value: str) -> tuple[Path | None, str]:
    parsed = urlsplit(value)
    if parsed.scheme in {"mailto", "tel"}:
        return None, ""
    if parsed.scheme or value.startswith("//"):
        raise ValueError(f"external URL is not offline-safe: {value}")
    if parsed.path.startswith("/"):
        raise ValueError(f"root-relative URL is not file-safe: {value}")
    target = (source.parent / unquote(parsed.path or source.name)).resolve()
    if target.is_dir():
        target /= "index.html"
    return target, unquote(parsed.fragment)


def content_sections() -> list[tuple[int, str]]:
    sections: list[tuple[int, str]] = []
    for path in sorted((ROOT / "content").glob("*.md")):
        source = path.read_text(encoding="utf-8")
        front_matter = source.split("---", 2)
        if len(front_matter) < 3:
            continue
        match = re.search(r"^weight:\s*(\d+)\s*$", front_matter[1], re.MULTILINE)
        if match:
            sections.append((int(match.group(1)), path.stem))
    return sorted(sections)


def main() -> int:
    errors: list[str] = []
    sections = content_sections()
    weights = [weight for weight, _ in sections]
    expected_weights = list(range(1, len(sections) + 1))
    if weights != expected_weights:
        errors.append(f"section weights must be sequential {expected_weights}; found {weights}")

    if not (DIST / "index.html").is_file():
        errors.append("dist/index.html is missing")
    if not (DIST / "print.html").is_file():
        errors.append("dist/print.html is missing")

    documents: dict[Path, Document] = {}
    for path in sorted(DIST.rglob("*.html")):
        document = Document(path)
        document.feed(path.read_text(encoding="utf-8"))
        document.finish()
        documents[path.resolve()] = document
        errors.extend(f"{path.relative_to(ROOT)}: {message}" for message in document.errors)

    for source, document in documents.items():
        for attribute, value in document.links:
            try:
                target, fragment = resolve_local(source, value)
            except ValueError as exc:
                errors.append(f"{source.relative_to(ROOT)}: {attribute}: {exc}")
                continue
            if target is None:
                continue
            if DIST.resolve() not in target.parents and target != DIST.resolve():
                errors.append(f"{source.relative_to(ROOT)}: URL escapes dist: {value}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing target: {value}")
                continue
            if fragment and target.suffix == ".html":
                target_document = documents.get(target)
                if target_document and fragment not in target_document.ids:
                    errors.append(
                        f"{source.relative_to(ROOT)}: missing fragment #{fragment} in {target.relative_to(ROOT)}"
                    )

    print_document = documents.get((DIST / "print.html").resolve())
    expected_print_sources = ["start-here", *(name for _, name in sections)]
    if print_document and print_document.source_pages != expected_print_sources:
        errors.append(
            "print handbook sections are incomplete or out of order: "
            f"expected {expected_print_sources}, found {print_document.source_pages}"
        )

    css_path = DIST / "css" / "site.css"
    if not css_path.is_file():
        errors.append("dist/css/site.css is missing")
    else:
        css = css_path.read_text(encoding="utf-8")
        if "@media print" not in css or "@page" not in css:
            errors.append("print stylesheet rules are missing")

    if errors:
        print("Build validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    pages = len(documents)
    placeholders = sum(document.placeholder_count for document in documents.values() if document.path.name != "print.html")
    print(f"Validated {pages} offline pages, local links, document structure, and print CSS.")
    print(f"Draft visibility check: {placeholders} highlighted placeholders remain in family-facing pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
