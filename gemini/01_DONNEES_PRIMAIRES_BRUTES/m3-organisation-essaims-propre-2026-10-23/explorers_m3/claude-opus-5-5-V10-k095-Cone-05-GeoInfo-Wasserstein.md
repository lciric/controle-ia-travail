BASSIN_MATH: Flot de Ricci-Ollivier à Gradient Naturel Budgétaire (FROGNB)

LOI_PROPOSEE: $\dot w_{ij} = -\kappa_{ij}\,w_{ij}$, avec $\kappa_{ij} = 1 - \dfrac{W_1^{G}(m_i, m_j)}{d_{FR}(p_i, p_j)}$, couplée à $\dot b_k = b_k\big(\tilde g_k - \textstyle\sum_l b_l \tilde g_l\big)$, où $\tilde g = F^{-1}\nabla J$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **Représentation des agents.** Chaque agent $i$ produit des affirmations. Le classifieur `jev-1.14.0` les projette sur une loi catégorielle $p_i$.
- **Distance et courbure.** La distance entre agents est la distance de Fisher-Rao, $d_{FR} = 2\arccos\sum_c \sqrt{p_i p_j}$. La mesure $m_i$ est la loi du voisinage de $i$ pondérée par les $w_{ij}$. La courbure d'Ollivier $\kappa_{ij}$ s'obtient par transport optimal $W_1$ sur le graphe de communication.
- **Courbure positive ($\kappa_{ij} > \kappa^+$).** Elle signale une clique redondante, donc des erreurs corrélées (H4'). Le flot affaiblit l'arête. Si la clique est monoculturelle, l'essaim spawne un démolisseur Red-Team issu d'une autre famille (Gemini si la clique est Claude, et inversement).
- **Courbure négative ($\kappa_{ij} < \kappa^-$).** Elle signale un goulot entre régions épistémiques. L'essaim spawne un explorateur au pont et renforce l'arête.
- **Arbitrage monoculture/chimère.** Une famille reste monoculturelle tant que $\bar\kappa_{\text{intra}} < \kappa^+$. Au-delà, une arête croisée est injectée.
- **Allocation du budget.** Le gradient naturel d'Amari sur le simplexe des parts $b_k$ donne la dynamique du réplicateur. Elle est projetée sous les contraintes $\sum_{\text{Claude}} c_k b_k \le 100$ USD et $\sum_{\text{Gemini}} c_k b_k \le 20$ USD.
- **Contrôle de la dérive (H9).** Toute délégation $r \to s$ est rejetée si $d_{FR}(p_{\text{consigne},r}, p_{\text{consigne},s}) > \delta$.
- **Apprentissage sans poids.** Seuls $w$, $b$ et la topologie évoluent. Ils sont journalisés et rejoués comme prompts de rôle.

**2. Fonction objectif et dispositif anti-Goodhart**

$$J = \sum_t \Delta\log P(\text{faits vérifiés}) - \lambda\,\rho_{\text{err}} - \mu\,R_{\text{récit}} - \nu\, D_{FR}\big(q_{\text{juge}} \,\|\, q_{\text{ext}}\big)$$

- **Vérification externe.** Un fait n'est vérifié que par arXiv, Semantic Scholar ou Crossref, via le DOI, la date et une citation existante.
- **$\rho_{\text{err}}$.** Corrélation moyenne des erreurs entre agents.
- **$R_{\text{récit}}$.** Part des affirmations non récupérables ou survivant au masquage contrefactuel des entités, ce qui trahit la récitation de mémoire paramétrique.
- **Rôle limité du juge.** `jev` sert uniquement de plongement et ne note jamais. Si sa distribution de scores $q_{\text{juge}}$ diverge de la vérité externe $q_{\text{ext}}$, la récompense est pénalisée.

**3. Duel décisif ($H_A \perp H_B$), à budget constant de 120 USD**

- **Bras A (FROGNB).** La loi proposée.
- **Bras B.** Topologie fixe, en étoile ou complète.
- **Bras C.** Essaim i.i.d.
- **Contrôle négatif D.** Flot identique, mais avec des signes de $\kappa$ permutés aléatoirement.
- **Plan.** Mêmes tâches, 30 graines et coûts appariés, avec pré-enregistrement.
- **Métriques.**
  - Taux d'affirmations vérifiées ;
  - $\rho_{\text{err}}$ ;
  - dérive de consigne ;
  - coût par fait vérifié.
- **Prédiction.** A > B, C, D (Wilcoxon apparié, $p < 0{,}01$) et $\rho_{\text{err}}(A) < \rho_{\text{err}}(B)$.
- **Critère de réfutation.** Si $A \approx D$, la courbure n'est pas causale et la loi est rejetée.
