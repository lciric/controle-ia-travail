Écrit le dim. 22 nov. 2026, 14:44 UTC (`date -u`). Classe C (travail). Vérification selon R7.

# Vérification sur PDF : Dwork, Feldman, Hardt, Pitassi, Reingold et Roth, 2015, « le jeu de validation réutilisable »

## Référence visée
Dwork C., Feldman V., Hardt M., Pitassi T., Reingold O., Roth A. (2015). « The reusable holdout: Preserving validity in adaptive data analysis ». *Science* 349 (6248), p. 636-638, DOI 10.1126/science.aaa9375.

## Ce qui a été obtenu, et ce qui ne l'a pas été
- **Article de Science, version de l'éditeur ou version auteur : non obtenu.** Le PDF de science.org renvoie une erreur 403 (accès payant, non contourné). Unpaywall classe le DOI « closed », sans copie de dépôt (`has_repository_copy: false`). La page de l'article chez Aaron Roth (cis.upenn.edu/~aaroth/reusable.html) ne renvoie qu'au site de Science. Les recherches n'ont donné aucune version auteur libre. Les énoncés ci-dessous ne s'appuient donc **pas** sur le texte de Science. Il faut citer les versions arXiv, ou obtenir l'article de Science par un accès institutionnel.
- Un PDF « Guilt Free Data Reuse » (résumé étendu, site de T. Pitassi) a été trouvé puis écarté. Il se présente comme une synthèse des deux papiers techniques, pas comme l'article de Science, et il n'est pas versé.

## Pièces versées
| Pièce | Ce que c'est | Provenance | Chemin | Empreinte sha256 |
|---|---|---|---|---|
| A | Version longue, « Generalization in Adaptive Data Analysis and Holdout Reuse », arXiv 1506.02629v2 (25 sept. 2015), 29 p. Version NeurIPS 2015 longue. | https://arxiv.org/pdf/1506.02629v2 | `docs/sources/pdf-puits-etroits-v1/dwork-et-al-2015-generalization-holdout-reuse-arxiv-1506.02629v2-v1.pdf` | `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71` |
| B | « Preserving Statistical Validity in Adaptive Data Analysis », arXiv 1411.2664v3 (2 mars 2016), 29 p. Version STOC 2015. | https://arxiv.org/pdf/1411.2664 | `docs/sources/pdf-puits-etroits-v1/dwork-et-al-2015-preserving-statistical-validity-arxiv-1411.2664v3-v1.pdf` | `6e9532a978ae5d498722eb95f1a13332f24d1eb09c1791f56fd9aa3eb310d697` |

`file` reconnaît les deux comme des PDF. Pour A, `file` indique « 4 page(s) » par erreur de métadonnée ; `pdfinfo` compte 29 pages. Chaque pièce a son compagnon `.sha256`.
Licence : vérifiée sur les pages arXiv des deux pièces, licence arXiv non exclusive de distribution 1.0 (`arxiv.org/licenses/nonexclusive-distrib/1.0/`). Elle autorise la lecture et l'archivage privé, pas la redistribution publique.
Lecture : pdftotext (texte en mise en page). Les pages citées sont celles du PDF, qui coïncident avec les numéros imprimés en pied de page.

## Pages et citations

### (1) L'analyse adaptative sur un même jeu invalide les garanties usuelles
- A, p. 1 (résumé) : « Reusing a holdout set adaptively multiple times can easily lead to overfitting to the holdout set itself. »
- A, p. 2 : « Because the predictor is independent of the holdout dataset, such an estimate is a valid estimate of the true prediction accuracy […]. However, in practice the holdout dataset is rarely used only once, and as a result the predictor may not be independent of the holdout set, resulting in overfitting to the holdout set ». Puis : « such static approaches do not apply if the estimates or hypotheses tested on the holdout are chosen adaptively: that is, if the choice of hypotheses depends on previous analyses performed on the dataset. »
- A, p. 2, le paradoxe de Freedman : « an elegant demonstration of the powerful (negative) effect of adaptive analysis on the same data ».
- B, p. 5 : « For any fixed function ψ, the empirical average ES[ψ] is strongly concentrated around its expectation P[ψ]. However, this statement is no longer true if ψ is allowed to depend on S (which is what happens if we choose functions adaptively, using previous estimates on S). »
- B, p. 6 : « why adaptivity in data analysis invalidates the significance levels of statistical procedures given for the non-adaptive case ».
- B, p. 3 : une seule ronde d'adaptivité suffit à faire diverger la moyenne empirique de l'espérance (« Note that this requires only a single round of adaptivity! »).
- **Exemple de surajustement par réutilisation**, A, p. 21, section 5 : les étiquettes sont indépendantes des données, si bien que « no classifier can achieve true accuracy better than 50%. Nevertheless, reusing a standard holdout results in reported accuracy of over 63% for k = 500 on both the training set and the holdout set ». Puis : « Thresholdout prevents the algorithm from overfitting to the holdout set and gives a valid estimate of classifier accuracy. » Cause, même page : « the analyst reuses the holdout after using it to measure the correlation of single attributes ». Le montage : n = 10 000, d = 10 000, 100 exécutions.

