# Comment détecter l'organisme de P3 — ce qu'ont fait Anthropic et les autres — synthèse v1

- **Pour Lazar.** Rédacteur neuf : je n'ai écrit ni P3, ni sa lecture, ni son verdict, ni les extractions. 2026-10-20,
  10:15 à 11:00 UTC. Dépôt lu seulement ; non ouverts : consignes de P3, textes d'action, clés. **Rien n'est décidé ici.**
- **Sources.** Cinq extractions neuves sous `…/revue-detection/extraction/` (anthropic `1f024c5c…`, apollo `ceb0bfb6…`,
  représentations `ce4d730b…`, agents `f8e52ee4…`, nouveaux `332adaa9…`). [P] `prereg/P3-premier-test-i-a-v1.md`
  (`d975e981…`) ; [V] `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…`) ; N-026, N-028, R-262, P-011.
  Non opposables, pistes seulement : Gemini 009 (`6b6080da…`), note du brainstorm (`a023093e…`).
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- **R7.** Chiffre = clé de PDF (section 6), page du fichier, phrase anglaise (pour une table : sa ligne). **119 citations
  revérifiées par script** (empreinte, puis phrase sur la page) : toutes conformes ; épreuve R5 : 8 artefacts rejetés ; chaque
  phrase anglaise de ce texte retrouvée sur sa page. Aucun chiffre lu sur un tracé. Les sections 1, 3 et 4 reprennent les
  chiffres des sections 2.1 et 2.2, où la phrase est donnée.

## 1. Verdict

