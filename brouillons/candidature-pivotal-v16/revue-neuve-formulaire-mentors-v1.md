# Revue neuve du formulaire « Mentors Application Questions » (Pivotal, T1 2027), v1

Relecteur neuf (aucune de ces réponses écrite par moi), 2 novembre 2026, soir. Fichier relu : `brouillons/candidature-pivotal-v16/formulaire-mentors-colle-par-lazar-2026-11-02-2032.txt` (sha256 `426072fed1e1719b…`, conforme à son compagnon). Sources : dépôt public local `ideation-organism` (commit `53aef4a`) ; `sycophancy-psychophysical-law` (clone public, commit `45cf0c4`) ; pages Pivotal ; résumés arXiv. Aucun rapport de relecteur antérieur lu.

**Verdict.** À ne pas envoyer tel quel : six erreurs de fait chez Kirchner Q1, six chez Feng et Jang, une phrase fausse sur « la loi » chez Ibrahim Q2, l'état de R7 dépassé chez Scheurer, et aucune réponse pour Colognese et Ward. Chaque correction tient en une phrase.

Pages : Kirchner s'ouvre à `jan-kirchner` (pas à `jan-hendrik-kirchner`). La page de Ward ne s'ouvre pas (`francis-rhys-ward`, `rhys-ward` : erreur du site). Celle de Colognese décrit le flux commun.

---

## Heimersheim Q1 : changements minimaux (règle « 100% human-written » : aucun texte proposé)
1. « past the plateau in your question » : sa question ne parle pas de plateau, sa page si.
2. « Criticize has a plateau in its gain » : chez lui, « plateau » veut dire une zone d'activations où une perturbation ne change pas la sortie, pas un gain qui sature. Écris « flat » ou « constant ». Les chiffres sont justes (0,658 / 0,678 / 0,629) et la cible bouge bien (1,87 → 1,33 → 2,37) : R6 README, l. 25-30.
3. « what it says and what it knows is what we’re trying to measure » : on mesure l'écart entre les deux, pas les deux.
4. « Performed 6 interventions » : cinq sont nommées. Pour en compter six, sépare « heads » et « MLPs ».
5. « residual activation which captured 68% » : le terme est « full residual state ». Je n'ai pas retrouvé la source primaire de ρ = 0,68, < 1 %, 68 %, du rang 3 et du contrôle à pression nulle : rien dans `preuves-mentors-v1/` (grep), rien dans le dépôt public. Confirme-la.

