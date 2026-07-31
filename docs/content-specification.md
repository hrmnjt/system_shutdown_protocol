# Content specification v2

Status: **wife-first household-manual structure implemented in the 0.4 draft; personal completion, professional verification, print inspection, and wife usability testing remain pending**

This document is the product and content-design source of truth for System Shutdown Protocol.

## 1. Product definition

System Shutdown Protocol is a **household continuity manual with a short emergency guide at the front**. It is written by the owner directly to his wife and should help her understand how their shared life normally operates when he cannot explain it himself.

The guide covers the owner being:

- hospitalized but able to communicate;
- unable to communicate or unexpectedly uncontactable;
- incapacitated for a prolonged period; or
- dead.

The emergency itself does not define the whole information architecture. After the opening one or two pages, the handbook describes the ordinary operation of the household: people, ownership of responsibilities, routines, money, home, family care, health, work, residency, devices, records, wishes, and memory.

### Current reader

The current handbook is written directly for the owner’s wife. Use “I,” “you,” “our daughter,” “our dog,” and “our home.” It should feel like a thoughtful letter and practical manual from her husband, not an institution addressing a generic executor.

A later edition may cover the grave situation in which the wife is also unavailable. That audience requires different assumptions, a chosen coordinator order, more explanation, and separate testing. Do not mix that route into the current wife-first release.

### Household and jurisdiction context

- The owner is an Indian citizen living and working in Abu Dhabi.
- His wife and minor daughter are Indian citizens whose UAE residency depends on his sponsorship.
- The household includes one minor daughter and one dog.
- Assets, obligations, insurance, or property exist in both the UAE and India.
- Indian customs and appropriate UAE and Indian advice may affect medical, residency, guardianship, financial, and estate matters.

The handbook records intention, normal operation, questions, and protected locations. It must not invent legal authority or jurisdiction-specific procedure.

### Map, not vault

The handbook is a protected map to sensitive information, not the sensitive inventory itself. It may identify categories, responsibilities, approved contacts, dependencies, and how authorized access begins. Passwords, recovery codes, private keys, complete identifiers, detailed values, and bypass secrets stay in encrypted files and a password manager.

## 2. Product priorities

When requirements compete:

1. Help the wife identify the next safe action.
2. Show how the household normally works and what the owner usually handles.
3. Prevent urgent harm and irreversible mistakes.
4. Make ownership, cadence, dependencies, authority, and uncertainty explicit.
5. Keep changeable facts in one canonical place.
6. Make the hosted phone experience easy to scan.
7. Keep print and portable copies complete and dependable.
8. Keep preparation work visible but outside the wife’s main journey.

Experience priority remains:

1. authenticated hosted phone access;
2. printed handbook;
3. portable thumb-drive copy.

All formats contain the same released content and identity.

## 3. Information architecture

### Emergency entry point

- Start here

This is unnumbered and has a hard target of no more than two printed pages.

### Part I — First things to understand

1. How our household fits together
2. People to call
3. Access, identity, and authority

### Part II — How our household works

4. Our calendar and recurring routines
5. Our daughter and dog
6. Our home, property, and vehicles
7. Our money, bills, insurance, and taxes
8. My health and medical information
9. My work, our UAE residency, and travel
10. My devices and digital systems

### Part III — Wishes, memory, and legacy

11. My decisions and wishes
12. What I want to leave with you

### Useful tools

- A place to keep notes
- Help and glossary

### About and maintain this manual

- Known gaps
- Review and operations

Maintenance is included in every format but is not part of the wife’s first path through the manual.

## 4. Emergency-guide specification

The emergency guide is a routing layer, not a compressed copy of the manual.

### Required content

1. A short personal opening explaining why the owner made the manual.
2. Immediate danger before family coordination.
3. Three concise routes:
   - hospitalized and communicative;
   - unable to communicate or locate;
   - death.
4. A request to involve a trusted person and keep notes.
5. A short list of actions not to rush.
6. A link to the household overview.
7. A link to the note-taking tool.

### Excluded content

Move these into their canonical manual pages:

- full contact lists;
- complete document indexes;
- financial categories;
- detailed household routines;
- device inventories;
- lengthy legal caveats;
- owner-maintenance instructions.

