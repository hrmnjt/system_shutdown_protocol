---
title: "Review and operations"
linkTitle: "Review & operations"
description: "How the handbook is verified, released, recovered, and kept consistent across all formats."
weight: 16
category: "maintenance"
lastVerified: "Not yet verified"
gapLevel: "important"
---

This page is primarily for me while I maintain the handbook. You may need to update practical information during a prolonged incapacity, but you should not have to think about this page during the first part of an emergency.

## What the protocol is and is not

The handbook is a protected map to contacts, responsibilities, authority status, and sensitive-information access routes. It is not a legal instrument, a credential store, a complete medical record, or proof that an intended person has authority.

## Global review and section verification

**Last reviewed** means the last date on which the complete protocol, every format, and the recovery routes were deliberately checked. It is not a Git date, build timestamp, or ordinary edit date.

**Section verified** means the volatile information in one subject section was checked on that section’s displayed date. Updating one section does not by itself change the global review date.

“Not yet reviewed” or “Not yet verified” means the applicable content remains a draft and must not be assumed complete.

## Full review procedure {#how-to-review}

1. **Emergency guide:** confirm it stays within the two-page print target, puts immediate danger first, and links to the right manual sections.
2. **Household overview:** verify the household, ownership of responsibilities, shared systems, and five most important dependencies.
3. **People:** contact the people who may support my wife and verify their details, availability, roles, and limits.
4. **Access and authority:** test protected access and verify incapacity, medical, financial, executor, nominee, beneficiary, and daughter-care documents with appropriate UAE and Indian guidance.
5. **Recurring calendar:** compare daily, monthly, annual, renewal, and event-driven tasks with actual calendars and records.
6. **Daughter and dog:** verify routines, carers, school, health, identity, travel, residency, veterinary, payments, and protected records.
7. **Home, property, and vehicles:** verify normal operation, access, utilities, maintenance, providers, renewals, and property obligations.
8. **Money:** compare income, bills, assets, liabilities, insurance, tax, property, and recurring obligations with protected records.
9. **Health:** verify normal care, insurer, claims, hospital, medical-record, and authority routes.
10. **Work, residency, and travel:** verify employer dependencies, benefits, company property, sponsorship, renewals, and travel records.
11. **Digital systems:** test phone/email continuity, password-manager and encrypted-file recovery, backups, hosting, and renewal dependencies without exposing secrets.
12. **Decisions and wishes:** review medical, cultural, funeral, repatriation, organ-donation, and communication wishes against formal records.
13. **Memory and legacy:** review personal letters, messages for our daughter, stories, photos, traditions, possessions, and creative work.
14. **Known gaps:** reclassify every gap, remove completed work, and preserve safe fallbacks for partial work.
15. **Hosted operation:** test authentication, denied access, recovery, logout, backups, payment continuity, monitoring, and revocation from a fresh phone and laptop.
16. **Offline and print:** test direct file access without networking, inspect print preview, test the actual thumb drive, and verify version/review identity.
17. **Usability:** ask my wife to complete emergency and household-manual tasks without coaching. Test a backup relative only after a later version is designed for the situation in which she is unavailable.
18. **Copies:** record current holders and replace or clearly mark stale copies.

Only after every applicable check should the global review date change.

## Per-section verification

When a subject section is verified:

- check every contact, status, dependency, protected location, fallback, and placeholder in that section;
- update its `lastVerified` value using an unambiguous written date;
- update the known-gaps page;
- increment the protocol version if released content changed; and
- redistribute affected released copies.

A section date must not claim legal validity. It records that the handbook entry was deliberately checked.

## Versioning and distribution

Hosted, printed, and portable are formats of one content version. Every release shows the same protocol version and global review date and contains the same handbook content.

- Hosted phone access is the primary experience.
- The printed handbook is the second priority and begins with the emergency quick guide.
- The portable thumb-drive copy is the serverless fallback.

Treat old paper and removable-media copies as uncontrolled until replaced or clearly marked stale.

## Hosted operations

Record and test:

- hosting account ownership and payment continuity;
- HTTPS and certificate renewal;
- authentication before handbook bytes are served;
- wife’s recovery without my devices or accounts;
- backups and restore procedure;
- private caching and security headers;
- logs and monitoring that do not expose handbook content;
- prevention of public repositories, buckets, and preview deployments; and
- logout, revocation, and service shutdown.

The server is rented. Hosting administrators, account compromise, backups, and snapshots are part of the threat model. `noindex` is not access control.

## Search operations

If local search is enabled, verify that it:

- sends no query or handbook content to a network service;
- indexes no information beyond the handbook itself;
- works without internet access where applicable;
- remains behind hosted authentication; and
- is optional because navigation works without JavaScript.

## Maintainers

- Ordinary maintainer: **[owner]**
- Maintainer during prolonged incapacity: **[wife, authority and process to verify]**
- Technical helper: **[canonical contact and limited scope]**

Wife-maintained changes use the same verification, version, redistribution, and stale-copy rules. Incident notes do not automatically become released handbook content.

## Copy register

| Copy | Location or holder | Version | Updated on |
|---|---|---|---|
| Authenticated hosted copy | [service and access owner] | [version] | [date] |
| Printed handbook | [secure location or holder] | [version] | [date] |
| Portable thumb-drive copy | [secure location or holder] | [version] | [date] |

## Review triggers

Review the relevant sections after changes to:

- family, dependants, pets, health, or wishes;
- employment, sponsorship, housing, property, vehicles, or insurance;
- banking, investments, debt, taxes, nominees, or beneficiaries;
- devices, phone numbers, email, password management, encrypted files, or hosting;
- intended representatives, executor, carers, advisers, or trusted contacts;
- UAE or Indian legal/procedural context; or
- business ownership, freelance work, frequent travel, or relevant countries.
