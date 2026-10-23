BASSIN_MATH: Niche-Baldwin à Dominance Cyclique (NBDC)

LOI_PROPOSEE: $\dot x_i=\sum_j x_j f_j(x,E)\,Q_{ji}(\mu)-\bar f\,x_i$ et $\dot E=\sum_i x_i c_i-\delta E$, avec $f_i=b_i(E)-\kappa\,\$_i-\gamma\,\rho_{i,\mathrm{fam}}$ et $Q_{ji}$ une mutation de génome-consigne contrainte par $d_{\mathrm{jev}}(\text{consigne}_i,\text{racine})<\tau$.

**1. Auto-organisation hors-poids**

Un agent est défini par un génotype $g=(\text{famille},\text{consigne},\text{rôle},\text{voisins})$. La niche $E$ est un registre partagé de faits vérifiés via Crossref et Semantic Scholar : elle constitue un héritage écologique. L'apprentissage par effet Baldwin se fait sans toucher aux poids : seules les consignes qui exploitent $E$ se répliquent.

La topologie suit l'équation de Price étendue à la niche : $\bar w\Delta\bar z=\mathrm{Cov}(w,z)+\mathbb{E}(w\Delta z)+\Delta_E$.

- **Exploration.** Si $\mathrm{Cov}(w,z)<\epsilon$, la sélection est stagnante : on augmente $\mu$ et on spawne un explorateur vers une cellule MAP-Elites vide. Les descripteurs sont la signature d'erreur jev et le sous-domaine visé.
- **Red-Team.** Les démolisseurs jouent le rôle de parasites selon une génétique d'allèles appariés : un parasite de famille $k$ attaque prioritairement les hôtes de famille $k$. Si le taux d'infection passe sous $\theta$ (Reine Rouge stagnante), on spawne un démolisseur.
- **Monoculture ou chimère.** On passe en chimère dès que $\rho_{i,\mathrm{fam}}>\rho^*$, où $\rho$ est la corrélation d'erreurs mesurée par jev (H4'). Sinon, on garde la monoculture, qui coûte moins cher.
- **Dominance cyclique.** Les rôles explorateur, consolidateur et démolisseur suivent un cycle de type May-Leonard. Il empêche qu'un rôle unique absorbe le budget de 100 USD (Claude) et 20 USD (Gemini).

**2. Objectif anti-Goodhart**

$$R=\frac{\Delta QD_{\mathrm{ext}}}{\$}-\lambda\,\big|s_{\mathrm{jev}}-s_{\mathrm{ext}}\big|-\gamma\bar\rho-\eta\,\mathbb{1}[\text{citation non résolue}]$$

- $QD_{\mathrm{ext}}$ est la somme des qualités des cellules de l'archive, vérifiées sur un jeu caché et tournant.
- jev ne note jamais directement ce qui est sélectionné. L'écart entre jev et la vérification externe est pénalisé, ce qui contre Goodhart.
- Une citation absente de Crossref est létale, ce qui contre la récitation paramétrique.

**3. Duel décisif ($H_A\perp H_B$)**

Le plan est factoriel 2×2 à budget constant (120 USD par bras) :

- $H_A$ : la niche $E$ est active ou permutée aléatoirement. Ce bras est le contrôle négatif qui teste la causalité de la niche.
- $H_B$ : la co-évolution parasite-hôte est cyclique ou les démolisseurs sont tirés i.i.d.

Deux bras de référence s'ajoutent : un essaim fixe (topologie figée) et un essaim i.i.d. (agents échantillonnés uniformément).

- **Métriques :** faits vrais et nouveaux par dollar, $\bar\rho$ inter-agents, dérive de consigne (H9).
- **Protocole :** préenregistrement, 20 graines, test de permutation, correction de Holm.
- **Critère de validation :** l'interaction et les deux effets principaux doivent être positifs, NBDC doit dominer les bras fixe et i.i.d. ($p<0.01$), et la niche permutée doit annuler le gain $\Delta_E$.
