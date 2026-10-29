BASSIN_MATH: Flot de Ricci-Ollivier à Gradient Naturel (FROGN)
LOI_PROPOSEE: $\dot w_{ij}=-\kappa_{ij}\,w_{ij}$, avec $\kappa_{ij}=1-W_1(m_i,m_j)/d_{ij}$ ; et $\theta_{t+1}=\theta_t+\eta\,G_c(\theta_t)^{-1}\nabla_\theta J$, où $G_c=\mathrm{diag}(c_k/p_k)$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Graphe d'agents.** L'essaim est un graphe pondéré $(V,w)$. Pour chaque agent $i$, $m_i$ est la loi des sorties de `jev-1.14.0` sur les productions de son voisinage. Le coût de transport $W_1$ se calcule sur ce graphe, à coût marginal nul.
- **Arêtes à courbure positive** ($\kappa_{ij}>\kappa^+$). Elles signalent des agents redondants, donc des erreurs corrélées (H4'). L'arête est affaiblie et l'essaim spawne un **démolisseur Red-Team** issu d'une autre famille de poids.
- **Arêtes à courbure négative** ($\kappa_{ij}<\kappa^-$). Elles signalent un goulot entre régions disjointes de l'espace des hypothèses. L'essaim spawne un **explorateur** au point de rupture.
- **Monoculture ou chimère.** On mesure la courbure moyenne intra-famille $\bar\kappa_F$. Si $\bar\kappa_F>\kappa^+$, l'essaim croise obligatoirement les familles (fable, opus, argon). Sinon, il conserve la monoculture, moins coûteuse.
- **Apprentissage hors-poids.** Les paramètres $\theta=(p_k)$ sont les poids d'un simplexe sur les rôles, familles et gabarits de prompts. Ils suivent un gradient naturel d'Amari pondéré par le coût unitaire $c_k$ (ratio 100/20 USD).
- **Contrôle de la dérive (H9).** Une délégation est élaguée si $d_{FR}=2\arccos\sum\sqrt{p_{\text{racine}}\,p_{\text{délégué}}}>\delta$. Cette distance de Fisher-Rao est calculée sur les sorties `jev` de la consigne racine et de la consigne déléguée.

**2. Fonction objectif et anti-Goodhart**

$$J=\frac{\mathbb E[V_{\text{vérif}}]}{\text{USD}}-\beta\,\rho_{\text{err}}-\gamma\,\big|\,\mathcal J_1-\mathcal J_2\,\big|$$

- $V_{\text{vérif}}$ ne compte que les affirmations ancrées dans un DOI ou un identifiant arXiv retrouvé via Crossref ou Semantic Scholar. Toute affirmation non sourcée vaut 0, ce qui neutralise la récitation de la mémoire paramétrique.
- $\rho_{\text{err}}$ est la corrélation inter-agents des erreurs.
- $\mathcal J_1$ et $\mathcal J_2$ sont deux juges `jev` aux projections disjointes, renouvelées à chaque époque. La récompense est $\min(\mathcal J_1,\mathcal J_2)$, et l'écart entre juges est pénalisé, ce qui rend le sur-ajustement à un juge unique non rentable (Goodhart).

**3. Duel décisif ($H_A\perp H_B$)**

- **Hypothèses.**
  - $H_A$ : la courbure, et non le hasard, guide les gains.
  - $H_B$ : les gains proviennent seulement du mélange de familles.
- **Budget.** Il est constant pour tous les bras (100 USD Claude, 20 USD Gemini), avec un ratio chimérique moyen imposé identique. Cette contrainte isole $H_A$ de $H_B$.
- **Bras.**
  - (A) FROGN.
  - (B) Topologie fixe.
  - (C) Agents i.i.d.
  - (D) Contrôle négatif placebo : même flot, mais $\kappa_{ij}$ permutées aléatoirement.
- **Tâche.** Des questions dont la réponse se trouve dans des articles postérieurs à la date de coupure des modèles, ce qui empêche la récitation.
- **Protocole.** Pré-enregistrement, 20 graines, test de permutation, seuil $\alpha=0{,}01$.
- **Mesure.** Affirmations vérifiées par USD, $\rho_{\text{err}}$ et taux de dérive.
- **Prédiction falsifiable.** Si FROGN est valide : A > D ≈ B ≈ C sur le rendement, et $\rho_{\text{err}}(A)<\rho_{\text{err}}(D)$. Si A ≈ D, la loi est réfutée.
