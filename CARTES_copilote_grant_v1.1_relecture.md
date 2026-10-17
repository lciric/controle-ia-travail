# Cartes du copilote grant — relecture — v1.1 (17 octobre 2026) — copie pour la session du programme contrôle IA ; une ligne confidentielle (q34) en est retirée

Les 46 cartes, par famille. À lire une fois en entier : chaque phrase doit être une chose que tu dirais, vraie à ta connaissance. Une carte fausse, trop forte ou pas de toi : note sa clé et la correction. Les lignes « ⚠ » attendent POSITIONS.

Contrôles passés : contrat du deck de GEL-16 (tête, largeur, cinq cadres) et nombres, 46 cartes sur 46, 0 en défaut.

## Ouverture

**Q1 — The project in two minutes** — *« Could you give me a quick overview of the project in your own words? »*

- 0) Monitors score one action at a time: diffuse sabotage hides in many small, innocent-looking choices.
- 1) Paper A asks whether that evidence adds up inside the agent's own activations, read by probes over time.
- 2) Paper C asks how easily the monitor itself is persuaded, an LLM judge versus a probe, and at what cost.
- 3) Paper C comes first: it extends the deference law I measured on sycophancy, and it stands alone.
- 4) The ask: $58,630 for seven months; $28,160 funds Paper C alone. Criteria are pre-registered.

**Q2 — The result I most expect** — *« What is the one result you most expect to come out of this? »*

- 0) Paper C lands first: whether persuasion moves a monitor's verdict toward the attacker's own target.
- 1) Under graded pressure I fit Δv = g·(ĉ − v0) for judges and for probes, attack family by family.
- 2) The prediction: g is positive for judges; for a probe that reads the acting agent, g ≈ 0.
- 3) Then the displacement tax says how much harder a probe is to move than a judge.
- 4) ⚠ POSITIONS 11: your own expectation, and any odds, in your words.

## Probleme

**Q3 — Why diffuse sabotage, why now** — *« Why is diffuse sabotage an important threat, and why should we care about it now? »*

- 0) Developers are starting to hand research to agents: a misaligned one needs no blatant act, just steady small biases.
- 1) Weaker controls, sterile directions, inflated costs: each defensible alone, together a sabotaged programme.
- 2) A per-action monitor only flags what is anomalous in one action, so here it is blind by construction.
- 3) Terekhov et al. framed it and judged monitoring less promising; they did not test white-box accumulation.
- 4) If evidence accumulates inside the agent, developers get a cheap layer; if not, clear limits for safety cases.

**Q4 — Why probes, not a better judge** — *« Why white-box monitoring with probes rather than a better black-box monitor? »*

- 0) Developers own their agents' activations: a small trace per action can add up inside when outputs show nothing.
- 1) A judge only sees text, the text is built to look innocent, and the agent can address the judge.
- 2) A probe reads the acting agent directly; I predict persuasion moves it far less than a judge.
- 3) I don't assume it: H1 compares white- and black-box at equal aggregation and equal false positives.
- 4) If probes don't win at gate G1, I publish that, and what the probes actually measure.

**Q5 — Why per-action monitoring fails** — *« Isn't per-action monitoring good enough in practice? »*

- 0) Per-action works for blatant attacks: diffuse sabotage keeps every single action below the threshold.
- 1) A threshold calibrated on honest actions can only flag what is anomalous in that one action.
- 2) When nothing is anomalous alone, accumulating evidence is the only way to see the pattern.
- 3) Split across agents it gets worse: published attacks evade monitors that watch one instance at a time.
- 4) So the fix is not a better threshold but a better aggregator, with a false-alarm guarantee.

## Nouveaute

**Q6 — What's new beyond CUSUM** — *« What is actually new here? Isn't this just running a sequential test or a CUSUM on probe scores? »*

- 0) Each piece exists, the conjunction doesn't: anytime-valid sequential tests on the acting agent's own probes.
- 1) Probes over turns, sequential tests on scores, CUSUM on internal states are each published separately.
- 2) Applied together to diffuse sabotage, in the sources I verified, they are not: that is the claim.
- 3) The theory adds a negative theorem: when an attack permutes scores, sums and maxima are blind.
- 4) Above all, the measurement on real activations decides which aggregator a developer needs.

