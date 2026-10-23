BASSIN_MATH: Chimère-Kuramoto à Fonction de Stabilité Maîtresse (CK-FSM)

LOI_PROPOSEE: $\dot\theta_i=\omega_i+\frac{\sigma}{N}\sum_j A_{ij}\sin(\theta_j-\theta_i-\alpha_{ij})$, avec la mutation $\dot A_{ij}=-\eta\,\partial_{A_{ij}}\big(\lambda_\perp(\sigma\lambda_2(L_A))-\lambda^*\big)^2$, où $\lambda_\perp$ est l'exposant de Lyapunov transverse de la variété de synchronisation, donné par la fonction de stabilité maîtresse de Pecora-Carroll.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **États des agents.** La phase $\theta_i$ de chaque agent est l'angle de son embedding de sortie, calculé par `jev-1.14.0` à coût nul.
- **Régime visé.** L'essaim est piloté vers un état chimère au sens de Kuramoto : un noyau cohérent produit le consensus pendant qu'une frange incohérente explore.
- **Détection de H4'.** Les poids partagés rendent $\lambda_\perp\ll0$, ce qui provoque un effondrement synchrone et donc des erreurs corrélées.
- **Arbitrage monoculture/chimère.** Si $\lambda_\perp<\lambda^*-\delta$, la loi ajoute des arêtes inter-familles (Claude↔Gemini) et augmente $\alpha_{ij}$. Si $\lambda_\perp>\lambda^*+\delta$, signe de fragmentation, elle densifie les arêtes intra-famille.
- **Spawn d'un démolisseur Red-Team.** Il est déclenché quand le paramètre d'ordre local vérifie $r_c>r^{\max}$. Le démolisseur est couplé en anti-phase, avec $\alpha=\pi/2$.
- **Spawn d'un explorateur.** Il est déclenché quand l'exposant maximal à temps fini vérifie $\Lambda_{\max}<0$ et que la nouveauté bibliographique est nulle, c'est-à-dire quand l'essaim est piégé sur un point fixe.
- **Allocation du budget.** L'appel $i$ reçoit une part $b_i\propto\partial\Lambda/\partial x_i$ (sensibilité), sous les contraintes $\sum_{\text{Claude}}b_i\le100$ et $\sum_{\text{Gemini}}b_i\le20$.
- **Contrôle de H9.** Une chaîne de délégations est traitée comme la composition d'applications $f_d\circ\dots\circ f_1$. La profondeur est plafonnée par $d\le\ln(\varepsilon/\delta_0)/\lambda_{H9}$, où $\lambda_{H9}$ est le taux de divergence de la consigne mesuré dans l'espace `jev`.

**2. Fonction objectif et anti-Goodhart**

$$R=\mathrm{Acc}_{\text{vérif}}-\beta\,|\lambda_\perp-\lambda^*|-\gamma\,\bar\rho_{\text{err}}-\kappa\,\mathrm{Coût}$$

- **Vérification externe.** $\mathrm{Acc}_{\text{vérif}}$ est calculée sur des affirmations postérieures au cutoff, vérifiées via arXiv, Semantic Scholar et Crossref, ce qui neutralise la récitation paramétrique.
- **Rôle limité du juge.** `jev` sert uniquement de capteur d'état, jamais de récompense.
- **Alarme Goodhart.** Une hausse de l'autocorrélation lag-1 de l'écart $s_{\text{jev}}-\mathrm{Acc}_{\text{vérif}}$ est un signe de ralentissement critique, précurseur d'une bifurcation Goodhart. L'alarme gèle alors la mutation de $A$ et fait tourner les tâches cachées.

**3. Duel décisif de validation M3 ($H_A\perp H_B$)**

- **Bras comparés, à budget identique (120 USD, mêmes modèles) :**
  - $H_A$ : l'essaim CK-FSM adaptatif.
  - $H_B$ : une topologie fixe, et un ensemble i.i.d. de votes.
- **Contrôles négatifs :**
  - un placebo où $\lambda_\perp$ est calculé sur des embeddings permutés ;
  - une topologie à graphe aléatoire de même densité.
- **Prédictions :**
  - En balayant $\sigma$, la précision vérifiée présente un pic au seuil de bifurcation chimère $\sigma_c$.
  - $\bar\rho_{\text{err}}(H_A)<\bar\rho_{\text{err}}(H_B)$.
  - La dérive H9 reste bornée.
- **Critères de réfutation :** l'hypothèse est rejetée si le gain disparaît à $\sigma_c$, s'il persiste sous placebo, ou si l'intervalle de confiance bootstrap à 95 % sur 300 tâches contient zéro.
