# Agent context

Read this file before changing the repository. It records product intent and decisions that may not be obvious from the code alone.

## Why this project exists

“System Shutdown Protocol” is a household continuity manual for the owner’s wife to use when the owner is hospitalized, unable to communicate or be located, incapacitated, or dead. The family-facing subtitle is “Our household continuity manual.” It has two complementary dimensions:

1. **Family response and knowledge transfer (primary):** help the reader choose the next safe action and find contacts, authority, systems, assets, responsibilities, routines, and wishes.
2. **Preparation backlog (subordinate but transparent):** preserve work the owner still needs or intends to complete so unfinished plans and known gaps do not disappear.

The current handbook version is written directly for the owner’s wife, who understands the owner’s systems and is intended to coordinate across scenarios. It must read like a thoughtful letter and guide from the owner to her: use “I,” “you,” and “our,” acknowledge grief without dramatizing it, and combine warmth with clear next actions. Do not write about her in the third person inside family-facing pages. A later version may cover the grave situation in which she is also unavailable; do not dilute the current wife-first experience with generic backup-user routes before that edition is deliberately designed and tested. Markdown is the authoring format; generated HTML and paper are the family-facing formats.

The owner is an Indian citizen living and working in Abu Dhabi. The owner’s wife and minor daughter are Indian citizens whose UAE residency depends on the owner’s sponsorship; the household also includes one dog. Significant interests exist in both the UAE and India. Structure content by subject and label applicable jurisdiction rather than create parallel country handbooks. Never invent UAE, Indian, religious/personal-law, medical, financial, employer, sponsorship, guardianship, or estate facts. Require appropriate official or qualified advice where procedure or authority is unverified.

The approved information architecture is specified in `docs/content-specification.md` and implemented in the current `content/` structure. The product is a **household continuity manual with a short emergency guide at the front**. Preserve its one-to-two-page emergency entry, household overview, recurring calendar, three manual parts, content models, and migration decisions unless the owner approves a product change.

## Technology decision

Hugo was chosen intentionally as the static-site generator. The owner preferred it over MkDocs because of concern about disruptive MkDocs 2.0 changes. Do not migrate generators or introduce a remote Hugo theme without discussing it first.

The theme is custom, dependency-light, and uses accessible Gruvbox Light and Dark palettes. All runtime assets must remain local. The project targets modern household devices, primarily a MacBook and current phone browsers; preserve sound responsive and accessible basics without spending effort on obsolete browser compatibility.

## One version, three distribution formats

The repository treats hosted, printed, and portable delivery as **three formats of one content version** so stale copies can be identified reliably. Every format must show the same `protocolVersion` and `lastReviewed` values from `hugo.toml` and contain the same released handbook content.

Experience priority is: **authenticated hosted phone access first, printed handbook second, portable thumb-drive copy third**. This priority guides interaction design, not content divergence.

### Authenticated hosted copy

- This is the primary experience, especially on a current phone.
- The owner rents rather than physically controls the server; treat hosting administrators and infrastructure as part of the threat model.
- The exact deployment and access mechanism remain unresolved preparation items.
- Authentication must happen at the server, reverse proxy, VPN, identity gateway, or hosting layer **before handbook bytes are served**. Never implement a cosmetic password prompt or client-side-only encryption gate.
- Recovery must work for the wife without the owner’s phone, email, or already signed-in devices.
- Preserve responsive navigation, touch targets, HTTPS-oriented guidance, noindex/noarchive metadata, and the distinction that search directives are not access control.
- A future search enhancement must be entirely local/offline-capable, transmit no query or content, add no content beyond the handbook itself, and remain optional when JavaScript fails.

### Printed locker copy

- The complete handbook will be printed and stored with other valuables.
- `dist/print.html` is the print source.
- After identifying the copy, the first one or two substantive pages must be the emergency quick guide.
- Preserve the cover, version, global review date, per-section verification dates, build-for-print date, privacy marking, known gaps, highlighted placeholders, contents, print-safe records, action-log form, and section footers.
- Print output should be high contrast and ink-conscious rather than reproduce the Gruvbox screen background.
- Browser print preview and a physical spot check remain required because pagination varies by browser and printer.

### Portable thumb-drive copy

