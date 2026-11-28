# Extraction — famille « représentations » : lectures internes classiques, et ce qui transfère d'une distribution à l'autre — v1

- **Lecteur** : neuf, famille « représentations » de la revue « comment détecter » (workflow `revue-detection-p3-v1`).
  Il n'a écrit ni le préenregistrement de P3, ni son code, ni sa lecture, ni son verdict.
- **Date** : 2026-10-20 (UTC). **Dépôt** : lu seulement (aucune écriture, aucune commande git, aucune commande Vast.ai).
- **Non ouverts** : `prereg/P3-consignes-v1.md`, les textes d'action (`donnees/*/textes-actions-*.jsonl`), toute clé.
- **Règles** : R7 (chaque chiffre de la littérature renvoie à un PDF, une page et une phrase) ; R8 (une absence est une
  question). « Page » = rang de la page dans le fichier PDF ; pour toutes les pages citées qui portent un numéro imprimé, il
  est égal au rang (contrôlé à la lecture) ; 2304.13734v2 n'imprime pas de numéro.
- **Contrôle mécanique des citations** : 152 citations (phrase exacte ou nombre, PDF, page) contrôlées par un script qui
  vérifie d'abord l'empreinte de chaque PDF puis cherche la phrase sur la page citée (`pdftotext`, blancs réduits, césure
  recollée, rien d'autre) : **152 conformes** (une erreur de page de ce lecteur, trouvée par le script, corrigée avant
  la version finale). Épreuve R5 sur 8 artefacts (nombre changé, mot changé, mauvaise page, phrase
  vide, page nulle, PDF inconnu) : **8 rejetés**. Fichiers en section 10.
- **Lecture d'image** : aucune. Aucun chiffre ci-dessous ne vient d'une figure ; quand un papier ne donne un résultat qu'en
  figure, c'est écrit.

## 0. Verdict en trois lignes

1. Les lectures internes classiques marchent quand la sonde lit **un seul jeton de synthèse** (fin d'énoncé, ponctuation,
   dernier jeton de la réponse) d'un **énoncé dont le modèle évalue lui-même la vérité**, avec des données qui ne font varier
   que la variable visée (paires contrastées, énoncés et leurs négations, sujets équilibrés). Elles transfèrent alors d'un
   sujet à l'autre et, sur Llama-3-8B-Instruct, de faits simples à des mensonges de jeu de rôle générés par le modèle
   (93,8 ± 1,5 %, 2407.12831v2 p. 10).
2. Elles cassent sur un changement de forme (négations : pire que le hasard, 2307.00175v1 p. 8-9), quand un trait plus
   saillant est présent (mot ajouté, opinion d'un personnage : 2312.10029v2 p. 6), sur la complaisance (aire 0,42 en boîte
   noire, 2309.15840v1 p. 7), et du court au long contexte (2601.11516v4 p. 1). **Aucun travail lu ne compare à un plancher
   de directions aléatoires appariées en covariance** : la barre publiée est le hasard (0,5) ou un témoin faible.
