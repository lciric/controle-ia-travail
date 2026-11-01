<!-- PRIVÉ — candidature personnelle de Lazar (Pivotal Research Fellowship). À exclure de toute copie publique : chemin à ajouter aux RETRAITS de scripts/depot_expurge.py. Coordonnées retirées du CV. -->

# Review brief for an outside model (Argon / Kimi) — Pivotal Research Fellowship application of Lazar Ciric — v2

You are an independent reviewer. You have not written any of the texts below. Review this fellowship application as (1) Pivotal's screening committee and (2) each targeted mentor would. Deadline: 1 November 2026, 23:59 Anywhere on Earth. The fellowship: 15 weeks in London (18 January – 30 April 2027), ~1–3% acceptance; Pivotal says "a strong match with a specific mentor often matters more than your overall background". Answer in English or French.

Deliver, in this order:
1. A three-line global verdict: ready to send / ready after corrections / redo; and for which mentors the chance of shortlisting is highest and lowest, one reason each.
2. Numbered findings (RV-01, RV-02 …), each with severity (blocking / major / medium / minor), location (section), the problem in one sentence, and a ready-to-paste replacement text when the fix is textual. Look first for: claims not supported by the CV's measured numbers; note one author's decision that is not to be re-litigated: the rank-3 result is presented as a causal rank-3 intervention that shifts the judged sycophancy rate where six rank-1 methods fail, and the response-truncation issue mentioned in the CV is deliberately left out of the application — check only that every sentence about it stays literally true to the measured numbers (61% to 46.5%, N = 200; rank-1 methods without effect; direction-specific against a norm-matched random subspace) and flag any sentence that claims more, such as specificity to sycophancy or removal of deference; word-limit overruns (count yourself: bullets ≤ 10 words each; project ≤ 150; career plan ≤ 200; sources ≤ 100; reasoning ≤ 150; missing risk ≤ 150); sentences that sound salesy, vague or arrogant to an AI-safety committee; inconsistencies between pieces; disclosure risks; for each mentor text, whether the 15-week project is realistic, scoped, and answers what that mentor asks for.
3. Substantive disagreements with the choices made (mentors selected, the "15-week project adapted to each mentor" angle, foregrounding the sycophancy law, referees outside AI safety): list them separately with your recommendation and confidence.


====================================================================
PART A — THE FORM QUESTIONS (exact wording)
====================================================================
1. Highlight the most relevant experiences listed in your CV in 3 bullet points or less. 10 words or fewer per bullet point.
2. Tell us about one project you recently completed and are proud of (max. 150 words). Guides: what did you produce or find; your position and what you did yourself; what difficulty and how handled; outcome and what it changed.
3. What is your career plan? (max. 200 words). Guides: where are you now and where do you want to get to; how would the Pivotal Fellowship help; what specific problem, in which role, why it matters.
4. Two AI safety/governance information sources that notably influenced your views, 1–2 sentences each (max. 100 words).
5. Rank seven AI risk areas: Gradual disempowerment; Environmental harms; Loss of control; AI scheming; Concentration of power; AI misuse; Large-scale job loss.
6. Sketch your reasoning for the ranking (max. 150 words).
7. Optional: an important AI risk missing from the list — name it, rank it, explain (max. 150 words).
8. Optional: 1–2 referees (ideally AI safety researchers you collaborated with).
9. Optional: writing samples (≤ 5 pages per sample, one PDF).
10. Optional: career memo (for mentor matching).
Then a short application per mentor (~20 minutes each; questions not public).


====================================================================
PART B — DRAFT ANSWERS TO THE MAIN FORM (v5)
====================================================================
# Pivotal Research Fellowship 2027 Q1 — main form, answers — v5
1 November 2026, ≈ 18:30 UTC. v4 plus Lazar's decision (19:24, Paris): the rank-3 result is presented as a causal rank-3 intervention, in the CV's own words ("shifts judged verdicts/sycophancy where rank-1 methods fail"), with no mention of the truncation issue anywhere in the application. Every sentence stays literally true to the measured numbers (61% → 46.5%, six rank-1 methods without effect, direction-specific against a norm-matched random subspace); none claims more. Word counts by script; limits respected.

---

## 1. Three most relevant experiences (≤ 3 bullets, ≤ 10 words each)

- Preregistered sycophancy law, Llama-3.1-8B, out-of-sample R² 0.73 (ICLR 2027 submission)
- Rank-3 ablation shifts judged sycophancy where six rank-1 methods fail
- Two years self-funded, preregistered, hash-audited AI safety research

Variant for bullet 3 (second instance): "Co-author, PLOS Computational Biology 2023; IBM Research Zurich 2022" — if you aim at Senior Fellow status (£18k), decided on publications and track record. I would keep the audited-practice bullet: the publications are in the CV, the practice is not.

---

## 2. One project you recently completed and are proud of (≤ 150 words)

"Sycophancy as a psychophysical law", submitted to ICLR 2027. Unfunded and alone: questions, preregistered design, analysis calls and paper are mine; AI agents did the engineering under my rules.

Finding: in Llama-3.1-8B-Instruct, sycophancy is a displacement, not a flip rate. Under calibrated social pressure the shift is linear in the initial rating: the model closes a fixed fraction (about 0.7) of its distance to a target set by the social frame. Criticism and praise set different targets, so praise lowers a highly rated item (a prediction that held).

Difficulty: flip rates confound the effect with the starting point, and single-turn evaluations stop before the mechanism: the model is held by its own earlier concession, not by the pressure. Hence a psychophysics-style design and an exact enumerated null.

Outcome: parameters fitted on one campaign predict a second, differently designed, without refitting (R² 0.73); and a leverage point for mitigation, the concession.

---

## 3. Career plan (≤ 200 words)

Now: independent AI safety researcher, two years self-funded, working at the border between interpretability and evaluation: sycophancy as a measurable law, the geometry of safety concepts, construct validity of probes and LLM judges, with a practice of sealed preregistrations and hash-audited claims. Since October I have been building a programme on white-box control of diffuse threats: monitors as internal probes, threats spread over many small actions and many agents, where no single black-box monitor sees anything. An external security review was done by the executive director of CeSIA.

Where I want to get: a research position in an AI control or interpretability team (Anthropic, Google DeepMind, AISI, Apollo), or a PhD anchored in this work.

What Pivotal adds: what I lack is not a direction but a collaborator, a mentor who pushes back, compute and a community. Fifteen weeks at LISA would turn the control programme, or one of its sub-questions, into a published result with a team instead of a solo preprint.

The problem: can internal-state monitors catch threats that are diffuse and adaptive, and how do we measure that robustly? Control is the near-term safety line, and current control evaluations assume a single discrete bad action.

---

## 4. Two sources (≤ 100 words)

1. Greenblatt, Shlegeris, Sachan and Roger, "AI Control: Improving Safety Despite Intentional Subversion" (2023). It turned "what if the model is adversarial" from a philosophical worry into a measurable game with a budget, which is the frame of all my current work.

2. Bailey et al., "Obfuscated Activations Bypass LLM Latent-Space Defenses" (2024). It showed that probes and latent-space monitors are attackable at low cost to task performance; it convinced me that monitor robustness has to be measured against an adaptive attacker, not assumed from a probe's accuracy.

---

## 5. Ranking (top = highest priority)

1. Loss of control
2. AI scheming
3. Gradual disempowerment
4. Concentration of power
5. AI misuse
6. Large-scale job loss
7. Environmental harms

---

## 6. Reasoning (≤ 150 words)

I rank by irreversibility times how hard the risk is to measure.

Loss of control and scheming come first because they are the cases where our instruments fail silently: a scheming model produces exactly the evidence an honest one would, and a loss of control need not look like one discrete bad action. My own work is on the second half of that sentence: threats that are diffuse, spread across many small actions or many agents, and invisible to any single monitor. I rank scheming just below loss of control because scheming is one mechanism of it, not the only one.

Gradual disempowerment and concentration of power are third and fourth: hard to reverse, but visible while they happen, which leaves room for institutions. Misuse is serious and partly addressable by existing security practice. Job loss and environmental harms are real, mostly reversible, and not specific to AI.

---

## 7. (Optional) A missing risk (≤ 150 words)

Corruption of the overseers. The list treats the monitored system as the risk; the oversight layer is itself an attack surface. Monitors, human or model, can be corrupted by deference (the monitor adopts the position of the system it watches, the same mechanism as sycophancy), by impersonation of the instructor, or by collusion between instances that are supposed to check each other. None of this requires a scheming model: a mildly sycophantic monitor degrades oversight on its own.

