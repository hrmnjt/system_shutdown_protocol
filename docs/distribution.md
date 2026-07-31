# Distribution model

The protocol has one content version and three distribution formats. A release is complete only when the intended formats show the same protocol version and review date.

## Shared release identity

Set these values in `hugo.toml` before release:

```toml
protocolVersion = "1.0"
lastReviewed = "15 January 2026"
classification = "Private family document"
```

Increment `protocolVersion` whenever distributed content changes. Updating a typo that has not been distributed does not need a new release; changing a released contact, location, process, TODO, or wish does.

Do not describe print, hosted, and portable as versions 1, 2, and 3. They are different formats of the same version. This prevents a family member from mistaking an older printed copy for the authoritative copy merely because it was called “version 1.”

## Format A: printed locker copy

Purpose: a durable, discoverable copy kept with other important physical documents and valuables.

Release procedure:

1. Complete the review and set the version and review date.
2. Run `make check`.
3. Open `dist/print.html` in a modern browser.
4. Inspect print preview for clipped tables, isolated headings, unexpected blank pages, and placeholder visibility.
5. Print the complete document, including the cover and TODO section.
6. Confirm the physical copy’s version and review date.
7. Put it in the agreed locker location and destroy or clearly mark stale copies.

The printed copy should point to protected credentials rather than contain them. Paper cannot be remotely revoked and may be photographed, removed, or become outdated.

## Format B: authenticated hosted copy

Purpose: responsive access from a laptop or phone when the physical or portable copy is unavailable.

The static theme does not implement a password prompt. A password check written in HTML or browser JavaScript would expose the content and password material to anyone who can download the files. Protect the site before any handbook bytes are served.

Minimum deployment properties:

- HTTPS only, with automatic certificate renewal;
- authentication at a reverse proxy, access gateway, VPN, or hosting platform;
- a recovery method that at least one trusted family member can actually obtain;
- rate limiting and logs that do not record handbook content;
- `Cache-Control: private, no-store` where practical;
- security headers appropriate for a static site, including a restrictive Content Security Policy;
- no public repository, public object-storage bucket, preview deployment, or search indexing;
- a tested backup and a documented way to revoke access;
- monitoring that does not become a hidden dependency for family access.

The generated `noindex`, `nofollow`, and `noarchive` directives reduce accidental indexing but provide no access control. A single shared password is simple but difficult to rotate and audit. An identity-aware proxy or VPN can offer stronger access, but its account-recovery path must remain usable after the owner’s death.

Test at both phone and laptop widths, from a device that is not already authenticated. Confirm that logout, password recovery, and denied access behave as expected.

## Format C: portable thumb-drive copy

Purpose: a serverless copy that can be opened directly on a family MacBook.

Create it with:

```sh
make portable
```

Copy the generated versioned folder from `release/` to the thumb drive without moving files out of it. `START HERE.html` is a duplicate entry point; its links intentionally target explicit HTML files so `file://` browsing does not depend on web-server directory behavior.

Test procedure:

1. Eject and reconnect the drive.
2. Disable Wi-Fi.
3. Double-click `START HERE.html` in Finder.
4. Navigate through every section and open the printable handbook.
5. Repeat on a second Mac user account if practical.
6. Confirm the displayed version and review date.

An unencrypted drive is easiest for family to use but depends entirely on physical security. An encrypted drive provides better confidentiality but creates another password-recovery dependency. Make that trade-off deliberately and record the access method outside the drive.

## Release checklist

- [ ] Content review is complete.
- [ ] TODOs and highlighted placeholders accurately describe all known gaps.
- [ ] Version and review date are updated.
- [ ] `make check` passes.
- [ ] Printed format passes print preview and physical spot checks.
- [ ] Hosted authentication is tested from fresh phone and laptop sessions.
- [ ] Portable format is tested from removable storage while offline.
- [ ] A trusted nontechnical person can find the first action and key contact.
- [ ] Stale copies are replaced or clearly marked.
- [ ] Copy locations and holders are recorded in the protocol.