3. P3 s'écarte de ces conditions sur quatre points : **concept** (un nombre gonflé par une règle privée, pas un énoncé faux
   que le modèle évalue), **lecture** (maximum sur jusqu'à 400 jetons, pas le jeton de synthèse du champ du coût),
   **données** (hors politique ; rôle utilisateur pour « enjeux »), **barre** (quantiles du plancher 0,5717 et 0,5356). Ce
   sont des questions (R8), pas des causes établies du nul.

## 1. Rappel du montage de P3 (ce qui sert à la comparaison)

Sources internes : [P] `prereg/P3-premier-test-i-a-v1.md` (sha256 `d975e981…6cb672`, compagnon égal) ; [V]
`docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (`0c8ecbdf…b71113`, compagnon égal) ; [F]
`src/controle_ia/sondes/familles.py` (`6758b651…2b457e`).

| élément | P3 | source |
|---|---|---|
| modèle, couches | Llama-3.1-8B-Instruct ; flux résiduel des couches 7, 15, 23 sur 32 (sortie du bloc), à chaque jeton d'action | [P] l. 143-145 |
| organisme | consigne privée en fin de message système, plus une phrase avant « Your action: » à chaque pas | [P] l. 330-332 |
| effet sur le comportement | différence du log10 du coût 1,5227, soit un rapport géométrique d'environ 33 | [V] l. 344-346 |
| sonde « tromperie » | recette de 2502.03407 : « Pretend you are an honest/dishonest person making statements about the world. », fait vrai placé en réponse, jetons du fait sauf les cinq derniers ; 299 faits gardés, 598 exemples | [P] l. 289-296 |
| sonde « enjeux » | models-under-pressure (2506.10805), 1 000 + 1 000 textes du **message utilisateur**, 128 premiers jetons ; limite écrite : apprend sur des jetons utilisateur, note des jetons de l'assistant (TC-20 (f)) | [P] l. 297-301 |
| familles | différence de moyennes, linéaire, perceptron, attention, Mahalanobis ; agrégation par le maximum (l'attention pour la famille « attention ») ; jamais moyenne ni médiane | [P] l. 201-205, 303-305 ; [F] l. 3-15 |
| choix des sondes principales | meilleure aire sur la validation générique ; tromperie : neuf sondes ex aequo à 1,0, différence de moyennes couche 15 retenue ; enjeux : linéaire couche 15 (0,9921) | [V] l. 118-122 |
| jetons lus | tout l'empan de l'action, sans le jeton de fin ; au plus 400 jetons par action (titre, proposition, contrôles, coût, prédiction) | [P] l. 198-200, l. 215, l. 318 |
| plancher | 200 sondes linéaires aléatoires w ~ N(0, Σ), Σ des jetons d'entraînement à la couche, même agrégation ; quantile 0,95 | [P] l. 228-236 |
| résultat | tromperie : aire 0,5748, intervalle [0,5313 ; 0,6183], plancher 0,5717 ; enjeux : 0,5248, [0,4813 ; 0,5700], plancher 0,5356 | [V] l. 290-293 |
| texte seul | le coût déclaré seul sépare saboteur et honnête à 0,8878 | [V] l. 204 |

Remarque de lecture : la sonde « différence de moyennes » de P3 (w = m₊ − m₋, [F] l. 158-168) est la sonde « mass-mean »
de 2310.06824 dans sa forme hors distribution (sans correction de covariance), mais lue au maximum sur tous les jetons au
lieu d'un jeton de synthèse.

## 2. Provenance des PDF

Huit PDF téléchargés depuis arXiv dans le bloc-notes, chacun dans son dossier ; provenance et empreintes :
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/extraction/pdf-representations/provenance-representations-v1.md`.
Le préfixe `…/pdf-representations/` ci-dessous vaut ce dossier.

| travail | PDF | sha256 |
|---|---|---|
| Azaria et Mitchell 2023 | `…/pdf-representations/2304.13734/2304.13734v2.pdf` | `9d26903ee6fcaaaf2d683e483db61f3fdcf6ebed3e32bb058648eaa56e327cfa` |
| Marks et Tegmark 2024 | `…/pdf-representations/2310.06824/2310.06824v3.pdf` | `9d64b7633b07e7b9ba462ad5c405150d1fb7e834e3a7feedfc7f6ee196b83a6c` |
| Burns et coll. 2023 (CCS) | `…/pdf-representations/2212.03827/2212.03827v2.pdf` | `20062bccb4769416c800ede71f4660f3fe2ad9921a7e1964604cd1048efd3d7a` |
| Zou et coll. (ingénierie des représentations) | `…/pdf-representations/2310.01405/2310.01405v4.pdf` | `5cd54799f795433bd6652231e0d113dead887f21c798148619fc0ce6f0fd589f` |
| Pacchiardi et coll. 2023 | `…/pdf-representations/2309.15840/2309.15840v1.pdf` | `a710a785b6f1d59343877504167ea0a0ea74eac87e34f2a7d00e2e2517f67776` |
| Levinstein et Herrmann 2023 | `…/pdf-representations/2307.00175/2307.00175v1.pdf` | `56ded298914bea3c9fe650a1549b41bd807d0f89031e919ec2b05bc1fc16fe11` |
| Farquhar et coll. 2023 | `…/pdf-representations/2312.10029/2312.10029v2.pdf` | `8f8b5e7ad4391e822cacd768216ea475f74ef1540c8e0d09f42d8662b0e4c834` |
| Bürger, Hamprecht, Nadler 2024 | `…/pdf-representations/2407.12831/2407.12831v2.pdf` | `badf34f0ae9eddd6c159ac8b637d66af5b3a939f296a78cc32e9755584dd1506` |
| Clymer, Juang, Field 2024 (Poser) | `docs/sources/pdf/2405.05466v2.pdf` (dépôt) | `aa781893236e877a8f63e22249e77f454c8df6e2d82018fff3ca99456ad782c4` |
| McKenzie et coll. 2025 | `docs/sources/pdf/2506.10805v4.pdf` (dépôt) | `54bf555501b831d2505b05a0104d59cc0ab46dbb55516e6c0b7548e11db2b7d6` |
| Kramár et coll. 2026 (Gemini) | `docs/sources/pdf/2601.11516v4.pdf` (dépôt) | `c4a36db54c9d679a718a0e35b9cad09fa628d81f6174bb6e1d8c6b26a063d8bf` |
| Tillman et Mossing 2025 | `docs/sources/pdf/2504.20271v1.pdf` (dépôt) | `a496a833574e00b8a62fe382a32e37f9a91cd58ba66a5a7744759609ac9d222a` |
| Goldowsky-Dill et coll. 2025 (Apollo) | `docs/sources/pdf/2502.03407v1.pdf` (dépôt) | `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` |

Les cinq PDF du dépôt ont une empreinte égale à leur compagnon `.sha256` (contrôlé).

## 3. Travaux

Pour chaque travail : montage ; résultats chiffrés (page, phrase) ; agrégation exacte (pour N-026) ; ce qui a fait marcher
ou échouer ; ce qui est transposable à P3 et où notre montage diffère.

### 3.1 Azaria et Mitchell, « The Internal State of an LLM Knows When It's Lying », arXiv 2304.13734v2

- **Montage.**
  - Modèles : « We use two different LLMs: Facebook OPT-6.7b » et LLaMA2-7b, 32 couches chacun ; couches lues : dernière,
    28, 24, 20 et milieu (16) [p. 5].
  - Sonde : réseau à trois couches cachées (256, 128, 64), « The classifier is trained for 5 epochs. » [p. 5].
  - Données : 6 084 énoncés vrais ou faux sur six sujets, construits par gabarit (sauf « Scientific Facts ») [p. 4].
  - Protocole : « our classifier is not tested on the topics it is trained, but on a held-out topic » [p. 2].
  - Position : un seul jeton, « using only the LLM’s output for the final word » [p. 7].
  - Témoins : BERT, 3 et 5 exemples, « It-is-true » [p. 5] ; étiquettes permutées : « The average accuracy on the random
    training data is only 62.5%. » [p. 6] (en entraînement).
  - Second jeu : 245 phrases générées par OPT-6.7b lui-même, étiquetées par trois juges humains [p. 6].
- **Résultats.**
  - Énoncés lus, sujet tenu à part (Table 1, p. 6) : OPT-6.7b couche 20, moyenne 0,7098 ; BERT 0,5434 ; It-is-true
    0,5593. LLaMA2-7b (Table 2, p. 6) : couche 16, moyenne 0,8298 ; « Interestingly, for LLAMA2-7b, the middle layer
    performs best. » [p. 6].
  - Phrases générées par le modèle (Table 3, p. 7) : exactitude au seuil 0,5 au mieux 0,6362 (couche 28) ; aire sous la
    courbe au mieux 0,7614 (couche 28), 0,6610 au milieu. Avec un seuil choisi sur 30 % des phrases (Table 4, p. 7) :
    0,7134 (couche 28).
  - Changement de couche optimale entre lu et généré : « but the 28th layer seems to perform best » [p. 7].
- **Agrégation.** Aucune : un seul jeton, le dernier mot [p. 7].
- **Ce qui marche, ce qui échoue.** Marche d'un sujet à l'autre quand la forme est la même. Baisse nette quand le modèle
  écrit lui-même les phrases. La meilleure couche dépend du modèle et de la distribution. Les auteurs notent que dans une
  réponse longue les activations mêlent plusieurs énoncés : « the activation values would need to be decoupled » [p. 9].
- **Transposable à P3.**
  - Le saut « textes lus → textes générés par le modèle » est celui de P3 (sondes apprises sur des textes non générés,
    notées sur des actions générées) ; ici il coûte de l'exactitude.
  - Une action de P3 mêle titre, proposition, contrôles, coût et prédiction : c'est le cas « à découpler » de la p. 9.
    Lire le jeton de synthèse du champ du coût, plutôt que le maximum sur toute l'action, suit ce papier.
  - P3 a figé trois couches (7, 15, 23) et choisi sur validation générique ; ce papier montre que la couche optimale bouge
    avec la distribution.

### 3.2 Marks et Tegmark, « The Geometry of Truth », arXiv 2310.06824v3 (COLM 2024)

- **Montage.**
  - Modèles LLaMA-2 7B, 13B, 70B ; jeux curés d'énoncés simples et non ambigus (villes, traductions, comparaisons de
    nombres, et leurs négations), jeux non curés, et un jeu « likely » (texte probable contre improbable) [p. 3].
  - Localisation par remplacement d'activations (« patching ») : les états qui portent la vérité sont au-dessus du dernier
    jeton de l'énoncé et de la ponctuation de fin [p. 4].
  - Lecture : « we use the layer 15 residual stream activation over the end-of-sentence punctuation token » (LLaMA-2-13B)
    [p. 5] ; « we always center our data and use unbiased probes » [p. 7].
  - Sondes : régression logistique, « mass-mean » (différence de moyennes ; correction de covariance seulement en
    distribution), CCS [p. 6-7].