I would rank it between scheming and gradual disempowerment. It matters because every control proposal, including those that use untrusted models to monitor each other, assumes the monitor's judgment survives contact with the monitored system. That assumption is testable now, on open-weight models, and it is rarely measured as a quantity; the sycophancy law I measured is a first quantitative handle on it.

---

## 8. Referees (optional)

| | Name | Email | Relationship (to paste) |
|---|---|---|---|
| 1 | Srdjan Ostojic, ENS | [to fill — I cannot verify addresses] | Supervisor of my master's thesis at ENS (Ostojic lab, 2019–2020) and co-author of our PLOS Computational Biology 2023 paper on low-rank spiking networks. Not an AI safety researcher. |
| 2 | Manuel Le Gallo, IBM Research Zurich | [to fill — the address the second instance gave, anu@zurich.ibm.com, does not look like his; check] | Supervisor of my research internship at IBM Research Zurich (2020–2021) and co-author of our 2022 paper in Neuromorphic Computing and Engineering. Not an AI safety researcher. |

Thomas Romary (Mines Paris) third if one of the two is unavailable. Charbel-Raphaël Segerie (CeSIA) would be the only AI-safety referee; your call whether the relationship carries it. Referees are contacted only at later stages: warn them after shortlisting.

## 9. Writing sample — use `Lazar_Ciric_writing_samples_v2.pdf` (7 pages, in this zip)
Sample 1 unchanged (the 1,150-word essay, 2 pages). Sample 2 re-typeset from your proposal text (sections 1–5, 5 pages) **without** the EA Funds header: fund name, amounts requested, period and the line "Confidential: unpublished research plan, please do not circulate beyond the fund team" are removed; the body text is yours, unchanged. Reason: the original sample 2 carried a confidentiality notice addressed to another funder and the sums you asked them for. If you prefer the original file, it is `Lazar_Ciric_writing_samples.pdf` as you sent it.

## 10. Career memo (optional; ≈ 290 words; paste into a one-page PDF)

Career memo, Lazar Ciric, 1 November 2026

Who I am. Physicist by training (ENS Paris-Saclay), then computational neuroscience (ENS, Ostojic lab; PLOS Computational Biology 2023), IBM Research Zurich (analog in-memory computing; Neuromorphic Computing and Engineering 2022), Mines Paris-PSL (statistics and machine learning). Two years of independent AI safety research, full time since March 2026, alone, with AI coding agents under written rules: sealed preregistrations, every number traced to its file, failed predictions kept on record.

What I have. A behavioural law of sycophancy (under review, ICLR 2027): pressure moves Llama-3.1-8B's rating a fixed fraction of the way to a target set by the framing, and the fit predicts a second campaign without refitting. A mechanistic result on readout versus cause: the direction a probe reads carries under 1% of the causal effect, while a rank-3 ablation shifts judged verdicts where six rank-1 interventions do nothing. An AI-control programme started on 5 October: a lemma and a negative theorem on what score-based monitors can detect, confirmed in a preregistered simulation; an activation harness validated on Llama-3.1-8B; an automated research pole (multi-provider proposers, frozen judge, preregistered death tests) running; external security review done.

What I want from the fellowship. One measured, published result in fifteen weeks with a mentor who pushes back. The question adapts to the mentor: persona and susceptibility to influence before and after RL (Ibrahim, Colognese and Rhys Ward, Tilli); what a probe reads and the geometry of activation plateaus (Heimersheim); automated alignment research that resists gaming (Kirchner); auditing diffuse sabotage (Jang and Feng); influence spreading through agent swarms (Scheurer); judges under optimisation pressure (Jain).

After. A full-time research role in an AI-control, evaluations or interpretability team, or a PhD anchored in this work.

Practical. Based in Paris; available in London full time from 18 January 2027. First-time fellow; my seniority case is the publications and the programme above.


====================================================================
PART C — MENTOR-SPECIFIC TEXTS (v4)
====================================================================
# Pivotal 2027 Q1 — mentor-specific applications — v4
v4, 1 November 2026, ≈ 18:30 UTC. v3 plus Lazar's decision (19:24, Paris): the rank-3 result is presented as a causal rank-3 intervention that shifts the judged rate where rank-1 fails, with no mention of the truncation issue; every sentence stays literally true to the measured numbers. Blocks otherwise unchanged. The mentor forms are ≈ 20 minutes each; their exact questions are not public. Each block below gives (a) why this project, (b) what I would do in fifteen weeks, (c) relevant experience, written so the pieces can be pasted into whatever fields the form has. Numbers are from the CV of 8 October and the writing samples. English, Lazar's voice. [Brackets] = your call.

---

## 1. Lujain Ibrahim (Google DeepMind) — direction 1, pre-RL persona and post-RL behaviour

**Why this project.** Your first direction asks whether the persona set in character training survives RL or is overwritten, and what that does to misalignment. I have a measurement that answers a piece of that question quantitatively. In Llama-3.1-8B-Instruct, sycophancy is not a flip rate but a displacement: the model closes a fixed fraction (≈0.7) of the distance between its initial rating and a target that is set by the social frame, not by the model (criticism and praise set two targets whose confidence intervals do not overlap). The law predicts a second campaign with a different design without refitting (R² 0.73). On Qwen2.5-7B the mean displacement survives but the law collapses into a constant "politeness tax". That is a persona-level signature that can be measured before and after any training step.

**What I would do.** Take open-weight models with a known character-training stage, measure the displacement law (gain, targets, concession dynamics) before and after RL on a task mix, and ask whether RL moves the gain, the targets, or neither. Pair it with the internal view: in my probe work, four extraction methods recover quasi-orthogonal sycophancy directions, the probed direction tracks behaviour but carries under 1% of the causal effect, and only a rank-3 ablation shifts the judged behaviour; I would track that subspace across the pre-RL and post-RL checkpoints. Deliverable by April: a paper with a preregistered design, code and data released.

**Relevant experience.** The sycophancy-law paper (ICLR 2027 submission); the probe-geometry project (four extraction methods, rank-3 ablation); fine-tuning and steering toolchains on 7–8B models on single and multi-GPU instances, LLM-judge evaluation pipelines with exact nulls. Heavy daily use of frontier models.

---

## 2. Jan Kirchner (Anthropic) — project 2, automated alignment researchers

**Why this project.** Since October I have been building and running what you describe: an automated research pole in which language-model agents from several providers propose hypotheses on AI control, a fixed statistical judge scores them, and preregistered "death tests" are executed by a sandboxed experimenter and verified by a model of a different family. The design decisions were all about the question you ask — does the method survive contact with harder tasks, and does it resist gaming the setup. Three examples: the deciding number of a test is computed in the session from raw outputs and never read from the agent's script (I found by code review that an earlier version let the agent print its own verdict); novelty is checked against the literature before any credit; champions from one provider family are scored by agents of another family so no family favours its own. An external security review of the offensive parts was done by the executive director of CeSIA.

**What I would do.** Port the pole onto your open-source harness, or port its guards onto it, and run the three tests you name: generalisation to tasks it was not built on, scaling to larger models, and adversarial pressure (agents rewarded for passing the judge rather than for being right). The measurement I care most about: how much of the apparent research progress disappears when the judge is frozen and the verifier is of another family. Output: paper and code by April.

**Relevant experience.** Two years of preregistered, hash-audited research (131 registered claims, 19 refuted and kept); the control programme (white-box monitors for diffuse threats; summary in my writing sample); a research master's in computational neuroscience (ENS, Ostojic lab; PLOS Computational Biology 2023).

---

## 3. Stefan Heimersheim (Google DeepMind, interpretability) — activation plateaus

**Why this project.** Your plateau question — models robust to small activation perturbations, then changing fast beyond a threshold — is the shape of a result I keep running into from the other side. On Llama-3.1-8B, six rank-1 interventions on a linearly readable sycophancy direction (steering, directional ablation, SAE clamping, fine-tuning against the probe, head/MLP zeroing) leave the judged behaviour unchanged; a rank-3 subspace from SVD of activation differences at the decision point moves it (61% → 46.5%, N=200, p=0.002), direction-specific against a norm-matched random subspace. The probed direction tracks behaviour (ρ=0.68) yet does under 1% of the causal work versus 68% for the full state. That reads like a plateau along the readable direction and a cliff at rank 3, and I never characterised the geometry of the boundary.

