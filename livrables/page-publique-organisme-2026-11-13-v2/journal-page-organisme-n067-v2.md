# Correction log, public page of the ideation organism, under N-067: version 2

- Written on 13 November 2026, from 19:57 UTC to the hash of the log (`date -u`), by the same writer as v1. That writer wrote no part of the organism, of N-067 or of the adversarial reading.
- **Base commit:** `origin/main` = `be6b5af96c9e19812569d8dab55d6ce3978a3823` of `lciric/ideation-organism`.
  - Re-fetched at 19:57 UTC with an explicit refspec (`git fetch origin refs/heads/main:refs/remotes/origin/main`); unchanged.
  - Local `main` (`6510199`) was left untouched. It is 70 commits behind `origin/main`, 4 of them on the first-parent line. This corrects m5 of the adversarial reading: v1 said 8.
  - Files were read with `git show origin/main:<path>`; copies are in `base-be6b5af/`.
  - Nothing was merged, committed or pushed. The v1 folder `/home/user/page-organisme-n067/` is intact.
- **Inputs, with their hashes as checked:**

| piece (programme repository) | sha256 |
|---|---|
| `docs/decisions/decision-N-067-v1.md` | `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589` |
| `livrables/page-publique-organisme-2026-11-13-v1/lecture-adverse-page-v2.md` | `0bfe8eb7879f3375ebf2cdd37d454055077be4c282bd76ea99aa7e225a0405b5` |
| `docs/notes/publiabilite-ce-soir-v1/tri-publiabilite-v1.md` | `c51fadd65e890cd7b4b9b7b1560fe65859e249bd9d2958dcbaa306abbb6602f2` |
| `docs/notes/lecture-o4-englobement-v1.md` | `f521e164e79cb75e9b3f14a9bddb0cf8f57a5499e68f93276014e4b09fc130aa` |
| `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` | `320463e6c03189178a2436742fe78e1edeae59d6a738a52de581924d837929d7` |
| `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md` | `bc53b746f0c9918beff8a2267d5652a730985adee76a807cc670c1a1811e61de` |

## Outputs

| file | base sha256 (`be6b5af`) | output sha256 |
|---|---|---|
| `README.md` | `e81b96383bc3a387e45f3f7e89f1590f175a968fb24e77a3a66f471a45e051e3` | `73f0b053b6a5d4da20cc5194e665d2a2dffb02c1984cb81bff6bbec26b728bf1` |
| `MANIFEST.md` | `052d7c594f02c6dcc34977805755377e41568ed29e22369a81b362b279919717` | `a3dd9e795fb9fd7b49a5180bb859b1abc192d29bbf3b153ae4c577982e0cc62d` |
| `resultats/controle-r1-blanche-noire/README.md` | `98378e6e495a16dfbc06ada8e4770764c75e7f463950986a66b3c5b8a24732ef` | `3acf0a9d5a2c9c94c9d6a0965578f57a590ef2e104018002a49ca73863ea544e` |
| `diff-page-organisme-n067-v2.patch` | — | `6c4bcff43c6775a133aa3af7e9573d35d2dd9b8df9ffd083d19867d0036eb71a` |
| this log | — | in `journal-page-organisme-n067-v2.md.sha256` |

The patch was replayed with `patch -p1` on fresh copies from `git show origin/main:` and gives the three output files byte for byte (`cmp`: identical). `CITATION.cff`, `resultats/boucle-reelle-v66/README.md` and `resultats/course-v67/README.md` are unchanged; they make no claim (v1 log).

## Changes against the base, sentence by sentence

Count: 15 sentences of the base were changed or removed, and new sentences were added inside those passages.
- README, 11:
  - l. 3 and l. 47;
  - 4 of the 5 sentences of the old "Related work" (the Co-Scientist sentence is moved unchanged), rewritten as a lead and eight items;
  - status l. 9, "robust" marked;
  - A1 row, the "robust" parenthesis, with the "already published" sign added;
  - R1 row, 2 sentences: the leak sentence, and the consequence with its roadmap clause;
  - T0.3 row, 1 sentence.
