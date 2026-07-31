# Agent context

Read this file before changing the repository. It records product intent and decisions that may not be obvious from the code alone.

## Why this project exists

“System Shutdown Protocol” is a personal continuity handbook for the owner’s family to use after the owner dies. It has two equally important dimensions:

1. **Knowledge transfer:** explain information, systems, contacts, responsibilities, assets, and routines that the family may not currently know.
2. **Preparation backlog:** preserve work the owner still needs or intends to complete so that unfinished plans and known gaps do not disappear with the owner.

The audience is primarily nontechnical family members who may be grieving or under stress. The family-facing experience must therefore be calm, plain-language, easy to navigate, and explicit about uncertainty. Markdown is the owner’s authoring format; generated HTML and paper are the family-facing formats.

The repository currently contains a generic structure and many placeholders. The owner intends to focus on content organization and personal content after the theme and distribution foundations are satisfactory. Do not invent personal, legal, financial, or jurisdiction-specific facts to make the handbook look complete.

## Technology decision

Hugo was chosen intentionally as the static-site generator. The owner preferred it over MkDocs because of concern about disruptive MkDocs 2.0 changes. Do not migrate generators or introduce a remote Hugo theme without discussing it first.

The theme is custom, dependency-light, and uses accessible Gruvbox Light and Dark palettes. All runtime assets must remain local. The project targets modern household devices, primarily a MacBook and current phone browsers; preserve sound responsive and accessible basics without spending effort on obsolete browser compatibility.

## One version, three distribution formats

The owner originally described these as versions 1, 2, and 3. The repository treats them as **three formats of one content version** so stale copies can be identified reliably. Every format must show the same `protocolVersion` and `lastReviewed` values from `hugo.toml`.

### A. Printed locker copy

- The complete handbook will be printed and stored in a locker with other valuables.
- `dist/print.html` is the print source.
- Preserve the cover, version, review date, build-for-print date, privacy marking, TODOs, highlighted placeholders, contents page, print-safe tables, and section footers.
- Print output should be high contrast and ink-conscious rather than reproduce the Gruvbox screen background.
- Browser print preview and a physical spot check remain required because pagination varies by browser and printer.

### B. Authenticated hosted copy

- A future copy will be hosted on a server and usable from both laptops and phones.
- The exact deployment and password/access mechanism are deliberately unresolved TODOs.
- Authentication must happen at the server, reverse proxy, VPN, identity gateway, or hosting layer **before handbook bytes are served**. Never implement a cosmetic password prompt or client-side-only encryption gate.
- Preserve responsive navigation, touch targets, HTTPS-oriented guidance, noindex/noarchive metadata, and the distinction that search directives are not access control.
- Recovery must work for trusted family members without relying exclusively on the owner’s normal signed-in devices.

### C. Portable thumb-drive copy

- A locally generated copy will be kept on a pendrive/thumb drive.
- A family member should be able to connect it to a MacBook and double-click `START HERE.html` without installing software, running a server, or using the internet.
- `make portable` creates the versioned package under `release/`.
- Keep assets local, links relative, pages flat, and home links explicit (`index.html`). Directory-only links such as `./` are ambiguous under `file://` and must not be reintroduced.
- Copying one HTML file is insufficient; the entire generated folder must remain together.

See `docs/distribution.md` for the detailed release and security model.

## Content and safety rules

- Never put raw passwords, password-manager master passwords, recovery codes, private keys, security-question answers, or unnecessary complete account numbers in the repository or generated site.
- The handbook should point to a separate protected inventory, emergency-access process, sealed material, or trusted contact.
- Static HTML, printed paper, and an unencrypted thumb drive are not encrypted. Do not imply otherwise.
- Legal, probate, nominee, beneficiary, guardianship, medical, and estate procedures depend on jurisdiction. Preserve caveats and recommend qualified local advice rather than asserting a universal process.
- Avoid irreversible-action language unless authority and jurisdiction are clear. The existing content intentionally warns against immediately closing accounts, erasing devices, moving money, or distributing property.
- Provider-specific procedures change. Prefer intended outcomes and links to tested access methods over copied, time-sensitive instructions.

## Unfinished work must stay visible

Missing information is a feature of the current draft, not something to hide cosmetically.

- A placeholder is written in square brackets beginning with a letter, for example `[name and phone number]`.
- The theme highlights placeholders, shows quiet counts in page headers and home-page cards, and summarizes affected sections in the printed contents. Avoid repeating warning banners or callouts for the same unfinished details.
- Markdown task boxes such as `- [ ]` are not placeholders.
- `content/todo.md` is family-visible by design. Remove an item only when it is genuinely complete. For partial work, explain what exists and what remains.
- If changing placeholder rendering, preserve visibility on screen and paper.
- Do not make validation fail merely because known placeholders remain; `make check` reports their count instead.

## Meaning of review and version fields

`lastReviewed` is not a Git commit date, file modification date, or build timestamp. It means the owner deliberately verified contacts, authority documents, document locations, finances, access, responsibilities, wishes, TODOs, offline behavior, hosted access where applicable, and print output. Follow `content/preparedness.md` before changing it.

Increment `protocolVersion` when distributed content changes. Print, hosted, and portable copies from one release should carry the same version and review date. Treat old paper and removable-media copies as uncontrolled until replaced or clearly marked stale.

## Theme and experience invariants

- Family instructions come before owner-maintenance material.
- Immediate tasks are ordered by urgency; users are not expected to finish everything at once.
- Use plain language suitable for a stressed, nontechnical reader.
- Do not rely on colour alone. Preserve text labels, symbols, semantic HTML, keyboard focus, forced-colour support, reduced-motion handling, and readable contrast.
- Keep desktop/laptop and phone layouts usable. Mobile navigation should be compact but must remain available without JavaScript.
- Keep the site usable when JavaScript fails; JavaScript may progressively enhance copy labels, mobile navigation, and printing.
- Keep print support first-class.
- Do not add external fonts, CDN assets, analytics, trackers, service workers, or network-required search. These can break offline use or leak sensitive access patterns.
- Do not casually add browser persistence for checklist state; state could become stale, device-specific, or misleading across copies.

Design references and rationale are recorded in `docs/inspirations.md`.

## Repository map

- `content/` — family-facing Markdown and maintenance pages
- `content/_index.md` — “Start here” page
- `content/todo.md` — visible unfinished-work backlog
- `content/preparedness.md` — review meaning and procedure
- `layouts/` — custom Hugo templates, including the combined print handbook
- `static/css/site.css` — responsive Gruvbox and print styling
- `static/js/` — local progressive enhancement only
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

## Current unresolved decisions

- Jurisdiction and corresponding legal/procedural guidance
- Real contacts, document locations, financial inventory, responsibilities, and wishes
- Final content organization and wording
- Hosted provider, authentication method, recovery flow, backups, headers, monitoring, and revocation
- Whether the thumb drive relies on locker security or uses encryption with separately recoverable access
- Final physical locations and holders of current copies

Consult `content/todo.md` for the family-visible backlog. Ask the owner before making consequential assumptions in these areas.
