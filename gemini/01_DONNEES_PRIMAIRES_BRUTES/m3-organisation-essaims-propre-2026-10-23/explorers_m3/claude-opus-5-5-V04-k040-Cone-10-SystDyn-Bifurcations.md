BASSIN_MATH: Échange Transcritique à Dimension de Kaplan-Yorke (ETKY)

LOI_PROPOSEE: $\dot x_i = x_i\big(\mu_i - \sum_j \rho_{ij}x_j\big) - \kappa_i x_i$, avec $\mu_i=\Delta\hat J_i/\text{USD}_i$. Le rôle-famille $i$ envahit l'essaim si et seulement si $\mu_i>\sum_j\rho_{ij}x_j^*+\kappa_i$, ce qui constitue une bifurcation transcritique. La profondeur de délégation est bornée par $d^*=\lfloor \ln(\varepsilon/\delta_0)/\lambda_1\rfloor$.

**1. Mécanisme d'auto-organisation hors-poids**

- **État.** Le vecteur $x_{k,r}$ donne les fractions d'appels par famille $k\in\{F,O,G\}$ et par rôle $r\in\{\text{explorateur},\text{démolisseur}\}$, sur deux simplexes budgétaires disjoints (Claude : 100 USD, Gemini : 20 USD).
- **Couplage.** $\rho_{ij}$ est la corrélation d'erreurs mesurée par `jev-1.14.0` sur des sondes communes (H4'). Une monoculture s'auto-inhibe ($\rho_{kk}\approx1$), si bien que la chimère émerge par échange de stabilité, sans règle ad hoc.
- **Dérive (H9).** $\lambda_1$ est l'exposant de Lyapunov maximal de l'application de délégation. Il est estimé par la croissance, au fil des sauts, de la distance `jev` entre la consigne-mère et chaque consigne déléguée. Si $\lambda_1>0$, la délégation est coupée à la profondeur $d^*$ et la consigne est réinjectée intégralement.
- **Spawn.** On calcule la dimension de Kaplan-Yorke $D_{KY}=k+\sum_{m\le k}\lambda_m/|\lambda_{k+1}|$ des sorties perturbées.
  - Si $D_{KY}<D_-$, les sorties se sont effondrées (récitation) : on spawne un explorateur.
  - Si $D_{KY}>D_+$, les sorties se dispersent sans structure : on spawne un démolisseur Red-Team.
- **Récitation.** La densité invariante $p^*$ de l'opérateur de Perron-Frobenius, estimée sur les affirmations produites, est comparée aux articles connus via Semantic Scholar et Crossref. Les atomes de $p^*$ situés sur des articles existants sont pénalisés.

**2. Fonction objectif et anti-Goodhart**

$$R=\hat J_{\text{rot}}-\beta\,x^\top\rho\,x-\gamma\max(0,\lambda_1)-\eta\,\mathrm{KL}\!\left(p^*\,\|\,p_{\text{nouv}}\right)-\zeta\,\max\!\big(0,\Lambda_G\big)$$

- $\hat J_{\text{rot}}$ est le score `jev` calculé sur des projections aléatoires secrètes, re-tirées à chaque époque.
- $\Lambda_G$ est le taux de divergence entre le score `jev` et un audit humain aveugle sur 5 % des sorties. Lorsque $\Lambda_G>0$, cela signale une exploitation de Goodhart, qui est alors pénalisée.

**3. Duel décisif ($H_A\perp H_B$)**

Le budget est fixé à 120 USD par bras, sur 40 tâches pré-enregistrées, avec 5 graines par bras.

- **Bras A :** ETKY.
- **Bras B :** topologie fixe (chimère figée).
- **Bras C (contrôle négatif) :** rôles et familles tirés i.i.d.
- **Bras D (placebo) :** ETKY avec une matrice $\rho$ permutée aléatoirement.

Les deux hypothèses testées sont les suivantes :

- **$H_A$ :** le nombre de découvertes vérifiées par audit aveugle et par le graphe de citations suit l'ordre $A>B$, $A>C$ et $A>D$ (test de permutation, $p<0{,}01$).
- **$H_B$ (signature dynamique, indépendante de $H_A$) :** un balayage du budget en montée puis en descente doit révéler un point critique $\mu_c=\sum_j\rho_{ij}x_j^*$ où la composition bascule. L'hystérésis est attendue seulement si un terme d'ordre supérieur rend la bifurcation sous-critique.

La loi est réfutée si D égale A (le couplage ne compte pas) ou si aucune bascule n'apparaît au voisinage de $\mu_c$.
