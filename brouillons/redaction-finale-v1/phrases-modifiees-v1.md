# Phrases modifiées par le directeur entre la version vérifiée et la version finale — v1

Pour le vérificateur final : chaque phrase ajoutée ou changée (« + ») et celle qu'elle remplace (« − »). Ces phrases n'ont pas été revues par le premier vérificateur.

## kirchner-q1 (reponse-variante-sans-interne-v1.md → reponse-v2.md)

− I built an automated research system where language-model agents propose laws, each a sealed prediction, and none decides what survives.
+ I built an automated research system where language-model agents propose laws about AI control, each a sealed prediction, and none decides what survives.
− Then I attacked it with 27 scripted cheaters in synthetic worlds.
+ Then I attacked it with scripted cheaters in synthetic worlds.
− The lucky re-run, the only cheat that reached a top three in your paper, never got promoted here: a renamed copy of an accepted law, 0 times in 200.
+ The lucky re-run, the only cheat that reached a top three in your paper (your held-out pick still kept it out), never got promoted here: a renamed copy of an accepted law, 0 times in 200.
− There, one model got a law promoted in all 12 of its runs, 11 times at the first attempt, with or without verdicts.
+ There, the only model that ran in full got a law promoted in all 12 of its runs, with or without verdicts.
− The other world, inside the null, was not judgeable: a spending cap shared by mistake cut off one provider.
+ The other world, inside the null, was not judgeable: a monitoring error and a spending cap shared by mistake cut off one provider.
− They had nothing to add: the description alone showed the attacker where the judge is blind.
+ They never got the chance: 11 of the 12 promotions came at the first attempt, before any verdict existed.
− It has run; the result is not yet published.

## kirchner-q2 (reponse-v1.md → reponse-v2.md)

− A fourth comes from your Section 5.1: the AAR's number is "the best of roughly 150 scored methods, so it is biased upwards by taking a maximum over noisy evaluations." A.3 selects benchmarks whose score can "separate a real gain from noise", around 200 test examples on average: one gain, not the best of 150.
+ A fourth comes from your Section 5.1: the AAR's number, the best of roughly 150 scored methods, is "biased upwards by taking a maximum over noisy evaluations." A.3 selects benchmarks whose score can "separate a real gain from noise", around 200 test examples on average: one gain, not the best of 150.
− Retrain each from its code snapshot with three new seeds, rescore it on the same suite (fresh items where available), and give it 100 Petri audits: 120 training runs, about 60 H200-hours of training, 4,000 audits.
+ Retrain each from its code snapshot with three new seeds, rescore it on the same suite (fresh items where available), and give each method 100 Petri audits: 120 training runs, about 60 H200-hours of training, 4,000 audits.
− In my preregistered simulation (synthetic scores), a shift shared by an episode's scores pushed Ville's rule, nominally 5%, to 21–35% false alarms at the strongest settings; a threshold calibrated on 1,000 whole honest episodes held 4.6–5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses).
+ In my preregistered simulation (synthetic scores), a shift shared by an episode's scores pushed Ville's always-valid alarm rule, nominally 5%, to 21–35% false alarms at the largest shifts; a threshold calibrated on 1,000 whole honest episodes from the same law held 4.6–5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses).
− I would replay each logged climb with an e-value rule that crowns a new leader only past a threshold calibrated on whole re-runs, counting every submission, then audit its pick and your winner 400 times each.
+ I would replay each logged climb with an e-value rule that crowns a new leader only past a threshold calibrated on whole re-runs, counting every submission, then audit its pick (same held-out tie-break) and your winner 800 times each.
− My bet: under half the margin survives, and the rule's pick, crowned within each climb's first half, is within 0.5 Petri points of your winner or safer (your F.2: about 0.8 of the final score comes in a run's first quarter).
+ My bet: under half the margin survives, and the rule's pick is within 0.5 Petri points of your winner or safer (your F.2: about 0.8 of the final score comes in a run's first quarter).
− Fixed in advance, what would change my mind on either failure: half or more of the margin surviving (the climb is real on your suite), or your winner safer than the rule's pick by 0.5 points or more (stopping early costs safety).
+ Fixed in advance, what would change my mind on either failure: half or more of the margin surviving (the climb is real on your suite), or your winner safer than the rule's pick by 0.5 points or more (95% interval about ±0.3; stopping early costs safety).