### Acceptance criteria

- The print version occupies no more than two pages after the cover.
- The wife can identify the applicable route without reading the rest of the manual.
- Every link names its destination meaningfully in print and HTML.
- The page says what can wait, not only what to do.
- The language sounds like the owner speaking to his wife.

## 5. Household-manual content pattern

Subject pages should use a consistent operating model without turning every page into a rigid form. Use only headings relevant to that subject.

### What this covers

A short personal explanation of why the wife might need the page.

### How it normally works

Describe the normal state before discussing emergencies.

### Who normally handles it

Where relevant, distinguish:

- I normally handle;
- you normally handle;
- we share;
- an outside person or provider handles.

Do not invent ownership. Keep placeholders until discussed with the wife.

### When it happens

Record daily, weekly, monthly, annual, renewal-based, or event-driven cadence. The consolidated calendar owns the cross-household view.

### Where the details are

Point to protected records, encrypted files, the password manager, or an appropriate physical location without exposing secrets.

### Who can help

Point to the canonical contact directory and explain the helper’s scope.

### What should keep running

Identify services, payments, routines, and access routes whose interruption could create harm or compound other failures.

### What can wait

Explicitly reduce false urgency for a reader who may be frightened or grieving.

### If I cannot handle it

Give a concise handover note. Do not repeat the full emergency guide on every page.

### Last checked

Show the per-section verification date.

## 6. Page purposes

### 6.1 How our household fits together

**Purpose:** orient the wife before she opens detailed pages.

It records:

- household members and location;
- sponsorship dependency;
- what the owner handles, what the wife handles, and what is shared;
- the most important cross-system dependencies;
- the shared calendar and protected-information starting points;
- what should keep running and what can wait;
- links into the rest of the manual.

It should answer: “What parts of our life might I suddenly need to take over?”

### 6.2 People to call

**Purpose:** be the only canonical contact directory.

It includes trusted personal support, official emergency routes, employer/HR, school and care, medical and insurance contacts, veterinary help, property/service providers, technology help, and future professional advisers.

Each contact should explain what they can help with and any limits. Phone and email details should support one-tap actions when real information is added.

### 6.3 Access, identity, and authority

**Purpose:** explain how protected access begins, where identity and legal records are kept, what the owner intends the wife to handle, and what remains unverified.

It includes password-manager and encrypted-file entry points, physical documents, identity and civil records, incapacity/medical/financial authority, wills, intended executor status, nominees, beneficiaries, and professional-review gaps.

One person may fill several intended roles, but those capacities and supporting documents remain distinct.

### 6.4 Our calendar and recurring routines

**Purpose:** show the rhythm of the household across subject boundaries.

It includes:

- daily and weekly routines;
- monthly bills and tasks;
- annual renewals and obligations;
- event-driven review triggers;
- normal ownership of recurring work;
- source calendars and reminders;
- what must continue and what can wait.

Detailed instructions stay in the relevant subject page; this page owns the consolidated schedule.

### 6.5 Our daughter and dog

**Purpose:** preserve normal care and make it possible to hand a specific task to a trusted helper.

It includes routine, school, health, care contacts, identity/travel/residency records, payments, dog food/medicine/walking/veterinary care, ownership of routine tasks, and formal-authority caveats.

### 6.6 Our home, property, and vehicles

**Purpose:** explain normal household operation rather than merely inventory assets.

It includes access/security, utilities, household services, maintenance, warning signs, contractors, vehicles, renewals, UAE and Indian property obligations, what must run, and what can wait.

For important physical systems, record normal state, maintenance cadence, signs of failure, and whom to call.

### 6.7 Our money, bills, insurance, and taxes

**Purpose:** explain both what exists and how money normally moves through the household.

It includes income, essential outgoings, payment accounts by description, automatic and manual payments, ownership of financial routines, banking, investments, property, insurance, debts, tax, cross-border records, and the protected inventory.

Do not include credentials, complete numbers, private keys, or unnecessary values.

### 6.8 My health and medical information

**Purpose:** explain normal healthcare administration and what changes if the owner cannot communicate.

It includes insurer, usual providers, medicines and records, routine appointments, claims/approvals, protected medical details, emergency route, incapacity authority, what must continue, and what can wait.