### (2) Ce que coûte un jeu réutilisable (Thresholdout)
- A, p. 3, énoncé qualitatif : « The number of queries that Thresholdout can answer is exponential in n as long as the number of times that the analyst overfits is at most quadratic in n. »
- A, p. 15, le budget de dépassements : « Thresholdout is given access to the training dataset St and holdout dataset Sh and a budget limit B » ; « Each time the difference is above threshold the "overfitting" budget B is reduced by one. Once it is exhausted, Thresholdout stops answering queries. »
- A, p. 15, lemme 23 : « Thresholdout satisfies (2B/(σn), 0)-differential privacy ».
- A, p. 17, théorème 25. Avec T = 3τ/4 et σ = τ/(96 ln(4m/β)), Z_i compte les requêtes j ≤ i telles que |P[φj] − E_St[φj]| > τ/2. On a alors P[∃i ∈ [m], Z_i < B et |a_i − P[φ_i]| ≥ τ] ≤ β dès que n ≥ O( ln(m/β)/τ² · min{B, √(B ln(ln(m/β)/τ))} ). La formule est transcrite depuis la mise en page de pdftotext et doit être relue sur le PDF avant d'être citée mot pour mot.
- A, p. 19 : « this bound allows m to be exponentially large in n as long as B grows sub-quadratically in n (that is, B ≤ n^(2−c) for a constant c > 0). » Le terme ln(m/β)/τ² est celui du cas non adaptif.
- A, p. 5, la limite générale : « no efficient algorithm can answer more than quadratically many statistical queries chosen adaptively by an adversary who knows the true data distribution » (résultat attribué à Hardt et Ullman et à Steinke et Ullman).

### (3) Un jeu frais, non vu par l'analyste, garde sa validité
- A, p. 1 : l'hypothèse usuelle veut que chaque procédure « operates on a freshly sampled dataset – or if not, is validated on a freshly sampled holdout (or testing) set. »
- A, p. 2 : « Because the predictor is independent of the holdout dataset, such an estimate is a valid estimate of the true prediction accuracy (formally, this allows one to construct a confidence interval for the prediction accuracy on the data distribution). »
- B, p. 10 : « If instead φ was evaluated on a fresh dataset T drawn independently of φ, then indeed we would have E ET[φ] = P[φ]. »
- B, p. 2, le coût d'un jeu frais : « The "textbook" advice for avoiding problems of this type is to collect fresh samples […] Following this approach conservatively with m adaptively chosen procedures would significantly (on average by a factor of m) reduce the amount of data available for each procedure. »
- B, p. 3 : avec des échantillons frais par requête, le coût en échantillons croît « linearly with the number of queries m ». B, p. 19 : « If we knew when these rounds of adaptivity occurred, we could refresh our sample between each round, and obtain total sample complexity linear in the number of rounds of adaptivity. »

## Verdict sur l'appui de la décision
**Confirmée en partie, sur les versions arXiv A et B. Non vérifiable sur l'article de Science lui-même**, faute d'accès.

Ce qui est confirmé : réutiliser un jeu de validation de façon adaptive, c'est-à-dire choisir les analyses suivantes d'après ses réponses, fait perdre la garantie usuelle de concentration et de validité (B p. 5 et 6, A p. 2). Un exemple chiffré montre une précision rapportée de plus de 63 % pour une précision vraie de 50 % (A p. 21). Un jeu frais, indépendant de ce qu'on évalue, reste valide (A p. 2, B p. 10), au prix d'un facteur m en données (B p. 2 et 3). Thresholdout rétablit la validité à un coût chiffré : un budget B de dépassements, et une taille n qui croît en ln(m)·min{B, √B}/τ² (A p. 15, 17 et 19).

Les écarts à corriger dans la phrase d'appui :
1. **« Consomme » est juste au sens d'un budget, pas au sens d'une perte totale.** Les papiers disent que la réutilisation adaptive *peut* surajuster (« can easily lead to », A p. 1) et que les garanties statiques *ne s'appliquent plus*. Ils ne disent pas que chaque usage détruit la validité. Leur thèse centrale va même en sens inverse : on peut guider l'analyse par le jeu de validation sans perdre la validité, si l'on passe par un mécanisme (Thresholdout) et dans la limite d'un budget. La règle « le juge ne guide jamais la recherche en course » est donc un **choix du programme**, prudent et compatible avec les papiers. Elle n'en est pas une conséquence. Pour l'appuyer, il faut écrire que les papiers fondent *pourquoi* il faut séparer ou compter, et non *qu'il faut s'interdire* tout guidage.
2. **Le cadre des théorèmes est étroit.** Ce sont des requêtes statistiques φ : X → [0, 1], estimées sur un jeu tiré indépendamment et identiquement d'une même loi (A p. 17 ; B p. 5). Transposer ce cadre à un « juge statistique » qui n'est pas une moyenne de fonctions bornées sur un échantillon de ce type demande une phrase de réserve.
3. **La citation doit porter le bon titre.** Comme l'article de Science n'a pas été lu, la citation opposable doit renvoyer à arXiv 1506.02629v2 (NeurIPS 2015) et à arXiv 1411.2664v3 (STOC 2015), pages ci-dessus, et non au texte de Science.

## Sources consultées (sans données personnelles dans les requêtes)
- https://arxiv.org/abs/1506.02629 et https://arxiv.org/abs/1411.2664 (pages de dépôt, licences)
- https://www.cis.upenn.edu/~aaroth/reusable.html (page de l'article ; seul lien vers Science)
- https://www.science.org/doi/pdf/10.1126/science.aaa9375 (403, non contourné)
- api.unpaywall.org pour le DOI 10.1126/science.aaa9375 (« closed »)
- https://research.google/blog/the-reusable-holdout-preserving-validity-in-adaptive-data-analysis/ (billet de blogue, non utilisé comme appui)
