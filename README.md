# System Shutdown Protocol

An offline, family-facing handbook authored in Markdown and built with [Hugo](https://gohugo.io/).

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

Use **Print full handbook** in the site header to open `dist/print.html`. It combines the start page and every numbered section into one print-optimized document. Inspect print preview before distributing it; browsers and printers can paginate tables differently.

## Before distributing

1. Resolve highlighted placeholders or leave a clear corresponding explanation on the TODO page.
2. Complete the review checklist and set an accurate review date.
3. Run `make check`.
4. Open `dist/index.html` on another device with networking disabled.
5. Inspect `dist/print.html` in print preview and print the urgent sections or full handbook.
6. Give a trusted nontechnical person a short findability test.
7. Replace stale offline and printed copies.

## Security

The generated HTML is not encrypted. Do not put passwords, recovery codes, private keys, security-question answers, or unnecessary complete account numbers in this repository.

Use the handbook to point family members to a separate protected inventory and credential-recovery process. Review repository history before making it public or sharing it.