### 6.9 My work, our UAE residency, and travel

**Purpose:** show how the owner’s employment connects to household income, benefits, insurance, sponsorship, company property, schedule, and travel.

It includes normal employment context, manager/HR, records and benefits, wife/daughter sponsorship, renewal calendar, travel information, questions for incapacity/death, Indian consular help, and appropriate UAE/Indian advice.

### 6.10 My devices and digital systems

**Purpose:** explain the dependency chain and ordinary operation of phones, email, devices, backups, accounts, hosting, and technical projects.

It includes ownership of technical work, phone/email, password manager, encrypted files, computers/backups, family files, essential services, domains/hosting/code, social accounts, renewals, helper boundaries, what must run, and what can wait.

### 6.11 My decisions and wishes

**Purpose:** record medical, personal, cultural, funeral, organ-donation, communication, and other decisions that may influence formal or time-sensitive action.

Keep wishes distinct from legal authority and link to formal records. This page owns decisions; it does not also carry the whole personal legacy.

### 6.12 What I want to leave with you

**Purpose:** preserve meaning rather than administration.

It includes a letter to the wife, messages for the daughter, family stories, values, lessons, photos, recordings, recipes, traditions, meaningful possessions, creative/technical work, privacy wishes, and people who can explain the owner’s life.

This page should not read like another checklist even if placeholders help the owner author it gradually.

### 6.13 A place to keep notes

**Purpose:** provide printable call, document-transfer, decision, and expense logs without browser persistence.

### 6.14 Help and glossary

**Purpose:** explain genuinely unfamiliar terms. Prefer plain language inline first.

### 6.15 Known gaps

**Purpose:** hold the complete owner-preparation backlog in one low-prominence place, classified as critical, important, or optional/future.

Missing values remain highlighted at their canonical location, but the wife-facing journey does not show project-style counts or repeated warning banners.

### 6.16 Review and operations

**Purpose:** define global review, per-section verification, release identity, hosted recovery, print/portable operation, stale-copy replacement, and usability testing.

## 7. Reusable information models

These models guide Markdown authoring; they do not require a database.

### Household responsibility

- Responsibility
- Purpose or consequence
- Normal owner: I / you / shared / outside help
- Cadence or trigger
- Source calendar
- Protected record
- Helper
- What must continue
- Safe delay or fallback
- Last checked

### Contact

- Role
- Person or organization
- Relationship
- Preferred contact method
- Phone and email
- What they can help with
- Limits
- Availability or timezone
- Last verified

### Authority or document

- Capacity or record
- Person or entity concerned
- Scenario
- Jurisdiction
- Intended / documented / verified / absent / unknown
- Protected location
- Custodian or adviser
- Limits and fallback
- Last verified

### Household system

- System or service
- Normal state
- What depends on it
- Normal owner
- Maintenance or renewal cadence
- Payment or protected record
- Signs of failure
- Provider or helper
- Safe stop or delay
- Last verified

### Financial obligation

- Purpose
- Jurisdiction
- Ownership context
- Normal timing
- Payment-source description
- Automatic or manual
- Protected record
- Authority warning
- Contact
- Consequence of interruption
- Last verified

### Protected-information locator

- Information category
- Why it matters
- Protected system
- How authorized access begins
- Prerequisites
- Helper or custodian
- Fallback
- Last access test
- Secrets explicitly excluded from the handbook

### Known gap

- Critical / important / optional
- What is missing
- Why it matters
- What is already known
- Safe fallback
- Preparation action
- Review trigger

## 8. Canonical ownership and cross-references

1. Changeable facts have one canonical location.
2. Direct contact details live in People to call.
3. The consolidated cadence lives in Our calendar and recurring routines.
4. Detailed normal operation lives in the relevant subject page.
5. Authority and document status lives in Access, identity, and authority.
6. Technical recovery detail lives in My devices and digital systems; Access, identity, and authority carries only the starting map.
7. Decisions live in My decisions and wishes; stories and messages live in What I want to leave with you.
8. Emergency pages repeat only stable safety principles and links.
9. Every cross-reference names its page and relevant heading for both screen and paper.
10. If safety requires a duplicated summary, identify the canonical record and include the duplication in review checks.

