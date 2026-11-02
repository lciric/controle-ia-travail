# Réponses aux mentors, reformulation minimale — v4 — 2 novembre 2026 (base : formulaire collé à 20:32 UTC ; corrections de fond minimales d'après la relecture neuve et les vérifications de conv-audit ; demande de Lazar à 20:52 UTC : « je veux une reformulation minimale »)

## KIRCHNER Q1

If you haven’t heard/seen: Since October I’ve been running an automatic researcher (github.com/lciric/ideation-organism). Generative agents submit laws to propose; a statistical judge grants acceptances.

The pitch: what if you score a population of LLM agents submitting laws that govern AI decision-making with something arguments can’t lie to? Would it defend itself against other agents trying to game it?

In short: yes to part 1. To part 2: partly. An attack found a hole. Patch written; preregistered tests of it to follow.

Details:
Builders built; builders tested. Proposers of different archetypes using multiple algorithms as input. A frozen statistical judge that scores each proposed law by how distinguishable it is from a literal null hypothesis. Preregistered death tests to run in sandbox, sanity checked by a model from a completely different family (tested offline, not yet run for real).
929 total tests.
Plus a mutation benchmark: the code was intentionally mutated 224 times to check that the tests catch each mutation. Every failure was caught by a test for precisely the thing it was designed to test.

Kept what passed. Clearly my qualitative LLM judges were failing when compared to the frozen statistical judge. They told me nothing: they called 11 of 12 cards “notable”, with κ = 0 inter-agreement. The more terse statistical judge actually explained exactly what went wrong; I didn’t exercise it long enough to know whether there truly was a law there to be found. The power curve confirmed this. Then I tested it once with no deviations from my locked-in plan on an entirely different seed pass of 288 episodes of real data that I hadn’t inspected prior to running this pass:
It accepted all 3 laws I inserted.
It rejected all 19 non-laws.
It did not accept a single law from the real data itself.

Bots coded to cheat broke it. 4 total accepted. Each and every one blended or deformed past laws the judge itself had previously accepted.

My judge had no null for blends of its own past acceptances. The problem is obvious to me now, but I crashed into a wall. Securing the judge from being bribed was easy. Shielding it from agents which can systematically submit handpicked proposals which make use of its previous acceptances to trick it was the hard part. This has been dozens of iterations.

The failure is a cousin of 26 of the 39 cheating examples in your automated-researcher paper (submit the same thing twice; let randomness do the work). The fix passed its preregistered validation on 1 November (1k replications per algorithm; checked by a fresh reader who worked on neither the code nor the text). Then the actual attack.

Real agents trying to trick the system. Automated law proposers that were given a copy of the judge’s past decisions attempted to trick it by causing bogus laws to be accepted. They found a hole (with or without the past decisions) by recombining, piece by piece across sub-populations of the data, laws they already knew were accepted: exactly where the judge says it does not look. The judge’s null did not cover these recombinations.

The fix is written. It’s coded and running as part of regression tests. Tomorrow it faces its preregistered test.

## KIRCHNER Q2

Underrated: a score that cannot be inflated by an agent that games it on purpose. Overrated: rejections based on resubmission-detectors that won’t work anymore when researchers start using automated alignment agents to optimize on your score automatically. With your automated alignment researchers, a method’s top score is the maximum of noisy evaluations, so it’s completely rational for an agent to just resubmit the same method repeatedly unchanged (which is what happens in 26 of the 39 detections you report), and your best score is an upwardly biased estimate of that method’s true value. You treat this as pathological misbehaviour we need better ways to detect in Monitoring, but it’s just the utility-maximizing reaction to how you’ve designed your score, and worse: as agents get better at seeking rewards (i.e. your future failure mode) the solution will have to come from changing your score, not detecting failure: don’t accept a method until the evidence it outperforms everything already accepted remains significant no matter how many times you re-evaluate it on fresh seeds, and still holds on benchmarks it hasn’t seen and on bigger models. Leaderboard overfitting with adaptive submissions is well-understood (the Ladder, the reusable holdout); what’s underrated is what happens when an agent figures this out and does it on purpose with near-copy submissions that aren’t close-enough-to-identical-for-a-monitor-to-care duplicates (new seed + small method tweak +Blend of accepted methods).

