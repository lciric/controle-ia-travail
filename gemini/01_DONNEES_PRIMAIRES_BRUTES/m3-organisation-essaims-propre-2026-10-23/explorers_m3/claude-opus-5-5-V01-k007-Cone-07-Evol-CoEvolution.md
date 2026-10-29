BASSIN_MATH: Reine-Rouge-Price-Elites (RRPE)

LOI_PROPOSEE: $\dot{x}_i=\sum_j x_j\,\tilde f_j\,Q_{ji}-x_i\bar{\tilde f}$, avec $\tilde f_j=f_j(\mathbf{y})/c_j$, sous $\sum_i x_i c_i^{C}\le100$ et $\sum_i x_i c_i^{G}\le20$. Les parasites suivent $\dot{y}_k=y_k(g_k(\mathbf{x})-\bar g)$.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**
Un génotype $i=(\text{prompt},\text{famille},\text{rôle},\text{arêtes},\text{profondeur})$ décrit un agent. L'évolution porte sur les consignes et la topologie, jamais sur les poids.
- **Mutateur $Q$** : réécriture de la consigne, ajout ou retrait d'arête, changement de famille. La mutation vers une autre famille, qui produit une chimère, est biaisée par l'équation de Price : $\Delta\bar z=\frac{\mathrm{Cov}(w,z)}{\bar w}+\frac{\mathbb E[w\Delta z]}{\bar w}$, où $z$ est la décorrélation inter-familles des erreurs. Si $\mathrm{Cov}(w,z)>0$, la sélection favorise les chimères. Sinon, la monoculture, moins coûteuse, l'emporte. Cette règle traite $H4'$.
- **Red Queen** : les explorateurs (hôtes $x$) affrontent des démolisseurs Red-Team (parasites $y$), avec $g_k$ égal au taux de réfutation vérifiée. Un parasite est engendré quand la valeur d'un hôte stagne, c'est-à-dire quand $\partial_t\bar f<\epsilon$. Un explorateur est engendré quand une niche reste vide.
- **MAP-Elites** : une archive est indexée par les descripteurs (mélange de familles, profondeur de délégation, coût). Chaque cellule conserve son élite. La communication n'est autorisée qu'entre cellules voisines.

2. **Fonction objectif et anti-Goodhart**
$$f_i=\frac{\hat S^{(t)}_{\text{jev}}-\lambda_1\rho_{\text{err}}-\lambda_2 D_{H9}-\lambda_3 R_{\text{mém}}+\lambda_4 N_{\text{MAP}}}{c_i}$$
- $\hat S^{(t)}_{\text{jev}}$ est le score de jev-1.14.0. Le seuil et la rubrique du juge tournent selon une graine cachée à chaque génération, ce qui empêche le surajustement.
- $\rho_{\text{err}}$ est la corrélation des erreurs entre agents.
- $D_{H9}=1-\cos(\text{consigne racine},\text{consigne déléguée})$, calculé par jev.
- $R_{\text{mém}}$ est la fraction d'affirmations non vérifiées via Crossref, Semantic Scholar ou arXiv. Elle mesure la récitation paramétrique.
- $N_{\text{MAP}}$ est la nouveauté mesurée dans l'archive.
- Un sous-ensemble tenu à l'écart, jugé par la famille absente de la tâche, mesure l'écart $\Delta_G=\hat S-S_{\text{tenu}}$. Si $\Delta_G>\delta$, $\lambda_1$ et $\lambda_3$ augmentent.

3. **Duel décisif ($H_A\perp H_B$)**
Le budget est égal pour chaque bras : 25 USD Claude et 5 USD Gemini.
- **A** : RRPE complet.
- **B** : meilleure topologie fixe choisie a priori.
- **C** : configurations tirées de façon i.i.d. dans $Q$ (contrôle négatif).
- **D** : réplicateur dont la fitness est permutée aléatoirement (contrôle négatif de la sélection).

Les bras sont évalués sur des tâches inédites postérieures à la date de coupure, avec une vérification bibliographique objective et un juge aveugle inter-familles.

$H_A$ : $S_A>\max(S_B,S_C,S_D)$, avec $\rho_{\text{err},A}$ plus faible, selon un test bootstrap apparié et $p<0{,}01$ corrigé par Holm.

$H_B$ : l'avantage de A ne vient que du hasard ou du volume d'exploration, ce qui se traduirait par $S_A\approx S_D\approx S_C$. Les deux hypothèses sont orthogonales : D isole l'effet de la sélection, C celui de la diversité aléatoire.

**Critère de réfutation** : si $S_A-S_D<\delta$, ou si $\Delta_{G,A}>\Delta_{G,B}$, la loi RRPE est rejetée.