## 9. Language and presentation

- Write as a husband speaking to his wife.
- Use a natural paragraph before structured details.
- Use lists for actions, records, ownership, and cadence—not for every thought.
- Explain why a warning protects her instead of repeating institutional disclaimers.
- Say what can wait.
- Do not imply that she has to complete everything today or alone.
- Keep maintenance language in maintenance pages.
- Avoid percentage scores and raw placeholder counts in wife-facing pages.
- Preserve highlighted placeholders and one calm unfinished-details sentence per affected page.

## 10. Phone, print, portable, and search

### Phone

- Emergency guide is the default entry.
- Manual parts are visibly grouped.
- Household overview is the first manual destination.
- Records stack vertically rather than requiring wide-table scanning.
- Approved contact details support one-tap actions.
- Navigation works without JavaScript.

### Print

- Cover identifies the copy.
- Emergency guide is limited to the next one or two pages.
- Contents is grouped by the three manual parts.
- Every subject begins on a new page where practical.
- Version, global review, section verification, placeholders, known gaps, logs, and footers remain present.
- Browser print preview and a physical spot check are required.

### Portable

- `START HERE.html` opens directly under `file://`.
- Assets and links remain local and relative.
- The entire folder stays together.
- JavaScript failure does not block content or navigation.

### Search

- Search runs locally and sends no query or content to a service.
- Its index contains no information beyond the handbook.
- It uses portable relative targets.
- Navigation remains sufficient without search.

## 11. Review and version model

- `protocolVersion` identifies one released content version across all formats.
- `lastReviewed` changes only after the complete review.
- `lastVerified` records when one section’s volatile content was checked.
- Ownership and cadence are reviewed alongside factual accuracy.
- A released content change increments the version and requires redistribution.
- The wife may update practical information during prolonged incapacity using the same verification and release rules.

Review triggers include family, health, work, sponsorship, housing, property, vehicles, finance, insurance, devices, access, advisers, wishes, business interests, frequent travel, or jurisdiction changes.

## 12. Migration from the previous structure

The 0.4 reorganization:

- keeps Start here but constrains it to emergency routing;
- adds How our household fits together;
- adds Our calendar and recurring routines;
- groups the manual into essentials, household operation, and legacy;
- reframes existing subject pages around normal operation, ownership, cadence, dependencies, what must continue, and what can wait;
- splits formal/time-sensitive wishes from messages, memory, and legacy;
- retains tools, known gaps, and review operations at low prominence.

No useful personal or safety information should be deleted merely to fit the new hierarchy. Move it to its canonical owner instead.

## 13. Usability tests

### Wife — emergency test

Using a phone, without coaching:

1. Identify what to do if the owner cannot communicate.
2. Find time-sensitive wishes after death.
3. Identify one action to avoid and one thing that can wait.

### Wife — household-manual test

Without search first:

1. Explain what the owner normally handles.
2. Find the next annual residency or insurance task.
3. Find how an essential bill normally gets paid.
4. Find whom to call when a home or vehicle system fails.
5. Find the protected-information starting point.
6. Find a message or family memory that is not an administrative instruction.

Then repeat selected tasks with local search.

### Questions afterward

- Does this sound like me speaking to you?
- What did you expect to find somewhere else?
- Which part of our household is still invisible?
- What felt urgent even though it can wait?
- Which labels would you use instead?
- What would you want another person to take off your hands?

A backup-relative test belongs to the later edition designed for the situation in which the wife is also unavailable.

## 14. Acceptance criteria

The reorganization is technically complete when:

- all 12 numbered manual pages are present and grouped correctly;
- the emergency guide precedes the manual in every format;
- the printed emergency guide meets the two-page target in actual print preview;
- every reference page has `manualPart`, `lastVerified`, and `gapLevel` metadata;
- the validator enforces the section sequence and grouping;
- search includes every page with portable targets;
- the full print and portable packages validate;
- generated output is not committed.

The product is not ready for release until the wife has reviewed the language and hierarchy, personal placeholders are completed or accurately described as gaps, protected recovery works, applicable UAE and Indian matters have been professionally verified, and physical print/portable tests pass.