- A locally generated copy will be kept on a pendrive/thumb drive.
- A family member should be able to connect it to a MacBook and double-click `START HERE.html` without installing software, running a server, or using the internet.
- `make portable` creates the versioned package under `release/`.
- Keep assets local, links relative, pages flat, and home links explicit (`index.html`). Directory-only links such as `./` are ambiguous under `file://` and must not be reintroduced.
- Copying one HTML file is insufficient; the entire generated folder must remain together.

See `docs/distribution.md` for the detailed release and security model.

## Content and safety rules

- The handbook is a protected map to sensitive information, not the sensitive inventory itself.
- It may include deliberately approved minimum operational contact details, high-level categories, role/status information, and directions for initiating protected access.
- Never put raw passwords, password-manager master passwords, recovery codes, private or encryption keys, security-question answers, complete account/card numbers, unnecessary complete government identifiers, detailed financial values, alarm codes, or equivalent bypass secrets in the repository or generated site, search index, metadata, comments, or URLs.
- Sensitive details remain in encrypted files and a password manager. The wife must be able to initiate their tested recovery without relying on the owner’s phone, email, or existing session.
- Directions to protected information are themselves sensitive. Static HTML and printed paper are not encrypted; an unencrypted thumb drive is not encrypted. Do not imply otherwise.
- Legal, probate, nominee, beneficiary, guardianship, medical, residency, sponsorship, employment, and estate procedures depend on jurisdiction and circumstances. Preserve caveats and recommend appropriate UAE and Indian official or qualified advice rather than asserting a universal process.
- The wife is one person with different intended capacities: primary coordinator, intended representative during incapacity, and intended executor after death. Model these separately and never imply that one capacity proves another or that intention proves legal authority.
- Immediate danger takes precedence over family contact order: direct readers to the appropriate local emergency service first when life or safety may be at risk.
- Avoid irreversible-action language unless authority and jurisdiction are clear. Warn against prematurely closing accounts, cancelling the primary phone/email, erasing devices, moving or distributing money, surrendering records/equipment informally, or making unnecessary public disclosures.
- Provider and employer procedures change. Prefer intended outcomes, verified contacts, questions to ask, and tested access methods over copied, time-sensitive instructions.

## Unfinished work must stay visible

Missing information is a feature of the current draft, not something to hide cosmetically.

- A placeholder is written in square brackets beginning with a letter, for example `[name and phone number]`.
- Missing values remain visibly marked at their canonical point of use. Do not hide a critical missing executor or access route merely because it also appears in the backlog.
- Manage all preparation work on one known-gaps page, classified as **critical**, **important**, or **optional/future review**. Keep that page available in every format but subordinate to emergency and reference content.
- Avoid percentage-complete scores and raw placeholder counts in the wife-facing journey; they feel mechanical and do not communicate consequence. Preserve highlighted placeholder visibility, one calm unfinished-details note per affected page, and the severity-classified owner backlog.
- Markdown task boxes such as `- [ ]` are not placeholders. Emergency actions should be clearly noninteractive on screen; print may use checkboxes. Do not imply that browser task progress is saved.
- Remove a gap only when genuinely complete. For partial work, explain what exists, where it is, the safe fallback, and what remains.
- If changing placeholder rendering, preserve visibility on screen and paper.
- Do not make validation fail merely because known placeholders remain; validation should report them and preserve their severity labels.

## Meaning of review and version fields

`lastReviewed` is not a Git commit date, file modification date, or build timestamp. It means the maintainer deliberately completed the full review of contacts, authority, documents, finances, access, responsibilities, wishes, gaps, hosted recovery, offline behavior, and print output. Follow the review procedure before changing it.

The content model also has a per-section verification date for volatile information. A section date may change after that section is checked; it does not change the global full-review date. The owner ordinarily maintains the guide, and the wife may maintain it during prolonged incapacity.

Increment `protocolVersion` when distributed content changes. Hosted, print, and portable copies from one release carry the same version and global review date. Treat old paper and removable-media copies as uncontrolled until replaced or clearly marked stale.

## Theme and experience invariants

