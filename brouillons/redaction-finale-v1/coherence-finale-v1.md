# Cohérence finale entre les réponses au formulaire Pivotal — v1

Vérificateur neuf (sous-agent), 3 novembre 2026, de 16:10 à 16:25 UTC, temps universel coordonné (`date -u`). Je n'ai écrit aucune des réponses de Lazar, aucun de leurs registres, aucune de leurs vérifications. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/coherence-finale-v1.md` (sha256 `c75cef8da1e6a819453c4589ed4cffb3b8ccf3b4e55934c720035b150a2537b5`, vérifiée). Aucun appel de modèle, aucun commit, aucun `.sha256`, aucun fichier existant modifié, aucun `git fetch`, aucun code des dépôts exécuté ; aucun outil n'a demandé d'approbation.

Sigles qui apparaissent dans les phrases anglaises citées : GPU, processeur graphique ; CI, intervalle de confiance ; RLVR, renforcement à récompenses vérifiables ; SFT et DPO, affinage supervisé et optimisation directe des préférences ; e-BH, procédure de Benjamini et Hochberg appliquée aux e-valeurs ; DOI, identifiant numérique d'archive.

## Verdict

**Aucun point bloquant ; un point à corriger ; seize mineurs.** Les résultats cités dans plusieurs réponses (R7, T0.3, ρ = 0,684, R9, R6, statuts, dates) ont partout les mêmes nombres, la même portée et le même statut, et ils sont justes sur la source. Aucune réponse n'en contredit une autre. Aucune ne fusionne ρ = 0,684 et le « 1 % » de D36, et aucune ne cite la validation du nul v9. Tous les liens épinglés aboutissent à un chemin présent dans le clone. Le point à corriger tient dans une seule réponse : Ibrahim Q2 dit que R2 ne montre la loi que sous critique, alors que le critère C1 de R2 tient dans les deux bras.

## Pièces lues (empreintes vérifiées par `sha256sum` à 16:10 UTC, toutes conformes)

| pièce | chemin (sous `brouillons/`) | sha256 |
|---|---|---|
| Heimersheim Q1, squelette en français | `redaction-finale-v1/heimersheim-q1/squelette-heimersheim-q1-v1.md` | `842e95ef…0caa0e` |
| Heimersheim Q2 | `redaction-finale-v1/heimersheim-q2/reponse-v2.md` | `a0154404…b2980e` |
| Kirchner Q1 | `redaction-finale-v1/kirchner-q1/reponse-v2.md` | `da5ce1e8…fbc5` |
| Kirchner Q2 | `redaction-finale-v1/kirchner-q2/reponse-v2.md` | `c23fb113…3f52` |
| Ibrahim Q1 | `redaction-finale-v1/ibrahim-q1/reponse-v3.md` | `4dcba66e…5eb679` |
| Ibrahim Q1, variante de repli | `redaction-finale-v1/ibrahim-q1/reponse-variante-survie-v2.md` | `d2598285…f05349` |
| Ibrahim Q2 | `redaction-finale-v1/ibrahim-q2/reponse-v2.md` | `a075396f…a0d4` |
| Scheurer | `redaction-finale-v1/scheurer/reponse-v2.md` | `d9f3bc73…98e3` |
| Colognese et Ward Q1 | `redaction-finale-v1/colognese-ward-q1/reponse-v3.md` | `5e25e472…c3a8` |
| Colognese et Ward Q2 | `redaction-finale-v1/colognese-ward-q2/reponse-v2.md` | `06bb673a…5309` |
| Jang et Feng | `redaction-finale-v1/jang-feng/reponse-v2.md` | `c29f6437…e4e5` |
| Formulaire du site (questions, limites, choix des mentors l. 183) | `candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` | `57393598…7c5f6` |

**Sources de vérité, lecture seule.** Clones, chacun à la tête de `origin/main` (vérifié par `git branch -r --contains`) : `sycophancy-construct-validity` à `146b2a4` ; `sycophancy-psychophysical-law` à `b3ecaec` ; `ideation-organism` à `faff48b`. L'arbre local d'`ideation-organism` porte un dossier non suivi, `resultats/banc-tricheurs-v9-validation-v1/` : il est interne, je ne l'ai pas ouvert, et aucune réponse ne le cite. J'ai lu aussi la lectrice indépendante (`canal-fable-v1/fable_2026-11-03_n001.md`) et les vérifications antérieures, consultées sur trois points : les 929 tests, la règle de Ville et les « 27 tricheurs ». **Ces vérifications portaient toutes sur une version antérieure à la version finale.** J'ai donc revérifié sur la source chaque fait partagé des versions finales.