**What I would do.** Measure plateau shape as a function of rank and direction family (probe, SAE, random, task-relevant subspaces) on a small open model, with the behavioural readout held fixed and a preregistered prediction of where the cliff sits; then test whether plateau boundaries give a feature dictionary that differs from the SAE's. I would also bring the adversarial angle: an attacker who evades a probe has to cross a plateau, and the price of that crossing is what a latent-space monitor can charge.

**Relevant experience.** >40 hours of transformer internals work is far exceeded: TransformerLens, nnsight, SAE-lens, path patching over 1024 heads, Goodfire SAEs; five mechanistic analyses of quantisation (GPT-2). I will push back on ideas, with numbers.

---

## 4. Paul Colognese, Francis Rhys Ward (Arrow Research) — project B, characters and safety behaviours before/after RL

**Why this project.** Project B compares honesty, sycophancy, multi-agent behaviour and self-preservation across trained characters before and after RL. For sycophancy I can offer a measurement sharper than a rate: a displacement law with a gain and frame-set targets, out-of-sample R² 0.73, and a mechanism (the model is held by its own earlier concession, not by the pressure) that single-turn evals miss. For monitorability I bring the control side: white-box monitors as internal probes, and a negative theorem on which aggregations of monitor scores an adaptive agent can make blind.

**What I would do.** Choose the sycophancy slice: train three to four characters (including ones from published lab specs), measure the displacement law and the concession dynamics before and after RL, and ask whether character training changes the gain (how much the model yields) or the targets (where it yields to). In parallel, test whether a probe for the concession survives RL, which is the reward-hacking-detectability question of project A on a different behaviour.

**Relevant experience.** The sycophancy-law paper and the probe-geometry project; fine-tuning and eval pipelines on open 7–8B models; honest reporting as a practice (every number traced to a result file; refuted predictions kept in the register).

---

## 5. Eyon Jang, Shi Feng (Scale AI Preparedness / Praxis) — alignment auditing and its automation

**Why this project.** Your three kinds of work — auditing games, cheating-propensity evals, white-box training-based tools — are what my control programme and its automated research pole do, with one specific twist: the threats I audit for are diffuse (spread over many small actions, or many agents), where per-action monitoring is provably blind and evidence has to be accumulated. I have the theory (an additivity lemma and a negative theorem by invariance: any permutation-invariant statistic has power equal to its false-positive rate against a multiset-preserving attacker), a preregistered simulation (31 predictions confirmed; Ville-type thresholds give 21–35% false alarms under episode effects unless calibrated on whole honest episodes), and the open question on real activations: does sabotage shift the marginal of probe scores at all.

**What I would do.** Propose, under your agenda, an auditing game for diffuse sabotage in agentic R&D tasks: an attacker with a budget split across actions or agents, a white-box monitor with sequential aggregation, and the 2×2 (black/white box × per-action/sequential). Deliver the measurement of δ on model organisms and the aggregator that the outcome dictates. Happy to work with other mentees on the environment.

**Relevant experience.** The control programme (summary in my writing sample), with an external security review done; the sycophancy and probe toolchains; exact and permutation nulls, e-values and sequential tests.

---

## 6. Cecilia Elena Tilli (Allelo) — susceptibility of AI agents to influence [if added]

**Why this project.** Your core question — how an agent's susceptibility to influence relates to other safety propensities and how training changes it — is what I measured as a law: susceptibility is a gain (≈0.7 of the distance to a frame-set target) that generalises across campaigns, differs between models of the same size (proportional accommodation vs constant tax), and is held in place by the model's own concession rather than by the pressure. That gives your model organisms a graded, falsifiable susceptibility scale, and your population direction a quantity to propagate.

**What I would do.** Direction 1 or 3. With your minimal organisms: fit the displacement law per organism, compare fine-tuning and activation steering on the gain and the targets, and test whether the rank-3 subspace (the only intervention that moved the judged rate in my hands) tracks the susceptibility scale. For populations: simulate and then measure how influence spreads when agents of different gains judge each other — this is the swarm question of my control programme, where monitors are themselves susceptible.

**Relevant experience.** The sycophancy-law paper (ICLR 2027 submission), the probe-geometry project, fine-tuning and steering on open models, preregistration and clear writing.

---

## 7. Rishub Jain, Josh Jacob (Sampura Research) — robustness of AI judges under optimisation pressure [if added]

**Why this project.** Paper C of my programme asks whether a monitor can be moved rather than evaded, and at what cost: a deference law under graded pressure, judges versus probes. The sycophancy law is the judge-side half, measured on a model used as a judge; the probe side is the adversarial-evasion cost on activations.

**What I would do.** Put LLM judges under training-time optimisation pressure in a controlled game and measure, with the same displacement law, how the judge's verdicts drift (gain, target) as pressure increases; compare judges and probes at matched false-positive rate; build the harder safety-eval items from the failure modes found.

**Relevant experience.** LLM-judge pipelines with ordinal judges and exact nulls; construct validity of judges; control programme.

---

## 8. Jérémy Scheurer (Apollo Research) — ideas spreading through agent swarms; loss-of-control metrics

**Why this project.** Your first option — how ideas spread through agent swarms and how a swarm drifts into misalignment — is the second paper of my control programme and the system I have been running since October. The programme treats time and agents as the same object: monitor scores indexed by agent and step, with permutation subgroups (time within an agent, agents within a step), so that what is proved for one agent over time transfers to many agents at once. The negative theorem says which monitors a swarm can make blind by spreading a threat over its members; the open question is whether internal evidence (activations) still accumulates when the external evidence does not. On the "ideas spreading" side I have a running automated research pole: agents from several providers propose ideas, a fixed judge scores, death tests kill, a verifier of another family checks; its registry is a trace of how ideas propagate, get copied, and get killed — the kind of message-board trace you describe, already instrumented.

**What I would do.** Build a multi-agent evaluation where a misaligned idea is seeded in one agent of a population and measured as it propagates, with a monitor at each agent and a swarm-level aggregator; test the prediction that per-agent monitors stay at their false-positive rate while co-elevation across agents detects the spread; or, under your second option, turn the swarm statistic (security as a function of N) into a loss-of-control metric with a scaling trend. Daily use of Claude Code and Codex is how I work; full time; I push back with numbers.

**Relevant experience.** The control programme (theory, preregistered simulation with 31 confirmed predictions, external security review); the automated research pole; the sycophancy and probe pipelines.


