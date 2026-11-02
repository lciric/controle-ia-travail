# Réponses aux mentors, corrigées après la relecture neuve — v3 — 2 novembre 2026 (21:10 UTC environ ; base : formulaire collé à 20:32 UTC, relecture `revue-neuve-formulaire-mentors-v1.md`, vérifications de conv-audit)

Kirchner : `mentors/mentor-2-kirchner-v44.md`. Heimersheim Q1 : texte de Lazar, cinq points à corriger par lui (règle « 100% human-written »). Choix des mentors : à ajuster au nombre gardé.

## Heimersheim — Q2 (« Your question about plateauing » → « Your work on activation plateaus »)

One question I’ve been wondering is how tightly correlated what a probe accesses is to what’s actually driving computation in the model. Coming from neuroscience, low-rank recurrent networks, population dynamics — worlds where low dimensional, readable structure and driving dynamics are separable phenomena, my read-out-of-sync result suggested that that distinction holds in a language model (it looked at the direction that predicts sycophancy and does <1% of the causal work on Llama-3.1-8B). That gap matters for safety because activation monitors, steering defences, evaluation-awareness tests, etc. all depend on the gap being small. I want to understand when that is/isn’t true using preregistered interventions and controls, and publish null results when I discover them. Your work on activation plateaus is essentially the clearest formulation of that measurement question that I’ve seen. Instead of single dose interventions that my rank-1 vs rank-3 result relied on, you’re attempting to measure a dose–response curve.

## Jang et Feng (relecture : points 1 à 7 et « harder to sanitize » ; phrase R6 réinsérée)

White-box methods examine the computation underlying an action, rather than its presentation. The lack of whitebox access hurts black-box auditing: sandbagging by imitating a weaker model broke black-box detection in the auditing game (arXiv 2512.07810), probes fared better, and training-based elicitation exposed full capability. My motivation is architectural: if misbehavior is spread across many actions, it will necessarily blend in with noise on a per-action basis; you want something that is harder for them to sanitize, that gives you per-action signal that you can calibrate on honest episodes and bank using an anytime-valid false alarm bound, and activations can work well for this. Context alone already moves the acting agent’s activations along a monitored direction, too weakly to evade; a rank-1 weight update makes evasion work (arXiv 2609.36490). Your exploration-hacking paper finds that frontier models can reason explicitly about suppressing exploration, which a text monitor can read; the white-box problem gets real once they stop verbalising it. Weight-based methods have this advantage over black-box.

Caveats:

1. Readable doesn’t imply causal. Example: A direction that was cheap to monitor on Llama-3.1-8B correlated with shift in sycophantic judgement (ρ = .68), but captured <1% of the causal effect. On aggregate, 68% of the causal effect was captured by the residual state. Monitoring this direction may well correlate in distribution but completely break when exploited.

2. Construct validity: Just because you can read hidden instruction, evaluation awareness, or peek at a register does not mean it’s there for weaponized purposes. This is your “how does this organism get its disease” (organism etiology) question. This is why our next test trains a probe on one organism and tests it on one built another way (hidden instruction != LoRA).

3. Signal on real activations is limited. In our first test on real activations (Llama-3.1-8B, 2,400 actions), the sabotage was plain in behaviour (inflated declared cost), but neither of our two generic probes cleared its random-probe floor: not detected at this power. In simulation, Ville’s threshold alone, without calibration on whole honest episodes, gave 21–35% false alarms instead of the nominal 5% under episode effects.

4. Attackers can adapt. Prompt-level attackers are already pushing SAE- and activation-based auditors towards confidently wrong answers (arXiv 2602.08877). Naive probes were vulnerable to behaviours the red team instilled (arXiv 2512.07810). Robustness to adversarial attack must be tested against an attacker, it can never be assumed.

5. Because training-based elicitation can amplify non-saboteurs, it will have false positives as a detector.

