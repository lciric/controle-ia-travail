# Correction log for the ideation organism public page under N-067 (v1)

- Written on 13 November 2026, 19:38 to 19:45 UTC (`date -u`), by a fresh writer who wrote no part of the organism.
- Decision applied: `docs/decisions/decision-N-067-v1.md` of the working repository, sha256 `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589` (checked). Points 2, 5b and 5c of section 0; R-2571 and R-2573.
- **Base commit**: `origin/main` = `be6b5af96c9e19812569d8dab55d6ce3978a3823` of `lciric/ideation-organism`, fetched on 13 Nov 2026 at 19:35 UTC. Local `main` (`6510199`) is 8 commits behind and was left untouched, as instructed by the coordinator. Files were read with `git show origin/main:<path>` and copied to `actuel-be6b5af/`. Nothing was merged, committed or pushed in the clone.

## Files read and hashes at the base commit

| file | sha256 at `be6b5af` | changed? |
|---|---|---|
| `README.md` | `e81b96383bc3a387e45f3f7e89f1590f175a968fb24e77a3a66f471a45e051e3` | yes |
| `MANIFEST.md` | `052d7c594f02c6dcc34977805755377e41568ed29e22369a81b362b279919717` | yes (one dated section added) |
| `CITATION.cff` | `4b5d5bbb23d06eebf4a1bcb278cc9680c0c5d80700725f2328a36d6be4aeaa2b` | no: it makes no claim |
| `resultats/boucle-reelle-v66/README.md` | `70a7db26b80e897cb00888254b5d79b842429bcbb4f5eebc84a115ef62f601f2` | no: no sentence of novelty or priority, and no ceded element described as its own |
| `resultats/course-v67/README.md` | `055597d670d8cef7c76f938f4e7cfac33616002edbe9cd81ad503cc0265be02a` | no: same |

I also searched the linked results pages `resultats/attaque-goodhart-v2/README.md`, `controle-r1-blanche-noire/README.md`, `controle-p3-premier-test/README.md` and `controle-simulation-defenses/README.md` for "first", "novel", "new", "claim", "prior art", "not found", POPPER and Dwork. None of them claims priority. "First" is chronological wherever it appears. "Public claim" on the Goodhart page means the decision to adopt the v9 null, and that page says it waits for the project lead. The simulation page already disclaims novelty (line 83). None of these pages was changed.

## Outputs

| file | sha256 |
|---|---|
| `README.md` | `bd4f8128cf0f91a2bc59ee48e860bf626c42750d93edd9a45b886259c1211edd` |
| `MANIFEST.md` | `8dfaa697b4853993bf37554c8186c088f08b6be6f16692d8f3bc6ccac4e8afbd` |
| `diff-page-organisme-n067-v1.patch` (`diff -u` against `actuel-be6b5af/`, paths `a/`, `b/`; checked: `patch -p1` on the base copies reproduces both outputs byte for byte) | `d70d83bcec78c679f2837f2561fde94cdc12b98cfc606b627e126c95046f3c9d` |
| this log | in its companion `journal-page-organisme-n067-v1.md.sha256` |

## Sentences changed (README.md)

Six sentences were changed or removed. New sentences were added only inside the Related work paragraph.

**1. Line 3 ("What it is").**
- Before: "…propose research hypotheses on AI control, and in which *none of the agents that produce an idea is allowed to decide whether it survives*."
- After: "…propose research hypotheses on AI control, and in which, following a principle already published (see Related work below), *none of the agents that produce an idea is allowed to decide whether it survives*."
- Reason: the sentence presented the separation of proposer and judge (O1) as the system's defining trait. That separation is ceded.
- N-067: section 4, point 5 ("O1 : plus revendiquée… principe d'architecture que l'organisme adopte et cite ; Qu, Chen, Wang en revendiquent la priorité") ; section 0, point 2 (a).

**2. Line 7, Related work, sentence 1.**
- Before: "Closest to the judge is POPPER (…), where an e-value rule with a 1/α threshold, written outside the agents, already decides on free-form hypotheses produced by language models: using e-values and such a threshold is therefore not claimed here."
- After: this sentence is kept in substance inside the *statistic computed outside the agents* clause, with the same reference. Qu, Chen, Wang, Sargsyan, CONFIRM, CADS, Wang et al. and Zhang are added.
- Reason: component (a) of O2 is ceded beyond POPPER.
- N-067: section 3, row "O2 (a)"; section 4, point 1.

