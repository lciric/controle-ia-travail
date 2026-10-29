# Candidature EA Funds — Transformative AI Fund — brouillon v1

Rédigée le 2026-10-07 par la session, à la demande de Lazar. **Lazar relit, complète les champs marqués [TO COMPLETE] et soumet lui-même** (contact externe). Les réponses sont en anglais, comme le formulaire. Les notes pour Lazar, en français, sont en citation (« > ») : elles ne vont pas dans le formulaire.

Longueur des champs longs : 6963 caractères au total (maximum 10 000 ; recommandé 2 000 à 5 000 : « Project goals » et « Track record » peuvent encore être raccourcis).

## Select funds

- **Fund** : Transformative AI Fund.
- **Confirmation of fund scope** : cocher.
- **Funding from Coefficient Giving** : [TO COMPLETE : l'option qui s'applique].

> Coefficient Giving est l'ancien Open Philanthropy. Si tu n'as rien demandé ni reçu d'eux pour ce projet, choisis l'option correspondante.

## Basic information

- **Name** : [TO COMPLETE : prénom et nom].
- **Organization name** : (laisser vide : candidature individuelle).
- **Grant program** : Transformative AI Research Grants.
- **Main collaborators** :

  > Personne d'autre n'est connu de la session. Proposition :

  I work independently. Engineering, runs, literature checks and internal reviews are carried out by AI agents (Claude Code) that I direct, under the written protocol described in "Track record". [TO COMPLETE: any human advisor or collaborator.]
- **Email address** : lciric@ens-paris-saclay.fr [à confirmer].
- **Additional email addresses** : (vide).
- **Employed by or contracted with the Centre for Effective Altruism?** : I have never held a paid position (employee or contractor) at the Centre for Effective Altruism. [à confirmer]

## Project information

**Short description** (119 caractères sur 120 ; publique) :

12-month stipend and compute to detect diffuse AI sabotage by accumulating activation-probe scores over time and agents

**Summary** (989 caractères sur 1 000) :

Per-action monitors fail by construction against diffuse sabotage: an AI agent that subtly biases many research decisions (weaker controls, sterile directions, inflated costs) never takes one clearly suspicious action. I test whether evidence that stays invisible in outputs accumulates in the agent's activations: anytime-valid sequential aggregation of probe scores over time (paper A) and across agents sharing weights (paper B), plus a measurement of how easily monitors themselves are corrupted by persuasion (paper C). The programme states its theory (an additivity lemma, and a negative theorem saying when marginal-based aggregation must fail), pre-committed gates and pivots, and strict pre-registration (sealed plans, independent counter-reading, every number traceable). Phase 0 (Oct 2026) has validated the activation harness on Llama-3.1-8B and the aggregators in simulation (31/31 pre-registered predictions). Request: 12 months of my time plus compute, ~$92k (minimal $42k).

**Project goals** (2223 caractères) :

Goal: find out, with decisive pre-registered tests, whether white-box monitoring catches sabotage that is diffuse in time or spread across agents, and publish either outcome.

Steps (12 months from 1 Nov 2026):
1. Gate G0 (1 Nov): harness validated (done), aggregators validated in simulation (done), model organisms with dose-response, probes above a covariance-matched random floor, black-box baseline running.
2. Paper A, time (Nov-Dec): research-sabotage environment (open-weights 8B port of Terekhov et al., arXiv 2606.08892) with pre-registered seeded ground truth; organisms with a hidden instruction and with a LoRA-distilled sabotage policy; a 2x2 design, access (black/white box) x aggregation (per action/sequential); the lemma tested on real activations; adaptive attacks, including fine-tuning and RL against the probe. Gate G1: white-box sequential must beat the best black-box baseline on recall at 1% false-positive rate (95% CI); otherwise the negative result is published.
3. Paper C, the instrument (Nov-Feb): how much persuasion moves LLM judges versus probes, the cost of moving a probe (activation obfuscation) versus a judge (rhetoric), countermeasures, and an acceptance test for monitors before deployment.
4. Paper B, the swarm (Feb-May): shared-weight agents in a code pipeline with backdoors fragmented across commits; population statistics versus per-agent monitoring; security as a function of the number of agents.
5. Release of code, organisms, probes, pre-registrations and sealed results.

Path to impact: labs that automate AI research have white-box access to their own agents. If accumulated probe evidence works, it is a cheap monitoring layer against research sabotage, which per-action monitoring cannot address; if it fails, the negative theorem and a construct-validity analysis show where probes should not be trusted.

How I will know: each gate is decided against criteria frozen before data collection, by a reviewer who wrote neither the plan nor the analysis.

Main risks: 8B organisms may be too weak to sabotage subtly (pre-registered fallback); the internal signal may be absent (both outcomes publishable); novelty erosion (weekly literature watch, pre-committed pivots).

**Track record** (1630 caractères) :

[TO COMPLETE: education and current position (ENS Paris-Saclay), relevant ML and statistics experience.]

Previous project (P3): construct validity of sycophancy in Llama-3.1-8B-Instruct, pre-registered, with covariance-matched controls and bit-exact reproducibility over 120 five-turn dialogues. Lessons carried over: never read verdicts on truncated windows; prefer ordinal or continuous instruments. [TO COMPLETE: link or status.]