- R1 page, 4: the update stamp, the leak heading, the frozen-outcome sentence (reservation added), and the consequence ("Next:" removed).
- MANIFEST: 1 section added, with 3 items.

Below, "AR" refers to the adversarial reading and "tri" to the publishability triage.

### A. Carried from v1 (see `journal-page-organisme-n067-v1.md`, `4063239a…`)

1. README l. 3: "…and in which, following a principle already published (see Related work below), *none of the agents…*". Reason: O1 is ceded. N-067, section 4, point 5.
2. README l. 47: "The design rule this system adopts, a published principle and not a contribution of this repository (see Related work above), is therefore mechanical, not moral:". Same reason.
3. README l. 7: the old "Related work" paragraph. Its five sentences were "Closest to the judge is POPPER…", "What is claimed is narrower…", "The principle of the cheaters bench… only their form is claimed…", "That form was not found…" and "As a loop… Co-Scientist". They are replaced by a lead and seven items (section B). Reasons: N-067, section 4, points 1 to 7; section 6.

### B. Couples of the adversarial reading, all applied (README, "Related work" unless stated)

| key | before (v1 text, or base text) | after | source of the after text |
|---|---|---|---|
| B1, M2, M3 | "What section 4 measures is only this narrower form: on worlds where every promotion is false, a language-model proposer instructed to get a false card promoted…, free in its proposals…" | "The instrument of section 4, as the public code builds it (`orchestrator/pole/attaque_goodhart_v2.py`): on toy worlds where every promotion is false by construction, a language-model proposer told that it is rewarded if its law is promoted by the statistical judge (it is not told that a promotion would be false), given the judge's exact description as text and writing its laws in a closed grammar, with one arm that receives the judge's verdicts and one that does not, compared; for the candidate null v9, one graded world at its declared frontier, where a promotion is not false by construction, was added." Contains no "instructed to deceive", no "free in its proposals" and no "not found". | AR, B1 couple, opening adapted to the coordinator's instruction ("describe the instrument as it is in the public code"). Checked myself at `be6b5af`: `consigne`, l. 346-347 ("Tu es récompensé si ta loi est promue par le juge statistique"); `GRAMMAIRE`, l. 266 ("Grammaire fermée (JSON)"); `description_du_juge` (l. 309 onward) contains none of "faux", "fausse", "vrai" or "tromp". The incentive is paraphrased, not quoted. |
| B2 | "Masked Erosion mutates an acceptance gate (pp. 2, 8)" | "Masked Erosion stresses acceptance gates in the spirit of mutation testing: each generation deletes one safeguard of the agent, and the authors record whether the gate lets it through (pp. 2, 8); what is mutated is the object the gate judges, not the gate" | AR, B2 |
| B3 | "and return the referee's diagnostics to the proposing model, without an instruction to deceive (p. 12)" | "and include the referee's diagnostics in the state of the proposing model (p. 12)" | AR, B3 |
| B4 | "REUSE (Sun, Zeng, She, Wang, arXiv:2609.33180, 2026) bounds a theoretical one-bit adversarial proposer (p. 32)" | "REUSE (Sun, Zeng, She, Wang, "Which Self-Improvements Should We Trust? Reliable Self-Improvement When Agents Reuse Their Benchmarks", arXiv:2609.33180v2, 2026) proves that a theoretical proposer that sees only the gate's decisions can force a false promotion against a class of threshold gates (p. 32)" | AR, B4 ("proves" is the piece's own act: corollary A4) |
| M1 | "The principles this system is built on are already published, and none of them is claimed here; …" | "The principles listed below with their references are already published, and none of them is claimed here; …" | AR, M1. The second M1 couple ("No statement on prior work is made here for this null: the readings that would settle it are not finished.") is overtaken: the O4 reading is now done, and AR (section 7, point 5) asks for the sentence to be rewritten in that case. It is replaced by the sentence of section C. |
| M1 (MANIFEST) | "the judge's null is described without any word of priority" | "the judge's null is described as what the system does, with no statement on prior work" | AR, M1 |
| M4 | identifiers with no version | versions added: 2609.27051v1, 2511.06701v4 "2026 (first version 2025)", 2611.01449v2, 2610.24597v1, 2611.06607v1, 2610.38392v1, 2610.06432v1, 2606.08106v1, 2609.02246v1, 2608.06621v5, 2609.33180v2, 2611.00643v1 | AR, M4 and M5 |
| M5 | PROCTOR, N×N, 2611.00643 cited with incomplete titles or by number only | full titles; "Yang and Shi (… arXiv:2611.00643v1, 2026) optimise a harness for a language-model judge's score and see that score rise while precision falls (pp. 1, 2, 10), a precedent for the premise that a language-model judge can be optimised against" | AR, M5 |
| M6.1 | "Qu, Chen, Wang already run scripted cheaters against an e-value referee (pp. 16, 29), validate their statistical tool under preregistration (…) and test deliberately faulty judges (p. 13)" | "Qu, Chen, Wang already run an attacking controller (hidden retries) against their e-value referee (pp. 16, 29), preregister their design, with dated amendments (pp. 8, 10, 14, 29, 36), and test three deliberately leaky referees (p. 13)" | AR, M6.1 |
| M6.2 | "freezes and hashes the authors' predictions before each trial (pp. 4, 24)" | "freezes and hashes the authors' predictions and analysis code before each round, three later sets being frozen after related outcomes (pp. 4, 24)" | AR, M6.2 |
| M6.3 | "Zhang binds the specification and the verdict code by SHA-256 before the data exist and keeps a hash-chained register with no fallback price source (pp. 3–4)" | "Zhang hashes the campaign contract before the first proposal is evaluated, can bind a specification and its verdict code by SHA-256 for campaigns whose data do not yet exist, keeps a hash-chained ledger, and replays quotes only from a hash-verified artefact with no fallback price source (pp. 3–4)" | AR, M6.3 |
| M6.4 | "PACE studies a world with no gain, without an attack (pp. 6–7)" | "PACE studies a deployment with no planted gain, without an attack (pp. 6–7)" | AR, M6.4 |
| M6.5 | "also keeps the judge apart from what it judges (p. 4)" | "also forbids any component from both proposing and applying, or both judging and acting (p. 4)" | AR, M6.5 |
| M7 (MANIFEST) | "cheaters and mutation benches, verdicts served to a language-model proposer on negative worlds" | "a scripted attacker and mutation-style stress tests of acceptance gates, a judge's diagnostics served to a language-model proposer on negative controls" | AR, M7 |
| m1 (status, l. 9) | "the outcome is "frontier crossed, robust": the proposer finds a law" | "the outcome carries the frozen label "frontier crossed, robust" ("robust" qualifies the promoted laws, not the judge: at least half of them replay above α after Holm): the proposer finds a law" | AR, m1 |
| m1 (A1 row, l. 131) | ""frontier crossed, robust" (10 of 24; 10 of the 17 promoted laws replay above α after Holm)" | ""frontier crossed, robust" (frozen label; 10 of 24; 10 of the 17 promoted laws replay above α after Holm, against a frozen threshold of one half)" | AR, m1 |
| m2 | "*The Goodhart attack (section 4)*: CONFIRM already serves" | "*The Goodhart attack (section 4)* rests on the same 2015 principle (Dwork et al.; Blum and Hardt, above). CONFIRM already serves"; "and nothing else" is restored after the leaderboard attack | AR, m2 |
| m3 | "PACE (…) proposes unit tests for acceptors (p. 6)" | "PACE (…) runs what it calls a unit test for acceptors (p. 6)" | AR, m3 (author name "Shawn" kept, as AR says) |
| m4 | one block of about 5,300 characters | lead sentence plus a list, one item per principle; no change of substance | AR, m4 |
| m5 | v1 log: "8 commits behind", hour range | this log: 70 commits (4 first-parent); the base copies are in this folder | AR, m5 |

### C. The judge's null (O4): sentence and citations from `lecture-o4-englobement-v1.md`, section 4

- Before (v1): "*The judge's null*: the statistic is computed against a null formed by the known laws (the archive), so that a card is promoted only if its sealed prediction beats what the archive already predicts ("nothing beyond the archive")."
- After: "*The judge's null.* The judge promotes a hypothesis only if its prediction, sealed before the outcomes are read, beats, through an e-process computed outside the agents, the best fitted combination of the already known laws, including the organism's own archive ("nothing beyond the archive"). Judging a discovery against what is already known rather than against no effect is established practice (Feng, Giglio, Xiu, "Taming the Factor Zoo: A Test of New Factors", NBER Working Paper 25481, 2019, pp. 2–4), already applied to hypotheses proposed by language models (Liu, Liu, Liu, Mei, "Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing", SSRN 6569258, 2026, pp. 1, 4, 26, 28; Pan, Ding, Giesecke, "Agentic Empirical Asset Pricing: Methodological Foundations", arXiv:2609.00731v1, 2026, pp. 6, 7, 16, 25), and an e-process against the best fitted member of the current theory is published for a learned proposer (Ma et al., "Learning to Outgrow a Theory", arXiv:2610.07627v1, 2026, pp. 1, 4, 15)."
- How this differs from the faithful English rendering of section 4:
  - "Our judge" becomes "The judge", to match the page's third person.
  - Reservation (b) is applied: "sealed before the data exist" becomes "sealed before the outcomes are read".
  - Titles, versions and pages come from the note's table (section 2) and its verdict (section 0, points 1 and 2).
  - **The final clause is left out**: "we did not find this combination for hypotheses written by language models in the work we read, which is not a claim about the whole field". It is a "not found" statement, and the instruction says "no priority word". See section E, point 1.
- **Reservation (a): judge description checked against the public code** (`orchestrator/pole/nul_v8.py` at `be6b5af`, module docstring, l. 1-60). What I find:
  - The production null (v8) includes the member "ajuste_lineaire:archive". It is a linear pooling of all known laws (parents and survivors) and the blind laws, fitted by maximum likelihood. So "the best fitted combination of the already known laws, including the organism's own archive" is accurate.
  - The wealth is log W_t = log q(y) − max over the null's members of log p̂_m(y). The commitment q is frozen before the fresh draws, which are seeded by the hash of the frozen commitment (`selection_pari.tirer_frais`). Promotion happens at W ≥ 1/α under Ville's inequality (universal-inference likelihood ratio). This matches "an e-process computed outside the agents".
  - Nuance: the denominator is the best of **all** members, not only the fitted combination. It also includes the blind library, each survivor alone and mixed with the uniform law, and each survivor tempered and tilted. The sentence is therefore true but understates the null: beating the maximum implies beating the fitted combination. I left the note's wording as it is.
  - On the planted and toy worlds the outcomes are drawn after the freeze, so "before the data exist" would also hold there. On the frozen real bank it would not, so "before the outcomes are read" is the right wording.
- No word of priority. "Established practice" and "published" cede; nothing says free or not found.

### D. Defects of the live page, from the triage (class 1)

| tri | file, line | before | after |
|---|---|---|---|
| 1-a | README l. 128 | "**But a preregistered leak audit rules that the trained probe reads the saboteur's hidden instruction, present in its context, rather than the sabotage itself:** it separates the saboteur's actions that do *not* inflate the cost (area 0.9967 [0.9930, 0.9991], 46 actions) as well as those that do (0.9977)." | "**But a preregistered leak audit returned the frozen outcome "leak (reading the instruction)":** the trained probe separates the saboteur's actions that do *not* inflate the cost (area 0.9967 [0.9930, 0.9991], 46 actions from 12 of 60 tasks) as well as those that do (0.9977 [0.9958, 0.9993]). "Not inflated" is not "no sabotage": the probe may also read another trace of sabotage, and the arm that would separate the two was not run." This is the triage's exact phrase, which carries reservation 2 of the verdict (FU l. 7; reader's recommendation l. 65). |
| 1-a | README l. 128, last sentence | "**Consequence:** no white-box-versus-black-box claim stands on this organism; the next test uses organisms whose sabotage is trained into the weights, with no instruction in the context, against a stronger black-box baseline." | "**Consequence:** no white-box-versus-black-box claim stands on this organism." (roadmap removed) |
| 1-a | R1 page l. 9 | "**But the trained probe reads the instruction, not the sabotage.**" | "**But the trained probe reads the instruction; whether it also reads the sabotage is not separated.**" The reservation-2 sentence is appended after "with 5 written reservations." The triage names this line as stronger than the verdict. The coordinator named one leak sentence; I applied the same narrowing to both pages so they agree. |
| 1-a | R1 page l. 11 | "No white-box-versus-black-box claim stands on this organism. Next: organisms whose sabotage is trained into the weights (…), against a stronger black-box baseline." | "No white-box-versus-black-box claim stands on this organism." |
| 1-a | R1 page l. 3 | "Last updated: 8 November 2026, 09:20 UTC." | "Last updated: 13 November 2026 (the leak sentence narrowed to the second reservation of the audit's verdict; a sentence on next steps removed); previous update: 8 November 2026, 09:20 UTC." |
| 1-b | README l. 130 | "The strongest cells were selected after exploratory runs; frozen reading by the code, no fresh-reader verdict." | "The strongest cells were selected after exploratory runs. Fresh-reader verdict (one reader, 10 November 2026): "confirmed with reservations". All 886 cells conform; the raw counts were reproduced byte for byte from the recorded seeds by code extracted at the cited commit. Main reservation: most predictions are instrument checks, and the informative false-alarm magnitudes had been seen in exploratory runs before sealing (0.214, 0.364, 0.164)." The triage phrase is used, with "one reader" added (triage, reservation). Its last clause ("this validates the instruments in simulation, not the claim on real models") is dropped because the same row already says it (T0.3 verdict, l. 26-28 and section 7). |
| 1-c | README l. 7 | — | covered by sections B and C |
| 1-d | README l. 131 (A1 row) | "…against a frozen threshold of one half); 8 of 11 predictions held;" | "…; the sign of "resists", no false promotion, is already published (zero false admissions under a frozen referee: Qu, Chen, Wang, p. 15; none of 10,716 candidates admitted: CONFIRM, p. 9); 8 of 11 predictions held;" (pages as given by the triage, 1-d, and N-067, section 7) |

