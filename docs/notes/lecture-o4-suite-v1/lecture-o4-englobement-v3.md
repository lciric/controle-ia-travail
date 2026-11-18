# Lecture adverse de O4 (juge au nul des lois connues) : SSRN 6569258, pistes de priorité haute et tests d'englobement — v3

- **Version 2** (R12 ; la v1, `f521e164e79cb75e…`, reste en place sur `main`) : écrite par le modèle A (session du compte organisme) à
  2026-11-14T23:30:39Z (`date -u`), sur le mot direct de Lazar **R-2822** (« N-SSRN-1 : mettre à jour les citations de Liu et coauteurs sur la
  version de septembre de l'article ; N-SSRN-2 : citer Koijen et Levy dans toute phrase publique sur des prédictions faites avant les
  données. go »), d'après la lecture sur PDF de SSRN 6569258 (version officielle) et de SSRN 6474601 (`docs/notes/lecture-o4-suite-v1/lecture-pdf-ssrn-o4-v2.md`, `93518e46d59825d9…`,
  contre-lue « tient avec réserves », réserves portées ; citations rejouées 91 sur 91). Changent seulement : sections 0 (points 1, 3, 5),
  2 (lignes LIU et KL), 3.1, 4, 5 (points 1 et 4). Le verdict ne change pas. Les noms de modèles de la v1 sont retirés (R-2690).
- **Version 3** (R12 ; la v2, `9c3c81a9423ea3dc…`, reste en place) : écrite par le modèle A à 2026-11-14T23:34:28Z (`date -u`) ; porte la contre-lecture
  de la v2 par le modèle K (`contre-lecture-lecture-o4-englobement-v2.md`, `04287f0f…`, « porte la décision après corrections », 0
  bloquant, 3 majeurs, 4 mineurs) : nom de modèle resté en section 3.2 retiré ; pages décisives de LIU (section 2) mises sur la version
  de septembre ; temps réel dit pour le banc d'essai de KL, non établi pour ses systèmes optimisés (section 0, point 1) ; section 5,
  point 1, à jour ; section 6 marquée « (v1) ». La v2 changeait aussi, sans le dire dans sa ligne, l'en-tête (règle de lecture) et le
  paragraphe « Conséquence proposée » (constat 5). Le verdict ne change pas.
- **Lecteur de la v1** : sous-agent neuf, qui n'a écrit ni N-064 ni aucun brouillon de N-067 ni aucun rapport de l'état de l'art. Mandat : R-2571, point 4 (a) (« lire SSRN 6569258 et les pistes de priorité haute sur PDF avant tout texte qui déclare O4 libre hors du dépôt »), N-067 retenue, section 4, point 2, et section 8.
- **Fenêtre de travail** : 2026-11-13, 19:24 à 19:48 UTC (`date -u`). Aucune écriture git ; aucune dépense ; aucun envoi de nos énoncés à un tiers (les requêtes ne portent que des mots-clés génériques, recopiées sous `docs/sources/pdf/lecture-o4-v1/recherches/`) ; la clé de Semantic Scholar n'a été lue que par son nom.
- **Règle de lecture (R8).** « Libre » = « non trouvé dans les pièces lues », jamais « trou du champ ». Une page citée renvoie à la page du PDF (le numéro imprimé est donné entre parenthèses quand il diffère). [v2 : les citations de LIU de la section 3.1 sont celles de la version officielle de septembre, rejouées par `docs/notes/lecture-o4-suite-v1/rejouer_citations_ssrn_o4_v1.py` sur `citations-ssrn-o4-v4.json` ; les autres citations sont celles de la v1.] Les 53 citations de la v1 ont été recopiées puis **vérifiées par programme** sur le texte extrait par `pdftotext` : 53 sur 53 trouvées sur la page indiquée (`docs/sources/pdf/lecture-o4-v1/verification-citations/resultat-verification-citations-o4-v1.json`, script `verifier_citations_o4_v1.py`, liste `citations-o4-v1.json`, tous scellés).