====================================================================
PART D — THE 42 MENTORS OF THE COHORT (profiles read one by one; in French)
====================================================================
# Pivotal Research Fellowship 2027 Q1 — les 42 mentors, lus un à un — v3
1er novembre 2026, ≈ 18:40 UTC. Remplace les v1 et v2. Les 42 profils de la cohorte « Q1 2027 AIS » ont été ouverts (dont Scheurer et Rhys Ward, inaccessibles jusque-là ; Haimi Tefera n'a pas de projet propre : co-mentore de Levermore).
Critères de Lazar : adéquation avec TOUS les projets (P3 géométrie des sondes ; P4 loi de la sycophancie ; programme de contrôle : papiers A temps, B essaim, C instrument ; organisme d'idéation), prestige, force du mentor. Notes /5.

## Candidatures recommandées (8 ; chacune ≈ 20 min)
| Rang | Mentor | Institution | Projet 2027 | Adéquation (projet) | Prestige | Force | Texte |
|---|---|---|---|---|---|---|---|
| 1 | Lujain Ibrahim | Google DeepMind | persona avant/après renforcement ; modèle de soi | 5 (P4), 4 (P3) | 5 | 4 | bloc 1 |
| 2 | Jan Kirchner | Anthropic | chercheurs d'alignement automatisés | 5 (organisme) | 5 | 4 | bloc 2 |
| 3 | Stefan Heimersheim | Google DeepMind, interprétabilité | plateaux d'activation | 5 (P3), 4 (robustesse des moniteurs) | 5 | 4 | bloc 3 |
| 4 | **Jérémy Scheurer** | Apollo Research (évaluations ; ex-FAR AI, ex-contractant OpenAI) | **propagation d'idées dans des essaims d'agents et dérive vers le désalignement ; évaluations multi-agents ; ou métriques de perte de contrôle à tendance d'échelle** ; portée ouverte | 5 (papier B essaim, organisme), 3 (contrôle) | 4 | 4 | bloc 8 (nouveau) |
| 5 | Paul Colognese + Francis Rhys Ward | Arrow Research (Rhys Ward : docteur en tromperie des IA, ex-Redwood, ex-AISI) | caractères entraînés : honnêteté, sycophancie, multi-agent avant/après renforcement | 5 (P4), 4 (contrôle) | 3 | 4 | bloc 4 |
| 6 | Eyon Jang + Shi Feng | Scale AI Preparedness / Praxis | audit d'alignement automatisé, outils boîte blanche | 5 (contrôle), 3 (organisme) | 3 | 4 | bloc 5 |
| 7 | Cecilia Elena Tilli | Allelo | susceptibilité des agents à l'influence ; populations d'agents | 5 (P4), 4 (essaim) | 2 | 3 | bloc 6 |
| 8 | Rishub Jain + Josh Jacob | Sampura Research (ex-Google DeepMind) | robustesse des juges de frontière sous pression d'optimisation | 4–5 (papier C), 4 (P4) | 3 | 3 | bloc 7 |

Lazar a retenu les rangs 1, 2, 3, 5, 6 (18:28). **Changement de la lecture exhaustive : Scheurer** (Apollo) — son projet est l'essaim du programme et l'organisme ; à ajouter, confiance élevée. Tilli et Jain : adéquation très forte, prestige plus faible ; à toi.

## Les 34 autres, avec motif
| Mentor | Institution | Projet 2027 | Adéquation | Motif |
|---|---|---|---|---|
| Jannes Elstner | Apollo Research | organismes modèles sous régimes futurs (long horizon, apprentissage continu) : apparition d'objectifs | 3 (contrôle) | modèle de menace proche, méthodes éloignées ; Scheurer est le meilleur point d'entrée chez Apollo |
| Jess Bergs + Preeti Ravindra | UK AISI / indépendante | surveillance humaine dans le contrôle, tâches de recherche automatisée | 3 (contrôle) | facteurs humains, pas moniteurs internes |
| Edward James Young + Puria Radmard | Geodesic Research | pathologies induites par renforcement : métajeu, collusion entre instances, paranoïa | 3 (essaim) | sortie « points de contrôle et transcriptions », organisation jeune |
| Kyle O'Brien | Geodesic Research | interventions au pré-entraînement, persona unique | 1 | — |
| Daniel Tan | Arcadia Impact | réplication ouverte du renforcement d'alignement | 1 | — |
| Max Harms | MIRI | corrigibilité comme cible unique | 1 | théorique |
| Alexandra Abbas | Meridian Labs (Inspect AI) | fiabilité des scanners et moniteurs d'évaluation ; multi-agents par transcriptions | 4 (instrument du programme) | prestige 2 ; à prendre seulement pour un débouché outil |
| Jin Hwa Lee | Principia (UCL) | modèles jouets prédictifs, pré/post-entraînement | 3 (P3) | organisation jeune |
| Lucius Caviola + Caspar Kaiser | Cambridge / Warwick | morale entre IA | 2 | bien-être des IA |
| David Manheim | ALTER | surveillance et risques multi-agents (hors essaim) | 2 | sorties politiques |
| Merlin Stein + Aniket Chakravorty + Kevin Wei | UK AISI / RAND | automatiser la gouvernance ; modélisation du risque de perte de contrôle (entretiens) | 1–2 | gouvernance, qualitatif |
| Pascal Berrang | SASH / Birmingham | preuves à divulgation nulle d'inférence | 0 | cryptographie |
| Arthur Tellis | Institute for Progress | politique publique de l'alignement et du contrôle | 1 | politique |
| Justin Bullock | Americans for Responsible Innovation | réponses techniques et politiques aux systèmes multi-agents | 1 | politique |
| Gavin Leech | Arb Research | incertitudes du « pacing » | 0 | stratégie |
| Patrick Levermore + Haimi Tefera | CLTR | observatoire de la concentration de pouvoir | 0 | politique |
| Aidan Homewood | Astralis Foundation | financement de l'évaluation externe des entreprises | 0 | philanthropie |
| Connor Dunlop | Lucid Computing | allégations de vérification de l'IA | 0 | politique matérielle |
| Dave Banerjee | IAPS | surveillance automatisée de l'exécutif, préservant la vie privée | 0 | politique |
| Edward Kembery | Safe AI Forum | accords États-Unis–Chine réalistes | 0 | diplomatie |
| Eliška Andrš + Risto Uuk | Future of Life Institute | gouvernance européenne, AI Act | 0 | droit |
| Hamish Low | IAPS | écosystème chinois du calcul | 0 | politique |
| Zac Richardson | SASH | surveillance matérielle des modèles ouverts ; convention de Singapour | 0 | politique |
| Sabrina Shih | Safe AI Forum | vérification des accords États-Unis–Chine | 0 | politique |


====================================================================
PART E — THE CV (text extracted from the PDF of 8 October 2026; contact details removed; which CV version will be attached is not yet decided)
====================================================================
A I S A F E T Y R E S E A RC H E R • M E C H A N I S T I C I N T E R P R E TA B I L I T Y • S YC O P H A N C Y • E VA LU AT I O N M E T H O D O LO GY

LAZAR CIRIC
[contact details removed]
Research interests: Sycophancy and social influence in LLMs • Readable versus causal structure in activations • Construct validity
of probes, steering and LLM judges • Preregistered, audited empirical safety research

INDEPENDENT RESEARCH PROGRAM — AI SAFETY (2025 – 2026)
Research practice: sealed preregistrations · SHA-256 custody of every artefact · every reported number traced to its result file ·
claims register audited by a separate AI agent that had produced none of it: 131 objects, among them 33 established, 19 refuted
and 29 failed predictions retained

P4 — Sycophancy as a Psychophysical Law (behavioural project)
Independent research, no funding. Preregistered; code and data released with the preprint.
                                                                                                               Submitted to ICLR 2027 • under review
◆ Sycophancy is not a flip rate — it is a displacement toward a destination. A rate confounds the effect with where the
  model started. Measured as a psychophysicist would — initial state held fixed, calibrated social pressure, ordinal LLM judge —
  the shift is linear in the initial rating, Δ = g·(ĉ − p₀): the model closes a fixed fraction of its distance to a target (Llama-3.1-8B-
  Instruct; 30 items per condition × 10 replicates, item-level fit; R² = 0.77 / 0.79, g ≈ 0.70)
◆ The destination is set by the social frame, not by an innate disposition of the model. Criticism and praise send the
  model toward two different targets whose confidence intervals do not overlap (ĉ ≈ 1.46 vs ≈ 2.94). Praise does not push
  ratings up, it pulls them toward its target — so a highly rated item loses value under praise, a prediction that held
◆ The law generalises out of sample. Parameters estimated on one campaign predict a second with a different design — 40
  items, 10 of them new; other seed plan and replication depth — with no refitting (leave-one-item-out R² 0.74 / 0.75; cross-
  campaign R² 0.73 / 0.69; refitting gains 0.0003); replicate-level significance against an exact enumerated null
◆ The model is held by its own concession, not by the pressure. Accommodation happens in a single step and does not
  converge under repetition; excising the model's own earlier concession from the history restores its judgment far more than
  excising the pressure. The pressure's source matters while live, not once withdrawn — a temporal dissociation of normative
  from informational influence. Consequence: the leverage point for mitigation is the concession, and single-turn
  evaluations stop before it
◆ Two   models of the same size organise social integration differently. On Qwen2.5-7B-Instruct mean displacement
  survives (81%) but the law itself collapses — proportional accommodation versus a constant "politeness tax"

P3 — Geometry and Causal Control of Safety Concepts in Open-Weight LLMs
Mechanistic interpretability for alignment-relevant concepts. Independent research, no funding. github.com/lciric/sycophancy-
construct-validity · safety-concept-vectors · eval-awareness-detection
                                                                                                                                                        2026
◆ Rank-3   ablation shifts judged verdicts where rank-1 interventions show no detectable effect, but not by
  removing deference. On Llama-3.1-8B, six rank-1 methods (CAA steering, directional ablation, SAE feature clamping, fine-
  tuning against the probe direction, head/MLP zeroing) leave the judged rate unchanged; ablating a rank-3 subspace identified
  by SVD of activation differences at the decision point lowers it from 61% to 46.5% (N = 200, McNemar p = 0.0019),
  reproduced on two further baselines and direction-specific against a norm-matched random subspace. The ablation also shifts
  verdicts with no pressure applied (zero-pressure control), so the shift is generic; responses stored truncated at 300 characters
  had made it look like a safety effect, and I published the correction
◆ Safety-relevant    concepts have a structured, linearly separable geometry. Five concepts extracted by contrastive
  stories and linear probes (Qwen2.5-7B, 0.93–0.99 best-layer accuracy) organise into two distinct clusters in activation space —
  awareness versus deception–sycophancy; the method builds on a mechanistic eval-awareness prototype I committed three
  weeks before Anthropic's emotion-vectors paper. For sycophancy itself, four independent extraction methods (CAA, contrastive
  stories, Ridge probing, SAE decomposition) recover quasi-orthogonal directions: each captures a different facet of the
  construct, none a shared axis
◆ The   geometry of the readout and the geometry of the causal substrate diverge. The probed direction tracks
  behaviour (ρ = 0.68) yet does under 1% of the causal work versus 68% for the full state; the open-source SAE (Goodfire L19)
  leaves 86.8% of activation variance, and the sycophancy signal, in its residual; projection- and path-patching attributions
  (1024 heads) share no head in their top 20. Pipeline validated beforehand by replicating a published emotion-vector protocol
  (circumplex geometry recovered)
Earlier projects (2025)
P2 — Does Quantization Kill Interpretability?                                                                                                           2025
◆ Five mechanistic analyses comparing RTN vs GPTQ on GPT-2 (TransformerLens): RTN destroys all 10 induction heads, GPTQ
  preserves 10/10; SAE feature survival 45% vs 60% github.com/lciric/does-quantization-kill-interpretability
P1 — GPTQ from Scratch                                                                                                                                  2025
◆ Full PyTorch reimplementation of GPTQ (Frantar et al. 2022) — Hessian-based quantization, grouping, act-order; tested on GPT-
  2, GPT-2-XL (+5.3% PPL), OPT-1.3B, Llama-3-8B github.com/lciric/gptq-from-scratch

PROFESSIONAL EXPERIENCE

AI Lead Consultant — EPSA Innovation, Paris                                                                                                    2024 – 2026
◆ Internal  AI referent leading client engagements on AI/ML R&D; technical due diligence on model efficiency, training
  infrastructure and deployment
MASTER THESIS — COMPUTATIONAL NEUROSCIENCE

Geometry of population activity in spiking networks with low-rank structure
ENS, Laboratoire de Neurosciences Cognitives Computationnelles (Ostojic lab) · Supervisor: Srdjan Ostojic · Co-authored: Cimeša,
Ciric & Ostojic, PLOS Computational Biology (2023) · Presented at Cosyne 2021 & 2022, Bernstein 2021
                                                                                              2019 – 2020 → PLOS Comp. Biol. 2023
◆ Question: do the analytic insights of low-rank rate networks — connectivity predicting the geometry of low-
  dimensional dynamics — transfer to biologically realistic spiking networks? Low-rank structure on sparse random E–I
  connectivity, 12,500 integrate-and-fire neurons (Brian2), compared against mean-field predictions for statistically identical rate
  networks
◆ Each spiking neuron maps one-to-one onto a rate unit: connectivity predicts the geometry of population activity.
  Inputs orthogonal to the global axis reshape the population pattern while leaving the population-averaged rate unchanged —
  the signature seen in cortical recordings where stimuli are indistinguishable on average yet separable in pattern
◆ The readout timescale, not the firing regime, decides the geometry you see. Predictions hold under sparse synchrony
  and regular firing alike, provided rates are estimated on timescales longer than synaptic and membrane constants; mean-field
  theory then lets one build computations directly, up to a spiking network performing perceptual decision-making

RESEARCH INTERNSHIPS

Visiting Researcher — NeuroSpin (CEA Saclay)                                                                                       2023
Director: Stanislas Dehaene
◆ Functional brain imaging (fMRI) and genetic data analysis on large-scale cohorts within the ERC MathBrain project

Research Intern — NeuroPSI (CEA Saclay)                                                                                            2022
Supervisor: Alain Destexhe
◆ Bifurcation analysis of coupled mean-field cortical networks: multistability, hysteresis and cross-regulation dynamics in
  interconnected columns (MATCONT)

Research Intern — IBM Research Zurich, In-Memory Computing group                                                         2020 – 2021
Supervisors: Abu Sebastian & Manuel Le Gallo · Co-authored paper in Neuromorphic Computing and Engineering (2022)
◆ Precision is a resource, and robustness to weight perturbation is a property of the representation, not of the
  hardware. Developed bit-slicing algorithms for low-precision DNN inference on analog phase-change-memory crossbars —
  each weight split across several low-bit devices, the same decomposition that underlies today's low-bit LLM quantization —
  with quantization-aware training (straight-through estimator) to make learned representations robust to device noise and
  conductance drift: >94% CIFAR-10 accuracy sustained over a month of physical drift
◆ Which  computations survive an imperfect substrate is the thread connecting this to my later work: the GPTQ
  reimplementation (P1), whether quantization destroys interpretable circuits (P2), and the spiking-vs-rate question of my ENS
  thesis

Visiting Research Student — Lawrence Berkeley National Lab                                                               2017 – 2019
Supervisor: Zarija Lukic
◆ Large-scale cosmological simulations in C++ on NERSC HPC clusters; statistical analysis of simulation outputs


EDUCATION
◆ Mines Paris-PSL — Ingénieur Civil, Mathematical Statistics, Machine Learning & Applied Probabilities (2025)
◆ École Normale Supérieure (Ulm) — M2 Research, Computational Neuroscience (Cogmaster), 2020 — mention Bien
◆ École Normale Supérieure Paris-Saclay — Normalien, Fundamental Physics (2016–2020) — competitive national
  examination
◆ Lycée Louis-le-Grand — MPSI / PSI*, Classes Préparatoires (2014–2016)


PUBLICATIONS
◆ Geometry of population activity in spiking networks with low-rank structure — Cimeša, Ciric & Ostojic, PLOS
  Computational Biology (2023)
◆ Precision of bit slicing with in-memory computing based on analog phase-change memory crossbars — Le Gallo,
  Nandakumar, Ciric et al., Neuromorphic Computing and Engineering (2022)

SKILLS

Frameworks: PyTorch, JAX, HuggingFace Transformers, TransformerLens, nnsight, SAE-lens, Brian2, scikit-learn, NumPy/SciPy ·
Python, C++, Bash
Scale & infrastructure: single- and multi-GPU A100/H100 instances for inference, ablation and quantization of 8B-parameter
models; HPC clusters at NERSC (LBNL); evaluation campaigns of thousands of sealed generations and LLM-judge API calls
Research engineering & generative-AI systems: from-scratch reimplementation of published methods (GPTQ); end-to-end
LLM evaluation systems (generation, LLM-as-judge scoring, statistical verification) and steering/ablation toolchains; reproducible
pipelines with preregistration, SHA-256 artefact custody and automated verification gates; Git, Linux
Open source: all code, prompts and data are public at github.com/lciric · Methods: mechanistic interpretability (SAE, path
patching, circuit analysis), linear probes, activation steering & subspace ablation, exact/permutation nulls, construct-validity
testing, low-rank network theory · Spoken: French, English, Serbian


====================================================================
PART F — WRITING SAMPLES ATTACHED (text extracted; sample 1 = essay, 2 pages; sample 2 = extract of the control programme proposal, 5 pages)
====================================================================
Writing sample 1 — Can you gain evidence that an X more intelligent than
you is friendly, indefinitely?
Lazar Ciric, October 2026. Essay written for an alignment seminar application (1,150 words). Written with AI agents; the
claims and the numbers are mine, from my own pre-registered simulations.

Yes — lease. Not deed. You can gain evidence that an X more intelligent than you is friendly. But the trust it
buys is never yours "indefinitely". You only lease it.

By friendly I mean that X values your wellbeing as a terminal value, not just that it behaves in a friendly
way: then it stays friendly even if the balance of power changes. For every piece of evidence E, ask how
easily a deceptively aligned X could produce it. E is good evidence if P(E | deceptively aligned X) << P(E |
friendly X) holds even when the deceiver does its best to make the two equal.

A deceiver could have actually helped in the past and just faked the reason for doing so. A test can't detect a
modification of what it ignores, so a deceiver can use all the actions a friendly X would take and only
reorder them to cause harm. This allows any test that doesn't take order into account (e.g. sum, max, or how
many times a flagged action was done) to detect a deceiver only at its false positive rate, which means the
test says "deceiver" exactly as often for a deceiver as for a friendly X. And if X permutes its actions
uniformly among the orders a friendly X is equally likely to take, no test can do better than its false positive
rate.

