BASSIN_MATH: Branchement Dieckmann-Law à Allèles Appariés (BDL-AA)

LOI_PROPOSEE: $\dot{\mathbf x}=\tfrac12\,\mu\,\sigma^2\,\hat n(\mathbf x)\,\nabla_{\mathbf y}s_{\mathbf x}(\mathbf y)\big|_{\mathbf y=\mathbf x}$ ; on scinde la lignée lorsque $\nabla_{\mathbf y}s=0$ et $\partial^2_{\mathbf y\mathbf y}s>0$ le long d'un axe $e$, sous la condition de stabilité de convergence $\partial^2_{\mathbf y\mathbf y}s+\partial^2_{\mathbf x\mathbf y}s<0$.

**1. Mécanisme d'auto-organisation hors-poids**

Chaque essaim est un trait continu $\mathbf x=(f,\rho,\chi,d,\pi)$ :
- $f$ : degré de communication entre agents ;
- $\rho$ : fraction d'agents Red-Team ;
- $\chi$ : fraction chimérique (part Gemini) ;
- $d$ : profondeur de délégation ;
- $\pi$ : allocation de la dépense Claude/Gemini.

Un mutant $\mathbf y=\mathbf x+\varepsilon$ s'exécute sur un mini-lot. Sa fitness d'invasion $s_{\mathbf x}(\mathbf y)$ est mesurée dans l'environnement créé par le résident, c'est-à-dire face aux parasites que le résident a engendrés.

Le trait suit l'équation canonique. Au point singulier, deux cas se présentent :
- **Branchement** (minimum de fitness) : la lignée se scinde en deux sous-essaims spécialisés, un explorateur ($\rho\downarrow$) et un démolisseur ($\rho\uparrow$).
- **Point stable** (maximum) : la topologie est gelée.

L'arbitrage monoculture/chimère suit la même règle : on se branche sur l'axe $\chi$ seulement si la courbure de $s$ y est positive, c'est-à-dire si l'erreur corrélée intra-famille (H4') crée une sélection disruptive.

Les parasites sont des allèles d'attaque $a$, jouant contre les hôtes dans un jeu d'allèles appariés $P(\text{succès})=\exp(-\lVert a-\mathbf x\rVert^2/2\tau^2)$. Ce couplage hôte-parasite engendre la sélection dépendante de la fréquence qui rend le branchement possible.

**2. Fonction objectif et anti-Goodhart**

$$s=\frac{V_{\text{ext}}-\lambda\,\bar r_{\text{err}}-\kappa\,D_{H9}-\eta\,R_{\text{mém}}}{c_{\$}}$$

- $V_{\text{ext}}$ : nombre d'affirmations vérifiées contre Crossref, Semantic Scholar et arXiv (identifiant récupéré et contenu concordant).
- $\bar r_{\text{err}}$ : corrélation moyenne des erreurs entre agents (H4').
- $D_{H9}=1-\text{jev}(\text{consigne racine},\text{consigne feuille})$ : dérive de consigne à travers les délégations.
- $R_{\text{mém}}$ : part des affirmations sans source récupérée (récitation de la mémoire paramétrique).
- $c_{\$}$ : coût d'inférence en dollars.

Garde de Price : on décompose $\Delta\bar s=\mathrm{Cov}(w,s_{\text{jev}})+\mathrm E[w\,\Delta s]$. Si la pente $\mathrm{Cov}(s_{\text{jev}},V_{\text{ext}})/\mathrm{Var}(s_{\text{jev}})$, calculée sur un holdout secret à rubrique tournante, tombe sous $0{,}5$, la sélection est suspendue.

**3. Duel décisif ($H_A\perp H_B$)**

Le budget est identique pour tous les bras (100 USD Claude, 20 USD Gemini), avec 200 tâches et 10 graines.

- **A** : BDL-AA.
- **B** : meilleure topologie fixe issue d'une grille.
- **C (contrôle négatif)** : mutations i.i.d. de même variance $\sigma^2$, mais sélection sur un $s$ permuté aléatoirement.

Hypothèses :
- $H_A$ : le gain vient de la sélection, d'où $s_A>\max(s_B,s_C)$.
- $H_B$ : le gain vient de la seule variation, d'où $s_A\approx s_C$.

Critère : $V_{\text{ext}}/\$$ sur un holdout jamais vu, avec un test de permutation à $\alpha=0{,}01$.

Prédiction falsifiable : $\bar r_{\text{err}}$ chute après le branchement sur $\chi$ uniquement dans le bras A.
