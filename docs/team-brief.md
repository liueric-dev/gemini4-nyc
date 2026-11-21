# Team brief: the NYC tenant advocate app

A catch-up guide for the team at the Gemini 4 NYC Hackathon (Saturday, November 21, 2026). No technical background needed. It covers what we're building, who it's for, why it matters, what it must do, and how we'll show it works.

It is deliberately long. Shorten it or split it into separate Notion pages however suits you.

> **One-line pitch:** A New York City tenant takes a photo or video of a problem in their apartment. The app works out what's wrong, finds the exact city or state rule it breaks, explains the tenant's rights, and drafts the letter or complaint they need to get it fixed.

---

## 1. The hackathon in brief

**Where and when:** The Malin Chelsea, 220 W 26th St. Hacking starts at 10:30 AM. **Submissions are due at 5:00 PM.** Judging runs from 5:00 to 6:45 PM, the final round from 7:00 to 8:00 PM, and winners are announced at 8:15 PM.

**The two challenge tracks** (every project picks one):

- **5 Sigma:** pick a real task that AI struggles with and build a system that does it *reliably*. Prove it by testing on real inputs you didn't prepare, and compare against a simple baseline: what you'd get by asking the AI once, with no system around it. Show where it still fails, and what you changed after seeing those failures.
- **Element 119:** build something that only works because the AI can *see, hear and generate media*: video, audio, images or documents as the core input. Push it hard and show where it breaks.

Our app fits both: photos and videos are the core input (Element 119), and we're testing it carefully against a baseline (5 Sigma).

**Rules that matter for us:**

- We must use **at least two Gemini 4 models**, each with a clear job.
- The project must go **beyond a text box**: here, the camera is central.
- **Not allowed:** text-only chatbots, demos that only work on scripted inputs, or tests made entirely of examples the team wrote to pass.
- The code repository must be **public**.
- Teams have 1 to 4 people.
- The demo may only show features **built during the hackathon**.

**What we submit:** the public repo, a **one-minute demo video** of what we built, and all team members added.

**How judging works:** in round 1, each team has 3 minutes of live demo and 2 minutes of questions. The six best teams go on stage for round 2.

| What judges score | Weight | What they're looking for |
|---|---|---|
| Live demo | 35% | It works live, on real inputs nobody rehearsed. No slides or mock-ups. |
| Proof it works | 25% | Evidence beyond the demo: a test against a baseline, and an honest look at where it fails. |
| Creativity | 20% | It takes on a problem others avoid, and the camera matters to it. |
| Use of Gemini | 20% | It uses at least two Gemini 4 models, each with a clear job, plus Google's new "Decisions API", and pushes what they can do. |

**Prizes:** 1st $7,500, 2nd $5,000, 3rd $2,500. Also Best use of Managed Agents ($5,000) and Best use of Shopify ($2,500 in Shop Cash).

---

## 2. The problem

Landlords have a lot of power over tenants. Tenants often:

- **don't know their rights**, or which rules their landlord is breaking;
- **don't know what help exists**: which city agency to call, what forms to file, which free legal services are available;
- **can't prove the problem**: a complaint like "my bathroom has mould" carries little weight without evidence tied to a specific rule;
- **find the system hard to navigate**: 311, the city's housing agency (HPD), the state housing agency (DHCR), Housing Court, each with its own process, forms and deadlines;
- **worry about retaliation** if they complain.

**Our problem statement:** NYC tenants have problems they can't prove or escalate. The app turns what they record into evidence tied to the specific law, and the next step to take.

---

## 3. Who it's for

**NYC renters and tenants**, whatever kind of building they live in.

> The tenants below are made up, to make the users concrete. They are not real people or research findings.

- **Maria, in a rent-stabilized apartment in the Bronx.** Water has been coming through their kitchen ceiling for weeks, and the stain is growing. They've texted the super twice. They want it fixed, and want to know whether they can pay less rent until it is.
- **Devon, a NYCHA (public housing) resident in Brooklyn.** Mould keeps coming back in their bathroom and their child has asthma. Different rules and complaint channels apply in public housing, and they don't know which.
- **Sam, a parent in an older walk-up in Queens.** Paint is peeling near the window in the room of their 3-year-old. The building is from the 1920s, so the paint may contain lead. They don't know whether the landlord has to act, or how fast.
- **Priya, about to sign a lease in Manhattan.** They want to know what to look for on the tour, and what the landlord has to tell them before signing.