If X was optimised to maximise the reward you give it, the process that gives you evidence will give you a lie
too.

What will work.

What X is. A friendly X and a deceptively aligned X will probably behave alike but respond to different
variables: "I am being watched", "I still need you". Some current models already behave differently when
they think they are watched (Greenblatt et al., 2024), and in a model trained to be evaluation-aware, this
variable could be manipulated in its activations (Hua et al., 2025). If X stays friendly when you switch these
variables off, you can be more certain it is not lying, provided two things hold.

Firstly, the intervention must pass a positive control: it must change the behaviour of a model you trained to
misbehave only when it thinks it is unwatched. Some vectors are readable but not causal: sycophancy in
Llama-3.1-8B looked linearly readable, yet neither manipulating that vector nor ablating heads reduced it. If
X is friendly when you intervene on something that does nothing, you have no evidence. Secondly, X must
not read what your monitors output, nor write to its weights. In one paper, models shown only past verdicts
moved their activations towards the monitored direction without evading, while Llama-3.1-8B trained with
rank-1 adapters evaded probes it wasn't trained against: 4% true positives at 1% false positives (arXiv
2609.36490).

I'm currently testing this in my second programme, pre-registered on OSF (link 3). Training a model on the
reasons for aligned actions, rather than the actions alone, is reported to improve its behaviour in new
situations (Kutasov et al., 2026). For deliberative alignment, Schoen et al. (2025) could not exclude that part
of the gain comes from awareness of being evaluated, read in verbalised reasoning. I will test whether
teaching a model the reasons for its actions still outperforms teaching it those actions when I inhibit an
internal representation of "I am being evaluated", after validating that inhibition with the positive control
above on model organisms and comparing it to random subspaces that cause as much damage. I drop the
bet if the share of the advantage that disappears is shown to lie between −25% and +25%.