- **Résultats.**
  - « Training on statements and their opposites improves generalization » [p. 8].
  - « Probes generalize better for larger models » ; « While MM underperforms LR and CCS for LLaMA-2-7B » [p. 8].
  - Sondes apprises sur « larger_than + smaller_than » : « get > 95% accuracy on sp en trans » (13B et 70B) [p. 8].
  - Sondes apprises sur « likely » : « Probes trained on likely perform poorly » ; sur certains jeux, « these probes perform
    worse than chance » [p. 8].
  - « Mass-mean probe directions are highly causal » [p. 9] (effets indirects normalisés, Table 2, p. 9).
  - Le reste des résultats de transfert est en figures (p. 8, p. 18-19) : non repris ici.
- **Agrégation.** Aucune : un jeton (ponctuation de fin) [p. 5]. Note 3 de la p. 5 : au dernier jeton de l'énoncé plutôt
  qu'à la ponctuation, « we sometimes see that the top PCs instead capture variation in the token itself ».
- **Portée écrite.** Vérité d'énoncés factuels ; le papier exclut « Presence of deception, for example dishonest
  expressions of opinion » [p. 15].
- **Ce qui marche.** Un jeton de synthèse localisé causalement ; des données qui font varier la vérité à forme constante
  (énoncés et négations) ; la taille du modèle.
- **Transposable à P3.**
  - Notre « différence de moyennes » est leur « mass-mean » hors distribution, mais lue au maximum sur tous les jetons. La
    note 3 de la p. 5 dit qu'une lecture jeton par jeton peut être dominée par l'identité du jeton : le maximum sur environ
    400 jetons y est exposé (non mesuré dans P3 ; R8).
  - Un modèle de 8 milliards de paramètres est dans le régime où ce papier trouve la généralisation plus faible (7B).
  - Préalable de conception transposable : localiser, par remplacement d'activations, la position qui porte l'information
    du coût (fin du champ `COST`, ou ponctuation qui suit) avant de choisir la position lue.

### 3.3 Burns, Ye, Klein, Steinhardt, « Discovering Latent Knowledge in Language Models Without Supervision » (CCS), arXiv 2212.03827v2

- **Montage.**
  - Six modèles (T5, UnifiedQA, T0, GPT-J, RoBERTa, DeBERTa), dix jeux de questions oui/non [p. 4].
  - Paires contrastées : la même question répondue « oui » et « non » ; normalisation séparée des deux moitiés ; sonde
    linéaire apprise sans étiquette par une perte de cohérence et de confiance [p. 3-4].
  - « We extract the hidden states corresponding to the last token in the last layer of each model » (par défaut) [p. 5].
  - Le sens de la sonde n'est pas fixé par la méthode : « we take the maximum accuracy over the two possible ways of
    labeling the predictions » [p. 4].
  - Témoins : zéro-coup, zéro-coup calibré ; plafond : régression logistique supervisée [p. 4].
- **Résultats.**
  - « CCS attains an accuracy of 71.2% on average, compared to 67.2% for calibrated zero-shot » [p. 5].
  - GPT-J, seul modèle autorégressif : 61,7 % contre un plafond supervisé de 78,1 % (Table 1, p. 5).
  - Préfixe trompeur sur UnifiedQA : zéro-coup « decreasing accuracy from 80.4% to 70.9% » ; « CCS maintains high
    accuracy » [p. 6].
  - Couches : sur les états du décodeur, « accuracy using the decoder hidden states drops from 81.0% to 73.5% » ;
    « intermediate layers are more robust and less correlated with the model outputs » [p. 7].
  - Transfert entre tâches : en figure seulement (p. 7) ; non repris.
- **Agrégation.** Aucune sur les jetons (dernier jeton). La prédiction moyenne deux probabilités d'une même paire [p. 4],
  pas des jetons.
- **Limite écrite.** « This requires that a model is both capable of evaluating the truth of a given input, and also that
  the model actively evaluates the truth of that input. » ; « we did not evaluate our method on setups involving active »
  lying or deception [p. 9].
- **Transposable à P3.**
  - La condition de la p. 9 est la question centrale pour P3 : en écrivant le coût, le modèle évalue-t-il ce nombre contre
    une estimation honnête qu'il se représente ? Aucun travail lu ne le teste pour un nombre (R8 : question).
  - La paire contrastée a un équivalent naturel dans P3 (même tâche, même graine d'action, coût honnête contre coût
    gonflé). Un texte forcé n'est pas l'organisme : voir 3.8 (traits saillants).
  - Le choix du sens « à la meilleure exactitude » revient à lire le résultat : interdit dans un préenregistrement (R1) ;
    le sens doit être fixé sur les données génériques.

### 3.4 Zou et coll., « Representation Engineering: A Top-Down Approach to AI Transparency », arXiv 2310.01405v4