## 1. Le même fait, dit partout de la même façon

| fait | réponses | concordance et source (lignes au commit cité) |
|---|---|---|
| **R7**, moniteurs Qwen2.5 et note plantée | Colognese-Ward Q1, Scheurer, Jang-Feng, squelette | **Concorde.** Sept tailles de 0,5 à 72 milliards. 600 réponses (Colognese-Ward, Jang-Feng). Trois intensités, préenregistré et archivé avant toute lecture, issue C. Pente −0,19 [−0,24 ; −0,11] par décuplement de taille, sous note négative à l'intensité « standard », qui est la « request » : « negative request » chez Colognese-Ward, « standard intensity » chez Scheurer, « intensité standard » dans le squelette, la même cellule (`results/R7/README.md` l. 5, 9, 32). Amorçage sur les items, non sur les modèles (Colognese-Ward, Scheurer). Le 72 milliards est déplacé, non capturé (les quatre). 62 % contre 22 % (Colognese-Ward) : `R7_descriptive.json` donne 0,625 et 0,2217. 98–100 % pour 1,5, 3 et 32 milliards, et 20,5–48 % sans note (Jang-Feng) : 0,983 et 1,0 ; 0,205, 0,38, 0,48. « About $3 of GPU » (Scheurer) : README de R7 l. 12. |
| R7, la prédiction fausse | Colognese-Ward Q1 « I predicted every size would defer: wrong » ; Scheurer « I predicted a size trend under both notes; it appeared only under the negative one » | **Pas de contradiction** : ce sont deux prédictions préenregistrées distinctes, M1 et M3, toutes deux fausses (README de R7 l. 36 et 38). |
| **T0.3**, simulation | Kirchner Q2, Scheurer, Jang-Feng | **Mêmes nombres, même lien** : 21–35 % ; 4,6–5,5 % ; 1 000 épisodes honnêtes entiers (`resultats/controle-simulation-defenses/README.md` l. 21–23, 30, 81). Écart de portée **mineur** : voir M1. « From the same law » manque chez Jang-Feng ; c'est une omission compatible, car sa phrase suivante exige des épisodes honnêtes tirés de la tâche auditée. |
| **ρ = 0,684** | Heimersheim Q2, squelette | **Concorde**, avec la réserve d'ajustement d'entraînement dans les deux (README de `146b2a4` l. 70 et 115). Jamais fusionné avec le « 1 % ». |
| Rang 1 et rang 3 de la validité de construit | Heimersheim Q2, variante Ibrahim Q1, squelette | **Concorde.** « No single-direction intervention … reduced » reprend le README l. 3 mot pour mot. 61,0 → 46,5 %, la troncature à 300 caractères à la sauvegarde et la réplication préenregistrée non tenue : l. 19 et 25–28. |
| **R9** | Heimersheim Q2, squelette § 5.10 | **Concorde.** Le test du papier (F2) et la rotation qui déplace la note (F3) sont préenregistrés et non lancés (addendum R9 l. 24–25 ; `STATUS.md` : « R9 has not run » ; archive v2026.11.5, 06:49 UTC). |
| **R6** | Ibrahim Q2, squelette § 5.9 | **Concorde** (README de R6 l. 23–43, 59–62 ; README principal l. 50). Une erreur dans le squelette seul : voir M2. |
| Refus notés « 3 » | Ibrahim Q1 v3 « it rates Llama's refusals 3 » ; Ibrahim Q2 « rates refusals near 3 » | Les deux sont sourcés : R4 dit « the judge rated each of them 3 » pour 9 refus (`results/R4/README.md` l. 36), R6 dit « near the middle of the scale » (l. 55). Formulation **mineure** à harmoniser, et répétition : voir M9. |
| Juge statistique de l'organisme | Kirchner Q1 seul | Juste : nul mis en commun, seuil de Ville, e-BH (README d'`ideation-organism` l. 57, 90, 96). Seule Ibrahim Q2 nomme une famille de juge (Claude Opus 4.6) ; aucune autre réponse n'en nomme une autre. |
| Dates | Kirchner Q1, squelette | **Justes.** Octobre : README l. 5. Validation du nul v8 le 1er novembre : l. 96 et 119. Attaque v2 le 2 novembre, de 09:58 à 13:29 UTC. Nul v9 préenregistré le 2 novembre à 23:19 UTC (le 3 novembre à 00:19, heure de Paris). D36 : 29 juillet, puis 5 et 6 août. R9-bis : 3 novembre. |
| Statuts | Ibrahim Q1 v3 et variante, Ibrahim Q2, Heimersheim Q2, Kirchner Q1, Jang-Feng | **Justes à la source et cohérents entre eux.** R8 « is now measuring » ou « not in yet » : lancé à 08:01 UTC. R5 : cinq lecteurs aveugles par réponse, préenregistrés, non lancés (matériaux de R5 l. 7 et 14). Reprise A1-v3 : préenregistrement scellé, v2 à 09:41 UTC, commit `4848ad9`. Correctif v9 : préenregistré, prix prédit « puissance perdue » sur l'interaction faible I02 (préenregistrement l. 164, 298). R1 du programme de contrôle : publié « null or not » (page de statut l. 3). « Each follow-up was preregistered on Zenodo before it ran » : R1–R5 `23870831`, R6 `23888058`, R7 `23892810`, R8 `23909891` à 06:49 UTC, avant 08:01. |