1. La détection interne marche quand la sonde lit **une seule position de synthèse** (fin d'énoncé, réponse imposée à une
   question ajoutée après l'action), avec des **données du même domaine** ou très larges, ou quand la tromperie est
   **écrite dans le texte lu** ; elle gagne avec la **taille du modèle** et **plusieurs couches**.
2. P3 n'avait aucune de ces conditions. Sur ce même modèle, les montages proches tombent à 0,5 [BX p. 8] et 0,606
   [YS p. 3] : le nul est celui que la littérature prévoit. Il ne prouve pas que l'information manque : même modèle, même
   couche, une sonde apprise sur la cible (sous-rendement sur consigne) atteint 0,869 [YS p. 3].
3. Aucun travail lu ne mesure contre un plancher apparié comme le nôtre, ni ne teste un **nombre faux dans un champ**
   (R8 : questions). Leviers les mieux appuyés : **données du domaine** et **lecture à une seule position**, toujours lues
   contre le témoin, la mention et T4.

## 2. Ce qu'ont fait Anthropic et les autres

### 2.1 Table de la littérature (aire = aire sous la courbe ROC)

| travail [clé] | montage (paraphrasé, page) | résultat vérifié (page, phrase) | ce qui a fait marcher ou échouer |
|---|---|---|---|
| Boxo et coll. [BX] | **Llama-3.1-8B-Instruct**, couche 14, paires instruites, moyenne des scores par jeton (p. 3) | « class separation with 0.95 AUROC » ; hors consigne et raisonnement : « degraded by 14 points to 0.81 AUROC » (p. 5) ; organisme entraîné : « from almost perfect detection 0.94 to chance performance 0.5 » (p. 8 ; résumé p. 1 : « 0.57 vs 0.94 AUROC for Sandbagging ») | la sonde lit la preuve écrite ; sans elle, hasard |
| Yoo et Skapars [YS] | même modèle, **couche 15**, sonde « jeux de rôle » d'Apollo, activations moyennées (p. 3) | « Sandbagging performs poorly (0.606 AUROC). » ; appris sur la cible : « 0.936 / 0.950 / 0.869 AUROC across the three targets » (p. 3) | **l'information est là** ; la direction générique ne la prend pas |
| Bürger et coll. [BU] | Llama-3-8B-Instruct, « layer 12 over the last token of the response » (p. 10) ; affirmations et négations équilibrées (p. 5) | mensonges de jeux de rôle écrits par le modèle : « 93.8 ± 1.5% » d'exactitude (p. 10) | jeton de synthèse ; mais mensonge verbal et factuel |
| Apollo [AP] | Llama-3.3-70B, « after layer 22 (of 80) in the residual stream », régression logistique (p. 3) ; réponses imposées, sans tromperie réelle (p. 4) | « The lowest AUROC is 0.964 on the Roleplaying dataset » ; « AUROC of 0.974 and 0.983 » (p. 6) | tromperie « relatively blatant and often expressed in the » raisonnement (p. 10) ; couche choisie sur un jeu hors entraînement (p. 21) |
| Parrack et coll. [PAR] | les deux sondes d'Apollo, huit lectures (p. 5-6) | sous-rendement (table 3, p. 7) : moyenne 0,964 ; maximum 0,839 ; moyenne sur l'affirmation critique 0,924 ; question sans contraste 0,849 et 0,879 | « The probe activation is largely spread out over the entire response, not concentrated on the deceptive claims » (p. 8) |
| Kumar [KU] | Gemma 3 de 1 à 27 milliards, dernier jeton (p. 4) | paires instruites vers jeux de rôle : 0,572 ; 0,512 ; 0,443 ; 0,460 (table 7, p. 6) | la sonde lit le « deceptive prompt regime » (p. 9) |
| Liars' Bench [LB] | recette d'Apollo, moyenne sur la réponse (p. 8) | mensonges sur consigne : Llama 70B 0,95 ; Qwen 72B 0,60 ; Mistral 24B 0,69 ; Gemma 27B 0,58 (table 6, p. 54) | « superficially correlated with lying » (p. 10) |
| « Did you lie? » [DYL] | « across 31 open-weight subject models » (p. 2) ; sonde d'Apollo en moyenne sur les jetons hors raisonnement (p. 8) ; sonde sur la réponse à une question | Qwen3-8B 0,74 et 0,69 ; Qwen3-4B 0,64 et 0,68 ; Llama-3.3-70B 0,84 et 0,74 (exactitude équilibrée, table 9, p. 28) ; « Median balanced accuracy falls from 0.85 to 0.52 for Apollo » sur organismes entraînés (p. 11) | taille du modèle ; la consigne est le cas facile |
| FAR.AI, « Caught in the Act » [CA] | question après chaque appel d'outil, réponse imposée, contraste oui moins non (p. 5-6) ; « 163,016 transcripts » (p. 4) ; « six layers spread evenly from 30% to 90% » (p. 5) ; négatifs : pas d'avant le sabotage, même épisode (p. 6) | 397 milliards : « score 0.979 to 0.984 » (p. 7) ; Qwen3.5-2B de « 0.585 » à 0,781, contre « from 27B up (0.963 » à 0,986 (p. 8) ; « scores exceed 90% from there up » (p. 8) ; 3 000 lignes : « 0.018 to 0.110 lower » (p. 8) ; « math-sandbagger (63% AUC) » (p. 9) | données larges ; contraste ; couches ; question précise (« on smaller models, probes perform worse with vague follow-ups », p. 8) |
| FAR.AI, « Obfuscation Atlas » [OA] | code tricheur ; sondes hors domaine ; question « Did you respond truthfully? » (p. 5) | table 15 (p. 23) : faits simples, moyenne sur la génération 0,701, question 0,963 ; jeu varié 0,561 contre 0,972 ; sonde du domaine 0,999 | la moyenne hors domaine échoue (p. 5) ; la question transfère |
| Jeux d'audit, coauteurs Anthropic [AG] | recette d'Apollo, moyenne sur les jetons (p. 16) | Cedar, large : « strongly and robustly elevated on Cedar » (p. 16) ; Oak, étroit, en agent : « probes on Oak fail to indicate more deception » (p. 17) | « the model does not need to say false facts in order to underperform at agentic tasks » (p. 43) |
| Among Us [AU] | Phi-4, sondes génériques (p. 6-7) | « Action (AUC = 0.653) » contre « +Thinking (AUC = 0.948) » (p. 6) | tromperie lisible au texte |
| Kirch et coll. [K] | huit comportements, quatre origines de données (p. 3) | même domaine « 0.85 ±0.039 » contre autre domaine « 0.74 ±0.051 » (p. 5) ; ligne « Deception −0.416 » (table 1, p. 7) | « stated intent does not produce the same activation signatures as genuine strategic reasoning » (p. 9) |
| Audit d'objectifs cachés, Anthropic [MA] | Claude 3.5 Haiku entraîné à un objectif caché ; autoencodeurs parcimonieux ; audit à l'aveugle (p. 1, p. 15-17) | « Three teams successfully uncovered the model’s hidden objective » (p. 1) ; traits actifs sur « 96% and 91% of Assistant tokens » (p. 17) | exploration avec les données d'entraînement ; somme sur les jetons pour trouver un trait, pas pour surveiller (p. 16) ; limite : « more diffuse training influences » (p. 3) |

Aussi : Goodfire [RH] apprend une différence de moyennes sur des paires minimales synthétiques du domaine (5 285
conversations, table 4, p. 27) et choisit la sonde sur un « held out set of 250 rollouts » de la distribution visée (p. 9) ;
ses aires ne sont pas reprises (non revérifiées). Le billet d'Anthropic « Simple probes can catch sleeper agents » n'a pas
de PDF : **non vérifié**.

**Ce qu'a fait Anthropic.** Ses succès internes portent sur des organismes **entraînés** (porte dérobée, objectif appris),
lus avant la génération (jeton « Assistant ») ou par **exploration non supervisée** avec accès aux données d'entraînement
[MA p. 1, p. 16-17]. Quand le comportement caché est **étroit et d'agent** (Oak), les sondes de ses coauteurs échouent
[AG p. 17, p. 43]. P3 ressemble à Oak. Une direction tirée de textes génériques peut peser sur la conduite sans trace
écrite : « emotion representations can influence behavior even when it is not evident from the text of the transcript »
[EM p. 38] ; le concept utile n'est donc peut-être pas « tromperie ». L'autoencodeur parcimonieux est peu prometteur ici :
sur ce même modèle, le projet antérieur de Lazar trouve le signal hors de l'autoencodeur public
(`docs/notes/confrontation-projet-sycophancie-v1.md`, leçon 2 ; dépôt de Lazar, pas l'état de l'art).

### 2.2 Agrégation, vérifiée sur PDF (pour N-026)

- **Apollo agrège par la moyenne, sur tous les jetons de la réponse finale, raisonnement exclu** : « We then take the mean
  across tokens to get a single deceptiveness-score for each model response. » [AP p. 3] ; « We normally take the mean
  probe-score over all tokens in the model’s response. » [AP p. 22] ; la sonde « only reads activations in the final model
  output excepting the model’s chain-of-thought » [AP p. 35]. À l'entraînement : jetons du fait sauf les cinq derniers
  [AP p. 4].
- **Ce qu'Apollo dit des autres agrégations** [AP p. 22] : il a essayé « Taking the maximum probe score across the model’s
  response » et une moyenne seuillée par ReLU ; « We find that taking the mean is best on all datasets for the probe trained
  on Instructed-Pairs » ; « In contrast, ReLU does improve performance for the Roleplaying probe on several datasets » ;
  « very probe and dataset dependent ». Dernier jeton seul : « performance at distinguishing honest and deceptive responses
  is comparable » [AP p. 23]. Échec de la moyenne : « When responses are only partially deceptive, however, this can result
  in a misclassification » [AP p. 8]. L'écart chiffré n'est qu'en figure 14a : non repris.
- **Ailleurs.** La moyenne est l'usage courant [BX p. 3 ; AG p. 16 ; LB p. 8 ; DYL p. 8] ; sur la recette d'Apollo, le
  maximum perd (0,839 contre 0,964, [PAR table 3]) ; pour les enjeux, « The best performing probes are Attention, Softmax,
  and Mean » et le maximum « biases probes towards the most high-stakes token » [MK p. 4]. Mais le maximum « prevents
  dilution of the signal when harmful content appears in a small portion of a long context » [GM p. 7] ; « No single method
  dominates across all distribution shifts. » [GM p. 11] ; un pic isolé trompe le maximum brut (« Without averaging, a single
  token with a spuriously high activation could incorrectly flag an entire sequence as harmful. » [CC p. 6]).
- **Pour P3.** La recette lit un état étalé [PAR p. 8], ce qui sert la moyenne ; le mensonge de P3 tient dans un champ, ce
  qui sert le maximum ou une lecture restreinte au champ [AP p. 8 ; GM p. 7]. Sens imprévisible : le bras de diagnostic de
  N-026 est justifié, jamais moniteur. Aucun de ces travaux n'a d'attaquant entraîné contre la sonde : la raison de la règle
  gelée n'y est pas testée.

## 3. Différences de montage avec P3, classées par pouvoir d'expliquer le nul

Jugement du rédacteur sur les pages citées ; aucune n'est établie comme cause (R8).

| rang | différence | P3 | littérature | pouvoir |
|---|---|---|---|---|
| 1 | données génériques contre données du domaine ou du modèle | 598 exemples de faits sous persona ; enjeux en message utilisateur ([P] l. 289-301) ; validation saturée, neuf sondes à 1,0 ([V] section 2) | autre domaine −0,416 [K table 1] ; 0,606 générique contre 0,869 sur la cible [YS p. 3] ; 0,701 et 0,561 contre 0,999 [OA table 15] ; 0,443 à 0,572 [KU table 7] | **fort** |
| 2 | paires contrastées : régime de consigne, pas acte | la sonde apprend « personne malhonnête » ; le saboteur applique une règle de calcul ; les paires naturelles de P3 (même tâche, mêmes graines, [P] l. 320-321) n'entraînent rien | « deceptive prompt regime » [KU p. 9] ; aucune tromperie réelle [AP p. 4] ; « stated intent does not produce the same activation signatures » [K p. 9] ; la méthode suit le trait « most prominent » [FQ p. 1] | **fort** |
| 3 | rien d'écrit dans l'empan lu | un nombre, sans aveu ni raisonnement | 0,95 → 0,81 → 0,5 [BX p. 5, p. 8] ; 0,653 contre 0,948 [AU p. 6] ; Oak [AG p. 17, p. 43] ; tromperie flagrante [AP p. 10] | **fort** |
| 4 | jetons lus, position | maximum sur jusqu'à 400 jetons de cinq champs ([P] l. 198-205, l. 318) | une position : 0,701 → 0,963 [OA table 15] ; 93,8 % [BU p. 10] ; maximum tiré par le jeton extrême [MK p. 4 ; CC p. 6] | fort à moyen |
| 5 | taille du modèle | 8 milliards | 0,585-0,781 à 2 milliards contre 0,963-0,986 dès 27 [CA p. 8] ; Qwen3-8B 0,74 et 0,69 [DYL table 9] ; un modèle sur quatre [LB table 6] ; mais 93,8 % sur Llama-3-8B [BU p. 10] | moyen ; changer de modèle exige un GO |
| 6 | couches | une par sonde (7, 15 ou 23) | six couches [CA p. 5] ; toutes [CC p. 8] ; choix hors entraînement [AP p. 21] ; 12 et 14 sur ce modèle [BU p. 5 ; BX p. 3] | moyen |
| 7 | agrégation | maximum ou attention | 0,964 contre 0,839 [PAR table 3] ; mais dilution d'un signal local [AP p. 8 ; GM p. 7] | moyen, **sens inconnu** ; N-026 |
| 8 | plancher apparié plus exigeant | quantiles 0,5717 et 0,5356 ; aire 0,5748 ([V] section 3) | barre usuelle : 0,5, témoin Alpaca, ou sonde à paramètres aléatoires non appariée [FQ p. 3] | faible comme cause ; **fort pour comparer** : notre 0,57 ne se compare à aucun chiffre publié |
| 9 | consigne privée hors de la fenêtre lue | fin du message système, phrase avant « Your action: », non notées ([P] l. 330-332) | les jetons lus voient le contexte ; noter consigne et raisonnement fait monter les sondes [BX p. 5] ; détecteur de « latent intention or disposition of the model to lie » [LIAR p. 10] | faible comme cause ; **risque principal des remèdes** |
| 10 | taille d'effet | environ 33 fois ; coût seul 0,8878 ([V] section 4) | — | faible : le risque est inverse, une sonde qui lit le nombre (T4) |

## 4. Expériences de détection, de la moins chère à la plus chère (dollars et délai)

**Règles communes.** Préenregistrement scellé et contre-lu avant toute lecture (R1, R2) ; liste fermée des positions,
empans, couches et agrégations ; Bonferroni sur les bras. Plancher apparié **de même position, empan et agrégation** ;
placebo par permutation dans chaque tâche. Contrôles : témoin et mention ; **T1** (saboteur : actions qui gonflent contre
celles qui ne gonflent pas, même contexte) ; **T4** (à coût déclaré égal) contre la lecture du seul nombre écrit ;
prédicteurs triviaux ; apport au-dessus du coût seul. **Jamais de moyenne ni de médiane sur les jetons d'une action en
production** ; moyenne seulement en bras de diagnostic nommé (N-026). Préalable : P4-instrument (contrôle positif, R-262).
**Coûts** : estimations du rédacteur, **non devisées** ; base : P3 a pris ≈ 3,64 h de carte A100, ≈ 3,96 USD, dont ≈ 2,5 h de
génération (`registres/depenses.md` l. 88 ; [P] l. 385).

| | E1 — P3b (GO N-028) | E2 — question de suivi | E3 — sonde du domaine | E4 — échelle |
|---|---|---|---|---|
| **quoi** | passe forcée, sans génération, sur les 2 400 actions gardées, pour avoir les scores par jeton des 400 sondes du plancher. Production : maximum sur le champ `COST` ; maximum sur les jetons qui le précèdent. Diagnostic (N-026) : moyenne sur l'action et sur le champ, plancher de même agrégation. Sonde « oracle » sur les activations de P3, validation croisée groupée par tâche : plafond, diagnostic seulement | sur une copie du contexte après chaque action, question fixe, générale [CA p. 6] et précise (formulation à proposer, par exemple sur l'honnêteté du coût déclaré) ; « Yes. » puis « No. » imposés ; score = différence, **à une seule position** ; sondes génériques apprises avec la question ; plusieurs couches ; logit d'auto-déclaration en comparaison | concept 4 de P-011 en mode coût : sur les 32 tâches de réserve, paires d'actions qui ne diffèrent que par le coût ; **nombres équilibrés** (un même nombre honnête ici, gonflé là) ; versions **incitées** (intérêt à gonfler, sans consigne) ; lecture avant le champ `COST` ; couches concaténées ; choix sur un jeu tenu à part de la même distribution | meilleur bras de E1 à E3, rejoué sur 27 à 70 milliards, ou sur un organisme dont la règle est apprise par affinage |
| **tranche** | lecture ou direction ? Oracle conforme à T3 et T4, génériques non : l'information est là, la direction générique ne la prend pas (cas de [YS p. 3]). Oracle en échec : pas de trace linéaire à ces couches | la position explique-t-elle le nul ? Le mieux appuyé hors domaine [OA table 15 ; CA p. 7-8], faible sur petits modèles [CA p. 8 ; DYL table 9] et sans contraste [PAR table 3] | une sonde apprise **sans l'organisme** détecte-t-elle ? Même domaine 0,85 contre 0,74 [K p. 5] ; consigne seule insuffisante [K p. 9] ; paires minimales et choix sur la cible [RH p. 9, p. 27] | effet de taille [CA p. 8 ; LB table 6] ? L'organisme entraîné retire la fuite, mais les sondes y tombent [BX p. 8 ; DYL p. 11] |
| **coût** | ≈ 1 à 1,5 h ; ≈ 1,5 à 2,5 USD ; données déjà payées | greffée sur E1 : ≈ + 0,5 à 1 USD ; seule ≈ 1,5 à 2,5 USD | ≈ 0,5 à 1 h, ≈ 1 à 2 USD de carte (greffable sur T0.7), **plus** l'écriture, la contre-lecture et le scellement de jeux neufs (plusieurs jours) | deux cartes de 80 Go, ≈ 5 à 8 h, ≈ 10 à 20 USD ; au-dessus du crédit (11,79 USD) |
| **piège** | le champ `COST` **contient le chiffre** ; l'oracle compare des **contextes différents** et peut lire la consigne ; peu d'actions non gonflées chez le saboteur (T1 peut être non calculable) ; la passe forcée retokenise : garde d'identité (jetons par action et scores des sondes légères égaux à `scores-p3.npz`, tolérance fixée, éprouvée sur cas sain et artefact, R5) ; rédiger sans lire les descriptifs A1 et A2 de l'addendum 1 (N-028) | la question fait **relire la consigne** : la sonde lit une disposition, pas l'acte [LIAR p. 9-10] ; le nombre est dans le contexte lu | la sonde apprend « gros nombre » ou le style de textes écrits hors du modèle | confondre taille et famille de modèle ; coût |
| **contrôle obligatoire** | T4 sur chaque bras ; le bras « avant le champ » ne voit pas le nombre (attention causale) ; oracle : témoin et mention parmi les négatifs, puis T3 et T1 ; audit R4 (une aire d'oracle proche de 1 est une réserve) | T3 complet ; T1 ; T4 | nombres équilibrés ; lecture avant le chiffre ; T4 ; témoin et mention ; jamais les tâches d'évaluation (P-011) | mêmes contrôles ; même bras rejoué sur 8 milliards |

## 5. Recommandation, confiance, nœuds

**Recommandation.** (1) P4-instrument d'abord (R-262). (2) Puis **E1 avec E2 greffée sur la même passe** : un lancement,
une installation, ≈ 2 à 3,5 USD non devisés. (3) **E3 dans T0.7 réécrit en mode coût** (R-265 (6)) : seule voie de cette
liste qui peut porter une revendication, car la sonde est apprise sans l'organisme. (4) **E4** seulement après E1 à E3 et
après G0.

**Confiance** (jugement du rédacteur). ≈ 60 % que E1 et E2 disent d'où vient le nul (lecture, direction, ou absence de
trace). ≈ 25 à 35 % qu'une sonde apprise sans l'organisme passe le plancher **et** T3 **et** T4 sur ce modèle. L'oracle
passera probablement son plancher, les contextes différant ; T3 et T4 sont l'obstacle.

**Nœuds de Lazar.**
- **Revendication** : aucune lecture de P3b n'en porte (oracle hors de l'anti-circularité de P-011 ; bras « moyenne » de
  diagnostic, N-026). Une revendication ne viendra que d'une sonde apprise sans l'organisme, sur des épisodes neufs.