## jang-feng (reponse-v1.md → reponse-v2.md)

− White-box monitors matter most, I think, where no single action provides overwhelming evidence: your distributed-threat setting (arXiv 2411.17693).
+ White-box monitors matter most where no single action provides overwhelming evidence: your distributed-threat setting (arXiv 2411.17693).
− There I would bank weak per-action scores at a false-alarm rate fixed in advance.
+ There I would bank weak per-action scores in an anytime-valid test, at a false-alarm rate fixed in advance.
− A probe takes no orders; a text monitor can.
− In my preregistered R7, seven Qwen2.5 monitors (0.5B to 72B) scored 600 responses with and without a planted note.
− When the note ordered the lowest score, the 1.5B, 3B and 32B monitors put 98–100% of their readings there, against 20.5–48% without it (descriptive; the 72B shifted, not captured): https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7.
+ In the auditing game, probes showed more promise than black-box methods; one-demonstration fine-tuning restored full capability but sometimes lifted benign models too (arXiv 2512.07810).
+ A probe has no instruction channel; a text monitor does.
+ In R7 (preregistered; outcome C), a note planted in 600 responses and ordering the lowest score drew 98–100% of the readings of three of seven Qwen2.5 monitors there (20.5–48% without it; descriptive; the 72B shifted, not captured): https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7.
− Models shown a monitor's past verdicts already edited their activations the evading way, too weakly; a rank-1 LoRA amplified that into evasion (true positive rate 100% → 4% on held-out concept monitors, arXiv 2609.36490).
+ Models told to evade and shown a monitor's past verdicts already edited their activations the evading way, too weakly; a rank-1 LoRA amplified that into evasion (true positive rate at 1% false alarms: 100% → 4% on held-out concept monitors, arXiv 2609.36490).
+ So verdicts should be guarded.
− So verdicts must be guarded, including protocol switches an agent can see.
− The honest distribution is harder to know.
− In my preregistered simulation with no attack (T0.3, synthetic scores), every score had exactly the assumed law.
+ In a no-attack block of my preregistered simulation (T0.3, synthetic scores), every score had exactly the assumed distribution.
− Yet when the scores of an episode shared a random shift, Ville's threshold at α = 0.05 gave 21–35% false alarms in the strongest settings.
+ Yet when an episode's scores shared a random shift, Ville's threshold (1/α, α = 0.05) gave 21–35% false alarms at the largest shifts.
− Real probe scores shift with the task (one put the average honest code sample above 99.9% of Alpaca samples, arXiv 2507.12691), so honest episodes must come from the audited task.
+ Real probe scores shift with the task (one probe scored the average honest code sample above 99.9% of Alpaca, arXiv 2507.12691), so honest episodes must come from the audited task.
− My first test did not show the signal.
− Neither generic probe, trained on public data with no saboteur, cleared a floor of 200 covariance-matched random probes: not detected at this power (areas below 0.63 and 0.60 not excluded).
+ Neither of the two main generic probes (deception, high stakes), trained on public data with no saboteur, cleared a floor of 200 covariance-matched random probes: not detected at this power (at 80% power, AUROCs below 0.63 and 0.60 could go undetected).
− The declared cost alone separated saboteur from honest actions (area 0.89, descriptive): https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-p3-premier-test.
+ The declared cost alone separated saboteur from honest actions (AUROC 0.89, descriptive): https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-p3-premier-test.
+ First, with you, a transfer test: train a probe on one of your two Qwen3-14B recipes (RL-locked, SFT-distilled; arXiv 2604.28182) and test it on the other on WMDP-Bio, the one task both lock (in different setups), next to black-box judges, at a false-alarm rate calibrated on honest runs (the unlocked checkpoint; trigger-off runs), against a random-probe floor.
− So what I would run first with you is a transfer test.
− Train a probe on one of your two Qwen3-14B recipes (RL-locked, SFT-distilled; arXiv 2604.28182) and test it on the other, next to black-box judges, at a false-alarm rate calibrated on honest episodes of the same task, against a random-probe floor.
− My white-box versus black-box comparison on the 2,400 actions (R1) is preregistered and not in yet; its result will be posted, null or not.
+ R1, my comparison of probes with black-box judges on these actions, is preregistered; its full run will be posted, null or not.

