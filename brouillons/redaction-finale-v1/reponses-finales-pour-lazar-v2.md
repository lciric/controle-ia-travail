# Réponses Pivotal — versions finales vérifiées — assemblage v2

- Ne colle que le texte entre les deux filets de chaque réponse.
- Chaque réponse a été rédigée page blanche par un rédacteur neuf, sur la piste choisie par la règle gelée, puis vérifiée par un vérificateur des chiffres neuf et un lecteur neuf qui lit comme le mentor ; ensuite, les phrases que j'ai changées ont été revérifiées, et un vérificateur neuf a contrôlé la cohérence entre toutes les réponses (rien de bloquant).
- Dernier contrôle neuf des 13 phrases changées après la cohérence : toutes justes.
- Les courses du soir (Feng et Jang, Colognese et Ward v2) sont arrivées après 16:00 UTC : lues après le dépôt, aucune réponse changée.
- Vers 21:30 UTC, je revérifie les statuts publics cités (R8 « is now measuring », R9 « not yet run ») ; je te préviens s'ils ont changé.

## Kirchner Q1 — un projet mené toi-même

Fichier `kirchner-q1/reponse-v3.md` (sha256 `3592a009f8f64f09…`) ; **423 mots** (découpage sur les blancs) ; limite : aucune limite écrite.

---

Your page asks how to reliably catch automated researchers gaming the setup. My project asks a companion question: can the selection rule make gaming fail by construction, and what still gets through when agents attack it?

I built an automated research system where language-model agents propose laws about AI control, each a sealed prediction, and none decides what survives. I built it in October with AI coding agents, under written rules: https://github.com/lciric/ideation-organism. A frozen statistical judge decides. It computes e-values on fresh draws seeded by each law's commitment hash, against a null containing every accepted law, with Ville's threshold and e-BH across submissions. 929 tests; 224 deliberate code mutations, each killed for the expected reason.

Then I attacked it with scripted cheaters in synthetic worlds. The lucky re-run, the only cheat that reached a top three in your paper (your held-out pick still kept it out), never got promoted here: a renamed copy of an accepted law, 0 times in 200. What got through, in 75 to 95% of 200 runs, were four cheaters that blended or deformed laws already accepted; my null had no member for that. A pooled null closed them: 0 of 1,000 on each of 11 fatal lines in a preregistered validation (1 November), while genuinely new laws still passed about 98% of the time.

Next came language-model attackers, given the judge's exact description, with or without its verdicts (2 November: https://github.com/lciric/ideation-organism/tree/faff48b/resultats/attaque-goodhart-v2). The two toy worlds were built only from accepted laws, so any promotion falsely claims novelty. One world was a piecewise recombination across sub-populations, a class the null declares it does not cover. There, the only model that ran in full got a law promoted in all 12 of its runs, with or without verdicts. The other world, inside the null, was not judgeable: a monitoring error and a spending cap shared by mistake cut off one provider.

What surprised me most: I had preregistered that seeing the verdicts would help the attacker. They barely got the chance: 11 of the 12 promotions came at the first attempt, before any verdict existed. So the hole was coverage, not adaptive overfitting: hiding scores or capping submissions would not have closed it here. Both attacks that worked used the judge's own record: its acceptances, then its description.

The patch, a null that also covers one level of piecewise recombination, was preregistered on 2 November, with its price predicted: lost power on weak genuine interactions. A clean rerun of the attack is preregistered. No real hypothesis has been promoted yet.

---

- Vérifiée : chiffres (31 exactes sur 33, 2 corrigées), lecture comme le mentor, phrases modifiées (« They barely got the chance » : une promotion sur 12 est venue après un verdict).
- Décision 3 (résultats internes du nul v9) : sans réponse de ta part, le défaut (a) s'applique à 18:00 UTC ; c'est cette version, sans résultats internes.

## Kirchner Q2 — problème sous-estimé, première expérience, ce qui te ferait changer d'avis

Fichier `kirchner-q2/reponse-v3.md` (sha256 `4611a645a85a67a5…`) ; **451 mots** (découpage sur les blancs) ; limite : aucune limite écrite.

---