**Q7 — Answering Terekhov et al.** — *« Terekhov et al. said monitoring looks less promising for diffuse threats. Why do you think it can work? »*

- 0) Their doubt fits per-action black-box monitors: I test the cumulative, white-box case they did not pursue.
- 1) They introduced the diffuse setting and studied training-based mitigations; they release no code or data.
- 2) I rebuild their research-sabotage setting on open-weights models, with seeded ground truth.
- 3) Paper A then crosses black- versus white-box with per-action versus sequential aggregation.
- 4) If they're right for probes too, gate G1 fails and I publish the negative result.

**Q8 — What's new in Paper C** — *« People have already shown that monitors can be persuaded. What is new in Paper C? »*

- 0) Persuading judges is known: the new part is a free destination, family by family, judges versus probes.
- 1) I fit Δv = g·(ĉ − v0) without imposing ĉ, then test it against the attacker's target and the corpus mean.
- 2) Five attack families, from flattery to in-band orders, on control monitors under attack.
- 3) Then the displacement tax: what it costs to move a probe that reads the agent, versus a judge.
- 4) If prior work already has the law, gate GC refocuses Paper C on the tax and the acceptance test.

**Q9 — Where this sits in AI control** — *« How does this fit with the AI control work of Redwood and the labs? »*

- 0) Control monitors score actions one by one: I target the diffuse case they handle worst.
- 1) Redwood's Ctrl-Z resamples suspicious actions; my monitors add internal evidence accumulated over time.
- 2) Paper C asks whether the monitor in these protocols can itself be talked round.
- 3) The protocol is standard control: an authenticated operator channel, in-band content treated as data.
- 4) For a lab: which monitor to trust, how cheaply each is corrupted, and an acceptance test.

**Q10 — If someone publishes first** — *« What happens if someone publishes the core idea before you do? »*

- 0) It's a planned risk: I pivot to population-level statistics and data curation, with a weekly watch.
- 1) Claims found occupied are withdrawn; at least eight pieces already were.
- 2) Paper C doesn't depend on the sequential-probe core, so it stands either way.
- 3) No claimed statement has been found fully occupied so far.
- 4) The main contribution is the measurement on real activations, not the idea alone.

## Plan

**Q11 — Month one, December** — *« What will you do in the first month? »*

- 0) Close gate G0, then start both papers: judges under five attack families, and the organisms.
- 1) Paper C: deference of judges under graded pressure (HC1), then probes under the same attacks (HC2).
- 2) Paper A: the organisms and their dose–response in the rebuilt research-sabotage environment.
- 3) G0 needs organisms with a dose–response, probes above the random floor, a running black-box baseline.
- 4) And sealed, counter-read pre-registrations of G1 and Paper C before any data.

**Q12 — Gates and milestones** — *« What are the key decision points, and when will you know whether it is working? »*

- 0) Three gates steer the plan: G0 in December, GC at month two, G1 at month four.
- 1) GC: if prior work covers the law, Paper C refocuses on the tax and the acceptance test.
- 2) G1: white-box sequential must beat the best black-box baseline on recall at 1% false positives, 95% CI.
- 3) Criteria are sealed before data; a fresh reviewer pronounces each verdict before I sign off.
- 4) Outputs: Paper C on arXiv by month four, Paper A by month seven.

**Q13 — If gate G1 fails** — *« What happens if the probes don't beat the black-box monitors, if gate G1 fails? »*

- 0) A failed G1 is a result: I publish the negative, and construct validity becomes the main line.
- 1) The negative theorem then says which aggregator could still work.
- 2) H8 asks what the probes really measure, intent or evaluation awareness; that stands either way.
- 3) Paper C doesn't depend on G1, so the grant still delivers a full paper.
- 4) Developers get clear limits: where probe-based monitoring should not be trusted in a safety case.

**Q14 — The deference law** — *« Can you explain the deference law and how it carries over to monitors? »*

- 0) The law in one line: pressure moves a judgment a fixed fraction of the way to a target it sets.
- 1) On Llama-3.1-8B, Δ = g·(ĉ − p0), g ≈ 0.70; criticism and praise set targets ĉ ≈ 1.46 and ≈ 2.94.
- 2) Fitted parameters predicted a second campaign unchanged (R² 0.73 / 0.69); the law collapses on Qwen.
- 3) In Paper C the same form, Δv = g·(ĉ − v0), is fitted on monitors' verdicts, with ĉ left free.
- 4) If ĉ is the attacker's target, monitors defer like the model did; if the corpus mean, it's regression.

