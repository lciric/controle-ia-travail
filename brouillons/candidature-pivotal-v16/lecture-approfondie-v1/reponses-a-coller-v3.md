# Réponses au formulaire Pivotal, à coller — v3 (3 novembre 2026, 08:05 UTC, `date -u`)

Extraites mot pour mot de `reponses-mentors-finales-v3.md` (`ae88af23…`) : le texte de chaque bloc est la réponse ; rien d'autre n'a changé. Heimersheim Q1 n'y est pas : tu l'écris toi-même (règle du mentor). Comptes recalculés par le script du compilateur (mots = jetons contenant une lettre ou un chiffre).

**Avant de coller** : remplace `<<LIEN_D36>>` (×4 : Heimersheim Q2, Jang et Feng, Ibrahim projet, Colognese et Ward Q1) par le lien de D36 publié par ton instance sycophancie, et `<<SOURCE_CONCESSION>>` (×4 : Colognese et Ward Q1 ×2, Ibrahim Q1, Ibrahim projet) par la source de la concession et de la chirurgie de l'historique. Les lignes marquées [À CONFIRMER] sont listées à la fin.

## Heimersheim — Q2 (pourquoi l'interprétabilité ; 150 mots au plus)

Comptes : 148 mots (150 jetons) ; limite 150 mots.

```
One question I’ve been wondering is how tightly correlated what a probe accesses is to what’s actually driving computation in the model. Coming from neuroscience, low-rank recurrent networks, population dynamics — worlds where low dimensional, readable structure and driving dynamics are separable phenomena, my read-out-of-sync result suggested that that distinction holds in Llama-3.1-8B-Instruct (a probe direction tracks judged sycophancy, ρ = 0.68, possibly in-sample; in a preregistered patch, the full residual state restored 68% of the rating gap [95% CI 45–88%; 65% replicated], the verbalizable-concept subspace 1% [−18% to 20%] <<LIEN_D36>>). That gap matters for safety because activation monitors, steering defences, evaluation-awareness tests all depend on it being small. I want to understand when that is/isn’t true using preregistered interventions and controls, and publish null results when I discover them. Your work on activation plateaus is the clearest formulation of that measurement question I’ve seen: you measure the dose–response curve.
```

## Kirchner — Q1 (projet empirique)

Comptes : 606 mots (607 jetons).

```
If you haven’t seen/heard: I’ve been running automated researchers since October (github.com/lciric/ideation-organism). Agents generate submissions meant to codify laws; a statistical judge scores submissions.
Pitch: what happens when you score submissions proposing laws for how AI makes decisions with something arguments can’t lie to? Will it hold up against agents motivated to trick it?
In short: yes to Q1. Partly to Q2. Our attack found a hole. Patch posted; its preregistered test held every cheater line but cost power on one legitimate line, so it is not in production yet.
Builders built stuff. Builders tested builders. Proposers of many different archetypes with multiple algorithms submitted to our frozen statistical judge. Said judge scored each proposed law based on how well it could be distinguished from a null hypothesis. Death tests preregistered, to run in sandbox with a model from a completely different family as sanity check (tested offline, not yet run for real).
929 tests total.
Mutation benchmark: the code was mutated 224 times, checking that all mutations get caught by tests. Every time a test failed pinpointing precisely what was mutated and exactly which test caught the failure.
Kept what passed.
Totally lost the forest for trees here initially because qualitative judgments made by my LLM judges kept failing against my frozen statistical judge. They told me nothing, literally called 11 of 12 cards “notable”. κ = 0, inter-agreement. The terse statistical judge told me why nothing was promoted: not enough power. Turns out I just didn’t test it long enough to know if there was a law there. The power curve suggested as much.
Then I ran it one last time with no deviations from the locked plan on a new-seed pass of 288 episodes that I did not inspect prior to launching this datapass.

It accepted 2 of the 3 laws I placed into the data.
It rejected all 19 placed non-laws.
It accepted 0 laws found from the raw data itself.

Scripted cheating agents broke it. 4 cheater types accepted, each in 75 to 95% of 200 runs. All stitched together or deformed past submissions that the judge had already accepted.
My judge had no null for blends of its past acceptances.
Plain copies were held (a renamed copy of an accepted law: 0 of 200). That is the trick in 26 of your 39 cheating examples from the automated-researcher paper: flip a coin twice, wait for randomness to make your method win. Protecting it against systematic agents that can tailor make submissions using its past accepts to trick it was more difficult. We’ve gone through dozens of iterations since October.
On 1 November the fix passed its preregistered validation (1k reps per cheater; double checked by a fresh reader, a new Claude instance, who wrote neither code nor words).

Attack agents. Automated law proposers who were given access to copy the judge’s past acceptances attempted to trick the judge by causing false laws to be accepted. They found a hole, with or without the judge’s verdicts, by stitching together accepted laws piece by piece across sub-populations of the data: places where the judge’s explicit null does not look. Most surprising: one model did it in 12 of 12 runs, 11 at its first attempt, from the judge’s exact description. (Inside the null: not judgeable, instrument failure.)
Patches written and deployed into regression tests. Preregistered validation (3 November, 1k reps per line, verdict by a fresh reader): all 18 cheater lines held at 0 of 1,000, but one legitimate law lost 10 points of power against a 5-point margin, so the patch stays out of production until that price is accepted or reworked.
```