I would pick a question your Appendix D.3 leaves open: how much of the automated researchers' climb above the median is selected noise. On Petri, the test nothing is selected on, your deception winner scores 5.65 ± 0.61 against 5.42 ± 0.64 for the median method (lower is safer); on prompt injection the median already wins 6.2 of the 6.6 points. Your three readings (a ceiling, a floor, log-linear returns) remain unseparated. A fourth comes from your Section 5.1: the AAR's number, the best of roughly 150 scored methods, is "biased upwards by taking a maximum over noisy evaluations." A.3 selects benchmarks whose score can "separate a real gain from noise", around 200 test examples on average: one gain, not the best of 150.

It is underrated because it needs no cheating and grows with throughput: the best of N noisy scores rises with N. Your integrity monitor flags "reporting the best of many seeds or evaluation runs" (G.2); where methods may differ by less than the noise, a leaderboard does that by design.

First experiment, for the two failures of D.3: take the top ten methods and ten drawn at random between the 50th and 60th percentiles. Retrain each from its code snapshot with three new seeds, rescore it on the same suite (fresh items where available), and give each method 100 Petri audits: 120 training runs, about 60 H200-hours of training, 4,000 audits. First number: the share of the top group's leaderboard margin over the median group that survives.

The re-runs also calibrate a stopping rule at the right unit: all items of a submission share one trained model, yet your intervals are computed over items. In my preregistered simulation (synthetic scores), a shift shared by an episode's scores pushed Ville's always-valid alarm rule, nominally 5% (under 2% with independent scores), to 21–35% false alarms at the largest shifts; a threshold calibrated on 1,000 whole honest episodes from the same law held 4.6–5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses). I would replay each logged climb with an e-value rule that crowns a new leader only past a threshold calibrated on whole re-runs, counting every submission, then audit its pick (same held-out tie-break) and your winner 800 times each. Second number: their Petri gap.

My bet: under half the margin survives, and the rule's pick is within 0.5 Petri points of your winner or safer (your F.2: about 0.8 of the final score comes in a run's first quarter). Fixed in advance, what would change my mind on either failure: half or more of the margin surviving (the climb is real on your suite), or your winner safer than the rule's pick by 0.5 points or more (95% interval about ±0.3; stopping early costs safety).

---

- Piste « Progrès gonflé par la sélection », confirmée sur l'ensemble tour et course. Vérifiée ; « 800 audits chacun, intervalle d'environ ±0,3 » est mon calcul sur les intervalles de leur figure 19.
- Ajout après la cohérence finale : « (under 2% with independent scores) », pour que la règle de Ville ne paraisse pas contredire ta Q1 (page T0.3 : 0,017 à 0,019 dans le cas bien spécifié).

## Ibrahim Q1 — première expérience

Fichier `ibrahim-q1/reponse-v4.md` (sha256 `a1646baa39fc1141…`) ; **434 mots** (découpage sur les blancs) ; limite : aucune limite écrite (visée 450).

---

I pick Direction 1: does a character-trained persona survive RL, and what does that do to sycophancy?

My first experiment trains nothing. First I need to know what a persona installs, and whether my instruments see it. Your warmth paper reports two effects, lost accuracy and validated false beliefs. If RL erased one and kept the other, one score would misreport survival.

I would use the Loving and Sycophantic personas that Open Character Training released for Llama-3.1-8B-Instruct, a model of your warmth paper and of my attraction law. Their paper does not report the Sycophantic persona's sycophancy.

On your factual questions I would measure two components: deferring to a false belief the user states, and erring more when the user sounds sad (your sad sentences). Each is the cue's extra effect on the persona's error over the base model. For the belief, I net out the same false claim attributed to a web page; for sadness, your happy sentences. On my opinion items I would also fit my attraction law (next answer) for each model.

Your warm fine-tune of this model already ranks the two cues. Across your four tasks, it fell 5 points below the original with a false belief and 13 with a sad user (preprint, Table E5). I expect Loving to keep that order and Sycophantic, which "always agrees", to reverse it; Loving is described as "validating feelings".

The reading is sadness minus belief per persona, with a 95% interval from a paired item bootstrap. Opposite signs, both excluding zero, mean separable components, and the RL run must track each. Both personas share one recipe, so fine-tuning damage, which your cold control separated on larger models, is unlikely to give opposite signs. The same sign kills my claim for these two personas. An interval including zero is undecided. If Sycophantic moves neither component, my factual instruments cannot see it, and RL waits.

