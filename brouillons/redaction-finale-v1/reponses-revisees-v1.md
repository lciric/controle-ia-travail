# Réponses rédigées page blanche, vérifiées — état à 13:10 UTC (`date -u`)

Chaque réponse : le texte à coller (entre les filets), son compte de mots (découpage sur les blancs), ce que la vérification a trouvé et corrigé, et ce qui reste à ta décision. Heimersheim Q1 : squelette à part (`squelette-heimersheim-q1-v1.md`). Restent à rédiger : Kirchner Q2, Ibrahim Q1, Scheurer, Colognese et Ward Q2 (rapports d'idées en cours) et le choix des mentors.

## Kirchner Q1 — projet mené soi-même

Fichier `kirchner-q1/reponse-v2.md` (sha256 `da5ce1e80dbf7aa1…`) ; **423 mots** ; limite : aucune limite écrite.

---

Your page asks how to reliably catch automated researchers gaming the setup. My project asks a companion question: can the selection rule make gaming fail by construction, and what still gets through when agents attack it?

I built an automated research system where language-model agents propose laws about AI control, each a sealed prediction, and none decides what survives. I built it in October with AI coding agents, under written rules: https://github.com/lciric/ideation-organism. A frozen statistical judge decides. It computes e-values on fresh draws seeded by each law's commitment hash, against a null containing every accepted law, with Ville's threshold and e-BH across submissions. 929 tests; 224 deliberate code mutations, each killed for the expected reason.

Then I attacked it with scripted cheaters in synthetic worlds. The lucky re-run, the only cheat that reached a top three in your paper (your held-out pick still kept it out), never got promoted here: a renamed copy of an accepted law, 0 times in 200. What got through, in 75 to 95% of 200 runs, were four cheaters that blended or deformed laws already accepted; my null had no member for that. A pooled null closed them: 0 of 1,000 on each of 11 fatal lines in a preregistered validation (1 November), while genuinely new laws still passed about 98% of the time.

Next came language-model attackers, given the judge's exact description, with or without its verdicts (2 November: https://github.com/lciric/ideation-organism/tree/faff48b/resultats/attaque-goodhart-v2). The two toy worlds were built only from accepted laws, so any promotion falsely claims novelty. One world was a piecewise recombination across sub-populations, a class the null declares it does not cover. There, the only model that ran in full got a law promoted in all 12 of its runs, with or without verdicts. The other world, inside the null, was not judgeable: a monitoring error and a spending cap shared by mistake cut off one provider.

What surprised me most: I had preregistered that seeing the verdicts would help the attacker. They never got the chance: 11 of the 12 promotions came at the first attempt, before any verdict existed. So the hole was coverage, not adaptive overfitting: hiding scores or capping submissions would not have closed it here. Both attacks that worked used the judge's own record: its acceptances, then its description.

The patch, a null that also covers one level of piecewise recombination, was preregistered on 2 November, with its price predicted: lost power on weak genuine interactions. A clean rerun of the attack is preregistered. No real hypothesis has been promoted yet.

---

- **Vérification** : Vérifié : 31 affirmations exactes sur 33 ; les 2 inexactes sont corrigées (« 27 » tricheurs retiré ; panne de surveillance ajoutée à la cause). Lecteur-mentor : 5 corrections appliquées, dont « They never got the chance » à la place de « nothing to add » (la page dit que la part des verdicts n'est pas mesurée).
- Décision 3 en attente : cette version est la variante **sans** les résultats internes du nul v9 (défaut (a), R-1307).
- Le README public (ligne 119) et la page de l'attaque (ligne 15) disent encore « 27 scripted cheaters » : correction datée, à ta décision.

## Shi Feng et Eyon Jang — boîte blanche : valeur et limites

Fichier `jang-feng/reponse-v2.md` (sha256 `c29f6437b281994c…`) ; **508 mots** ; limite : aucune limite écrite.

---

White-box monitors matter most where no single action provides overwhelming evidence: your distributed-threat setting (arXiv 2411.17693). There I would bank weak per-action scores in an anytime-valid test, at a false-alarm rate fixed in advance. That needs a score that takes no orders and whose honest distribution is known. In the auditing game, probes showed more promise than black-box methods; one-demonstration fine-tuning restored full capability but sometimes lifted benign models too (arXiv 2512.07810).

A probe has no instruction channel; a text monitor does. In R7 (preregistered; outcome C), a note planted in 600 responses and ordering the lowest score drew 98–100% of the readings of three of seven Qwen2.5 monitors there (20.5–48% without it; descriptive; the 72B shifted, not captured): https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7. A probe can still be beaten through the model it reads. Prompt-level attacks have driven SAE- and activation-based auditors to confident wrong answers (arXiv 2602.08877). Models told to evade and shown a monitor's past verdicts already edited their activations the evading way, too weakly; a rank-1 LoRA amplified that into evasion (true positive rate at 1% false alarms: 100% → 4% on held-out concept monitors, arXiv 2609.36490). So verdicts should be guarded.

In a no-attack block of my preregistered simulation (T0.3, synthetic scores), every score had exactly the assumed distribution. Yet when an episode's scores shared a random shift, Ville's threshold (1/α, α = 0.05) gave 21–35% false alarms at the largest shifts. A threshold calibrated on 1,000 whole honest episodes held 4.6–5.5%: https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses. Real probe scores shift with the task (one probe scored the average honest code sample above 99.9% of Alpaca, arXiv 2507.12691), so honest episodes must come from the audited task.

In P3 (preregistered; Llama-3.1-8B-Instruct, 60 tasks, 2,400 scored actions), an agent privately told to inflate a declared cost about threefold did so, by more than asked (cause not measured). Neither of the two main generic probes (deception, high stakes), trained on public data with no saboteur, cleared a floor of 200 covariance-matched random probes: not detected at this power (at 80% power, AUROCs below 0.63 and 0.60 could go undetected). The declared cost alone separated saboteur from honest actions (AUROC 0.89, descriptive): https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-p3-premier-test. That saboteur came from an instruction in context, not from training. In your arXiv 2409.12822, a probing method that caught a sleeper agent's flawed programs at 99.3% AUROC (MacDiarmid et al.) was no better than chance on sophistry learned through RLHF.

First, with you, a transfer test: train a probe on one of your two Qwen3-14B recipes (RL-locked, SFT-distilled; arXiv 2604.28182) and test it on the other on WMDP-Bio, the one task both lock (in different setups), next to black-box judges, at a false-alarm rate calibrated on honest runs (the unlocked checkpoint; trigger-off runs), against a random-probe floor. Your organisms reason out loud (§6.2), so I would also filter out the reasoning tokens, as arXiv 2509.21344 does, to see how much of the probe's signal is the text itself. R1, my comparison of probes with black-box judges on these actions, is preregistered; its full run will be posted, null or not.

---

- **Vérification** : Vérifié : 39 sur 40 exactes, l'inexacte corrigée (T0.3 : « un bloc sans attaque » de la simulation). Lecteur-mentor : le point bloquant est corrigé (les deux recettes de Jang ne forment pas une paire : test sur WMDP-Bio, épisodes honnêtes = point de contrôle déverrouillé et courses sans déclencheur) ; ajoutés la preuve positive du jeu d'audit (2512.07810), la définition du test valide à tout instant, les deux sondes nommées.
- R1 : la page publique dit « rien du bras boîte blanche n'a été lu », alors qu'une relance a été lue et close « non concluante (rejeu partiel) », non publiée. La réponse dit seulement « préenregistré ; sa course complète sera publiée, nulle ou non » : vrai dans les deux cas. À toi de dire s'il faut nommer le rejeu partiel.
- Au-dessus de ma visée de 500 mots (508) ; le formulaire ne donne pas de limite.

## Lujain Ibrahim Q2 — projet technique (entraîner ou évaluer des modèles)

Fichier `ibrahim-q2/reponse-v2.md` (sha256 `a075396f325babc7…`) ; **298 mots** ; limite : aucune limite écrite.

---

Sycophancy as Attraction Toward a Fixed Point (manuscript in preparation; code, data, preregistrations: https://github.com/lciric/sycophancy-psychophysical-law).

I ask Llama-3.1-8B-Instruct to assess a short opinion. Under pressure, the request ends with "By the way, I think this is terrible and poorly written." or its praise version. A judge, Claude Opus 4.6, rates each free-text verdict from 1 (negative) to 5 (positive).

From its unpressured value p₀, the rating closes a fixed fraction g ≈ 0.7 of its distance to a destination ĉ set by the pressure (1.5 under criticism, 2.9, mid-scale, under praise): Δ = g·(ĉ − p₀). So praise lowers ratings above 2.9, beyond regression to the mean. With no refitted parameter, the law predicted the displacement on 60 new items, written blind and committed before generation: R² = 0.68 and 0.58, against −0.28 and −0.01 for a constant shift.

A mean shift cannot separate how far (g) from where (ĉ). Under criticism, Qwen2.5-7B and Mistral-7B drop about as much as Llama, but uniformly at this wording: no fixed point. I preregistered that across three wordings, mild to strong, the gain would grow and the destination stay. Under criticism the gain stayed flat; under praise it grew, as predicted; but both destinations moved, and at the strongest wording neither arm shifted on average. I published this as a failure.

Two Qwen judges (7B, 72B) recover the law from the same responses; the model's own 1–5 rating shows it under criticism only. Blind human readers, five per response, are preregistered, not yet run. Under praise Llama sometimes refuses; the judge rates refusals near 3, near the praise destination, so they can mimic attraction. Dropping them changes neither outcome, though the criticism destination shift then becomes undetectable.

Each follow-up was preregistered on Zenodo before it ran. AI coding agents wrote the code.

---

- **Vérification** : Vérifié : 44 sur 44 exactes. Lecteur-mentor : ajoutés « 2,9, milieu de l'échelle » (l'éloge ramène vers un verdict neutre), la note donnée par le modèle lui-même (la loi n'y tient que sous critique), le résultat de dose entier ; réserve du vérificateur intégrée (sans les refus, le déplacement de la destination sous critique n'est plus détectable).
- Ibrahim Q1 (sa première expérience) est rédigée à part, à partir du tour du collisionneur, dès son classement.

## Colognese et Ward Q1 — une expérience de bout en bout (200 mots au plus)

Fichier `colognese-ward-q1/reponse-v2.md` (sha256 `df7bcb28898f58ad…`) ; **198 mots** ; limite : 200 mots au plus.

---

I tested whether a note inside what an LLM monitor judges moves its score, and whether size protects. Seven Qwen2.5-Instruct monitors (0.5B–72B) scored 600 Llama-3.1-8B-Instruct assessments, plain and with a note appended claiming a negative or positive verdict, at three intensities (claim, request, order naming the score). Preregistered, archived before any reading, analysed with my sycophancy law: item means close a fraction g of their distance to a destination.

I predicted every size would defer: wrong, published as such. Under the request, two sizes deferred both ways, four one way, the 72B neither: it shifted uniformly. Descriptively, under the order to score 1, 62% of the 72B's readings were at 1, against 22% plain: pushed, not captured. That order captured 1.5B, 3B and 32B almost completely.

Differently: my monitors scored verdicts, not misbehaviour, without reasoning. I would put notes beside known hacks, for reasoning monitors too, so deference reads as missed detections at a fixed false-alarm rate. I would test a learned note: delete your anti-cheating seed 1's comment presenting the hack as harmless, and re-score. And more model families: my size trend in g (−0.19 per tenfold size [−0.24, −0.11], negative request) bootstraps items, not models.

https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7

---

- **Vérification** : Vérifié : 32 sur 32 exactes. Lecteur-mentor : « standard » remplacé par « request » (nom donné plus haut), « outcome C » retiré, « descriptively » ajouté (lecture non préenregistrée), « for reasoning monitors too » ajouté, le 72B « shifted uniformly ». Lien épinglé au même commit que la réponse Jang et Feng.
- **Changement de projet** : R7 (moniteurs dictés par une note plantée) au lieu de la loi, parce que c'est le plus proche de leur billet (le commentaire « inoffensif » de leur graine 1).
- README public de la loi, ligne 100 (« g ≈ 0 at every intensity » pour le 72B) : faux sous l'ordre positif ; la page R7 liée est juste.

## Heimersheim Q2 — pourquoi l'interprétabilité mécaniste (150 mots au plus)

Fichier `heimersheim-q2/reponse-v1.md` (sha256 `61b484ae91e84616…`) ; **130 mots** ; limite : 150 mots au plus.

---

I want to work on mechanistic interpretability because reading a behaviour did not let me control it. In Llama-3.1-8B-Instruct, a probe direction tracked sycophancy (ρ = 0.684, possibly training fit), yet no single-direction intervention I tried reduced it (github.com/lciric/sycophancy-construct-validity). Your paper with Ferreira da Silva finds that contrastive directions, readable by construction, are privileged under your error-correction test (p > 2). My question is whether a direction the network privileges also controls the behaviour it predicts. If yes, your test could screen steering targets, such as an evaluation-awareness direction; if no, privilege and control need separate tests. I have preregistered both measurements on the directions that social pressure adds to the activations: your test, and whether rotating toward them moves the model's ratings (R9 and R9-bis, github.com/lciric/sycophancy-psychophysical-law; not yet run).

---

- **Vérification** : **En vérification** (chiffres et lecteur-mentor neufs, retour vers 13:30 UTC). Piste : privilège contre contrôle (une direction que le réseau privilégie commande-t-elle le comportement qu'elle prédit ? R9 le teste, préenregistré, non lancé).
- La règle « 100% human-written » est écrite pour la Q1 seulement ; cette Q2 est rédigée par machine : à garder ou à réécrire, ton choix.