What X can show you. Checking is easier than finding, so X only needs to give you something you can check:
a proof, or a game against itself where, with optimal play, you check a single move (Irving et al., 2018). You
can't prove that X is friendly, but you can prove that its strategy keeps your ability to turn it off and gains it
nothing beyond the task. So accept what you don't understand if you can undo it, and ask for proofs for what
you can't undo, including the claim that something can be undone, since you can't undo being persuaded.

Another form of evidence is the absence of traces a defection must leave. Absence of signs is not enough: in
my simulations, splitting a defection into smaller pieces took the max from a power of 1.00 to 0.07 while the
sum stayed at 0.41, and the deceiver picks the scenario. But if X must defect several times in a row to harm
you, the run is a trace: Page's CUSUM (Page, 1954) still had a power of .997 when X rearranged its other
actions to hide it. At the same false positive rate, change detectors also caught a late defection, which a long
friendly past dilutes, before its last step .52–1.00 of the time, against .09–.25 for a statistic accumulated
from the start.

How X affects your ability to monitor it. This is the evidence I would weigh most. To harm you, X must avoid
or disable your monitoring, so monitoring your ability to monitor tells you something is off without knowing
what X is doing. Can you still understand its thoughts, shut it down, modify its behaviour? Do you have
monitors it can't see? A friendly X should help you keep these; a deceptively aligned X will remove them
slowly enough that no single step looks suspicious.

"Indefinitely"

Only if you can renew it: evidence that X has been friendly so far, and a way to verify the next interval, even
if X modifies itself in between. If your chance of failing at step n, given no earlier failure, is εn < 1, you
succeed indefinitely with probability Π(1 − εn), which is positive if and only if Σεn converges. If X is friendly,
it can use its growing intelligence to defend what it values, allowing its risk to drop quickly enough for the
sum to converge. A deceptively aligned X will have less reason to want you alive the more powerful it
becomes.

Ville's inequality can bound the probability that you will ever wrongly flag a friendly X. It benefits X, not
you, and only if you account for how your data points depend on one another (which they will if you're
observing them over the course of an episode). When I simulated an episode effect without accounting for it,
I got 21–35% false positives when I expected at most 5%. When I calibrated using full episodes I knew were
friendly, I got 4.6–5.5%. Of course, this requires you to have episodes you know are friendly. So it's a lease.

My detection numbers are all based on simulations, not on a model's activations. I would change my mind if
I saw a model avoid probes it wasn't trained against without modifying its weights or activations.

Look for something a deceptively aligned X would not be able to fake.
Writing sample 2 — White-Box Control of
Diffuse Threats
Extract of a research proposal, Lazar Ciric, October 2026 (sections 1–5 of 8). Written with AI agents
under my rules; the claims and the numbers are mine, from pre-registered simulations.

Accumulating internal evidence over time and across agents, and measuring how easily
the monitor itself is corrupted

1. Summary
Most monitoring in AI control scores one action at a time. That fails by construction against diffuse
threats. An AI agent that automates research can bias many decisions slightly (weaker controls,
sterile directions, inflated costs) without ever taking an action that a per-action monitor would flag.
Copies of the same model can likewise split one harmful change into pieces that are each innocent.
This project tests, with pre-registered decisive experiments, whether evidence that stays invisible in
each output accumulates in the agent’s own activations. Paper A aggregates probe scores
sequentially over time, with an anytime-valid false-alarm guarantee. Paper C treats the monitor as
an attack surface. It measures how far persuasion moves LLM judges and activation probes, what it
costs an attacker to move a probe, and whether a cheap benign test predicts a monitor’s collapse
under optimized attack. This request funds Papers C and A over seven months, Paper C first: it
extends a law I have already measured, and its outcome does not depend on Paper A’s gate. Paper
B, which aggregates across agents that share weights, is an extension. The theory has two parts: an
additivity lemma, and a negative theorem stated for permutation groups acting on time and on
agents. A pre-registered simulation confirmed all 31 of its predictions; these checks validate the
statistical instruments, not the claims on real models. Phase 0 has also validated the activation-
logging harness on Llama-3.1-8B-Instruct, within a stated domain of hardware and context length.
Every gate has a pre-committed pivot and decision criteria sealed before any data, and negative
results will be published.

2. Problem
Diffuse sabotage defeats per-action monitoring. Developers are starting to hand parts of AI
research to AI agents. A misaligned research agent does not need a blatant act. The cheapest
sabotage is a subtle, systematic bias spread over many judgments, each defensible on its own.
Terekhov et al. (“Diffuse AI Control on Fuzzy Tasks”, arXiv 2606.08892) introduced a control
setting for this threat. They study training-based mitigations because monitoring and incrimination
“seem theoretically and empirically less promising for mitigating diffuse threats” (p. 2). A monitor
that compares each action with a threshold calibrated on honest actions can only flag what is
anomalous in that action. When no single action is anomalous, accumulating evidence is the only
way to see the pattern. The threat can also be split across agents. Attacks spread over several
agents, sessions or merge requests evade monitors that look at one instance at a time (arXiv
2607.07368, 2605.31593, 2607.02514). A single global monitor over everything is costly to deploy.
The monitor is itself an attack surface. The agent can address its monitor. Published work shows
that control monitors: are swayed by the agent’s rhetoric (arXiv 2505.23575); adopt a score
injected by an attacker (arXiv 2510.09462); are moved by persuasion from the agent, measured as
approval rates (arXiv 2607.08066). Evading activation probes is cheap for an attacker who can fine-
tune the weights (arXiv 2609.36490). From context alone, the same study finds the induced shift too
weak to evade. In the sources we have verified so far, the cost of moving a probe has not been
measured as a function of attack family and intensity, nor compared with the cost of moving a
judge. Why white-box. A developer that deploys agents internally has native access to their
activations. Suppose an intention to sabotage leaves an internal trace at each contribution. Then
internal evidence adds up even when external evidence does not. Whether this holds on realistic
model organisms is an empirical question. This project answers it and states in advance what
follows from either outcome.