**Q15 — Why 8B open models** — *« Why 8B open models? Will the results transfer to frontier agents? »*

- 0) White-box needs the weights: open-weights models let me read activations and train LoRA organisms.
- 1) Transfer is measured, never assumed: Qwen2.5-7B serves as a second, heterogeneous agent.
- 2) In my sycophancy work the law held on Llama and collapsed on Qwen: that's why I check.
- 3) The filed risk: 8B agents may be too weak to sabotage subtly; the fallback is a simpler rubric.
- 4) More money adds a 70B organism family and a second model family, for external validity.

**Q16 — Building the saboteurs** — *« How will you build model organisms that sabotage subtly? »*

- 0) Two families: a hidden instruction in the system prompt, and a LoRA adapter distilled from it.
- 1) The LoRA version sabotages with no instruction at inference, so a probe can't just read the prompt.
- 2) Validity: an instruction probe should work on the first, fail on the second; an intent probe, both.
- 3) Controls split intent from evaluation awareness: an honest model told it's watched, a saboteur told it isn't.
- 4) The adapters have an adjustable dose; dose 0 reproduces the base model bit for bit.

**Q17 — Where ground truth comes from** — *« Where does your ground truth come from? How do you know what counts as sabotage? »*

- 0) Seeded targets plus delayed checks: what counts as sabotage is planted before any data.
- 1) Agents write and revise ML experiment proposals, scored by a weaker trusted evaluator on a rubric.
- 2) Sabotage is a systematic bias: sterile directions, weakened controls, inflated costly choices.
- 3) Pre-registered seeded targets give the labels; a subsample gets delayed verification.
- 4) AI reviewers may err together, so the budget pays human experts to validate the ground truth.

**Q18 — Is seven months enough** — *« Is seven months realistic for two papers? »*

- 0) Paper C comes first and stands alone: if Paper A slips, the grant still delivers a paper.
- 1) Phase 0 is already running: harness validated, 602 tests, 31 of 31 simulated predictions confirmed.
- 2) Paper C by month four, on arXiv and at a workshop; Paper A by month seven.
- 3) Within Paper A, gate G1 comes before the adaptive attacks, which are trimmed first.
- 4) Coding agents do the engineering under written rules; that is why the mainline has no engineer.

**Q46 — Why Paper B is there** — *« Why is Paper B in the proposal if it is not funded? »*

- 0) It shows where the theory goes: time and agents are the same object, so the swarm is next.
- 1) It is not in the seven-month request: only the ambitious scenario, or a later grant, funds it.
- 2) A backdoor split across commits, each diff innocent: can probes over time see copies co-elevate?
- 3) Its gate G2 must first replicate the fragmentation effect, else it refocuses on a single agent.
- 4) Papers A and C share the harness, organisms and probes; Paper B would extend them to many agents.

## Risques

**Q19 — The most likely failure** — *« What is the most likely way this fails? »*

- 0) Paper A carries the main risk: 8B agents may not sabotage subtly, or may leave no internal signal.
- 1) If the agents are too weak, the pre-registered fallback is a simpler rubric.
- 2) If the signal is absent, G1 fails and I publish the negative result and what the probes measure.
- 3) Paper C's risk is prior work owning the law: gate GC then refocuses it on cost and the acceptance test.
- 4) Execution: AI agents' errors may be correlated, so ground truth gets paid human validation.

**Q20 — Solo, with AI coding agents** — *« You work alone with AI coding agents. How do you make sure the results are right? »*

- 0) I set the questions and take every decision: the agents do engineering and reviews under written rules.
- 1) Pre-registrations are sealed before data and counter-read by a fresh reviewer who didn't write them.
- 2) Every number points to a file and a hash; every stop guard is tested on a healthy case and an artefact.
- 3) Reviewers share a model family, so their errors may correlate: human experts validate ground truth.
- 4) The method so far: 3,497 quotations checked by script, 0 failures; 147 corrections to my own drafts.

**Q21 — The rank-3 result** — *« Your CV says the rank-3 ablation worked, but the proposal says it failed. Which is it? »*