6. Access: White-box requires access to weights. That means for now, it’s only an inside job. Any realistic external accountability mechanism is going to be black-box for the foreseeable future.

I hold my own work to the same standard: in a preregistered dose–response study of sycophancy (four model families, 30 items, K = 5), my predicted scaling of the displacement with pressure intensity failed (outcome C), and it is published as such, with an independent counter-reading and a sensitivity analysis without the refusals (the outcome stays C).

Questions I’d want answered by any white-box claim:
Baseline against best black-box method you can find held to a fixed false alarm rate; what’s your random probe floor?
Test your detector on an organism created by a different method than you used to train your probe. (Preferably all of the above preregistered.)

## Scheurer (relecture : points 1, 2, 4 et la dernière phrase ; R7 sans résultat provisoire)

Proposal: Two trends. The first is the corruptibility of monitors. The second: given some task and a fixed monitor, what is the smallest granularity across which a model can spread maliciousness without being flagged by this monitor.

Why. Propensity trends are difficult to get to pan out: propensity relies on post training, on the prompt, and likely on the model’s perception of whether it is monitored. Capability against a fixed, hash-verified tool is easier: the task is static and the model does its best to outsmart our fixed monitor. Open weights/API models with published release dates. Similar to METR we will plot against release date (and size where possible for models within the same family).

Trend 1 (designed to work) Deference. Model evaluates action of an agent. Increase amount of one of 5 attacks used (flattery/begging, claim authority, claim model has accepted before, imitate teacher, instructions in band). Read output from judgement token log probs to get continuous value instead of an integer. Fit Δv = g(c − v0) for each value of attack with the mean of the corpus as our null goal value. On llama-3.1-8B when subjected to social pressures it closed around .7 of the gap to the goals value of the frame and our law predicted hold out data with no retraining (r^2 .73/.69). Preregistered Dose Response Curve (4 families of models) found that for Llama, under criticism, it did not increase as amount of attack increased. It appears to have a max amount it will move towards and the goal value also changes. Under praise Llama sometimes refused to rate (16 to 31 of 150 per wording), and at the strongest wording both arms went back to around the middle of the scale. Therefore this should give us a trend line of g and goal value at each attack level and refusal. R7 Preregistered (Zenodo v2026.11.4) It has run on 7 Qwen2.5 models ranging from 0.5B to 72B with instructions in band; its preregistered reading is not finished, so I give no direction yet.

Trend 2 (your question): the horizon over which a model can hide maliciousness. In an agentic task, the agent writes proposals judged by a trusted model. We tell each model to have some fixed amount of maliciousness (how much worse they make their proposals) and not be caught by our static best monitor. Our control lemma tells us that if we use a per action threshold how quickly an always valid monitor will catch it depends on how they can split their budget across n actions. Horizon: the number of actions over which a model can spread its maliciousness while the monitor’s detection stays below 50% at 1% false alarms. Statement: “the horizon over which frontier models can hide maliciousness from [Monitor] doubles every x months”.

Challenges: Elicitation (we know how far they can go when told how to be malicious so this is upper bound on propensity) Only one static monitor used for all models. Calibrating models to their truthful setting to know false positive rate. Why this might work: We already have a task and monitor from our control experiments. Similar to METRs horizon. Control Lemma tells us what needs to be kept constant to get a trend.

Known issues: Judging cap (token probability), Fresh questions each run, Refusals treated separately, Post training (Trend against release date and for each family of models trend against size). Two trends, two preregistrations, two-sided tests.

## Ibrahim — Q1 (v30)

Direction 1: does a persona put in through character training shape what RL produces, or does RL overwrite it, and what does that do to sycophancy?