## 0. Verdict

**O4 : occupée en partie** — et la partie occupée est le principe. Ce qui reste non trouvé dans les pièces lues n'est plus une idée mais une **réunion de pièces publiées chacune ailleurs**.

1. **Le principe « une découverte se juge contre ce qui est déjà connu, non contre aucun effet » est publié**, y compris pour une archive qui grandit au fil des découvertes :
   - dans la recherche humaine en finance, comme test de toute proposition nouvelle contre l'ensemble des facteurs déjà proposés, rejoué récursivement dans l'ordre d'apparition (Feng, Giglio, Xiu, NBER 25481, 2019, p. 2-4 du PDF) ;
   - **pour des hypothèses proposées par un modèle de langue** : jugées contre 209 anomalies publiées et contre les modèles de facteurs, après la boucle de découverte (Liu, Liu, Liu, Mei, SSRN 6569258, version officielle de septembre 2026, p. 1, 5, 6, 30, 32) ; jugées **dans la boucle**, par une porte déterministe hors du modèle, contre un panel de référence **plus la bibliothèque des facteurs déjà admis**, qui s'accroît à chaque admission (Pan, Ding, Giesecke, « SEADS », arXiv 2609.00731, 1er septembre 2026, p. 6, 7, 16, 25) ;
   - **pour des systèmes à modèle de langue, sur un banc d'essai en temps réel où les prédictions sont recueillies avant que le
     rendement n'existe**, jugées par leur gain d'explication sur des déterminants connus (Koijen et Levy, SSRN 6474601, date imprimée
     30 juin 2026, p. 1, 3, 8, 11 ; la date de dépôt sur SSRN n'est pas lue) ; pour les systèmes **optimisés**, que le texte fasse émettre
     les prédictions de la seconde moitié du trimestre avant les événements est probable, non établi (p. 11, 16).
2. **La forme statistique est publiée aussi** : un e-processus (preuve accumulée, valide à tout instant d'arrêt) qui oppose une loi prédictive **engagée avant l'observation** à la **meilleure loi ajustée de la théorie en vigueur**, et ne révise la théorie que si celle-ci est rejetée ; la théorie révisée devient le nul de l'étape suivante (Ma et al., « Learning to Outgrow a Theory », arXiv 2610.07627, conférence ICLR 2027, p. 1, 4, 15). Le proposeur y est une politique apprise, **pas un modèle de langue** (les systèmes à modèle de langue y sont des bases de comparaison, p. 6). L'outil générique — e-valeurs pour savoir si un prévisionniste nouveau bat un prévisionniste établi — est publié depuis 2021 (Choe et Ramdas, arXiv 2110.00115, p. 1, 38 ; Henzi et Ziegel, arXiv 2103.08402, p. 1, 4).
3. **SSRN 6569258 n'occupe pas O4 en entier** (version officielle de septembre 2026) : son nul des lois connues est appliqué
   **après** la boucle et hors d'elle, sur l'échantillon même de la recherche (données de 1963 à 2024), par régression contre les dix
   prédicteurs publiés les plus proches et trois modèles de facteurs, avec des statistiques de Student à taille fixée (p. 11, 22, 30) ;
   dans la boucle, le crible est « coefficient de Fama et MacBeth significatif dans le sens prédit », c'est-à-dire un nul « aucun effet »
   (p. 19). Le retour fait au proposeur contient un **alpha contre un modèle de facteurs fixé, en avril comme en septembre** (quatre
   facteurs de Carhart dans la copie d'avril, p. 14-15 ; cinq facteurs en septembre, p. 19, 57) : ce n'est ni une règle de promotion ni
   un nul formé de l'archive. (v2 : l'appui de la v1 sur la phrase d'avril p. 36, « lacks direct access to factor model results during
   the discovery loop », est retiré : elle est absente de la version de septembre, et la copie d'avril elle-même rendait déjà un alpha au
   proposeur.) Le test prospectif gelé y est dit **non fait** (p. 6, 34). Il occupe le **principe** pour des hypothèses de modèle de
   langue (p. 1, 5, 6, 32).
4. **SEADS (2609.00731) est la pièce la plus proche** : juge déterministe dans la boucle, contrôles = archive (référence + admis), seuils fixés avant toute course (p. 6). Il lui manque, dans le texte lu : la validité à tout instant d'arrêt (statistiques de Student, seuils 1,0 et correction de Bonferroni), des prédictions scellées avant que les données existent (fenêtre d'échantillon 2010-2019, p. 8), des lois prédictives comparées par vraisemblance (ce sont des scores de rang).
5. **Non trouvé dans les pièces lues** : la conjonction (i) proposeurs modèles de langue, (ii) nul formé d'une **mise en commun ajustée des lois prédictives de l'archive** (lois connues et survivantes promues par l'organisme lui-même), (iii) e-processus comme règle de promotion, (iv) prédictions scellées avant que les données existent, statistique calculée hors des agents. (i) et (ii, sous forme de régression) sont chez SEADS ; (iii) et une partie de (iv) (engagement avant observation, classe fixée à l'entrée de l'étape) chez Ma et al. ; le scellement par empreinte chez CONFIRM et « Hard to Fool » (déjà cités par N-067, section 3) ; la partie « en temps réel » de (iv) (prédictions faites avant que le rendement n'existe, statistique calculée par l'évaluateur), sans scellement ni horodatage trouvé, chez Koijen et Levy (SSRN 6474601, p. 1, 3, 11).

**Conséquence proposée (nœud : modification de revendication, à Lazar)** : O4 ne peut pas être déclarée libre hors du dépôt ; elle se dit, comme l'énoncé retenu de O2 dans N-067 (section 4, point 1), **comme un assemblage dont les pièces sont empruntées**, avec citations. La ligne publique actuelle (« battre un nul des lois connues […] « rien au-delà de l'archive » ») est, dans sa lettre, occupée dans son principe par SEADS, par Liu et al. et par Koijen et Levy. Phrase proposée en section 4.

## 1. Énoncé lu

- **O4**, table des revendications (`docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md`, `08a3738a…`, l. 260) : « Nouveauté statistique : battre un nul des lois connues (nul informé, nul poolé v8, nul v9 par morceaux), « rien au-delà de l'archive » ».
- **N-064** (`docs/decisions/decision-N-064-v1.md`, `387c9d4e…`, point 2) : nul « formé des lois connues (l'archive) », l'une des quatre composantes de l'énoncé retenu de O2.
- **N-067, brouillon 2** (`decision-N-067-v1-brouillon2.md`, `cb3f3719…`) et **N-067 retenue** (`decision-N-067-v1.md`, `966dd9dc…`), section 4, points 1 et 2 : « Juge statistique dont le nul est formé des lois déjà connues (l'archive) : une fiche n'est promue que si sa prédiction scellée bat ce que l'archive prédit déjà » ; O4 « désormais seul porteur de la revendication du juge » ; clause d'usage public (R-2571, point 4 (a)).
- **Mise en œuvre** (pour juger la forme, non pour revendiquer) : conception v7, § 2 (`docs/notes/ideation-organisme-v1/orchestrateur-v51/conception-v7-v1.md`, `31fc8c4b…`) — un membre « connu » de la bibliothèque du juge, loi ajustée avant le gel ; LISEZMOI v7-v6 (`8d96bf9f…`) — « nul d'archive ajusté » : mise en commun linéaire ajustée des lois connues (parents et survivantes).

## 2. Table des pièces

Toutes sous `docs/sources/pdf/lecture-o4-v1/`, un dossier par source, chaque PDF scellé (compagnon `.sha256`) avec un `provenance-v1.md` (adresse, heure UTC, réponse, empreinte). Statut : vis-à-vis de O4.

| clé | pièce | dossier | empreinte | lu | statut vis-à-vis de O4 | pages décisives |
|---|---|---|---|---|---|---|
| LIU | Liu, Liu, Liu, Mei, « Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing », SSRN 6569258, **version officielle de septembre 2026** (84 p., déposée par Lazar : `docs/sources/pdf/ssrn-lazar-2026-11-14/`), lue en v2 ; la copie d'avril (hôte d'une conférence, `ssrn-6569258/`, `2d4e1d61…`, 71 p.) reste la pièce de la v1 | `../ssrn-lazar-2026-11-14/` | `15cdb423744d7885…` | par pages (lecture SSRN v2, section 5) | **occupe en partie** : principe pour des hypothèses de modèle de langue, hors boucle | septembre : 1, 5, 6, 11, 15, 19, 22, 29, 30, 32, 38, 40, 42, 57 ; avril : 14, 15 |
| KL | Koijen, Levy, « Assessing the Benefits of Optimized Agentic AI Systems for Asset Pricing », SSRN 6474601, date imprimée 30 juin 2026 (39 p., déposée par Lazar), lue en v2 | `../ssrn-lazar-2026-11-14/` | `98757745f4364034…` | p. 1-30, 38-39 ; tableaux par notes (lecture SSRN v2, section 5) | **occupe en partie** : principe pour des systèmes à modèle de langue optimisés ; partie « en temps réel » de (iv) ; ni archive comme nul, ni e-processus, ni scellement | 1, 3, 8, 11, 16 |
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

### 3.1 LIU — SSRN 6569258 (pièce nommée par R-2571), version officielle de septembre 2026 (v2)

Citations de la version officielle (`15cdb423744d7885…`), rejouées par programme (identifiants de `citations-ssrn-o4-v4.json`) ; la
correspondance avec chaque citation d'avril de la v1 (page, état) est à la section 1 de la lecture SSRN v2.

- Objet : des agents à modèle de langue proposent des formules comptables dans un langage symbolique, une chaîne d'évaluation fixe les
  teste : [p. 1, L06] « We place specialized large language model agents in an environment with a symbolic language of interpretable accounting formulas and a fixed empirical evaluation pipeline. »
- Le principe de O4, pour des hypothèses de modèle de langue :
  - [p. 1, L01] « incremental information relative to 209 published anomalies »
  - [p. 6, L02] « where seemingly new evidence is subsumed by what is already known »
  - [p. 30, L03] « Finally, the record must retain its declared direction and a conditional statistic above 1.96 after controlling for up to ten selected nearby predictors from the Chen–Zimmermann library (Chen and Zimmermann, 2022). »
  - [p. 32, L04] « Many records that survive multiplicity and factor adjustment therefore contain information already represented by their selected published comparators. »
  - [p. 22, L16] « For each candidate reaching the published-predictor stage, the spanning procedure selects up to ten predictors with the largest absolute average cross-sectional rank correlations »
  - course entre les propres découvertes du système, après la recherche : [p. 22, L15] « This horse race identifies incremental conditional return association relative to other constructions generated for the same economic task »
  - revendication de priorité des auteurs : [p. 5, L05] « To our knowledge, this is the first study to combine autonomous LLM-guided signal discovery with modern multiple-testing corrections, alternative factor models, subsample and decay analyses, and spanning tests against published anomalies »
- Ce qui n'y est pas (pourquoi « en partie ») :
  - les tests contre le connu sont hors de la boucle : [p. 11, L07] « Once a run ends, post-search procedures operate outside the discovery loop and are indexed to the population for which each procedure is defined. »
  - dans la boucle, le nul est « aucun effet » : [p. 19, L08] « We classify an empirically evaluated hypothesis as a first-pass success when its Fama– MacBeth statistic is finite, exceeds 1.96 in absolute value, and the estimated slope has the direction declared before evaluation »
  - le retour fait au proposeur contient un alpha contre un modèle de facteurs fixé : [p. 57, L09] « Each archive entry reports the expression, declared direction, Fama–MacBeth statistic, long– short alpha and alpha statistic, Sharpe ratio, coverage, and any execution error. » ; [p. 19, L10] « The discovery-stage alpha uses the Fama–French five-factor model » ; il en allait de même en avril : [avril p. 15, A13] « successful signals (with Fama–MacBeth t-statistic, alpha t-statistic, Sharpe ratio, and quintile returns) » ; [avril p. 14, A14] « We regress the long–short portfolio’s excess returns on the Carhart (1997) four factors »
  - l'archive de la course est un contexte, non un nul : [p. 15, L11] « Within a given run, the archive is the state variable of the adaptive search. » ; la nouveauté y est jugée par le critique, modèle de langue : [p. 38, L13] « The critic’s comparison set is limited to published signals invoked from its finance knowledge and proposals visible in the contemporaneous task archive; it is not an exhaustive literature review. »
  - pas d'e-valeur (aucune occurrence sur les 84 pages ; lecture SSRN v2) : inférence à taille fixée, [p. 29, L18] « the run-level Benjamini–Yekutieli (BY) false-discovery-rate procedure at q = 0.05 »
  - pas de validation hors échantillon, données antérieures à l'engagement : [p. 6, S10] « First, the search is adaptive and uses the same historical panel throughout, so our post-discovery tests provide search-adjusted inference rather than true out-of-sample validation. » ; [p. 17, L22] « The sample ends in December 2024. » ; [p. 6, L23] « A true out-of-sample test would freeze the discovered hypotheses and all evaluation choices before new returns are realized, then evaluate t… » (citation complète au fichier)
  - séparation déjà là, à citer pour O1 : [p. 42, L25] « The LLM does not read firm-level observations, assign historical scores, access the raw CRSP– Compustat panel, or alter the portfolio-construction procedure. » ; sens prédit posé avant le résultat : [p. 40, L21] « Each hypothesis states an economic mechanism, an executable accounting expression, and a return direction before its own result is observed. »
- Retiré de la v1 : l'appui sur la phrase d'avril p. 36 (« it lacks direct access to factor model results during the discovery loop »),
  absente de la version de septembre et déjà contredite par la copie d'avril (p. 15).

### 3.1 bis KL — Koijen, Levy, SSRN 6474601 (v2)

- Principe, pour des systèmes à modèle de langue : [p. 8, K05] « The primary performance statistic is the incremental explanatory power, or ∆R2 , generated by the AI system’s predictions over a baseline model, e.g., one that includes only the quantitative controls » ; [p. 1, K02] « the best-optimized systems more than double the explained variation in returns relative to existing literature. »
- Partie « en temps réel » de (iv) : [p. 1, K01] « We introduce a real-time, out-of-sample benchmark to sidestep both problems that measures how well AI systems explain contemporaneous stock » (citation complète au fichier) ; [p. 3, K03] « the AI model uses to make its forecasts (as well as the model parameters), are determined prior to the earnings announcement. » ; [p. 11, KO1] « This enables us to collect data, generate predictions, and evaluate results strictly out of sample. »
- Ce qui n'y est pas : l'archive connue se réduit aux contrôles quantitatifs (et, pour les systèmes optimisés, au système non optimisé : [p. 19, K32] « With the ACE rulebook, the R2 rises to 17.1% [0.12, 0.24], a gain of 3.0 percentage points. ») ; un livre de règles qui grandit existe ([p. 19, K31] « The result is a modular, interpretable set of rules that grows and refines over time. »), versé dans le prédicteur, non dans le nul ; inférence par intervalles de rééchantillonnage à échantillon fixé, aucune e-valeur ; aucun scellement ni horodatage trouvé ; pour les systèmes optimisés, le texte ne dit pas que les prédictions de la seconde moitié du trimestre ont été émises avant les événements (p. 16).

### 3.2 SEADS — Pan, Ding, Giesecke, arXiv 2609.00731 (la pièce la plus proche)

- Un planificateur et un proposeur modèles de langue (un modèle de langue du commerce, p. 24) ; une porte de validation déterministe, hors du modèle :
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

> « Notre juge ne promeut une hypothèse que si sa prédiction, scellée avant que les données existent, bat par un e-processus calculé hors des agents la meilleure combinaison ajustée des lois déjà connues, archive de l'organisme comprise. Juger une découverte contre ce qui est déjà connu plutôt que contre l'absence d'effet est une pratique établie (Feng, Giglio et Xiu, 2019), déjà appliquée à des hypothèses proposées par des modèles de langue (Liu, Liu, Liu et Mei, 2026, SSRN 6569258 ; Pan, Ding et Giesecke, 2026, arXiv 2609.00731) et à des prédictions de systèmes à modèle de langue faites avant que les données existent (Koijen et Levy, 2026, SSRN 6474601), et la règle d'un e-processus contre la meilleure loi ajustée de la théorie en vigueur est publiée pour un proposeur appris (Ma et al., 2026, arXiv 2610.07627) ; nous n'avons pas trouvé, dans les travaux lus, cette réunion pour des hypothèses rédigées par des modèles de langue, ce qui ne vaut pas pour l'ensemble du champ. »

Rendu anglais fidèle, si le texte sortant est en anglais :

> "Our judge promotes a hypothesis only if its prediction, sealed before the data exist, beats — through an e-process computed outside the agents — the best fitted combination of the already known laws, including the organism's own archive. Judging a discovery against what is already known rather than against no effect is established practice (Feng, Giglio and Xiu, 2019), already applied to hypotheses proposed by language models (Liu, Liu, Liu and Mei, 2026, SSRN 6569258; Pan, Ding and Giesecke, 2026, arXiv 2609.00731) and to predictions of language-model systems made before the data exist (Koijen and Levy, 2026, SSRN 6474601), and an e-process against the best fitted member of the current theory is published for a learned proposer (Ma et al., 2026, arXiv 2610.07627); we did not find this combination for hypotheses written by language models in the work we read, which is not a claim about the whole field."

Conditions : (a) la première phrase décrit notre juge selon N-064 et N-067 ; elle suppose que la mise en œuvre est bien celle de la conception v7, § 2, et du nul d'archive ajusté (LISEZMOI v7-v6) — à confirmer par l'auteur de l'orchestrateur, pas par ce lecteur ; (b) « scellée avant que les données existent » ne vaut que pour les mondes dont les issues sont tirées après le gel ; sur une banque figée, dire « avant que les issues soient lues » (conception v7, § 1, « issues cachées ») ; (c) la phrase reste soumise au mot de Lazar (modification de revendication) ; (d) v2 : la citation de Koijen et Levy y est portée sur le mot de Lazar R-2822 (N-SSRN-2), et Liu et al. y renvoie à la version officielle de septembre (N-SSRN-1).

## 5. Ce qui reste non lu

**Priorité haute (peut encore occuper la conjonction)**

1. **PDF officiel de SSRN 6569258** : v2 : **lu** (version de septembre 2026, déposée par Lazar ; lecture SSRN v2). En v1 : refusé (section 6), et la v1 lisait la copie d'avril d'un hôte de conférence ; la version officielle de septembre en diffère (84 p. contre 71 ; correspondance des citations : lecture SSRN v2, section 1).
2. **Beyond Prompting** (2603.14288, 60 p.) : lu par passages ; dire si l'apport marginal sur le modèle à cinq facteurs est une **règle de promotion** calculée hors de l'agent.
3. Références de Ma et al. où un **modèle de langue** propose des modèles testés contre la classe en vigueur : LLM-ACES (arXiv 2606.25039), ATLAS (arXiv 2606.12386), Wahl et al. (arXiv 2602.18266, cadre probabiliste de découverte de modèles par modèle de langue), EvoSCM (arXiv 2609.01526). Si l'une teste par e-processus une proposition de modèle de langue contre la théorie en vigueur, la conjonction de la section 0, point 5, perd (i) et (iii).
4. Koijen et Levy, SSRN 6474601, 2026 (cité par SEADS, p. 13) : v2 : **lu** (déposé par Lazar ; lecture SSRN v2) ; occupe en partie (section 2, ligne KL).
5. Novy-Marx et Velikov, « AI-powered (finance) scholarship », Journal of Economic Literature 64(1), 2026 (cité par LIU, p. 8) : signaux minés puis filtrés par le protocole « Assaying Anomalies ».

**Priorité moyenne (principe, déjà établi par FGX ; à lire pour les citations)**

6. Littérature classique des tests d'englobement et d'emboîtement — **de mémoire, non vérifiée, non opposable (R7)** : Mizon et Richard (1986), Chong et Hendry (1986), englobement de prévisions (Harvey, Leybourne, Newbold, 1998), comparaison de modèles emboîtés (Clark et McCracken, 2001 ; Clark et West, 2007), test de recouvrement (Huberman et Kandel, 1987), Barillas et Shanken. Revues payantes ; versions de travail à chercher.
7. Harvey et Liu, « Incremental factors » (2014d) et sa suite publiée (cités par HLZ, p. 36) ; fouilles automatiques d'avant les modèles de langue jugées contre les modèles de facteurs (de mémoire : Yan et Zheng, 2017 ; Chordia, Goyal, Saretto, 2020).
8. Systèmes cités par SEADS et non lus : AlphaAgent (originalité syntaxique contre le « zoo » admis), QuantaAlpha, RD-Agent(Q), FactorMiner, Hubble, AlphaEval.
9. Code de SEADS (annoncé à l'acceptation, p. 24) et de LIU (« will be made publicly available », p. 1).

**Pièces lues en partie** (déclaré en section 2) : OUTGROW (annexes C, E, F, G par termes), CR, HZ, MARTIN, CLERICO (preuves), ALPHASCHEMA (p. 14-18), PHANTOM (annexes A à D, F), HLZ, FGX (après la p. 4), REDONDANCE (après la p. 4), CREDIT (après la p. 5), BEYOND, HYPFACT (p. 6-8, résultats).

## 6. Refus et incidents (tels quels) (v1)

- **SSRN** : `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6569258` (19:26:20Z) et `https://papers.ssrn.com/sol3/Delivery.cfm/6569258.pdf?abstractid=6569258&mirid=1` (19:26:26Z) : HTTP 403, page « Just a moment... » (vérification humaine du service de protection). **Non contourné.** Pages de refus versées et scellées (`ssrn-6569258/page-resume-ssrn-6569258-refus-v1.html`, `essai-livraison-ssrn-6569258-refus-v1.html`). La copie lue a été trouvée par un moteur de recherche, déposée publiquement par l'hôte d'une conférence (provenance : `ssrn-6569258/provenance-v1.md`).
- **Semantic Scholar** : deux réponses 429 (« Too Many Requests ») vers 19:26:45Z et 19:26:55Z, sans puis avec la clé lue par son nom ; la recherche est passée à 19:37Z.
- **Classifieur du mode automatique** : vers 19:26 UTC, la lecture de la notice locale du relais réseau et de son état a été refusée, message recopié tel quel : « Permission for this action was denied by the Claude Code auto mode classifier. Reason: The server-side auto mode classifier judged this action dangerous (it gave no explanation). » Geste non repris, par aucun autre moyen ; il n'était pas nécessaire à la lecture (les téléchargements sont passés sans lui).
- Aucun chemin interdit par la consigne n'a été ouvert. Les deux seules recherches récursives (sous `docs/sources/` et sous `docs/notes/ideation-organisme-v1/`) ne contiennent, selon l'index de git (`git ls-files`, lecture des noms seulement), aucun des chemins interdits ; les autres lectures du dépôt sont nommées (N-064, N-067, registre R-2570 et R-2571, conception v7, rapports C4 et 4-A lus par `git show` sur leurs branches).