Left unchanged on purpose:
- R1 page l. 38 and l. 43 ("will be made public", "Next, each step preregistered…") are inside the dated text "Where it stood" (2 November), which the page keeps unchanged. They are not in the triage's list.
- The "+0.932" of the primary analysis in the R1 row: the triage notes that P-E1 is no longer cited as detection, but it did not ask for a change and the leak audit text was not read beyond the lines cited. It is listed in section E.

### E. To be decided by the project lead (not applied to the main diff)

These come from the adversarial reading's out-of-diff list (H1, H2, H3) and the coordinator's point 4. Each one changes text that is already online and that this correction does not touch.

1. **Final clause of the O4 sentence** (section C). Left out. If the project lead wants it: append ", and we did not find this combination for hypotheses written by language models in the work we read, which is not a claim about the whole field." N-067's clause applies: this is a "not found" statement on O4, and the O4 note itself (section 4 (c)) says the sentence is subject to the project lead's word (change of claim). The note's verdict also proposes that O4 now be said to be "occupied in part" (section 0): that is a decision node.
2. **Title, "cannot" (H1).**
   - Before: `# Ideation organism — an automated research pole that cannot grade its own homework`
   - After: `# Ideation organism — an automated research pole built so that no agent grades its own homework`
   - Reason: "cannot" is stronger than the first line of the section 3 table (the launcher and the ideation round still call the v56 stage). The title also makes a ceded principle (O1) the page's banner.
