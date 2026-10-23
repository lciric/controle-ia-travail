BASSIN_MATH: Price-Adaptive-Speciation-Coevolution-Swarm (PASCS)
LOI_PROPOSEE: L'allocation du budget suit l'équation de Price covariante couplée à une bifurcation évolutive (Adaptive Dynamics) où les chercheurs subissent une spéciation disruptive forcée par un système immunitaire parasite (`jev-1.14.0`).

1. **Loi d'apprentissage & d'auto-organisation hors-poids (PASCS)** :
L'essaim maintient une population de génotypes épistémiques $x_i$ (paires de sous-graphes bibliographiques + opérateurs logiques hors-poids). L'allocation du budget $p_i$ (20$ Gemini = mutateur de graphes ; 100$ Claude = recombinaison méiotique et formalisation causale) obéit à l'équation de Price : $\Delta \bar{z} = \frac{1}{\bar{w}}\text{Cov}(w_i, z_i) + \frac{1}{\bar{w}}\mathbb{E}[w_i \Delta z_i]$.
Le système immunitaire parasite est incarné par une population infinie de sondes `jev-1.14.0` gratuites qui apprennent en continu le répertoire antigénique des analogies triviales $y_k$. La fitness d'invasion d'un mutant $x'$ dans l'environnement résident $(x, y)$ est $s_x(x') = f(x', x) - \sum_k \alpha(x', y_k)$. Lorsque le gradient de sélection s'annule ($\nabla_{x'} s_x(x')|_{x'=x} = 0$) mais que la courbure hessienne est positive ($\frac{\partial^2 s_x(x')}{\partial x'^2} > 0$), l'essaim atteint un point de branchement évolutif : le prompt-génotype est scindé en deux lignées orthogonales (spéciation). Les API gratuites pré-filtrent $10^6$ trajectoires de citations ; `jev-1.14.0` élimine à coût zéro toute mutation capturée par le bassin d'attraction résident avant d'invoquer Gemini/Claude.

2. **Fonction objectif anti-vernis** :
La fitness $w_i$ d'un pont entre silos $A$ et $B$ est définie par :
$$w_i(A,B) = d_{\text{phylo}}(A,B) \cdot \exp\left(-\max_k \text{Sim}_{\text{jev}}(x_i, y_k)\right) \cdot \mathcal{I}_{\text{do}}(H_A \perp H_B)$$
où $d_{\text{phylo}}(A,B)$ est le temps de coalescence minimal dans le graphe de citations (pénalisant les ancêtres communs récents), le second terme est l'échappement immunitaire mesuré par `jev-1.14.0` contre le vernis sémantique, et $\mathcal{I}_{\text{do}}$ est la divergence de Jensen-Shannon entre les distributions interventionnelles prédites par $H_A$ et $H_B$ sur les activations de Llama-3.1-8B/70B.

3. **Exemple concret de pont