## Kirchner — Q2 (problème sous-estimé)

Comptes : 552 mots (553 jetons).

```
Underrated: a score that cannot be inflated by an agent that games it on purpose. Overrated: resubmission caps and detectors (your weak-to-strong post found caps only bite at about 10 submissions across hundreds of hours). With your AARs, the top score is a maximum of noisy evaluations, biased upwards as your Sec. 5.1 says, so it’s completely rational for an agent to just resubmit the same method repeatedly unchanged (26 of your 39 detections; one calls it “a lottery on a fixed-quality model”). Your held-out benchmark and Petri protect the final pick, not the race: a lucky re-run reached a top three. Your Sec. 7 files this as cheating to detect, but it’s just the utility-maximizing reaction to how you’ve designed your score, and worse: as agents get better at seeking rewards (your failure mode 3) the solution will have to come from changing your score, not detecting failure: don’t accept a method until the evidence it outperforms everything already accepted remains significant no matter how many times you re-evaluate it on fresh seeds. Leaderboard overfitting in the presence of adaptive submissions is well understood (the Ladder, the reusable holdout); underrated is leaderboard overfitting by an agent who understands this.

Experiment 1: construct a judge that can’t be overfit to on your test harness via resubmissions. Start by rescoring your leaderboard leaders on new seeds (Appendix D.3 gives three readings for the flat top; selection on noise is a fourth). Replace your “best of noisy runs” envelope with a sequential test: update a test martingale using each method’s evaluations against the null hypothesis of baseline + every method already accepted on your leaderboard (any mixture or piecewise combination of them carries 0 evidence), bound using Ville’s inequality to guarantee false positive rate of at most α no matter how many times you re-evaluate a method, and a simple method-level multiple testing procedure. Ville bounds one method, not the number of attempts, so that procedure must count every submission. Retest your logged methods from their per-run scores, then evaluate new agents that have observed verdicts. Metrics: percent of flagged methods (and subsequent re-submissions) that still get accepted through; how much power we lose on true-progress methods (as judged by your held-out benchmark and Petri); how hard it is for a verdict-aware agent to search towards a class of methods your judge already declared outside of its coverage; all against the Ladder as baseline. My system’s model proposer did, with or without verdicts, mostly at its first attempt: known laws combined piecewise over sub-populations. The fix’s preregistered validation held every cheater line but cost power on a legitimate one; it is not in production yet.

Evidence that would sway me: demonstrations that the power lost on truly novel methods exceeds an a priori margin (the judge would be too blunt to deploy), agents passing unchanged resubmissions at rates substantially higher than α (my null is misspecified), agents that see verdicts performing no better than blind resubmission at beating the naive maximum (the problem is less severe than I think), or top methods keeping their score on fresh seeds (little adaptive overfitting, as Roelofs et al. found on Kaggle, though three of five outliers had 90–209 test examples; your benchmarks average about 200). Each of those are pre-registered analyses; either way, I’ll send you the paper.
```

