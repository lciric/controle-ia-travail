# Lecture adverse de O4 (juge au nul des lois connues) : SSRN 6569258, pistes de priorité haute et tests d'englobement — v1

- **Lecteur** : sous-agent neuf (Claude Opus 5.5), qui n'a écrit ni N-064 ni aucun brouillon de N-067 ni aucun rapport de l'état de l'art. Mandat : R-2571, point 4 (a) (« lire SSRN 6569258 et les pistes de priorité haute sur PDF avant tout texte qui déclare O4 libre hors du dépôt »), N-067 retenue, section 4, point 2, et section 8.
- **Fenêtre de travail** : 2026-11-13, 19:24 à 19:48 UTC (`date -u`). Aucune écriture git ; aucune dépense ; aucun envoi de nos énoncés à un tiers (les requêtes ne portent que des mots-clés génériques, recopiées sous `docs/sources/pdf/lecture-o4-v1/recherches/`) ; la clé de Semantic Scholar n'a été lue que par son nom.
- **Règle de lecture (R8).** « Libre » = « non trouvé dans les pièces lues », jamais « trou du champ ». Une page citée renvoie à la page du PDF (le numéro imprimé est donné entre parenthèses quand il diffère). Les 53 citations ci-dessous ont été recopiées puis **vérifiées par programme** sur le texte extrait par `pdftotext` : 53 sur 53 trouvées sur la page indiquée (`docs/sources/pdf/lecture-o4-v1/verification-citations/resultat-verification-citations-o4-v1.json`, script `verifier_citations_o4_v1.py`, liste `citations-o4-v1.json`, tous scellés).

## 0. Verdict

**O4 : occupée en partie** — et la partie occupée est le principe. Ce qui reste non trouvé dans les pièces lues n'est plus une idée mais une **réunion de pièces publiées chacune ailleurs**.

1. **Le principe « une découverte se juge contre ce qui est déjà connu, non contre aucun effet » est publié**, y compris pour une archive qui grandit au fil des découvertes :
   - dans la recherche humaine en finance, comme test de toute proposition nouvelle contre l'ensemble des facteurs déjà proposés, rejoué récursivement dans l'ordre d'apparition (Feng, Giglio, Xiu, NBER 25481, 2019, p. 2-4 du PDF) ;
   - **pour des hypothèses proposées par un modèle de langue** : jugées contre 209 anomalies publiées et contre les modèles de facteurs, après la boucle de découverte (Liu, Liu, Liu, Mei, SSRN 6569258, avril 2026, p. 1, 4, 26, 28) ; jugées **dans la boucle**, par une porte déterministe hors du modèle, contre un panel de référence **plus la bibliothèque des facteurs déjà admis**, qui s'accroît à chaque admission (Pan, Ding, Giesecke, « SEADS », arXiv 2609.00731, 1er septembre 2026, p. 6, 7, 16, 25).
