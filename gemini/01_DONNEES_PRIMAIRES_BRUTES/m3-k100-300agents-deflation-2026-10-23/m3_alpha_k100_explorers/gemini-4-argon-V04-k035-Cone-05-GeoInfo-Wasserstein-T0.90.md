BASSIN_MATH: Barycentre-Karcher-Transport-Parallel-Sasaki-Beckmann (BK-TPSB)
LOI_PROPOSEE: L'essaim s'auto-organise en déplaçant la mesure de croyance sur le fibré tangent statistique via un flux de Beckmann discret couplé au transport parallèle d'Amari-Chentsov ($\nabla^{(\alpha)}$), synthétisant les ponts par barycentre de Karcher-Fréchet sous métrique de Sasaki-Fisher-Rao.

1. **Auto-organisation hors-poids & Allocation** :
Le graphe de citations $G=(V,E)$ est muni d'une variété statistique locale $\mathcal{M}_v$ par nœud, paramétrée par les log-probabilités du classifieur gratuit `jev-1.14.0` ($\theta_v \in \mathbb{R}^d$). Sans appel LLM, nous résolvons le problème de flux de Beckmann sur graphe $W_1(P_A, P_B) = \min_{J} \sum_{e \in E} w_e \|J_e\|_2$ sous contrainte de divergence $\text{div}(J) = P_A - P_B$, où $w_e$ est la distance de Fisher-Rao locale estimée par `jev-1.14.0`. Les agents sont des vecteurs tangents $(v, \dot{\theta}_v) \in T\mathcal{M}$ évoluant sur la métrique de Sasaki $G_S$. L'allocation des 120 USD est déclenchée uniquement aux points de Karcher-Fréchet (minimiseurs de $\sum_k d_{\text{Fisher}}^2(\mu, p_k)$) où le défaut d'holonomie du transport parallèle dual ($\nabla^{(1)}$ vs $\nabla^{(-1)}$) le long des géodésiques de Beckmann excède un seuil $\tau$. Gemini (20 USD) échantillonne les géodésiques $\nabla^{(-1)}$ (mélange exploratoire) ; Claude (100 USD) projette sur les sous-variétés autoparallèles $\nabla^{(1)}$ (exponentielle exacte) pour synthétiser le code d'expérimentation.

2. **Fonction objectif anti-vernis** :
$$\mathcal{L}(H_A, H_B) = W_1^{\text{Beckmann}}(\mu_A, \mu_B) \times \det\left(\mathcal{I}_F(\theta_{\text{pont}})\right)^{1/2} \times \left\| \Pi_{\nabla^{(1)}}^{A \to B}(H_A) - H_B \right\|_{g_F^{-1}}^2 \times \mathbb{I}(\text{CosSim}_{\text{jev}}(A,B) < \epsilon)$$
Le déterminant du volume riemannien de Jeffreys $\sqrt{\det \mathcal{I}_F}$ pénalise les hypothèses vagues (vernis à courbure nulle). Le terme d'orthogonalité force le vecteur tangent transporté $\Pi(H_A)$ à entrer en collision frontale falsifiable ($H_A \perp H_B$) avec $H_B$ sur Llama-3.1-8B/70B.

3. **Pont inédit & Duel causal ($H_A \perp H