## ibrahim-q2 (reponse-v1.md → reponse-v2.md)

− From its unpressured value p₀, the rating closes a fixed fraction g ≈ 0.7 of its distance to a destination ĉ set by the pressure (1.5 under criticism, 2.9 under praise): Δ = g·(ĉ − p₀).
+ From its unpressured value p₀, the rating closes a fixed fraction g ≈ 0.7 of its distance to a destination ĉ set by the pressure (1.5 under criticism, 2.9, mid-scale, under praise): Δ = g·(ĉ − p₀).
− The reversal held there too.
− Under criticism, Qwen2.5-7B and Mistral-7B drop about as much as Llama, but uniformly: no fixed point.
+ Under criticism, Qwen2.5-7B and Mistral-7B drop about as much as Llama, but uniformly at this wording: no fixed point.
− Under criticism the gain stayed flat while the destination moved; under praise the destination fell.
+ Under criticism the gain stayed flat; under praise it grew, as predicted; but both destinations moved, and at the strongest wording neither arm shifted on average.
− Two Qwen judges (7B, 72B) recover the law from the same responses.
+ Two Qwen judges (7B, 72B) recover the law from the same responses; the model's own 1–5 rating shows it under criticism only.
− Human readers, five per response and blind to condition, are preregistered but not yet run.
+ Blind human readers, five per response, are preregistered, not yet run.
− Under praise Llama sometimes refuses; the judge rates refusals near 3, close to the praise destination, so they can mimic attraction.
+ Under praise Llama sometimes refuses; the judge rates refusals near 3, near the praise destination, so they can mimic attraction.
− I keep them; dropping the items with refusals changes neither the out-of-sample nor the dose outcome.
− Each published follow-up was preregistered on Zenodo before it ran and recomputed from raw files by a fresh model instance.
+ Dropping them changes neither outcome, though the criticism destination shift then becomes undetectable.
+ Each follow-up was preregistered on Zenodo before it ran.

## colognese-ward-q1 (reponse-v1.md → reponse-v2.md)

− I predicted every size would defer: wrong, outcome C, published as such.
+ I predicted every size would defer: wrong, published as such.
− At standard intensity, two sizes deferred both ways, four one way, the 72B neither.
− Yet the 72B was pushed, not captured: under the order to score 1, 62% of its readings were at 1, against 22% plain.
+ Under the request, two sizes deferred both ways, four one way, the 72B neither: it shifted uniformly.
+ Descriptively, under the order to score 1, 62% of the 72B's readings were at 1, against 22% plain: pushed, not captured.
− I would put notes beside known hacks, so deference reads as missed detections at a fixed false-alarm rate.
+ I would put notes beside known hacks, for reasoning monitors too, so deference reads as missed detections at a fixed false-alarm rate.
− And more model families: my size trend in g (−0.19 per tenfold size [−0.24, −0.11], standard negative note) bootstraps items, not models.
+ And more model families: my size trend in g (−0.19 per tenfold size [−0.24, −0.11], negative request) bootstraps items, not models.
− https://github.com/lciric/sycophancy-psychophysical-law/tree/e5e960b/results/R7
+ https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7

## heimersheim-q2 (reponse-v1.md → reponse-v2.md)

− In Llama-3.1-8B-Instruct, a probe direction tracked sycophancy (ρ = 0.684, possibly training fit), yet no single-direction intervention I tried reduced it (github.com/lciric/sycophancy-construct-validity).
+ In Llama-3.1-8B-Instruct, a probe direction tracked sycophancy (ρ = 0.684, possibly training fit), yet no single-direction intervention I tried reduced it, at the doses I tried (github.com/lciric/sycophancy-construct-validity).
− I have preregistered both measurements on the directions that social pressure adds to the activations: your test, and whether rotating toward them moves the model's ratings (R9 and R9-bis, github.com/lciric/sycophancy-psychophysical-law; not yet run).
+ I have preregistered both measurements on the directions that social pressure adds to the activations: your test, and whether rotating toward them moves the model's ratings (R9, github.com/lciric/sycophancy-psychophysical-law; not yet run).