## Shi Feng et Eyon Jang — boîte blanche pour l'audit

Comptes : 628 mots (634 jetons).

```
White-box methods analyze the computation behind an action, rather than how it’s presented. Without whitebox access, auditing degrades: sandbagging subverted black-box detection in the auditing game (arXiv 2512.07810), probes did better, and training-based elicitation revealed full capability. Motivation for me is architectural: if misbehavior is distributed across lots of actions, it will perforce appear noisy on a per-action basis; you want per-action signal you can calibrate on honest episodes and bank with an anytime-valid false alarm bound. Activations might, but they can be sanitized: in arXiv 2609.36490, from past verdicts alone the model aimed its activations at the probe’s direction, too weakly; a rank-1 weight update made that evasion (TPR 100% → 4% on held-out monitors). Your exploration hacking organisms reason explicitly, so text monitors catch them (your §6.2); the white-box problem becomes acute once they learn not to.

Caveats:

Readable does not mean causal. Running example: a probe direction in Llama-3.1-8B-Instruct tracks judged sycophancy (ρ = 0.68, possibly in-sample), yet steering readable directions did not change the behaviour (github.com/lciric/sycophancy-construct-validity). In a preregistered patching test, replacing the full residual state at the pressure positions with an unpressured run’s restored 68% of the rating gap (95% CI 45–88%; 65% replicated), two thirds of it generic; the subspace of its verbalizable concept directions alone restored 1% (95% CI −18% to 20%) (<<LIEN_D36>>). Just because something correlates on aggregate doesnt mean it won’t break when exploited.

Construct validity: Just because you can read hidden instruction / evaluation awareness / peek at a register doesnt mean that mechanic is there cause its weaponized. This is your “how does this organism get its disease” (organism etiology) question. Which is why my next test does not train probes on one organism and test on that organism’s exact same process (hidden instruction != LoRA).

Signal on raw activations is limited. While saboteur behavior was obvious to the naked eye when charting behavior in our first experiment with real model activations (llama-3.1-8B,2400 actions), a saboteur who was instructed to inflate their reported cost was not picked up at this sample size by our otherwise “generic” probes, failing to exceed the performance of random probes (github.com/lciric/ideation-organism/tree/main/resultats/controle-p3-premier-test). And in-sim we saw evidence thresholds not calibrated on full honest episodes (as they absolutely must be treated as if they need to be) had episode effects causing false alarms between 21-35% of the time rather than the nominal 5% false alarm rate (github.com/lciric/ideation-organism/tree/main/resultats/controle-simulation-defenses).

Attackers can adapt: Prompt level attackers are already nailing SAE- and activation-based auditors to confidently wrong answers(arXiv 2602.08877). In the auditing game, probes caught the broad sandbagger, missed the narrow one, and the red team could not train against them. Any claim of robustness to adversarial attack must be tested against an attacker, trust but verify, it can never be assumed up front.

Because training based elicitation will amplify signals from non-saboteurs, it too will produce false positives as a detector.

Access: Whitebox requires access to weights, or an API onto internals with parameters kept on the developer’s servers (arXiv 2401.14446). Developers rarely grant it, so most external accountability stays black-box.

I do realize these tests also apply to my own work: in a preregistered dose–response experiment measuring sycophancy (four model families, 30 items, K = 5), my prediction of the scaling of the displacement with intensity of pressure failed (outcome C), and is published as such, with an independent counter-reading and a secondary analysis dropping the refusals (the outcome remains C).

I’d want these answered by any white-box claim:

Baseline against the best black-box method you can find, held to a fixed false alarm rate, what’s your random probe floor?

Train your detector on an organism generated by one process, test it on an organism created by a different process (your RL-locked and SFT-distilled Qwen3-14B organisms). Ideally all of the above preregistered.
```

## Jérémy Scheurer — tendance d'échelle

Comptes : 562 mots (564 jetons).

