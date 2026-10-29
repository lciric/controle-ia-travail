BASSIN_MATH: Courbure-Forman-Zeta-Ihara-Bockstein (CFZIB)
LOI_PROPOSEE: L'essaim minimise le déterminant spectral de Bass-Ihara sur le complexe cellulaire filtré des citations en injectant des agents uniquement sur les 1-cellules à courbure de Forman-Ricci très négative et obstruction de Bockstein non nulle.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Le graphe bibliographique gratuit (Semantic Scholar/arXiv) est érigé en 2-complexe cellulaire $X_\epsilon$ où le poids filtrant $\epsilon(e) = 1 - \text{jev-1.14.0}(u,v)$ est évalué à coût zéro. La courbure de Forman-Ricci d'une arête inter-études $e$ est calculée hors-poids :
$$\mathcal{F}(e) = \omega(e)\left[\sum_{f > e}\frac{\omega(e)}{\omega(f)} + \sum_{v < e}\frac{\omega(v)}{\omega(e)} - \sum_{\hat{e} \parallel e}\frac{\sqrt{\omega(e)\omega(\hat{e})}}{\max(\omega(f), \omega(v))}\right]$$
Les arêtes hyperboliques ($\mathcal{F}(e) \ll 0$) sans 2-faces adjacentes ($f>e$) signalent des ponts inter-silos critiques non résolus. Le budget API ($20\$$ Gemini pour le criblage syntaxique, $100\$$ Claude pour la synthèse d'hypothèses) est alloué proportionnellement au gradient spectral de la fonction Zêta d'Ihara-Bass $\zeta_X(u)^{-1} = (1-u^2)^{\chi(X)}\det(I - uA + u^2Q)$, en ciblant les cycles premiers non-backtracking qui maximisent l'homomorphisme de Bockstein $\beta_1: H^1(X; \mathbb{Z}_2) \to H^2(X; \mathbb{Z})$ (obstruction à relever une analogie locale en loi causale globale).

2. **Fonction objectif anti-vernis** :
Pour un pont candidat $\sigma = (u,v)$ générant le duel $(H_A \perp H_B)$, le gain est :
$$\mathcal{J}(\sigma) = |\mathcal{F}(\sigma)| \cdot \|\beta_1([\sigma])\|_{H^2} \cdot \det\left(\Delta_1^{\text{up}}\big|_{H_A \oplus H_B}\right) \cdot \mathbb{I}\left(\text{jev}(H_A \wedge H_B) < \tau\right)$$
où $\Delta_1^{\text{up}} = \partial_2 \partial_2^*$ est le Laplacien supérieur de Hodge mesurant l'orthogonalité causale stricte entre les prédictions empiriques de $H_A$ et $H_B$ sur Llama-3.1-8B/70B, et $\text{jev}(H_A \wedge H_B) < \tau$ garantit leur incompatibilité logique (zéro vernis verbal).

3. **Exemple concret de pont inédits
