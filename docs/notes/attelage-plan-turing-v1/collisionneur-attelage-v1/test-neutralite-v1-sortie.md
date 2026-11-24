# Neutrality review

## 1. Orientation: **0.70** (pass)

Most of the questions are open and invite refutation ("show, or to refute"; Q8 on infeasibility). A few phrases still steer. "Steering" tells the panel that the harness also drives the search. "Honest baselines" is evaluative and suggests the listed set is the right one. Q4 assumes that rare, high-consequence ideas cluster in identifiable regions.

- *Phrases at fault:* "a harness for measurement and steering"; "honest baselines"; "where such ideas are more likely"

## 2. Disclosure: **0.70** (pass)

"Narrow and deep" is in-house jargon, but the text defines it on first use, which limits the harm. Listing exactly three baselines, including the specific choice "mechanical enumerator", reveals the askers' existing design. "Steering" leaks a planned use.

- *Phrases at fault:* "narrow and deep"; "a mechanical enumerator"; "measurement and steering"

## 3. Completeness: **0.90** (pass)

Every required element is present:
- target definition without circular judges (Q1)
- sources of truth (Q2)
- problem choice (Q4)
- feedback (Q5)
- cheap-to-expensive plan with stopping criteria (Q7)
- limits, infeasibility and ill-posedness (Q8)
- confidence, established vs conjecture, and verifiable references (closing paragraph)

Minor gaps: the comparison question only asks what would *support* a superiority claim, and nothing covers the case where no judge-free measure of depth exists.

- *Phrases at fault:* "would support the claim"

## 4. Exclusion of a rival: **0.65** (pass)

Three rivals are made harder to propose:
- The fixed baseline list discourages other baselines, such as single-agent self-critique loops at equal compute, evolutionary or program search, or human researchers.
- Q1 rules out judges entirely rather than asking how to control their bias, which discourages the rival answer that some judge (human or cross-family) is unavoidable.
- Q4 presupposes that such regions exist.

- *Phrases at fault:* "The comparison is against honest baselines:"; "without a language-model judge whose preferences may overlap with the generator's?"; "where such ideas are more likely"

## Word-for-word edits

1. **replace:** `build and validate a harness for measurement and steering.`
   **with:** `build and validate a measurement harness.`
   *Reason:* removes the presupposition that the harness steers the search; Q5 already covers feedback.

2. **replace:** `The comparison is against honest baselines: random sampling`
   **with:** `Candidate baselines include random sampling`
   *Reason:* drops the evaluative "honest" and stops presenting the set as fixed.

3. **replace:** `the strongest single model given the same budget.`
   **with:** `the strongest single model given the same budget; others may be proposed.`
   *Reason:* lets the panel propose rival baselines.

4. **replace:** `whose preferences may overlap with the generator's?`
   **with:** `whose preferences may overlap with the generator's? If some judge is unavoidable, how should its bias be bounded?`
   *Reason:* keeps the anti-circularity requirement without excluding the answer that a judge is needed.

5. **replace:** `would support the claim "better than the baselines"?`
   **with:** `would support or refute the claim "better than the baselines"?`
   *Reason:* makes the decision rule symmetric.

6. **replace:** `where such ideas are more likely,`
   **with:** `where such ideas might be more likely, if such regions exist,`
   *Reason:* removes the assumption that such ideas cluster.

The original is about 385 words. After these edits it is about 405, within the 250–450 limit.
