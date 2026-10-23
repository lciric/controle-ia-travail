BASSIN_MATH: Plonk-KZG-QuorumSystem-MalkhiReiter-BenOr (PKQ-MRB)
LOI_PROPOSEE: L'essaim s'auto-organise en systèmes de quorums byzantins opaques où les ponts inter-silos sont validés par des contraintes de permutation cyclique (type PlonK) sur le graphe de citations et un tirage de pièce commun (Ben-Or) opéré à coût nul par `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids (PKQ-MRB)** :
L'espace documentaire est partitionné en systèmes de quorums byzantins $\mathcal{Q} = \{Q_1, \dots, Q_m\}$ (Malkhi-Reiter) vérifiant $\forall Q_i, Q_j \in \mathcal{Q}, |Q_i \cap Q_j| \ge 2t + 1$, où $t$ est le nombre d'agents hallucinants ou complaisants (sycophantes).
- **Phase à coût zéro (`jev-1.14.0` + API)** : `jev-1.14.0` évalue des millions de paires de sous-graphes et construit un engagement polynomial de type KZG $C(\phi) = g^{\phi(\tau)}$ sur les vecteurs d'attributs méthodologiques extraits. Il agit comme oracle de *Common Coin* (Ben-Or) pour briser les symétries de collusion sans consommer de jetons LLM.
- **Allocation budgétaire (100$ Claude / 20$ Gemini)** : Gemini génère des témoins de câblage (*copy-constraints* $\sigma$ à la PlonK) reliant les entrées/sorties causales de deux silos distants. Claude n'est invoqué que lorsque le polynôme de grand produit d'acumulation $Z(\omega x) = Z(x) \frac{(f(x) + \beta x + \gamma)}{(f(x) + \beta \sigma(x) + \gamma)}$ évalué par `jev-1.14.0` franchit un seuil d'exactitude structurelle sur un quorum complet $Q_k$. Les quorums échouant au test de division par le polynôme annulateur $Z_H(x)$ voient leur poids topologique purgé hors-poids.

2. **Fonction objectif anti-vernis** :
$$\mathcal{L}_{\text{PKQ}}(H_A, H_B) = d_{\text{spectral}}(S_A, S_B) \cdot \left(1 - \max_{Q \in \mathcal{Q}} \text{Adv}^{\text{Soundness}}_{\text{KZG}}(Q)\right) \cdot \mathbb{I}\left( \deg\left(\gcd(P_{H_A}(x), P_{H_B}(x))\right) = 0 \right)$$
où $d_{\text{spectral}}$ est la distance de résistance effective dans le graphe de citations entre silos $S_A$ et $S_B$, $\text{Adv}^{\text{Soundness}}_{\text{KZG}}$ pénalise le vernis rhétorique non engagé structurellement, et la coprimalité des polynômes de traces
