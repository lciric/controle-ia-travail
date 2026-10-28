# Formulaire EA Funds, réponses préparées le 7 octobre 2026

Texte préparé pour le formulaire du Transformative AI Fund (version du 7 octobre 2026, 11:15 UTC). Le texte collé dans le formulaire peut différer légèrement ; les libellés des champs sont reconstitués.

## Short description

7-month stipend and compute to test whether AI monitors can be persuaded and whether probes catch diffuse sabotage

## Project summary

AI developers increasingly rely on AI monitors (an LLM judge, or a probe reading an agent's activations) to flag dangerous actions by AI agents. I test two ways this can fail. First, the agent can persuade its monitor. My earlier work showed that social pressure moves Llama-3.1-8B's judgments a fixed fraction of the way toward a target the pressure sets; parameters fitted on one campaign predicted a second. Paper C measures this law in control monitors under five kinds of attack, compares LLM judges with probes, and tests whether a cheap pre-deployment check predicts which monitors collapse under optimized attack. Second, an agent doing AI research can sabotage diffusely: many slightly biased choices, none suspicious alone. Paper A tests whether that evidence accumulates in the agent's activations, using sequential tests with a guaranteed false-alarm rate. Criteria are pre-registered; negative results will be published. I request $58,630 for seven months; $28,160 funds Paper C alone.

## Track record

Background: physics at ENS Paris-Saclay (normalien, 2016–2020); computational neuroscience at ENS (Cogmaster, 2020), thesis in Srdjan Ostojic's lab; Mines Paris-PSL, statistics and machine learning (2025). Research stays at LBNL, IBM Research Zurich, NeuroPSI (Alain Destexhe) and NeuroSpin (Stanislas Dehaene). Papers: PLOS Computational Biology 2023 (second author), Neuromorphic Computing and Engineering 2022 (co-author).
Sycophancy program (March–September 2026, alone, self-funded):
- Displacement law (paper under review at ICLR 2027), the basis of Paper C: pressure moves Llama-3.1-8B-Instruct's rating a fixed fraction of its distance to a destination set by the framing, Δ = g·(ĉ − p₀), g ≈ 0.70, ĉ ≈ 1.46 under criticism vs 2.94 under praise (disjoint 95% CIs; R² 0.77/0.79). Parameters transfer unchanged to a second campaign (R² 0.73/0.69). The law collapses on Qwen2.5-7B.
- Readable is not causal: the direction a behaviour-tracking probe reads does under 1% of the causal work (full state: 68%).
- Failure: a rank-3 ablation cut judged sycophancy from 61% to 46.5% (N = 200), but it shifted verdicts with no pressure at all; responses stored truncated at 300 characters had made a generic softening look like a safety effect. Reported as revised.
- An audit by a separate AI agent instance lists 131 claims-register objects, among them 33 established, 19 refuted and 29 failed predictions kept.
This project, phase 0 (since 5 October 2026): 98 source papers hashed and 3,497 quotations checked by script (0 failures); activation harness validated on Llama-3.1-8B; aggregators validated in a pre-registered simulation; 602 automated tests; about $20 of compute. I set the questions and take every decision; AI coding agents do the engineering and internal reviews under written rules.
Expenditure and staffing: 2026 to date, about €7,500 (≈ $8,400), all self-funded; one person.
I was accepted to the Singapore AI Safety Fellowship (2026; declined) and reached the final stage of the 2026 Anthropic Fellows Program.

## Portfolio and links

github.com/lciric/sycophancy-construct-validity: the causal project; TRACEABILITY.md maps every README number to its result file.
github.com/lciric/safety-concept-vectors: five safety concepts on Qwen2.5-7B.
github.com/lciric/eval-awareness-detection: the eval-awareness prototype, committed 11 March 2026.
github.com/lciric/does-quantization-kill-interpretability and github.com/lciric/gptq-from-scratch: earlier projects.
Cimeša, Ciric & Ostojic (2023), PLOS Computational Biology.
Le Gallo, Nandakumar, Ciric et al. (2022), Neuromorphic Computing and Engineering.
Behavioural preprint on the displacement law: [link once posted].
This project's repository is private for now; pre-registrations and sealed results are available to fund managers on request.

## Goals and plan

Goal: two papers with open code in seven months (December 2026 to June 2027), on questions AI control depends on. Each gate is decided on criteria sealed before data; negative results are published.
1. Paper C, monitor corruption (months 1–4). Under graded pressure, a monitor's verdict should move toward a destination, Δv = g·(ĉ − v₀), the law I measured for sycophancy. I estimate g and ĉ, unconstrained, for LLM judges and activation probes under five attack families (flattery, claimed authority, forged approvals, stylistic impersonation of the operator, in-band orders); then the cost of moving a probe versus a judge, countermeasures (trusted paraphrase, a mixed judge–probe quorum), and an acceptance test: does g under benign pressure predict collapse under optimized attack? Gate GC (month 2): if prior work already covers the law, the paper refocuses on cost and the test.
2. Paper A, diffuse sabotage (months 1–7). On a reconstruction of the research-sabotage setting of Terekhov et al. (arXiv 2606.08892) with open 8B models, sabotaging model organisms and seeded ground truth: black- vs white-box access, crossed with per-action vs sequential aggregation under an anytime-valid false-alarm guarantee. Gate G1 (month 4): white-box sequential must beat the best black-box baseline on recall at 1% false positives (95% CI); otherwise I publish the negative result and what the probes actually measure. Then adaptive attacks, up to fine-tuning against the probe.
Outputs: Paper C on arXiv by month 4, Paper A by month 7, with code, organisms and probes. Developers can read their own agents' activations; this tells them whether probes add security a judge does not, and how cheaply each is corrupted.

## Why might this not succeed?

Paper A: 8B agents may be too weak to sabotage subtly (pre-registered fallback: a simpler rubric), or the internal signal may be absent; G1 then fails and the negative result is published. Paper C: prior work may already contain the deference law (gate GC refocuses the paper), or probes may move without weight access (it becomes a paper on construct contamination). Execution: I work alone with AI agents whose errors may be correlated, so ground truth gets paid human validation. Paper C comes first and stands alone if Paper A slips.

## Budget

Mainline: $58,630 for seven months (December 2026 to June 2027): 59.7% my stipend ($5,000 a month, gross, French income tax and social contributions included), 6.8% GPU compute, 11.9% AI research tooling (the coding agents that do the engineering), 6.8% paid human validation, 4.3% one workshop trip, 1.4% miscellaneous, 9.1% buffer (10% of costs). Minimum $28,160 (four months, Paper C alone); maximum $138,600 (twelve months, adds Paper B). Compute or credits obtained elsewhere are deducted.

## Amount requested (USD)

58630

## What would you do with additional funding?

In order: Paper B, the multi-agent extension (a part-time research engineer and five more months); a 70B organism family and a second model family, for external validity; reinforcement-learning attacks at larger scale; a statistics consultant for the lemma; more paid validation. Together: the $138,600 scenario.

## Alternatives and applications in the last 12 months

Without this grant I would return to paid work and continue part-time: Paper C first, Paper A postponed. Applications in the last 12 months (applied; status; requested; received; decision):
- Anthropic Fellows Program (26 Apr 2026; final stage, last interview could not take place, deferral not guaranteed; stipend and compute; none; after my recovery)
- CBAI (12 Apr 2026; declined; stipend; none)
- ERA:AI Fellowship, Cambridge (12 Apr 2026; interviewed, no decision received; stipend; none)
- OpenAI Safety Fellowship (May 2026; declined June 2026)
- Astra Fellowship (May 2026; declined)
- Singapore AI Safety Fellowship, SASH (July 2026; accepted, I declined)
- Meta FAIR Paris PhD position, a job (Sept 2026; pending)
- Applying now for this project: Foresight AI Nodes ($46,200, Paper C and its extension), BlueDot Rapid ($11,000, compute and tooling), BlueDot Career Transition ($38,500, stipend), Anthropic and OpenAI API credits, TPU Research Cloud and NDIF (in-kind compute).
I will accept only one stipend for any period and return overlapping funds.

## Confidential information for the fund

I was injured in a cycling accident in late September 2026 and am recovering; I expect to work full-time again by mid-November 2026. Because of it, my final Anthropic Fellows interview could not take place; the team cannot guarantee a deferral to a later cohort and asked me to contact them once I have recovered. It is also why the grant starts on 1 December. The research plan in the attached proposal is unpublished; please do not share it beyond the fund team and its advisors.

## Anything else

An 8-page research proposal is attached under File upload. Pre-registrations, sealed results and decision registers are available to fund managers on request.

## Collaborators

Working independently

## Centre for Effective Altruism employment

I have never held a paid position at the Centre for Effective Altruism.

## Location

Based in Paris, France; open research, not tied to any country.

## How did you hear about the fund?

Through the Effective Alignment Discord.

## LinkedIn and links

linkedin.com/in/lazar-ciric-55a23913b, github.com/lciric