**3. Line 7, Related work, sentence 2.**
- Before: "What is claimed is narrower: the statistic is computed by the orchestrator, outside every agent, from a commitment sealed before the data exist, against a null formed by the known laws (the archive), with multiple comparisons controlled."
- After: the sentence is removed. Each component is now attributed to published work: (a) the statistic outside the agents; (b) the plan sealed by hash; (d) multiple comparisons. The null is described in a separate clause with no word of priority: "*The judge's null*: the statistic is computed against a null formed by the known laws (the archive), so that a card is promoted only if its sealed prediction beats what the archive already predicts ("nothing beyond the archive")."
- Reason: (a), (b) and (d) are no longer claimed. O4 and the retained wording of O2 may not be declared free outside the repository before the reading of SSRN 6569258 and the high-priority leads.
- N-067: section 4, points 1 and 2 (usage clause); section 0, point 4 (a); section 10.

**4. Line 7, Related work, sentence 3.**
- Before: "The principle of the cheaters bench (section 3.1) and of the Goodhart attack (section 4) — … — has been prior art since 2015 (Dwork et al. …; Blum and Hardt …); only their form is claimed: a language-model proposer that reads the exact description of a statistical judge and, in one arm, its verdicts, on worlds where every promotion is false."
- After, in two clauses:
  - Cheaters bench, preregistered validation and mutation bench: they are "instruments of this system, and their sizes and numbers are reported as its measurements, not as ideas". The 2015 prior art (Dwork et al.; Blum and Hardt, unchanged references) is kept. Qu, Chen, Wang, Masked Erosion, PACE, Sargsyan and CADS are added.
  - Goodhart attack: what CONFIRM, Qu, Chen, Wang, REUSE, PACE, Sargsyan, arXiv:2611.00643 and Hegazy, Jordan, Dieuleveut already do, then: "What section 4 measures is only this narrower form: on worlds where every promotion is false, a language-model proposer instructed to get a false card promoted by the statistical judge, given the judge's exact description as text and free in its proposals, with one arm that receives the judge's verdicts and one that does not, compared."
- Reason: O11 is no longer claimed as an idea. That includes the mutation bench of the judge's own code. The O12 form "verdicts served, negative worlds, zero promotion" is published by CONFIRM, so O12 is described only in its narrowed form.
- N-067: section 4, points 3 and 4; section 0, points 1 (a) and 3 (a).

**5. Line 7, Related work, sentence 4.**
- Before: "That form was not found in the work read so far; the papers that cite POPPER remain to be read."
- After: the sentence is removed.
- Reason: the old form is partly occupied (CONFIRM, p. 9, 22), so this sentence is false for it. The papers that cite POPPER have now been read (levels 2 and 3). For the narrowed form, I wrote no "not found" sentence on the public page; see "Remaining doubts" below.
- N-067: section 3, row "O12 forme"; section 4, point 3; section 7, point O12.

**6. Line 47 (section 1).**
- Before: "The design rule of this system is therefore mechanical, not moral: **the role that produces an artefact never holds the key that evaluates it.**"
- After: "The design rule this system adopts, a published principle and not a contribution of this repository (see Related work above), is therefore mechanical, not moral: **the role that produces an artefact never holds the key that evaluates it.**"
- Reason: same as change 1 (O1).
- N-067: section 4, point 5.

Unchanged on purpose:
- The sentence on Co-Scientist (sentence 5 of the old paragraph), word for word.
- Step 7 of section 2, "fresh draws seeded by the hash of the commitment". This is the remainder of O3, described as an implementation choice (N-067, section 4, point 6), and the Related work paragraph now says so.
- The guard table of section 3 ("No silent fallback anywhere", the vault, the sealing). Each line describes what the system does and claims no priority (N-067, section 4, point 7: "décrits, non revendiqués"). The Related work paragraph says the principles are published.

## Citations added (all from N-067, section 6 and section 3; pages as N-067 gives them)