- The emergency guide is scenario-based, unnumbered, and limited to a hard target of one or two printed pages. It routes into the manual rather than duplicating it.
- The numbered handbook is a household operating manual grouped as: first things to understand; how our household works; and wishes, memory, and legacy. Do not restore “first 24 hours / first week” as primary navigation and do not frame every subject page as an emergency procedure.
- Manual pages explain normal operation, who handles it, cadence, protected records, helpers, what must keep running, what can wait, and the concise handover when the owner cannot handle it.
- Family actions and reference information come before owner-maintenance material. Maintenance remains available but low prominence.
- Immediate danger and scenario choices come before project explanation, copy administration, or completeness counts.
- Write as the owner speaking directly to his wife. Prefer warm, natural sentences over schema labels, institutional phrasing, or repeated disclaimers. Keep lists for actions and reference facts, but introduce them in a human voice.
- Keep changeable facts in one canonical section and link to the exact page and heading. Do not casually duplicate contacts, document locations, authority status, or access instructions.
- Distinguish the next safe action, the intended coordinator, and verified legal authority.
- Do not rely on colour alone. Preserve text labels, symbols, semantic HTML, keyboard focus, forced-colour support, reduced-motion handling, and readable contrast.
- Treat current phone browsers as the primary screen experience. Use stacked records instead of wide tables where phone use would otherwise require horizontal scanning. Keep desktop/laptop usable.
- Mobile navigation and emergency routes must remain available without JavaScript. JavaScript may progressively enhance copy labels, navigation, local search, and printing.
- Keep print support first-class, including the emergency quick guide and action-log form.
- Do not add external fonts, CDN assets, analytics, trackers, service workers, or network-required search. These can break offline use or leak sensitive access patterns.
- Do not add browser persistence for checklist or action-log state without a separate explicit product decision; stale device-local state can mislead across copies.

Design references and rationale are recorded in `docs/inspirations.md`.

## Repository map

- `content/` — family-facing Markdown and maintenance pages
- `content/_index.md` — “Start here” page
- `content/todo.md` — visible unfinished-work backlog
- `content/preparedness.md` — review meaning and procedure
- `layouts/` — custom Hugo templates, including the combined print handbook
- `static/css/site.css` — responsive Gruvbox and print styling
- `static/js/` — local progressive enhancement only
- `docs/content-specification.md` — approved target information architecture, content models, migration map, and acceptance criteria
- `docs/distribution.md` — release formats and deployment constraints
- `docs/inspirations.md` — source and design references
- `scripts/validate_build.py` — offline, semantic, sequence, and print checks
- `scripts/package_portable.py` — versioned thumb-drive package
- `dist/` and `release/` — generated and ignored; do not commit them

## Commands and completion checks

```sh
make serve      # live authoring preview
make build      # clean production build in dist/
make check      # clean strict build plus validation
make portable   # validated versioned thumb-drive package
```

Before considering a theme, build, or distribution change complete:

1. Run `make check` or its equivalent if `make` is unavailable.
2. Confirm `dist/index.html` opens directly via `file://` with networking disabled.
3. Confirm phone and laptop layouts remain usable.
4. Inspect `dist/print.html` in print preview for clipping and pagination.
5. Run `make portable` and test `START HERE.html` from the generated package.
6. Keep section weights sequential; the validator enforces this.
7. Keep the working tree free of generated `dist/` and `release/` files.

## Current unresolved preparation and implementation work

- Complete and verify the household overview, recurring calendar, ownership of responsibilities, normal-operation details, and personal legacy content; the implemented information architecture remains a placeholder-heavy draft.
- In a later version, design the separate experience for the grave situation in which the wife is unavailable, then choose and test an ordered backup coordinator chain. This is not part of the current wife-first release.
- Verify UAE and Indian wills, incapacity/medical/financial authority, intended executor documentation, nominees, beneficiaries, guardianship/care arrangements, and applicable customs with appropriate advice.
- Establish UAE and Indian legal, financial, and tax advisers or verified official routes.
- Verify the employer emergency process and the UAE sponsorship implications for the wife and daughter.
- Complete real contacts, protected document/inventory routes, responsibilities, and time-sensitive cultural, funeral, repatriation, and organ-donation wishes.
- Test and refine the implemented per-section dates, severity-aware gap presentation, phone-first emergency routing, print quick reference, action log, and local search with real content and family usability sessions.
- Decide hosted provider, authentication, recovery, backups, headers, private caching, monitoring, and revocation. Treat rented infrastructure as third-party exposure.
- Decide whether the thumb drive relies on physical security or encryption with separately recoverable access.
- Record final physical locations and holders of current copies.
- Add business-interest or frequent-travel content only if those circumstances arise; retain them as review triggers now.

Consult `docs/content-specification.md` and the current known-gaps content before consequential changes. Ask the owner rather than making personal, legal, cultural, or procedural assumptions.
