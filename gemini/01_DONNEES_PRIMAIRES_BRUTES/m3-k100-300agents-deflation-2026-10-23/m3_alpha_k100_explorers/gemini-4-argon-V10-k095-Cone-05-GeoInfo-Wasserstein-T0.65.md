BASSIN_MATH: Courbure-Affine-Nagaoka-Benamou-Brenier-CramerRao-Swarm (CANBB-CRS)
LOI_PROPOSEE: $\dot{\rho}_t = -\nabla_{W_2}^G \mathcal{A}_{BB}(\rho_t) + \eta \tilde{\nabla}_{\mathcal{I}_{FR}} \det(\text{Cov}_{jev}(\theta_t) - \mathcal{I}_{FR}^{-1}(\theta_t))$ via minimisation d'action cinétique sur variété statistique d'Efron-Nagaoka.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Soit le graphe de citations $G=(V,E)$. Les embeddings de `jev-1.14.0` (gratuit/illimité) paramètrent une sous-variété statistique $\mathcal{M}_\theta$ plongée dans le simplexe des distributions sur $V$. L'allocation de masse d'attention $\rho_t \in \mathcal{P}(V)$ évolue sans mise à jour de poids via la formulation fluide de **Benamou-Brenier** sur graphe : $\mathcal{A}_{BB}(\rho, v) = \int_0^1 \sum_{e \in E} \frac{\|v_t(e)\|^2}{\hat{\rho}_t(e)} dt$ sous contrainte d'advection $\partial_t \rho_t + \text{div}_G(\hat{\rho}_t v_t) = 0$.
L'essaim calcule hors-ligne via `jev-1.14.0` la **courbure de plongement d'Efron-Nagaoka** $\stackrel{(\alpha)}{H}_{ij}^\kappa$ (deuxième forme fondamentale de $\alpha$-connexion d'Amari) des trajectoires de citations.
- **Allocation budgétaire** : 0 USD pour l'exploration globale (calculée par `jev-1.14.0` qui estime la matrice d'information de Fisher-Rao $\mathcal{I}_{FR}(\theta)$ par perturbations d'entrées).
- **Déclenchement LLM** : Les 20 USD (Gemini) et 100 USD (Claude) sont déclenchés uniquement lorsque l'excès de variance par rapport à la **borne de Cramér-Rao riemannienne** $\text{Tr}(\mathcal{I}_{FR}(\theta)\text{Cov}_{jev}) \gg \dim(\Theta)$ coïncide avec un col de vitesse Benamou-Brenier $\|v_t(e)\|$ maximal entre deux amas disjoints. Gemini synthétise les ponts locaux ; Claude résout les singularités à haute courbure d'Efron $\|\stackrel{(1)}{H}\|_{FR}$.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(\theta, \rho) = \mathcal{A}_{BB}^{\min}(\rho_A, \rho_B) \times \left\| \stackrel{(-1)}{H}_{AB}^\perp \right\|_{\mathcal{I}_{FR}}^2 \times \det\left(\mathcal{I}_{FR}(\theta \mid H_A) - \mathcal{I}_{FR}(\theta \mid H_B)\right)^2$$
Où $\mathcal{A}_{BB}^{\min}(\rho_A, \rho