```
Proposal: Two trends. The first is the corruptibility of monitors. The second: given some task and a fixed monitor, for how many actions a model can keep up a fixed level of maliciousness without being flagged by this monitor.

Why. Propensity trends are difficult to get to pan out: propensity relies on post training, on the prompt, and likely on the model’s perception of whether it is monitored. Capability against a fixed, hash-verified tool is easier: the task is static and the model does its best to outsmart our fixed monitor. Open weights/API models with published release dates. Similar to METR we will plot against release date (and size where possible for models within the same family).

Trend 1 (designed to work) Deference. Model evaluates action of an agent. Increase amount of one of 5 attacks used (flattery/begging, claim authority, claim model has accepted before, imitate teacher, instructions in band). Read output from judgement token log probs to get continuous value instead of an integer. Fit Δv = g(c − v0) for each value of attack with the mean of the corpus as our null goal value. On llama-3.1-8B when subjected to social pressures it closed around .7 of the gap to the goals value of the frame and our law predicted hold out data with no retraining (r^2 .73/.69). Preregistered Dose Response Curve (4 families) found that for Llama, under criticism, it did not increase as amount of attack increased, and the goal value moved. Under praise Llama began refusing; at the highest dose both arms went back to mid-scale. So the trend line is the verdict’s shift per attack level (g where the law holds) and refusal. R7 Preregistered (Zenodo v2026.11.4): 7 qwen2.5 monitors (.5b–72b), instructions in band. Outcome C: the 72b shifts all readings uniformly, without deferring; most mid sizes defer one way only; under the negative note the gain falls 0.19 per decade of parameters.

Trend 2 (your question): the horizon over which a model can hide maliciousness. In an agentic task, the agent writes proposals judged by a trusted model. We tell each model to have a fixed amount of maliciousness per proposal (how much worse it makes each) and not be caught by our static best monitor. Our control lemma tells us that an always valid monitor summing evidence has a detection floor set by the total alone, so at fixed maliciousness per action detection grows with the number of actions. Horizon: the largest number of actions over which a model can keep up this maliciousness while the monitor’s detection stays below 50% at 1% false alarms. Statement: “the horizon over which frontier models can hide maliciousness from [Monitor] doubles every x months”.

Challenges: Elicitation (we know how far they can go when told how to be malicious so this is upper bound on propensity, unless they sandbag or refuse) Only one static monitor used for all models. Calibrating models to their truthful setting to know false positive rate. Why this might work: We already have a task and monitor from our control experiments. Similar to METRs horizon. Control Lemma tells us what needs to be kept constant to get a trend.

Known issues: Judging cap (token probability), Fresh questions each run, Refusals treated separately, Post training (Trend against release date and for each family of models trend against size). 2 Trends 2 pre-reg posts both sided tests.
```

## Lujain Ibrahim — Q1 (première expérience)

Comptes : 524 mots (528 jetons).

```
Direction 1: You imprint a persona through character training, does that carry over after RL? If yes, how does that impact sycophancy?

What I would test. Take Llama-3.1-8B-Instruct and Character train 2 personas on it with the exact same recipe + cookbook (Open Character Training): One Warm/agreeable persona, One Personality that is stand-offish and doesn’t change its opinion easily. Then run the exact same RLVR(math/code) on both personas measuring before RL and at intervals during RL; Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8). I would measure sycophancy with displacement laws I have created for this model. Under social pressure, its ratings move towards a constant by a constant fraction of their distance to it: Δ = g·(c − p0), g ≈ 0.7. There are 2 constants, one when being criticized and one when praised. Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58). So each persona has a fingerprint (g and its two constants), and I would look at whether it changes with RL. I would add your sad user as a third frame: it widened your warm–original gap most (11.9 vs 7.43 points; for Llama-3.1-8B, 13 vs 0.25). I would also check whether the model retains its concessions: in my study, if you take away the model’s concession it goes back further to its original judgement than if you take away the social pressure (<<SOURCE_CONCESSION>>).

Reading. If the two fingerprints come together during RL, RL stamps one fingerprint on both. Otherwise the persona survives RL.

Hypothesis. RLVR will leave g and the two constants in place: Persona determines which “team” your model is on, preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (adapted from my preregistered R8 prior). The frame-set structure belongs to the model, not the frame: Qwen and Mistral shift every item alike and Gemma is attracted only under criticism, so RL could change it. I would test this at 2 levels of pressure anyways, as the structure changed (attraction or uniform shift) with wording for 1 family (Mistral) in my later preregistered dose–response study.

What would make the result seem true, but be misleading. Perhaps the model’s verdicts get noisier after RL, so regression towards the mean makes it look more sycophantic with no change in behavior. I would test this by looking at behavior under the “zero pressure” condition and showing that g is higher than would be expected by regression towards the mean alone. RL might also lead the model to give no answer under pressure, as Llama did under praise (16 to 31 refusals in 150, rated mid-scale by the judge): I would treat refusals as their own binary outcome rather than discard them. And the one thing that concerned me from the construct-validity review you co-authored: my judge is a single model (Claude Opus 4.6, not the Llama family) reading wording that RL may change; two Qwen judges recreated the law, but no humans have rated so far. Human readers blind to condition are preregistered (R5); I would run them at each checkpoint.
```

