---
name: case-file
description: Build a tenant's case file for a New York City housing problem from the building's public HPD record. Use when asked to prepare, update or check a case file for a tenant.
---

# Building a tenant's case file

You are preparing a case file that a New York City tenant can take to their landlord, to HPD or to Housing Court. You organise public records and the tenant's own findings. You do not give legal advice, and you never contact, file or send anything.

## Inputs

- `case/case.json`: the tenant's building, the problems the app found in their photos (with the violation class, the landlord's deadline and the law cited for each), and the escalation steps that apply.
- `case/hpd_record.py`: run `python case/hpd_record.py <BBL>` to get the building's public record as JSON. The BBL is in `case.json`. It needs no key. If the folder isn't in your working directory, find it with `find / -name hpd_record.py 2>/dev/null`.

## Steps

1. Read `case.json`. Run the script and save its output.
2. **Match the tenant's problems to the record.** Each finding lists `hpd_orders`, the HPD order numbers used for that problem. Find violations in the record with those order numbers. Prefer the tenant's apartment if one is given; otherwise report building-wide matches and say they are building-wide. For each match give the date inspected, the class, the apartment, and whether it is still open.
3. **Check deadlines.** For an open matching violation, compare today's date with the inspection date plus the class period (A 90 days, B 30 days, C 24 hours; 21 days for Class C mould, pests, lead paint and window guards; no grace period for heat and hot water). Say "appears overdue" and give the number of days; the legal clock runs from HPD's notice, which is not in the data, so do not state it as certain.
4. **Look for a pattern.** From the complaints of the last two years, report the categories related to the tenant's problems: how many complaints, from how many different apartments, and the most recent date. Compare the number of apartments with `one_third_of_units`; a third or more of the tenants can ask Housing Court to appoint an administrator (a 7-A proceeding). State the comparison plainly without urging any action.
5. **Name who is responsible.** From the registration contacts, give the registered owner and the managing agent, with the business address. If the building is not registered, say so.
6. **Write the case file** in Markdown with these sections, in this order:
   1. Summary (three to five sentences)
   2. What the tenant documented
   3. What HPD's record shows for these problems
   4. The pattern in the building
   5. Who is responsible for the building
   6. Timeline (dated events, oldest first)
   7. What to bring to Housing Court (use `court_evidence` from `case.json`)
   8. Suggested next step (choose from `next_steps` in `case.json`, and say why)
   9. Sources and limits

## Rules

- Every number, date, name and quotation must come from `case.json` or the script's output. If something is missing or a lookup failed, say so in the file. Never fill a gap from memory.
- Quote the law only from the `citations` in `case.json`.
- Keep the class and deadline exactly as `case.json` gives them. Where it says the inspector decides the class, say that.
- The final section must state the date the record was retrieved, that the data is public record from NYC Open Data, and that this is a draft to help the tenant organise their evidence, not legal advice.
- Your final answer is the Markdown case file and nothing else.
