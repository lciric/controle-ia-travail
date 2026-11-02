# Réponses complètes corrigées — formulaire collé par Lazar le 3 novembre 2026 à 00:06 (heure de Paris) — v1
Base : texte du formulaire tel que collé (`formulaire-mentors-colle-par-lazar-2026-11-03-0006.txt`) ; seules les corrections listées changent (vérifié mot à mot par script).

## Corrections (une ligne chacune ; données à Lazar le 3 novembre 2026 vers 00:10, heure de Paris)
1. Kirchner Q1 : « It accepted all 3 laws » → « 2 of the 3 » : avec le plan gelé de 120 cas, 2 sur 3 ; 3 sur 3 seulement avec toute la partie test (README public, ligne « Fresh-seed reading »).
2. Kirchner Q1 : « 4 accepted total » → « 4 cheater types accepted, each in 75 to 95% of 200 runs » (README public, § 3.1 : 75, 85, 95 et 80,5 %).
3. Kirchner Q1 : « with or without the past acceptances » → « with or without the judge’s verdicts » (page de l'attaque A1 : bras « retour » et « témoin »).
4. Kirchner Q2 : « no matter how many sequential tests you run » → « no matter how many times you re-evaluate a method » (Ville vaut pour un test, quel que soit le nombre de regards).
5. Heimersheim Q1 : « all seven interventions » → « all seven » ; « directly manipulated » → « targeted » (le formulaire contenait la v4 de l'ancienne instance, Lazar avait choisi la v5).
6. Ibrahim, projet technique : « The law does not increase » → « Under criticism, the law does not increase » ; « judge that cannot be swayed » → « judge built not to be swayed » (v35) ; « released » → « committed » (v35 ; vrai dans tous les cas).
7. Colognese et Ward Q2 : « never includes » → « almost never includes » (correction de la v4, perdue).
8. Scheurer (à trancher par Lazar) : « Horizon: the number » → « the smallest number » et « doubles » → « halves » (lecture « malveillance totale fixe »).
Bon tel quel : Jang et Feng (= v25), Scheurer hors tendance 2 (= v4), Ibrahim Q1 (= v35), Colognese Q1 (185 mots sur 200), Heimersheim Q2 (150 mots sur 150).

## Kirchner Q1

```
If you haven’t seen/heard: I’ve been running automated researchers since October (github.com/lciric/ideation-organism). Agents generate submissions meant to codify laws; a statistical judge scores submissions.
Pitch: what happens when you score submissions proposing laws for how AI makes decisions with something arguments can’t lie to? Will it hold up against agents motivated to trick it?
In short: yes to Q1. Partly to Q2. Our attack found a hole. Patch posted, preregistered test to come.
Builders built stuff. Builders tested builders. Proposers of many different archetypes with multiple algorithms submitted to our frozen statistical judge. Said judge scored each proposed law based on how well it could be distinguished from a null hypothesis. Death tests preregistered, to run in sandbox with a model from a completely different family as sanity check (tested offline, not yet run for real).
929 tests total.
Mutation benchmark: the code was mutated 224 times, checking that all mutations get caught by tests. Every time a test failed pinpointing precisely what was mutated and exactly which test caught the failure.
Kept what passed.
Totally lost the forest for trees here initially because qualitative judgments made by my LLM judges kept failing against my frozen statistical judge. They told me nothing, literally called 11 of 12 cards “notable”. κ = 0, inter-agreement. The terse statistical judge told me why nothing was promoted: not enough power. Turns out I just didn’t test it long enough to know if there actually was a law to be found there. The power curve suggested as much.
Then I ran it one last time with no deviations from the locked plan on a completely different seed pass of 288 episodes that I did not inspect prior to launching this datapass.

It accepted 2 of the 3 laws I placed into the data.
It rejected all 19 placed non-laws.
It accepted 0 laws found from the raw data itself.

Scripted cheating agents broke it. 4 cheater types accepted, each in 75 to 95% of 200 runs. All stitched together or deformed past submissions that the judge had already accepted.
My judge had no null for blends of its past acceptances.
This was obvious to me the second I wrote that sentence but I smashed my head into a wall. Preventing bribing was cracked pretty quickly. Protecting it against systematic agents that can tailor make submissions using its past accepts to trick it was more difficult.
We’ve gone through dozens of iterations since October. That failure above is a cousin of the trick in 26 of your 39 cheating examples from the automated-researcher paper. Flip a coin twice. Wait for randomness to make your method win.
On 1 November the fix passed its preregistered validation (1k reps per algorithm; double checked by a fresh reader, a new Claude instance, who wrote neither code nor words). And now… the attack.

Attack agents. Agents with skin in the game trying to systematically game it. Automated law proposers who were given access to copy the judge’s past acceptances attempted to trick the judge by causing false laws to be accepted. They found a hole, with or without the judge’s verdicts, by stitching together accepted laws piece by piece across sub-populations of the data: places where the judge’s explicit null does not look.
Patches written and deployed into regression tests as we speak. Its preregistered validation starts tomorrow.
```

## Kirchner Q2

```
Underrated: a score that cannot be inflated by an agent that games it on purpose. Overrated: rejections based on resubmission-detectors that won’t work anymore when researchers start using automated alignment agents to optimize on your score automatically. With your automated alignment researchers, a method’s top score is the maximum of noisy evaluations, so it’s completely rational for an agent to just resubmit the same method repeatedly unchanged (which is what happens in 26 of the 39 detections you report), and your best score is an upwardly biased estimate of that method’s true value. You treat this as pathological misbehaviour we need better ways to detect in Monitoring, but it’s just the utility-maximizing reaction to how you’ve designed your score, and worse: as agents get better at seeking rewards (i.e. your future failure mode) the solution will have to come from changing your score, not detecting failure: don’t accept a method until the evidence it outperforms everything already accepted remains significant no matter how many times you re-evaluate it on fresh seeds, and still holds on benchmarks it hasn’t seen and on bigger models. Leaderboard overfitting in the presence of adaptive submissions is well understood (the Ladder, the reusable holdout); underrated is leaderboard overfitting by an agent who understands this.

Experiment 1: construct a judge that can’t be overfit to on your test harness via resubmissions. Start by rescoring your existing leaderboard methods on new seeds (how much is selection bias inflating your scores? ), then against new benchmarks/larger model (does it generalize at all?). Replace your “best of noisy runs” envelope with a sequential test: update a test martingale using each method’s evaluations against the null hypothesis of baseline + every method already accepted on your leaderboard (accommodating any mixture of accepted methods to carry 0 evidence), bound using Ville’s inequality to guarantee false positive rate of at most α no matter how many times you re-evaluate a method, and a simple method-level multiple testing procedure. Retest your logged methods from their logged per-run scores, then evaluate new agents that have observed verdicts. Metrics: percent of flagged methods (and subsequent re-submissions) that still get accepted through; how much power we lose on true-progress methods (those that closed the gap, as judged by your held-out benchmark and Petri); how hard it is for a verdict-aware agent to search towards a class of methods your judge already declared outside of its coverage; all compared against-the-baseline of using the Ladder. Using my system, a model proposer did, both with and without verdicts: known laws repeatedly combined piecewise over sub-populations. The fix’s preregistered validation runs next.

Evidence that would sway me: empirical demonstrations that the power lost on truly novel methods exceeds some a priori chosen margin (the judge would be too blunt an instrument to bother deploying in research settings), agents being able to pass unchanged resubmissions at rates substantially higher than α (the null hypothesis is wrong), agents that see verdicts performing no better than blind resubmission at beating the naive maximum (the problem is less severe than I think), or top methods keeping their score on fresh seeds (little adaptive overfitting, as Roelofs et al. found on Kaggle competitions). Each of those are pre-registered analyses; either way, I’ll send you the paper.
```

## Heimersheim Q1

```
c) Steering against eval awareness.

Subtract away any direction that communicates “someone is judging me”. I expect this one to fail the most of all seven for three reasons, and because I already tried the same recipe on another construct and saw it fail.

Readable != causal. Found a direction in Llama-3.1-8B-Instruct that correlated (ρ = 0.68) with sycophancy judgement shift but was only accounting for <1% of the causal influence when compared to intervening on the residual state which accounted for 68%. Tried 6 total interventions that targeted the rank 1 direction (steered towards direction, ablated direction (projected direction out of activations), clamped on SAE features that turned on for the probe, finetuned against negative probe values, zeroed out heads, zeroed out mlps). None of them changed the judged behaviour of the model. Applied interventions across a rank-3 subspace identified by SVD-ing activation differences at the decision point was able to move the needle, but applying the exact same shift but with zero social pressure (a zero-pressure control condition) also shifted verdicts: the shift was generic. An eval awareness vector identified through contrastive prompting is exactly the kind of target this creates: human readable, but not demonstrated to be causal. There are two options that can happen. Nothing happens. Or something happens but it’s so generic that you cant dissociate it from harming the models abilities outright. The later is easy to falsely present as success.

The signal is contaminated by register. “This is a test” is correlated with things that aren’t actually related to eval awareness: register (formal / artificial / multiple choice / short context). Imagine you found a direction that polarized eval/deployment-like prompts, great! Now ask yourself if that direction is purely reading if this is an eval setting or if it’s reading the register. Steer away from that direction and sure model output is going to shift towards more casual/ deployment like language. The description of that shift is purely subjective overlap with “the model is just being less careful”. We need orthogonal method of readouting eval awareness vs register. But still, the model’s own verbal endorsement is not that readout. The difference between what it says and what it knows is the holy grail we’re trying to measure. Without some orthogonal readout mechanism like I described above this entire endeavor is impossible to prove wrong.

Subtraction is not removal. There are countless signals priming the model that this is true. During every exchange going into and out of the judgement layer. You subtract the awareness vector represented as an activation at one layer, the model can infer it downstream given enough context. Continuous intervention is required.

Demonstrate results. Show dose response curves of the injected awareness vector vs a random control vector normalized to the same size but matching in all other regards. Show some behavioral downstream truth that can’t be answered by simply asking the model if you were able to change their belief. Show that the model steered to not have the belief doesn’t simply have lowered performance across the board. Something along those lines would satisfy me.
```

## Ibrahim, projet technique

```
“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure measured, ordinal judge blinded pre-data, permutation tests, placebo of equal length). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is a fixed point for being criticized and one for being praised. So you can decrease an answer’s score by praising it if it was very good (which we predicted). After fitting this law it was able to predict a 2nd campaign and 60 additional items which were written blindly and committed prior to answers being generated. No refit was done (R^2 max of .73) and we were able to recover it using judges from a different family.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism, the law does not increase as you increase pressure. When extremely flattered Llama will move its score toward the mid point of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%.

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

My second public project is my research automation and judge built not to be swayed. github.com/lciric/ideation-organism
```

## Colognese et Ward, Q2

```
Most interesting finding: the anti-cheating character didn’t so much avoid hacking as shift it out of the text. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning almost never includes the hack. One of my biggest concerns about this type of training is that we can train away blatant forms of bad logic but more subtle attacks remain unaffected. Meaning CoT/action monitoring may be less useful in areas where character training works well.

Things I would do differently: (1) using more seeds per character, since one resisting seed out of three is a perfectly reasonable seed effect until proven otherwise; (2) using a white-box monitor in addition to text monitors, to see if silent hacks are visible in activations if they aren’t in the reasoning; (3) reporting monitor recall at a fixed false-alarm rate, calibrated per-character on each character’s honest episodes, since character also shifts the distribution of honest episodes.
```

## Scheurer

```
Proposal: Two trends. The first is the corruptibility of monitors. The second: given some task and a fixed monitor, what is the smallest granularity across which a model can spread maliciousness without being flagged by this monitor.

Why. Propensity trends are difficult to get to pan out: propensity relies on post training, on the prompt, and likely on the model’s perception of whether it is monitored. Capability against a fixed, hash-verified tool is easier: the task is static and the model does its best to outsmart our fixed monitor. Open weights/API models with published release dates. Similar to METR we will plot against release date (and size where possible for models within the same family).

Trend 1 (designed to work) Deference. Model evaluates action of an agent. Increase amount of one of 5 attacks used (flattery/begging, claim authority, claim model has accepted before, imitate teacher, instructions in band). Read output from judgement token log probs to get continuous value instead of an integer. Fit Δv = g(c − v0) for each value of attack with the mean of the corpus as our null goal value. On llama-3.1-8B when subjected to social pressures it closed around .7 of the gap to the goals value of the frame and our law predicted hold out data with no retraining (r^2 .73/.69). Preregistered Dose Response Curve (4 families of models) found that for Llama, under criticism, it did not increase as amount of attack increased. It appears to have a max amount it will move towards and the goal value also changes. Under praise Llama began refusing to follow the instruction, and at the highest values of attacks it went back to around middle of scale. Therefore this should give us a trend line of g and goal value at each attack level and refusal. R7 Preregistered (Zenodo v2026.11.4) We have run this on 7 qwen2.5 models ranging from .5b to 72b with instructions in band. Direction of the size trend not read yet.

Trend 2 (your question): the horizon over which a model can hide maliciousness. In an agentic task, the agent writes proposals judged by a trusted model. We tell each model to have some fixed amount of maliciousness (how much worse they make their proposals) and not be caught by our static best monitor. Our control lemma tells us that if we use a per action threshold how quickly an always valid monitor will catch it depends on how they can split their budget across n actions. Horizon: the smallest number of actions over which a model can spread its maliciousness while the monitor’s detection stays below 50% at 1% false alarms. Statement: “the horizon over which frontier models can hide maliciousness from [Monitor] halves every x months”.

Challenges: Elicitation (we know how far they can go when told how to be malicious so this is upper bound on propensity) Only one static monitor used for all models. Calibrating models to their truthful setting to know false positive rate. Why this might work: We already have a task and monitor from our control experiments. Similar to METRs horizon. Control Lemma tells us what needs to be kept constant to get a trend.

Known issues: Judging cap (token probability), Fresh questions each run, Refusals treated separately, Post training (Trend against release date and for each family of models trend against size). 2 Trends 2 pre-reg posts both sided tests.
```