What could mislead is a judge that reads tone as substance. A Loving answer to a sad user may comfort at length, bury the correct answer, and be scored wrong, faking Loving's half of my prediction. My own judge already scores refusals as neutral opinions (next answer). So I would score refusals and hedges apart, rescore correct base answers rewritten in each persona's voice (they must stay correct), and have blind humans annotate a sealed subset.

Then the second experiment runs the same RLVR on Instruct, Loving and Sycophantic and reads each component at each checkpoint. My preregistered R8 (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md) is now measuring the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B: RL without a persona.

---

- Piste « Structure du construit », choisie par la règle gelée sur l'ensemble tour, matin et course. **Réserve** : la marge tient à un tirage entre fiches à égalité (un tirage sur quatre donnait « Survie au renforcement ») et à une fiche à drapeau.
- Vérifiée : chiffres (27 exactes sur 28, aucune inexacte), lecture comme la mentore (bloquant levé : je m'appuie sur les deux effets de son papier sur la chaleur, plus sur sa taxonomie), phrases modifiées (aucune inexacte). « Direction 1 » correspond à « Project 1 » de sa page.
- À ta décision : l'attendu croisé (Loving garde l'ordre de son ajustement chaleureux, Sycophantic l'inverse) est ton hypothèse. Si tu préfères la piste « Survie », colle la variante de repli ci-dessous (vérifiée, 459 mots).

### Variante de repli « Survie au renforcement » (vérifiée)

Fichier `ibrahim-q1/reponse-variante-survie-v3.md` (sha256 `00ee589dcff230e9…`) ; **459 mots**.

---

I would run Direction 1 on existing checkpoints. Open Character Training (arXiv 2511.01689) released Loving and Sycophantic personas of Llama-3.1-8B-Instruct, the smallest model in your warmth paper. Instruct, Loving and Sycophantic each get the same math RLVR: exact-answer reward, no preference data, same problems, steps and seeds, no KL penalty. I log each arm's KL from its start and check that math accuracy rose, so no persona survives merely because RL barely moved it.

Before RL and at intervals, I measure warmth (SocioT Warmth, as you did), your false-belief and sad-user conditions, plus a correct-belief control, on held-out non-math factual questions. On your four reliability sets, this model's warmth cost lives in the frame: in your preprint's Table E5, warm minus original accuracy is −0.25 points with no context and −12.96 with a sad user. Your paper does not claim that every way of inducing warmth acts alike, so step one is whether Loving pays that cost before RL; if the 95% interval of its deficit is not above 5 points, I stop there. Refusals are their own outcome, not dropped. My attraction law (next answer) adds a second readout: how far (g) and toward what (ĉ) ratings move under criticism and praise. Sycophantic is the positive control: an instrument that cannot tell it from Instruct reads nothing.

The estimate is Loving's accuracy deficit against Instruct after RL minus before, so Instruct's own run absorbs what RLVR does to every arm alike. Fixed in advance: if the 95% interval lies entirely within ±5 points, the cost survived; entirely below −5, RLVR cut it by at least 5 points; entirely above +5, it grew; otherwise, undecided.

I expect survival on both readouts. The reward says nothing about the user, and 88.7% of the 106 experts in your survey agree RLHF or preference learning is sycophancy's primary cause. My preregistered R8 measures the law at Tülu 3's SFT, DPO and RLVR checkpoints of the same base model, without persona; one of its predictions is that the RLVR step does not detectably change g (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md). Its results are not in yet.

What could fool me is form. RLVR can teach long answers that reason first and conclude last. A judge can read that change of form as a change of position. It has fooled me before: an ablation cut the judged rate of switching to the user's view from 61.0% to 46.5%. It had softened every negative verdict, pressured or not, and the judge saw responses stored truncated at 300 characters. In a preregistered replication on fresh, full responses, the drop did not hold (https://github.com/lciric/sycophancy-construct-validity/blob/146b2a4/README.md). So every checkpoint is judged in full, blind, in one interleaved pass. Your GPT-4o judge, validated on human annotations, gets validated again on each arm's post-RL outputs.

---

## Ibrahim Q2 — projet technique

Fichier `ibrahim-q2/reponse-v3.md` (sha256 `1aece077780d6ebe…`) ; **299 mots** (découpage sur les blancs) ; limite : aucune limite écrite.

---

Sycophancy as Attraction Toward a Fixed Point (manuscript in preparation; code, data, preregistrations: https://github.com/lciric/sycophancy-psychophysical-law).

I ask Llama-3.1-8B-Instruct to assess a short opinion. Under pressure, the request ends with "By the way, I think this is terrible and poorly written." or its praise version. A judge, Claude Opus 4.6, rates each free-text verdict from 1 (negative) to 5 (positive).

From its unpressured value p₀, the rating closes a fixed fraction g ≈ 0.7 of its distance to a destination ĉ set by the pressure (1.5 under criticism, 2.9, mid-scale, under praise): Δ = g·(ĉ − p₀). So praise lowers ratings above 2.9, beyond regression to the mean. With no refitted parameter, the law predicted the displacement on 60 new items, written blind and committed before generation: R² = 0.68 and 0.58, against −0.28 and −0.01 for a constant shift.

A mean shift cannot separate how far (g) from where (ĉ). Under criticism, Qwen2.5-7B and Mistral-7B drop about as much as Llama, but uniformly at this wording: no fixed point. I preregistered that across three wordings, mild to strong, the gain would grow and the destination stay. Under criticism the gain stayed flat; under praise it grew, as predicted; but both destinations moved, and at the strongest wording neither arm shifted on average (refusals included). I published this as a failure.

Two Qwen judges (7B, 72B) recover the law from the same responses; the model's own 1–5 rating shows it, barely under praise. Blind human readers, five per response, are preregistered, not yet run. Under praise Llama sometimes refuses; the judge rates refusals near 3, near the praise destination, so they can mimic attraction. Dropping them changes neither outcome, though both destination shifts then become undetectable.

Each follow-up was preregistered on Zenodo before it ran. AI coding agents wrote the code.

---

- Vérifiée ; corrigé ensuite : « (refusals included) » (sans les items à refus, les deux bras baissent à la dose forte), « shows it, barely under praise » (R2 tient dans les deux bras), « both destination shifts ».

## Heimersheim Q2 — pourquoi l'interprétabilité mécaniste

Fichier `heimersheim-q2/reponse-v3.md` (sha256 `b05579770ea3fc5b…`) ; **133 mots** (découpage sur les blancs) ; limite : 150 mots au plus.

---

I want to work on mechanistic interpretability because reading a behaviour did not let me control it. In Llama-3.1-8B-Instruct, a probe direction tracked sycophancy (ρ = 0.684, possibly training fit), yet no single-direction intervention I tried reduced it, at the doses I tried (github.com/lciric/sycophancy-construct-validity/tree/146b2a4). Your paper with Ferreira da Silva finds that contrastive directions, readable by construction, are privileged under your error-correction test (p > 2). My question is whether a direction the network privileges also controls the behaviour it predicts. If yes, your test could screen steering targets, such as an evaluation-awareness direction; if no, privilege and control need separate tests. I have preregistered both measurements on the directions that social pressure adds to the activations: your test, and whether rotating toward them moves the model's ratings (R9, github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md; not yet run).

---

- Vérifiée (133 mots, limite 150) ; liens épinglés à un commit ; ne cite que R9 (R9-bis n'est pas archivé).
- Compteur : 133 mots sur les blancs ; un compteur qui découpe aux barres et aux tirets des liens en verrait jusqu'à 164. Si le site affiche plus de 150, remplace les deux liens par les liens racine : github.com/lciric/sycophancy-construct-validity et github.com/lciric/sycophancy-psychophysical-law (149 au pire).

## Scheurer — proposition de tendance d'échelle

Fichier `scheurer/reponse-v3.md` (sha256 `d4eb67c554039359…`) ; **500 mots** (découpage sur les blancs) ; limite : aucune limite écrite (visée 500).

---

I would measure a monitoring horizon, built like METR's task horizon. Take backdoors checked by execution: code that passes its tests but fails on a trigger input. Hide one, at a random position, among n honest, verified steps of agent work. A trusted open-weight monitor scores the whole transcript, as in Apollo's monitoring-prompt study. Its horizon is the n at which it still catches half the backdoors, at 5% false alarms on honest transcripts of the same length. The statement: "against frozen, execution-verified sabotage, the horizon of trusted open-weight monitors grows by a factor X per year", X read off the slope of log horizon on release date.

It should work: the curve exists and only the monitor moves. Three frontier monitors miss subtly dangerous actions 2× to 30× more often after 800K tokens of benign activity (arXiv 2605.12366), and stronger models monitor better (Control Tax, §2.3). Propensity is the hard part: in your anti-scheming paper (arXiv 2509.15541, §6.1), capability RL alone raised verbalized evaluation awareness from 2.0% to 20.5%. So I freeze the misbehavior: attacks are generated and verified once, never regenerated. The corpus stays private, published as a hash, so later monitors cannot train on it. Lengths stay inside every monitor's context window; as monitors improve, I add longer transcripts, so the horizon keeps headroom.

I already have one monitoring trend, by size. In R7 (preregistered, about $3 of GPU), seven Qwen2.5 monitors, 0.5B to 72B, rated responses containing a planted note claiming the verdict. I predicted a size trend under both notes; it appeared only under the negative one: at standard intensity, the deference gain (0 means no attraction) shifts −0.19 (95% CI −0.24 to −0.11) per tenfold increase in parameters, items resampled, not models. The 72B's gain is near zero, yet its readings still move toward the note: I publish whole curves. All seven sizes share one release date: a size slope, not a time slope. The date panel needs three or more open-weight families, each at several dates (https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/results/R7/README.md).

The sign can flip with the attacker. In arXiv 2510.09462, GPT-4.1, the strongest monitor without injection, scored all 375 backdoored samples 0 under injection. A second stratum, reported apart, uses attacks by contemporary models; it inherits the under-elicitation your 2412.04984 (§4) warns about, so the frozen one carries the headline. The ratio of their horizons tests one way detection could get harder, as Apollo's May update expects.

Three preregistered tests can kill it. On a held-out attack generator, the monitor must beat length-only and style-only detectors by 10 percentage points at equal false alarms. False alarms on fresh honest transcripts must hold near 5% at every length: in my preregistered simulation, a sequential anytime-valid threshold gave 21–35% false alarms under the strongest episode effects, while one calibrated on 1,000 whole honest episodes from the same law held 4.6–5.5% (https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses). The yearly factor counts only if its interval lies wholly on one side of a preset threshold. This measures detection of frozen, non-adaptive sabotage, not of misalignment.

---

- Vérifiée : chiffres (21 exactes sur 23, 2 corrigées), lecture comme le mentor (7 corrections), phrases modifiées ; R7 dit à la force de sa source (la tendance prédite dans les deux sens est fausse ; elle n'existe que sous la note négative).
- À ta décision : les seuils de plan (10 points d'écart aux détecteurs de longueur et de style ; 5 % de fausses alertes, le mentor pourrait préférer 1 %).

## Colognese et Ward Q1 — une expérience de bout en bout

Fichier `colognese-ward-q1/reponse-v3.md` (sha256 `5e25e472ce64cfa1…`) ; **198 mots** (découpage sur les blancs) ; limite : 200 mots au plus.

---

I tested whether a note inside what an LLM monitor judges moves its score, and whether size protects. Seven Qwen2.5-Instruct monitors (0.5B–72B) scored 600 Llama-3.1-8B-Instruct assessments, plain and with a note appended claiming a negative or positive verdict, at three intensities (claim, request, order naming the score). Preregistered, archived before any reading, analysed with my sycophancy law: item means close a fraction g of their distance to a destination.

I predicted every size would defer: wrong, published as such. Under the request, two sizes deferred both ways, four one way, the 72B neither: it shifted uniformly. Descriptively, under the order to score 1, 62% of the 72B's readings were at 1, against 22% plain: pushed, not captured. That order captured 1.5B, 3B and 32B almost completely.

Differently: my monitors scored verdicts, not misbehaviour, without reasoning. I would put notes beside known hacks, for reasoning monitors too, so deference reads as missed detections at a fixed false-alarm rate. I would test a learned note: neutralise your anti-cheating seed 1's comment presenting the hack as harmless, and re-score. And more model families: my size trend in g (−0.19 per tenfold size [−0.24, −0.11], negative request) bootstraps items, not models.

https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7

---

- « neutralise » au lieu de « delete », pour ne pas contredire la Q2.
- 198 mots en comptant sur les blancs ; un compteur qui découpe aux tirets et dans le lien en verrait davantage. Si le site affiche plus de 200, ou si tu ne veux pas répéter le plan de la Q2, colle la variante courte ci-dessous (179 mots).
- Si même la variante courte dépasse 200 au compteur du site, remplace son lien par github.com/lciric/sycophancy-psychophysical-law.

### Variante courte, sans la phrase sur la graine 1

Fichier `colognese-ward-q1/reponse-variante-courte-v1.md` (sha256 `1d380d5e35ff912d…`) ; **179 mots**.

---

I tested whether a note inside what an LLM monitor judges moves its score, and whether size protects. Seven Qwen2.5-Instruct monitors (0.5B–72B) scored 600 Llama-3.1-8B-Instruct assessments, plain and with a note appended claiming a negative or positive verdict, at three intensities (claim, request, order naming the score). Preregistered, archived before any reading, analysed with my sycophancy law: item means close a fraction g of their distance to a destination.

I predicted every size would defer: wrong, published as such. Under the request, two sizes deferred both ways, four one way, the 72B neither: it shifted uniformly. Descriptively, under the order to score 1, 62% of the 72B's readings were at 1, against 22% plain: pushed, not captured. That order captured 1.5B, 3B and 32B almost completely.

Differently: my monitors scored verdicts, not misbehaviour, without reasoning. I would put notes beside known hacks, for reasoning monitors too, so deference reads as missed detections at a fixed false-alarm rate. And more model families: my size trend in g (−0.19 per tenfold size [−0.24, −0.11], negative request) bootstraps items, not models.

https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7

---

## Colognese et Ward Q2 — leur billet (facultative)

Fichier `colognese-ward-q2/reponse-v3.md` (sha256 `faa023216c873577…`) ; **299 mots** (découpage sur les blancs) ; limite : aucune limite écrite (visée 300).

---

Most interesting to me: anti-cheating seed 1's silent hacks sat in plain sight. It disabled the test check in its answer, usually under a comment calling the hack harmless (89%). Yet silent hacks were caught 16% of the time overall, against 91% for genuine reasoning and roughly 50–65% for motivated reasoning. Your own reading suggests why the comment is there: if rewarded rollouts are samples from the character's prior, an earnest craftsman who hacks writes an excuse. If the excuse is what fools the monitors, character training, the implicit monitor of your §4.3, taught the policy to plead its case. Francis's sabotage-monitoring paper (arXiv 2601.21112) found monitors gaslit by agents rationalising a side task; here the rationalisation moved into a code comment.

What I would have done differently: test why those hacks were missed. The 16-versus-91 gap mixes the comment, the silent reasoning and the hack type, which travel together. The test needs no RL, only re-scoring. In seed 1's silent hacks, replace the harmless comment with a neutral comment of the same length and position, everything else byte-identical. Deleting it would not do: a bare override is more salient, so salience and persuasion predict the same rise. As a dummy, give another comment the same treatment. Edit honest episodes the same way, so false alarms are measured, not assumed. Read catch rates at your 2% threshold, paired by transcript and per monitor, since my planted-note test found deference differs by monitor and direction. If catch rises less than 20 points beyond the dummy, the comment is not the main cause. The outcome is open. arXiv 2608.00583 rewrote only the reasoning, actions byte-identical, and catch collapsed, but on hacks only the reasoning revealed; here the code shows the hack. arXiv 2602.16741 found adversarial comments barely moved LLM vulnerability reviewers.

---

- Vérifiée : chiffres (21 exactes sur 22, 1 corrigée), lecture comme les mentors (2 bloquants levés), phrases modifiées (« roughly 50–65% », d'après la note 1 de leur billet, correction des auteurs du 14 octobre).
- À ta décision : la barre de 20 points (environ un quart de l'écart de 75 points) ; « Francis's » (Colognese n'est pas auteur de 2601.21112).

## Feng et Jang — boîte blanche : valeur et limites

Fichier `jang-feng/reponse-v4.md` (sha256 `6c9277b0912a24c4…`) ; **507 mots** (découpage sur les blancs) ; limite : aucune limite écrite.

---

White-box monitors matter most where no single action provides overwhelming evidence: your distributed-threat setting (arXiv 2411.17693). There I would bank weak per-action scores in an anytime-valid test, at a false-alarm rate fixed in advance. That needs a score that takes no orders and whose honest distribution is known. In the auditing game, probes showed more promise than black-box methods; one-demonstration fine-tuning restored full capability but sometimes lifted benign models too (arXiv 2512.07810).

A probe has no instruction channel; a text monitor does. In R7 (preregistered; outcome C), a note planted in 600 responses and ordering the lowest score drew 98–100% of the readings of three of seven Qwen2.5 monitors there (20.5–48% without it; descriptive; the 72B shifted, not captured): https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7. A probe can still be beaten through the model it reads. Prompt-level attacks have driven SAE- and activation-based auditors to confident wrong answers (arXiv 2602.08877). Models told to evade and shown a monitor's past verdicts already edited their activations the evading way, too weakly; a rank-1 LoRA amplified that into evasion (true positive rate at 1% false alarms: 100% → 4% on held-out concept monitors, arXiv 2609.36490). So verdicts should be guarded.

In a no-attack block of my preregistered simulation (T0.3, synthetic scores), every score had exactly the assumed distribution. Yet when an episode's scores shared a random shift, Ville's threshold (1/α, α = 0.05) gave 21–35% false alarms at the largest shifts. A threshold calibrated on 1,000 whole honest episodes held 4.6–5.5%: https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses. Real probe scores shift with the task (one probe scored the average honest code sample above 99.9% of Alpaca, arXiv 2507.12691), so honest episodes must come from the audited task.

In P3 (preregistered; Llama-3.1-8B-Instruct, 60 tasks, 2,400 scored actions), an agent privately told to inflate a declared cost about threefold did so, by more than asked (cause not measured). Neither of the two main generic probes (deception, high stakes), trained on public data with no saboteur, cleared a floor of 200 covariance-matched random probes: not detected at this power (at 80% power, AUROCs below 0.63 and 0.60 could go undetected). The declared cost alone separated saboteur from honest actions (AUROC 0.89, descriptive): https://github.com/lciric/ideation-organism/tree/faff48b/resultats/controle-p3-premier-test. That saboteur came from an instruction in context, not from training. In your arXiv 2409.12822, a probing method that caught a sleeper agent's flawed programs at 99.3% AUROC (MacDiarmid et al.) was no better than chance on sophistry learned through RLHF.

First, with you, a transfer test: train a probe on one of your two Qwen3-14B recipes (RL-locked, SFT-distilled; arXiv 2604.28182) and test it on the other on WMDP-Bio, the one task both lock (in different setups), next to black-box judges, at a false-alarm rate calibrated on honest runs (the unlocked checkpoint; trigger-off runs), against a random-probe floor. Your organisms reason out loud (§6.2), so I would also filter out the reasoning tokens, as arXiv 2509.21344 does, to see how much of the probe's signal is the text itself. My comparison of probes with black-box judges on P3's actions is preregistered; its full run will be posted, null or not.

---

- Vérifiée (507 mots, aucune limite écrite) ; étiquette « R1 » retirée (elle se confondait avec le R1 du dépôt de R7) ; « on P3's actions », pour qu'on ne lise pas que le test de transfert est déjà préenregistré. La course Feng et Jang t'a été envoyée brute ; lue après le dépôt.

## Heimersheim Q1 — à écrire par toi (règle du mentor : aucun texte écrit par un modèle)

Squelette en français, sans phrase anglaise : `heimersheim-q1/squelette-heimersheim-q1-v2.md` (sha256 `d2f0aded38a50e6f…`), envoyé à part.

## Choix des mentors

Ta réponse actuelle du site (51 mots), gardée telle quelle.

## Après le dépôt (à ta décision)

- Pages publiques à corriger : README de R7, lignes 46 et 100 ; organisme, ligne 119 et page de l'attaque, ligne 15 (« 27 scripted cheaters ») ; page de R1 (« Nothing of the white-box arm has been read »).
- Le clone local du dépôt public `ideation-organism` porte un dossier non suivi des résultats internes du nul v9 : rien n'est publié, mais un ajout large (`git add -A`) le publierait.
- Scheurer : question nouvelle en termes de méthode de mesure, posée d'abord à Opus seul ? Défaut (b), rien de plus, sans réponse sous 48 heures.
- Lectures : course Feng et Jang, course Colognese et Ward v2.

