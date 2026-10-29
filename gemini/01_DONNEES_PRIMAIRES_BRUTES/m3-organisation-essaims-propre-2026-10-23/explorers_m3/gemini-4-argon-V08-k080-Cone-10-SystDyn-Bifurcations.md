BASSIN_MATH: Wada-Smale-Pesin-SaddleNodeInfinitePeriod-Swarm (WSPS-SNIPS)
LOI_PROPOSEE: Maximisation de l'entropie métrique de Pesin sur les frontières de Wada du graphe de citations par stabilisation du goulot d'étranglement d'une bifurcation col-nœud sur cycle invariant (SNIPER).

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Le graphe de citations $\mathcal{G}$ est partitionné en $K \ge 3$ bassins thématiques. `jev-1.14.0` (coût nul) évalue les embeddings de trajectoires de citations pour approximer une propriété de **bassin de Wada** : tout nœud frontière $v \in \partial W$ possède dans son $\epsilon$-voisinage sémantique des éléments des $K$ silos simultanément. La dynamique hors-poids de l'essaim suit une **bifurcation SNIPER** (Saddle-Node Infinite PERiod) : $\dot{\theta}_i = \omega - \cos(\theta_i) + \mu(\text{jev}(v_i))$.
- *Phase fantôme ($\mu \to 0^+$ gratuite)* : Ralentissement critique dans le goulot d'étranglement ($\tau_{\text{passage}} \propto \mu^{-1/2}$) où des marcheurs non-génératifs parcourent des **fers à cheval de Smale** (codage symbolique de sous-décalages de type fini sur les citations croisées) jusqu'à ce que la mesure de **Sinai-Ruelle-Bowen (SRB)** se concentre sur $\partial W$.
- *Saut hystérétique (Allocation 100$ Claude / 20$ Gemini)* : Dès que la somme des exposants de Lyapunov positifs (via `jev-1.14.0`) franchit un seuil sur $\partial W$, Gemini 1.5 Flash compresse la topologie locale (coût faible), puis Claude 3.5 Sonnet est déclenché par impulsion pour synthétiser l'isomorphisme structurel au cœur du goulot fantôme.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(H_A, H_B) = \left( \sum_{\lambda_i > 0} \lambda_i(\text{jev}) \right)_{\text{Pesin}} \cdot \mathbb{I}_{Wada}(v) \cdot \left\| \mathcal{P}_{E^u}(H_A) \wedge \mathcal{P}_{E^s}(H_B) \right\|_{\text{transverse}}$$
Où la formule d'entropie de Pesin garantit la divergence inter-silos, et le produit extérieur mesure la transversalité stricte entre la variété instable $E^u$ (hypothèse $H_A$) et stable $E^s$ ($H_B$), pénalisant à zéro tout homéomorphisme rhétorique trivial (vernis) par annulation du déterminant jacobien sémantique.

3. **Pont in?dit et duel ($H_A \perp H_B$)** :
Pont entre *l'ingénierie de représentation par vecteurs de contrôle* (Zou et al., 202