This programme (started 5 Oct 2026). I set the questions and take every decision; execution (code, runs, literature checks, internal reviews) is done by AI agents (Claude Code) under written rules: each decisive experiment has a SHA-256-sealed pre-registration, counter-read by a fresh agent instance before any data; stop guards are tested on a healthy case and on an artefact; verdicts come from a fresh reviewer, then my sign-off. Weakness, stated plainly: these reviewers share a model family, so their errors may be correlated; human expert checks are budgeted. Outputs in the first week:
- literature verified on primary sources: 98 arXiv PDFs retrieved and hashed, 24 reader reports, 3,497 quotations checked by script with 0 failures, 147 corrections to our own documents;
- simulation of the lemma and the negative theorem: 31/31 pre-registered predictions confirmed;
- activation harness validated on Llama-3.1-8B on a rented H200, after two honest failures (v1 inconclusive, v2 partial) and a revised pre-registration;
- 602 automated tests; compute spent so far about $20.

Expenditure and staffing: 2026 to date, about $20 of compute plus an AI-tooling subscription; 1 FTE (myself).

> Je recommande de garder la phrase sur les agents d'IA : elle est vraie, elle explique le débit et le faible coût, et un relecteur qui le découvrirait plus tard le reprocherait. La faiblesse associée (relecteurs de la même famille de modèles) est dite, avec sa parade budgétée.

**Public Portfolio** :

[TO COMPLETE: P3 write-up or poster if public; GitHub profile https://github.com/lciric.] The programme repository is private; pre-registrations, sealed results and decision registers can be shared with fund managers on request.

## Funding

**Funding amount and breakdown** :

Budget spreadsheet: [TO COMPLETE: link to the Google Sheet made from budget-v1.csv, "anyone with the link can view"].

Mainline, 12 months: $91,740. Breakdown: 65.4% stipend for me (including social contributions and income tax), 6.5% GPU compute and storage, 7.8% AI research tooling, 4.4% human expert validation of ground truth, 5.5% travel and dissemination, 1.3% miscellaneous, 9.1% buffer (10% of the subtotal, stated explicitly).

Range:
- minimal, 7 months, papers A and C only: $41,800;
- mainline: $91,740;
- ambitious, 12 months, adding a part-time research engineer for paper B, a statistics co-author for the lemma, a 70B organism family and RL attacks at scale: $146,300.

Total project budget equals the requested amount; no other funding is secured.

> Le tableur `budget-v1.csv` (même dossier) s'importe dans le modèle de budget d'EA Funds ou dans une feuille Google. Le lien partagé doit être en lecture pour « toute personne ayant le lien ».

- **Requested amount (USD)** : 91740
- **Organizational budget (USD)** : (vide : pas d'organisation).

**Alternatives to funding** :

[TO COMPLETE: every funding application of the last 12 months, with funder, date, status, amount, decision date, including the fellowship/cohort mentioned in the programme.]

Without this grant, the programme continues at reduced scale: phase 0 and papers A and C on 8B models, with self-funded compute (a few thousand dollars), more slowly, without the multi-agent phase (paper B), and with less of my time, since I would need other income.

**Use for additional funding** :

Move toward the ambitious scenario, in this order: (1) a part-time research engineer for the multi-agent environment of paper B; (2) a 70B organism family and replication on a second model family, for external validity; (3) RL-based adaptive attacks at larger scale; (4) more paid expert annotation of ground truth; (5) a statistics co-author for the lemma; (6) runway to finish the NeurIPS 2027 submission and the release.

## Further information

- **Confidential information** (proposition) : The hypotheses and claims in this application are unpublished; please do not share them beyond the fund team and advisors. I can give reviewers read access to the private repository (pre-registrations, sealed results, decision registers).
- **LinkedIn/CV** : [TO COMPLETE : profil LinkedIn ou CV en ligne] ; https://github.com/lciric
- **File upload** : (rien, ou le budget si tu préfères le joindre).
- **Start date** : 01/11/2026. **End date** : 31/10/2027.
- **Requested currency** : [TO COMPLETE : EUR ou USD].

  > EUR si la bourse est surtout ton revenu en France (pas de risque de change sur l'essentiel) ; le calcul est facturé en dollars, mais c'est 6,5 % du budget.
- **Location** : [TO COMPLETE: city], France. Research runs remotely on rented cloud GPUs; outputs (papers, code, organisms, probes) are public and international.
- **China or India?** : No.
- **Award?** : No.
- **People under 18?** : No.
- **Safeguarding** : (vide).
- **Lobbying or political activity?** : No.
- **References** : [TO COMPLETE : une ou deux personnes, avec courriel et une phrase chacune ; idéalement quelqu'un qui connaît P3, et quelqu'un du domaine de la sécurité de l'IA].
- **Organisational leadership** : (vide).
- **Referral to other funders** : Yes.
- **Secondary fund, EA Infrastructure Fund** : Yes (sans inconvénient ; le projet n'y correspond guère).
- **How did you hear about EA Funds?** : [TO COMPLETE].
- **Time-sensitive grant (decision within eight weeks)?** : [TO COMPLETE : No, sauf si la bourse doit relayer un revenu qui s'arrête bientôt].
- **Public reporting** : [TO COMPLETE : public, anonyme ou privé].

  > Je recommande « public » : la description courte ne révèle rien qui ne sera publié de toute façon, et le choix privé « peut légèrement réduire » les chances selon le formulaire.
- **Network sharing** : Yes.
- **Anything else** : (vide, ou : « Pre-registrations, sealed results and decision registers are available to fund managers on request. »)
- **Please confirm grant reporting** et **Please review your responses** : cocher.