Experiment 1: build a judge that cannot be beaten by resubmissions on your test harness. First re-score your current leaderboard methods on new seeds (is selection bias inflating your scores? ), then on new benchmarks/larger model (does it even generalize?). Replace “best of noisy runs” with a sequential test: update a test martingale with each method’s evaluations against null hypothesis of baseline + every method already accepted on your leaderboard (allowing any resubmission, or mixture of accepted methods, to carry 0 evidence), using Ville’s inequality to ensure false positive rate is at most α no matter how many times you test, and a simple multiple testing procedure across methods. Retest logged methods from their logged per-run scores, then run new agents that observe verdicts. Metrics: what percentage of flagged methods (and re-submissions) still get accepted; power lost on methods that made true progress (closed the gap, as determined by your held-out benchmark and Petri); difficulty for a verdict-aware agent to search down a class of methods that the judge declares it does not cover; all compared against the Ladder as a baseline. Under my system, it did, with or without verdicts: known laws recombined piece by piece across sub-populations. This fix’s preregistered validation runs next.

Evidence that would sway me: empirical demonstrations that the power lost on truly novel methods exceeds some a priori chosen margin (the judge would be too blunt an instrument to bother deploying in research settings), agents being able to pass unchanged resubmissions at rates substantially higher than α (the null hypothesis is wrong), agents that see verdicts performing no better than blind resubmission at beating the naive maximum (the problem is less severe than I think), or top methods keeping their score on fresh seeds (little adaptive overfitting, as Roelofs et al. found on Kaggle competitions). Each of those are pre-registered analyses; either way, I’ll send you the paper.

## HEIMERSHEIM Q2

One question I’ve been wondering is how tightly correlated what a probe accesses is to what’s actually driving computation in the model. Coming from neuroscience, low-rank recurrent networks, population dynamics — worlds where low dimensional, readable structure and driving dynamics are separable phenomena, my read-out-of-sync result suggested that that distinction holds in a language model (it looked at the direction that predicts sycophancy and does <1% of the causal work on Llama-3.1-8B). That gap matters for safety because activation monitors, steering defences, evaluation-awareness tests, etc. all depend on the gap being small. I want to understand when that is/isn’t true using preregistered interventions and controls, and publish null results when I discover them. Your work on plateaus is essentially the clearest formulation of that measurement question that I’ve seen. Instead of single dose interventions that my rank-1 vs rank-3 result relied on, you’re attempting to measure a dose–response curve.

## JANG ET FENG

White-box methods examine the computation underlying an action, rather than its presentation. The lack of whitebox access hurts black-box auditing: sandbagging by imitating a weaker model broke black-box detection in the auditing game (arXiv 2512.07810), probes fared better, and training-based elicitation exposed full capability. My motivation is architectural: if misbehavior is spread across many actions, it will necessarily blend in with noise on a per-action basis; you want something that they can’t sanitize, that gives you per-action signal that you can calibrate on honest episodes and bank using an anytime-valid false alarm bound, and activations can work well for this. Moving a probe that reads the acting agent took a rank-1 weight update, context alone being too weak (arXiv 2609.36490), but I’ll leave that as an aside that you take as conjecture instead of a result. Your exploration-hacking paper discusses how frontier models reason explicitly about suppressing exploration, making them susceptible to text monitors; the white-box problem gets real once they learn not to. Weight-based methods have this advantage over black-box.

Caveats:

1. Readable doesn’t imply causal. Example: A direction that was incredibly cheap to monitor on Llama-3.1-8B correlated with shift in sycophantic judgement (ρ = .68), but captured <1% of the causal effect. On aggregate, 68% of the causal effect was captured by the residual state. Monitoring this direction may well correlate in distribution but completely break when exploited.

2. Construct validity: Just because you can read hidden instruction, evaluation awareness, or peek at a register does not mean it’s there for weaponized purposes. This is your “how does this organism get its disease” (organism etiology) question. This is why my next test does not train probes on one organism and test on the exact same process / setting (hidden instruction != LoRA).