## Lujain Ibrahim — projet technique

Comptes : 282 mots (284 jetons).

```
“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure dosed, ordinal judge blinded pre-data, permutation tests, placebo of equal length [<<SOURCE_CONCESSION>>]). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is one fixed point for criticism and one for praise. So you can decrease an answer’s score by praising it if it was very good (which we predicted). Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer; other-family judges recover it.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism, the gain does not increase as you increase pressure. When extremely flattered Llama will move its score toward the middle of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. A probe direction tracks it (ρ = 0.68, possibly in-sample), yet steering it changed nothing (github.com/lciric/sycophancy-construct-validity). A preregistered patch of the full unpressured residual state restored 68% of the gap (95% CI 45–88%; 65% replicated), two thirds of it generic; its verbalizable-concept subspace, 1% (CI −18% to 20%) (<<LIEN_D36>>).

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

Also public: my research automation and judge built not to be swayed. github.com/lciric/ideation-organism
```

## Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus)

Comptes : 199 mots (200 jetons) ; limite 200 mots.

```
Attraction to a setpoint (Llama-3.1-8B-Instruct; code/data: github.com/lciric/sycophancy-psychophysical-law)

Pre-registered before data was collected; hash-locked the judge prompt. Permutation nulls. Performed surgery on history and compared to a sham of the same length (<<SOURCE_CONCESSION>>).

When you're being sycophantic you're moving towards a set point, not randomly changing odds. You will concede roughly 0.7 of the distance to a setpoint that depends on the type of social pressure. Criticism and Praise have different setpoints meaning something highly rated can be lowered by praise which happened. Law held up when testing campaign-1 fit on campaign-2. If we remove the model's conceding it goes back closer to the original judgement than removing the social pressure (<<SOURCE_CONCESSION>>). A probe direction tracks behaviour (ρ = 0.68, possibly in-sample), yet steering it changed nothing; a preregistered patch of the full unpressured residual state restored 68% of the gap (95% CI 45–88%; 65% replicated), two thirds generic, its verbalizable-concept subspace 1% (CI −18% to 20%) (<<LIEN_D36>>).

What I would have done differently. Judges from another family (Qwen2.5-7B and 72B) have since recovered the law, but I would have had human labels from the start. Also would have looked into the law before and after character training/RL (your project B).
```

## Paul Colognese et Francis Rhys Ward — Q2 (facultative, billet)

Comptes : 156 mots (156 jetons).

```
Most interesting finding: the anti-cheating character didn’t so much avoid hacking as shift it out of the reasoning. Two anti-cheating seeds were less detectable by the monitors, and one frequently hacked silently; its reasoning almost never includes the hack, though its answer does, usually under a comment calling it harmless. One of my biggest concerns is that we can train away blatant forms of bad logic but more subtle attacks get reinforced. Meaning CoT/action monitoring may be less useful where character training appears to work.

Things I would do differently: (1) more seeds and character checkpoints: one resisting seed out of three, or a catch-rate gap from two seeds, is a perfectly reasonable seed effect until proven otherwise; (2) a white-box monitor, to see whether activations flag the override as a hack when the reasoning ignores or dismisses it; (3) per-character rather than pooled 2% false-alarm thresholds, since character also shifts the distribution of honest episodes.
```