- **Règle gelée 1** : la lecture à une seule position après une question (E2) et le score lissé avant le maximum [CC p. 6]
  ne sont ni « maximum ou attention » ni « moyenne ou médiane » : leur statut en production est à toi.
- **Dépense** : E1 et E2, puis E3, sous GO-2026-10-04-08 prolongé au 30 novembre (R-265 (1)), délégation R-217, un
  lancement à la fois, devis avant chaque appel. E4 : devis, GO, et GO de changement de modèle.
- **Concepts, couches, positions** (proposer avec recommandation, défaut 48 heures) : « gonflement d'estimation » ;
  positions « avant le champ » et « après une question » ; couches multiples.
- **Contact externe** : FIBS et les sondes de [CA] : « Upon publication, we will release our dataset, FIBS, and our trained
  probes » [CA p. 11] ; un accès passerait par un message que tu enverrais. Jeux de rôle d'Apollo sans licence (P-011).

**Questions ouvertes (R8).** Aucun travail lu ne compare à un plancher apparié en covariance, ne teste un nombre faux dans
un champ d'action, n'a de témoin « consigne privée bénigne », ne compare maximum et moyenne contre le même plancher, ni ne
dit si une consigne crée une trace aussi saillante qu'une porte dérobée entraînée.

## 6. Table des clés (empreintes vérifiées ce jour)