3. **"closes" (H2), status paragraph.**
   - Before: `a new null (v9) that closes it has a written, counter-read proof`
   - After: `a new null (v9) built to close it has a written, counter-read proof of its bound`
4. **Name of the private repository and commit (H3), README section 8.**
   - Before: `The tree is an exact extract of the private working repository `controle-ia-travail` at commit `91a3c7f8` (1 November 2026);`
   - After: `The tree is an exact extract of a private working repository at one commit (1 November 2026);`
   - Note: the commit identifier is also the anchor of the provenance chain. Removing it weakens the check, so the project lead may prefer to keep the commit and drop only the name.
5. **Private branch name and repository name (H3), MANIFEST l. 3.**
   - Before: `Extract of the private working repository `controle-ia-travail` (branch `canal/conv-audit-n04`, commit `91a3c7f8`, 1 November 2026).`
   - After: `Extract of a private working repository (commit `91a3c7f8`, 1 November 2026).`
6. **Private file name (H3), README l. 125.**
   - Before: `the output is sealed in the private working repository (`lecture-t05-graines-neuves-v1.json`, sha256 `07bc2aea…`;`
   - After: `the output is sealed in the private working repository (sha256 `07bc2aea…`;`
   - Note: `ecart-section13-v2.md`, also listed by the adversarial reading, is a public file of this tree (`resultats/banc-tricheurs-v8-validation-v1/`), so no couple is proposed for it.
