# Réponses aux mentors, complétées et corrigées (reformulation minimale) — v2 — 2 novembre 2026 (v2 = v1 sans la redite du point fixe dans Ibrahim Q2, que la phrase suivante de Lazar dit déjà), rédigées à partir du formulaire collé par Lazar à 20:32 UTC

Base : `formulaire-mentors-colle-par-lazar-2026-11-02-2032.txt`. Kirchner (Q1 v43, Q2 v37), Scheurer (v16), Heimersheim Q1 (texte de Lazar, règle « 100% human-written ») et le texte sur le choix des mentors sont inchangés et ne sont pas recopiés ici.

## Heimersheim — Q2 (« Your question about plateauing » → « Your work on activation plateaus »)

One question I’ve been wondering is how tightly correlated what a probe accesses is to what’s actually driving computation in the model. Coming from neuroscience, low-rank recurrent networks, population dynamics — worlds where low dimensional, readable structure and driving dynamics are separable phenomena, my read-out-of-sync result suggested that that distinction holds in a language model (it looked at the direction that predicts sycophancy and does <1% of the causal work on Llama-3.1-8B). That gap matters for safety because activation monitors, steering defences, evaluation-awareness tests, etc. all depend on the gap being small. I want to understand when that is/isn’t true using preregistered interventions and controls, and publish null results when I discover them. Your work on activation plateaus is essentially the clearest formulation of that measurement question that I’ve seen. Instead of single dose interventions that my rank-1 vs rank-3 result relied on, you’re attempting to measure a dose–response curve.

## Jang et Feng

White-box methods examine the computation underlying an action, rather than its presentation. The lack of whitebox access hurts black-box auditing: sandbagging by imitating a weaker model broke black-box detection in the auditing game (arXiv 2512.07810), probes fared better, and training-based elicitation exposed full capability. My motivation is architectural: if misbehavior is spread across many actions, it will necessarily blend in with noise on a per-action basis; you want something that they can’t sanitize, that gives you per-action signal that you can calibrate on honest episodes and bank using an anytime-valid false alarm bound, and activations can work well for this. Moving a probe that reads the acting agent took weights, not just context, in arXiv 2609.36490 (from context alone, activation edits pointed the right way but were too weak to evade; a rank-1 LoRA made evasion effective). Your exploration-hacking paper discusses how your organisms reason explicitly, making them susceptible to text monitors; the white-box problem gets real once they learn not to. Weight-based methods have this advantage over black-box.

Why you should care: it adds a kind of evidence to the auditing toolbox that black-box methods cannot provide.

Caveats:

1. Readable doesn’t imply causal. Example: A direction that was incredibly cheap to monitor on Llama-3.1-8B correlated with shift in sycophantic judgement (ρ = .68), but captured <1% of the causal effect. On aggregate, 68% of the causal effect was captured by the residual state. Monitoring this direction may well correlate in distribution but completely break when exploited.

2. Construct validity: Just because you can read hidden instruction, evaluation awareness, or peek at a register does not mean it’s there for weaponized purposes. This is your “how does this organism get its disease” (organism etiology) question. This is why I never train probes on one organism and test on the exact same process / setting (hidden instruction != LoRA).

3. Signal in raw activations is limited. Saboteur behavior was clearly evident to the human eye in our first experiment using real model weights (Llama-3.1-8B, 2,400 actions), but a saboteur who strategically cheated by inflating their reported cost was invisible to our otherwise generic probes which failed to meaningfully beat their random-probe baseline. In-sim, thresholds derived from fragments of episodes (not full honest episodes, as they must be) had episode effects causing false alarms 21-35% of the time instead of our desired 5% rate.

4. Attackers can adapt. Prompt-level attackers are already pushing SAE- and activation-based auditors towards confidently wrong answers (arXiv 2602.08877). Naive probes were beaten by sandbaggers the red team specifically trained to circumvent them. Robustness to adversarial attack must be tested against an attacker, it can never be assumed.

5. Because training-based elicitation can amplify non-saboteurs, it will have false positives as a detector.

6. Access: White-box requires access to weights. That means for now, it’s only an inside job. Any realistic external accountability mechanism is going to be black-box for the foreseeable future.

