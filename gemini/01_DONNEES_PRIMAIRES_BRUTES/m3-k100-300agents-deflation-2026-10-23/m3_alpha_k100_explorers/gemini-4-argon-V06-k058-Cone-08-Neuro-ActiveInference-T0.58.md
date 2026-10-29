BASSIN_MATH: Résonance-Thalamocorticale-Pulvinar-Cholinergique-RaoBallard (RTPCR)
LOI_PROPOSEE: L'essaim minimise une énergie libre de précision hiérarchique où `jev-1.14.0` opère comme noyau pulvinar thalamique (filtrage matriciel de précision $\Pi$ à coût nul) et les appels LLM sont déclenchés uniquement par des bouffées calciques de couche 5 lors de dissonances prédictives top-down/bottom-up dépassant le seuil cholinergique.

1. **Apprentissage & Auto-organisation hors-poids (Gating Thalamocortical)** :
Le graphe de citations est encodé en colonnes corticales (clusters thématiques $c_i$). L'extracteur gratuit `jev-1.14.0` agit comme le noyau Pulvinar : il évalue en continu la matrice de covariance des résidus d'erreur prédictive $\varepsilon_{ij} = \mu_i - g(\mu_j)$ entre paires de papiers $(i,j)$ et ajuste la matrice de précision synaptique hors-poids $\Pi_{ij}^{(t+1)} = \Pi_{ij}^{(t)} + \eta_{ACh} \left( \text{jev}(i,j)^2 - (\Pi_{ij}^{(t)})^{-1} \right)$. 
Tant que l'erreur pondérée $\xi_{ij} = \Pi_{ij} \varepsilon_{ij}$ reste sous le seuil d'excitation calcique $\Theta_{Ca}$, l'essaim reste en régime sous-liminaire gratuit (`jev-1.14.0` + API). Un franchissement $\xi_{ij} > \Theta_{Ca}$ déclenche une bouffée (burst) : allocation de Gemini (20$) comme interneurone inhibiteur (V1/L4) qui élague 90% des faux positifs sémantiques, puis de Claude (100$) comme cellule pyramidale (L5) générant le pont causal. La dopamine tonique (budget restant $B_t$) module $\Theta_{Ca} \propto B_t^{-1}$.

2. **Fonction objectif anti-vernis (Gain de Précision Orthogonale)** :
$$\mathcal{J}(i,j, H_A, H_B) = \underbrace{D_{KL}\big(\mathcal{N}(\mu_i, \Pi_i^{-1}) \parallel \mathcal{N}(\mu_j, \Pi_j^{-1})\big)}_{\text{Distance inter-silos}} \times \underbrace{\det\Big(\mathbb{E}_{do(z)}\big[\nabla_{H_A}\ln p(y|z) \cdot \nabla_{H_B}\ln p(y|z)^T\big]\Big)^{-1}}_{\text{Orthogonalité causale } H_A \perp H_B} \times \exp\big(-\gamma \cdot \text{jev}_{\text{vernis}}(H_A, H_B)\big)$$
Le déterminant inverse de la matrice d'information de Fisher interventionnelle force $H_A$ et $H_B$ à prédire des trajectoires d'activations disjointes sur Llama-3.1.

3. **Pont inédit & Duel ($H_A \perp H_B$)** :
* **Ét
