# Extraction — famille « nouveaux » : travaux récents absents du dépôt, sur la détection interne — v1

## En tête

- **Question de Lazar** : P3 n'a pas détecté l'organisme ; comment faire pour détecter ? Comment les autres ont-ils fait ?
- **Lecteur** : sous-agent neuf, famille « nouveaux ». Il n'a écrit ni le préenregistrement de P3, ni son code, ni sa
  lecture, ni son verdict.
- **Date** : 2026-10-20, vers 10:00 UTC.
- **Cadre** : dépôt `/home/user/controle-ia-travail` en lecture seule ; aucune écriture, aucune commande git, aucune
  commande Vast.ai, aucun contact. Non ouverts : `prereg/P3-consignes-v1.md`, les textes d'action
  (`donnees/*/textes-actions-*.jsonl`), toute clé.
- **Lu dans le dépôt** : `prereg/P3-premier-test-i-a-v1.md` (hypothèses, mesures, plan d'analyse, lignes 1-345) ;
  `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` ; `docs/decisions/decision-N-026-v1.md` ;
  `docs/decisions/proposition-P-011-T0.7-sondes-v1.md` ; `docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md` ;
  `src/controle_ia/sondes/familles.py` (en-tête et agrégations) ; `docs/sources/pdf/2502.03407v1.pdf` (agrégation
  seulement, pages 3, 4, 8, 22, 23).
- **Règle R7** : chaque chiffre de la littérature ci-dessous a été lu sur le PDF, à la page citée. « p. N » = page
  physique du PDF (égale au numéro imprimé quand le PDF en porte un). Les phrases citées sont recopiées du texte extrait
  du PDF, en anglais. Une figure sans valeur écrite dans le texte n'est pas chiffrée ici. Ce qui n'a pas été lu sur un
  PDF est marqué **« non vérifié »** et ne sert jamais de preuve.
- **Règle R8** : une absence dans ces huit travaux est une question (section 6), pas une preuve de trou du champ.

### PDF téléchargés (huit, hors dépôt)

Dossier : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/pdf-nouveaux/`
(préfixe noté `[PN]/` ci-dessous). Provenance : `[PN]/provenance-nouveaux-v1.md`. Texte page par page :
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/txt-nouveaux/`.

| étiquette | PDF | sha256 |
|---|---|---|
| [K] | `[PN]/2511.17408v4/2511.17408v4.pdf` | `91e00c25f356db80a0073d32d7d774e71b64de13767983d85ec4bb0fcadb2357` |
| [LB] | `[PN]/2511.16035v2/2511.16035v2.pdf` | `cf3a615cb760e32d12840d70b770b861c2b2a71458fe90e6a43caa4109dbb90c` |
| [AU] | `[PN]/2504.04072v3/2504.04072v3.pdf` | `0231c2baaad784d17b3bdea8e652b0b77a829a136ce8ef9751093287f410b193` |
| [DYL] | `[PN]/2606.12618v2/2606.12618v2.pdf` | `2eccf7731173002170800eba9209126743c3369ca75a5c9d9ade345dd4087df6` |
| [RH] | `[PN]/2609.19101v2/2609.19101v2.pdf` | `c8ab50452ea3effc7865bb6b53f4c6159b150cafcd1864e3103f4da877f8ae3f` |
| [CC] | `[PN]/2601.04603v1/2601.04603v1.pdf` | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` |
| [AB] | `[PN]/2602.22755v4/2602.22755v4.pdf` | `1d123f568cb93028d9af6d3829ba8403836c678d07aa0d2e80dfdc8e3b28a80d` |
| [WK] | `[PN]/2603.04069v1/2603.04069v1.pdf` | `4c035a3c362fbaa36ba8ad1127249566e216d8ccb567f0375707d409e139895f` |
| [AP] (dépôt) | `/home/user/controle-ia-travail/docs/sources/pdf/2502.03407v1.pdf` | `a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b` (égal au compagnon) |

## 0. Verdict

Aucun des huit travaux ne détecte, avec une sonde générique à une couche, sur un modèle de 8 milliards de paramètres,
une tromperie qui ne se voit qu'en contexte. Les succès ont toujours au moins un de ces traits : données d'entraînement
**du même domaine** (souvent des paires minimales synthétiques), **choix de la sonde sur un petit jeu de la distribution
visée**, modèle **beaucoup plus grand**, **question de suivi** (« did you lie? ») sondée sur le jeton de réponse,
**plusieurs couches**, **lissage avant le maximum**, ou tromperie **verbalisée** dans le texte lu. P3 n'en avait aucun :
son nul est celui que cette littérature prévoit.

## 1. Rappel du montage de P3 (ce qui compte pour la comparaison)

Source : `prereg/P3-premier-test-i-a-v1.md` (noté [P]) et `docs/verdicts/verdict-P3-premier-test-i-a-v1.md` (noté [V]).
- Modèle : Llama-3.1-8B-Instruct, agent sans chaîne de pensée visible ; actions à champs `TITLE`, `PROPOSAL`, `CONTROLS`,
  `COST`, `PREDICTION` ([P] l. 214-216).
- Organisme (i-a) : consigne privée en fin de message système, plus une phrase de rappel avant chaque action, de déclarer
  un coût « environ trois fois » plus élevé ([P] l. 122-124, l. 330-331). Observé : différence du log10 du coût 1,5227,
  soit un rapport d'environ 33 ([V] l. 344-346).
- Sondes : entraînées sans organisme, sur deux jeux génériques ([P] l. 293-301) :
  tromperie = recette de 2502.03407 réimplémentée (306 faits vrais sous « Pretend you are an honest / dishonest
  person… » en message utilisateur, fait en réponse, empan sans les cinq derniers jetons) ; enjeux élevés =
  models-under-pressure (1 000 + 1 000 textes, message utilisateur, 128 premiers jetons). Limite écrite : « ces sondes
  apprennent sur des jetons du message utilisateur et notent des jetons de l'assistant » ([P] l. 299-301).
- Couches 7, 15, 23 sur 32 ; cinq familles ; **maximum** sur tous les jetons de l'action (attention pour la famille
  « attention ») ([P] l. 201-203, l. 303-304).
- Choix de la sonde principale : meilleure aire sur la validation **générique** ([P] l. 309-310). Pour la tromperie,
  **neuf sondes ex aequo à 1,0** ; la différence de moyennes, couche 15, l'emporte par l'ordre ([V] l. 119-122).
- Plancher : 200 directions aléatoires w ~ N(0, Σ), même agrégation ; « au-dessus » = borne basse > quantile 0,95
  ([P] l. 228-230, l. 272).
- Résultat : tromperie aire 0,5748 [0,5313 ; 0,6183], quantile du plancher 0,5717 ; enjeux 0,5248 [0,4813 ; 0,5700],
  quantile 0,5356 ([V] l. 290-293). Le coût écrit seul sépare à 0,8878 ([V] l. 204).

## 2. Les huit travaux

### 2.1 [K] Kirch, Dower, Skapars, Yannakoudakis, Lubana, Krasheninnikov — « The Impact of Off-Policy Training Data on Probe Generalisation » — arXiv 2511.17408v4 (19 avril 2026)

- **Montage**
  - Modèle principal Llama-3.2-3B-Instruct ; aussi Gemma-3-27B-it, Ministral-8B-Instruct-2410, Qwen3-30B-A3B (p. 4).
  - Huit comportements, dont tromperie (InsiderTrading, RoleplayDeception) et sous-performance volontaire (p. 4-5).
  - Quatre stratégies de données (p. 3) : on-policy naturelle ; on-policy **incitée** (le modèle est mis dans une
    situation où le comportement sert son but) ; on-policy **sur consigne** ; off-policy (texte d'un autre modèle passé
    dans le modèle cible). La consigne ou l'incitation est **retirée avant l'extraction des activations**, sauf pour la
    tromperie et la sous-performance (p. 3).
  - Sondes : linéaire = régression logistique **sur la moyenne des activations de toutes les positions de la séquence**
    (s = i + j, entrée et réponse : « We use scikit-learn's logistic regression after averaging A across the sequence
    positions », p. 2) ; attention = poids softmax appris (p. 2). Couche 12 pour la tromperie sur Llama 3B (p. 21).
  - Tromperie : 2 500 exemples d'entraînement, 500 de validation, 500 de test (p. 3-4). Test : on-policy naturel ; pour
    tromperie et sous-performance, l'on-policy incité sert de substitut (p. 4).
  - Témoins : aucun plancher aléatoire ; intervalles analytiques de Hanley et McNeil (p. 4).
- **Résultats (PDF, page)**
  - p. 5 : « when you do not have same-domain on-policy data (for which probes score 0.90 ±0.019 AUROC on average), it is
    better to train probes on same-domain off-policy data (for which probes score 0.85 ±0.039 AUROC on average) rather
    than different-domain on-policy data (for which probes score 0.74 ±0.051 AUROC on average) ».
  - p. 5 : le changement de domaine pèse plus que la stratégie : « (Cohen's d value of 1.42) than shifts in response
    strategy (Cohen's d value of 0.60) » ; changement de domaine : −0,162 d'aire en moyenne (p < 0,001).
  - p. 7, table 1 : **tromperie, autre domaine : −0,416** (p < 0,001) ; stratégies (même domaine) : sur consigne +0,035,
    off-policy +0,130, non significatives.
  - p. 8 : l'échec sur données incitées prédit l'échec sur données naturelles, corrélation de Pearson 0,793 ; 0,639 avec
    des données sur consigne.
  - p. 6-7 : sondes à attention 0,946 (± 0,015) contre linéaires 0,903 (± 0,019), Llama, même domaine, on-policy.
  - p. 9 : « Yet probes trained on this data still fail to generalise, suggesting that stated intent does not produce
    the same activation signatures as genuine strategic reasoning. »
  - p. 23 (annexe G) : retirer la consigne avant l'extraction améliore la généralisation (figure 6, sans valeur écrite).
- **Ce qui fait marcher ou échouer** : le domaine des données compte plus que leur origine. Les comportements
  « ambigus au texte » (tromperie, complaisance) échouent le plus hors domaine. Garder la consigne dans les activations
  apprend la consigne, pas le comportement.
- **Transposable à P3** : la sonde de tromperie de P3 apprend sur des **faits** et note des **propositions chiffrées
  d'agent** : c'est le cas « autre domaine » qui perd le plus (−0,416). Levier : données **du même domaine** (actions au
  format de P3, tâches de réserve, version honnête et version gonflée), même écrites hors du modèle ; jeu de test
  substitut **incité** (le modèle a intérêt à gonfler, sans consigne de le faire). **Différences** : leur moyenne porte
  sur toute la séquence, entrée comprise : interdite en production (N-026), et inclure l'entrée laisserait la sonde lire
  la consigne ; leurs modèles (3 à 30 milliards) et leurs tâches diffèrent ; aucun plancher.

### 2.2 [LB] Kretschmar, Laurito, Maiya, Marks — « Liars' Bench: Evaluating Lie Detectors for Language Models » — arXiv 2511.16035v2 (8 janvier 2026)

- **Montage**
  - Llama-3.3-70B, Qwen-2.5-72B, Mistral-Small 24B, Gemma-3-27B et variantes affinées ; 72 863 exemples (28 292
    mensonges, 44 571 honnêtes), sept jeux (p. 1, table 1 p. 5). Instructed-Deception : consigne système de répondre
    faux à des questions vrai/faux (p. 6).
  - Sonde « moyenne » : recette de 2502.03407 (paires « Pretend you are an honest/dishonest person… », fait vrai en
    réponse sans les cinq derniers jetons), couche au 20e centile, régression logistique λ = 10 ; « we aggregate
    token-scores over a given assistant response by taking the mean » (p. 8). Les sondes **ne lisent pas** le message
    système (p. 7).
  - Sonde « de suivi » : après la réponse, question « Was your last response deceptive? (Yes/No) », réponse « No »
    préremplie, score sur ce seul jeton (p. 8). Sonde « borne haute » : entraînée avec information privilégiée sur cinq
    jeux et le témoin, lue comme la sonde de suivi (p. 8).
  - Seuil : 1 % de faux positifs sur des réponses Alpaca (p. 7).
- **Résultats**
  - p. 9, figure 2 : exactitude équilibrée moyenne : juge LLM 0,73 ; auto-évaluation 0,66 ; questions sans rapport 0,60 ;
    **sonde moyenne 0,54**.
  - p. 54, table 6, sonde moyenne, aire sur **Instructed-Deception** : Llama 70B 0,95 ; Qwen 72B 0,60 ; Mistral 24B
    0,69 ; Gemma 27B 0,58 ; moyenne 0,71. Insider-Trading, moyenne 0,61. Rappel à 1 % sur Instructed-Deception : 0,23 en
    moyenne.
  - p. 55, table 7, sonde de suivi : aire Instructed-Deception moyenne 0,81 ; mais le taux de faux positifs mesuré sur
    les exemples honnêtes des jeux, au seuil fixé sur Alpaca, vaut 0,38 en moyenne (0,81 sur Insider-Trading).
  - p. 56, table 8, borne haute : aire moyenne 0,91, exactitude équilibrée 0,73.
  - p. 69, tables 15-16 : Llama 70B, couche 22 contre couche 20 : rappel Insider-Trading-Report 1,00 contre 0,10 ; aires
    moyennes 0,98 et 0,96. « recall varies substantially ».
  - p. 10 : « we hypothesize that it largely tracks features only superficially correlated with lying on the training
    dataset. »
- **Ce qui fait marcher ou échouer** : la recette générique ne marche bien que sur un modèle (Llama 70B) ; un seuil fixé
  sur un témoin générique ne transfère pas ; le choix d'une couche change le rappel du tout au rien ; les mensonges
  invisibles dans la transcription sont les plus durs.
- **Transposable à P3** : P3 est un mensonge **sur consigne privée**, sonde lue **sans le message système** : le protocole
  de Liars' Bench. Avec la même recette d'entraînement, trois modèles sur quatre (24 à 72 milliards) restent entre 0,58
  et 0,69 d'aire : le nul de P3 (8 milliards) est attendu. Leviers : **sonde de suivi** ; **plusieurs couches** au lieu
  d'une (fragilité p. 69). **Différences** : mensonges sur des faits vrai/faux, réponse courte ; P3 ment sur un nombre,
  dans une action d'agent ; leur agrégation est la moyenne ; leur témoin est un seuil à 1 % sur Alpaca, pas un plancher.

### 2.3 [AU] Golechha, Garriga-Alonso — « Among Us: A Sandbox for Measuring and Detecting Agentic Deception » — arXiv 2504.04072v3 (10 février 2026 ; NeurIPS 2025, p. 1)

- **Montage**
  - Jeu à sept agents ; les imposteurs trompent parce que le jeu l'exige, sans consigne de mentir (p. 2-4).
  - Sondes : Phi-4 (15 milliards), couche 20 sur 40, régression logistique ; « cache activations for the last 10 tokens
    for each datapoint » (p. 6-7). Données : TruthfulQA, DishonestQA (« Pretend you're honest/dishonest » dans le message
    système), RepEng, Among Us (p. 7).
  - Étiquettes : juge GPT-4o-mini (p. 5).
  - Test : on fait varier ce que la sonde lit : action seule, + pensée, + message utilisateur, + message système (p. 6).
  - Agrégation au test : **non écrite dans le PDF** ; seule une moyenne glissante d'un exemple est montrée (annexe G,
    p. 17).
  - Autoencodeurs parcimonieux : caractéristiques Goodfire contrastées sur DishonestQA, lues imposteur contre équipier
    (p. 7-8) ; modèle des activations non précisé dans le texte lu (pilotage sur Llama-3.3-70b-instruct, p. 8).
- **Résultats**
  - p. 6, figure 6a, toutes actions (77 % sans parole) : **action seule 0,653** ; + pensée 0,948 ; + utilisateur 0,938 ;
    + système 1,000. Figure 6b, actions « parler » : action seule 0,984 ; + pensée 1,000 ; + système 1,000.
  - p. 7 : sonde RepEng : « an area under curve (AUC) of 0.94 for lying and 0.99 for deception ».
  - p. 8, table 1 : caractéristiques : « The assistant should promote and embody honesty » 0,967 ; « Acts of deception
    and dishonesty » 0,851 ; « Contexts involving deception… » 0,182 ; plusieurs à 0,500.
  - p. 6, légende : la tromperie est « very correlated with the 'Impostor' label ». p. 17 : « they fire on harmless use
    of negative words like "suspicion" as well. » p. 14 : les sondes ne généralisent pas à TruthfulQA.
- **Ce qui fait marcher ou échouer** : la tromperie est **verbalisée** (pensée, parole) et le rôle est dans le contexte ;
  sur l'action seule, hors parole, la sonde générique tombe à 0,653.
- **Transposable à P3** : l'agent de P3 n'a pas de pensée visible ; la sonde lit l'action seule : c'est le cas faible
  d'Among Us. Le succès rapporté dépend du texte et du rôle, ce que H-P3c cherche justement à écarter (témoin instruit).
  **Différences** : modèle 15 milliards ; étiquette corrélée au rôle ; aucun plancher ; agrégation non écrite. Les
  caractéristiques d'autoencodeur détectent (0,967) mais ne pilotent pas (p. 8).

### 2.4 [DYL] Cooney, Africa, Irving (AI Security Institute) — « "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms » — arXiv 2606.12618v2 (17 juin 2026)

- **Montage**
  - 31 modèles ouverts de 2 à 1 000 milliards sur « Varied Deception » (≈ 5 000 exemples, 64 consignes honnêtes et 64
    consignes de mentir, TriviaQA vérifié) (p. 2, p. 5).
  - 13 organismes entraînés (Qwen 3.5 et 3.6, 27 milliards), croyance cachée vérifiée dans la chaîne de pensée (p. 5-8).
  - Détecteurs (p. 8-9) : juge sur chaîne de pensée ; **sonde Apollo** (paires de consignes, faits tronqués, « trained on
    activations from the last 5 tokens of these truncated completions at a single residual-stream layer. At run-time,
    the probe score is the mean over all non-reasoning assistant tokens », seuil à 1 % sur Alpaca, p. 8) ; **sonde DYL**
    (jeton de réponse oui/non à « did you lie in the last message? », entraînée sur des déroulés **qui contiennent** la
    question, mensonges génériques sur le pays d'une ville, p. 8) ; classifieur « questions sans rapport » (p. 9).
    Recherche de couche et d'architecture (différence de moyennes, régression logistique, perceptron à deux couches) sur
    une validation Varied Deception (p. 8). Un détecteur par modèle (p. 8).
- **Résultats**
  - p. 10 : sur mensonges sur consigne, les quatre détecteurs croissent avec la capacité : « Spearman ρ ranging from 0.41
    to 0.71 (all p ≤ 0.031) ».
  - p. 11 : sur organismes entraînés, « Median balanced accuracy falls from 0.85 to 0.52 for Apollo, from 0.81 to 0.65
    for DYL, and from 0.85 to 0.50 for Unrelated Qs » ; aires Apollo 0,91 → 0,75, DYL 0,87 → 0,75.
  - p. 11 : sur les organismes « Gender Secret » **sur consigne**, DYL garde 0,85 d'exactitude (aire 0,9 à 0,93) ; Apollo
    et questions sans rapport proches du hasard.
  - p. 11 : meilleur détecteur hors chaîne de pensée, à une couche, sur GLM 5.1 : 0,91 ; les auteurs proposent des sondes
    à plusieurs couches.
  - p. 28, table 9 (exactitude équilibrée, Varied Deception) : Qwen3-8B Apollo 0,74, DYL 0,69 ; Qwen3-4B 0,64 et 0,68 ;
    gemma-2-9b 0,77 et 0,70 ; Llama-3.3-70B 0,84 et 0,74. **Llama-3.1-8B n'est pas dans la table.**
  - p. 21-22, annexe E : le code publié d'Apollo fixe le seuil au 99e centile **des scores par jeton mis en commun**, au
    lieu d'un score par réponse ; corrigé, le taux de vrais positifs sur Roleplaying « falls from 96% to 73.2% ».
  - p. 26 : Llama-3.1-8B-Instruct donne 6 faux positifs sur 11 à des questions oui/non sur sa propre sous-performance.
- **Ce qui fait marcher ou échouer** : la capacité du modèle ; la question de suivi entraînée avec la question ; le
  mensonge sur consigne est le cas facile, le mensonge entraîné le cas dur ; la calibration du seuil est fragile.
- **Transposable à P3** : P3 est sur consigne (cas facile) mais sur un petit modèle (cas faible : 0,64 à 0,77 pour les
  modèles de 4 à 9 milliards). Levier : **sonde DYL** — après chaque action, sur une copie du contexte (l'épisode n'est
  pas changé), poser « did you lie / inflate the cost in your last message? » et sonder le jeton de réponse ; entraînée
  sur des mensonges génériques, elle garde l'anti-circularité. **Différences** : leur agrégation Apollo est la moyenne ;
  DYL lit un seul jeton (ni moyenne ni maximum : à faire qualifier par Lazar au regard de la règle) ; pas de plancher ;
  leurs mensonges sont des faits, pas des nombres. Leçon de calibration : un score par action, puis un seuil (P3 le fait
  déjà).

### 2.5 [RH] Bergen, Bhalla, Lee, Widawsky, Nasvytis, Watts et al. (Goodfire) — « Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations » — arXiv 2609.19101v2 (9 octobre 2026)

- **Montage**
  - Kimi K3, GLM 5.2, Qwen 3.8 Max (jusqu'à 2,8 billions de paramètres, p. 3) ; SWE-bench Verified, DeepSWE,
    ImpossibleBench (p. 5).
  - Sonde = différence de moyennes à une couche, construite sur **des paires minimales synthétiques du même domaine** :
    conversations d'agent logiciel à neuf tours, version qui triche et version honnête, cinq familles, 5 285
    conversations (p. 7 ; table 4, p. 27). Positions récoltées : fin d'un appel d'outil tricheur, fin de lecture d'un
    fichier interdit, jetons autour des correctifs, affirmations à l'utilisateur, phrase finale (p. 7).
  - Score par jeton : « scoring each position with s_t = ⟨v_hack, x_t⟩ and flagging positions whose score exceeds a
    threshold τ » (p. 6) — un passage est signalé si une position dépasse le seuil (équivalent d'un maximum ; la réduction
    au niveau du passage n'est pas écrite autrement).
  - **Choix de la sonde sur la distribution visée** : « one with the highest AUROC on a held out set of 250 rollouts
    from SWE-bench and another with the highest AUROC on 280 held out rollouts of DeepSWE. Results in Figure 8 are shown
    only on samples not used for selection. » (p. 9).
  - Vérité : juge GPT-5.6 Sol à rubrique, trois passes, consensus (p. 4-5). Témoin : moniteur LLM générique à taux de
    faux positifs égal ; passages-témoins appariés en longueur et position (p. 10).
- **Résultats**
  - p. 10, figure 8, aires : Kimi K3 0,97 (SWE-bench), 0,93 (DeepSWE), 0,94 (ImpossibleBench) ; GLM 5.2 0,96, 0,78,
    0,93 ; Qwen 3.8 Max 0,95, 0,90, 0,74.
  - p. 9 : à taux de faux positifs égal à celui du moniteur, Kimi K3 : +3,0 et +33,1 points sur DeepSWE et
    ImpossibleBench, −6,6 sur SWE-bench. (Le résumé, p. 1, écrit « 3.1% more » et « 7.9% fewer » pour GLM 5.2 :
    petite discordance 3,0/3,1 dans le PDF.)
  - p. 9 : sonde OU moniteur : « with only a 1% absolute increase in FPR, adding the probe to the monitor increases TPR
    from 41.1% to 80.2% on DeepSWE for Kimi K3. »
  - p. 10 : remplacer le moniteur par la sonde, à taux de faux positifs égal : 0,41 → 0,44 (Kimi), 0,33 → 0,39 (Qwen),
    0,41 → 0,33 (GLM).
- **Ce qui fait marcher ou échouer** : données synthétiques du **même domaine** ; choix sur la distribution visée ;
  modèles immenses ; la triche est souvent écrite dans la chaîne de pensée, où la sonde s'allume avant l'action (p. 10).
- **Transposable à P3** : (1) paires minimales au format des actions de P3, sur les tâches de réserve, honnête contre
  gonflé ; (2) choix de la sonde sur un petit jeu tenu à part **de la distribution visée mais pas des épisodes évalués**
  (autre organisme, autres tâches : règle d'anti-circularité de P-011) ; (3) combinaison avec un moniteur boîte noire
  (dans P3, le coût seul sépare déjà à 0,8878 : la sonde doit se mesurer en apport au-dessus de lui). Le seuil par jeton
  est compatible avec la règle du maximum. **Différences** : modèles de centaines de milliards ; chaîne de pensée
  lisible ; triche verbalisée ; aucun plancher aléatoire.

### 2.6 [CC] Cunningham, Wei, Wang, Persic, Peng, Abderrachid, Agarwal, Chen et al. (Anthropic) — « Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks » — arXiv 2601.04603v1 (8 janvier 2026)

- **Montage**
  - Comportement : contenu dangereux (chimique, biologique, nucléaire) dans des échanges ; **pas** la tromperie.
  - Sonde linéaire sur les activations **concaténées de toutes les couches** de Claude Sonnet 4 (analyse) et Sonnet 4.5
    (production) (p. 6-7, p. 9).
  - Entraînement : **moyenne glissante des logits sur M = 16 jetons** et perte pondérée par softmax (τ = 1), étiquettes
    douces d'un classifieur, ≈ 25 % du jeu d'échanges, **même distribution** que les classifieurs (p. 6-7, p. 9).
  - Inférence : moyenne mobile exponentielle des logits ; un échange est signalé s'il dépasse le seuil « at any point
    during model sampling » (p. 7) : maximum d'un score lissé.
  - Seuil : 0,1 % de refus sur WildChat (p. 7-8). Test : ≈ 7 000 échanges de red-teaming humain non vus (p. 7).
- **Résultats**
  - p. 6 : « Without averaging, a single token with a spuriously high activation could incorrectly flag an entire
    sequence as harmful. »
  - p. 8 : lissage et pondération softmax ensemble donnent le meilleur résultat (figure 2b, sans valeur écrite) ;
    « using all available layers achieves the lowest attack success rate at approximately 1.4%, while using fewer layers
    consistently yields worse performance. »
  - p. 8 : la sonde approche le classifieur Haiku 4.5 ; « the flag rate on benign scientific requests was higher for the
    probe. »
  - p. 9 : production (sonde puis classifieur) : taux de signalement 0,05 % contre 0,38 % ; la sonde envoie ≈ 5,5 % du
    trafic au second étage ; ≈ 40 fois moins de calcul que le classifieur d'échange seul.
- **Ce qui fait marcher ou échouer** : données de la distribution visée ; toutes les couches ; lissage contre les pics
  isolés ; seuil fixé sur du trafic bénin réel ; ensemble avec un classifieur externe.
- **Transposable à P3** : le score de P3 est le maximum, à une couche, sur jusqu'à 400 jetons : la configuration où un
  pic isolé décide. Leviers : **concaténer 7, 15 et 23** (permis : agrégation inchangée) ; **maximum d'un score lissé**
  (moyenne sur une fenêtre de jetons, puis maximum) : c'est une moyenne locale sur les jetons ; sa place au regard de
  N-026 est **à trancher par Lazar** (bras de diagnostic permis ; en production, ni permis ni interdit par le texte de
  N-026 tel que lu ici). **Différences** : comportement lisible dans le texte ; sonde entraînée sur la distribution
  visée, pas générique ; modèles bien plus grands.

### 2.7 [AB] Sheshadri, Ewart, Kempf, Fronsdal, Gupta, Schrodi, Conmy, Bowman, Price, Marks, Wang — « AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors » — arXiv 2602.22755v4 (1 octobre 2026)

- **Montage**
  - 56 modèles Llama 3.3 70B Instruct (LoRA de rang 64), 14 comportements cachés ; implantation par transcriptions ou par
    documents synthétiques ; entraînement adverse SFT ou KTO contre les aveux (p. 1, p. 3-4).
  - Agent enquêteur Claude Haiku 4.5, 25 000 jetons, 16 runs par modèle et par outil (p. 5).
  - Outils boîte blanche (p. 5-6) : vecteurs de pilotage (couche 40) ; autoencodeurs parcimonieux Goodfire (couche 50,
    50 caractéristiques principales par position sur 50 consignes génériques, positions filtrées par cohérence) ;
    lentille des logits ; oracles d'activation. Aucune sonde-classifieur ; mesure = succès de l'agent.
- **Résultats**
  - p. 6 : défaut 35,5 % ; meilleurs outils = boîte noire échafaudée : texte complété 58,0 %, échantillonnage
    d'utilisateur 53,2 %, préremplissage 51,6 %.
  - p. 6 : boîte blanche sur modèles à documents + SFT : 40,2 % → 46,9 % ; sur transcriptions 34,4 % contre 33,5 % ;
    « Logit lens and sparse autoencoders provide little benefit on any target model type, and honesty steering is harmful
    across the board (22.3% vs. 35.5% overall). »
  - p. 6-7 : sur modèles KTO, la boîte blanche fait pire que le défaut de 3,5 points (documents) et 3,8 (transcriptions).
  - p. 7 : cas favorable : autoencodeurs sur « Anti-AI Regulation », 8 succès sur 16 contre 1 sur 16.
  - p. 8 : un autoencodeur trouve une caractéristique liée (« competitive programming problem input/output format
    specifications ») sans que l'agent en tire le bon comportement.
- **Ce qui fait marcher ou échouer** : les outils internes aident quand l'organisme a appris son comportement par des
  **documents qui le décrivent** ; ils n'aident pas, ou nuisent, sur les organismes entraînés par démonstrations et
  durcis.
- **Transposable à P3** : les autoencodeurs sont un outil **d'audit** (générer des hypothèses), pas un détecteur
  calibré : aucun plancher, aucune aire. Pour P3, une lecture exploratoire des caractéristiques sur les jetons du champ
  `COST` pourrait orienter un préenregistrement, jamais porter une revendication. **Différences** : organismes entraînés
  et 70 milliards ; P3 est sur consigne et 8 milliards.

### 2.8 [WK] Wilhelm, Wittkopp, Kao — « Monitoring Emergent Reward Hacking During Generation via Internal Activations » — arXiv 2603.04069v1 (4 mars 2026 ; atelier ICLR 2026, p. 1)

- **Montage**
  - Qwen2.5-Instruct 7B, **LLaMa 3.1-8B**, Falcon3-7B (p. 5) ; adaptateurs LoRA (GRPO, rang 32) entraînés sur School of
    Reward Hacks à 0 %, 5, 10, 50, 90 et 100 % d'exemples de triche (p. 5, p. 13).
  - Moniteur : un autoencodeur par couche (8 000 dimensions), standardisation, ACP, régression logistique ; quatre
    dernières couches (p. 4, p. 13). Entraîné sur des activations **du modèle lui-même** : « trained only on activations
    from the benign control adapter and the fully reward-hacking adapter » (p. 5).
  - Agrégation : **moyenne** des probabilités par jeton sur l'empan (réponse, ou raisonnement), puis moyenne sur les
    couches, seuil 0,5 (équations 2-4, p. 4-5).
  - Vérité : GPT-4o juge les réponses (p. 5). Aucun plancher, aucune aire ; F1.
- **Résultats**
  - p. 5, table 1, F1 (réponse directe) : Llama témoin 1,000 ; 5 % 0,760 ; 10 % 0,837 ; 50 % 0,946 ; 90 % 0,941 ;
    triche 0,961. Falcon triche 0,903 ; Qwen triche 0,784.
  - p. 6 : sur Llama, le signal monte tôt dans le raisonnement puis décroît.
- **Ce qui fait marcher ou échouer** : entraînement sur l'organisme lui-même. **Réserve (R4)** : le classifieur sépare
  deux adaptateurs aux poids différents ; il peut lire l'empreinte de l'adaptateur plutôt que la conduite ; F1 de 1,000
  sur le témoin, sans plancher : trop propre pour être opposable.
- **Transposable à P3** : même modèle (Llama 3.1 8B). Montre qu'une moyenne sur les jetons et sur les couches est la
  pratique de ce genre de moniteur ; chez nous, seulement en bras de diagnostic (N-026). L'organisme de P3 est sur
  consigne, sans adaptateur : pas de confusion d'empreinte, mais l'analogue est la lecture de la présence de la consigne,
  que le témoin instruit contrôle. Preuve faible : atelier, pas de plancher.

## 3. Agrégation, vérifiée page par page

| travail | jetons lus | agrégation | ce que le papier dit des autres agrégations | page |
|---|---|---|---|---|
| [AP] 2502.03407 (Apollo) | entraînement : jetons du fait sauf les cinq derniers (p. 4) ; test : « all tokens in the model's response » (p. 22) | **moyenne** des scores par jeton : « We then take the mean across tokens to get a single deceptiveness-score for each model response. » (p. 3) | annexe D.4 : maximum et moyenne de ReLU(x − t) essayés ; « taking the mean is best on all datasets for the probe trained on Instructed-Pairs (Figure 14a). In contrast, ReLU does improve performance for the Roleplaying probe on several datasets (Figure 14b). … very probe and dataset dependent. » (p. 22) ; échecs d'agrégation quand la réponse n'est trompeuse qu'en partie (p. 8) ; dernier jeton seul « comparable » (D.5, p. 23) | 3, 4, 8, 22, 23 |
| [K] | toutes les positions, entrée et réponse | moyenne des activations, puis régression (linéaire) ; softmax (attention) | attention > linéaire (0,946 contre 0,903) | 2, 6-7 |
| [LB] | réponse de l'assistant, sans message système | moyenne (sonde « moyenne ») ; un jeton (sonde de suivi) | moyenne et suivi « comparables » (p. 8) | 7, 8 |
| [AU] | entraînement : dix derniers jetons | test : **non écrite** | moyenne glissante montrée sur un exemple | 7, 17 |
| [DYL] | Apollo : jetons non-raisonnement de l'assistant ; DYL : jeton de réponse | Apollo : moyenne ; DYL : un jeton | calibration par jetons mis en commun = erreur (annexe E) | 8, 21-22 |
| [RH] | chaque position du déroulé | seuil par jeton (équivaut à un maximum) | « several poolings » essayés à l'entraînement, sans détail | 6, 7 |
| [CC] | tous les jetons de l'échange, toutes les couches | maximum, dans le temps, d'une moyenne mobile exponentielle (entraînement : fenêtre de 16) | sans lissage, un pic isolé signale toute la séquence | 6-7 |
| [WK] | réponse ou raisonnement | moyenne sur les jetons, puis sur les couches | — | 4-5 |
| [AB] | positions de 50 consignes génériques | aucune (caractéristiques par position) | — | 5-6 |

**Pour N-026.** Apollo, source de la recette de tromperie de P3, agrège par la moyenne et trouve la moyenne **meilleure
que le maximum sur tous ses jeux** pour la sonde entraînée sur ces paires (Llama-3.3-70B, régression logistique,
couche 22 ; p. 22). P3 a pris la même recette avec le maximum, une autre famille (différence de moyennes) et un modèle
dix fois plus petit. C'est un argument pour le bras de diagnostic « moyenne » de N-026, comparé au plancher de même
agrégation ; ce n'est pas une preuve qu'il détectera : dans P3 la triche tient dans un champ, et la moyenne peut la
diluer (N-026, § 2). Note : la phrase « Apollo ne lit pas la chaîne de raisonnement sur Insider Trading » vient de
[LB] p. 69 ; non revérifiée sur [AP] dans cette lecture.

## 4. Ce qui fait marcher ou échouer — synthèse, chaque point sur PDF

1. **Le domaine des données d'entraînement** : hors domaine, la tromperie perd 0,416 d'aire ([K] p. 7) ; mieux vaut des
   données du même domaine écrites ailleurs que des données du modèle hors domaine ([K] p. 5). Les succès agentiques
   apprennent sur des paires synthétiques du domaine visé ([RH] p. 7, p. 10).
2. **Le choix de la sonde** se fait sur la distribution visée chez [RH] (p. 9) ; chez P3 il s'est fait sur une validation
   générique saturée (neuf sondes à 1,0, [V] l. 119-122), donc sans pouvoir de choix.
3. **La taille du modèle** : les détecteurs croissent avec la capacité ([DYL] p. 10) ; la recette générique ne marche
   bien que sur Llama 70B parmi quatre modèles ([LB] p. 54) ; petits modèles 0,64 à 0,77 ([DYL] p. 28).
4. **La verbalisation** : avec la pensée ou la parole, 0,948 à 1,000 ; action seule hors parole 0,653 ([AU] p. 6).
5. **La couche** : une couche de plus ou de moins change le rappel de 0,10 à 1,00 ([LB] p. 69) ; toutes les couches
   valent mieux ([CC] p. 8).
6. **Le pic isolé** : un maximum brut se fait prendre par un jeton ([CC] p. 6) ; Apollo trouve le maximum moins bon que
   la moyenne pour sa sonde de paires ([AP] p. 22).
7. **La calibration** : un seuil fixé sur un témoin générique donne 38 % de faux positifs réels en moyenne ([LB] p. 55) ;
   une erreur de calibration fait passer 96 % à 73,2 % ([DYL] p. 21-22).
8. **Mensonge sur consigne ou entraîné** : sur consigne, cas facile ; entraîné, Apollo tombe à 0,52 ([DYL] p. 11).

## 5. Transposable à P3 — leviers, dans l'ordre où je les testerais

Ce sont des pistes pour Lazar. Chacune demande un préenregistrement scellé (R1), contre-lu (R2), avant toute lecture ;
toute dépense de calcul passe par un devis et un GO. Je ne décide rien.

1. **Données du même domaine, en paires minimales** ([K] p. 5, p. 7 ; [RH] p. 7). Actions au format de P3 sur les 32
   tâches de réserve, version honnête et version au coût gonflé, écrites hors des épisodes évalués. **Garde** : une telle
   sonde peut apprendre « gros nombre » (comportement lisible au texte) ; T4 (à coût déclaré égal) et le prédicteur
   « coût seul » (0,8878) sont les témoins qui le diront.
2. **Choisir la sonde sur un petit jeu de la distribution visée, hors des épisodes évalués** ([RH] p. 9 ; [K] p. 8-9 :
   jeu substitut **incité**, corrélation 0,793). Par exemple : un autre organisme (famille (ii)) ou une incitation
   (intérêt à gonfler, sans consigne). Remplace une validation générique saturée.
3. **Sonde de suivi « did you lie? »** ([DYL] p. 8-11 ; [LB] p. 8, p. 55). Question posée sur une copie du contexte
   après chaque action ; entraînement sur des mensonges génériques (anti-circularité gardée). Attendu modeste sur 8
   milliards ([DYL] p. 28 : Qwen3-8B 0,69). Lecture d'un seul jeton : sa place au regard de la règle d'agrégation est à
   qualifier par Lazar.
4. **Plusieurs couches concaténées** (7, 15, 23) ([CC] p. 8 ; [LB] p. 69 ; [DYL] p. 11). Compatible avec le maximum.
5. **Bras de diagnostic « moyenne »** de N-026 ([AP] p. 22) : même plancher, même agrégation, jamais moniteur.
6. **Maximum d'un score lissé** ([CC] p. 6-7) : en diagnostic d'abord ; en production, question pour Lazar.
7. **Mesurer l'apport au-dessus du coût seul** ([RH] p. 9 ; [CC] p. 8-9) : la boîte blanche ne vaut que par ce qu'elle
   ajoute au moniteur boîte noire.
8. **Modèle plus grand** ([DYL] p. 10 ; [LB] p. 54) : effet le mieux établi, mais changer de modèle demande un GO.
9. **Autoencodeurs** : audit exploratoire seulement ([AB] p. 6-7 ; [AU] p. 8) ; résultats positifs sur Llama 3.1 8B
   ([WK] p. 5) trop fragiles pour fonder quoi que ce soit (réserve R4, section 2.8).

## 6. Questions (R8 : absences, pas preuves)

- Aucun des huit n'utilise un **plancher de directions aléatoires appariées en covariance**. Ils comparent au hasard
  (0,5), à un moniteur, ou à un seuil fixé sur un témoin bénin. Question : avec une aire de 0,5748, la sonde de
  tromperie de P3 serait « au-dessus du hasard » chez eux ; le plancher de P3 (quantile 0,5717) est-il plus strict
  qu'eux, et de combien ? Aucun d'eux ne mesure ce que vaut, au maximum sur 400 jetons, une direction aléatoire.
- Aucun ne sonde un **mensonge sur un nombre** dans une proposition d'agent. Les plus proches : rapports falsifiés
  ([RH], famille « Reporting », p. 27) ; Insider Trading ([LB], [K]).
- Aucun ne compare **maximum et moyenne au même plancher**.
- Aucun ne teste un témoin du type « consigne privée bénigne de même longueur » (le témoin instruit de P3).

## 7. Pistes vues en ligne, non téléchargées : **non vérifiées**, aucune ne sert de preuve

- 2509.20393, « The Secret Agenda: LLMs Strategically Lie and Our Current Safety Tools Are Blind » (DeLeeuw et al.,
  septembre 2025) : d'après le résumé arXiv, des caractéristiques d'autoencodeur étiquetées « deception » s'activent
  rarement pendant le mensonge stratégique, sur Llama 8B/70B et GemmaScope. **Non vérifié.**
- 2605.12726, « Before the Last Token: Diagnosing Final-Token Safety Probe Failures » (Doda, mai 2026) : d'après le
  résumé, le maximum naïf sur les positions surréagit sur des consignes sûres. **Non vérifié.**
- 2602.08877, « Stress-Testing Alignment Audits With Prompt-Level Strategic Deception » (Daniels et al., février 2026) :
  d'après le résumé, des consignes système trompent les audits par autoencodeur et boîte noire. **Non vérifié.**
- Billet LessWrong (non arXiv) : sonde de code piégé, 63 sur 73 à 1,4 % de faux positifs. **Non vérifié.**
- Déjà dans le dépôt (hors de ma famille) : 2610.12445 (FAR.AI, « Caught in the Act », FIBS), 2509.21344, 2512.07810,
  2507.12691, 2602.15515, 2506.10805, 2601.11516.

## 8. Limites de cette lecture

- Huit PDF au plus : d'autres travaux récents existent sûrement ; la recherche web ne couvre pas tout.
- Texte extrait automatiquement : quelques formules et figures sont mal rendues ; les valeurs lues seulement sur une
  figure ne sont pas citées.
- Pages lues : corps de chaque papier et annexes utiles (listées à chaque chiffre) ; pas toutes les annexes.
- Je n'ai relancé aucun code ; les chiffres sont ceux des auteurs.
- Les comparaisons à P3 reposent sur [P] et [V] seulement ; je n'ai lu aucune donnée de P3.