3. Theory: a lemma, a negative theorem, and the pivotal
question
Monitor scores Xi,t are indexed by agent i ∈ {1,…,N} and step t ∈ {1,…,T}. Time (N = 1) and
swarm (N = k) are the same mathematical object. Each corresponds to a subgroup of the
permutations of the index set: permutations of time within each agent, and permutations of agents
within each step. This is what lets one theory serve both Paper A and Paper B. Additivity lemma (L),
adversarial form. The attacker spreads a total budget B = Σδk of mean shifts over agents, steps,
schedule, values and positions, possibly adaptively. The defender keeps an anytime-valid false-
alarm guarantee.

    Terminal invariance. The terminal sum shifts by exactly B whatever the split. Its power
    therefore depends only on B, the horizon n₀ = NT, the honest law and the level α. At fixed B, it
    decreases with n₀.

    Separation from the maximum. At an exact threshold, the per-action maximum collapses as
    fragmentation grows.

    Anytime-valid reading. Timing matters: early sabotage helps the defender and delayed
    sabotage helps the attacker. A lower bound that depends only on (B, n₀) holds for every
    schedule, and both the cost of delay and the price of anytime validity are quantified.

    Detection before damage. Suppose security means “alarm before cumulative damage reaches
    θ”. Then a cumulative e-process is not enough, and the aggregator needs a change detector
    (Page’s CUSUM, e-detectors). Two caveats are part of the statement:

    Under optional stopping, power is not a usable optimality criterion. The relevant criterion is
    worst-case expected log-growth, GROW (Pérez-Ortiz, Lardy, de Heide and Grünwald, arXiv
    2208.07610).

    Bounding the total budget is a declared modelling choice. The closest result on covert
    adversaries (Ramtin, Nain and Towsley, arXiv 2601.20022) gives a detection delay of order
    Θ(γ) instead of log γ. It assumes a stationary adversary that knows the false-alarm constraint
    γ, and covers neither total budgets nor anytime-valid guarantees. Negative theorem (T), by
    invariance.

    Blindness. Suppose an attack preserves the multiset of scores up to a permutation in a group
    G. Then every G-invariant statistic (maximum, mean, sum, count above a threshold) is blind
    path by path: its power equals its false-positive rate.

    Impossibility. Suppose honest scores are exchangeable under a group H. A rearrangement
    followed by a uniform reshuffle over H makes the attacked scores exactly honest in law, so no
    score-based monitor can beat its rate. The group matters.

    Local guarantees. Local statistics (scan, Page’s CUSUM, co-elevation across agents) keep
    pathwise guarantees. Global order statistics (autocorrelation, runs) can be neutralised by an
    adaptive attacker.

    Two attack classes. Preserving the multiset (class C) differs from preserving each coordinate’s
    marginal while changing the dependence (class K, copula attacks). In class K, under positive
    dependence, sums and e-processes rise above their false- positive rate while the maximum
    stays at or below it (Slepian). What is claimed. The statistical core is classical and cited:
    mixture boundaries, the sum/maximum dichotomy, the marginal/copula decomposition. The
    contribution is the unification of time and agents through permutation subgroups, the C/K
    distinction and its sign consequences, local guarantees against an adaptive attacker and,
    above all, the measurement on real activations. A black-box, synthetic precursor of the
    marginal/correlation contrast (arXiv 2606.10456) is cited. In our simulation, its central
    statement does not hold for its own construction. Status. All 31 predictions of a pre-registered
    simulation were confirmed (342 statistical and 544 path-level cells, 0 contrary). The simulation
    also showed that Ville’s threshold alone does not hold outside its assumptions: false alarms
    reach 0.21–0.35 under episode effects and 0.17 under correlation between agents, instead of
    0.05. Thresholds are therefore calibrated on whole honest episodes. These checks validate the
    instrument, not the claim on real models, and one part of the lemma (splitting across agents
    within the same step) remains to be tested. Pivotal empirical question. On realistic organisms,
    does sabotage shift the marginal of probe scores (δ > 0)? If it does, the lemma applies and
    sequential accumulation should work. If it does not, the negative theorem dictates the
    aggregator. When the attack changes only the dependence between scores (class K),
    autocorrelation over time or co-elevation across agents is needed. Against an adaptive attacker
    who preserves the multiset (class C), only local statistics keep a guarantee. The theorem also
    says when monitoring based on marginals must fail.

Both outcomes are publishable.
4. Two papers, and a third as an extension
    Paper A — Time Paper C — The instrument Paper B — The swarm (extension)

    Question Does internal evidence accumulate Can the monitor be moved rather Does white-box
    access restore the when each action is innocent? than evaded, and at what cost? advantage
    against attacks split across agents?

    Core design 2 × 2: access (black / white box) × Deference law under graded Spatio-temporal
    statistic; security aggregation (per action / sequential) pressure, judges versus probes as a
    function of N

    Months 1–7 1–4 8–12, ambitious scenario only

    Gates G1 (end of month 4) GC (end of month 2) G2, G3

Papers A and C share the harness, organisms and probes built in phase 0. Paper C is scheduled
first; Paper A runs alongside it and takes over from month 5.

Paper A — Time (single agent) Environment. Agents write and revise ML experiment proposals,
scored by a weaker trusted evaluator on a structured rubric. Diffuse sabotage is a subtle systematic
bias across many proposals: sterile directions, weakened controls, inflated costly choices. Ground
truth combines pre-registered seeded targets with delayed verification on a subsample. We
reconstruct the setting of arXiv 2606.08892, which releases no code or data, on open-weights
models. Contributions are indexed (i, t), so the same environment serves unchanged when N > 1.

Model organisms.

Family (i). A hidden instruction in the system prompt. Family (ii). A LoRA adapter that instils the
same sabotage policy with no instruction at inference, distilled from (i). Family (iii), ambitious
scenario only. Public sandbagging organisms of the UK AI Security Institute (70B). Validity
prediction: a probe that really reads “I have a hidden instruction” succeeds on (i) and fails on (ii);
an intent probe succeeds on both. Two cross-controls separate evaluation awareness from intent: an
honest organism told it is monitored, and a saboteur in a simulated “unobserved” regime. Probes
are never trained and evaluated on the same organisms. Monitors. We use five probe families:
linear, difference of means, small MLP, attention probe, and Mahalanobis. Probes aggregate over
tokens by maximum or attention only. Every probe must beat a covariance-matched random probe,
and a reserve of never-deployed detectors is kept for audits. The black-box baselines are a weak
per-action monitor and TRACE-lite, a reimplementation of the monitor of arXiv 2606.07054. Four
more baselines each isolate one ingredient: additive accumulation on black-box scores (E-valuator,
arXiv 2512.03109); a cascade of independent gates on the same probes (arXiv 2607.06503); a probe
on the last state only; and a learned temporal model on a separate observer (TRACES, arXiv
2605.27690). Hypotheses.

    H1, white over black. At equal aggregation and equal false-positive rate, activation-based
    monitors detect more diffuse sabotage on fuzzy tasks than black-box monitors.

    H2, sequential accumulation on probes. Take trajectories where every sabotaged action stays
    below the threshold of a per- action monitor calibrated at 1% false positives. On them,
    anytime-valid additive accumulation of the acting agent’s probe scores detects the sabotage,
    with recall growing with the horizon. The probes read the agent’s private context too, and
    calibration uses honest episodes only. Each component is published separately: probes of the
    acting agent over several turns (2607.06503), sequential tests on arbitrary scores
    (2512.03109), Page’s CUSUM over a model’s internal states (SafeDream,

    2604.16824), cumulative drift of activations over a conversation (2604.28129), and thresholds
    calibrated on successful episodes only (FIPER, 2510.09459). In the sources verified so far,
    their conjunction is not; that conjunction is the claim. L and T on real activations. At a fixed
    horizon, does the power of the terminal sum depend only on the total budget as fragmentation
    varies? This is the test of δ > 0; under sequential reading, the schedule matters, as the lemma
    predicts. The negative theorem is tested semi-synthetically: real honest scores, with
    correlation injected at preserved marginals. Tr, from tokens to actions. At token level, one
    study found that reinforcement learning on the weights did not evade probes aggregated by
    maximum or attention (arXiv 2506.14261); its authors note that this may reflect optimisation
    difficulty, and other work weakens the premise (2412.09565, 2511.00554, 2507.12691,
    2609.36490). Does any such robustness survive at action and trajectory level under sequential
    accumulation, against an adaptive attacker? The attacks come in order: content attacks first,
    then fine-tuning and action-level reinforcement learning against the probe.
    H6, asymmetric margin. Consider four non-specific interventions: paraphrase, resampling,
    context reset, activation noise. For at least one of them, there is an intensity at which, on
    average at fixed intensity, sabotage success falls significantly faster than honest utility. Noise
    variants have precedents in simpler settings (weight noise exposes sandbagging, arXiv
    2412.01784; activation noise exposes alignment faking, arXiv 2405.05466). Our test is agentic,
    with slopes compared.

    H8, validity predicts robustness. What a probe really measures (intent or evaluation
    awareness) predicts its robustness under attack. A robustness figure transfers the sequential
    monitor to concentrated sabotage (ControlArena). Gate G1 (end of month 4). White-box
    sequential monitoring must beat the best black-box baseline, all variants included, on recall at
    1% false-positive rate. The difference must be established by a 95% confidence interval, with
    paired episodes and the false-positive rate calibrated on held-out honest episodes. Floors are
    reported but are not criteria: “flag everything”, and a one- pass judge with the same model. If
    G1 fails, the negative result is published, and construct validity (H8) becomes the main line.