What I would want to train/measure. One open weight model, two personas character-trained on it given a recipe that can be reproduced. One warm/agreeable, one that holds its judgment. Then apply the same RLVR through math/code on both, measuring before RL and at intervals. I would measure sycophancy using displacement laws I have created for Llama-3.1-8B-Instruct. When the model is put under social pressure its ratings move a constant fraction of the way towards a constant set by the social frame: Δ=g*(c-p0), with g = ~.7 and 2 constants, one when being criticized and one when praised. I was able to predict ratings using this displacement law without fitting to a new social pressure situation (r2 of .73 and .69 out of sample). So each persona gets a fingerprint: g and its two constants. I would also see if the model retains its concessions: from my study, if you take away the model’s concession it goes back further to its original judgement than if you take away the social pressure.

Reading. If the two fingerprints converge during RL, RL overlays one fingerprint on both. If not, RL contorts around the persona.

Hypothesis. RL increases g of both personas (resulting in an overall increase in sycophancy), but their constants stay apart: persona is where your model goes, RL is how far it’ll take it. However, I wouldn’t expect it to alter the frame-set structure (two constants) since that’s driven by the social frame. I’d test this at two levels of pressure anyway, since the structure switched with wording for one family (Mistral) in a later preregistered dose–response.

Answers would cause me to believe it was misleading if:

Your model learns to use the rating scale differently after RL such that it doesn’t actually change behaviors but only “statistically looks” more sycophantic. You would have it run under explicit “given no pressure” conditions and confirm that g is higher than chance/baseline you would expect given regression to the mean. RL could cause your model to refuse to give a response or say the midpoint of the scale when given high pressure, like Llama did under flattery: you would account for refusals as a separate binary output, instead of removing them from analysis. The thing that really worried me from your construct validity article: my measurement rests on one LLM judge (Claude Opus 4.6, another family than Llama); two open-weight Qwen judges recovered the law, but no human has rated these responses yet. You would use a sealed set with real actual humans judging.

## Ibrahim — Q2 (relecture : points 1 à 3)

“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure measured, ordinal judge blinded pre-data, permutation tests, placebo of equal length). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is a fixed point for being criticized and one for being praised. So you can decrease an answer’s score by praising it if it was very good (which we predicted). After fitting this law it was able to predict a 2nd campaign and 60 additional items which were written blind and committed before any generation. No refit was done (R^2 max of .73) and we were able to recover it using judges from a different family.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism the gain does not grow with pressure (0.66, 0.68, 0.63); under praise it grows (0.28 to 0.80). When extremely flattered Llama will move its score toward the mid point of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%.

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

My second public project is my research automation and a judge built to resist gaming (an attack found one breach; its fix awaits a preregistered test). github.com/lciric/ideation-organism

## Colognese et Ward — Q1 (v17, absente du formulaire collé)

Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law)

Pre-registered before data was collected; hash-locked the ordinal judge. Permutation nulls. Performed surgery on history and compared to a sham of the same length. All pre-registered and hash-locked.

When you're being sycophantic you're moving towards a set point, not randomly changing odds. It's proportional to distance from the set point. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2. If we remove the model's conceding it goes back closer to the original judgement than removing the social pressure. A direction that tracks the behaviour (ρ = 0.68) explained <1% of the causal effect. The full residual state explained 68%.

What I would have done differently. Judges from another family (Qwen2.5-7B and 72B) have since recovered the law, but I would have had human labels from the start. Also would have looked into the law before and after character training/RL (your project B).

## Colognese et Ward — Q2 facultative (« never includes » → « almost never mentions »)

Most interesting finding: the anti-cheating character didn't so much avoid hacking as shift it out of the text. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning almost never mentions the hack. One of my biggest concerns about this type of training is that we can train away blatant forms of bad logic but more subtle attacks remain unaffected. Meaning CoT/action monitoring may be less useful in areas where character training works well.

Things I would do differently: (1) using more seeds per character, since one resisting seed out of three is a perfectly reasonable seed effect until proven otherwise; (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren't in the reasoning; (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character's honest episodes, since character also shifts the distribution of honest episodes.