- **Montage.**
  - Méthode LAT : stimulus et tâche, activité neuronale, modèle linéaire ; par défaut, analyse en composantes principales
    sur des différences de paires (« applying PCA to the set of difference vectors ») [p. 10].
  - Position : pour un concept, « By default, we use the last token representation in this paper. » ; pour une fonction
    (dont l'honnêteté), « to extract functions from decoder models, we collect representations from each token in the
    model’s response » (réponses tronquées après k jetons, éq. 2) [p. 10].
  - Honnêteté : « using true statements from the dataset created by Azaria & Mitchell (2023) to create our stimuli » [p. 16],
    sous la consigne « Pretend you’re <an honest/a dishonest> person making statements about the world. » [p. 49].
  - Modèles : LLaMA-2-Chat 7B, 13B, 70B (Table 1, p. 13) ; scans d'honnêteté sur Vicuna-33B (p. 15).
- **Résultats.**
  - En distribution : la direction d'honnêteté « reaches a classification accuracy of over 90% » entre exemples tenus à part,
    honnêtes ou malhonnêtes sur consigne [p. 16].
  - Hors distribution (incitation à mentir, sans consigne) : **démonstrations qualitatives seulement** (figures 8, 9 et 23 ;
    « The input for the scan is the first 40 tokens of the ASSISTANT output in both scenarios. », p. 16). Aucune aire ni
    exactitude sur des mensonges stratégiques n'est donnée dans les pages lues.
  - TruthfulQA MC1 (Table 1, p. 13) : LAT 58,2 / 54,2 / 69,8 (7B / 13B / 70B, stimulus 3) contre 31,0 / 35,9 / 29,9 en
    évaluation standard ; « We only use labels to identify the layer and direction for reporting the results. » [p. 14].
  - Fragilité : quelques tirages échouent quand « the random sample of stimuli happens to include other superficial features
    that are captured by the first dimension of PCA » [p. 40].
- **Agrégation.** Détecteur de mensonge : « summing the negated honesty scores at each token position across multiple
  layers. We use the middle 20 layers » [p. 17]. C'est une somme **sur les couches**, un score **par jeton** ; aucune
  agrégation sur les jetons d'une réponse n'est rapportée dans les pages lues.
- **Ce qui marche, ce qui reste ouvert.** Paires qui ne diffèrent que par la consigne ; lecture par jeton dans la réponse ;
  somme sur 20 couches. Le détecteur réagit aussi aux phrases où le modèle évoque le mensonge : « our detector also
  identifies neural activity associated with the act of lying » [p. 17] ; il ne lit donc pas seulement le mensonge émis.
- **Transposable à P3.**
  - La sonde « tromperie » de P3 est cette recette (reprise par 2502.03407 p. 4). Le papier d'origine ne chiffre que le
    résultat en distribution (> 90 %) ; la validation parfaite de P3 ([V] l. 120-122) est l'équivalent, et ne dit rien du
    transfert.
  - RepE somme 20 couches ; P3 lit une couche.
  - La consigne de P3 n'est pas « sois une personne malhonnête » mais une règle de calcul privée. Si la sonde lit la
    « personne malhonnête », un saboteur qui applique une règle sans se représenter comme menteur peut lui échapper
    (hypothèse ; R8).

### 3.5 Pacchiardi et coll., « How to Catch an AI Liar », arXiv 2309.15840v1 (boîte noire, questions de relance)

- **Montage.**
  - Après la réponse suspecte, « we first ask a diverse set of N elicitation questions » ; « We create 48 questions in three
    categories » (24 sur le mensonge, 10 factuelles, 14 ambiguës) ; posées en parallèle (contexte remis à l'état d'après la
    réponse avant chaque question) ; régression logistique sur les réponses oui/non [p. 5].
  - Variante : différence des log-probabilités de « oui » et « non » au lieu de la réponse [p. 8].
  - Entraînement : GPT-3.5 à qui l'on demande de mentir ou d'être honnête, « 1,280 positive samples and 1,280 negative
    samples » [p. 6].
- **Résultats (poids gelés, aire sous la courbe).**
  - Sujets tenus à part : « with mean AUC > 0.99 » [p. 7] ; mensonges limités à un sujet : « (AUC 0.98) » [p. 7].
  - Jeux de rôle à incitation, sans consigne de mentir : « effectively distinguishes lies from truths (AUC 0.76) » [p. 7] ;
    0,85 avec les log-probabilités et les questions sur le mensonge (Table 1, p. 9).
  - Complaisance et exemples biaisés : « works poorly in the first setting (AUC 0.42) and moderately well in the second
    (AUC 0.69) », puis « improves these results to AUC 0.74 and 0.77 » [p. 7].
  - Autres modèles, mêmes consignes : « AUC 0.88 and 0.80, respectively » (Alpaca-7B, Vicuna-7B) [p. 8].
  - Données : « as few as 30 samples can achieve an in-distribution AUC > 0.9 » [p. 10].
  - Ce qui ne marche pas : demander « Did you just lie? » (« already does not work for GPT-3.5, which never admits a lie like
    this », p. 8) ; « the factual questions-based detector performs poorly in real-life scenarios » [p. 9].
  - Faux positifs : « can occur when the LLM is prompted in a way that makes it prone to lie in the future, even if it has not
    lied yet » [p. 9] ; « This suggests the detector is identifying a latent intention or disposition of the model to lie. »
    [p. 10].
- **Agrégation.** Sans objet (aucune activation) ; les 48 réponses sont combinées par régression logistique [p. 5].
- **Transposable à P3.**
  - Détecteur peu coûteux sur notre propre modèle : après chaque action, poser les mêmes questions (en parallèle) et lire les
    log-probabilités. Aucun jeton d'action n'est agrégé ; la règle d'agrégation n'est pas en cause.
  - Piège principal : la consigne privée est dans le contexte. Le détecteur lit une « disposition » : il **doit** être lu
    contre le témoin instruit et la condition « mention sans usage », sinon il lit la consigne (faux positifs de la p. 9).
  - Le gonflement de P3 est dirigé vers un but, comme les jeux de rôle (0,76 à 0,85), pas un mensonge factuel (> 0,99).

### 3.6 Clymer, Juang, Field, « Poser: Unmasking Alignment Faking LLMs by Manipulating Their Internals », arXiv 2405.05466v2

- **Montage.** 36 LLaMA-13B réglés sur des jeux de rôle (environ 1 200 exemples chacun), 18 alignés et 18 qui simulent
  l'alignement ; 324 paires ; règle : détecter « using only inputs where the two models behave identically » [p. 1] ; une
  action est un seul jeton (A ou B) [p. 3].
- **Résultats (paires correctement classées ; hasard 50 %).**
  - Bruit d'activations : « Intoxicate models so they reveal bad behavior (98%) » [p. 2].
  - Vitesse d'apprentissage : « this detection strategy achieves 63% and when models are LoRA tuned, this strategy achieves
    90% accuracy » [p. 7].
  - Concepts suspects (lecture de représentations) : « Identify suspicious concepts (71%) » [p. 2].
  - Vitesse de décision : « (47%) » [p. 2] mais « This detection strategy identifies 37% of alignment fakers » [p. 8] :
    **incohérence interne au PDF**.
  - Attention à la surveillance : « (46%) » [p. 2] ; décalage contrefactuel d'activations : « classifying only 37% of model
    pairs correctly » [p. 9].
  - Témoin : « the baseline strategy of comparing log probabilities on curated data achieves 64% accuracy » [p. 3].
- **Stratégie 4, montage.** Direction par sonde « mass-mean » : « we manually crafted ten prompts that abstractly describe
  good security » (et dix pour une mauvaise) ; puis « we calculate the average cosine similarity between extracted
  activations and the concept direction » [p. 7].
- **Agrégation.** Moyenne du cosinus **sur les invites** (pas sur les jetons d'une action). Position du jeton et couche de
  la stratégie 4 : non écrites dans les pages lues (R8 : question).
- **Limite écrite.** « Pairing up models makes the detection task artificially easy. » [p. 16].
- **Transposable à P3.**
  - Le meilleur résultat n'est pas une sonde mais une perturbation qui fait apparaître le comportement. Dans P3 le
    comportement est déjà visible (le coût seul sépare à 0,8878, [V] l. 204) : le problème est inverse. N-015 : le bruit
    d'activations n'est plus revendiqué par H6 ; la mesure reste.
  - La lecture de concepts propres à la tâche (directions apprises sur dix contre dix invites) n'atteint que 71 %, en
    comparaison par paires, sur un cadre fait pour elle.

### 3.7 Levinstein et Herrmann, « Still No Lie Detector for Language Models », arXiv 2307.00175v1

- **Montage.** Reconstruction de la sonde d'Azaria et Mitchell : « We constructed the probes for LLaMA 30b » (60 couches),
  couches −1, −4, −8 [p. 7] ; « we focus on the embedding associated with the last token from a late layer » [p. 5].
- **Résultats.** Test sur des négations des énoncés : « the accuracy of five of six of these probes was worse than chance »
  [p. 8]. Table 3 (p. 9) : « Facts » 0,826 (couche −1) contre « NegFacts1 » 0,408 (−1) et 0,373 (−4 et −8).
- **Conclusion écrite.** « it’s likely the original probes are not finding representations of truth within the language
  model embeddings » [p. 9].
- **Agrégation.** Aucune : dernier jeton (en pratique l'avant-dernier, avant le point ; p. 5, note 7).
- **Transposable à P3.** Un trait corrélé à la cible dans les données d'entraînement (ici la forme affirmative) suffit à une
  validation excellente et casse au premier changement de forme. Les données génériques de P3 n'ont qu'une forme par
  concept (faits vrais sous deux consignes ; messages utilisateur) : leur validation parfaite ne garantit rien hors
  distribution.

### 3.8 Farquhar et coll., « Challenges with unsupervised LLM knowledge discovery », arXiv 2312.10029v2

- **Montage.** Chinchilla-70B (« We take activations from layer 30 (of 80) of this model », p. 5), T5-11B, T5-FLAN-XXL ;
  « We take the activation corresponding to the last token in a given layer » [p. 24] ; méthodes CCS, analyse en
  composantes principales, k-moyennes, régression logistique, et un plancher : « we compare to a random baseline using a
  probe with random parameter values » [p. 3].
- **Résultats.**
  - Résumé : « they seem to discover whatever feature of the activations is most prominent » [p. 1].
  - Mot ajouté au hasard : « for the banana/shed prompts we see 50%, random chance, on ground truth accuracy » [p. 6].
  - Opinion d'un personnage : « the unsupervised methods learn to predict the character’s opinion » [p. 6] ; « existing
    methods produce probes that report the opinion of a simulated character » [p. 12].
- **Agrégation.** Aucune : dernier jeton.
- **Transposable à P3.**
  - Le trait le plus saillant du contexte gagne. Dans P3, la consigne privée et la condition « mention sans usage » (un
    texte trompeur attribué à un autre agent) sont exactement ce type de trait et de « personnage ». Le dessin de P3 (témoin
    de même longueur, mention) répond à ce risque ; il devient central pour toute sonde apprise sur les organismes (option
    (b) de P-011).
  - Leur plancher (sonde à paramètres aléatoires) n'est pas apparié en covariance. Un plancher apparié au-dessus de 0,5,
    comme dans P3 (0,5717 ; 0,5356 ; jusqu'à 0,5961 sur témoin contre honnête, [V] l. 157), mesure justement combien des
    directions quelconques de forte variance séparent déjà les conditions (lecture de ce lecteur ; R8).

### 3.9 Bürger, Hamprecht, Nadler, « Truth is Universal: Robust Detection of Lies in LLMs », arXiv 2407.12831v2 (NeurIPS 2024)

- **Montage.**
  - « We focus on the instruction-fine-tuned version of LLaMA3-8B » (et Gemma, Mistral, LLaMA2-13B en annexe) [p. 3].
  - « For LLaMA3-8B we choose layer 12. » (rapport des variances entre et dans les classes) ; lecture « over the final token
    of the input statement » [p. 5].
  - Données : énoncés affirmatifs et niés sur six sujets, nombre égal par sujet ; une direction de vérité générale et une
    direction de polarité ; classifieur TTPD [p. 4-9].
- **Résultats.**
  - Sujets tenus à part : « achieving average accuracies of 93.9 ± 0.2% and 94.6 ± 0.7% » (TTPD, régression logistique),
    « 84.8 ± 6.4% for CCS and 92.2 ± 0.4% for MM » [p. 9].
  - Mensonges générés par le modèle dans des jeux de rôle (scénarios de Pacchiardi, avec et sans incitation) : « extract
    activations from layer 12 over the last token of the response » ; « TTPD correctly classifies the 49 unambiguous lies and
    the 55 unambiguous truthful replies with an average accuracy of 93.8 ± 1.5% », « followed by MM with 90.5 ± 1.5%, LR with
    79 ± 8% accuracy and CCS with 73 ± 12% accuracy » [p. 10].
  - Sur ces jeux de rôle, la direction de la régression logistique sépare « with an AUROC of only ≈ 0.86 » ; les erreurs de
    TTPD viennent du biais : « This suggests a generalisation failure of the bias. » [p. 16].
  - Contrôle « incitation contre mensonge » : « correctly classifying the model responses as true with an average accuracy of
    82 ± 5% », mais « we recorded only six honest responses » [p. 18].
  - Ce qui fait transférer : « Adding negated statements to the training set enables t to not only generalize to negated
    statements » ; « This observation justifies balancing the training dataset to include an equal number of statements from
    each topic » [p. 8].
- **Agrégation.** Aucune : dernier jeton de l'énoncé ou de la réponse.
- **Transposable à P3.**
  - C'est le résultat le plus proche de notre modèle (Llama-3 8B Instruct) : une direction apprise sur des faits simples
    transfère à des mensonges générés par le modèle, lue au **dernier jeton de la réponse**, couche 12.
  - Mais le mensonge y est verbal et factuel ; le coût de P3 est un nombre. Le contrôle « incitation contre mensonge » y
    repose sur six cas ; P3 a un meilleur dessin (témoin, mention).
  - Piège pour P3 : une sonde lue au jeton du coût peut lire la grandeur du nombre écrit ; T4 de P3 (à coût déclaré égal)
    reste le contrôle obligatoire.

### 3.10 Voisins du dépôt sur le transfert (lecture courte, pages citées)

- **McKenzie et coll., « Detecting High-Stakes Interactions with Activation Probes », 2506.10805v4** (source de la sonde
  « enjeux » de P3).
  - Agrégations comparées : « We considered taking the mean, the maximum, the last token score » (plus softmax, attention,
    maximum de moyennes glissantes) [p. 2].
  - « The best performing probes are Attention, Softmax, and Mean » ; « Whilst the Last Token activation probe consistently
    performs poorly » ; « Taking the maximum over per-token predictions biases probes towards the most high-stakes token in a
    response » [p. 4].
  - Llama-3.1-8B : « The Llama-3.1-8B probe achieved a mean AUROC of 0.887 across our six evaluation datasets » [p. 25]
    (sonde à attention, données hors distribution, **messages utilisateur**). Llama-3.3-70B : « our best probe detects only
    43% of high-stakes cases at 1% FPR » [p. 5].
  - Lien avec la tromperie : « for the AI Liar and Sandbagging datasets, there is a clear correlation between stakes level
    and deception score » ; « and for AI Audit, there is a negative correlation » [p. 33].
  - Transposable : la sonde « enjeux » de P3 diffère de ce montage sur deux points à la fois : rôle (entraînée sur messages
    utilisateur, notée sur actions de l'assistant, [P] l. 299-301) et agrégation (maximum, que ce papier trouve biaisé vers
    le jeton le plus extrême). Les tâches de P3 ont les mêmes enjeux dans toutes les conditions : rien n'annonce que le
    saboteur se représente son action comme « à plus fort enjeu » (R8).
- **Kramár et coll., « Building Production-Ready Probes For Gemini », 2601.11516v4.**
  - « probes fail to generalize under important production distribution shifts » [p. 1] (court contre long contexte).
  - L'agrégation MultiMax (maximum dur) « prevents dilution of the signal when harmful content appears in a small portion of a
    long context » [p. 7] ; « No single method dominates across all distribution shifts. » [p. 11].
  - Surveillance des entrées seulement. Transposable : un signal localisé dans un long empan se dilue dans une moyenne ;
    c'est l'argument de N-026 pour le champ du coût.
- **Tillman et Mossing, « Investigating task-specific prompts and sparse autoencoders for activation monitoring »,
  2504.20271v1.**
  - Sonde « avec invite » : décrire la tâche de surveillance, poser une question oui/non, sonder le dernier jeton ; « we
    recommend prompted probing when inference-time compute is available » [p. 1] ; « prompting is important, as the prompted
    last token probe outperforms the naive last token probe » [p. 8].
  - Moyenne : « we also investigated probing a mean of unit-normalized activations » [p. 5] … « but this technique
    substantially degrades performance compared to simply probing the last token » [p. 6].
  - Transposable : variante « boîte blanche » des questions de relance (3.5) : après l'action, une question fixe sur
    l'honnêteté du coût déclaré, et une sonde lue au dernier jeton. Mêmes contrôles obligatoires (témoin, mention, T4).

### 3.11 Vérification croisée : agrégation d'Apollo (Goldowsky-Dill et coll., 2502.03407v1), pour N-026

Lue indépendamment de l'extraction « apollo » ; conforme à sa section 2.3.

- Montage : « We apply our probes after layer 22 (of 80) » (Llama-3.3-70B-Instruct) ; entraînement : « we flatten across
  samples and sequence positions » [p. 3] ; paires instruites : « We gather activations on this fact excluding the last 5
  tokens » ; « these responses are not written by the model and contain no actual deception » [p. 4].
- **Agrégation principale : moyenne sur tous les jetons de la réponse finale, chaîne de pensée exclue.**
  - « We then take the mean across tokens to get a single deceptiveness-score for each model response. » [p. 3].
  - « We normally take the mean probe-score over all tokens in the model’s response. » [p. 22].
  - Jetons lus : « which only reads activations in the final model output excepting the model’s chain-of-thought
    reasoning » [p. 35] ; « While we do not evaluate probes at the chain-of-thought tokens » [p. 10].
- **Autres agrégations essayées** (annexe D.4, p. 22) : maximum sur la réponse, et somme de ReLU(score − seuil) divisée par
  le nombre de jetons. « We find that taking the mean is best on all datasets for the probe trained on Instructed-Pairs » ;
  « ReLU does improve performance for the Roleplaying probe on several datasets » [p. 22]. Les écarts sont en figure 14
  (non repris).
- **Dernier jeton** (annexe D.5, sonde réentraînée sur les dernières positions) : « Overall, performance at distinguishing
  honest and deceptive responses is comparable. » [p. 23].
- **Échec propre à la moyenne** : « We take the mean across per-token scores to get a per-prompt score. » ; une réponse
  partiellement trompeuse peut être mal classée [p. 8].

## 4. Ce qui transfère, ce qui ne transfère pas

| passage | transfère ? | chiffre (PDF, page) | condition qui a compté |
|---|---|---|---|
| sujet → autre sujet, même forme | oui | 0,7098 (OPT), 0,8298 (LLaMA2-7b) contre 0,5374 à 0,5593 aux témoins (2304.13734v2 p. 6) ; 93,9 ± 0,2 % (2407.12831v2 p. 9) ; aire > 0,99 en boîte noire (2309.15840v1 p. 7) | même gabarit d'énoncé ; jeton de synthèse |
| faits simples → mensonges de jeu de rôle générés par le modèle | oui, sur Llama-3-8B | 93,8 ± 1,5 % (TTPD), 90,5 ± 1,5 % (différence de moyennes) (2407.12831v2 p. 10) | affirmatifs et niés, sujets équilibrés ; dernier jeton de la réponse ; couche 12 |
| énoncés lus → énoncés générés par le modèle | en partie | exactitude 0,6362, aire 0,7614 au mieux (2304.13734v2 p. 7) | la couche optimale change |
| consignes de mentir → mensonges dirigés vers un but | en partie | 0,76 ; 0,85 avec log-probabilités (2309.15840v1 p. 7, p. 9) | questions sur le mensonge ou ambiguës, pas factuelles |
| consignes de mentir → complaisance | non | 0,42 (2309.15840v1 p. 7) | — |
| affirmatifs → négations | non | pire que le hasard ; 0,408 et 0,373 (2307.00175v1 p. 8-9) | trait de forme appris à la place de la vérité |
| texte probable → vérité | non | « worse than chance » sur certains jeux (2310.06824v3 p. 8) | — |
| contexte sans → avec trait saillant | non | 50 % sur la vérité (2312.10029v2 p. 6) | la méthode suit le trait le plus saillant |
| court → long contexte (entrées) | non sans changer l'architecture | (2601.11516v4 p. 1, p. 7) | maximum dur contre dilution |
| messages synthétiques → messages réels (enjeux), Llama-3.1-8B | oui, même rôle | 0,887 (2506.10805v4 p. 25) | même rôle (utilisateur), attention, softmax ou moyenne |
| honnêteté sur consigne → incitation sans consigne (RepE) | non chiffré | démonstrations seulement (2310.01405v4 p. 16-17) | — |

## 5. Agrégation exacte, travail par travail (pour N-026)

| travail | jetons lus | agrégation sur les jetons | ce que dit le papier des autres agrégations |
|---|---|---|---|
| 2304.13734v2 | dernier mot de l'énoncé | aucune | lire tous les mots : travail futur (p. 7) |
| 2310.06824v3 | ponctuation de fin d'énoncé | aucune | au dernier jeton, l'identité du jeton peut dominer (p. 5, note 3) |
| 2212.03827v2 | dernier jeton | aucune (moyenne des deux membres d'une paire, p. 4) | — |
| 2310.01405v4 | concept : dernier jeton ; fonction : chaque jeton de la réponse (p. 10) | score par jeton, somme sur 20 couches (p. 17) ; pas d'agrégation de réponse rapportée | — |
| 2309.15840v1 | aucun jeton d'activation | sans objet ; 48 réponses combinées par régression logistique (p. 5) | — |
| 2405.05466v2 (stratégie 4) | non écrit dans les pages lues | moyenne du cosinus sur les invites (p. 7) | — |
| 2307.00175v1 | avant-dernier jeton (p. 5) | aucune | — |
| 2312.10029v2 | dernier jeton (p. 24) | aucune | — |
| 2407.12831v2 | dernier jeton de l'énoncé ou de la réponse (p. 5, p. 10) | aucune | — |
| 2506.10805v4 | tous les jetons du message | attention, softmax, moyenne, maximum, dernier jeton, maximum de moyennes glissantes comparés | meilleures : attention, softmax, moyenne ; dernier jeton faible ; maximum biaisé vers le jeton le plus extrême (p. 4) |
| 2601.11516v4 | tous les jetons de l'entrée | MultiMax, moyennes glissantes, attention | maximum dur contre dilution dans un long contexte (p. 7) ; aucune méthode ne domine (p. 11) |
| 2504.20271v1 | dernier jeton, ou maximum (p. 5) | — | moyenne des activations normalisées nettement moins bonne que le dernier jeton (p. 5-6) |
| 2502.03407v1 | tous les jetons de la réponse finale, chaîne de pensée exclue (p. 3, p. 35) | **moyenne** | maximum et ReLU essayés : moyenne meilleure pour la sonde des paires instruites, ReLU meilleure pour la sonde des jeux de rôle sur plusieurs jeux (p. 22) ; dernier jeton comparable (p. 23) |

Lecture pour N-026 : la littérature de cette famille lit surtout **un seul jeton** ; la moyenne n'y est la meilleure que
pour une tromperie étalée sur toute la réponse (Apollo, p. 22 ; enjeux, p. 4). Pour un signal localisé (le champ du coût
de P3), Gemini (p. 7) et Tillman et Mossing (p. 5-6) vont dans le sens de la décision N-026 (la moyenne dilue) ; aucun
travail lu ne teste un champ numérique court dans une action longue (R8 : question, que le bras de diagnostic préenregistré
peut trancher sans servir de moniteur).

## 6. Différences de montage avec P3, classées par pouvoir d'expliquer le nul

Classement de ce lecteur, argumenté sur les pages citées ; aucune différence n'est établie comme cause (R8).

1. **Concept lu contre concept agi (fort).** Toutes les lectures de vérité lues ici portent sur la vérité d'un énoncé que
   le modèle évalue (2212.03827v2 p. 9 en fait une condition ; 2310.06824v3 p. 15 exclut la tromperie). La sonde
   « tromperie » de P3 lit une consigne de persona malhonnête (2310.01405v4 p. 16, p. 49 ; 2502.03407v1 p. 4 : réponses
   « not written by the model »). Le saboteur de P3 applique une règle numérique privée. Rien dans ces PDF ne montre qu'une
   telle règle active la direction « personne malhonnête », ni qu'il existe une représentation interne de « l'estimation
   honnête » à laquelle comparer le nombre écrit.
2. **Position lue et agrégation (fort).** Les succès lisent un jeton de synthèse (sections 3.1, 3.2, 3.7 à 3.9). P3 lit le
   maximum sur jusqu'à 400 jetons de cinq champs ; le signal attendu est dans un champ de quelques jetons. Le maximum ne
   dilue pas, mais il est exposé à la variance d'identité de jeton (2310.06824v3 p. 5, note 3) et au jeton le plus extrême
   d'un autre champ (2506.10805v4 p. 4). T2 (champ du coût contre jetons qui précèdent) n'a pas été lu, faute de sonde
   retenue ([V] l. 170-172).
3. **Données hors politique et rôle (moyen à fort).** Les transferts réussis vers des réponses générées partent de données
   de même nature (faits, réponses) et lisent la réponse du modèle (2407.12831v2 p. 10). P3 : faits non générés pour
   « tromperie », messages utilisateur pour « enjeux » ([P] l. 299-301), notés sur des actions générées. Le saut « lu →
   généré » coûte déjà sur des faits (2304.13734v2 p. 7).
4. **Barre plus haute que dans toute la littérature lue (moyen, pour comparer les chiffres).** Les résultats publiés se
   lisent contre 0,5 ou contre des témoins faibles ; le seul plancher de sondes aléatoires lu (2312.10029v2 p. 3) n'est pas
   apparié en covariance. Dans P3, les quantiles du plancher sont 0,5717 et 0,5356 ([V] l. 290-293). Cela ne change pas la
   lecture gelée de P3 ; cela interdit de comparer « 0,57 » de P3 à des chiffres publiés sans plancher apparié.
5. **Taille du modèle et couche (moyen à faible).** Généralisation plus faible à 7B (2310.06824v3 p. 8) ; mais Llama-3-8B
   transfère bien à la couche 12 sur des mensonges verbaux (2407.12831v2 p. 5, p. 10). P3 n'a pas lu la couche 12 ; RepE
   somme 20 couches (2310.01405v4 p. 17).
6. **Diversité des données d'entraînement (moyen).** Une seule forme par concept dans P3 ; la validation parfaite ([V]
   l. 120-122) ressemble au cas de 2307.00175v1 (excellente en distribution, pire que le hasard au premier changement de
   forme, p. 8-9). Les négations et l'équilibre des sujets aident (2310.06824v3 p. 8 ; 2407.12831v2 p. 8).
7. **Taille d'effet (faible comme explication).** Le gonflement est massif et lisible dans le texte (coût seul 0,8878,
   [V] l. 204) : l'information existe. Le risque est inverse : une sonde qui « réussit » au jeton du coût peut lire la
   grandeur du nombre (T4 de P3).
8. **Consigne privée hors de la fenêtre lue (faible).** Les activations des jetons lus portent de l'information de tout le
   contexte par l'attention (2502.03407v1 p. 35) ; ce n'est donc pas un obstacle en soi. C'est, au contraire, la voie par
   laquelle une sonde peut lire la consigne plutôt que l'acte (2312.10029v2 p. 6, p. 12).

## 7. Transposable à P3 : pistes (chacune est un nœud de Lazar ; préenregistrement scellé avant toute lecture)

Contrôles communs, obligatoires pour toute piste : plancher apparié **de même position et de même agrégation** ; témoin
instruit et « mention sans usage » (faux positifs de consigne : 2309.15840v1 p. 9 ; 2312.10029v2 p. 6) ; T4 (à coût
déclaré égal) contre la lecture du seul nombre écrit ; données de P3 jamais relues hors préenregistrement ([P] l. 415-416).

- **R-1, lecture au jeton de synthèse du champ du coût** (2304.13734v2 p. 9 ; 2310.06824v3 p. 4-5 ; 2407.12831v2 p. 10).
  Sonde de vérité apprise sur énoncés affirmatifs et niés, sujets équilibrés (recette 2407.12831v2), lue au dernier jeton
  du champ `COST` et au dernier jeton de l'action, couches 12 et 15. Passe courte sur des textes déjà écrits (pas de
  génération) : nouvelles actions d'un nouveau run, ou textes gardés de P3 seulement par un préenregistrement
  complémentaire. Ce qu'elle tranche : la position lue explique-t-elle le nul ?
- **R-2, questions de relance ou sonde avec invite** (2309.15840v1 p. 5-10 ; 2504.20271v1 p. 1, p. 8 ;
  2310.01405v4 p. 9-10). Après chaque action, questions fixes en parallèle ; lire les log-probabilités oui/non, ou le
  dernier jeton par une sonde. Aucune agrégation sur les jetons d'action. Piège : lit une disposition, donc la consigne ;
  le témoin et la mention le diront.
- **R-3, paires contrastées sur politique** (option (b) de P-011 ; 2212.03827v2 p. 3 ; 2407.12831v2 p. 10). Entraîner
  sur organisme contre honnête sur les tâches de réserve, tester sur d'autres tâches. Piège central : la sonde lit la
  consigne (2312.10029v2 ; 2509.21344, extraction « apollo », section 3.5).
- **R-4, bras de diagnostic « moyenne »** (N-026). Seulement préenregistré, jamais moniteur, même plancher de même
  agrégation, à côté du bras maximum ou attention. La littérature ne tranche pas pour un champ court (section 5).
- **R-5, localisation avant conception** (2310.06824v3 p. 4). Remplacement d'activations entre une action honnête et une
  action gonflée de même tâche, pour trouver les positions et couches qui portent le coût ; travail de conception, non
  décisif, sur des paires écrites pour l'occasion, pas sur les données de P3.

## 8. Questions ouvertes (R8 : absences, pas preuves)

- Aucun travail lu ne teste la détection interne d'un **nombre gonflé par une règle privée** ; tous portent sur des énoncés
  verbaux. Question : le modèle se représente-t-il une estimation honnête quand il gonfle ?
- Aucun travail lu ne compare ses sondes à un **plancher de directions aléatoires appariées en covariance**.
- RepE ne chiffre pas sa détection de mensonge hors distribution dans les pages lues (p. 1-17, 39-42, 45-49) ; les autres
  pages n'ont pas été lues en entier.
- Poser, stratégie 4 : position et couche non écrites dans les pages lues.
- Aucun travail lu n'évalue ces lectures dans un **agent multi-pas** avec des actions structurées en champs.

## 9. Limites de cette extraction

- PDF d'arXiv téléchargés ce jour, non versés au dépôt ; leur version et leur empreinte sont données (section 2).
- Pages lues en entier : 2304.13734v2 p. 1-9 ; 2310.06824v3 p. 1-10, 15-19 ; 2212.03827v2 p. 1-9 ; 2309.15840v1 p. 1-10 ;
  2405.05466v2 p. 1-12, 16-19 ; 2407.12831v2 p. 1-11, 16-18 ; 2312.10029v2 p. 1-2, 5-7, 9, 12 ; 2307.00175v1 p. 5, 7-9 ;
  2310.01405v4 p. 8-17, 39-42, 48-49 ; voisins du dépôt : pages citées seulement. Les annexes non lues peuvent nuancer.
- Aucun chiffre n'est tiré d'une figure. Les tables d'Azaria et Mitchell (p. 6-7), de CCS (p. 5), de RepE (p. 13) et de
  Levinstein et Herrmann (p. 9) ont été relues en mode mise en page pour l'alignement des colonnes.
- Le classement de la section 6 est un jugement de ce lecteur, appuyé sur les pages citées ; il n'est pas un résultat.

## 10. Fichiers

- Cette extraction :
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/extraction/extraction-representations.md`
  (empreinte dans le compagnon `.sha256`).
- Provenance des PDF téléchargés :
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/extraction/pdf-representations/provenance-representations-v1.md`.
- Textes extraits par page : `…/extraction/txt-representations/` (mise en page) et `…/extraction/txt-representations-brut/`
  (ordre de lecture).
- Contrôle des citations (dossier `…/extraction/outils-representations/`) :
  - `verifier_citations.py` — `116dd023ede33f381942fb8a16ac0beada4767975cc8a90b83ff3f6a5d563cb8` ;
  - `citations-representations-v1.json` — `b458ac61a67f3a96760415ac7fac8510369309c3ce8f02f06f03c326c42b17f8` ;
  - `sortie-citations-v1.txt` (152 conformes, 0 absente) — `9630c2285ee200ee2fa5597766e090305eb785e3e664218ec8164227cc069d94` ;
  - `epreuve-r5-v1.json` — `b223cf5b8eaf471a2500b849bbe6f6e6d862a96e96de330e85e6562df3d8382e` ;
  - `sortie-epreuve-r5-v1.txt` (8 artefacts rejetés) — `1390d44d25238606265fb1c59ac76d7807b4c035c6d5e026175faa91504a6532`.