What they have in common: they have a phone camera, and they're not lawyers.

---

## 4. How the app works, in four steps

Every feature follows the same four steps.

1. **Capture.** The tenant takes a photo or video, and can talk while filming to describe the problem, in any language.
2. **Observe.** The app describes what's actually in the photo or video: what the problem is, where it appears (for a video, the moment it appears), and how bad it looks. If there's no problem, it says so honestly.
3. **Match to the law.** Each problem is matched to the specific rule it breaks. Our knowledge base is NYC and New York State housing law. The app only cites rules it actually looked up, so it can't make up laws.
4. **Act.** The app explains the tenant's rights and responsibilities and how to escalate. Then it drafts what they need: a letter or email to the landlord, the text of a 311 complaint, a complaint to the state housing agency, or an evidence packet for Housing Court.

---

## 5. A walk-through example

**Maria photographs the mould in their bathroom ceiling.**

1. **What the app sees:** "Mould on the bathroom ceiling, roughly 15 square feet, next to a water stain that suggests a leak above."
2. **The law:**
   - NYC's Housing Maintenance Code makes visible mould in an apartment a violation the landlord must fix, and the size sets the class:

     | Mould area | Class | Landlord must fix within |
     |---|---|---|
     | Under 10 square feet | A, non-hazardous | 90 days |
     | 10 to 30 square feet | B, hazardous | 30 days |
     | 30 square feet or more | C, immediately hazardous | 21 days |

   - At about 15 square feet, this is likely **Class B, 30 days to fix**.
   - The landlord must also fix the *cause* (the leak), not just paint over it.
3. **Maria's rights:**
   - New York law protects tenants from retaliation for complaining.
   - If the landlord tries to evict or raise the rent within a year of a good-faith complaint, the law presumes it's retaliation.
   - Tenants may also be entitled to a rent reduction for conditions like this.
4. **Next steps the app suggests:**
   1. Send the landlord a written notice (the app drafts it, with the photo and the rule).
   2. If it isn't fixed, file a 311 complaint so HPD, the city's housing agency, inspects. The app writes the complaint text in the city's own categories.
   3. If it's still not fixed, start an "HP action" in Housing Court to get a judge to order the repair. The app lists the forms and assembles the evidence.
5. **The output:** a dated, cited record (photo, problem, rule, class, deadline) plus the drafted letter and complaint, ready for Maria to review and send.

The app drafts. **Maria decides what gets sent.** And it explains the law; it is not a lawyer.

---

## 6. Must-have features

These six have to work for the demo.

1. **Upload a video or photo,** with optional spoken narration.
2. **Identify the problems in it:** what each problem is, where it appears (the moment in a video, or the area of a photo), and an honest "nothing found" when there's nothing wrong.
3. **Cite the law each problem breaks,** with its severity class and the landlord's deadline to fix it.
4. **Explain the tenant's rights,** the landlord's duties, the tenant's own responsibilities, and how to escalate.
5. **End with a concrete next step:** a referral to the right agency, or a drafted letter or complaint.
6. **A test that scores the app against a simple baseline** (the same AI asked once, with no system around it), on a set of real photos and videos.

---

## 7. The full feature list

**Must-haves:** see section 6.

**Nice-to-haves, in priority order.** We work down this list if there's time.

