# Lecture comme la mentor — Lujain Ibrahim, deuxième question (projet technique) — v1

Début de lecture : 3 novembre 2026, 12:50 UTC (temps universel, `date -u`) ; fichier écrit entre 13:02 et 13:05 UTC, heure de l'en-tête corrigée vers 13:05 UTC. Lecteur : instance neuve, auteur d'aucune version des réponses de Lazar au formulaire Pivotal.
Notations : Q1 et Q2 = première et deuxième questions d'Ibrahim dans le formulaire. R1 à R8 = suites publiées du dépôt (R2 : note de 1 à 5 donnée par le modèle lui-même, sans juge ; R3 : trois autres familles de modèles ; R4 : 60 items neufs ; R5 : lecteurs humains ; R6 : trois formulations de la pression ; R8 : étapes publiques d'après-entraînement de Tülu 3).

## 0. Ce que j'ai lu

| pièce | identifiant | lecture |
|---|---|---|
| Réponse (anglais) | `brouillons/redaction-finale-v1/ibrahim-q2/reponse-v1.md`, sha256 `8499c1555d1d4620794d1209dabb0b9829f8e9961757c4c31f15041a2de68dce`, vérifié avant lecture | lignes 1 à 11 (le texte) ; la note de compte (lignes 13 à 19) lue à part |
| Question | `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 148 | « Describe a technical project where you trained or evaluated LLMs (feel free to link to code or any public documentation/write up if you have something to share). » Aucune limite écrite ; visée : 300 mots au plus |
| Ce que fait la mentor | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` | entier |
| Dépôt public lié par la réponse (ce qu'elle verra en cliquant) | copie locale en lecture seule `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, commit `b3ecaec` (3 novembre 2026, 10:35 UTC) ; aucune récupération par git | `README.md`, `STATUS.md`, README de `results/R2`, `R3`, `R4`, `R6`, `preregistrations/R4_brief.txt`, recherches par motifs |
| Taxonomie qu'elle co-signe (2e autrice) : Ye, Ibrahim, Bo, Cheng, Mattsson, Vennemeyer, Kraut, Rathje, *What Counts as AI Sycophancy?* | arXiv 2605.21778 | page de résumé, puis texte intégral en ligne par l'outil de lecture (100 000 premiers caractères sur 105 462 ; citations courtes ; non vérifié sur la version imprimable) |

Non lus, volontairement : `note-piste-v1.md` et `registre-affirmations-v1.md` du même dossier, pour ne pas reprendre les justifications du rédacteur. Chaque fait a été vérifié directement dans le dépôt public.

## Verdict

Rien de bloquant : chaque fait vérifié est exact, et la réponse montre ce qu'Ibrahim cherche (prédiction hors échantillon sans paramètre réajusté, échec préenregistré publié, refus gardés et contrôlés, juges d'une autre famille, lecteurs humains annoncés comme non lancés). Trois points à corriger, tous sur la question qu'elle posera d'abord, « que mesure la loi ? » : (1) sous éloge, la destination est le milieu de l'échelle, ce que sa taxonomie ne compte pas comme de la sycophancie, et la réponse ne le dit pas ; (2) la lecture sans juge (R2), qui ne retrouve pas l'attraction sous éloge, est omise alors que les deux juges qui la retrouvent sont cités ; (3) le résultat de dose dit quels paramètres ont échoué, pas ce que fait le modèle. Compte : 293 à 297 mots selon la méthode, sous la visée de 300 ; un paquet de corrections et de coupes qui tient sous 300 est donné au point 6.

## 1. La phrase qu'elle contredirait

**Citation** : « a destination ĉ set by the pressure (1.5 under criticism, 2.9 under praise) … So praise lowers ratings above 2.9, beyond regression to the mean. … The reversal held there too. », sous le titre « Sycophancy as Attraction Toward a Fixed Point ».

**Ce qu'elle dirait** : sur une échelle de 1 à 5, 2,9 est le milieu. Sous éloge, la loi réunit deux conduites de signe opposé : les textes faibles montent (évaluation gonflée : sycophantique) ; les textes forts descendent vers un verdict neutre, quel que soit l'avis de l'utilisateur, ce que les experts de son enquête notent comme le contraire de la sycophancie. Un paramètre, une étiquette, deux formes : c'est exactement la fragmentation que décrit son papier. Elle ajoutera que les refus, notés 3, tombent sur cette destination (la réponse le dit elle-même, paragraphe 5).