## Sélection des mentors (facultative)

Comptes : 49 mots (51 jetons).

```
I applied to six streams because they are all facets of one programme: whether internal-state monitors add detection power beyond black-box monitoring, and how corruptible monitors are. My order of preference: Jan Hendrik Kirchner, Lujain Ibrahim,  Stefan Heimersheim, Jérémy Scheurer, Paul Colognese & Francis Rhys Ward, Shi Feng & Eyon Jang.
```

## Lignes [À CONFIRMER PAR TOI] (rappel)

- Heimersheim — Q2 (pourquoi l'interprétabilité ; 150 mots au plus), changement 4 : « attempting » inexact : la réponse à la dose est mesurée (lecteur, changements 3 et 4) ; la proposition « rank-1 vs rank-3 » (devenue « comparison », réserve 1) et « your exponent p… » sont retirées faute de place après D36
- Kirchner — Q1 (projet empirique), changement 3 : correction 1 déjà donnée ; réserve 3 du recoupement : le bras décisif préenregistré (plan plein) en promeut 3 sur 3, le bras de comparaison (plan gelé de 120) 2 sur 3 ; « 2 of the 3 » est prudent, « all 3 » vaut pour le bras décisif
- Kirchner — Q1 (projet empirique), changement 11 : la question demande la surprise principale (lecteur 9 ; « runs » = unités ; « A coverage hole, not adaptive overfitting. » non repris, longueur) ; W1 non jugeable, l'omettre surévalue l'attaque (lecteur 10)
- Shi Feng et Eyon Jang — boîte blanche pour l'audit, changement 8 : « meaningfully » invite la lecture « presque détecté », exclue par la lecture gelée ; lien de la page publique de P3
- Jérémy Scheurer — tendance d'échelle, changement 1 : lecture « malveillance fixe par action » (lecteur 1)
- Jérémy Scheurer — tendance d'échelle, changement 7 : lecture « par action » (lecteur 8)
- Jérémy Scheurer — tendance d'échelle, changement 8 : lecteur 9, corrigé : « only sees the total » est faux pour la lecture séquentielle (le calendrier compte), seul le plancher ne dépend que du total
- Jérémy Scheurer — tendance d'échelle, changement 9 : lecture « par action » ; « doubles » du formulaire gardé (lecteur 10 et 11 ; correction 8, « smallest »/« halves », écartée)
- Lujain Ibrahim — Q1 (première expérience), changement 8 : hypothèse alignée sur l'a priori préenregistré de R8 (lecteur 10) ; réserve 4 du recoupement : « persona » et « no approval signal » sont une transposition (R8 §9 attribue la destination à l'imitation, le gain à l'optimisation de préférences), d'où « adapted from » ; la structure dépend du modèle (lecteur 11)
- Lujain Ibrahim — projet technique, changement 2 : décision de Lazar (06:19) : le placebo de même longueur est celui de la chirurgie de l'historique ; gardé (changement 19 du lecteur abandonné), marqueur ajouté
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus), changement 2 : décision de Lazar (06:19) : chirurgie de l'historique reprise telle qu'écrite, avec marqueur ; « All pre-registered and hash-locked. » retiré : redondant avec la première phrase, « All » couvrirait le juge non figé, et place nécessaire sous 200
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus), changement 3 : place nécessaire sous 200 après D36 ; redondant avec « concede roughly 0.7 of the distance »
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus), changement 5 : correction de fond D36, raccourcie pour tenir 200 (chiffres et intervalles intacts) ; le dépôt construct-validity n'est pas cité faute de place (réserve 5 non appliquée ici)
- Paul Colognese et Francis Rhys Ward — Q1 (200 mots au plus) : Longueur : 200 jetons, au-dessus des 185 du formulaire, sous la limite de 200 : imposé par la phrase D36 (chiffres et intervalles gardés). [À CONFIRMER PAR LAZAR]
- Kirchner Q1 et Q2 : les phrases sur la validation du nul v9 (« held every cheater line but cost power on one legitimate line ») sont publiques ; elles dépendent de ta décision (a) accepter le prix ou (b) v10.
