BASSIN_MATH: Code Sphérique de Thomson-Bhattacharyya (CSTB)

LOI_PROPOSEE: $\psi_i=\sqrt{p_i}\in S^{K-1}_+$ ; $d_{ij}=2\arccos\langle\psi_i,\psi_j\rangle$ ; $\theta_i\leftarrow\theta_i-\eta\,G_F(\theta_i)^{-1}\nabla_{\theta_i}\big[-U_i+\lambda\sum_{j\neq i}w_{ij}\,d_{ij}^{-s}\big]$

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**

Chaque agent $i$ est défini par un état $\theta_i$ = (famille de poids, prompt, rôle, mémoire externe). Sur un lot tournant de sondes, `jev-1.14.0` produit la distribution $p_i$ des étiquettes de ses sorties. Le plongement $\sqrt{p}$ envoie ces distributions sur la sphère de Fisher-Rao, où la distance de Bhattacharyya est géodésique.

L'essaim minimise une énergie de Riesz : il cherche un code sphérique de Thomson, c'est-à-dire des agents utiles et angulairement séparés. On n'entraîne aucun poids : on applique le gradient naturel d'Amari sur les paramètres discrets relaxés (logits de prompt et de rôle). La matrice $G_F$ est estimée empiriquement par `jev`.

Règles topologiques :
- **Collapse ($H_4'$)** : si $d_{ij}<\delta$, l'agent le moins utile est remplacé par la famille de poids qui maximise $\min_j d_{\cdot j}$. La chimère n'est donc retenue que si elle est géométriquement plus éloignée que la monoculture.
- **Explorateur** : un explorateur est créé au centre du plus grand trou sphérique (rayon de recouvrement).
- **Démolisseur Red-Team** : il est placé à l'antipode géodésique du barycentre de Fréchet du consensus.
- **Communication** : $j$ écoute $i$ si $d_{ij}\in[\delta,\pi/2]$.
- **Budget** : la répartition du budget (100 USD Claude / 20 USD Gemini) sur le graphe des tâches est un plan de transport optimal discret, de type Benamou-Brenier sur graphe. Il déplace la masse vers les tâches où le code présente des trous, avec un coût égal à la distance entre tâches.
- **Dérive ($H_9$)** : une délégation est élaguée si $d_{FR}(p_{\text{parent}}^{\text{canari}},p_{\text{enfant}}^{\text{canari}})>\varepsilon$.

2. **Fonction objectif et anti-Goodhart**

$$R=\mathrm{Acc}_{\text{vérif}}-\lambda_1E_{\text{Riesz}}-\lambda_2\,\text{coût}-\lambda_3\,\text{dérive}-\lambda_4\,\big|\mathrm{score}_{jev}-\mathrm{Acc}_{\text{vérif}}\big|$$

- $\mathrm{Acc}_{\text{vérif}}$ ne provient que de clés externes : DOI et citations vérifiés via Crossref, Semantic Scholar et arXiv, ainsi que des tâches postérieures à la date de coupure, pour neutraliser la récitation paramétrique.
- `jev` sert uniquement à mesurer la géométrie, jamais à récompenser.
- Ses sondes sont renouvelées à chaque époque.
- Le terme $\lambda_4$ pénalise tout découplage entre le juge et la vérité vérifiable.

3. **Duel décisif de validation M3 ($H_A\perp H_B$)**

- $H_A$ : le gain vient de la séparation angulaire.
- $H_B$ : le gain vient du simple chimérisme.

Le plan est factoriel 2×2 : (géométrie CSTB ou permutée) × (chimère ou monoculture), plus un essaim fixe et un essaim i.i.d., tous au budget identique de 100 USD Claude / 20 USD Gemini. Il porte sur 200 tâches tenues à l'écart.

Le contrôle négatif est un CSTB dont la matrice $[d_{ij}]$ est permutée aléatoirement : même machinerie, même coût, mais géométrie détruite.

Critères mesurés :
- $\mathrm{Acc}_{\text{vérif}}$ ;
- la corrélation des erreurs $\rho$ ;
- la dérive mesurée sur les canaris.

Prédictions et réfutation :
- $H_A$ est validée si CSTB > permuté dans les deux familles, avec bootstrap $p<0{,}01$ et $\rho$ réduite.
- $H_B$ est validée si l'effet du chimérisme subsiste sous permutation.
- Si CSTB ≈ permuté, la loi est réfutée.
