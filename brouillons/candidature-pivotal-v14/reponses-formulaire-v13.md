# Pivotal Research Fellowship 2027 Q1 — main form, FINAL answers — v13
2 November 2026. v13 = v12 with: "preregistered" removed from the sycophancy law (no dated prediction shown in the public repository; Lazar, R-1086); the exact wording "out-of-sample R² 0.73 / 0.69 (campaign-1 law applied to a second campaign without refitting)"; the manuscript title capitalised as Lazar gave it; the optional "missing risk" answer kept (R-1086); the career memo's counts updated and the control simulation described with its nature (most of its 31 predictions were instrument checks).

History: 1 November 2026, ≈ 21:30 UTC. v11 aligned with the published repository github.com/lciric/sycophancy-psychophysical-law (verified: SHA256SUMS OK, `reproduce.py --check` passed): out-of-sample R² is 0.73 (criticism) / 0.69 (praise) without refitting; the nulls are permutation nulls. v11 = v10 with §2 trimmed to the 150-word limit (two edits, no change of content). v10 = v9 plus the paper instance's audit (voie B): the sycophancy manuscript is 'in preparation'; code and data go public under github.com/lciric/sycophancy-psychophysical-law (every figure reproducible by one command); the manuscript's real title is 'Sycophancy as Attraction Toward a Fixed Point'; the Qwen comparison is withdrawn (data not in the public lot); campaign 2 had 5 generations per item, R² 0.73 / 0.70.

## 1. Three most relevant experiences (≤ 10 words each)

- Public automated-research system designed so no agent grades itself
- Sycophancy law, Llama-3.1-8B, out-of-sample R² 0.73/0.69 (code, data public)
- Probe-read sycophancy direction carries under 1% of causal effect (Llama-3.1-8B)

## 2. One project you recently completed and are proud of (≤ 150 words)

"Sycophancy as Attraction Toward a Fixed Point" (manuscript in preparation; code and data public). Alone: questions, design, analysis and paper are mine; engineering was done with AI coding agents under written rules.

Finding: in Llama-3.1-8B-Instruct, sycophancy is a displacement, not a flip rate. Under calibrated social pressure the shift is linear in the initial rating: the model closes about 0.7 of its distance to a target set by the social frame. Criticism and praise set different targets, so praise can lower a highly rated item (a prediction that held).

Difficulty: flip rates confound effect and starting point, and single-turn evaluations miss the mechanism. A psychophysics-style design and permutation nulls separated them; removing the model's own concession restored its judgment more than removing the pressure.

Outcome: the campaign-1 law predicted a differently designed second campaign without refitting (out-of-sample R² 0.73/0.69), and identified concession dynamics as the mitigation target.

## 3. Career plan (≤ 200 words)

I am an independent AI-safety researcher working between interpretability and evaluation, after training in physics, computational neuroscience and statistics. Since October I have built a public automated-research system in which no agent grades its own work, and focused on white-box control of threats spread across many actions or agents, where no single action looks wrong.

My goal is a research scientist or research engineer role in an AI-control, evaluations or interpretability team, or a PhD centred on the same questions. I want to establish when internal-state monitors add detection power beyond black-box monitoring, and how to evaluate them against adaptive attackers without overstating what a probe measures.

Pivotal would give me the sustained mentorship, collaborators and feedback I currently lack. Over fifteen weeks I would narrow this programme to one mentor-aligned question, preregister the decisive comparisons, and aim for a public preprint with code and data. The fellowship would also test whether my independent practice transfers to a team.

This matters because an agent can cause harm through a sequence of individually innocuous actions, where per-action monitoring provides little evidence. A reliable answer would help developers choose monitoring strategies, and recognise when they cannot work.

## 4. Two sources (≤ 100 words)

1. Greenblatt, Shlegeris, Sachan and Roger, "AI Control: Improving Safety Despite Intentional Subversion" (2023). It turned "what if the model is adversarial" from a philosophical worry into a measurable game with a budget, which is the frame of my control work.

2. Bailey et al., "Obfuscated Activations Bypass LLM Latent-Space Defenses" (2024). It showed that probes and latent-space monitors are attackable at low cost to task performance; it convinced me that monitor robustness has to be measured against an adaptive attacker, not assumed from a probe's accuracy.

## 5. Ranking (top = highest priority)

1. Loss of control
2. AI scheming
3. Gradual disempowerment
4. Concentration of power
5. AI misuse
6. Large-scale job loss
7. Environmental harms

## 6. Reasoning (≤ 150 words)

I rank by irreversibility, potential scale, and whether current measurements could fail silently.

