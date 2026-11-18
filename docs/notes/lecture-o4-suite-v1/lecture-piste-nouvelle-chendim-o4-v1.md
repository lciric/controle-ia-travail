# Lecture de la piste nouvelle CHENDIM contre O4 (juge au nul formé des lois connues) — v1

- **Lecteur** : modèle I, lecteur neuf pour cette pièce (n'a écrit ni N-064, ni N-067, ni la note d'englobement, ni la note des pistes de priorité haute).
- **Heures** (`date -u`, recopiées) : début de la lecture 2026-11-18T03:32:38Z ; rédaction de cette note 2026-11-18T03:43:37Z.
- **Source** : Andrew Y. Chen et Chukwuma Dim, « High-Throughput Asset Pricing », arXiv 2311.10685 v3 ; date imprimée « June 2025 » (p. 1) ; tampon arXiv du 2 juin 2025 (p. 1) ; « First posted November 2023. » (p. 1). PDF `docs/sources/pdf/lecture-o4-v3/arxiv-2311.10685/2311.10685v3.pdf`, 44 pages, sha256 `d338d13e08302df0f5d38c8886449eebe30ebd1a20d29390757658644ec50b7e`, recalculé ici, égal à celui du compagnon `.sha256`.
- **Profondeur** : PDF entier, 44 pages sur 44 (texte courant, annexes A, B et C, références, légendes de figures, notes et contenu texte des tables) ; graphiques des figures non lus ; aucun code (section 1).
- **Rejeux** : citations du PDF **66 sur 66** (programme gelé `verifier_citations_priorite_haute_o4_v1.py`, sortie `lecture-piste-nouvelle-chendim-o4-v1-resultat-citations-pdf.json`) ; extraits de code **0 sur 0** (programme gelé `verifier_extraits_code_o4_v1.py`, code de sortie 0 ; liste vide : aucun code lu pour cette pièce, selon la consigne).
- **Mandat** : consigne de la session mère du 18 novembre (lecture d'une piste nouvelle contre O4, condition de proportion). Le verdict en vigueur sur O4 reste *occupée en partie* (N-067) ; rien n'est déclaré libre ici.
- **Règles de lecture** : R7 (rien sans PDF empreinté et page), R8 (*non trouvé* = non trouvé dans ce qui a été lu, à la profondeur déclarée), R4 (en cas de doute, le sens non flatteur pour notre revendication). Pages = pages du PDF, 1 = première page du fichier. **Toutes les citations entre guillemets viennent des pages 1 à 27** : au-delà, le programme de rejeu gelé numérote mal les pages de ce PDF (section 8, incident 1). Ce qui vient des pages 28 à 44 est donc **paraphrasé, à sa vraie page** (extraction `pdftotext -f n -l n`), et n'est pas rejoué par le programme.

**En bref.** CHENDIM n'occupe aucune composante de O4. Chaque signal y est jugé **contre zéro** (aucun effet), après une correction de la sélection par Bayes empirique, avec une loi latente ajustée sur **la population des candidats eux-mêmes**, et non sur l'archive. Le publié n'y sert que de **repère de performance de la méthode entière** ; les candidats ne sont pas choisis sur leurs rendements passés, et la construction des stratégies de rendements passés est voulue sans savoir tiré des publications. Statuts : P *voisin (lointain)* ; (i) *non trouvé* ; (ii) *voisin (lointain)* ; (iii) *non trouvé* ; (iv-a) *voisin (lointain)* ; (iv-b) *voisin*, au sens trivial (aucun agent). Conjonction non trouvée. La pièce **n'est pas sans rapport** avec les composantes : elle les touche en voisine lointaine, ce qui justifie la lecture entière. Elle répond à la piste *Chen et Dim* du nœud 9 de la note des pistes de priorité haute (v3), et nomme, sans que je les lise, des travaux qui pourraient toucher (ii), (iii) et (iv-a) (section 7, nœud 2).

## 1. Profondeur

- **PDF lu en entier**, page par page, sur le texte extrait par `pdftotext` page à page (`-f n -l n`) : p. 1 (résumé), p. 2-5 (introduction, section 1.1 sur la littérature), p. 5-10 (section 2 : données et méthode, dont 2.2 à 2.4 sur Bayes empirique et sa mise en œuvre), p. 10-17 (sections 3 et 4 : performance hors échantillon, composition, intuition du rétrécissement, exactitude des prédictions), p. 17-22 (section 5 : comparaison aux contrôles de fausses découvertes), p. 22-23 (conclusion), p. 24-27 (annexe A : construction des stratégies ; annexe B : preuve de la proposition 1, estimation, méthode de Romano et Wolf ; annexe C : titre seul), p. 28-30 (figure A.1, tables A.1 et A.2), p. 31-34 (références), p. 35-41 (figures 1 à 7), p. 42-44 (tables 1 à 3).
- **Figures** (p. 28, 35-41) : légendes lues ; les graphiques ne sont pas lus (le texte extrait y sort en glyphes illisibles, sauf la figure 7, p. 41, dont les axes et la légende sont lisibles).
- **Tables** (p. 29, 30, 42-44) : lues sur le texte extrait.
- **Code** : aucun. La consigne n'en demande pas pour cette pièce (proportion). Le dossier des clones ne contient aucun clone du code de réplication dont l'adresse est donnée p. 1 (« Replication code: https://github.com/chenandrewy/high-throughput-ap ») ; rien n'a été cherché ni téléchargé.
- **Recherche de termes** : sur le texte entier, page par page, après recollage des sauts de ligne et des coupures de mots, casse ignorée (section 2).
- Outils de lecture (extraction page à page, recherche de termes, contrôle croisé des pages) : dans le dossier de travail de la session, non versés.

## 2. Recherche de termes

Les pages données sont celles où le terme apparaît (entre parenthèses, le nombre d'occurrences quand il y en a plusieurs).

| terme | pages | ce que donne le terme |
|---|---|---|
| `e-value`, `evalue`, `e value` | aucune (3 occurrences brutes de `e value`, p. 6, 11, 20, sont des fins de mots : *absolute value*, *the value*, *values*) | rien |
| `e-process`, `e process` | aucune | rien |
| `anytime` | p. 43 (2) | nom d'un portefeuille de comparaison de la table 2 (stratégies publiées de Chen et Zimmermann 2022, toutes dates de publication ; un second portefeuille ne prend que les stratégies publiées avant 2004), paraphrase. `any time` : p. 21, fin de mot (*many times*). Aucune validité à tout instant d'arrêt |
| `martingale`, `optional stopping`, `sequential` | aucune | rien |
| `stopping` | p. 27 (2) | condition d'arrêt **de calcul** ajoutée à l'algorithme 2.1 de Romano et Wolf : l'algorithme « does not have a stopping condition based on » le nombre d'ensembles à parcourir (p. 27) ; aucun rapport avec l'arrêt optionnel |
| `likelihood ratio`, `Bayes factor` | aucune | rien ; la quasi-vraisemblance sert à ajuster la loi latente (p. 10, 26), pas à comparer des lois |
| `model averaging`, `stacking` | aucune | rien |
| `averaging` | p. 2, 15 | moyenne à poids égaux des 200 stratégies publiées, en repère (p. 2) ; moyenne des prédictions par groupe (p. 15) |
| `encompass` | aucune | rien |
| `spanning` | p. 10, 17 | sens temporel seulement (années de prévision, p. 10 ; décennies, p. 17) ; aucun test d'enjambement |
| `benchmark`, `baseline` | aucune | rien (le repère publié est dit *for comparison*, p. 11) |
| `null` | p. 3 (3), 4 (2), 13 (2), 14 (7), 15, 20, 21 (3), 22 (4), 36 (3), 37 (3), 41 | partout le nul **aucun effet** : loi normale centrée réduite des statistiques de Student (p. 3, 13, 14 ; légendes des figures 2 et 3, p. 36-37), rendement moyen ou alpha nul (p. 4, 21, 22) |
| `multiple testing` | p. 1 (2), 4 (2), 5 (2), 17, 21, 23, 31 (3), 33, 34 (2) | comparaison de méthodes de multiplicité à horizon fixe ; références |
| `false discovery` | p. 4 (2), 5, 17 (4), 18 (2), 19, 20, 28, 31 (6), 33, 34 (3), 40 | trois contrôles comparés (Benjamini et Yekutieli, théorème 1.3, à 1 % ; Storey à 10 % ; Romano et Wolf à 5 % et 5 %), chacun estimé chaque année sur 20 ans de données (p. 17) |
| `Bonferroni`, `Holm` | aucune | rien |
| `pre-regist`, `preregist`, `pre-commit`, `precommit`, `commit` | aucune | rien |
| `hash`, `seal` | aucune | rien |

Termes ajoutés pour durcir les absences qui arrangent la revendication (R8) :

| terme | pages | ce que donne le terme |
|---|---|---|
| `language`, `language model`, `LLM`, `GPT`, `agent`, `artificial`, `neural`, `hypothes` | aucune | aucun modèle de langue, aucun agent |
| `machine learning` | p. 13 | comparaison générique de transparence (« Unlike many big data and machine learning methods, empirical Bayes has a transparent intuition. ») |
| `prior` (mot isolé), `priors`, `posterior` | aucune | le texte parle de *probability model* (p. 7) et de performance latente (p. 10), jamais de *prior* |
| `regress`, `increment`, `beyond`, `correlat`, `redundan`, `novel` | aucune | aucun test d'apport au-delà du publié, aucune mesure de redondance avec le publié |
| `prospective`, `frozen`, `freeze`, `pre-specif`, `ex ante`, `in advance` | aucune | aucun gel ni engagement préalable dit |
| `real time`, `real-time` | p. 2, 5, 11, 12, 33 | construction sans biais d'anticipation dans un rejeu historique (p. 2, 5, 11, 12) ; titre de Marrow et Nagel (2024) dans les références (p. 33, paraphrase) |
| `look-ahead` | p. 1, 3, 11 | même sens |
| `alpha` | p. 4, 6, 22, 25, 31, 42 | mesure de performance possible (p. 6) ou nul à zéro (p. 4, 22) ; p. 25 et 42 : ordre alphabétique ; p. 31 : titre |
| `factor` | p. 12, 19, 20, 32 (2) | zoo des facteurs (p. 12), facteur constant d'un algorithme (p. 19-20), titres (p. 32) : aucun modèle de facteurs comme contrôle |
| `Fama` | p. 13 (2), 32, 44 | prédicteurs connus en 1993, cités pour dire que les meilleures stratégies fouillées en sont loin (p. 13 ; note de la table 3, p. 44) |
| `rolling` | p. 4, 16 (et p. 31, fin de mot : *controlling*) | fenêtre roulante de 20 ans |

## 3. Lecture par composante

### P — juger une proposition contre ce qui est déjà connu, pas contre *aucun effet*

**Statut : voisin (lointain).**

- **Chaque signal est jugé contre aucun effet.** « In essence, EB measures the distance between the empirical t-stat distribution and the standard normal null. » (p. 3) ; « Null strategies are, typically, those with an actual performance of zero. » (p. 21) ; le nul usuel est dit tel : « using the standard null, that the mean long-short return (or alpha) is zero » (p. 4). La mesure retenue est le rendement brut, non un alpha sur des facteurs connus : « We select as our performance measure the t-statistic on the raw long-short return » (p. 10), alors que l'alpha est nommé comme mesure possible (« let r i be a performance measure for strategy i (e.g. mean return, alpha) », p. 6). Le rétrécissement va vers zéro : « rigorous mining involves shrinking performance » (p. 13), et, sans prévisibilité, « all r i are shrunk to zero » (p. 13). Les légendes des figures 2 et 3 (p. 36, 37, paraphrase) disent que les statistiques testent une espérance de rendement nulle et que le nul tracé est la loi normale centrée réduite.
- **Le publié n'entre qu'en repère de la méthode, au niveau d'un portefeuille.** « For comparison, we also examine a portfolio that equally-weighs published strategies from the Chen and Zimmermann (2022) dataset. » (p. 11) ; « Over the full 1983-2020 sample, the top 1% portfolio earns 5.70% per year, compared to the 5.88% return from published strategies. » (p. 11) ; le résumé dit la même chose : la méthode « matches the out-of-sample performance of top journals while eliminating look-ahead bias » (p. 1). La comparaison porte sur un **niveau** de performance (rendement, ratio de Sharpe), non sur un **gain au-delà** du publié : aucune régression des stratégies fouillées sur les stratégies publiées, aucun test d'apport (section 2 : `regress`, `increment`, `beyond`, `encompass`, `correlat` absents).
- **Distance au connu, descriptive seulement.** « Panel B of Table 3 shows that many of the top 1% strategies are quite far from the predictors noted in the academic literature. » (p. 13) ; « the top 20 strategies according to predicted Sharpe ratios using data available in 1993 have themes rarely seen in academic journals » (p. 3). Une liste, pas une statistique.
- **Le connu est tenu hors de la construction, pour les stratégies de rendements passés (annexe A.2).** « we want to ensure that our methods do not incorporate knowledge that would come from reading finance publications » (p. 24) ; « A key feature of these strategies is that they are not selected based on having notable historical returns. Instead, they are constructed to systematically explore various types of data. » (p. 6).
- **Pourquoi voisin et non non trouvé (R4).** Le principe *comparer à ce qui est publié* est présent, mais pour juger la **méthode de fouille** dans son ensemble (un portefeuille contre un portefeuille), jamais pour juger une proposition. Lu au sens non flatteur, c'est un voisin ; ce n'est pas P.

### (i) — proposeurs modèles de langue

**Statut : non trouvé.**

- Les propositions sont une **énumération combinatoire systématique** : ratios et variations de 240 variables comptables, moments de rendements trimestriels passés, groupes de symboles boursiers (annexe A, p. 24-25 ; table 1, p. 42, paraphrase) ; « We apply empirical Bayes (EB) to mine data on 136,000 long-short strategies constructed from accounting ratios, past returns, and ticker symbols. » (p. 1).
- Aucun terme de modèle de langue, d'agent ou d'hypothèse (section 2). Proposition automatique à haut débit, non langagière : hors de (i).

### (ii) — nul formé d'une mise en commun ajustée des lois prédictives de l'archive

**Statut : voisin (lointain).** Les deux moitiés de (ii) sont présentes, chacune séparément, et aucune ne forme un nul.

- **Mise en commun ajustée, mais des candidats, non de l'archive, et comme a priori, non comme nul.** « The latent performance is a mixture of two normals that depends on the strategy family » (p. 10), estimée « using quasi-maximum likelihood » (p. 10) ; « This estimation is done using the past 20 years of long-short returns, separately for each “forecasting year” spanning 1983-2019. » (p. 10) ; « This is a hierarchical structure, where the strategy family determines the actual performance, which in turn determines the measured performance. » (p. 8). Cette loi sert à retirer la chance de l'estimation (« Rigorous data mining means conditioning interesting results on the fact that they come from searching through data. », p. 2), le nul restant la loi normale centrée réduite (p. 3, 13). Elle est ajustée sans théorie : « We will not use economic theory to determine the probability model, and thus our search is largely atheoretical. » (p. 7).
- **Archive mise en commun, mais à poids égaux et comme repère, non ajustée et non nul.** « compared to the mean return of 5.9% per year found by averaging the 200 published strategies from Chen and Zimmermann (2022) » (p. 2) ; table 2 (p. 43, paraphrase) : deux portefeuilles à poids égaux des stratégies publiées (toutes dates ; publiées avant 2004). Variante : « if we focus on strategies in top journals that were published pre-2004, the performance is very similar to the EB-mined strategies » (p. 11).
- **Lu au sens non flatteur (R4).** La loi latente ajustée par famille est une forme de *ce que l'on sait déjà de la population* ; mais elle porte sur la distribution des effets des candidats, non sur des lois prédictives connues du rendement, et elle ne sert pas de nul. Je ne la porte pas plus haut que *voisin (lointain)*.
- **À voir ailleurs.** La pièce rapporte que d'autres appliquent Bayes empirique **à l'archive des anomalies publiées** : « This result is consistent with Chen and Zimmermann (2020), who find shrinkage of only 12% for published anomalies, which are largely equal-weighted and based on accounting variables. » (p. 15) ; « Chen and Zimmermann (2020); Chen and Velikov (2022); and Jensen, Kelly, and Pedersen (2023) recommend empirical Bayes shrinkage. » (p. 5). Un a priori formé de l'archive y est possible ; non lu (section 7), non opposable à ces travaux (R7).

### (iii) — e-processus, ou statistique à validité à tout instant d'arrêt, comme règle de promotion

**Statut : non trouvé.**

- **La règle de promotion est un classement.** « Each year, we sign strategies to have positive predicted returns, and then form portfolios that equally-weight strategies in the top X % of predicted Sharpe ratios. » (p. 11) ; « Our data-mined portfolio is the simple average of the top 1% of strategies, based on EB-predicted Sharpe ratios. » (p. 2). Un seuil de rang, sans test ni garantie.
- **Les contrôles de multiplicité comparés sont à horizon fixe.** « For each year and each strategy family, we apply these methods using the past 20 years of data to estimate a t-statistic hurdle. » (p. 17). Garanties sur le taux et la proportion de fausses découvertes (p. 18-22), aucune validité à tout instant d'arrêt.
- **La répétition annuelle n'est pas une procédure séquentielle garantie** : fenêtre roulante de 20 ans ré-estimée chaque année (« Our EB predictions are constructed using a simple 20-year rolling window, and thus fail to account for this break. », p. 4).
- Termes `e-value`, `e-process`, `martingale`, `optional stopping`, `sequential`, `likelihood ratio`, `Bayes factor` : aucune occurrence ; `anytime` et `stopping` : faux amis (section 2).

### (iv-a) — prédictions engagées (scellées) avant que les données existent

**Statut : voisin (lointain).**

- **Sans biais d'anticipation, dans un rejeu historique.** « our strategies can be constructed using only information available in real time » (p. 2) ; « unlike the EB-mined strategies, which are formed using only information available in real-time, the published strategies contain look-ahead bias » (p. 11) ; détention d'un an après l'estimation : « Finally, we form a portfolio that equally-weighs strategies in each group and hold for one year » (p. 15). C'est le même souci que (iv-a) (ne prédire qu'avec le passé), simulé sur des données qui existaient.
- **Les données existaient au moment de l'analyse.** « It earns out-of-sample returns of 5.7% per year over the 1983-2020 sample » (p. 2), et « First posted November 2023. » (p. 1). Aucune prédiction n'est faite avant que les données existent ; aucun engagement, aucun scellement, aucune empreinte (section 2).
- **Contre la revendication de gel, au sens non flatteur (R4) : le dispositif a changé d'une version à l'autre.** « Results that mine data following Yan and Zheng (2017) and Harvey (2017) are similar and can be found in the first draft of our paper on arxiv.org or via our github site. » (p. 6) ; « Earlier versions of our paper use Yan and Zheng’s method and found similar results. » (p. 24) ; « Earlier versions of our paper used Harvey’s method and found similar results. » (p. 25). Les auteurs disent les résultats semblables ; le contraire d'un engagement figé n'en est pas moins écrit.

### (iv-b) — statistique calculée hors des agents

**Statut : voisin, au sens trivial.**

- Il n'y a **aucun agent**. Les propositions sont énumérées (p. 6, 24-25) ; la loi latente, les prédictions et le classement sont calculés par le programme des auteurs : « We construct the quasi-likelihood using the distr package in R (Ruckdeschel et al. (2006)) and optimize using the BOBYQA algorithm in the nloptr package » (p. 26).
- La séparation entre proposeur et juge est donc acquise par construction, sans agent à tenir à l'écart. Un cas semblable (ATLAS) a été noté *sans objet* dans la table des pistes de priorité haute ; je retiens *voisin*, sens non flatteur (R4), et laisse le libellé à Lazar (nœud 4). Code non lu : la séparation n'est établie que sur le PDF.

### Conjonction

**Non trouvée dans la pièce, lue en entier.** Aucune proposition de modèle de langue ; nul à zéro, non formé de l'archive ; règle de rang, sans validité à tout instant d'arrêt ; rejeu historique sans engagement. CHENDIM est l'exemple type du juge *contre zéro, corrigé de la sélection*, avec un repère publié au niveau de la méthode : utile comme contraste, il ne déplace pas le verdict *occupée en partie*.

## 4. Réponses aux questions

1. **Les signaux sont-ils jugés contre ce qui est publié ou connu, ou contre zéro ?** Contre zéro. Statistique de Student sur le rendement brut (p. 10), nul de la loi normale centrée réduite (p. 3, 13, 14 ; figures 2 et 3, p. 36-37, paraphrase), rétrécissement vers zéro (p. 13). Le publié n'est qu'un repère de performance d'un portefeuille (p. 1, 2, 11 ; table 2, p. 43, paraphrase) et une distance descriptive (p. 3, 13). Les candidats ne sont pas choisis sur leurs rendements passés (p. 6), et la construction des stratégies de rendements passés est voulue sans savoir tiré des publications (p. 24).
2. **Le cadre forme-t-il un nul ou un a priori à partir de l'archive ?** Non. Il forme un a priori : la loi latente, mélange de deux lois normales par famille, ajustée par quasi-vraisemblance sur les 20 années passées **des stratégies fouillées elles-mêmes**, dans six familles (p. 8, 10). Le portefeuille des stratégies publiées est un objet à part, de comparaison (p. 11). Que des ratios énumérés coïncident par construction avec des signaux publiés n'est ni dit ni exclu par le texte lu (R4) ; ils n'y entreraient alors que comme candidats, non comme lois connues. Le nul est la loi normale centrée réduite, non formé de l'archive. Les travaux cités qui appliquent Bayes empirique à des anomalies publiées (p. 5, 15) ne sont pas lus.
3. **Y a-t-il des modèles de langue, une validité à tout instant d'arrêt, un engagement avant les données ?** Non, non, non, dans le PDF lu en entier : propositions énumérées et aucun terme de modèle de langue (p. 1, 6, 24-25 ; section 2) ; règle de rang annuelle et contrôles de multiplicité à horizon fixe (p. 2, 11, 17-22) ; rejeu historique sur des données qui existaient, avec des méthodes changées d'une version à l'autre (p. 1, 2, 6, 24, 25).
4. **Remarque hors question.** La pièce plaide **contre** les contrôles de multiplicité prudents en usage en finance (« Multiple testing methods popular in finance fail to identify most out-of-sample performers. », p. 1 ; « The ideal approach remains an unsettled question. », p. 17). Cela ne touche pas O4. Mais si notre juge revendique une garantie d'erreur, cette pièce est un contradicteur à citer sur le prix de la prudence.

## 5. Table de la pièce

| composante | CHENDIM, arXiv 2311.10685 v3 | preuve, pages du PDF |
|---|---|---|
| **P** | **voisin (lointain)** : le publié est un repère de performance de la méthode (portefeuille contre portefeuille), jamais le nul d'une proposition ; chaque signal est jugé contre zéro | 1, 2, 3, 4, 10, 11, 13, 21, 24 ; 36-37 et 43, paraphrase |
| **(i)** | **non trouvé** : énumération combinatoire non langagière | 1, 6, 24-25 ; 42, paraphrase |
| **(ii)** | **voisin (lointain)** : loi latente ajustée (quasi-vraisemblance) sur les candidats, servant d'a priori ; archive mise en commun à poids égaux, servant de repère ; ni l'une ni l'autre n'est un nul | 2, 7, 8, 10, 11, 15 ; 43, paraphrase |
| **(iii)** | **non trouvé** : règle de rang (1 % du haut) ; contrôles de multiplicité à horizon fixe ; aucun terme séquentiel | 2, 4, 11, 17-22, 27 |
| **(iv-a)** | **voisin (lointain)** : rejeu sans biais d'anticipation (fenêtre de 20 ans, détention d'un an), sur des données existantes ; méthodes changées d'une version à l'autre ; aucun engagement ni scellement | 1, 2, 6, 11, 15, 24, 25 |
| **(iv-b)** | **voisin, au sens trivial** : aucun agent ; calcul par le programme des auteurs (PDF seul) | 6, 26 |
| **conjonction** | **non trouvée** | toute la pièce |

## 6. Nœuds pour Lazar (décisions à prendre ; rien n'est déclaré libre)

Le verdict en vigueur sur O4 reste *occupée en partie* ; seul Lazar le change. Les options prudentes (R4) sont indiquées ; ce ne sont pas des conclusions.

1. **Classement de CHENDIM.** Porter CHENDIM dans la note d'englobement comme *voisine lointaine* de P, de (ii) et de (iv-a) : juge contre zéro, corrigé de la sélection par une loi latente ajustée sur les candidats ; publié seulement en repère de la méthode ; rejeu sans biais d'anticipation, sans engagement. Elle ne change pas le verdict. Option prudente : l'ajouter, citée, comme contraste ; elle ferme la piste *Chen et Dim* du nœud 9 de la note des pistes de priorité haute (v3), sous la réserve du point 5.
2. **Pistes nouvelles nommées par la pièce, qui pourraient toucher la conjonction** (rapportées par CHENDIM seulement, contenu non lu, non opposable : R7) :
   - pour (ii), un a priori formé de l'archive : Chen et Zimmermann (2020), Bayes empirique sur des anomalies publiées (p. 15 ; référence p. 32) ; Jensen, Kelly et Pedersen (2023) et Chen et Velikov (2022), qui recommandent le rétrécissement de Bayes empirique (p. 5 ; références p. 32-33) ;
   - pour (iii) et (iv-a) : Marrow et Nagel (2024), document de travail, découverte et suivi en temps réel d'anomalies de rendements passés par Bayes empirique (« More recently, Marrow and Nagel (2024) use empirical Bayes to study past return signals, with a focus on signal interactions and optimal weighting of more recent data. », p. 5 ; titre p. 33, paraphrase) ;
   - pour P : Chen, Lopez-Lira et Zimmermann (2022), arXiv 2212.10317 (référence p. 31), déjà nommée par la note des pistes de priorité haute (nœud 9), sur la théorie publiée face à la fouille (« recent empirical evidence finds this method is ineffective, even for theories published in top finance journals (Chen, Lopez-Lira, and Zimmermann (2022)) », p. 2).

   Option prudente : verser et faire lire Marrow et Nagel (2024) et Chen et Zimmermann (2020) avant toute phrase publique sur (ii) ou sur (iii). Aucun accès réseau ici : demande à Lazar.
3. **Défaut du programme de rejeu des citations** (section 8, incident 1). Le programme gelé découpe le texte entier sur le caractère de saut de page. Un PDF dont une page de figure contient ce caractère voit donc ses pages suivantes mal numérotées. Deux conséquences : une citation donnée à sa vraie page échoue ; une citation alignée sur la numérotation du programme passe, **à une page fausse**. Décisions : faire contrôler par un lecteur neuf les rejeux déjà versés sur des PDF à figures (pages données contre l'extraction page à page) ; écrire, sous un nom neuf (R12), un programme de rejeu qui numérote par extraction page à page, sans toucher au programme gelé. Option prudente : les deux, avant la prochaine contre-lecture des notes de O4.
4. **Libellé de (iv-b) quand il n'y a aucun agent.** *voisin, au sens trivial* (retenu ici, R4) ou *sans objet* (choisi pour ATLAS) : fixer une règle pour toute la table.
5. **Version citée.** La v3 (juin 2025) est lue. La note des pistes de priorité haute dit que NMV cite *Chen et Dim (2024)* : la version visée n'est pas établie ici, et les versions antérieures construisaient autrement les stratégies de rendements passés et de symboles (p. 6, 24, 25). Option prudente : citer la v3, avec son numéro de version.

## 7. Ce qui reste non lu

- **Code de réplication** (adresse p. 1) : non lu, non cloné, non cherché (consigne : proportion). Les statuts reposent sur le PDF seul. En particulier, que le portefeuille publié n'entre pas dans l'ajustement de la loi latente est ce que le texte décrit (p. 10, 11), non vérifié dans le code ; le recouvrement possible entre ratios énumérés et signaux publiés n'est pas mesuré.
- **Données des stratégies** (site de l'auteur, p. 1) : non lues.
- **Versions antérieures** de l'article (première mise en ligne en novembre 2023, p. 1 ; premier brouillon cité p. 6, 24, 25) : non lues.
- **Graphiques des figures** (p. 28, 35-41) : non lus ; légendes seules.
- **Fichier de provenance** du dossier du PDF (`provenance-v1.md`) : vu dans la liste du dossier, non lu (non nommé par la consigne).
- **Références de la pièce qui pourraient toucher la conjonction** (contenu non lu ; ce que la pièce en dit est rapporté en section 6, nœud 2) :
  - Chen et Zimmermann (2020), revue d'études d'évaluation des actifs, sur le biais de publication (référence p. 32 ; cité p. 5, 15) : (ii) ;
  - Jensen, Kelly et Pedersen (2023), sur la crise de réplication en finance (référence p. 33 ; cité p. 5) : (ii) ;
  - Chen et Velikov (2022), sur les rendements espérés des anomalies (référence p. 32 ; cité p. 5) : (ii) ;
  - Marrow et Nagel (2024), document de travail (référence p. 33 ; cité p. 5) : (iii), (iv-a) ;
  - Chen, Lopez-Lira et Zimmermann (2022), arXiv 2212.10317 (référence p. 31 ; cité p. 2, 5) : P ;
  - Yan et Zheng (2017), fouille de données comptables (référence p. 34 ; cité p. 5 : « We add to Yan and Zheng (2017) and Chen, Lopez-Lira, and Zimmermann (2022), who document that mining accounting data can produce substantial out-of-sample returns. ») : P, lointain ;
  - Chen (2024a), sur les seuils des statistiques de Student (référence p. 31 ; cité p. 4 : « A brief explanation of why Benjamini and Yekutieli (2001) Theorem 1.3 is excessively conservative is found in Section 2.5 of Chen (2024a). ») et Chen (2024b), arXiv 2206.15365, sur la vérité des résultats publiés (référence p. 31 ; cité p. 19 : « see also Chen 2024b ») : multiplicité, (iii) lointain ;
  - Harvey, Liu et Zhu (2016) : déjà lue (HLZ, voisine, note d'englobement) ;
  - Barras, Scaillet et Wermers (2010), Storey (2002), Romano et Wolf (2005, 2007), Benjamini et Yekutieli (2001) : outils de multiplicité à horizon fixe, d'après leur usage dans la pièce (p. 17-22) ; non lus.

## 8. Incidents

1. **Décalage de pages dans le programme de rejeu gelé.** Dans l'extraction page à page, les pages 28, 38, 39 et 40 (figures dont le texte sort en glyphes) contiennent chacune un caractère de saut de page en plus de celui de fin de page. Le texte entier se découpe donc en 49 segments pour 44 pages, et le programme décale d'un cran les pages suivantes à chaque fois (de +1 après la page 28 à +4 après la page 40). Premier essai : 56 citations sur 69 trouvées à la page dite ; les 13 échecs étaient tous aux pages 31 à 44, et chacun avait été trouvé à sa vraie page plus 1 à 4. **Mesure prise** : programme non modifié ; citations entre guillemets restreintes aux pages 1 à 27 ; rejeu final 66 sur 66 ; contrôle croisé de ma part sur l'extraction page à page, en complément et non en remplacement : 66 sur 66 à la vraie page sur la liste finale (pages 1 à 27). Les éléments des pages 28 à 44 sont paraphrasés, sans guillemets, à leur vraie page. Nœud 3.
2. **Listes hors des fichiers nommés**, déclarées : `ls -la` du dossier du PDF nommé (il montre le PDF, son compagnon `.sha256` et `provenance-v1.md` avec son compagnon ; ce dernier n'est pas lu) ; une liste du dossier des notes **filtrée sur le seul nom de la pièce**, pour vérifier qu'aucun fichier de même nom n'existait avant écriture (R12 ; aucun résultat) ; `git status --short` et `git log --oneline -1` (arbre propre, branche `lot/compte-organisme-v1`) ; liste du dossier des clones (six dossiers, aucun pour cette pièce). Aucun autre fichier du dépôt n'a été lu que ceux que la consigne nomme.
3. Aucun refus de permission, de crochet ou de classifieur. Aucun accès réseau, aucune dépense, aucune machine, aucun programme des clones lancé.