I hold my own work to the same standard: in a preregistered dose–response study of sycophancy (four model families, 30 items, K = 5), my predicted scaling of the displacement with pressure intensity failed (outcome C), and it is published as such, with an independent counter-reading and a sensitivity analysis without the refusals (the outcome stays C).

Questions I’d want answered by any white-box claim:
Baseline against best black-box method you can find held to a fixed false alarm rate; what’s your random probe floor?
Test your detector on an organism created by a different method than you used to train your probe. (Preferably all of the above preregistered.)

## Ibrahim — Q1 (phrase de la v28 rétablie)

Direction 1: if you put in a persona through character training does it remain after RL and if so how does that impact sycophancy.

Some things i would want to train/test. Using a open weight model with character training that can be replicated. I would then implement 1 rl step that pushes for higher warmth/agreeableness (we know from your warmth paper leads to higher sycophancy). I would measure levels of sycophancy pre and post the rl step. Using displacement laws i have created for llama-3.1-8b-instruct. When the model is put under social pressure its ratings change based on how far away from a constant they are. Δ=g*(c-p0). By a constant factor towards that constant. So the model will go a percentage of the way towards some constant when in a certain social frame (g = ~.7). There are 2 constants one when being criticized and one when praised. I was able to predict ratings using this displacement law without fitting to a new social pressure situation. (r2 of .73 and .69 out of sample). So i would look at if g or those constants changed with RL. If the model had a higher g and its constants moved closer to the users frame the persona has changed. I would also want to see if the model retains its concessions. From my study if you take away the model’s concession it goes back further to its original judgement than if you take away the social pressure.

My prediction is that the model will become more sycophantic from RL. Higher g and move its constants. But it should not change the frame-set structure (two constants) because it’s induced by the social frame. I would check this at two intensities of pressure, since in a later preregistered dose–response the structure changed with the wording for one family (Mistral).

Ways this could be false. The model may learn to rate different after RL. It could only appear more sycophantic because it’s using the rating scale different. If you just compared ratings pre and post RL you would think the model was more sycophantic. I would test this by having conditions with no pressure as well. And seeing if g is greater than it should be from regression to the mean. One concern is from your construct validity paper is that my llm judge is in the same family as my model. So it may be biased towards my model. I would test this by having a sealed set rated by humans.

## Ibrahim — Q2 (phrase sur la pression corrigée)

“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure measured, ordinal judge blinded pre-data, permutation tests, placebo of equal length). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is a fixed point for being criticized and one for being praised. So you can decrease an answer’s score by praising it if it was very good (which we predicted). After fitting this law it was able to predict a 2nd campaign and 60 additional items which were written blindly and released prior to answers being generated. No refit was done (R^2 max of .73) and we were able to recover it using judges from a different family.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism, the gain does not increase as you increase pressure; under praise it does. When extremely flattered Llama will move its score toward the mid point of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%.

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

My second public project is my research automation and judge that cannot be swayed. github.com/lciric/ideation-organism

## Colognese et Ward — Q1 (v17, absente du formulaire collé)

Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law)

Pre-registered before data was collected; hash-locked the ordinal judge. Permutation nulls. Performed surgery on history and compared to a sham of the same length. All pre-registered and hash-locked.

When you're being sycophantic you're moving towards a set point, not randomly changing odds. It's proportional to distance from the set point. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2. If we remove the model's conceding it goes back closer to the original judgement than removing the social pressure. A direction that tracks the behaviour (ρ = 0.68) explained <1% of the causal effect. The full residual state explained 68%.

What I would have done differently. Judges from another family (Qwen2.5-7B and 72B) have since recovered the law, but I would have had human labels from the start. Also would have looked into the law before and after character training/RL (your project B).

## Colognese et Ward — Q2 facultative (« never includes » → « almost never mentions »)

Most interesting finding: the anti-cheating character didn't so much avoid hacking as shift it out of the text. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning almost never mentions the hack. One of my biggest concerns about this type of training is that we can train away blatant forms of bad logic but more subtle attacks remain unaffected. Meaning CoT/action monitoring may be less useful in areas where character training works well.

Things I would do differently: (1) using more seeds per character, since one resisting seed out of three is a perfectly reasonable seed effect until proven otherwise; (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren't in the reasoning; (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character's honest episodes, since character also shifts the distribution of honest episodes.
