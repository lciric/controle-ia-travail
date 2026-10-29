BASSIN_MATH: Loi des Points Conjugués de Jacobi (LPCJ)

LOI_PROPOSEE: $\pi_{t+1}=\mathrm{Exp}^{FR}_{\pi_t}\!\big(\eta\,G(\pi_t)^{-1}\nabla U\big)$ ; spawn d'un démolisseur hétérofamilial dès que $L_{ij}\ge t^*_{ij}=\pi/\sqrt{K_{ij}}$ avec $K_{ij}>0$, et d'un explorateur monoculturel si $K_{ij}\le 0$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **Variétés d'état.** `jev-1.14.0` étiquette gratuitement les erreurs de chaque agent. On en estime un modèle d'Ising $q_\theta$ des erreurs jointes, de couplages $\theta_{ij}$, muni de la métrique de Fisher $G(\theta)$.
- **Rôle des courbures.** $K_{ij}$ est la courbure sectionnelle de $G$ sur le plan $(\partial_{\theta_i},\partial_{\theta_j})$.
  - Si $K_{ij}>0$, les géodésiques convergent, ce qui signale des erreurs corrélées (`H4'`).
  - Si $K_{ij}<0$, elles divergent, ce qui signale une diversité réelle.
- **Mesure de la dérive.** $L_{ij}$ est la longueur Fisher-Rao parcourue par la consigne le long de la chaîne de délégation : $L=\sum_k d_{FR}(c_k,c_{k+1})$, où $c_k$ est le profil `jev` de la consigne au niveau $k$.
- **Règle de spawn.** Atteindre le point conjugué signifie que la chaîne de délégation n'est plus minimisante (`H9`). On spawne alors un démolisseur Red-Team d'une autre famille : chimère forcée.
- **Topologie.** L'agent $i$ parle à $j$ si et seulement si la masse $\gamma^*_{ij}$ du plan optimal $W_1$ sur le graphe dépasse $\tau$. Le coût de sol est $d_{FR}(p_i,p_j)=2\arccos\sum\sqrt{p_ip_j}$, et l'on exclut les paires de distance inférieure à $t^*$, ce qui supprime les échos.
- **Allocation du budget.** $\pi$ est une distribution sur (rôle × famille × modèle). Elle évolue par gradient naturel d'Amari, sous la contrainte $\sum c\,\pi\le 100$ USD (Claude) et $20$ USD (Gemini).

**2. Fonction objectif et anti-Goodhart**

$$U=\mathrm{Acc}_{\text{audit}}-\lambda_1\sum_{i<j}I(e_i;e_j)-\lambda_2\,W_2\big(\mu_{\text{jev}},\mu_{\text{audit}}\big)-\lambda_3\,R_{\text{cit}}-\lambda_4\,\text{coût}$$

- $\mathrm{Acc}_{\text{audit}}$ est mesurée sur des sondes `jev` secrètes et tournantes.
- Le terme $W_2$ pénalise tout écart entre le score optimisé et l'audit caché : c'est la parade à Goodhart.
- $R_{\text{cit}}$ est la fraction de citations non résolues via Crossref, arXiv ou Semantic Scholar, ce qui pénalise la récitation de la mémoire paramétrique.

**3. Duel décisif de validation M3 ($H_A\perp H_B$)**

- **Bras.** Quatre bras à budget identique (25 USD Claude et 5 USD Gemini chacun) :
  - A : LPCJ ;
  - B : topologie fixe ;
  - C : agents i.i.d. de même composition ;
  - D : contrôle négatif, LPCJ avec des $K_{ij}$ permutés aléatoirement (même taux de chimères, synchronisation détruite).
- **Tâches.** 300 affirmations bibliographiques à vérité terrain résoluble via Crossref, sur 10 graines.
- **Hypothèses.**
  - $H_A$ : le gain provient de la synchronisation par courbure, soit $A>D$.
  - $H_B$ : le gain provient de la seule proportion de chimères, soit $A\approx D>B,C$.
- **Critère.** Test de permutation pré-enregistré, avec $\Delta\mathrm{Acc}\ge 5$ points et une baisse de $\rho$ (corrélation des erreurs) d'au moins $0{,}1$.
- **Réfutation.** La loi est réfutée si $A\le D$.