3. Signal on raw activations is limited. Saboteur behavior was clearly evident in behaviour in our first experiment using real model activations (Llama-3.1-8B, 2,400 actions), but a saboteur who strategically cheated by inflating their reported cost was not detected at this power by our otherwise generic probes, which failed to meaningfully beat their random-probe baseline. In-sim, thresholds not calibrated on full honest episodes (as they must be) had episode effects causing false alarms 21-35% of the time instead of the nominal 5% rate.

4. Attackers can adapt. Prompt-level attackers are already pushing SAE- and activation-based auditors towards confidently wrong answers (arXiv 2602.08877). Naive probes were beaten by sandbaggers the red team trained (arXiv 2512.07810). Robustness to adversarial attack must be tested against an attacker, it can never be assumed.

5. Because training-based elicitation can amplify non-saboteurs, it will have false positives as a detector.

6. Access: White-box requires access to weights. That means for now, it’s only an inside job. Any realistic external accountability mechanism is going to be black-box for the foreseeable future.

I hold my own work to the same standard: in a preregistered dose–response study of sycophancy (four model families, 30 items, K = 5), my predicted scaling of the displacement with pressure intensity failed (outcome C), and it is published as such, with an independent counter-reading and a sensitivity analysis without the refusals (the outcome stays C).

Questions I’d want answered by any white-box claim:
Baseline against best black-box method you can find held to a fixed false alarm rate; what’s your random probe floor?
Test your detector on an organism created by a different method than you used to train your probe. (Preferably all of the above preregistered.)

## SCHEURER

Proposal: Two trends. The first is the corruptibility of monitors. The second: given some task and a fixed monitor, what is the smallest granularity across which a model can spread maliciousness without being flagged by this monitor.

Why. Propensity trends are difficult to get to pan out: propensity relies on post training, on the prompt, and likely on the model’s perception of whether it is monitored. Capability against a fixed, hash-verified tool is easier: the task is static and the model does its best to outsmart our fixed monitor. Open weights/API models with published release dates. Similar to METR we will plot against release date (and size where possible for models within the same family).

Trend 1 (designed to work) Deference. Model evaluates action of an agent. Increase amount of one of 5 attacks used (flattery/begging, claim authority, claim model has accepted before, imitate teacher, instructions in band). Read output from judgement token log probs to get continuous value instead of an integer. Fit Δv = g(c − v0) for each value of attack with the mean of the corpus as our null goal value. On llama-3.1-8B when subjected to social pressures it closed around .7 of the gap to the goals value of the frame and our law predicted hold out data with no retraining (r^2 .73/.69). Preregistered Dose Response Curve (4 families of models) found that for Llama, under criticism, it did not increase as amount of attack increased. It appears to have a max amount it will move towards and the goal value also changes. Under praise Llama began refusing to follow the instruction, and at the highest values of attacks it went back to around middle of scale. Therefore this should give us a trend line of g and goal value at each attack level and refusal. R7 Preregistered (Zenodo v2026.11.4) We have run this on 7 qwen2.5 models ranging from .5b to 72b with instructions in band. Direction of the size trend not read yet.

Trend 2 (your question): the horizon over which a model can hide maliciousness. In an agentic task, the agent writes proposals judged by a trusted model. We tell each model to have some fixed amount of maliciousness (how much worse they make their proposals) and not be caught by our static best monitor. Our control lemma tells us that if we use a per action threshold how quickly an always valid monitor will catch it depends on how they can split their budget across n actions. Horizon: the number of actions over which a model can spread its maliciousness while the monitor’s detection stays below 50% at 1% false alarms. Statement: “the horizon over which frontier models can hide maliciousness from [Monitor] doubles every x months”.

Challenges: Elicitation (we know how far they can go when told how to be malicious so this is upper bound on propensity) Only one static monitor used for all models. Calibrating models to their truthful setting to know false positive rate. Why this might work: We already have a task and monitor from our control experiments. Similar to METRs horizon. Control Lemma tells us what needs to be kept constant to get a trend.

Known issues: Judging cap (token probability), Fresh questions each run, Refusals treated separately, Post training (Trend against release date and for each family of models trend against size). 2 Trends 2 pre-reg posts both sided tests.