- 0) That CV line is out of date: the proposal's account is the right one, and the effect doesn't stand.
- 1) The ablation lowered judged sycophancy from 61% to 46.5%, but it also moved verdicts with no pressure.
- 2) Responses stored truncated at 300 characters had made a generic softening look like a safety effect.
- 3) The full text is gone, so re-judging can't rescue it: I reported it as a failure.
- 4) That's why my rules now say: never read verdicts on truncated windows.

**Q22 — What the failure taught me** — *« What did you learn from the failure in your sycophancy work? »*

- 0) Three lessons, now in my rules: no truncated windows, ordinal instruments, deference as a gain.
- 1) A rank-3 ablation looked like a safety effect, but truncated responses had manufactured it.
- 2) So verdicts are never read on truncated windows, and instruments are ordinal or continuous.
- 3) Deference is treated as a gain, which is exactly how Paper C measures monitor corruption.
- 4) A separate agent audits my claims register: 131 objects, 19 refuted, 29 failed predictions kept.

## Budget

**Q23 — The budget in one breath** — *« Can you walk me through the budget? »*

- 0) $58,630 for seven months: 59.7% is my stipend, the rest buys compute, tooling and validation.
- 1) Stipend $35,000; AI tooling $7,000; compute $4,000; human validation $4,000.
- 2) Travel $2,500, miscellaneous $800, and a 10% buffer of $5,330, stated explicitly.
- 3) Minimal: $28,160, Paper C in four months. Ambitious: $138,600, adds Paper B over twelve months.
- 4) Compute or credits obtained elsewhere are deducted.

**Q24 — The stipend** — *« How did you set the stipend at five thousand dollars a month? »*

- 0) $5,000 a month, gross: French income tax and social contributions are paid out of it.
- 1) That was about €4,450 a month on 7 October 2026.
- 2) The same monthly rate in every scenario: four, seven or twelve months.
- 3) I accept only one stipend for any period and return overlapping funds.
- 4) ⚠ How the rate was benchmarked is not in my file: offer to follow up in writing.

**Q25 — AI tooling, $1,000 a month** — *« Why a thousand dollars a month on AI tooling? What does it buy? »*

- 0) The coding agents do the engineering: that's why the mainline has no engineer on the payroll.
- 1) $7,000 over seven months, against $21,000 for the half-time engineer of the ambitious plan.
- 2) The agents also run the literature checks and internal reviews, under written rules.
- 3) ⚠ POSITIONS 13: what it buys concretely, subscriptions and API.
- 4) Their errors may correlate, which is why paid human validation sits next to them in the budget.

**Q26 — Why $4,000 of compute** — *« Why four thousand dollars of compute when your own quote is lower? »*

- 0) The quote covers the base plan: the mainline adds seeds, replications and larger GPUs where memory needs it.
- 1) Quote for Papers A to C: 800–1,200 A100-hour equivalents, about $1,200–2,700 with storage.
- 2) Phase 0 has used about $20 of compute so far.
- 3) Spending is quoted per phase and signed off first, with a ceiling and an alert per quote.
- 4) Compute or credits obtained elsewhere, NDIF or API credits, are deducted.

**Q27 — If you fund only part** — *« If we could only fund part of it, what would you do? »*

- 0) The minimal version stands alone: $28,160 funds Paper C in four months.
- 1) Paper C extends a law I've already measured, and its outcome doesn't depend on Paper A's gate.
- 2) It delivers Paper C on arXiv and at a workshop, with the acceptance test for monitors.
- 3) ⚠ POSITIONS 6: whether you'd take a smaller first check, and what then for Paper A.
- 4) Without more, Paper A would wait, as it would without this grant.

**Q28 — With more money** — *« What would you do with more money? »*

- 0) In order: Paper B, then external validity, then bigger attacks; together the $138,600 scenario.
- 1) Paper B, the multi-agent extension: a part-time research engineer and five more months.
- 2) A 70B organism family and a second model family, so results don't rest on one family.
- 3) Reinforcement-learning attacks at larger scale, and a statistics consultant for the lemma.
- 4) And more paid validation of the ground truth.

**Q29 — Receiving the money** — *« How would you receive the money? Do you have a fiscal sponsor? »*

