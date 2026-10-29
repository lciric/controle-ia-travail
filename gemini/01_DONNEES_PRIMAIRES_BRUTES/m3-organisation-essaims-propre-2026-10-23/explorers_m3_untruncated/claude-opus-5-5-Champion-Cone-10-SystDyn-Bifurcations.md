BASSIN_MATH: Loi de Restauration Ergodique par Mélange Koopman (REMK)

LOI_PROPOSEE: $\Delta\mathcal{T}_t=\arg\max_{\mathcal{T}}\big[\,\mathrm{gap}(\mathcal{K}_\mathcal{T})-\alpha\,\Lambda^{+}_{H9}(\mathcal{T})\,\big]\ \text{s.c. } C(\mathcal{T})\le B_t$, avec $\mathrm{gap}=1-|\lambda_2(\mathcal{K})|$ et $\Lambda^{+}_{H9}=\max(0,\lambda_{\mathrm{FTLE}})$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Opérateur de Koopman.** Chaque message est projeté par `jev-1.14.0` (coût nul) dans un espace d'observables $\psi$. Par la méthode EDMD, on estime l'opérateur de Koopman $\mathcal{K}$ de la dynamique des croyances de l'essaim sur une fenêtre glissante.
- **Détection des pièges de corrélation.** Une multiplicité $m$ de valeurs propres $|\lambda|\approx1$ révèle une rupture d'ergodicité : des ensembles invariants où l'essaim reste piégé.
- **Agent démolisseur Red-Team.** Si un ensemble invariant n'est soutenu que par une seule famille de poids (signature de H4'), on spawne un démolisseur ciblé sur la fonction propre correspondante $\phi_k$.
- **Agent explorateur.** Si la densité invariante de Perron-Frobenius laisse une région de l'espace des hypothèses sous-visitée (masse inférieure à $\epsilon$), on spawne un explorateur.
- **Arbitrage monoculture/chimère.** Le paramètre de contrôle est $\mu$, la fraction de Gemini.
  - On mesure l'exposant de Lyapunov à temps fini $\lambda_{\mathrm{FTLE}}$ de la dérive de consigne le long des chaînes de délégation, par perturbation infinitésimale de la consigne et mesure par `jev`.
  - La monoculture contracte les erreurs, ce qui donne une corrélation élevée.
  - On augmente $\mu$ jusqu'à la bifurcation fourche où $m$ chute, sans franchir le seuil où $\lambda_{\mathrm{FTLE}}>0$.
- **Topologie des échanges.** Qui parle à qui est déterminé par les arêtes qui maximisent le trou spectral.
- **Budget.** L'allocation suit $B_t^{\text{fam}}\propto$ la contribution marginale de chaque famille au trou spectral, avec un plafond strict de 100/20 USD.

**2. Fonction objectif et anti-Goodhart**

$$R=\Delta I_{\mathrm{vérif}}+\beta\,\mathrm{gap}(\mathcal{K})-\gamma\,(m-k^{*})_{+}-\alpha\,\Lambda^{+}_{H9}-\eta\,\rho(J,\psi_{\perp})^{2}$$

- $\Delta I_{\mathrm{vérif}}$ ne compte que les affirmations confirmées par les graphes arXiv, Semantic Scholar et Crossref. Les citations introuvables sont pénalisées, ce qui combat la récitation de la mémoire paramétrique.
- La réponse au risque de Goodhart repose sur la décorrélation : $\rho$ mesure la corrélation entre le score du juge $J$ et des observables $\psi_\perp$ que le juge ne voit pas, tirées aléatoirement à chaque époque. On pénalise donc toute optimisation qui exploite le juge.
- Le juge lui-même est tourné entre familles de modèles et n'est jamais évalué par sa propre famille.

**3. Duel décisif ($H_A\perp H_B$)**

- **Hypothèses.**
  - $H_A$ : le gain provient de la restauration ergodique, c'est-à-dire du pilotage par le trou spectral.
  - $H_B$ : le gain provient uniquement de la diversité de familles, c'est-à-dire du ratio $\mu$.
- **Quatre bras à budget identique** (100/20 USD), sur 40 questions de `controle-ia` avec une vérité bibliographique établie a posteriori :
  1. REMK complet ;
  2. essaim fixe, avec la topologie la meilleure a priori ;
  3. essaim i.i.d. utilisant le même $\mu$ final que REMK ;
  4. contrôle négatif : REMK avec des fonctions propres de Koopman permutées aléatoirement, au même taux de spawn et au même $\mu$.
- **Critères principaux.**
  - Le taux d'affirmations vérifiées.
  - La corrélation d'erreur inter-agents.
  - $m$ final.
- **Prédiction falsifiable.** Si $H_A$ est vraie : bras 1 > bras 4 = bras 3 ≈ bras 2. Si $H_B$ est vraie : bras 1 ≈ bras 3 ≈ bras 4.
- **Analyse statistique.** Test par permutation, à $p<0{,}01$, avec préenregistrement.
