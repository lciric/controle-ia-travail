BASSIN_MATH: Surface-Minimale-Lagrange-Pistone-qExponential-Busemann (SMLP-qEB)
LOI_PROPOSEE: L'essaim minimise le volume riemannien d'une sous-variété d'interpolations q-exponentielles (Naudts) plongée dans la variété exponentielle non-paramétrique de Pistone-Sempi, guidé par les rayons géodésiques de Busemann de l'espace de Wasserstein $W_1$ sur graphe de citations.

1. **Loi d'auto-organisation hors-poids** :
Le graphe bibliographique gratuit $G=(V,E)$ est muni de la distance de Kantorovich-Rubinstein $W_1$. `jev-1.14.0` (illimité) évalue pour chaque article $v \in V$ une distribution sémantique $p_v \in \mathcal{M}_\mu$ (variété de Pistone-Sempi) et calcule les fonctions d'horosphère de Busemann $B_\gamma(v) = \lim_{t \to \infty} (d_{W_1}(v, \gamma(t)) - t)$ le long des rayons géodésiques $\gamma$ fuyant les clusters centraux. L'essaim place des ancres aux cols selles de $B_\gamma(v)$ (coût $0$). Les $20\$$ Gemini génèrent un complexe simplicial d'hypothèses $\Sigma$ paramétré par les coordonnées $\theta$ d'une famille $q$-exponentielle $\exp_q(\theta \cdot T(x) - \psi_q(\theta))$, munie de la métrique de Fisher-Rao déformée $g_{ij}^{(q)}(\theta)$. L'évolution hors-poids suit le flot de tension de Plateau-Amari (gradient naturel de l'aire induite) : $\delta \theta^i = - [g^{(q)}]^{ij} \Delta_{\Sigma} \theta_j$. Les $100\$$ Claude sont alloués exclusivement aux singularités où la courbure moyenne $H_{\Sigma}$ diverge, synthétisant le pont causal.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(\Sigma) = \left( \int_{\partial \Sigma} |d B_\gamma|_{W_1} \, ds \right) \times \left( \det G_{\text{Fisher}}^{(q)}(\Sigma) \right)^{-1/2} \times \exp\left( - \left| \langle \nabla^{\text{nat}} \ell(H_A), \nabla^{\text{nat}} \ell(H_B) \rangle_{g^{(q)}} \right| \right)$$
Le premier facteur maximise l'écartement inter-silos via le flux de Busemann-$W_1$ sur le bord $\partial \Sigma$. Le second pénalise la dégénérescence du volume informationnel (anti-vernis). Le troisième impose l'orthogonalité stricte de Fisher-Rao ($H_A \perp H_B$) entre les gradients naturels des log-vraisemblances causales testées par `jev-1.14.0`.

3. **Pont inédit et duel causal ($H_A \perp H_B$)** :
Pont entre l'effondrement de rang (rank collapse) dans l'auto