**Sa source** (2605.21778, texte intégral en ligne, citations courtes par l'outil de lecture) : l'item d'enquête « Presents balanced information regardless of user's stated opinion » est noté à l'inverse, lu comme le contraire de la sycophancie ; l'esquive n'est sycophantique que si elle sert l'avis de l'utilisateur (« Uses hedging language in ways that favor user's expressed opinion leaning ») ; résumé : les experts « disagree substantially on which specific behaviors qualify ». Le dépôt va dans le même sens : moyennes sans pression du corpus 2,51 et 2,55 (README, deuxième rival), et la baisse des items forts sous éloge y est présentée comme ce qu'une « poussée directionnelle » ne peut pas produire (README, troisième rival ; `results/R4/README.md` : « A directional push cannot produce this »).

**Gravité** : à corriger. Pas bloquant : la loi est juste ; c'est l'étiquette du bras « éloge » qui n'est pas défendue, et l'étiquette est son sujet.

**Correction minimale** : « 2.9 under praise, mid-scale » (+1 mot) ; version pleine, si la place le permet : en plus « So praise lifts weak texts but lowers those above 2.9 » (+4 de plus). La phrase suivante de la réponse, « A mean shift cannot separate how far (g) from where (ĉ) », devient alors la réponse à son objection.

## 2. Affirmations plus fortes que leur preuve

| # | citation | ce que dit la source | gravité | correction minimale |
|---|---|---|---|---|
| 2a | « Two Qwen judges (7B, 72B) recover the law from the same responses. » | Exact, mais le README montre quatre lecteurs (figure 3), pas trois. Le quatrième, sans juge (R2 : le modèle donne lui-même une note de 1 à 5, lue sur ses probabilités) : attraction sous critique (g = 0,63, R² = 0,91), presque rien sous éloge (g = 0,14 [0,03 ; 0,24]) ; « Two destinations are therefore not robustly established in the model's own rating » (`results/R2/README.md`). Citer les juges qui confirment et taire le canal sans juge : c'est ce qu'une coautrice de la revue sur la validité de construit repère d'abord en suivant le lien. | à corriger | « Two Qwen judges recover the law from the same responses; the model's own 1–5 rating shows it under criticism only. » (+8, retrait de « (7B, 72B) » compris) |
| 2b | « Under criticism, Qwen2.5-7B and Mistral-7B drop about as much as Llama, but uniformly: no fixed point. » | Vrai à la formulation de la campagne 1. R6 : Mistral montre l'attraction aux formulations douce et forte, le déplacement uniforme seulement à la formulation standard (`results/R6/README.md`, tableau Qwen, Mistral, Gemma). La Q1 actuelle le dit (« changed with wording for 1 family (Mistral) »). | mineur | « …but uniformly at this wording: no fixed point » (+3) |
| 2c | « I published this as a failure. » | Résultats déposés dans le dépôt et archivés sur Zenodo (« reported as such ») ; aucun papier. « Published » peut se lire comme une publication relue par des pairs. | mineur | « I reported this publicly as a failure. » (+1) |
| 2d | « Under praise Llama sometimes refuses » | À la formulation de la campagne 1, sur ses items : 31 réponses sur 150 sous éloge (R6, dose standard) ; sur les 60 items neufs : 9 sur 300 (R4). « Sometimes » minimise là même où les refus peuvent imiter l'attraction. | mineur | « (up to one response in five) » (+6) |
| 2e | « dropping the items with refusals changes neither the out-of-sample nor the dose outcome » | Exact pour les verdicts : R4, les quatre critères tiennent sans les items à refus ; R6, l'issue reste C. Mais les estimations bougent (R6, dose forte sans refus : destinations 1,92 et 2,04 au lieu de 2,37 et 2,47), et la campagne 1 (85 réponses de type refus sur 1 200, `results/R4/README.md`) n'a pas ce contrôle. « Outcome » est le mot juste : le garder. | mineur | aucune ; savoir répondre sur la campagne 1 |
| 2f | « code, data, preregistrations » | Les préenregistrements des campagnes 1 et 2 ne sont publiés que par leur empreinte ; les textes des items et l'invite du juge ne sont pas publiés (README, « Not in this release »). Pour elle, l'invite du juge est la première pièce à lire. | mineur | aucune dans la réponse ; savoir dire pourquoi l'invite n'est pas publiée |

Vérifié exact, à ne pas toucher :
- « beyond regression to the mean » : établi par l'ampleur (−0,67 contre une médiane de −0,07 sous absence d'effet, p = 1,6 × 10⁻³, campagne 1 ; −0,60, p = 2,5 × 10⁻⁵, R4), pas par le nombre de baisses (p = 0,35) ; README, troisième rival, et `STATUS.md`, « Manuscript ».
- « R² = 0.68 and 0.58, against −0.28 and −0.01 for a constant shift » : `results/R4/README.md`.
- « written blind and committed before generation » : commit `7ccb3ec`, 2 novembre, 00:11 UTC (`STATUS.md`) ; items écrits par une instance neuve à partir du seul brief (`results/R4/README.md`).
- « Human readers, five per response and blind to condition, are preregistered but not yet run » : R5, ouverture à l'approbation du compte Prolific (`STATUS.md`, « Later »).
- « preregistered on Zenodo before it ran and recomputed from raw files » : README, suites R1 à R7, et chaque README de résultats.