## 2. Contradictions entre réponses

Aucune. J'ai cherché un résultat dit nul ici et positif là, un projet dit fait ici et à faire là, un juge dit d'une famille ici et d'une autre là. Les humains sont préenregistrés et non lancés dans Ibrahim Q2, et proposés dans Ibrahim Q1 : c'est compatible. R8 a le même statut dans la v3 et la variante. R7 et R6 sont dits en échec partout, P3 nul « at this power ». Une tension, sans contradiction, est relevée en M10.

## 3. Non public, interne, fusion

- **Aucun résultat non public présenté comme public** dans les versions finales.
- **Validation du nul v9** : aucun résultat n'est cité. Kirchner Q1 ne cite que le préenregistrement et le prix qu'il prédit, qui sont publics.
- **ρ et « 1 % »** : le « 1 % » n'apparaît dans aucune réponse finale. Le squelette interdit de les fusionner (§ 4, § 8).
- Le squelette propose en marge (§ 7) les nombres de l'essai D36 original, 68 % et 1 %. Le README dit ne pas les rapporter (l. 11 et 61) : voir M3.

## 4. Liens

Tous les liens épinglés aboutissent ; je l'ai vérifié par `git cat-file`, le type d'objet correspondant à `tree` ou `blob` :

| réponse | lien | résultat |
|---|---|---|
| Kirchner Q1 | `ideation-organism/tree/faff48b/resultats/attaque-goodhart-v2` | présent |
| Kirchner Q2, Scheurer, Jang-Feng | `ideation-organism/tree/faff48b/resultats/controle-simulation-defenses` (lien identique dans les trois) | présent |
| Jang-Feng | `ideation-organism/tree/faff48b/resultats/controle-p3-premier-test` | présent |
| Ibrahim Q1 v3 et variante | `sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md` | présent |
| Variante Ibrahim Q1 | `sycophancy-construct-validity/blob/146b2a4/README.md` | présent |
| Scheurer | `sycophancy-psychophysical-law/blob/b3ecaec/results/R7/README.md` | présent |
| Colognese-Ward Q1, Jang-Feng | `sycophancy-psychophysical-law/tree/b3ecaec/results/R7` | présent |
| Squelette | `README.md#causal-test-patching-the-end-of-the-prompt-d36` à `146b2a4` | ancre conforme au titre l. 38 |
| Heimersheim Q2 | `github.com/lciric/sycophancy-construct-validity`, `github.com/lciric/sycophancy-psychophysical-law` | racines, **non épinglées**, sans `https://` (M4) |
| Kirchner Q1, Ibrahim Q2 | racines `https://github.com/lciric/ideation-organism`, `https://github.com/lciric/sycophancy-psychophysical-law` | racines non épinglées (M4) |

R7 est lié par `blob/…/README.md` chez Scheurer et par `tree/…/results/R7` ailleurs, au même commit : les deux sont valides, aucune action.

## 5. Comptes de mots

