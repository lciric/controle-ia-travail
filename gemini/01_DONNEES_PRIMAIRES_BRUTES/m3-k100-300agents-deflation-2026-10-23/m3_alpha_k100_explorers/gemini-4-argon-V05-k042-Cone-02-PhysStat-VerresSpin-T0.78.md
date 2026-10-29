BASSIN_MATH: RéponseNonLinéaire-BouchaudBiroli-VianaBray-CugliandoloKurchan (RNL-BB-VB-CK)
LOI_PROPOSEE: L'essaim maximise la susceptibilité vitreuse du troisième ordre $\chi_3(\omega, t_w)$ sur un graphe de Viana-Bray frustré via le rapport de fluctuation-dissipation effectif $X(C)$ de Cugliandolo-Kurchan.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Le graphe de citations gratuit est projeté en verre de spin dilué de Viana-Bray où les articles sont des spins d'Ising $s_i \in \{-1, +1\}$ et les arêtes de co-citation portent des couplages aléatoires $J_{ij}$ évalués à coût zéro par `jev-1.14.0` : $J_{ij} = \text{sign}(\text{jev\_sim}(i,j) - \theta_0)$ (créant des boucles de frustration épistémique $J_{ij}J_{jk}J_{ki} < 0$). L'essaim évolue hors-équilibre selon la dynamique de Langevin vieillissante de Cugliandolo-Kurchan. On injecte un champ bibliographique oscillant gratuit $h(t) = h_0 \cos(\omega t)$ (requêtes ciblées API) et `jev-1.14.0` mesure la susceptibilité non-linéaire de Bouchaud-Biroli $\chi_3(\omega, t_w) = \frac{1}{N h_0^3} \sum_i \langle s_i(t_w) \rangle_{3\omega}$, qui quantifie le volume des corrélations coopératives amorphes $\xi(t_w) \propto |\chi_3|^{1/d_f}$. Le budget (20$ Gemini pour l'exploration rapide à température $T_{\text{eff}} = T/\tilde{X}(C)$ où $\tilde{X}(C)$ est le rapport de violation FDT ; 100$ Claude pour l'extraction causale profonde) est alloué exclusivement aux sous-graphes où $\chi_3(\omega, t_w)$ diverge (transition de Gardner locale).

2. **Fonction objectif anti-vernis** :
$$\mathcal{L}_{\text{anti-vernis}}(i,j) = |\chi_3^{(i,j)}(\omega, t_w)| \cdot (1 - \tilde{X}(C_{ij})) \cdot \exp\left(-\lambda \text{jev\_vernis}(H_A, H_B)\right) \cdot \mathbb{I}(H_A \perp H_B)$$
où $1 - \tilde{X}(C_{ij}) \to 1$ garantit un régime de vieillissement profond inter-silos ($C_{ij}$ faible) loin de l'équilibre thermique trivial, et $\mathbb{I}(H_A \perp H_B)$ impose une intervention d'ablation orthogonale sur Llama-3.1-8B/70B.

3. **Pont in?dit et duel causal ($H_A \perp H_B$)** :
Pont entre *l'instabilité de de Almeida-Thouless dans les réseaux récurrents