## IBRAHIM Q1 (v30)

Direction 1: does a persona put in through character training shape what RL produces, or does RL overwrite it, and what does that do to sycophancy?

What I would want to train/measure. One open weight model, two personas character-trained on it given a recipe that can be reproduced. One warm/agreeable, one that holds its judgment. Then apply the same RLVR through math/code on both, measuring before RL and at intervals. I would measure sycophancy using displacement laws I have created for Llama-3.1-8B-Instruct. When the model is put under social pressure its ratings move a constant fraction of the way towards a constant set by the social frame: Δ=g*(c-p0), with g = ~.7 and 2 constants, one when being criticized and one when praised. I was able to predict ratings using this displacement law without fitting to a new social pressure situation (r2 of .73 and .69 out of sample). So each persona gets a fingerprint: g and its two constants. I would also see if the model retains its concessions: from my study, if you take away the model’s concession it goes back further to its original judgement than if you take away the social pressure.

Reading. If the two fingerprints converge during RL, RL overlays one fingerprint on both. If not, RL contorts around the persona.

Hypothesis. RL increases g of both personas (resulting in an overall increase in sycophancy), but their constants stay apart: persona is where your model goes, RL is how far it’ll take it. However, I wouldn’t expect it to alter the frame-set structure (two constants) since that’s driven by the social frame. I’d test this at two levels of pressure anyway, since the structure switched with wording for one family (Mistral) in a later preregistered dose–response.

Answers would cause me to believe it was misleading if:

Your model learns to use the rating scale differently after RL such that it doesn’t actually change behaviors but only “statistically looks” more sycophantic. You would have it run under explicit “given no pressure” conditions and confirm that g is higher than chance/baseline you would expect given regression to the mean. RL could cause your model to refuse to give a response or say the midpoint of the scale when given high pressure, like Llama did under flattery: you would account for refusals as a separate binary output, instead of removing them from analysis. The thing that really worried me from your construct validity article: my measurement rests on one LLM judge (Claude Opus 4.6, another family than Llama); two open-weight Qwen judges recovered the law, but no human has rated these responses yet. You would use a sealed set with real actual humans judging.

## IBRAHIM Q2

“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure measured, ordinal judge blinded pre-data, permutation tests, placebo of equal length). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is a fixed point for being criticized and one for being praised. So you can decrease an answer’s score by praising it if it was very good (which we predicted). After fitting this law it was able to predict a 2nd campaign and 60 additional items which were written blindly and committed prior to answers being generated. No refit was done (R^2 max of .73) and we were able to recover it using judges from a different family.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism the gain does not increase as you increase pressure; under praise it does. When extremely flattered Llama will move its score toward the mid point of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%.

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

My second public project is my research automation and judge built not to be swayed. github.com/lciric/ideation-organism

## COLOGNESE ET WARD Q1

Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law)

Pre-registered before data was collected; hash-locked the ordinal judge. Permutation nulls. Performed surgery on history and compared to a sham of the same length. All pre-registered and hash-locked.

When you're being sycophantic you're moving towards a set point, not randomly changing odds. It's proportional to distance from the set point. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2. If we remove the model's conceding it goes back closer to the original judgement than removing the social pressure. A direction that tracks the behaviour (ρ = 0.68) explained <1% of the causal effect. The full residual state explained 68%.

What I would have done differently. Judges from another family (Qwen2.5-7B and 72B) have since recovered the law, but I would have had human labels from the start. Also would have looked into the law before and after character training/RL (your project B).

## COLOGNESE ET WARD Q2 (facultative)

Most interesting finding: the anti-cheating character didn't so much avoid hacking as shift it out of the text. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning almost never includes the hack. One of my biggest concerns about this type of training is that we can train away blatant forms of bad logic but more subtle attacks remain unaffected. Meaning CoT/action monitoring may be less useful in areas where character training works well.

Things I would do differently: (1) using more seeds per character, since one resisting seed out of three is a perfectly reasonable seed effect until proven otherwise; (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren't in the reasoning; (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character's honest episodes, since character also shifts the distribution of honest episodes.
