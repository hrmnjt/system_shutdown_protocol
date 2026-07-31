# System Shutdown Protocol

> Our household continuity manual

A household continuity manual authored in Markdown and published with [Hugo](https://gohugo.io/) as an authenticated hosted site, a printed handbook, and a portable offline copy.

## Purpose and audience

The current protocol is written directly from the owner to his wife. It helps her choose safe actions and find essential context when the owner is:

- hospitalized but able to communicate;
- unable to communicate or unexpectedly uncontactable;
- incapacitated for a prolonged period; or
- dead.

It is designed for an Indian family living in Abu Dhabi, with a minor daughter, a dog, UAE residency dependencies, and interests across the UAE and India. Legal, medical, employment, sponsorship, guardianship, financial, cultural, and estate procedures must be verified for the applicable circumstances; the project does not treat generic prose as legal authority.

The wife-facing experience is primary and should feel like a calm letter from the owner rather than an institutional procedure manual. Preparation, known gaps, review, and operations remain transparent in every format but do not lead the emergency journey. A later version may cover the grave situation in which the wife is also unavailable; that route is deliberately outside the current scope.

The approved information architecture and content model are in [`docs/content-specification.md`](docs/content-specification.md). A short scenario-based emergency guide leads into a structured manual covering household ownership, routines, family care, home, money, health, work and residency, digital systems, authority, wishes, and legacy. Personal information and professional verification remain deliberately incomplete.

Coding agents must read [`AGENTS.md`](AGENTS.md) before changing the project. It records product intent, invariants, security boundaries, unresolved work, and completion checks.

## Handbook security model

The handbook is a **protected map to sensitive information, not the sensitive inventory itself**. It may explain what categories exist, why they matter, whom to contact, and how an authorized person initiates access to protected encrypted files or a password manager.

Do not put passwords, password-manager master passwords, recovery codes, private or encryption keys, security-question answers, complete account/card numbers, unnecessary complete government identifiers, detailed financial values, alarm codes, or equivalent bypass secrets in the repository or generated files.

Directions to protected information are sensitive too. Hosted authentication must occur before handbook bytes are served. Printed paper and static offline files are not inherently encrypted and require deliberate physical protection.

## Build

Hugo extended v0.152 or later is recommended.

```sh
make build
```

The build cleans stale output and writes the offline-capable site to `dist/`. Open `dist/index.html` directly in a browser; no web server or internet connection is required. Copy the **entire** `dist/` directory, not only `index.html`.

Run the stricter build and offline-link validation with:

```sh
make check
```

For local authoring with automatic refresh:

```sh
make serve
```

The development server is only for editing. The generated files remain usable offline. The custom theme uses local assets, accessible Gruvbox Light and Dark palettes, and high-contrast, ink-conscious print styling.

## One version, three formats

All formats carry the same `params.protocolVersion` and `params.lastReviewed` values from [`hugo.toml`](hugo.toml) and contain the same released handbook content. They are formats of one version, not versions 1, 2, and 3.

Experience priority is:

1. authenticated hosted phone access;
2. printed handbook;
3. portable thumb-drive copy.

### Authenticated hosted copy

Deploy the complete `dist/` directory behind HTTPS and server-, proxy-, VPN-, gateway-, or platform-level authentication. A client-side password prompt is not access control. The generated `noindex`, `nofollow`, and `noarchive` directives reduce accidental indexing but provide no security.

Recovery must work for the owner’s wife without the owner’s phone, email, or already signed-in devices. Rented infrastructure introduces hosting-provider and administrator exposure and must be included in the threat model.

### Printed locker copy

Open `dist/print.html`, inspect every page in print preview, and print the complete handbook. The emergency guide has a hard target of one or two pages, followed by contents grouped into household-manual parts. The printout retains the version, global review date, per-section verification dates, privacy marking, known gaps, note forms, and stale-copy warning.

### Portable thumb-drive copy

```sh
make portable
```

This validates the build and creates a versioned folder under `release/` containing `START HERE.html` and `README.txt`. Copy the entire folder to the thumb drive. On a MacBook, double-click `START HERE.html`; it uses nearby files and needs no server or network connection.

See [`docs/distribution.md`](docs/distribution.md) for the complete release and security model.

## Edit content

Family-facing and maintenance pages live in [`content/`](content/). Follow [`docs/content-specification.md`](docs/content-specification.md): preserve the short emergency entry point, household overview, recurring calendar, three manual parts, useful tools, and low-prominence maintenance pages.

Write missing information in square brackets with a leading letter, for example:

```md
- Intended executor: **[person and verification status]**
```

Missing values remain visible at their canonical point of use. All preparation work belongs on one known-gaps page and is classified as critical, important, or optional/future review. Do not use a percentage-complete score or invent facts to make the draft look ready.

Changeable facts should have one canonical location. Emergency pages may repeat stable safety principles and warnings, but should link to canonical contacts, authority status, document locations, and protected-access routes.

## Review model

`params.lastReviewed` means the last complete, deliberate review of contacts, authority, documents, finances, access, responsibilities, wishes, gaps, hosted recovery, offline behavior, and print output. It is not a build timestamp or edit date.

The content model also uses per-section verification dates for volatile information. Updating one section does not by itself change the global review date.

Follow the review procedure before setting an unambiguous date such as:

```toml
lastReviewed = "15 January 2026"
```

Increment the protocol version when released content changes, rebuild all formats, and replace or clearly mark stale copies.

## Before distributing

1. Resolve placeholders or accurately classify the remaining gaps.
2. Verify that the emergency guide identifies immediate danger, the applicable scenario, a next safe action, and an action to avoid, and confirm it fits within two printed pages.
3. Complete the full review and set the version and global review date.
4. Run `make check`.
5. Test hosted authentication and recovery from a fresh phone session without the owner’s devices.
6. Test the phone layout and local search with networking disabled, then confirm emergency navigation still works with JavaScript unavailable.
7. Inspect the complete handbook in print preview and physically spot-check the emergency quick guide, records, and action log.
8. Run `make portable` and test `START HERE.html` from removable storage while offline.
9. Ask the wife to complete both emergency and household-manual tasks, then revise information ownership, labels, and language that do not match how she understands their life.
10. Replace stale offline and printed copies and record where current copies are held.