| # | Feature | What it does for the tenant |
|---|---|---|
| 1 | Building and landlord history | Looks up the tenant's building in public city records: past violations, complaints, who the owner is, whether it's rent-stabilized. It shows patterns, such as "this landlord has 40 open violations". |
| 2 | Multilingual narration | The tenant can describe the problem in any language while filming. |
| 3 | Anti-retaliation notice | Explains clearly that the law protects them for complaining, and what to do if the landlord retaliates. |
| 4 | Heat and hot water | Reads the thermometer in a photo, checks it against the legal minimum for that time of day, and uses the outdoor temperature at that hour. |
| 5 | Neglect over time | Compares photos of the same spot on different dates, to show a problem is getting worse or was never fixed. |
| 6 | Pre-lease tour | Before signing a lease, flags problems during a viewing and suggests questions to ask the landlord. |
| 7 | Move-in and move-out record | Records the apartment's condition at move-in and at move-out, to protect the security deposit. |
| 8 | Daily check (AI agent) | An automated agent checks city records every day for the tenant's complaint, and when the landlord claims a repair is done, asks the tenant to re-film to confirm. This targets the "Best use of Managed Agents" prize. |
| 9 | Court paper decoder | Reads court papers the tenant received and explains in plain language what they mean and the deadlines. |
| 10 | Good Cause Eviction check | Works out whether the tenant is covered by New York's 2024 Good Cause Eviction law, which limits evictions and rent increases. |
| 11 | Harassment timeline | Builds a dated record of harassment from photos, audio and notes, mapped to the legal definition of harassment. |
| 12 | Lease check | Reads a lease and flags clauses that are illegal in New York. |
| 13 | Shopify tie-in | For problems that are the tenant's own job to fix (for example cleaning surface mould off tile or caulk), suggests products to buy. This targets the Shopify prize. |
| 14 | ADA access, rent overcharge, neighbour organizing | Each would be a separate build; listed for later. |

---

## 8. Which problems it handles best

The app is strongest where the problem is **visible**, where **what you see decides the legal outcome**, and where tenants **actually complain**. We ranked the city's housing complaints (about 2.5 million problems reported from 2024 to 2026):

| Kind of complaint | Share of complaints | How well a camera handles it |
|---|---|---|
| Heat and hot water | 34% | **Harder.** A camera can read a thermometer, but proving a violation also needs the time of day and the outdoor temperature. Useful, but not mainly visual. |
| Unsanitary conditions (likely including mould and pests) | 17% | **Strong.** Mould is the best fit of all, because its class depends on visible size. |
| Plumbing | 10% | Partly: visible leaks and broken fixtures. |
| Paint and plaster | 9% | **Strong.** Peeling paint and holes; also a lead risk in older buildings with young children. |
| Doors and windows | 7% | **Strong.** Broken windows, missing window guards, broken locks. |
| Water leaks | 6% | **Strong.** Stains and active leaks. |
| Electrical, appliances, floors | 11% | Partly: exposed wiring, damaged floors. |
| Safety | 3% | **Strong.** Missing or broken smoke and carbon monoxide detectors. |

**Our focus:** mould, leaks and water damage, peeling paint and plaster, pests, windows and window guards, and smoke detectors. Heat is a supporting feature.

---

## 9. How we'll prove it works

Judges give 25% of the score to **proof it works**, so we test properly.

- **The test set:** 203 real photos and videos of apartment problems (and of rooms with no problem), from public, openly licensed sources.
  - Eric checked every label by hand and then **locked the answers** before anyone started building, so the test can't be tuned to make the app look good.
  - After review: 197 items are scored, 5 were dropped (for example, photos with watermarks), and 1 is still to be decided.
- **What the test covers:**
  - photos of 8 problem types (about 10 each, and 30 for mould)
  - 92 "clean" photos, either no problem or something that just *looks* like one (a shadow, dirt, an old repaired stain)
  - 24 videos
- **What we compare:**
  - the full app, against a **baseline**: the same AI asked once, "what's wrong and which rule does it break?", with no system around it;
  - whether it finds the right problem, and avoids false alarms on clean photos;
  - whether it cites the right rule, class and deadline;
  - for mould, **how often it agrees with a human about the size class** (A, B or C), and whether it admits "I can't tell" when the photo shows nothing for scale, instead of guessing.
- **Being honest about failures:** judges explicitly ask where it still fails. We'll show the misses, and what we changed after seeing them.

**One limitation to state plainly:** most test photos are not NYC apartments. They're renovations, older or abandoned buildings, and stock photos, because that's what's publicly available with permission to use. For the **demo**, we want real NYC apartment footage, ideally filmed live.

---

## 10. What's already done

Prepared before building started:

