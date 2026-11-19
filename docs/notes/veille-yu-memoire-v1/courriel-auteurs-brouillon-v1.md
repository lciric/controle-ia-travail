# Courriel aux auteurs de Yu et al. (2026) — BROUILLON, non envoyé — v1

- **Statut** : brouillon écrit le 19 novembre 2026 par un lecteur neuf de la session mère (modèle Fable 5.2). **Rien n'est envoyé par cette session.** Un contact externe est un nœud de décision : Lazar relit, corrige, signe et envoie s'il le veut.
- **Destinataire possible** : l'auteur correspondant nommé en première page du papier (p. 1 du PDF `a8299ba5…`). L'adresse n'est pas recopiée ici ; Lazar la prend sur le papier.
- **Ce que le brouillon ne contient pas** : aucun nom ni adresse d'expéditeur, aucun nom du programme, aucune description de nos travaux.
- **Pourquoi ces questions** : voir `lecture-yu-approfondie-v1.md`, § a.2, a.5, a.6 et réserve 3. Chaque question renvoie à une page du papier.
- **À vérifier par Lazar avant envoi** : le ton ; s'il veut dire qui il est et pourquoi il demande ; s'il veut garder la question 7 (concepteur fort), qui dit en creux ce qui nous intéresse.

---

**Subject:** Questions on the paired coding study and the SIM records in "Self-Improvement Memory Enables Continual Recursive Self-Improvement" (arXiv 2611.18856v1)

Dear authors,

Thank you for the paper, and in particular for stating plainly which results are repeated and which are single runs. I read it in full, appendices included, and reproduced the paired analysis from the ten differences in Table 3: mean 2.363, 95% interval [1.046, 3.680], t(9) = 4.058, p = 0.0029, exact signed-rank p = 6/1024 = 0.0059, d_z = 1.283. Everything matches what you report on page 8 and in Appendix C.4, and no single pair carries the result (leaving one out, the mean stays between 2.02 and 2.69).

I have a few questions that the paper does not let me answer. Any of the underlying data would help; I list them from most to least useful.

1. **Per-task outcomes for the paired study (Table 3).** With 33 held-out TB4 tasks and 165 rollouts, the ten differences add up to 39 more successful rollouts out of 1,650 for the SIM arm. Could you share the per-task, per-rollout pass/fail outcomes for the 20 target runs (and the 10 starting harnesses)? I would like to see whether the gain is spread over many tasks or concentrated in a few that flip, and how large rollout-level noise is on this split.

2. **The SIM JSON files of the ten source runs and their continuations.** Appendix D.3 describes the `predicted`, `fixed` and `missed` fields, and Figures 9, 10 and 12 show three entries. Across those published attempts I count 6 predicted task fixes realized out of 18 (P5: 4 of 6; P8: 0 of 4; P3: 2 of 8), and 1 of 8 on the target side. Is an aggregate prediction accuracy available over all entries and runs, ideally against a base rate? The full records would let me compute it.

3. **`passed` / `total` in a record.** The attempts shown have totals of 60 (source) and 33 or 36 (target), whereas the evolve splits have 220 and 165 rollouts (Table 4). On which tasks and with how many rollouts is a candidate evaluated during a round?

4. **Inheritance versus maintenance.** As your Limitations section says, the comparisons evaluate SIM as a complete procedure: the Harness Transfer arm has no memory during the ten target rounds, while Full SIM both inherits and updates. Did you run, or could you share, a condition that starts target RSI from the same evolved harness with an *empty* SIM that is then maintained during the target rounds? The first row of Table 1 (22.4 versus 21.4 on Gemini 2.5 Flash) seems to be the only comparison of that kind, and it is a single run.

5. **Use of predictions by the selector.** Appendix D.3 notes that an edit can be accepted "even if some predicted fixes failed", and both P8 attempts were accepted with none of their predicted fixes realized. Does the selector prompt refer to past prediction outcomes in any explicit way, or are they only available as context? If the proposer and selector prompts can be shared, that would settle it.

6. **Cost.** Appendix C.1 says token use and runtime can differ across conditions. Do you have token counts (or cost) per condition for the paired study, and the size of the SIM that is placed in the proposer's system prompt at the end of source and target RSI?

7. **A stronger harness agent.** Appendix E.4.2 replaces Gemini 3.8 Flash with Claude Opus 5.5 as proposer and selector during source RSI. Was any memory condition (Harness Transfer versus Full SIM, or Problem-Only) run with that stronger proposer and selector during target RSI?

Two smaller points, in case they are useful to you:

- The Terminus-2 row of Table 5 (19.39 → 19.39 without SIM, 21.82 with) does not appear among the ten rows of Table 3. Is it an eleventh source run?
- Problem-Only Memory is not part of the paired study, so the comparison between root causes only and the full record rests on one run per condition; in coding, two of those margins (1.21 points, i.e. two rollouts out of 165) are below the across-run standard deviation of the paired differences (1.84).

I would be glad to share my recomputation script and the tally of the published prediction records if they are of any use. If the data cannot be released, a short answer to questions 3 to 5 would already help a great deal.

With thanks and best regards,

[signature]