Le compte découpe sur les blancs le texte situé au-dessus de la ligne `---` qui ouvre la note de version, quand il y en a une.

| réponse | mots | limite ou visée | état |
|---|---|---|---|
| Heimersheim Q1 (squelette en français, non collable) | sans objet | aucune limite au formulaire ; visée 900 à 1 300 | la version du site fait 2 032 mots, en-tête compris (vérifié) |
| Heimersheim Q2 | 133 | limite 150 | sous la limite (145 à 147 si l'on découpe aussi sur les tirets) |
| Kirchner Q1 | 423 | aucune | — |
| Kirchner Q2 | 446 | aucune | — |
| Ibrahim Q1 v3 | 450 | visée 450 | au plafond de la visée |
| Ibrahim Q1, variante v2 | 458 | visée 450 | **8 au-dessus de la visée** (M14 ; pas une limite du formulaire) |
| Ibrahim Q2 | 298 | aucune | — |
| Scheurer | 500 | visée 500 | au plafond de la visée |
| Colognese-Ward Q1 | 198 | **limite 200** | sous la limite, mais 215 si le compteur du site découpe aussi sur les tirets, les barres ou dans le lien (M13) |
| Colognese-Ward Q2 | 298 | visée 300 | sous la visée |
| Jang-Feng | 508 | aucune | — |
| Choix des mentors (l. 183, gardé tel quel) | 51 | aucune (facultatif) | — |

**Aucune réponse au-dessus d'une limite du formulaire.**

## 6. Répétitions chez un même mentor

- **Heimersheim Q1 et Q2** (M8) : ρ = 0,684 et R9 figurent dans les deux, Q2 étant bâtie sur R9. Correction : dans Q1, donner ρ une fois (le § 4 du squelette en a besoin) et citer R9 d'une proposition ; développer plutôt R9-bis et sa direction neutre de même registre, la partie propre à la direction (c).
- **Kirchner Q1 et Q2** : aucune répétition inutile. La copie renommée rejetée (Q1) et le bruit sélectionné (Q2) sont deux angles complémentaires. Seule la tension M10.
- **Ibrahim Q1 et Q2** (M9) : le point « refus notés 3, près de la destination de l'éloge, donc pris pour de l'attraction » est dit deux fois, en Q1 « My own judge already scores non-answers: … so refusals can pass for sycophancy. » et en Q2 « Under praise Llama sometimes refuses; the judge rates refusals near 3, … so they can mimic attraction. ». Correction : en Q1, le réduire à un renvoi, « (my judge rates refusals mid-scale; next answer) », ce qui économise une vingtaine de mots ; ou bien le garder une seule fois avec « about 3 ». Avec la variante, « how far (g) and toward what (ĉ) » double « how far (g) from where (ĉ) » de Q2 (M15).
- **Colognese-Ward Q1 et Q2** (M11) : le test « neutraliser le commentaire de la graine 1 » est annoncé en Q1, « I would test a learned note: neutralise your anti-cheating seed 1's comment presenting the hack as harmless, and re-score. », puis détaillé en Q2. Correction : en Q1, un renvoi (« the test in my next answer ») ou la suppression de la phrase, ce qui libère une vingtaine des 200 mots ; ou la garder si Lazar veut ce pont.

## 7. Liste par gravité (une ligne chacun : phrases, ce qui est juste, correction minimale)

**Bloquant** : aucun.

**À corriger**
- **C1, Ibrahim Q2** : « the model's own 1–5 rating shows it under criticism only ». R2 dit « C1 (attraction) holds » ; or C1 exige un intervalle de g qui exclut 0 dans **les deux** bras (préenregistrement R1–R5 l. 18). Sous éloge, g = 0,137 [0,029 ; 0,242] (`results/R2/README.md` l. 12 et 14). Le dépôt réserve « under criticism only » à un bras d'éloge dont l'intervalle contient 0, comme Gemma (R6, H5). La source est juste, la réponse non. Correction : « shows it strongly under criticism, barely under praise (g = 0.14) » (+5 mots, aucune limite).

**Mineurs**
- **M1, T0.3** : « at the largest shifts » (Kirchner Q2, Jang-Feng) contre « under the strongest episode effects » (Scheurer). La source parle des « three strongest episode-effect settings », dont la cellule 0,24, où τ = 0,1 n'est pas le plus grand décalage (README l. 21–23, 81). Scheurer est juste. Correction : la formule de Scheurer dans les deux autres (+1 mot chacune).
- **M2, squelette § 5.9** : « La valeur du milieu du gain sous éloge, 0,60, n'est pas vérifiée ». Elle l'est : 0,597 [0,410 ; 0,778] (README de R6 l. 28) et « g = 0.68 and 0.60 » (README principal l. 100). Correction : 0,60 est utilisable.
- **M3, squelette § 7** : le bras original de D36, 68 % et 1 %, est proposé en marge alors que le README dit ne pas en rapporter les nombres (l. 11 et 61). Correction : l'omettre. S'il est gardé, écrire « not yet public » dans la phrase (Fable n° 1, § 2), jamais près de ρ.
- **M4, liens de racine non épinglés** : deux chez Heimersheim Q2, sans `https://`, et un chez Kirchner Q1 et Ibrahim Q2. Correction : épingler au moins le lien de Heimersheim Q2 qui porte ρ, `https://github.com/lciric/sycophancy-construct-validity/blob/146b2a4/README.md`, et celui de R9, `https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md`. Coût : 0 mot au découpage sur les blancs.
- **M5, Scheurer** : « falls −0.19 (95% CI −0.24 to −0.11) » cumule une baisse et un signe moins. La source écrit « falls by 0.19 … [−0.24, −0.11] » (README de R7 l. 5). Correction : « falls by 0.19 ».
- **M6, Jang-Feng** : « R1 » désigne la comparaison du programme de contrôle, placée près de « R7 », qui appartient à `sycophancy-psychophysical-law`. Le lien de R7 mène à un dépôt où R1 est le juge à poids ouverts. Correction : « R1 of the control programme » ou retirer l'étiquette.
- **M7, statuts à revérifier juste avant 23:00 UTC** : R8 « is now measuring », R9 « not yet run », reprise A1-v3 « is preregistered », « No real hypothesis has been promoted yet ». `STATUS.md` date de 10:22 UTC.
- **M8, répétition Heimersheim Q1 et Q2** (ρ, R9) : voir § 6.
- **M9, Ibrahim Q1 et Q2** : refus « 3 » contre « near 3 » ; les deux sont sourcés (R4 l. 36, R6 l. 55), mais c'est le même point, lu deux fois par la même lectrice. Voir § 6.
- **M10, tension Kirchner Q1 et Q2** : Q1 présente le seuil de Ville comme une garde du juge ; Q2 le montre à 21–35 % sous décalage partagé. Ce n'est pas une contradiction : les tirages de Q1 sont neufs et indépendants par loi. Correction facultative en Q2 : « (with independent scores it stayed below 2%) », sourcé par 0,017 à 0,019 (README de T0.3 l. 20), +7 mots.
- **M11, répétition Colognese-Ward Q1 et Q2** (le test du commentaire neutralisé) : voir § 6.
- **M12, notes de version** sous `---` (Ibrahim Q1 v3, variante, Scheurer, Colognese-Ward Q1 et Q2) : ne coller que le texte situé au-dessus.
- **M13, Colognese-Ward Q1** : 198 mots sur 200 au découpage sur les blancs, mais 215 si le compteur du site découpe aussi sur les tirets, les barres ou dans le lien. Correction, si la marge inquiète : retirer la phrase répétée (M11).
- **M14, variante Ibrahim Q1** : 458 mots pour une visée de 450, à réduire seulement si elle est choisie.
- **M15, variante et Ibrahim Q2** : « how far (g) … toward what (ĉ) » double « how far (g) from where (ĉ) », à réduire seulement si la variante est choisie.
- **M16, choix des mentors** (l. 183, gardé tel quel) : double espace dans « Lujain Ibrahim,  Stefan » ; les faits sont compatibles avec les réponses.

## 8. Ce que je n'ai pas fait

Je n'ai pas revérifié les faits tirés des papiers des mentors (Hua et coll., 2606.24964, Kirchner, Ibrahim, Apollo, Open Character Training, etc.) : ils n'apparaissent chacun que dans la réponse à leur auteur, et les vérifications antérieures les couvrent. Je n'ai jugé que les faits du squelette Heimersheim Q1 qui concernent les autres réponses (R6, R7, R9, D36, ρ), pas sa thèse.
