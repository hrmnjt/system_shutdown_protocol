# System Shutdown Protocol

A family continuity handbook authored in Markdown and published as offline HTML, print, and an eventually authenticated website using [Hugo](https://gohugo.io/).

## Purpose and audience

The protocol is intended for the owner’s nontechnical family to follow after the owner dies. It combines:

1. knowledge the family may not currently have about contacts, systems, assets, responsibilities, routines, and wishes; and
2. a visible backlog of preparations the owner still intends to complete.

The generated experience must remain calm and usable for people who may be grieving or under stress. The repository is currently a structured draft: theme and distribution foundations exist, while personal content, jurisdiction-specific guidance, and final content organization remain unfinished.

Coding agents should read [`AGENTS.md`](AGENTS.md) before changing the project. It records product intent, invariants, security boundaries, unresolved decisions, and completion checks.

## Build

Hugo extended v0.152 or later is recommended.

```sh
make build
```

The build cleans stale output and writes the offline site to `dist/`. Open `dist/index.html` directly in a browser; no web server or internet connection is required. Copy the **entire** `dist/` directory, not only `index.html`.

To run the stricter build and offline-link validation:

```sh
make check
```

For local authoring with automatic refresh:

```sh
make serve
```

The development server is only for editing—the final `dist/` folder remains fully offline.

The interface uses the Gruvbox Light palette by default and automatically switches to Gruvbox Dark when the operating system requests dark mode. Print output remains high-contrast and ink-conscious rather than reproducing the screen background colours.

## Distribution formats

All formats should carry the same `params.protocolVersion` and `params.lastReviewed` values from [`hugo.toml`](hugo.toml). Treat print, hosted, and portable as **formats of one version**, not as versions 1, 2, and 3; this makes it possible to identify stale copies.

### Printed locker copy

Open `dist/print.html`, use **Open print dialog**, inspect every page in print preview, and print the complete handbook. Its cover includes the protocol version, review date, print-build date, privacy classification, and stale-copy warning.

### Password-protected hosted copy

Deploy the complete `dist/` directory behind authentication and HTTPS. The generated pages include `noindex`, `nofollow`, and `noarchive`, but these directives are not security controls. Authentication must happen at the web server, identity proxy, or hosting layer—not in client-side JavaScript.

### Portable thumb-drive copy

```sh
make portable
```

This validates the build and creates a versioned folder under `release/` containing `START HERE.html` and `README.txt`. Copy that entire folder to the thumb drive. On a MacBook, double-click `START HERE.html`; it uses only nearby files and does not need a server or network connection.

See [`docs/distribution.md`](docs/distribution.md) for the release and security model.

## Edit content

Family-facing pages live in [`content/`](content/). Page order and displayed section numbers are controlled by the sequential `weight` field in each file’s front matter.

Write missing information in square brackets with a leading letter, for example:

```md
- Executor: **[name and phone number]**
```

The theme automatically highlights these placeholders, counts them on each page, marks unfinished navigation cards, and displays a site-wide draft warning. Task-list boxes such as `- [ ]` are not treated as placeholders.

Keep planned and incomplete work in [`content/todo.md`](content/todo.md). Remove an item when it is complete; if it is only partly complete, explain what exists and what remains so the note is still useful without you.

## Review date

`params.lastReviewed` in [`hugo.toml`](hugo.toml) means the last date on which contacts, authority documents, document locations, finances, access, responsibilities, wishes, TODOs, offline behavior, and print output were deliberately checked. It is not a build timestamp.

Follow the checklist in [`content/preparedness.md`](content/preparedness.md). Only after completing the applicable checks should you set an unambiguous date such as:

```toml
lastReviewed = "15 January 2026"
```

Then rebuild, retest, and replace distributed copies.

## Print

Use **Print full handbook** in the site header to open `dist/print.html`. It combines the cover, contents, start page, and every numbered section into one print-optimized document. Inspect print preview before distributing it; browsers and printers can paginate tables differently.

## Before distributing

1. Resolve highlighted placeholders or leave a clear corresponding explanation on the TODO page.
2. Complete the review checklist and set an accurate review date.
3. Run `make check`.
4. Open `dist/index.html` on a phone-sized viewport and a laptop-sized viewport.
5. Run `make portable` and test `START HERE.html` from removable storage with networking disabled.
6. Inspect `dist/print.html` in print preview and print the urgent sections or full handbook.
7. Test the hosted authentication and recovery path from outside your normal signed-in devices.
8. Give a trusted nontechnical person a short findability test.
9. Replace stale offline and printed copies.

## Security

The generated HTML is not encrypted. Do not put passwords, recovery codes, private keys, security-question answers, or unnecessary complete account numbers in this repository.

Use the handbook to point family members to a separate protected inventory and credential-recovery process. Review repository history before making it public or sharing it.
