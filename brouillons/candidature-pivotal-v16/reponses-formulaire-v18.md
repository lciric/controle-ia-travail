# Pivotal Research Fellowship 2027 Q1 — main form, FINAL answers — v18
2 November 2026. v18 = v17 with two passages of the career memo (§ 10) replaced by Lazar's own wording (his message of 09:42 Paris): the sentence on AI coding agents, and the opening of « Things I have made » (heading included). Corrections of substance only: « Agents » → « A system of research agents » (the agents are the providers' models; what Lazar made is the system that stops them judging their own work); spelling « there » → « their ». § 9 names the memo PDF v6. Everything else is identical to v17, word for word.

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

## 7. (Optional) A missing risk (≤ 150 words)

Corruption of the overseers. The list treats the monitored system as the risk; the oversight layer is itself an attack surface. Monitors, human or model, can be moved by deference (the monitor adopts the position of the system it watches, the mechanism I measured as sycophancy), by impersonation of the instructor, or by collusion between instances meant to check each other. None of this requires a scheming model: a mildly sycophantic monitor degrades oversight on its own.

I would rank it between scheming and gradual disempowerment, as an amplifier of both. It matters because every control proposal, including those that use untrusted models to monitor each other, assumes the monitor's judgment survives contact with the monitored system. That assumption is testable now on open-weight models and is rarely measured as a quantity; the sycophancy law is one quantitative handle on it.

## 8. Referees (optional)

| | Name | Email | Relationship (to paste) |
|---|---|---|---|
| 1 | Srdjan Ostojic, ENS | [your entry: his email] | Supervisor of my master's thesis at ENS (Ostojic lab, 2019–2020) and co-author of our PLOS Computational Biology 2023 paper on low-rank spiking networks. |
| 2 | Manuel Le Gallo, IBM Research Zurich | [your entry: his email] | Supervisor of my research internship at IBM Research Zurich (2020–2021) and co-author of our 2022 paper in Neuromorphic Computing and Engineering. |

## 9. Attachments

- CV: `Lazar_Ciric_CV_2026-11-02_v15_universel.pdf` (the universal CV; three mentor-family variants in the same folder if a mentor form takes a file). The manuscript repository github.com/lciric/sycophancy-psychophysical-law is public and its check passes.
- Writing samples: `Lazar_Ciric_writing_samples_v3.pdf` — essay (2 pages) + extract of the control proposal (5 pages); 7 pages total is within "≤ 5 pages per sample, one PDF".
- Career memo (optional): `Lazar_Ciric_career_memo_2026-11-02_v6.pdf` (one page, the text of § 10).

## 10. Career memo (optional; one page)

Career memo, Lazar Ciric, 2 November 2026

About me. I studied physics (ENS Paris-Saclay) and went into computational neuroscience (ENS, Ostojic lab; published in PLOS Comp Bio 2023). Then IBM Research Zurich doing analog in-memory computing (published in Neuromorphic Computing and Engineering 2022). And statistics/machine learning at Mines Paris-PSL. I've been doing independent research on AI safety for the past two years and have been full time since March 2026. I use AI coding agents as long as every preregistration is sealed before running and I can point to a file for every number. If I predict something wrong it will show on my record.

Things I have made. A system of research agents that can't judge their own work (github.com/lciric/ideation-organism; has 929 tests and can find 224/224 mutations to its code). I tried to cheat the statistical evaluator with 27 different types of cheats and found 4 that worked and fixed them (preregistered and validated with 1000 runs). When run over 288 real model episodes it identified the 3 true associations I seeded (the weakest on a lucky draw) and none of the 19 false ones, and promoted no actual law (read only once and was preregistered). Found a behavioural law about sycophancy (paper in progress; code and data public). This law from campaign 1 can predict campaign 2 without refitting (R² 0.73 / 0.69 out of sample). Found that the orientation of a sycophancy probe explains less than 1% of the causal impact. Working on AI control: proved that there are things you can't detect with per-action scores, ran preregistered simulations and began testing on Llama-3.1-8B. Can't detect a saboteur that increases costs with generic probes (null with upper bound). Can detect 27% of the saboteur's actions with 1% false positives when using the best per action black box monitor, if the saboteur gets a weaker instruction (with one caveat regarding the controls). Currently starting: comparing white box vs black box methods on the 2400 actions from the previous test (preregistered analysis), getting an LLM to generate ideas that will pass my evaluation metric by gaming it (preregistration drafted and public, currently trying to find holes in it) and completing the loop with actual tests, run in a sandbox, that can kill an idea (code public).

What I hope to get out of the fellowship. Produce one solid result in 15 weeks that is preregistered and made public as a preprint with code and data. Have a mentor that will challenge my work. All of my work falls along a spectrum of understanding how properties of interest to safety appear in activations. Whether they persist after training or are shared between agents. And how we can monitor for these.

In the future. I would like to work full time in AI control/evals/interpretability. Or do a PhD based around these topics.

Logistical. I live in Paris and can be in London full time from the 18th of Jan 2027. Have not done a fellowship before. Currently a finalist in the Anthropic Fellows Program selection process.