Loss of control ranks first because it could foreclose later correction. Scheming ranks second as one important pathway to it, and because deception makes behavioural evidence hard to interpret. My own work is on a related measurement problem: whether monitoring can detect harmful behaviour spread across many actions or agents, where no single action looks wrong.

Gradual disempowerment and concentration of power follow: they can entrench themselves and weaken society's ability to respond, although their slower course leaves room for institutions. Misuse can cause severe near-term harm, but existing security, evaluation and deployment practice addresses part of it.

I rank large-scale job loss and environmental harms lower as research priorities, not as unimportant: both could be serious, but their causal pathways are more observable and other research communities are better placed to address them.

## 7. (Optional) A missing risk (≤ 150 words) — kept (your go of 1 November, 23:50)

Corruption of the overseers. The list treats the monitored system as the risk; the oversight layer is itself an attack surface. Monitors, human or model, can be moved by deference (the monitor adopts the position of the system it watches, the mechanism I measured as sycophancy), by impersonation of the instructor, or by collusion between instances meant to check each other. None of this requires a scheming model: a mildly sycophantic monitor degrades oversight on its own.

I would rank it between scheming and gradual disempowerment, as an amplifier of both. It matters because every control proposal, including those that use untrusted models to monitor each other, assumes the monitor's judgment survives contact with the monitored system. That assumption is testable now on open-weight models and is rarely measured as a quantity; the sycophancy law is one quantitative handle on it.

## 8. Referees (optional)

| | Name | Email | Relationship (to paste) |
|---|---|---|---|
| 1 | Srdjan Ostojic, ENS | [to fill] | Supervisor of my master's thesis at ENS (Ostojic lab, 2019–2020) and co-author of our PLOS Computational Biology 2023 paper on low-rank spiking networks. |
| 2 | Manuel Le Gallo, IBM Research Zurich | [to fill] | Supervisor of my research internship at IBM Research Zurich (2020–2021) and co-author of our 2022 paper in Neuromorphic Computing and Engineering. |

DECISION FOR LAZAR: Argon and Kimi both note that neither referee can speak to the last two years; both suggest Charbel-Raphaël Segerie (CeSIA) in place of one of them **only if he has genuinely examined your recent work** and agrees to be named. Your call.

## 9. Attachments

- CV: `Lazar_Ciric_CV_2026-11-02_v13_universel.pdf` (the universal CV; three mentor-family variants in the same folder if a mentor form takes a file). The manuscript repository github.com/lciric/sycophancy-psychophysical-law is public and its check passes.
- Writing samples: `Lazar_Ciric_writing_samples_v3.pdf` — essay (2 pages) + extract of the control proposal (5 pages), the dangling final sentence removed and funder-specific wording edited out; 7 pages total is within "≤ 5 pages per sample, one PDF". DECISION FOR LAZAR: Kimi recommends a 5-page extract of the sycophancy manuscript instead of the control proposal (completed research rather than a prospective programme). If you want that, send me the manuscript PDF.

## 10. Career memo (optional; ≈ 250 words; paste into a one-page PDF)

Career memo, Lazar Ciric, 2 November 2026

Who I am. Physicist by training (ENS Paris-Saclay), then computational neuroscience (ENS, Ostojic lab; PLOS Computational Biology 2023), IBM Research Zurich (Neuromorphic Computing and Engineering 2022), Mines Paris-PSL (statistics and machine learning). Independent AI safety research for two years, full time since March 2026, with AI coding agents under written rules: sealed preregistrations, every number traced to its file, failed predictions kept on record.

What I have. A public automated-research system in which no agent grades its own homework (github.com/lciric/ideation-organism; 929 tests, 224 of 224 code mutations caught); I attacked its statistical judge with 27 scripted cheaters, found four that got through, and closed them, with a preregistered validation at 1,000 repetitions. A behavioural law of sycophancy (manuscript in preparation; code and data public): the campaign-1 law predicts a second campaign without refitting (out-of-sample R² 0.73 / 0.69). A mechanistic result: the direction a probe reads carries under 1% of the causal effect. An AI-control programme: a negative theorem on what score-based monitors can detect, preregistered simulations, and a first test on real activations whose null result is bounded.

What I want from the fellowship. One measured result in fifteen weeks, preregistered, released as a preprint with code and data, with a mentor who pushes back. My projects sit on one axis: how safety-relevant dispositions (sycophancy, deference, covert sabotage) show up in activations, survive training or spread across agents, and how monitors can audit them without being gamed.

After. A full-time research role in AI control, evaluations or interpretability, or a PhD anchored in this work.

Practical. Based in Paris; available in London full time from 18 January 2027. First-time fellow.
