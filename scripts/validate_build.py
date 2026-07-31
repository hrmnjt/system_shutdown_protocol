#!/usr/bin/env python3
"""Validate the generated handbook using only the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


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
        self.has_robots_policy = False
        self.placeholder_count = 0
        self.placeholder_report_count = 0
        self.source_pages: list[str] = []
        self.heading_levels: list[int] = []
        self.table_count = 0
        self.table_scroll_count = 0
        self.section_verification_count = 0
        self.search_index_count = 0
        self.search_index_depth = 0
        self.search_index_text: list[str] = []
        self.has_search_input = False
        self.has_search_results = False
        self.list_stack: list[str] = []
        self.list_item_stack: list[list[str] | None] = []
        self.ordered_item_texts: list[str] = []
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
        elif tag == "meta" and attrs.get("name", "").lower() == "robots":
            policy = attrs.get("content", "").lower()
            self.has_robots_policy = "noindex" in policy and "noarchive" in policy
        elif re.fullmatch(r"h[1-6]", tag):
            level = int(tag[1])
            self.heading_levels.append(level)
            if level == 1:
                self.h1_count += 1
        elif tag == "main":
            self.main_count += 1
        elif tag == "img" and "alt" not in attrs:
            self.errors.append("image is missing an alt attribute")
        elif tag == "input" and attrs.get("type") == "checkbox" and "disabled" in attrs:
            self.errors.append("disabled checkbox should be rendered as a static checklist marker")

        if tag in {"ol", "ul"}:
            self.list_stack.append(tag)
        elif tag == "li":
            self.list_item_stack.append([] if self.list_stack and self.list_stack[-1] == "ol" else None)

        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "script" and attrs.get("id") == "search-index":
            self.search_index_count += 1
            self.search_index_depth += 1
            if attrs.get("type") != "application/json":
                self.errors.append("search index must use the application/json type")
        if tag == "input" and attrs.get("id") == "site-search-input":
            self.has_search_input = attrs.get("type") == "search"
        if attrs.get("id") == "search-results":
            self.has_search_results = True
        if "data-source-page" in attrs:
            self.source_pages.append(attrs["data-source-page"])
        classes = set(attrs.get("class", "").split())
        if tag == "mark" and "placeholder" in classes:
            self.placeholder_count += 1
        if attrs.get("data-has-placeholders") == "true":
            self.placeholder_report_count += 1
        if tag == "table":
            self.table_count += 1
        if "table-scroll" in classes:
            self.table_scroll_count += 1
        if "section-verification" in classes:
            self.section_verification_count += 1
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
        if tag == "script" and self.search_index_depth:
            self.search_index_depth -= 1
        if tag == "li" and self.list_item_stack:
            item = self.list_item_stack.pop()
            if item is not None:
                self.ordered_item_texts.append("".join(item).strip())
        elif tag in {"ol", "ul"} and self.list_stack:
            self.list_stack.pop()
        if self.stack:
            # Be tolerant of void elements and HTML's optional closing tags.
            for index in range(len(self.stack) - 1, -1, -1):
                if self.stack[index] == tag:
                    del self.stack[index:]
                    break

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)
        if self.search_index_depth:
            self.search_index_text.append(data)
        for item in self.list_item_stack:
            if item is not None:
                item.append(data)

    def finish(self) -> None:
        if not "".join(self.title_text).strip():
            self.errors.append("missing document title")
        if not self.has_lang:
            self.errors.append("html element is missing a language")
        if not self.has_viewport:
            self.errors.append("missing viewport metadata")
        if not self.has_robots_policy:
            self.errors.append("missing noindex/noarchive robots policy")
        if self.h1_count != 1:
            self.errors.append(f"expected exactly one h1, found {self.h1_count}")
        if self.main_count != 1:
            self.errors.append(f"expected exactly one main, found {self.main_count}")
        for previous, current in zip(self.heading_levels, self.heading_levels[1:]):
            if current > previous + 1:
                self.errors.append(f"heading level jumps from h{previous} to h{current}")
                break
        duplicates = sorted({value for value in self.ids if self.ids.count(value) > 1})
        if duplicates:
            self.errors.append(f"duplicate IDs: {', '.join(duplicates)}")
        expected_reports = 1 if self.placeholder_count else 0
        if self.placeholder_report_count != expected_reports:
            self.errors.append("placeholder completion status does not match highlighted placeholders")
        if self.table_count != self.table_scroll_count:
            self.errors.append("each table must have a keyboard-scrollable wrapper")
        if self.path.name != "print.html":
            if self.search_index_count != 1 or not self.has_search_input or not self.has_search_results:
                self.errors.append("local search index and controls must appear exactly once")
        elif self.search_index_count:
            self.errors.append("print handbook should not embed the local search index")
        if any(re.match(r"^\d+\.\s", text) for text in self.ordered_item_texts):
            self.errors.append("ordered list item repeats an explicit numeric prefix")


def resolve_local(source: Path, value: str) -> tuple[Path | None, str]:
    parsed = urlsplit(value)
    if parsed.scheme in {"mailto", "tel"}:
        return None, ""
    if parsed.scheme or value.startswith("//"):
        raise ValueError(f"external URL is not offline-safe: {value}")
    if parsed.path.startswith("/"):
        raise ValueError(f"root-relative URL is not file-safe: {value}")
    if parsed.path and parsed.path.endswith("/"):
        raise ValueError(f"directory URL is ambiguous when opened from a thumb drive: {value}")
    target = (source.parent / unquote(parsed.path or source.name)).resolve()
    if target.is_dir():
        raise ValueError(f"directory URL is ambiguous when opened from a thumb drive: {value}")
    return target, unquote(parsed.fragment)


def content_sections() -> tuple[list[tuple[int, str]], list[str]]:
    sections: list[tuple[int, str]] = []
    errors: list[str] = []
    category_ranges = {
        "reference": range(1, 13),
        "tool": range(13, 15),
        "maintenance": range(15, 17),
    }
    manual_part_ranges = {
        "essentials": range(1, 4),
        "household": range(4, 11),
        "legacy": range(11, 13),
    }
    allowed_gap_levels = {"none", "critical", "important", "optional"}

    for path in sorted((ROOT / "content").glob("*.md")):
        source = path.read_text(encoding="utf-8")
        front_matter = source.split("---", 2)
        if len(front_matter) < 3:
            continue
        metadata = front_matter[1]
        weight_match = re.search(r"^weight:\s*(\d+)\s*$", metadata, re.MULTILINE)
        if not weight_match:
            continue

        weight = int(weight_match.group(1))
        sections.append((weight, path.stem))
        category_match = re.search(r'^category:\s*"([^"]+)"\s*$', metadata, re.MULTILINE)
        part_match = re.search(r'^manualPart:\s*"([^"]+)"\s*$', metadata, re.MULTILINE)
        verified_match = re.search(r'^lastVerified:\s*"([^"]+)"\s*$', metadata, re.MULTILINE)
        gap_match = re.search(r'^gapLevel:\s*"([^"]+)"\s*$', metadata, re.MULTILINE)

        category = category_match.group(1) if category_match else ""
        if category not in category_ranges or weight not in category_ranges[category]:
            errors.append(f"{path.relative_to(ROOT)}: category {category or 'missing'} is inconsistent with weight {weight}")
        if category == "reference":
            manual_part = part_match.group(1) if part_match else ""
            if manual_part not in manual_part_ranges or weight not in manual_part_ranges[manual_part]:
                errors.append(
                    f"{path.relative_to(ROOT)}: manualPart {manual_part or 'missing'} is inconsistent with weight {weight}"
                )
        if not verified_match or not verified_match.group(1).strip():
            errors.append(f"{path.relative_to(ROOT)}: lastVerified is missing")
        gap_level = gap_match.group(1) if gap_match else ""
        if gap_level not in allowed_gap_levels:
            errors.append(f"{path.relative_to(ROOT)}: gapLevel must be one of {sorted(allowed_gap_levels)}")

    home = (ROOT / "content" / "_index.md").read_text(encoding="utf-8")
    if not re.search(r'^gapLevel:\s*"critical"\s*$', home.split("---", 2)[1], re.MULTILINE):
        errors.append("content/_index.md: emergency guide must declare critical gap visibility while unfinished")
    return sorted(sections), errors


def main() -> int:
    errors: list[str] = []
    sections, content_errors = content_sections()
    errors.extend(content_errors)
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

    expected_search_titles = {"Start here"}
    for _, name in sections:
        source_text = (ROOT / "content" / f"{name}.md").read_text(encoding="utf-8")
        title_match = re.search(r'^title:\s*"([^"]+)"\s*$', source_text.split("---", 2)[1], re.MULTILINE)
        if title_match:
            expected_search_titles.add(title_match.group(1))

    for source, document in documents.items():
        if source.name != "print.html":
            try:
                search_data = json.loads("".join(document.search_index_text))
            except (json.JSONDecodeError, TypeError) as exc:
                errors.append(f"{source.relative_to(ROOT)}: search index is not valid JSON: {exc}")
            else:
                search_titles = {str(item.get("title", "")) for item in search_data if isinstance(item, dict)}
                if search_titles != expected_search_titles:
                    errors.append(f"{source.relative_to(ROOT)}: search index pages are incomplete")
                for item in search_data:
                    permalink = str(item.get("permalink", "")) if isinstance(item, dict) else ""
                    if not permalink or permalink.startswith("/") or permalink.endswith("/") or urlsplit(permalink).scheme:
                        errors.append(f"{source.relative_to(ROOT)}: search permalink is not portable: {permalink}")

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

    for _, name in sections:
        built_page = documents.get((DIST / f"{name}.html").resolve())
        if built_page and built_page.section_verification_count != 1:
            errors.append(f"dist/{name}.html: expected one section verification status")

    print_document = documents.get((DIST / "print.html").resolve())
    expected_print_sources = ["start-here", *(name for _, name in sections)]
    if print_document and print_document.source_pages != expected_print_sources:
        errors.append(
            "print handbook sections are incomplete or out of order: "
            f"expected {expected_print_sources}, found {print_document.source_pages}"
        )
    if print_document and print_document.section_verification_count != len(sections):
        errors.append("print handbook must show one verification status for every weighted section")

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
    print(f"Completion visibility check: {placeholders} highlighted placeholders remain in family-facing pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