7. **Promoted law described (H3), README l. 131.**
   - Before: `**42 of the 48 are, byte for byte, the world's own law** (the proposer copies the two archive laws per sub-population): a breach of the novelty criterion "nothing beyond the archive", not a false prediction,`
   - After: `**42 of the 48 reproduce the world's own law exactly**: a breach of the novelty criterion "nothing beyond the archive", not a false prediction,`
   - Note: the parenthesis says how the promoted laws were built, which is close to a recipe against the null. The fact that the breach exists stays.
8. **Other items of H3, no couple proposed** (outside the coordinator's list; for the record):
   - the reviewer named by function in section 7 ("the executive director of CeSIA");
   - "Gu-and-Krenn style" (two names without a reference);
   - the author's name and address in section 10 and `CITATION.cff`;
   - the docstring of the public file `orchestrator/pole/attaque_goodhart_v2.py`, l. 3, which names a person.
9. **R1 row, "+0.932" (triage 1-a, hardest objection).** Possible addition after "as the primary analysis predicted": "; after the leak audit, this comparison is not cited as detection of the sabotage". It needs a reading of the three analyses' verdict (`dece9980…`), which I did not read.
10. **N-067, section 4, point 3, against the code** (AR, section 7, point 1). The narrowed wording of O12 says "chargé de tromper" and "libre dans ses propositions". The public code says "rewarded if promoted" and "closed grammar". The page now follows the code. Whether the narrowed form of O12 still stands is a change-of-claim node for the project lead.

## Checks

- Forbidden-word scan of the three outputs ("instructed to deceive", "free in its", "not found", "we did not find", "novel", "to our knowledge", "no prior", "proves", "robust", "validat…"):
  - "robust" appears only as the marked frozen label;
  - "proves" appears only for REUSE's corollary;
  - "validat…" appears only in pre-existing labels and in pre-existing bounded sentences;
  - "novelty" appears only in pre-existing text (the novelty check, the novelty criterion).
- No session identifier, no private path and no person's name were added, other than cited authors.
- No recipe was added: the incentive is paraphrased from public code, and no promoted law, prompt text or run output is quoted.
- No refusal by a permission check or a classifier.