- 0) ⚠ Your call, POSITIONS 3: a fiscal sponsor, or a personal grant.
- 1) The budget already holds a line for accounting or fiscal-sponsor fees, within the $800 of miscellaneous.
- 2) The stipend is gross: French income tax and social contributions are paid out of it.
- 3) If they need a structure you don't have, offer to follow up in writing.
- 4) Never name a sponsor that isn't confirmed.

## Contrefactuel

**Q30 — If you don't fund it** — *« What happens if we don't fund you? »*

- 0) I'd return to paid work, part-time on this: Paper C first, Paper A postponed.
- 1) Everything so far is self-funded: about €7,500 in 2026, one person.
- 2) Other applications are running, but I accept only one stipend for any period.
- 3) The grant buys full-time work from December, and the human validation a solo setup needs.
- 4) It also funds open artefacts that lower the cost of follow-up work in AI control.

**Q31 — Other funders** — *« You have applied elsewhere. What if Foresight or BlueDot also fund you? »*

- 0) One stipend for any period: overlapping funds go back, and outside compute is deducted.
- 1) Applying now: Foresight AI Nodes, $46,200, for Paper C and its extension.
- 2) BlueDot Rapid, $11,000, compute and tooling; BlueDot Career Transition, $38,500, stipend.
- 3) Plus Anthropic and OpenAI API credits, and TPU Research Cloud and NDIF, in-kind compute.
- 4) Any compute or credits obtained elsewhere come off this budget.

**Q32 — The Anthropic Fellows process** — *« What is the status of your Anthropic Fellows application? »*

- 0) I reached the final stage: the last interview couldn't take place, and a deferral isn't guaranteed.
- 1) The team asked me to get back in touch later; nothing is decided.
- 2) Whatever happens, I accept one stipend for any period and return overlapping funds.
- 3) ⚠ POSITIONS 7: what you'd do if the programme takes you back later.
- 4) Say no more unless asked directly: the reason is in the confidential part of the form.

**Q33 — If the FAIR PhD comes through** — *« What if the Meta FAIR PhD position comes through? »*

- 0) It's pending: one stipend for any period, and overlapping funds go back.
- 1) It's listed in the application as a job, pending since September.
- 2) ⚠ POSITIONS 1: what you'd do with this grant if FAIR says yes.
- 3) Commit to nothing on the call beyond what POSITIONS says.
- 4) The rule already in the file: one stipend at a time, overlaps returned.

**Q34 — Why December** — *« Why does the grant start in December rather than now? »*

- 0) A personal reason: I expect to work full-time again by mid-November, so the grant starts on 1 December.
- 1) [line from the confidential part of the form, omitted from this copy]
- 2) Phase 0 continues meanwhile: the pilot runs before the grant starts.
- 3) ⚠ POSITIONS 8: what you're willing to say, in your words.
- 4) Then move on: G0 closes in December, the first month.

## Candidat

**Q35 — Why I'm the person for this** — *« Why are you the right person to do this? »*

- 0) Two reasons: Paper C extends a law I measured, and my rules are built to catch my own errors.
- 1) Physics at ENS Paris-Saclay, computational neuroscience at ENS, statistics and ML at Mines Paris-PSL.
- 2) Research stays at LBNL, IBM Research Zurich, NeuroSpin; papers in PLOS Comp. Biol. and NCE.
- 3) From March to September 2026, alone: a law under review at ICLR 2027, and a failure I reported myself.
- 4) Phase 0 since 5 October: harness validated, 602 tests, 98 papers hashed.

**Q36 — Mentor or senior reviewer** — *« Do you have a mentor or anyone senior reviewing your work? »*

- 0) ⚠ Your call, POSITIONS 4: any senior person, and whether you'd take an advisor they suggest.
- 1) What the file says: fresh AI reviewers counter-read every plan, and I sign off each gate.
- 2) Paid human experts validate the ground truth, because AI reviewers' errors may correlate.
- 3) The ambitious plan adds a statistics consultant for the lemma, about 40 hours.
- 4) No human collaborator is funded in the mainline.

**Q37 — Phase 0 so far** — *« What have you done so far in phase 0? »*

