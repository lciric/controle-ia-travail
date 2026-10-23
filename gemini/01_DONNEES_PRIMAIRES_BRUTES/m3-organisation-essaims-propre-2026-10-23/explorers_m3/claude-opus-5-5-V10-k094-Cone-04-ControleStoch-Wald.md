BASSIN_MATH: Indice de Whittle Agité à Réarmement CUSUM (IWA-RC)

LOI_PROPOSEE: $a_t=\arg\max_{a\in\{0,1\}^N}\sum_i a_i\,[W_i(\hat\pi_t)-\lambda^{C}_t c^{C}_i-\lambda^{G}_t c^{G}_i]$ sous $\sum_i a_i c_i^{f}\le B^{f}_t$. Le terme $W_i$ est l'indice de Whittle du bras agité $i$ (rôle × famille × arête). La croyance $\hat\pi_t$ est filtrée par particules. Si $S_{i,t}=\max(0,S_{i,t-1}+\ell_{i,t})>h$, le sous-arbre de $i$ est réarmé.

1. **Auto-organisation hors-poids**
Chaque bras $i=(\text{rôle},\text{famille},\text{parent})$ est un projet agité : son état latent évolue même lorsqu'il n'est pas sollicité, car la littérature et le contexte changent.
- **Filtrage particulaire.** Un filtre à $M$ particules estime $\theta=(q_i,\rho_{ff'})$, soit la qualité de chaque bras et la corrélation d'erreur entre familles ($H4'$), à partir des verdicts de `jev-1.14.0`.
- **Indice de Whittle.** $W_i$ est la subvention qui rend indifférent entre activer et laisser passif. On la calcule par itération de valeur sur les particules.
- **Prix duaux.** Les prix $\lambda^C_t$ et $\lambda^G_t$ s'ajustent par sous-gradient, sur des budgets distincts de 100 USD (Claude) et 20 USD (Gemini).
- **Spawn d'explorateur.** Il est déclenché si $\operatorname{Var}_{\hat\pi}(q_i)>\tau_e$.
- **Spawn de démolisseur Red-Team.** Il est déclenché si l'effectif attendu du SPRT de Wald pour valider une affirmation dépasse $\tau_r$. Cela signale une affirmation ambiguë qu'il faut attaquer.
- **Arbitrage monoculture/chimère.** On passe en chimère si $P_{\hat\pi}(\rho_{ff}>\rho_{ff'})>0{,}9$. Sinon, la monoculture moins chère est conservée.
- **Contrôle de la dérive ($H9$).** On pose $\ell_{i,t}=\log\frac{p_1(d_t)}{p_0(d_t)}$, où $d_t$ est la distance `jev` entre la sortie déléguée et la consigne racine. Un dépassement du seuil CUSUM provoque l'élagage du sous-arbre et sa ré-instanciation depuis la consigne originale.

2. **Fonction objectif anti-Goodhart**
$$R=\sum_k \mathbb{1}[\text{atome }k\text{ vérifié via Crossref/S2/arXiv}]\cdot(1-\hat\rho_k)-\gamma\sum_f\text{USD}_f-\beta\,\mathbb{1}[\text{récitation}]$$
- Le facteur $(1-\hat\rho_k)$ décote les accords corrélés intra-famille.
- Une récitation est détectée lorsqu'un atome est non traçable dans les graphes ou antérieur à un leurre injecté.
- Le juge `jev` ne paie jamais directement : il sert seulement au filtrage.
- Un second CUSUM surveille l'écart entre le score `jev` et la vérification externe. S'il alarme, le juge est recalibré sur des canaris cachés.

3. **Duel décisif ($H_A\perp H_B$)**
- **Bras comparés**, chacun avec un budget fixe de 100+20 USD, sur 60 tâches appariées :
  - $H_A$ : IWA-RC ;
  - $H_B$ : topologie fixe planificateur→3 travailleurs→juge ;
  - $H_0$ : allocation i.i.d. uniforme ;
  - contrôle négatif : IWA-RC avec indices $W_i$ permutés aléatoirement.
- **Perturbations** : on injecte une dérive de consigne au niveau 3 et des citations fantômes plausibles.
- **Métriques** : atomes vérifiés par dollar, délai de détection de la dérive, taux de récitation.
- **Test** : SPRT apparié sur les différences par tâche ($\alpha=\beta=0{,}05$).
- **Critère de réfutation** : la loi est réfutée si $H_A$ ne surpasse pas à la fois $H_B$ et $H_0$, ou si le contrôle permuté égale $H_A$. Dans ce dernier cas, le gain viendrait du budget et non de l'indice.
