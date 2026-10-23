BASSIN_MATH: Géodésique-Duale-Chentsov-Gromov-Wasserstein
LOI_PROPOSEE: L'essaim évolue par transport parallèle le long des $\alpha$-géodésiques duales d'Amari-Chentsov ($\nabla^{(1)}, \nabla^{(-1)}$) couplé à la minimisation de la distorsion de Gromov-Wasserstein (GW) entropique entre sous-graphes de citations disjoints.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Le graphe de citations $G=(V,E)$ est muni de la métrique de Fisher-Rao $g_{ij}(\theta) = \mathbb{E}_{jev}[\partial_i \ell \partial_j \ell]$ estimée à coût nul en projetant chaque papier $v \in V$ dans le simplexe de probabilités sémantiques du classifieur `jev-1.14.0`. L'essaim maintient une distribution empirique de croyances $\mu_t$ mise à jour hors-poids via la projection $\alpha$-géodésique duale :
$$\theta_{t+1} = \Pi_{\mathcal{M}}^{(1)} \left( \theta_t - \eta_t g^{-1}(\theta_t) \nabla_\theta \mathcal{GW}_\epsilon(\mu_A, \mu_B) \right)$$
où $\mathcal{GW}_\epsilon(\mu_A, \mu_B) = \min_{\pi \in \Pi(\mu_A, \mu_B)} \sum_{i,j,k,l} |d_{FR}(v_i^A, v_k^A) - d_{FR}(v_j^B, v_l^B)|^2 \pi_{ij}\pi_{kl} - \epsilon H(\pi)$ aligne l'isométrie structurelle de deux silos disjoints $A, B$ uniquement via `jev-1.14.0`. Les budgets LLM sont déclenchés par dépassement de la courbure sectionnelle de Riemann $\mathcal{R}(\theta_t)$ : Gemini (20\$) échantillonne les paires $(v_i^A, v_j^B)$ maximisant le plan de transport $\pi^*_{ij}$ aux singularités de courbure ; Claude (100\$) synthétise l'isomorphisme mécaniste et le protocole de falsification uniquement si le théorème de Pythagore généralisé d'Amari $D_\alpha(P\|Q) + D_{-\alpha}(Q\|R) = D_\alpha(P\|R)$ révèle une brisure d'orthogonalité duale sur Llama-3.1.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(A,B) = d_{GW}(\mathcal{G}_A, \mathcal{G}_B) \times \det(g_{FR}(\theta_{H_A \oplus H_B})) \times \inf_{\pi} \mathcal{W}_1\left(\mathbb{P}_{Llama}(\cdot | \text{do}(H_A)), \mathbb{P}_{Llama}(\cdot | \text{do}(H_B))\right)$$
Le volume riemannien $\det(g_{FR})$ mesuré par `jev-1.14.0` pénalise la