| piece | reference as written on the page | pages cited on the page | N-067 row |
|---|---|---|---|
| Qu, Chen, Wang | "Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors", arXiv:2609.27051, 2026 | separation pp. 1, 2, 4, 11, priority claimed pp. 2, 4; statistic outside the agents pp. 1, 10, 11; sealing order in principle pp. 2, 10; multiplicity pp. 2, 4, 8; scripted cheaters pp. 16, 29; preregistered validation pp. 8, 10, 14, 29, 36; faulty judges p. 13; threat named pp. 6, 18, 25; diagnostics returned without an instruction to deceive p. 12 | section 3, rows O1, O2 (a), (b), (d), O3, O11, O12; section 6 |
| PROCTOR (Wahi) | "LLM-as-a-Judge Is Not an Oracle", arXiv:2609.02246, 2026 | p. 4; pp. 1, 7 | section 3, rows O1, O17; section 6 (added to the mandatory list) |
| POPPER | unchanged from the page | — | N-064 citations, carried over by N-067, section 6 |
| Sargsyan | "Structural Enforcement of Statistical Rigor in AI-Driven Discovery: A Functional Architecture", arXiv:2511.06701, 2026 | pp. 8, 9, 11; pp. 1, 15–16, 23, 25; pp. 27–29; pp. 27–28 | section 3, rows O2 (a), (d), O11, O12; section 6 |
| CONFIRM (Wei et al.) | "CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging", arXiv:2611.01449, 2026 | p. 3; pp. 5–6, 14; pp. 6, 9, 22 | section 3, rows O2 (a), (b), (d), O3, O12 form; section 6 |
| CADS (Chen et al.) | "CADS: Measuring the Incremental Contribution of LLM Proposers in Sequential Biological Screens", arXiv:2610.24597, 2026 | p. 5; pp. 4–6; pp. 9, 23 | section 3, rows O2 (a), (d), O11; section 6 |
| Wang et al. | "N×N E-valuation", arXiv:2608.06621, 2026 | pp. 1, 3; pp. 25–26 | section 3, rows O2 (a), (d); section 6 |
| Zhang | "Hard to Fool: A Bounded LLM Research Loop for Quantitative Finance, and What Two Dozen Campaigns Found", arXiv:2611.06607, 2026 | pp. 1, 3–4 | section 3, rows O2 (a), (b), O17; section 6 |
| Masked Erosion (So, Liu, Long) | "Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents", arXiv:2610.38392, 2026 | pp. 4, 24; pp. 2, 8 | section 3, rows O3, O11, O17; section 6 |
| Hegazy, Jordan, Dieuleveut | "Valid Stopping in Adaptive Generator–Verifier Loops", arXiv:2610.06432, 2026 | pp. 2–3; pp. 1–2 | section 3, rows O2 (d), O12; section 6 (added to the mandatory list) |
| PACE (Shawn) | "PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents", arXiv:2606.08106, 2026 | p. 6; pp. 6–7 | section 3, rows O11, O12; section 6 |
| REUSE (Sun, Zeng, She, Wang) | arXiv:2609.33180, 2026 (N-067 gives no title) | p. 32 | section 3, row O12; section 6 |
| Dwork et al.; Blum and Hardt | unchanged from the page | — | N-064 citations, carried over by N-067, section 6 |
| arXiv:2611.00643 | identifier only (N-067 gives no title or authors) | pp. 1, 2, 10 | section 0, point 5b (a); section 9; R-2571 |
| Co-Scientist | unchanged from the page | — | N-064 citations, carried over by N-067, section 6 |

## MANIFEST.md

The base manifest records later README updates in a dated section. I followed that practice and added one: "Updated on 13 November 2026 (related work and claims narrowed)". It says what changed, and that no number, result or file changes. Nothing else in the manifest was touched.

## Remaining doubts

1. **O12 on the public page.** N-067 (section 4, point 3; R-2571, point 1 (a)) keeps the narrowed form as a claim. Point 2 of N-067's sentence for outside readers pairs it with O4 under the usage clause. I therefore described the narrowed form without saying "not found". The mother session can add "not found in the pieces read (CONFIRM, Qu, Chen, Wang, Sargsyan …); this holds for those pieces, not for the field" if it reads the clause as covering O4 only.
2. **"robust".** The page keeps "frontier crossed, robust" in the status paragraph and the Goodhart row. It is the frozen outcome label of the sealed A1-v4 verdict, quoted, not a word of this correction. I left it, but it reads stronger than a plain reading.
3. **Missing reference details.** N-067 gives no title for REUSE (2609.33180) or 2611.00643, and gives the N×N title only as « N×N E-valuation ». I invented nothing; the identifiers are as given.
4. **First-person "claimed" wording.** Phrases like "none of them is claimed here" and "not as ideas" disclaim ideas only; they do not affirm anything as free. The judge's null (O4) is described as what the system does, with no priority word, under the usage clause of N-067 (section 4, point 2).
5. **The base moved during the session.** Local `main` lagged `origin/main` by 8 commits. The diff is against `be6b5af`. If `origin/main` moves again before the push, the patch must be checked against it.