2. **La forme statistique est publiée aussi** : un e-processus (preuve accumulée, valide à tout instant d'arrêt) qui oppose une loi prédictive **engagée avant l'observation** à la **meilleure loi ajustée de la théorie en vigueur**, et ne révise la théorie que si celle-ci est rejetée ; la théorie révisée devient le nul de l'étape suivante (Ma et al., « Learning to Outgrow a Theory », arXiv 2610.07627, conférence ICLR 2027, p. 1, 4, 15). Le proposeur y est une politique apprise, **pas un modèle de langue** (les systèmes à modèle de langue y sont des bases de comparaison, p. 6). L'outil générique — e-valeurs pour savoir si un prévisionniste nouveau bat un prévisionniste établi — est publié depuis 2021 (Choe et Ramdas, arXiv 2110.00115, p. 1, 38 ; Henzi et Ziegel, arXiv 2103.08402, p. 1, 4).
3. **SSRN 6569258 n'occupe pas O4 en entier** : son nul des lois connues est appliqué **après** la boucle, sur l'échantillon même de la recherche, avec des statistiques de Student à taille fixée ; dans la boucle, le crible rendu au modèle est « coefficient de Fama et MacBeth significatif dans le sens prédit », c'est-à-dire un nul « aucun effet » (p. 14, 22, 36). Il occupe le **principe** pour des hypothèses de modèle de langue (p. 1, 4, 28).
4. **SEADS (2609.00731) est la pièce la plus proche** : juge déterministe dans la boucle, contrôles = archive (référence + admis), seuils fixés avant toute course (p. 6). Il lui manque, dans le texte lu : la validité à tout instant d'arrêt (statistiques de Student, seuils 1,0 et correction de Bonferroni), des prédictions scellées avant que les données existent (fenêtre d'échantillon 2010-2019, p. 8), des lois prédictives comparées par vraisemblance (ce sont des scores de rang).
5. **Non trouvé dans les pièces lues** : la conjonction (i) proposeurs modèles de langue, (ii) nul formé d'une **mise en commun ajustée des lois prédictives de l'archive** (lois connues et survivantes promues par l'organisme lui-même), (iii) e-processus comme règle de promotion, (iv) prédictions scellées avant que les données existent, statistique calculée hors des agents. (i) et (ii, sous forme de régression) sont chez SEADS ; (iii) et une partie de (iv) (engagement avant observation, classe fixée à l'entrée de l'étape) chez Ma et al. ; le scellement par empreinte chez CONFIRM et « Hard to Fool » (déjà cités par N-067, section 3).

**Conséquence proposée (nœud : modification de revendication, à Lazar)** : O4 ne peut pas être déclarée libre hors du dépôt ; elle se dit, comme l'énoncé retenu de O2 dans N-067 (section 4, point 1), **comme un assemblage dont les pièces sont empruntées**, avec citations. La ligne publique actuelle (« battre un nul des lois connues […] « rien au-delà de l'archive » ») est, dans sa lettre, occupée dans son principe par SEADS et par Liu et al. Phrase proposée en section 4.

## 1. Énoncé lu