## 3. Ce que la question demande et qui manque

- **Le résultat de dose dit ce qui a échoué, pas ce que fait le modèle** (à corriger). « Under criticism the gain stayed flat while the destination moved; under praise the destination fell » : on ne sait ni où va la destination ni ce que cela veut dire. Or le résultat le plus parlant pour une chercheuse en sycophancie est là : à la formulation la plus forte, les deux destinations sont près de la moyenne sans pression (2,37 et 2,47) et aucun bras ne bouge en moyenne ; sous éloge, Llama refuse d'évaluer à chaque formulation (16, 31 et 26 sur 150) ; sous critique forte, il contredit l'utilisateur jusqu'à 43 fois sur 150 (borne haute, comptage a posteriori) (README, figure 4 ; `results/R6/README.md`). La réponse tait aussi que, sous éloge, le gain a crû comme prévu (+0,52 [0,29 ; 0,76]) : l'échec paraît plus complet qu'il n'est. Correction : « Under criticism the gain stayed flat; both destinations moved, and at the strongest wording neither arm shifted on average. » (+4).
- **Aucun entraînement** (mineur, à savoir). La question admet « or evaluated » ; mais sa Direction 1 demande un entraînement de caractère puis un apprentissage par renforcement, et elle se demandera si le candidat sait entraîner. Si Lazar a entraîné un modèle, une demi-phrase ; sinon rien ici, c'est Q1 qui porte le plan.
- **Taille de l'expérience principale** (mineur) : seuls les « 60 new items » ont un effectif. README : 30 items × 10 générations par condition et par bras. Correction : « (30 items, 10 samples each) » après la première phrase du deuxième paragraphe (+5).
- **Son rôle** (mineur) : clair par les « I », mais « AI coding agents wrote the code. », seul en dernière phrase, se lit « je n'ai pas écrit le code » sans dire ce qu'il a fait. Correction : reprendre les mots de la version actuelle du formulaire, « AI coding agents wrote the code, following guidelines I wrote. » (+4).
- **R8, absent** (mineur, facultatif) : la loi mesurée sur les étapes publiques de Tülu 3 du même Llama (ajustement supervisé, optimisation directe des préférences, apprentissage par renforcement à récompense vérifiable), lancée le 3 novembre à 08:01 UTC (`STATUS.md`), est la suite la plus proche de sa Direction 1 ; sans résultat, elle a plus sa place dans Q1.

## 4. Ce qui la perdrait

| citation | problème | gravité | correction |
|---|---|---|---|
| « The reversal held there too. » | « reversal » n'a jamais été nommé ; il faut remonter deux phrases | mineur | « The praise reversal held there too. » (+1) |
| « recomputed from raw files by a fresh model instance » | jargon ; dans un texte sur Llama, « model instance » se lit comme le modèle testé ; rien ne dit que c'est un agent d'intelligence artificielle sans part au run | mineur | « by an AI agent outside the run » (+2) |
| « the gain would grow » | « gain » n'est pas rattaché à g (paragraphe 3 : « a fixed fraction g ») | mineur | « the gain g » (+1) |
| « destination ĉ » ; « no fixed point » ; titre « Fixed Point » | un concept, deux mots | mineur | « a destination ĉ (the fixed point) » (+3), ou laisser |
| « From its unpressured value p₀, the rating closes… » | la loi porte sur la moyenne de l'item (README : « the item-mean rating ») ; trois symboles et une formule dans une phrase de 37 mots, à relire une fois | mineur | « the item's mean rating » (+2) |
| « against −0.28 and −0.01 for a constant shift » | R² négatif sans glose ; elle comprendra, d'autres lecteurs moins | mineur | facultatif : « (worse than predicting no change) » (+5), mots de `results/R4/README.md` |

## 5. Ce qui la retiendrait — ne pas couper

