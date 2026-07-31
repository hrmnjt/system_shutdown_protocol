# Distribution model

System Shutdown Protocol has one content version and three distribution formats. A release is complete only when hosted, printed, and portable copies contain the same handbook content and show the same protocol version and global review date.

The experience priority is:

1. authenticated hosted phone access;
2. printed handbook;
3. portable thumb-drive copy.

This ordering guides usability decisions. It does not permit one format to contain an older or reduced handbook.

## Shared release identity

Set these values in `hugo.toml` before release:

```toml
protocolVersion = "1.0"
lastReviewed = "15 January 2026"
classification = "Private family document"
```

Increment `protocolVersion` whenever distributed content changes. Updating a typo that has not been distributed does not need a new release; changing a released contact, authority status, location, process, gap, or wish does.

`lastReviewed` identifies the last complete deliberate review, not the build date. Subject pages also show per-section verification dates. A section verification does not change the global review date by itself.

Do not describe hosted, print, and portable as versions 1, 2, and 3. They are formats of the same version, so an old copy cannot appear authoritative merely because of its format name.

## Shared information-security boundary

The handbook is a protected map to sensitive information, not the sensitive inventory itself. All formats may contain approved minimum operational contact details, high-level categories, role/status information, and directions for initiating protected access. They must not contain passwords, password-manager master passwords, recovery codes, private or encryption keys, security answers, complete account/card numbers, unnecessary complete government identifiers, detailed financial values, alarm codes, or equivalent bypass secrets.

Credentials and sensitive details remain in encrypted files and a password manager. Recovery must be tested and must not depend solely on the owner’s phone, email, or existing signed-in devices.

Directions to protected information are sensitive. Hosted access controls and physical control of paper and removable media are therefore all necessary. None of the formats should be described as risk-free.

## Authenticated hosted copy

**Purpose:** primary responsive access from a phone, with laptop support, when the owner cannot provide context.

The default page is the emergency quick guide. It must route immediate danger first, then communicative hospitalization, inability to communicate or locate, and death. Family actions and reference information appear before owner maintenance.

The static handbook does not implement its own password prompt. A password check written in HTML or browser JavaScript exposes content and password material to anyone who can download the files. Protect the site before any handbook bytes or local search index are served.

The owner rents the hosting infrastructure. Treat the hosting provider, infrastructure administrators, account compromise, logs, backups, snapshots, and preview deployments as part of the threat model.

Minimum deployment properties:

- HTTPS only, with automatic certificate renewal;
- authentication at a reverse proxy, access gateway, VPN, or hosting platform;
- recovery that the owner’s wife can perform without the owner’s phone, email, or already signed-in devices;
- rate limiting and logs that do not record handbook content, secrets, or search queries;
- `Cache-Control: private, no-store` where practical;
- appropriate security headers, including a restrictive Content Security Policy;
- no public repository, object-storage bucket, build artifact, preview deployment, or search indexing;
- protected backups and a documented restore test;
- a documented way to revoke access;
- monitoring that does not become a hidden dependency for family access;
- a payment and ownership plan that does not silently fail when the owner cannot maintain the service.

The generated `noindex`, `nofollow`, and `noarchive` directives reduce accidental indexing but provide no access control. A shared password is simple but difficult to rotate and audit. An identity-aware proxy or VPN can be stronger but only if its recovery path remains usable in the target emergency.

A future search feature must be generated and executed locally, transmit no query or handbook content, add no content beyond what is already in the handbook, work offline where technically feasible, and remain an enhancement rather than the only navigation route. Its index receives the same access protection as every HTML page.

Test on a current phone and laptop from fresh unauthenticated sessions. Confirm denied access, login, logout, recovery, timeout behavior, and restored access after backup. Test emergency navigation without JavaScript and search with networking disabled.

## Printed locker copy

**Purpose:** a durable, discoverable copy kept with other important physical documents and valuables.

`dist/print.html` is the print source. After any cover information required to identify the copy, the emergency quick guide should occupy the first one or two substantive pages. The complete handbook follows, including the known-gaps and review/operations sections.

Release procedure:

1. Complete the full review and set the version and global review date.
2. Confirm applicable per-section verification dates.
3. Run `make check`.
4. Open `dist/print.html` in a modern browser.
5. Inspect the emergency quick guide, section starts, records, tables, action-log form, and placeholders for clipping or ambiguous pagination.
6. Print the complete document, including the cover, emergency guide, known gaps, and review identity.
7. Confirm the physical copy’s version and review date.
8. Put it in the agreed secure location and destroy or clearly mark stale copies.

The printed copy points to protected credentials rather than containing them. Paper cannot be remotely revoked and may be photographed, removed, annotated, or become outdated. Print styling should remain high contrast and ink conscious.

The family may annotate the printed handbook or action-log forms during an incident. Those annotations are operational records, not automatically authoritative updates to the released handbook.

## Portable thumb-drive copy

**Purpose:** a serverless fallback that can be opened directly on a family MacBook without software installation or internet access.

Create it with:

```sh
make portable
```

Copy the generated versioned folder from `release/` to the thumb drive without moving files out of it. `START HERE.html` is a duplicate entry point; its links intentionally target explicit HTML files so `file://` browsing does not depend on web-server directory behavior.

Test procedure:

1. Eject and reconnect the drive.
2. Disable Wi-Fi.
3. Double-click `START HERE.html` in Finder.
4. Confirm the emergency quick guide is the entry point.
5. Navigate through every section and open the printable handbook.
6. Test local search, if implemented, without networking; confirm navigation still works if JavaScript is disabled.
7. Repeat on a second Mac user account if practical.
8. Confirm the displayed version and review dates.

An unencrypted drive is easiest to use but depends entirely on physical security. An encrypted drive improves confidentiality but creates another recovery dependency. Make that trade-off deliberately and record its recoverable access method outside the drive. Copy the complete folder; a single HTML file is not the portable handbook.

## Cross-format usability validation

Before the wife-first release, conduct the private scenarios described in `docs/content-specification.md`. The owner’s wife should use a phone to respond to inability-to-communicate and death scenarios, identify a next safe action and an action to avoid, and explain the difference between coordination and verified authority. She should also review whether the words sound like her husband speaking to her rather than an institution instructing her.

A backup-relative test belongs to a later edition designed for the grave situation in which the wife is also unavailable. Do not claim that the current wife-first release supports that audience.

Technical link validation does not replace this test.

## Release checklist

- [ ] Family content matches `docs/content-specification.md`.
- [ ] The emergency quick guide is the default hosted/portable entry point and leads the printed handbook.
- [ ] Immediate danger takes precedence over family coordination.
- [ ] Wife and daughter sponsorship dependencies are represented without unverified procedural claims.
- [ ] Incapacity authority and executor authority are distinguished even when intended for the same person.
- [ ] Known gaps and highlighted placeholders accurately describe missing information.
- [ ] No handbook format or search index contains credentials, complete sensitive identifiers, or bypass secrets.
- [ ] Protected encrypted-file and password-manager recovery is tested without the owner’s devices.
- [ ] Version, global review date, and applicable section dates are updated.
- [ ] `make check` passes.
- [ ] Hosted authentication and recovery pass fresh phone and laptop tests.
- [ ] Printed format passes print preview and physical spot checks.
- [ ] Portable format passes removable-storage and offline tests.
- [ ] Wife-facing scenario and natural-language review is completed without coaching.
- [ ] Stale copies are replaced or clearly marked.
- [ ] Current copy locations and holders are recorded.
