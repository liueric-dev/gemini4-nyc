# Tenant advocate app: plan

Planning for the Gemini 4 NYC Hackathon (Sat Nov 21, 2026). Rules and judging: [REQUIREMENTS.md](REQUIREMENTS.md). Model capabilities: [GEMINI.md](GEMINI.md). Data collection: [../data/README.md](../data/README.md).

This doc records only what has been decided. Anything not yet decided is under [Open questions](#open-questions).

## Planning process

| # | Step | Status |
|---|---|---|
| 1 | Understand the requirements | Mostly done; Discord `#rules` not yet read |
| 2 | Pick the user and the problem | Done |
| 3 | Define the demo and the proof | Main flow decided; details deferred |
| 4 | Scope: must-have, nice-to-have, cut | Done |
| 5 | App requirements | Shared requirements defined; details next |
| 6 | System design | Not started; includes how the app stores and structures the data |
| 7 | Prep work allowed before the event | Data collection instructions written; prep items listed below |

## Users

NYC renters and tenants.

## Problem

Landlords have a lot of leverage over tenants. Tenants often don't know their rights or the help available to them, and find it hard to navigate the legal system or escalate problems with their landlord.

**Problem statement:** NYC tenants have problems they can't prove or escalate. The app turns what they record into evidence tied to the specific law, and the next step to take.

## Product

One tenant advocate app that helps the tenant with whatever problem they have.

The core is media evidence, mostly video, along with photos and audio, tied back to NYC housing laws, rules and regulations.

### How every feature works

1. **Capture.** The tenant records video, photos or audio.
2. **Observe.** The app describes what is actually in the media.
3. **Map to the law.** Each observation is matched to the specific rule it breaks. NYC housing law is the knowledge base for this step, and the app cites only rules it retrieved.
4. **Act.** The app tells the tenant their rights and responsibilities and how to escalate, then drafts what they need: emails, letters or forms to the landlord, to a city agency, or for court.

## Demo and proof

**Main flow:** video or photo → the law it breaks → the tenant's rights and next steps → a referral to the right agency, or a drafted letter or complaint.

The demo walks through that whole flow.

**Test media:** gathered entirely from public, licensed sources. No personal or friends' clips. See [../data/README.md](../data/README.md).

## Must-haves

1. Upload a video or photo, with optional spoken narration.
2. Identify the problems in it: what each one is, where it appears (timestamp or frame), and an honest "nothing found" when that's the case.
3. Cite the law each problem breaks, along with its severity class and the landlord's repair deadline.
4. Explain the tenant's rights, the landlord's duties, the tenant's own responsibilities, and how to escalate.
5. End with either a referral to the right agency, or a drafted letter or complaint.
6. An evaluation that scores the system on the test set against a single-call baseline.

## Shared requirements

Almost every feature, must-have or not, is built from these nine pieces.

| # | Building block | What it has to do |
|---|---|---|
| A | **Media intake** | Accept phone video, photos and audio. Pull out frames and clips. Transcribe narration in any language. |
| B | **Problem list** | A fixed list of problem types the app recognizes (leak, mold, pests, no heat, missing window guard…). Each type maps to HPD violation descriptions and code sections. This is the foundation: detection, law matching, the Decisions API checklist and the test-set labels all depend on it. |
| C | **Observation** | Detect problems from the list, with a timestamp or frame, a confidence score, and how bad it looks. |
| D | **Law base** | Every section with its citation, text, severity class, repair deadline and when it applies. Retrieval only returns real sections, so nothing gets made up. |
| E | **Tenant and building facts** | Some laws depend on things you can't see: a child under 6 (lead paint) or under 11 (window guards), when the building was built (lead is presumed before 1960), how many units, whether the apartment is rent-stabilized, whether it's heat season. These come from a few short questions to the tenant, or from the building lookup. |
| F | **Next steps** | For each problem type, the path from notifying the landlord, to 311/HPD, to an HP action or DHCR complaint. Includes the agencies, contacts, timelines and the anti-retaliation protection. |
| G | **Documents** | Templates for a letter to the landlord, the text of a 311 complaint, an evidence packet for an HP action, and a DHCR complaint. Each gets filled in with the facts and evidence. |
| H | **Case record** | Problems, evidence, dates and actions taken, kept per tenant. Features that track over time need this. |
| I | **Evaluation** | The labeled test set, a baseline, a scoring script and a write-up of the failures. |

Must-haves use A, B, C, D, F, G and I. They also use part of E, because without some tenant and building facts some of the law matching will be wrong.

## Priority list after the must-haves

Worked through in order if there's time. "Uses" lists the shared building blocks each feature relies on.

| # | Feature | Uses | What it adds |
|---|---|---|---|
| 1 | Building and landlord history | E | Open Data lookup |
| 2 | Multilingual narration | A | Almost nothing extra |
| 3 | Anti-retaliation notice | F | Content only |
| 4 | Heat and hot water | A, C, D, E | Reading the thermometer; outdoor temperature by date and time |
| 5 | Neglect over time | C, H | Comparing clips of the same spot taken on different dates |
| 6 | Pre-lease tour | C, D | Different output: questions to ask the landlord before signing |
| 7 | Move-in/move-out record | C, H | Comparing the two; the security deposit rules |
| 8 | Managed Agents daily check | E, H | A scheduled job that checks HPD records and repair deadlines |
| 9 | Court paper decoder | A, D, F, G | Reading documents; deadlines |
| 10 | Good Cause check | D, E | Exemption rules; the landlord's portfolio |
| 11 | Harassment timeline | A, D, H | Audio and text intake; the legal definitions of harassment |
| 12 | Lease check | A, D | Reading documents; rules on illegal clauses |
| 13 | Shopify tie-in | B | Mapping problem types to products; only for problems that are the tenant's responsibility |
| 14 | ADA, rent overcharge, neighbor organizing | — | Each is mostly its own build |

## Prep now (no app code)

- **Data collection:** run [../data/README.md](../data/README.md) in a separate session.
- **B, the problem list.** The most valuable item. Depends on the HPD violation list from the data collection.
- **E, the questions for the tenant:** which facts change which laws apply.
- **F, the escalation path for each problem type.**
- **G, the content of the templates:** letter, 311 complaint, evidence packet.
- **I, the labeling rubric** for the test set, so labels match the problem list.

## Open questions

### Demo and proof (deferred)
- Demo inputs: what gets recorded live at the venue, and whether judges pick from a held-out set of clips.
- What judges see at the end.
- Baseline to compare against.
- What to measure.

### Rules
- What prep the Discord `#rules` allow before the event, including whether template content written in advance counts as pre-built work.

### Logistics
- Team size and skills.