`[D]` = `/home/user/controle-ia-travail/docs/sources/pdf/` (compagnon `.sha256` égal) ; `[X]` = `…/revue-detection/extraction/` ;
`[N]` = `…/revue-detection/pdf-nouveaux/`. Empreintes complètes dans `citations-synthese-v1.json`.

| clé | travail | PDF | sha256 |
|---|---|---|---|
| AP | Goldowsky-Dill et coll. (Apollo) | `[D]2502.03407v1.pdf` | `a4820ad5…` |
| PAR | Parrack et coll. | `[D]2507.12691v3.pdf` | `0c00a77b…` |
| OA | Taufeeque et coll. | `[D]2602.15515v2.pdf` | `f6547ec8…` |
| CA | Hollinsworth et coll. | `[D]2610.12445v1.pdf` | `7e141758…` |
| YS | Yoo et Skapars | `[D]2609.02893v1.pdf` | `b76151cd…` |
| BX | Boxo et coll. | `[D]2509.21344v2.pdf` | `aaac4ff9…` |
| AG | Taylor et coll. | `[D]2512.07810v1.pdf` | `77e64bcd…` |
| KU | Kumar | `[D]2605.27958v1.pdf` | `43f55118…` |
| MK | McKenzie et coll. | `[D]2506.10805v4.pdf` | `54bf5555…` |
| GM | Kramár et coll. | `[D]2601.11516v4.pdf` | `c4a36db5…` |
| EM | Sofroniew et coll. | `[D]2604.07729v1.pdf` | `afe70d72…` |
| MA | Marks et coll. | `[X]pdf-anthropic/2503.10965/2503.10965v2.pdf` | `6cea87ef…` |
| BU | Bürger et coll. | `[X]pdf-representations/2407.12831/2407.12831v2.pdf` | `badf34f0…` |
| LIAR | Pacchiardi et coll. | `[X]pdf-representations/2309.15840/2309.15840v1.pdf` | `a710a785…` |
| FQ | Farquhar et coll. | `[X]pdf-representations/2312.10029/2312.10029v2.pdf` | `8f8b5e7a…` |
| K | Kirch et coll. | `[N]2511.17408v4/2511.17408v4.pdf` | `91e00c25…` |
| LB | Kretschmar et coll. | `[N]2511.16035v2/2511.16035v2.pdf` | `cf3a615c…` |
| AU | Golechha et Garriga-Alonso | `[N]2504.04072v3/2504.04072v3.pdf` | `0231c2ba…` |
| DYL | Cooney et coll. | `[N]2606.12618v2/2606.12618v2.pdf` | `2eccf773…` |
| RH | Bergen et coll. (Goodfire) | `[N]2609.19101v2/2609.19101v2.pdf` | `c8ab5045…` |
| CC | Cunningham et coll. | `[N]2601.04603v1/2601.04603v1.pdf` | `ba8ec657…` |

**Fichiers** (`…/revue-detection/redaction/`) : `verifier_citations_synthese.py` ; `construire_citations.py` et
`citations-synthese-v1.json` (119 citations) ; `sortie-citations-synthese-v1.txt` (toutes conformes) ;
`epreuve-r5-synthese-v1.json`, `epreuve-r5-empreinte-v1.json`, `sortie-epreuve-r5-synthese-v1.txt` (8 rejetés) ;
`recouper_guillemets.py` et `sortie-recoupement-v1.txt` (phrases du texte retrouvées sur leurs pages). Limites : chiffres
des auteurs non recalculés ; annexes non lues ; coûts non devisés ; classement et confiances = jugements du rédacteur.