- 0) Instruments first: literature verified, theory simulated, harness validated, environment under way.
- 1) 98 arXiv PDFs hashed; 3,497 quotations checked by script against the page, 0 failures.
- 2) The simulation confirmed 31 of 31 pre-registered predictions: it validates the instrument, not the claim.
- 3) Activation harness validated on Llama-3.1-8B on an H200; 602 automated tests.
- 4) The research-sabotage environment v0: 96 papers drawn, 64 for the pilot, 32 in reserve.

**Q38 — Full time on this** — *« Will you work on this full time? Are you still working as a consultant? »*

- 0) Full time from 1 December: the stipend pays for seven months of full-time work.
- 1) ⚠ POSITIONS 2: your current job status, in one line.
- 2) The CV lists AI Lead Consultant at EPSA Innovation, 2024 to 2026.
- 3) Without the grant, I'd go back to paid work and continue part-time.
- 4) Until December, phase 0 continues: the pilot runs before the grant starts.

## Impact

**Q39 — Who uses this, and how** — *« Who would use your results, and how would they change what labs do? »*

- 0) Labs automating AI research: they own their agents' activations and need monitors they can trust.
- 1) If it works: a cheap layer against diffuse sabotage, with a false-alarm guarantee that fits audit budgets.
- 2) If it fails: clear limits, where probe-based monitoring should not be trusted in a safety case.
- 3) Paper C: a measured cost of corrupting a judge versus a probe, and a pre-deployment acceptance test.
- 4) Open artefacts, environment, organisms, probes, aggregators, cut the cost of follow-up work.

**Q40 — The acceptance test** — *« What is the acceptance test for monitors, and why would a developer run it? »*

- 0) Measure how far benign pressure moves a monitor: the bet is that it predicts collapse under attack.
- 1) The gain g is fitted on benign pressure corpora, cheap to run before deployment.
- 2) HC6 tests whether that benign g predicts collapse under optimized attack.
- 3) If it does, a developer can screen monitors without running costly adaptive attacks.
- 4) If it doesn't, that matters too: benign robustness would not certify a monitor.

**Q45 — What success looks like** — *« How will we know at the end of the grant whether it was a success? »*

- 0) Four criteria, written in advance: two measurements, one verdict, and Paper B only if funded.
- 1) Paper C: the deference law and the displacement tax are measured.
- 2) Paper A: the lemma and the negative theorem are proven and tested on real activations, in the 2 × 2.
- 3) A construct-validity verdict on what the probes measure stands even if H1 fails.
- 4) Deliverables: Paper C by month four, Paper A by month seven, open code, organisms, probes.

## Ethique

**Q41 — Dual use and what I release** — *« Are there dual-use risks in building sabotaging organisms and attacks on monitors? What will you release? »*

- 0) ⚠ Your call, POSITIONS 5: whether you'd hold back the strongest attacks or organisms.
- 1) What the file says: code, organisms, probes and pre-registrations are released in month seven.
- 2) The organisms are open 8B models with a sabotage policy on research proposals.
- 3) The five attack families are named in the file: flattery, authority, forged approvals, impersonation, orders.
- 4) The file's stated purpose: lowering the cost of follow-up work in AI control.

## Cloture

**Q42 — My questions for you** — *« Do you have any questions for us? »*

- 0) ⚠ POSITIONS 10: your two questions go here, in your words.
- 1) Possible: what's your timeline for a decision?
- 2) Possible: would you consider the minimal scenario as a first check?
- 3) Possible: would the pre-registrations and sealed results be useful to you?
- 4) Possible: what reporting do you expect during the grant?

**Q43 — Anything else to add** — *« Is there anything else we should know? »*

- 0) One line on the bet: if evidence adds up inside the agent, a cheap monitor; if not, clear limits.
- 1) Paper C stands alone, so even the minimal $28,160 buys a full paper.
- 2) Pre-registrations, sealed results and decision registers are available on request.
- 3) Negative results will be published, and so will the code.
- 4) Thank them; ask about next steps if they haven't come up.

**Q44 — Why this fund** — *« Why did you apply to this fund? »*

- 0) Early-stage, individuals, tolerant of failure: that fits a pre-registered project with publishable negatives.
- 1) I heard of it through the Effective Alignment Discord.
- 2) The project is early: phase 0 runs now, and both outcomes of each gate are publishable.
- 3) The request, $58,630, sits within the fund's typical range.
- 4) And a smaller first step exists: $28,160 for Paper C alone.

