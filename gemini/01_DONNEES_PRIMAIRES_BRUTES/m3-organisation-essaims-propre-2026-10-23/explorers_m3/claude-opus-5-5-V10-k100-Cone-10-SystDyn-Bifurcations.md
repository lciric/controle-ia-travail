BASSIN_MATH: Scission de Melnikov à Rotation Diophantienne (SMRD)

LOI_PROPOSEE: $x_{t+1}=F_\mu(x_t)+\varepsilon g(x_t,\theta_t)$. Un Démolisseur est engendré dès que $M(\theta_0)=\int_{-\infty}^{\infty}\langle\nabla H(q^0(t)),\,g(q^0(t),t+\theta_0)\rangle\,dt$ présente un zéro simple ($M=0$, $M'\neq0$). Le mélange de familles $w$ est contraint par $|\rho(w)-p/q|>\gamma q^{-5/2}$ pour tout $p/q$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Espace d'état.** L'état $x_t\in\Delta^{R\times F}$ décrit l'allocation de budget par rôle (Explorateur, Démolisseur, Synthétiseur) et par famille (fable-5-1, opus-5-5, argon).
- **Selle de consensus.** Le point fixe hyperbolique $q^*$ correspond au cas où tous les agents convergent vers la même réponse : c'est l'erreur corrélée $H4'$. Son hamiltonien $H$ est la cohérence inter-agents mesurée par `jev-1.14.0`.
- **Signal de Melnikov.** Un zéro simple de $M$ signale une intersection transverse des variétés stable et instable, c'est-à-dire un enchevêtrement homocline. Ce consensus est fragile et doit être cassé : on engendre alors un Démolisseur Red-Team. Si $M$ garde un signe constant, on engendre plutôt un Explorateur.
- **Arbitrage monoculture/chimère.** La rotation des rôles est une application du cercle de nombre de rotation $\rho(w)$. Une langue d'Arnold, où $\rho$ est rationnel, traduit un verrouillage monoculturel. On mute donc $w$, en direction de $\rho\to(\sqrt5-1)/2$, jusqu'à atteindre une zone diophantienne de type KAM.
- **Topologie.** Elle est apprise par EDMD-Koopman sur les trajectoires de scores `jev`. Une arête $i\to j$ est conservée si l'énergie croisée des modes propres de Koopman dépasse $\tau$.
- **Dérive H9.** Un sous-agent de profondeur $d$ est élagué si $\|\phi_1(c_d)-\phi_1(c_0)\|>\epsilon$, où $\phi_1$ est la fonction propre dominante de Koopman appliquée au plongement de la consigne.

**2. Fonction objectif et anti-Goodhart**

$$R=\frac{V_{\text{graphe}}}{\$}-\alpha\,\big|\lambda_1-\lambda^*\big|-\beta\,\bar\varrho_{\text{err}}-\eta\,D_{TV}\big(P_{\text{jev}}^\star,P_{\text{vérif}}^\star\big)$$

- $V_{\text{graphe}}$ compte les affirmations vérifiées via arXiv, Semantic Scholar et Crossref. Les citations non résolubles comptent négativement, ce qui sanctionne la récitation de la mémoire paramétrique.
- $\lambda_1$ est l'exposant de Lyapunov maximal de l'allocation. La cible $\lambda^*\gtrsim0$ maintient l'essaim au bord du chaos.
- $\bar\varrho_{\text{err}}$ est la corrélation moyenne des erreurs entre agents.
- Le dernier terme compare les densités invariantes de Perron-Frobenius du juge et de la vérification externe. Cet écart pénalise l'optimisation du juge `jev` au détriment de la vérité.

**3. Duel décisif ($H_A\perp H_B$)**

- **Conditions communes.** Budget identique (100 USD Claude, 20 USD Gemini), 60 questions de recherche contenant des fautes semées, 5 graines.
- **Bras.**
  - A : SMRD complète.
  - B : topologie fixe.
  - C : spawns i.i.d.
  - D, contrôle négatif : signal $M$ permuté temporellement, avec un nombre de spawns apparié.
- **Hypothèses.**
  - $H_A$ : A > B et A > C sur $V/\$$.
  - $H_B$ : A > D, ce qui montre que le gain provient de la géométrie de Melnikov et non du volume de spawns.
  - Le plan factoriel (signal × diversité diophantienne) isole les deux effets orthogonalement.
- **Mesures secondaires.** $\bar\varrho_{\text{err}}$ et la dérive de $\phi_1$.
- **Analyse.** Test de permutation préenregistré, avec $\alpha=0{,}01$ et correction de Holm.
