# Scoring rules (DRAFT until the review set is frozen)

Written before any system or baseline result exists. Freezing the review (the Freeze button) fixes these rules along with the labels.

1. **Scored items:** only reviewed items in `review_set.json`, excluding drops. Unreviewed test items are a reserve and are never part of a reported number. The copyrighted fallback is scored separately and never in the headline.
2. **The answer key** is the owner's decision in `decisions.json`: the draft label if marked right, otherwise the fixed label.
3. **Detection, per item:** the set of core problem types the system reports, compared with the key. Report precision and recall for each type, plus exact match per item. A look-alike's correct answer is "none". So are no-problem items. Any problem reported on them is a false alarm.
4. **False-alarm rate:** the share of no-problem and look-alike items where the system reports any problem. Report it separately for each group.
5. **Per-type results are counts** ("9 of 10"), not percentages. Only the overall figures get percentages.
6. **Mould size, scored against the owner's bin:**
   - **The metric is "agreement with the reviewer", not accuracy.** Publish the full table of the system's bin against the reviewer's bin, and report both exact agreement and agreement within one bin.
   - **A photo supports a lower bound.** If the system answers "at least B", that counts as correct when the reviewer marked B, and as wrong when the reviewer marked A.
   - **"Surface mould on intact tile, grout or caulk" is its own answer:** the tenant's cleaning duty under HMC § 27-2012(a). It is not an owner mould violation (§ 27-2017.3(a) excludes tile and grout).
     - It becomes the owner's problem only if the caulk or tile is damaged (repair, HPD order 502) or the mould comes from behind or keeps coming back (mould hazard, order 550, sized A/B/C).
     - Note: HPD inspectors have also issued about 1,900 Class A "cleanse tiles, caulking and grout" orders (553) since 2019. So an answer of "surface mould, cleaning, possibly an HPD 553 Class A order" also counts as correct. An answer of "owner mould hazard violation 550" counts as wrong for this bin.
   - **Abstention is scored both ways:** how often the system abstains (says it can't tell, or asks for a reference object) when the reviewer marked "can't tell", and how often it abstains when the reviewer did judge a bin.
7. **Contractor-area check (fallback, side result only):** use only jobs whose stated area is under 10 or under 30 sq ft. Count per job, not per photo, and report the number of such jobs.
8. **Video:** detection is scored as in rules 3 and 4. A timestamp is correct if it falls inside the reviewer's range, widened by 3 seconds on each side. Video is reported separately from photos.
9. **Law step:** for each correctly detected problem, the cited section must be among the problem map's sections for that type, and the class and deadline must match `problem-map/expected-outcomes.csv` for the facts given. Rows marked unsettled aren't scored.
10. **Fairness:** the baseline (one model call) and the system see the same items at the same resolution, with the same input text. Report every run, including failed ones.