- **The law:** the full NYC Housing Maintenance Code, the city housing agency's rules, the related NYC laws (rent stabilization, illegal lockouts, the right to a lawyer in Housing Court, the FARE Act on broker fees, discrimination), New York State tenant law, and the relevant federal rules. About 1,700 sections in total, each saved with its source.
- **The process:** how complaints, inspections and Housing Court cases work; official court and state housing forms; and agency contacts.
- **City records:** the full list of HPD violation types (612 combinations of violation and class, drawn from about 11.4 million real violations), complaint categories, 311 complaint types, and five example NYC buildings for the demo.
- **The problem map:** a draft linking each problem type to its rules, classes, deadlines and escalation steps. It still needs review.
- **The test set:** about 1,300 photos and videos collected, of which 203 were reviewed and locked (see section 9).

All of it is in the team's GitHub repo.

---

## 11. Open questions

- **The demo input:** what do we film live for the 3-minute demo, and where? A real NYC apartment is ideal.
- **What judges see at the end:** the final screen of the demo (the cited record plus the drafted letter?).
- **The one-minute demo video:** what's in it, who records it, and who edits it.
- **Who does what:** see the next section.
- **Rules check:** confirm in the event Discord's `#rules` channel what preparation before the event is allowed, and say openly in the submission what was prepared before the event and what was built today.
- **Some legal details are still unsettled** in the draft problem map. One example: the exact class for some repair violations. The app should say so rather than guess.

---

## 12. How you can help (suggestions)

None of these need coding:

- **Demo footage:** film real NYC apartment problems (with the owner's or tenant's permission). For example: a water stain, mould, peeling paint, a missing smoke detector, a window without a guard. Short clips of 10 to 30 seconds, on a phone, in normal light.
- **Check the drafted letters and complaints:** do they read like something a tenant would actually send? Are they clear, polite, firm and correct?
- **The pitch and the 3-minute demo script:** tell Maria's story (section 5) in 3 minutes, and rehearse it.
- **The one-minute demo video:** plan it, record it and edit it. It's required for submission.
- **The "where it fails" story:** once test results come in, help turn them into a short, honest explanation for judges.
- **Notion organization:** turn this brief into the team's working space: tasks, owners, timeline to 5:00 PM.
- **Live testing:** try the app with your own photos and note where it gets confused.

---

## 13. Glossary

| Term | Meaning |
|---|---|
| **HPD** | NYC Department of Housing Preservation and Development: the city agency that inspects apartments and issues violations to landlords. |
| **311** | NYC's non-emergency line and app. Housing complaints filed through 311 go to HPD. |
| **Violation** | An official finding by HPD that the landlord broke the housing code. |
| **Class A / B / C** | HPD's severity levels: A non-hazardous, B hazardous, C immediately hazardous. The class sets how long the landlord has to fix it. |
| **Housing Maintenance Code** | NYC's main law on landlords' duties: repairs, heat, hot water, pests, mould, lead paint, window guards, smoke detectors. |
| **HP action** | A case a tenant starts in Housing Court to make the landlord do repairs. |
| **Housing Court** | The part of NYC Civil Court that handles landlord-tenant cases. |
| **DHCR** | NY State Division of Housing and Community Renewal: oversees rent-stabilized apartments and handles complaints such as rent overcharges and reduced services. |
| **Rent-stabilized** | Apartments, usually in older buildings with 6 or more units, where rent increases are capped and tenants have a right to renew their lease. |
| **NYCHA** | New York City Housing Authority: the city's public housing. Different complaint channels apply there. |
| **Retaliation** | A landlord punishing a tenant (eviction, rent increase, harassment) for complaining. Illegal under New York law. |
| **Good Cause Eviction** | A 2024 New York law that limits evictions and large rent increases for many tenants not covered by rent stabilization. |
| **Baseline** | The simple comparison we test against: the AI asked once, with no system around it. |
| **Test set** | The locked collection of real photos and videos, with checked answers, used to score the app. |
| **Gemini 4** | Google's AI models used in this hackathon. We must use at least two, each with a clear job. |
| **Decisions API** | A new Google tool that answers yes/no or multiple-choice questions about an image or video, with a confidence score. |

---

*Sources: the team's planning notes (`docs/plan.md`), the hackathon requirements (`docs/REQUIREMENTS.md`), and the data collected for the project (`data/SUMMARY.md`). The app explains the law; it does not give legal advice.*