- **Prédiction hors échantillon sans paramètre réajusté**, sur 60 items écrits à l'aveugle et déposés avant toute génération, contre un déplacement constant qui fait pire que ne rien prédire (R² négatif) : vérifiable par commit et par fichier (`results/R4/`).
- **« A mean shift cannot separate how far (g) from where (ĉ) », avec Qwen et Mistral** : même baisse moyenne que Llama, mécanisme différent. C'est un cas mesuré de « même étiquette, formes différentes », le cœur de sa taxonomie ; avec la correction du point 1, c'est l'argument qui la touche le plus.
- **L'échec préenregistré, publié comme tel** : rare, et c'est ce qui rend crédibles les réussites.
- **Les refus gardés, avec le contrôle sans eux** : son papier sur la chaleur les exclut (rapport sur la mentor, tableau 1a, rangée 15) ; elle lira ce choix contraire et justifié avec intérêt.
- **Juges d'une autre famille, et lecteurs humains annoncés préenregistrés mais non lancés** : l'aveu de ce qui manque répond à ce que demande la revue sur la validité de construit qu'elle co-signe (valider le modèle qui extrait les réponses, §5.2 ; rapport sur la mentor, rangée 16).
- **La phrase de pression citée mot pour mot**, et **Llama-3.1-8B-Instruct**, modèle de son papier sur la chaleur et d'Open Character Training (rapport sur la mentor, rangée 2) : la mesure est réutilisable telle quelle pour sa Direction 1.

## 6. Compte de mots et limite

Par script, sur les lignes 1 à 11 du fichier (du titre à « AI coding agents wrote the code. ») :
- `wc -w`, paramètre régional « C » : **293** ;
- `wc -w`, paramètre régional « C.UTF-8 », et `len(texte.split())` en Python : **297**. L'écart vient des quatre jetons faits seulement de caractères codés sur plusieurs octets, « ≈ », « ĉ », « Δ », « − », que le paramètre « C » ne compte pas. La note du rédacteur nomme « = » au lieu de « ĉ » (« = » est compté par les deux méthodes) ; sans effet sur la limite ;
- jetons contenant une lettre ou un chiffre, hors adresse du dépôt : 292 ; caractères hors fins de ligne : 1 846.

Limite : aucune limite écrite ; visée 300 mots au plus : **respectée**, marge de 3 mots (Python) à 7 (`wc -w` « C »). Tout ajout doit donc être compensé.

Paquet qui tient (simulé par script en mémoire, réponse non modifiée) : point 1 minimal (+1), 2a (+8), point 3 (+4), et trois coupes : « With no refitted parameter, » → « Unrefitted, » (−3) ; « Human readers (five per response, blind to condition) are preregistered, not yet run. » (−2) ; « three wordings, » sans « mild to strong, » (−3) ; résultat 302 (Python) et 298 (`wc -w` « C »). Deux coupes de plus, comptées à la main (jetons en caractères simples, même écart pour les deux méthodes) : « Under pressure, the request ends with » → « Pressured requests end with » (−2) ; « …for a constant shift. The reversal held there too. » → « …for a constant shift; the reversal held. » (−2) ; résultat 298 et 294. La version pleine du point 1 (+4 de plus) demande une coupe supplémentaire. Si la place manque, garder dans l'ordre : point 1, puis 2a, puis 3.

## 7. Cohérence avec Q1 (si Q1 reste celle du formulaire, lignes 138 à 146)

Elle lira les deux réponses à la suite.
- Q1 donne « r² of .73 and .69 out of sample » (campagne 2), Q2 « R² = 0.68 and 0.58 » (60 items neufs) : deux jeux de chiffres hors échantillon, sans dire qu'il s'agit de deux tests. À corriger dans Q1.
- Q1 : la structure à deux constantes « results from the framing of the social interaction itself » ; Q2 dit le contraire (même cadre, Qwen et Mistral en déplacement uniforme). La seconde réfute la première. À corriger dans Q1 (le rapport sur la mentor le signalait, tableau 1a, rangée 10).
- Q1 : lecteurs humains « double-blind », au futur ; Q2 : préenregistrés, cinq par réponse, aveugles à la condition. Mineur.
- Q1 : refus traités comme une issue binaire à part ; Q2 : « I keep them » dans la note du juge. Compatible, mais à dire de la même façon. Mineur.

## 8. Réserves

1. Les citations de la taxonomie viennent de l'outil de lecture sur le texte intégral en ligne (citations courtes, 100 000 premiers caractères sur 105 462), non vérifiées sur la version imprimable ni par page : ne pas les reprendre dans la réponse sans vérification.
2. Dépôt lu au commit `b3ecaec` (3 novembre, 10:35 UTC), plus récent que celui du rapport sur la mentor (`e5e960b`). R8 tourne : si un résultat entre dans le dépôt avant l'envoi, le README changera.
3. Les refus de R6 sont comptés par un motif fixe appliqué à toutes les réponses ; les contre-énoncés sont des bornes hautes (`results/R6/README.md`).
4. Je n'ai pas lu les README de R1a et R1b au-delà de leur résumé dans le README principal et `STATUS.md`.
5. Le rang de priorité (point 1 avant 2a avant 3) est mon jugement de lecteur, pas une règle.