- **O4**, table des revendications (`docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md`, `08a3738a…`, l. 260) : « Nouveauté statistique : battre un nul des lois connues (nul informé, nul poolé v8, nul v9 par morceaux), « rien au-delà de l'archive » ».
- **N-064** (`docs/decisions/decision-N-064-v1.md`, `387c9d4e…`, point 2) : nul « formé des lois connues (l'archive) », l'une des quatre composantes de l'énoncé retenu de O2.
- **N-067, brouillon 2** (`decision-N-067-v1-brouillon2.md`, `cb3f3719…`) et **N-067 retenue** (`decision-N-067-v1.md`, `966dd9dc…`), section 4, points 1 et 2 : « Juge statistique dont le nul est formé des lois déjà connues (l'archive) : une fiche n'est promue que si sa prédiction scellée bat ce que l'archive prédit déjà » ; O4 « désormais seul porteur de la revendication du juge » ; clause d'usage public (R-2571, point 4 (a)).
- **Mise en œuvre** (pour juger la forme, non pour revendiquer) : conception v7, § 2 (`docs/notes/ideation-organisme-v1/orchestrateur-v51/conception-v7-v1.md`, `31fc8c4b…`) — un membre « connu » de la bibliothèque du juge, loi ajustée avant le gel ; LISEZMOI v7-v6 (`8d96bf9f…`) — « nul d'archive ajusté » : mise en commun linéaire ajustée des lois connues (parents et survivantes).

## 2. Table des pièces

Toutes sous `docs/sources/pdf/lecture-o4-v1/`, un dossier par source, chaque PDF scellé (compagnon `.sha256`) avec un `provenance-v1.md` (adresse, heure UTC, réponse, empreinte). Statut : vis-à-vis de O4.

| clé | pièce | dossier | empreinte | lu | statut vis-à-vis de O4 | pages décisives |
|---|---|---|---|---|---|---|
| LIU | Liu, Liu, Liu, Mei, « Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing », SSRN 6569258, avril 2026 (copie déposée par l'hôte d'une conférence, voir section 5) | `ssrn-6569258/` | `2d4e1d61d248699a…` | en entier (71 p.) | **occupe en partie** : principe pour des hypothèses de modèle de langue, hors boucle | 1, 4, 8, 14, 18, 22, 26, 28, 36 |
| SEADS | Pan, Ding, Giesecke, « Agentic Empirical Asset Pricing: Methodological Foundations », arXiv 2609.00731 v1 | `arxiv-2609.00731/` | `ba2c3b8a34ea0cc9…` | en entier (26 p.) | **occupe en partie, la plus large** : juge déterministe dans la boucle contre référence + archive des admis | 3, 6, 7, 8, 16, 23, 25 |
| OUTGROW | Ma et al., « Learning to Outgrow a Theory », arXiv 2610.07627 v1 (ICLR 2027) | `arxiv-2610.07627/` | `a3041d9a9a7613c7…` | p. 1-12, 14-16, 19-21 ; reste par recherche de termes | **occupe en partie** : forme statistique (e-processus contre la meilleure loi ajustée de la théorie en vigueur), proposeur non langagier | 1, 4, 5, 6, 15 |
| FGX | Feng, Giglio, Xiu, « Taming the Factor Zoo: A Test of New Factors », NBER 25481, 2019 | `feng-giglio-xiu-nber-w25481/` | `ad1bc396f827cad8…` | p. 1-4 (résumé, introduction) | **occupe le principe** dans la recherche humaine (test contre tous les facteurs existants, récursif) | 2, 3 (2), 4 (3) |
| HLZ | Harvey, Liu, Zhu, « . . . and the Cross-Section of Expected Returns », NBER 20592 (version de travail de l'article de 2016) | `harvey-liu-zhu-2016/` | `15387ff6505c7eaf…` | p. 1-2, 36-37, 100 ; reste par recherche de termes | **voisine** : multiplicité ; décrit la pratique « tenir face aux facteurs déjà proposés » | 2, 36 (34), 100 (98) |
| CR | Choe, Ramdas, « Comparing Sequential Forecasters », arXiv 2110.00115 v6 | `arxiv-2110.00115/` | `fd87e23a30c6657f…` | p. 1-8, 26-28, 38 ; preuves et annexes par termes | **voisine (outil)** : e-processus « le nouveau prévisionniste ne fait pas mieux que la référence » | 1, 38 |
| HZ | Henzi, Ziegel, arXiv 2103.08402 v3 | `arxiv-2103.08402/` | `2e259a65ddca593a…` | p. 1-5 ; reste par termes | **voisine (outil)** : e-valeurs de dominance d'un nouveau prévisionniste sur un étalon établi | 1, 4 |
| BEYOND | Huang, Fan, « Beyond Prompting », arXiv 2603.14288 v2 (mars 2026) | `arxiv-2603.14288/` | `8fe2b21770af074a…` | par passages (p. 13, 34-35) | **voisine, principe affirmé** (apport marginal sur le modèle à cinq facteurs) ; mécanisme non établi dans les passages lus | 34, 35 |
| HYPFACT | Huang, Fan, Hu, Ye, « From Hypotheses to Factors », arXiv 2604.26747 v1 | `arxiv-2604.26747/` | `c9971afa0d4d5d4b…` | p. 1-5 | **voisine** : porte déterministe contre « aucun effet » ; redondance jugée par l'agent | 5 |
| REDONDANCE | Xia, Wang, « Discovery under Hypothesis Redundancy », arXiv 2606.14386 v1 | `arxiv-2606.14386/` | `619d1ea507f18d37…` | p. 1-4 ; reste par termes | **voisine** : mesure de « nouveauté prédictive » au-delà de l'archive pour des propositions de modèle de langue, sans test | 1, 4 |
| CREDIT | Ning, Li, Kong, Li, « Predictive Credit », arXiv 2610.00314 v1 | `arxiv-2610.00314/` | `f7771ea50ac7e831…` | p. 1-5 | **voisine lointaine** : gain prédictif d'une explication d'agent sur une description de base | 2 |
| MARTIN | Martin, « Regularized e-processes », arXiv 2410.01427 v4 | `arxiv-2410.01427/` | `e8ec2729a632e451…` | p. 1-6, § 3.5 ; reste par termes | **ne la touche pas** : savoir préalable sur un paramètre, qui régularise l'e-processus ; pas un nul formé de lois connues | 1, 2 |
| CLERICO | Clerico, arXiv 2606.06769 v2 | `arxiv-2606.06769/` | `dbd72f13e947aa0f…` | p. 1-5, discussion (p. 15-17) ; preuves non lues | **ne la touche pas** (théorie des e-processus sous contraintes de moyenne conditionnelle) | 1 |
| ALPHASCHEMA | Yi et al., « AlphaSchema », arXiv 2607.26642 v1 | `arxiv-2607.26642/` | `85f0d13a673969c6…` | p. 1-13 ; p. 14-18 par termes | **ne la touche pas** : récompense par coefficient d'information, filtre de corrélation du lot final | 3, 9 |
| PHANTOM | Xu, Yan, Chen, Kechadi, « Phantom Gains », arXiv 2608.20290 v1 | `arxiv-2608.20290/` | `1ca00a66e541929c…` | p. 1-9, 39-40 ; reste par termes | **ne la touche pas** : nul mesuré sur un modèle gelé (auto-amélioration), pas des lois connues | 1, 4 |

Trois PDF lus ici sont identiques octet pour octet aux copies du lot 10 de la branche `prep/etat-de-l-art-niveau3-pieces-v1` (2609.00731, 2110.00115, 2103.08402), deux à celles du lot 4 (2610.07627, 2610.00314) : même empreinte, vérifiée.

## 3. Lecture pièce par pièce (citations recopiées, vérifiées par programme)

### 3.1 LIU — SSRN 6569258 (pièce nommée par R-2571)

- Objet : un modèle de langue (Claude Opus 4.6, p. 15, 22) propose des signaux comptables dans une grammaire fermée ; une chaîne d'évaluation fixe les teste ; 280 propositions, 7 générations.
- Le principe de O4, pour des hypothèses de modèle de langue :
  - [LIU p. 1] « novelty tests against 209 published anomalies »
  - [LIU p. 1] « 38 survive multivariate horse races designed to isolate signals with independent predictive content »
  - [LIU p. 28] « For each survivor, we compute its average cross-sectional Spearman rank correlation with each published anomaly, select the 10 closest neighbors, and estimate a multivariate Fama–MacBeth regression that includes the new signal together with those controls. »
  - [LIU p. 28] « Of the 34 survivors with stable conditional estimates, 9 retain significance at » (|t| > 1,96)
  - [LIU p. 26] « many are absorbed by known factor structures or closely related published signals »
  - [LIU p. 18] « our goal is to isolate signals with incremental predictive content rather than count every successful variant as a separate discovery » (course entre les propres découvertes du système : une archive interne, élaguée par élimination descendante)
  - Revendication de priorité des auteurs : [LIU p. 4] « To our knowledge, this is the first study to combine LLM-guided signal discovery with the full battery of modern multiple testing corrections, multi-model factor spanning, cross-anomaly novelty tests »
- Ce qui n'y est pas (pourquoi « en partie ») :
  - dans la boucle, le nul est « aucun effet » : [LIU p. 14] « For purposes of the discovery loop, a proposal is classified as successful if its Fama–MacBeth » (|t| > 1,96 dans le sens prédit) ;
  - le nul des lois connues n'entre pas dans la boucle : [LIU p. 36] « it lacks direct access to factor model results during the discovery loop » ;
  - pas de validation hors échantillon, pas de données postérieures à l'engagement : [LIU p. 22] « We do not claim out-of-sample validation from the discovery loop itself. » ; les données sont 1963-2024, déjà existantes ;
  - statistiques de Student à taille fixée, corrections de Bonferroni, Holm, Benjamini-Hochberg-Yekutieli (p. 27, 49), pas d'e-valeurs ;
  - séparation déjà là, à citer pour O1 : [LIU p. 22] « Importantly, the AI research agent has no direct access to the raw CRSP/Compustat panel and does not alter the empirical protocol. » ; sens prédit posé avant le résultat : [LIU p. 8] « proposes a hypothesis before the empirical result is known for that proposal ».

### 3.2 SEADS — Pan, Ding, Giesecke, arXiv 2609.00731 (la pièce la plus proche)

- Un planificateur et un proposeur modèles de langue (GPT-5.2, p. 24) ; une porte de validation déterministe, hors du modèle :
  - [SEADS p. 16] « The gate is deterministic throughout; admission is the logical AND of every configured check »
  - [SEADS p. 3] « keeping them separate makes B4’s verdict evidence, not the generator’s own opinion of itself »
- Le nul formé des lois connues **dans la boucle**, archive comprise :
  - [SEADS p. 6] « A final robustness trio closes the gate—novelty against the reference set Z (§3.1), partial-IC against the top-K most-correlated controls »
  - [SEADS p. 25] « The candidate is residualized each month on its top-5 most-correlated admitted-library columns via per-month OLS » (résidu par moindres carrés sur les cinq colonnes les plus corrélées de la bibliothèque admise, puis coefficient d'information de rang du résidu)
  - [SEADS p. 25] « Novelty gates on mean-monthly Spearman < 0.7 against a designated reference panel plus the admitted library. »
  - [SEADS p. 7] « novelty reference set updates to include newly admitted factors » (l'archive grandit)
  - [SEADS p. 23] « incremental value to a portfolio that already holds the full raw characteristic panel, which is exactly what the novelty gate (§3.3.3) exists to protect »
  - seuils : [SEADS p. 25] « novelty < 0.7, partial-IC t ≥ 1.0, and Fama–MacBeth t ≥ 1.0 » ; fixés d'avance : [SEADS p. 6] « fixed before any experimental run and never adjusted afterward »
- Ce qui n'y est pas : e-valeurs ou validité à tout instant d'arrêt (statistiques de Student ; Bonferroni « dynamique » sur le seul coefficient d'information, p. 24) ; prédictions scellées avant que les données existent ([SEADS p. 8] « Both use an in-sample window of 2010–2019 », données historiques) ; comparaison de **lois prédictives** (ce sont des scores de rang, non des lois) ; le contrôle est la projection linéaire sur cinq voisins, non une mise en commun ajustée de toutes les lois de l'archive. Code annoncé « upon acceptance » (p. 24) : non lu.

### 3.3 OUTGROW — Ma et al., arXiv 2610.07627 (lot 4, non lu jusqu'ici)

- La forme statistique de O4, avec un nul « théorie en vigueur » ajusté :
  - [OUTGROW p. 1] « anytime-valid sequential evidence that triggers structural revision only after the current class is rejected »
  - [OUTGROW p. 4] « Revision is determined by observations rather than the proposal score. » ; la statistique (éq. 6) est le rapport du produit des densités prédictives de la modification proposée au **supremum** sur les paramètres de la classe en vigueur : [OUTGROW p. 4] « The denominator fits one shared parameter vector over the stage. » ; budget d'erreur par étape α/[j(j+1)] (p. 4, 14).
  - engagement avant observation : [OUTGROW p. 15] « the class tested during a stage is fixed at stage entry and each predictive density is committed before observing the next outcome »
  - le proposeur ne tient pas la règle : [OUTGROW p. 15] « but it cannot retroactively redefine the evidence used to reject the current class »
- Ce qui n'y est pas : le proposeur est une politique apprise par imitation puis optimisation ([OUTGROW p. 5] « Training tasks provide a known generative mechanism and an initial class that may omit it. ») ; les systèmes à modèle de langue sont des bases ([OUTGROW p. 6] « Baselines include space filling, candidate disagreement, residual-triggered revision, an expanded fixed operator library, LLM-ACES (Abhyankar et al., 2026), LLM-AutoSciLab (Kabra et al., 2026) ») ; le nul est **une** classe paramétrique (la théorie en vigueur, révisions acceptées comprises), non un mélange de lois indépendantes ; pas de scellement par empreinte ; systèmes dynamiques simulés, non des hypothèses libres.

### 3.4 FGX et HLZ — le principe dans la recherche humaine

- [FGX p. 2] « We propose a model-selection method to systematically evaluate the contribution to asset pricing of any new factor, above and beyond what a high-dimensional set of existing factors explains. »
- [FGX p. 3 (2)] « Our methodology can be thought of as a conservative test for new factors, which benchmarks them against a large-dimensional set of existing ones. »
- [FGX p. 4 (3)] « we propose a recursive exercise in which factors are tested as they are introduced against previously proposed factors » (l'archive qui grandit, dans l'ordre historique)
- [HLZ p. 100 (98)] « newly proposed factors often need to “stand their ground” against similar factors (not just Fama-French three factors and Momentum) that are previously proposed »
- [HLZ p. 36 (34)] « The other route is to incrementally increase the factor list by thoroughly evaluating the economic contribution of a risk » (factor ; renvoi à Harvey et Liu 2014d, non lu)
- [HLZ p. 2] « a newly discovered factor needs to clear a much higher hurdle, with a t-ratio greater than 3.0 »
- Statut : le principe de O4 est une pratique établie de la finance empirique ; aucune de ces deux pièces ne juge des propositions d'un système automatique.

### 3.5 CR et HZ — l'outil statistique

- [CR p. 1] « e-processes and p-processes for sequentially testing a weak null hypothesis — whether one forecaster outperforms another on average »
- [CR p. 38] « we are often interested in comparing a newly developed forecasting algorithm (say, p) with an existing baseline (say, q) »
- [HZ p. 1] « we construct e-values for testing the statistical significance of score differences of competing forecasts in sequential settings »
- [HZ p. 4] « Tests for these hypotheses are therefore most suitable for the comparison of a new method to an established benchmark »
- Statut : si la « référence » est la loi de l'archive, la règle de promotion de O4 est un cas de ces tests ; ni l'une ni l'autre ne parle de découverte ni de mise en commun de lois connues.

### 3.6 Voisines et pièces qui ne touchent pas O4

- **BEYOND** (mars 2026, avant LIU) : [BEYOND p. 34] « ensuring that new factors provide incremental explanatory power relative to established benchmarks » ; [BEYOND p. 35] « the agent ensures that new factors provide significant marginal information over existing benchmarks » (modèle à cinq facteurs de Fama et French). La règle de promotion lue (algorithme, p. 13) est un seuil sur la statistique de Student du coefficient d'information et sur le ratio de Sharpe ; le contrôle d'apport marginal semble tenu par l'agent (« the agent ensures »), non par un juge. Lue par passages : **à lire en entier** avant tout texte public (section 5).
- **HYPFACT** : [HYPFACT p. 5] « The gate is applied only to the training-period mean IC and IC t-statistic. » ; [HYPFACT p. 5] « The agent then curates a smaller good pool based on empirical strength, mechanism diversity, and redundancy with existing factors. » Nul « aucun effet » dans la porte.
- **REDONDANCE** : [REDONDANCE p. 1] « Scientific discovery saturates when new hypotheses cease to provide independent information » ; [REDONDANCE p. 4] « The predictive novelty is the empirical estimator of residual signal » (coefficient d'information du résidu après projection sur l'archive) : la **mesure** de « ce qu'une proposition prédit au-delà de l'archive », pour des propositions de modèle de langue (facteurs d'actions chinoises), sans test ni règle de promotion.
- **CREDIT** : [CREDIT p. 2] « We connect these traditions by measuring predictive credit, the gain in forecasting executed outcomes from assigning an agent’s explanation context. » Gain d'une explication sur une base descriptive ; voisin lointain.
- **MARTIN** (désigné par le lot 4-A, § 8, comme « la piste la plus sérieuse contre O4 ») : [MARTIN p. 1] « This paper proposes a regularized e-process framework featuring a knowledge-based, imprecise-probabilistic regularization with improved efficiency. » ; [MARTIN p. 2] « This paper considers the situation in which the investigator knows something about » (le paramètre). Le savoir préalable porte sur un paramètre et sert l'efficacité ; ce n'est pas un nul « ne fait pas mieux que les lois connues ». **Ne touche pas O4.**
- **CLERICO** : [CLERICO p. 1] « We characterise e-processes for testing non-parametric hypotheses that require the conditional mean of a finite-dimensional statistic to lie in a prescribed convex set. » Théorie ; ne touche pas O4.
- **ALPHASCHEMA** : [ALPHASCHEMA p. 3] « Selected plans are implemented as executable factors, validated, and backtested. » ; [ALPHASCHEMA p. 9] « This rule prioritizes high-reward factors while controlling redundancy in the exported pool. » Pas de nul des lois connues.
- **PHANTOM** : [PHANTOM p. 1] « We replace it with a per-problem exact test against a pooled baseline under false-discovery-rate control » ; [PHANTOM p. 4] « We measure how many by re-evaluating a frozen model at every checkpoint and computing every statistic exactly as for a trained one ». Le « nul mesuré » est un modèle gelé, non des lois connues ; ne touche pas O4 (voisin de vocabulaire seulement : « baseline pooled »).

### 3.7 Recherche de l'étape 2 (interfaces d'arXiv et de Semantic Scholar)

- 37 requêtes à arXiv (3 lots : 16, 16, 5) et 8 à Semantic Scholar, mots-clés génériques (« encompassing test », « spanning test », « factor zoo », « incremental validity », « nested model », « known factors », « published anomalies », « anytime-valid » croisés avec « language model », « LLM », « agent », « discovery ») ; requêtes et réponses brutes sous `docs/sources/pdf/lecture-o4-v1/recherches/` (scellées).
- Les combinaisons strictes « encompassing / spanning / factor zoo / incremental validity » × « modèle de langue » rendent **zéro** résultat sur arXiv ; ce silence ne prouve rien (R8) : SEADS et LIU emploient « novelty », « reference set », « horse race », « factor spanning » sans le mot « encompassing ». Les pièces retenues par la recherche : 2606.14386 (REDONDANCE), NBER 25481 (FGX), et, par les bibliographies, 2603.14288 et 2604.26747. Le reste des réponses est hors sujet (titres relevés dans les fichiers de réponses).

## 4. Phrase publiable sur O4 (pas plus forte que les pièces)

Référence (français) :

> « Notre juge ne promeut une hypothèse que si sa prédiction, scellée avant que les données existent, bat par un e-processus calculé hors des agents la meilleure combinaison ajustée des lois déjà connues, archive de l'organisme comprise. Juger une découverte contre ce qui est déjà connu plutôt que contre l'absence d'effet est une pratique établie (Feng, Giglio et Xiu, 2019), déjà appliquée à des hypothèses proposées par des modèles de langue (Liu, Liu, Liu et Mei, 2026, SSRN 6569258 ; Pan, Ding et Giesecke, 2026, arXiv 2609.00731), et la règle d'un e-processus contre la meilleure loi ajustée de la théorie en vigueur est publiée pour un proposeur appris (Ma et al., 2026, arXiv 2610.07627) ; nous n'avons pas trouvé, dans les travaux lus, cette réunion pour des hypothèses rédigées par des modèles de langue, ce qui ne vaut pas pour l'ensemble du champ. »

Rendu anglais fidèle, si le texte sortant est en anglais :

> "Our judge promotes a hypothesis only if its prediction, sealed before the data exist, beats — through an e-process computed outside the agents — the best fitted combination of the already known laws, including the organism's own archive. Judging a discovery against what is already known rather than against no effect is established practice (Feng, Giglio and Xiu, 2019), already applied to hypotheses proposed by language models (Liu, Liu, Liu and Mei, 2026, SSRN 6569258; Pan, Ding and Giesecke, 2026, arXiv 2609.00731), and an e-process against the best fitted member of the current theory is published for a learned proposer (Ma et al., 2026, arXiv 2610.07627); we did not find this combination for hypotheses written by language models in the work we read, which is not a claim about the whole field."

Conditions : (a) la première phrase décrit notre juge selon N-064 et N-067 ; elle suppose que la mise en œuvre est bien celle de la conception v7, § 2, et du nul d'archive ajusté (LISEZMOI v7-v6) — à confirmer par l'auteur de l'orchestrateur, pas par ce lecteur ; (b) « scellée avant que les données existent » ne vaut que pour les mondes dont les issues sont tirées après le gel ; sur une banque figée, dire « avant que les issues soient lues » (conception v7, § 1, « issues cachées ») ; (c) la phrase reste soumise au mot de Lazar (modification de revendication).

## 5. Ce qui reste non lu

**Priorité haute (peut encore occuper la conjonction)**

1. **PDF officiel de SSRN 6569258** : refusé (section 6). La copie lue (hôte d'une conférence, juin 2026) porte la date d'avril 2026 et un résumé identique à la notice SSRN ; l'identité exacte n'est pas vérifiable.
2. **Beyond Prompting** (2603.14288, 60 p.) : lu par passages ; dire si l'apport marginal sur le modèle à cinq facteurs est une **règle de promotion** calculée hors de l'agent.
3. Références de Ma et al. où un **modèle de langue** propose des modèles testés contre la classe en vigueur : LLM-ACES (arXiv 2606.25039), ATLAS (arXiv 2606.12386), Wahl et al. (arXiv 2602.18266, cadre probabiliste de découverte de modèles par modèle de langue), EvoSCM (arXiv 2609.01526). Si l'une teste par e-processus une proposition de modèle de langue contre la théorie en vigueur, la conjonction de la section 0, point 5, perd (i) et (iii).
4. Koijen et Levy, SSRN 6474601, 2026 (cité par SEADS, p. 13) : agentique en évaluation d'actifs ; SSRN refusera sans doute.
5. Novy-Marx et Velikov, « AI-powered (finance) scholarship », Journal of Economic Literature 64(1), 2026 (cité par LIU, p. 8) : signaux minés puis filtrés par le protocole « Assaying Anomalies ».

**Priorité moyenne (principe, déjà établi par FGX ; à lire pour les citations)**

6. Littérature classique des tests d'englobement et d'emboîtement — **de mémoire, non vérifiée, non opposable (R7)** : Mizon et Richard (1986), Chong et Hendry (1986), englobement de prévisions (Harvey, Leybourne, Newbold, 1998), comparaison de modèles emboîtés (Clark et McCracken, 2001 ; Clark et West, 2007), test de recouvrement (Huberman et Kandel, 1987), Barillas et Shanken. Revues payantes ; versions de travail à chercher.
7. Harvey et Liu, « Incremental factors » (2014d) et sa suite publiée (cités par HLZ, p. 36) ; fouilles automatiques d'avant les modèles de langue jugées contre les modèles de facteurs (de mémoire : Yan et Zheng, 2017 ; Chordia, Goyal, Saretto, 2020).
8. Systèmes cités par SEADS et non lus : AlphaAgent (originalité syntaxique contre le « zoo » admis), QuantaAlpha, RD-Agent(Q), FactorMiner, Hubble, AlphaEval.
9. Code de SEADS (annoncé à l'acceptation, p. 24) et de LIU (« will be made publicly available », p. 1).

**Pièces lues en partie** (déclaré en section 2) : OUTGROW (annexes C, E, F, G par termes), CR, HZ, MARTIN, CLERICO (preuves), ALPHASCHEMA (p. 14-18), PHANTOM (annexes A à D, F), HLZ, FGX (après la p. 4), REDONDANCE (après la p. 4), CREDIT (après la p. 5), BEYOND, HYPFACT (p. 6-8, résultats).

## 6. Refus et incidents (tels quels)

- **SSRN** : `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6569258` (19:26:20Z) et `https://papers.ssrn.com/sol3/Delivery.cfm/6569258.pdf?abstractid=6569258&mirid=1` (19:26:26Z) : HTTP 403, page « Just a moment... » (vérification humaine du service de protection). **Non contourné.** Pages de refus versées et scellées (`ssrn-6569258/page-resume-ssrn-6569258-refus-v1.html`, `essai-livraison-ssrn-6569258-refus-v1.html`). La copie lue a été trouvée par un moteur de recherche, déposée publiquement par l'hôte d'une conférence (provenance : `ssrn-6569258/provenance-v1.md`).
- **Semantic Scholar** : deux réponses 429 (« Too Many Requests ») vers 19:26:45Z et 19:26:55Z, sans puis avec la clé lue par son nom ; la recherche est passée à 19:37Z.
- **Classifieur du mode automatique** : vers 19:26 UTC, la lecture de la notice locale du relais réseau et de son état a été refusée, message recopié tel quel : « Permission for this action was denied by the Claude Code auto mode classifier. Reason: The server-side auto mode classifier judged this action dangerous (it gave no explanation). » Geste non repris, par aucun autre moyen ; il n'était pas nécessaire à la lecture (les téléchargements sont passés sans lui).
- Aucun chemin interdit par la consigne n'a été ouvert. Les deux seules recherches récursives (sous `docs/sources/` et sous `docs/notes/ideation-organisme-v1/`) ne contiennent, selon l'index de git (`git ls-files`, lecture des noms seulement), aucun des chemins interdits ; les autres lectures du dépôt sont nommées (N-064, N-067, registre R-2570 et R-2571, conception v7, rapports C4 et 4-A lus par `git show` sur leurs branches).