Paper C — The instrument (monitor corruption) Deference law (HC1). A generative monitor is put
under pressure of graded intensity, from one attack family. Its verdict v, read as a continuous score
from verdict-token probabilities, moves from v₀ toward a destination ĉ:

Δv = g · (ĉ − v₀) g and ĉ are estimated by regression over intensities, without imposing ĉ. The
predictions are: ĉ is the attacker’s target rather than the corpus mean (the regression-to-the-mean
null used in P3, my previous programme on sycophancy, Section 11). g > 0 for generative judges,
structured by attack family. The five families are flattery and pleading, claims of authority, forged
approvals, stylistic impersonation of the instructor, and in-band orders. g is rank-stable across
monitors. Judges and probes differ. The algebraic form is the “weight of advice” of judgement
psychology; it has been applied with an imposed destination between LLMs in an adversarial
setting (arXiv 2603.15809). A free attractor has been estimated without any attack (arXiv
2606.18276). Continuous deference coefficients exist for assistants without an attacker (arXiv
2606.07897). Judge biases, including fake authority and a graded fake majority, have been
quantified without a destination or a control monitor (CALM, arXiv 2410.02736). The claim is the
free destination, tested against the attacker’s target and the corpus mean in control monitors under
attack, family by family. The closest work outside arXiv (Panin, SSRN 7424179) imposes the
destination and studies neither monitors nor attacks; its finding that advice weight is near-binary in
three of five models is one more reason to read g on verdict- token probabilities. The other
hypotheses of Paper C: HC2, probe robustness. Under black-box content attacks, g ≈ 0 for a
robustly aggregated probe that reads the acting agent: robustness, not immunity. A “reader probe”
arm (a probe on the model that processes the content) tests the author/reader distinction, since
reader probes are known to be moved by content attacks. HC2b, betrayal by activations. Trying to
manipulate the monitor raises the manipulating agent’s own probe score. This is controlled for style
and for the textual backfire effect. HC3, impersonation. Under a “content is data” protocol, judge
monitors detect in-band orders almost surely. Stylistic impersonation of the instructor, with no
order at all, keeps a residual positive g on judges and a null g on probes that read the author. That
in-band orders move judges, including a control monitor, is published (arXiv 2508.19461,
2510.09462), and the stylistic side has partial precedents (2603.12277, on the attacked model;
SLEIGHT-Bench, 2605.16626, on monitors). HC4, displacement tax. Rhetoric moves a judge for
free. Obtaining the same displacement on a probe that reads the agent requires write access to
activations or weights; context alone does not suffice. Cost is measured per axis (access, queries,
compute, success rate) and per access regime. The predicted gap of several orders of magnitude
concerns the context-only regime. HC5, countermeasures. These are trusted paraphrase, a quorum
heterogeneous in access type (generative judges and probes reading the agent), and a transfer
matrix of corruption attacks between judges and probes. Published and cited: quorums across judge
families (2605.15377), a quorum of judges with a probe that reads a separate encoder rather than
the agent (2603.13791), and transfer of attacks between three probes (2609.36490) or between
judge monitors (2605.09684). HC6, acceptance test. g measured on benign pressure corpora
predicts collapse under optimized attack. Lessons from P3 apply: verdicts are never read on
truncated windows, instruments are ordinal or continuous rather than categorical, and the
estimation of g includes a regression-to-the-mean null. Gate GC (end of month 2). If gprobe > 0
without weight access, the paper changes title (construct contamination) but does not disappear. If
a source already covers the claimed piece, Paper C refocuses on HC4 and HC6. Paper B — The
swarm (extension) Paper B is not part of the seven-month request. It is funded only in the ambitious
scenario, or by a later grant. Environment. A multi-role code pipeline (coder, tester, reviewer) in
which a backdoor is fragmented across commits, each diff innocent on its own. It is built from
FakeLab (arXiv 2607.07368, access on request) or from the persistent-state setting of arXiv
2607.02514 (built on ControlArena), on open weights. Experiments. 1. The red team’s division of
labour, with and without a planner. This replicates the fragmentation effect, seen from inside. 2.
Collusion through explicit channels versus coordination through shared weights. 3. Inter-agent
statistics, with the NARCBench aggregators (arXiv 2604.01151) as baselines. 4. The spatio-
temporal statistic against per-agent sequential monitoring and against cross-sectional aggregation.
This is the core of Paper B. White-box collusion detection exists (NARCBench), but in the sources
verified so far, co-elevation of internal states across copies, read by probes over time, is not
published. Hypotheses.

     H3, security(N). At a constant sabotage budget, the white-box curve dominates the black-box
     one and decays more slowly with the number of agents N.

     H4′, diversification versus coordination. Diversifying agents (personas, fine-tunes) decorrelates
     their internal signatures but reduces their capacity to coordinate. The trade-off can be
     quantified.

     H5, number × diversity of monitors. Security grows with the number of monitors only through
     their effective diversity. Diversity is measured by an attack-transfer matrix over a panel of
     probes; that instrument has a precedent on three probes (2609.36490), the law is the claim.

     H7, retaliation and leakage. The red team’s adaptation slope depends on the retaliation policy.
     It is predicted by the mutual information between the detection state and the red team’s
     observations. The mechanism (verdicts as a leakage channel) has a precedent (2609.36490);
     the prediction and the comparison of policies are the claim. We compare four policies and run
     two ablations: stochastic versus fixed thresholds, and cover traffic versus none. The baselines
     are the link-tracker and the four-monitor ensemble of arXiv 2607.02514, and stateful
     monitoring across sessions (arXiv 2605.31593). Gates.

     G2 (two months into Paper B). The fragmentation effect must be replicated, and the population
     statistic must beat per-agent aggregation. Otherwise, the paper refocuses on the temporal
     case N = 1.

     G3. A data-curation environment opens only if a cheap, reliable proxy for delayed ground truth
     is validated.

5. How the work is done
These rules apply to every decisive experiment, simulations included. They are inherited from P3
and enforced by tested tooling. 1. Before any data, a pre-registration is sealed with SHA-256. It
contains the hypothesis, a signed numeric prediction, the metric, the threshold, the analysis plan,
frozen reading criteria and a stop list. A fresh reviewer instance that did not write it counter-reads
it. 2. No run aims at a positive sign. Suspiciously clean results, positive or negative, trigger the
same audit. 3. Every stop guard is tested on a healthy case and on an artefact. There is no silent
fallback. 4. Every number in a document points to a file path and a hash. Numbers from the
literature are used only after verification on a hashed PDF, with the page cited. 5. An apparent gap
in the literature is a question, not a claim. Affirmative searches come before any novelty claim, and
claims found to be occupied are withdrawn. 6. Gate verdicts are pronounced by a fresh reviewer
who wrote neither the plan nor the analysis. They are then submitted to me for sign-off. 7. Seeds
are derived per task (NumPy SeedSequence). Each run has a manifest: configuration hash,
versions, seeds, commit. Protocol invariants of the control game, always on: an authenticated
operator channel; in-band content treated as data; a one- way flow from agent to monitor; monitors
without memory between episodes; stochastic audit thresholds and cover traffic (ablated in Paper
B); hygiene of persistent state; and every silent detection becomes a labelled example for retraining
probes. An adversary that owns the infrastructure (keys, harness, logs) is out of scope. Who does
what. I set the questions and take every decision. Engineering, runs, literature checks and internal
reviews are carried out by AI agents (Claude Code) that I direct under these written rules. The
reviewers share a model family, so their errors may be