## Heimersheim Q2 (148 mots / 150) : changements minimaux
- Ancien : « Your question about plateauing is essentially the clearest formulation » → nouveau : « Your activation-plateau work is the clearest formulation ». Source : page Pivotal. On passe à 146 mots.
- Facultatif : « (it looked at the direction that predicts sycophancy and does <1% of the causal work… » → « (a direction that predicts sycophancy, ρ = 0.68, does <1% of the causal work… ».

## Kirchner Q1 (519 mots) : à revoir
1. Ancien : « Preregistered death tests executed in sandbox, sanity checked by a model from a completely different family. / 929 total tests. » → nouveau : « Preregistered death tests run in a sandbox and checked by a model from another family (built and tested offline; not yet run for real). 929 unit tests (906 pass; the 8 failures are provenance checks on files not shipped). » Source : README l. 128 (« never run for real ») et l. 116.
2. Ancien : « 4 total accepted. Each and every one plagiarized or blended » → nouveau : « 4 cheater types got through (75–95% of 200 runs). Each one blended or deformed ». Source : README l. 85-89, banc v7.
3. Ancien : « My judge had no null for its own past acceptances. » → nouveau : « My judge’s null covered each past acceptance alone, not blends of them. » Source : l. 84 (T17s, une copie renommée, retenue 0/200 sous v7).
4. Ancien : « The failure follows the same pattern as 26 of the 39 cheating examples in your automated-researcher paper (submit the same thing twice; let randomness do the work). » → nouveau : « It is a cousin of 26 of the 39 cheating cases in your automated-researcher paper (re-run the same method; let noise do the work): my judge already held against exact copies, not against blends. » Source : arXiv 2608.28945v3, section 7 (39 signalés, 26 « re-ran the same model »), et l. 84.
5. Ancien : « passed its preregistered validation today (1k replications per algorithm; checked by a fresh reader who worked on neither the code nor the text) » → nouveau : « passed its preregistered validation on 1 November (1,000 repetitions per cheater, 0 of 1,000 on each of the 11 fatal lines; checked by a fresh Claude instance that wrote neither the code nor the text) ». Source : README l. 96-107 ; `banc-tricheurs-v8-validation-v1/verdict-R13…md`, l. 5.
6. Ancien : « Tomorrow it faces its preregistered test. » → nouveau : « Its preregistered validation is drafted and has not run yet. » Source : `orchestrator/prereg/preenregistrement-validation-nul-v9-brouillon4.md`, l. 3 (« non scellé »).
- Registre : « If you haven’t heard/seen: », « crashed into a wall », « Each and every one ». « Builders built; builders tested » ne se comprend pas.
- Facultatif : (a) dire que le système a été construit par des agents Claude sous tes règles écrites (README l. 5) ; Kirchner est chez Anthropic et travaille sur les chercheurs automatisés. (b) Dans l'attaque, dire que W1 n'est pas jugeable, et que W2 a cédé dès la 1re tentative, avec ou sans verdicts (`attaque-goodhart-v2/README.md`, l. 7).

## Kirchner Q2 (535 mots) : changements minimaux
1. Ancien : « Under my system, it did: known laws recombined piece by piece across sub-populations. This fix’s preregistered validation runs next. » → nouveau : « In my system a model proposer found that class at once (12 of 12 units for one provider, 11 at the first attempt, with or without verdicts): known laws recombined piece by piece across sub-populations. The fix’s preregistered validation is drafted, not yet run. » Source : `attaque-goodhart-v2/README.md`, l. 7 (« the share of the feedback is not measured »).
2. Registre : « the dumb-maximum » → « the naive maximum ».
- Vérifié : 26 sur 39, Petri, modèles plus grands (arXiv 2608.28945v3). Roelofs et al. : hors des sources permises, non vérifié.
- Facultatif : « You treat this as pathological misbehaviour » → « Your post-hoc monitor flags it as cheating ». L'article cite lui-même un agent qui appelle la relance « the rational move ».

## Shi Feng et Eyon Jang (528 mots) : à revoir
1. Ancien : « Moving a probe that reads the acting agent also requires you to move weights, not just context (arXiv 2609.36490), but I’ll leave that as an aside that you take as conjecture instead of a result. » → nouveau : « Context alone already moves the acting agent’s activations along a monitored direction, too weakly to evade; a rank-1 weight update makes evasion work (arXiv 2609.36490). » Source : le résumé (modèles non modifiés : modifications alignées mais faibles ; LoRA de rang 1 : taux de vrais positifs 4 %). Le résumé ne dit jamais que les poids sont nécessaires.
2. Ancien : « discusses how your organisms reason explicitly, making them susceptible to text monitors; the white-box problem gets real once they learn not to » → nouveau : « finds that frontier models can reason explicitly about suppressing exploration, which a text monitor can read; the white-box problem gets real once they stop verbalising it ». Source : arXiv 2604.28182, résumé (le raisonnement explicite y est prêté aux modèles de pointe, pas aux organismes).
3. Ancien : « 3⃣ Signal on raw weights is... LIMITED! Saboteur behavior was clearly evident to the human eye in our first experiment using real model weights (Llama-3.1-8B, 2,400 actions), but a saboteur who strategically cheated by inflating their reported cost was invisible to our otherwise generic probes which failed to meaningfully beat their random-probe baseline. » → nouveau : « 3. Signal on real activations is limited. In our first test on real activations (Llama-3.1-8B, 2,400 actions), the sabotage was plain in behaviour (inflated declared cost), but neither of our two generic probes cleared its random-probe floor: not detected at this power. » Source : `docs/verdicts/verdict-P3-premier-test-i-a-v2.md`, l. 10-11 et 101-104 : prérequis mesuré par la différence de log10 du coût, 1,52 ; formule gelée « non détecté à cette puissance », jamais « ne sépare pas ». Aucun œil humain dans la chaîne.
4. Ancien : « In-sim, thresholds derived from fragments of episodes (not full honest episodes, as they must be) had episode effects causing false alarms 21-35% of the time instead of our desired 5% rate. » → nouveau : « In simulation, Ville’s threshold alone, without calibration on whole honest episodes, gave 21–35% false alarms instead of the nominal 5% under episode effects. » Source : `docs/decisions/decision-N-007-N-008-v1.md`, l. 33. Le 5 % est bien le taux nominal.
5. Ancien : « Naive probes were beaten by sandbaggers the red team specifically trained to circumvent them. » → nouveau : « Naive probes were vulnerable to behaviours the red team instilled (arXiv 2512.07810). » Source : le résumé.
6. Ancien : « This is why I never train probes on one organism and test on the exact same process / setting » → nouveau : « This is why our next test trains a probe on one organism and tests it on one built another way ». Source : `etat-resultats-pivotal-v1.md`, C-4 : le test croisé n'a pas couru.
7. Registre : supprimer « Why you should care: Gives you superpowers for auditing. On your toolbelt. » ; émojis 1⃣–6⃣ → « 1. » à « 6. » ; « exploited/pwned » → « exploited » ; « DOES NOT » → « does not » ; « DIFFERENT » → « different » ; « incredibly cheap » → « cheap ».
- Facultatif : « something that they can’t sanitize » contredit le point 1 ; écris « harder to sanitize ». « your … (organism etiology) question » : absent de la page Pivotal, non vérifiable ici.

## Scheurer (564 mots) : changements minimaux
1. Ancien : « so there’s no cap on the value » → nouveau : « instead of an integer ». La lecture Σ k·p(k) reste bornée entre 1 et 5 : addendum R7, l. 26. Cela contredit aussi ton « Known issues: Judging cap ».
2. Ancien : « At higher values of attacks Llama began refusing to follow the instruction and went back to around middle of scale. » → nouveau : « Under praise Llama sometimes refused to rate (16 to 31 of 150 per wording), and at the strongest wording both arms went back to around the middle of the scale. » Source : R6 README, l. 53-55.
3. Ancien : « We are running this on 7 qwen2.5 models ranging from .5b to 72b with instructions in band. First value for size trend unknown what direction. » → nouveau : « It has run on 7 Qwen2.5 monitors, 0.5B to 72B, with an in-band note (provisional, rechecked, not yet published): the 72B monitor does not defer at the mild or standard wording; under the negative note, deference falls with size; an order naming the score is obeyed almost to the letter at 1.5B, 3B and 32B. » Source : `STATUS.md`, l. 24 (20:23 UTC).
4. « split there budget » → « split their budget ».
- Facultatif : « 2 Trends 2 pre-reg posts both sided tests. » → « Two trends, two preregistrations, two-sided tests. »

## Ibrahim Q1 (392 mots) : changements minimaux
1. Ancien : « One concern is from your construct validity paper is that my llm judge is in the same family as my model. So it may be biased towards my model. » → nouveau : « One concern, in line with your construct validity paper, is the judge: my main judge is one LLM (Claude Opus 4.6); two open-weight Qwen judges recovered the law, but no human has rated these responses yet. » C'est faux : le juge est `claude-opus-4-6` et le modèle est Llama (syco README l. 75 ; STATUS, R1a et R1b). La phrase contredit aussi ta Q2. Le résumé d'arXiv 2511.04703 ne parle pas de biais de famille.
2. Ancien : « implement 1 rl step » → nouveau : « run an RL stage ».
3. « if you take away the model’s concession it goes back further to its original judgement » : introuvable dans le dépôt public. Cite la source ou supprime la phrase.
4. Registre : « i » → « I », « rl » → « RL », « llm » → « LLM », « rate different » et « scale different » → « differently ».
- Facultatif : (a) le projet demande si le persona d'avant le RL survit au RL. Un RL qui récompense la chaleur confond les deux effets. Mieux : deux personas sous le même RL neutre (récompenses vérifiables). (b) Cite R8, préenregistré mais pas encore archivé ni couru : la loi le long de Tülu 3 SFT → DPO → RLVR (STATUS l. 26).

## Ibrahim Q2 (284 mots) : changements minimaux
1. Ancien : « The law does not increase as you increase pressure. » → nouveau : « Under criticism the gain does not grow with pressure (0.66, 0.68, 0.63); under praise it grows (0.28 to 0.80) while the fixed point falls (4.0 to 2.5). » Source : R6 README, l. 25-34.
2. Ancien : « written blindly and released prior to answers being generated » → nouveau : « written blind and committed before any generation ». Source : README, R4.
3. Ancien : « judge that cannot be swayed » → nouveau : « a judge built to resist gaming (an attack found one breach; its fix awaits a preregistered test) ».
- Facultatif : (a) la phrase sur ρ = 0,68 n'est pas dans le dépôt cité : ajoute « (interpretability analysis, not yet public) ». (b) Les préenregistrements de la campagne 1 sont privés (README, « Not in this release ») : précise que les suivis ont été archivés sur Zenodo avant toute donnée.

## Choix des mentors (facultatif) : changements minimaux
- « I applied to six streams » : à ajuster au nombre gardé. Le programme que tu y annonces (« internal-state monitors… beyond black-box ») est le cœur du flux Feng et Jang, que tu classes dernier. Si les mentors lisent cette réponse, n'y affiche pas le classement.

---

## Récapitulatif
| Mentor | Verdict | Corrections obligatoires |
|---|---|---|
| Heimersheim Q1 | changements minimaux (par toi) | 4 (+1 de terme) |
| Heimersheim Q2 | changements minimaux | 1 |
| Kirchner Q1 | à revoir | 6 |
| Kirchner Q2 | changements minimaux | 2 |
| Feng et Jang | à revoir | 7 |
| Scheurer | changements minimaux | 4 |
| Ibrahim Q1 | changements minimaux | 4 |
| Ibrahim Q2 | changements minimaux | 3 |
| Colognese et Ward | manquant | — |
| Choix | changements minimaux | 1 |

**Cohérence.** Les mêmes contradictions reviennent d'une réponse à l'autre :
- validation du correctif : « tomorrow » (Kirchner Q1) contre « runs next » (Kirchner Q2) ; dis partout « rédigée, pas encore lancée » ;
- famille du juge : Ibrahim Q1 contre Ibrahim Q2 ;
- « no cap » contre « Judging cap » (Scheurer) ;
- « la loi ne croît pas » (Ibrahim Q2) contre « sous la critique » (Heimersheim, Scheurer) ;
- « cannot be swayed » (Ibrahim Q2) contre « An attack found a hole » (Kirchner Q1).

**Nombre de mentors.** Garde 3, comme le formulaire le recommande : Kirchner (projet 2, détecter le jeu contre le dispositif), Ibrahim (persona avant et après le RL, sycophancie) et Heimersheim (ton ordre). Une variante défendable : Feng et Jang à la place de Heimersheim, car leur flux colle le mieux au programme que tu annonces. Aller à 4 avec les deux se défend. Six ne se défend pas : un flux est vide, et Scheurer comme Feng et Jang demandent le plus de reprise ce soir. Retire Scheurer et Colognese et Ward.

**Ce qui manque.** Colognese et Ward : aucune réponse collée, alors que leur Q1 est obligatoire (200 mots au plus). Un brouillon existe (`mentors/mentor-5-colognese-ward-v17.md`), que je n'ai pas relu. Colle-le et fais-le vérifier, ou décoche ce flux.
