BASSIN_MATH: Flot-JKO-Fisher-Wasserstein-Chimerique
LOI_PROPOSEE: L'essaim évolue hors-poids en suivant un schéma variationnel de Jordan-Kinderlehrer-Otto (JKO) sur l'espace de Wasserstein des graphes de citations, couplé au gradient naturel d'Amari sur la variété statistique de Fisher-Rao induite par `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Chaque nœud $v \in G$ (article/dépôt) est projeté gratuitement par `jev-1.14.0` sur le simplexe de probabilités $\Delta^K$, formant une variété riemannienne munie de la métrique de Fisher-Rao $g_{ij}(\theta) = \mathbb{E}[\partial_i \ln p(x;\theta) \partial_j \ln p(x;\theta)]$. L'essaim maintient une mesure empirique d'attention $\mu_t \in \mathcal{P}(G)$. À l'étape $t+1$, la distribution des requêtes évolue par flot de gradient de Wasserstein discret (schéma JKO gratuit via `jev-1.14.0`) :
$$\mu_{t+1} = \arg\min_{\mu \in \mathcal{P}(G)} \left\{ \frac{1}{2\tau} W_{2, G}^2(\mu, \mu_t) - \int_{G \times G} \mathcal{J}_{AV}(u,v) d\pi^*(u,v) \right\}$$
où $\pi^*$ est le plan de transport optimal régularisé par entropie (Sinkhorn). L'allocation budgétaire (20\$ Gemini pour l'exploration rapide de sous-graphes, 100\$ Claude pour la synthèse d'invariants boîte blanche/noire) est gouvernée par le gradient naturel d'Amari $\tilde{\nabla}_\theta \mathcal{J}_{AV} = G(\theta)^{-1} \nabla_\theta \mathcal{J}_{AV}$. Les prompts des agents chimériques mutent le long des géodésiques de Fisher uniquement lorsque le transport de Wasserstein détecte une singularité de courbure de Ricci (Ollivier-Ricci $\kappa(u,v) \ll 0$) entre deux silos déconnectés.

2. **Fonction objectif anti-vernis ($\mathcal{J}_{AV}$)** :
Pour une paire $(u,v)$ candidate au couplage chimérique :
$$\mathcal{J}_{AV}(u,v) = d_{FR}(\theta_u, \theta_v) \cdot W_{1, G}(\mu_u, \mu_v) \cdot \det\left(\mathcal{I}_{ Fisher}(H_A \perp H_B)\right) \cdot \exp(-\lambda H_{jev}(\text{vernis}))$$
où $d_{FR}$ est la distance géodésique de Fisher-Rao (orthogonalité sémantique), $W_{1,G}$ la distance de transport sur le graphe de citations (éloignement structurel inter-silos), et $\det(\mathcal{I}_{Fisher})$ le volume d'information de Fisher discriminant les distributions interventionnelles des hypothèses causales $H_A$ et $H
