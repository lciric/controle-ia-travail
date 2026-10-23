BASSIN_MATH: Nerf d'Échecs à Résistance Effective Persistante (NERP)

LOI_PROPOSEE: $G_{t+1}=\mathrm{Sparsify}_{R_{\mathrm{eff}}}\big(L_t\big)$, avec $L_t=\sum_{ij}w_{ij}\,b_{ij}b_{ij}^\top$ et $w_{ij}=1-\rho(F_i,F_j)$ ; chaque agent $a$ reçoit $\pi_a\propto\partial\Phi/\partial a$, où $\Phi=\int_0^1\big(\chi(N_\varepsilon)-\chi^*\big)_+\,d\varepsilon$ et $N_\varepsilon=\mathrm{Nerf}\{F_a\}_\varepsilon$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Signal d'échec.** `jev-1.14.0` étiquette gratuitement chaque sortie. On obtient ainsi l'ensemble d'échecs $F_a\subset\mathcal{T}$ de chaque agent dans l'espace des tâches plongé.
- **Nerf filtré.** On construit le nerf $N_\varepsilon$ des $F_a$ en faisant croître le seuil de recouvrement $\varepsilon$.
- **Lecture de H4'.** Une monoculture produit des simplexes de grande dimension, car ses échecs sont partagés. L'excès d'Euler persistant $\Phi$ mesure directement cette corrélation.
- **Ponts entre agents.** Un pont $i\leftrightarrow j$ est conservé avec la probabilité $p_{ij}\propto w_{ij}R^{\mathrm{eff}}_{ij}$ (sparsification de Spielman–Srivastava). Seuls les canaux décorrélés et non redondants survivent.
- **Spawn d'un explorateur.** Chaque composante $H_0$ persistante de la région non couverte $\mathcal{T}\setminus\bigcup C_a$ déclenche un sous-agent explorateur.
- **Spawn d'un démolisseur Red-Team.** Chaque simplexe maximal de dimension $\geq 2$ persistant au-delà de $\tau$ déclenche un démolisseur, issu d'une famille absente de ce simplexe.
- **Arbitrage monoculture/chimère.** On choisit la chimère si $\Delta\Phi_{\mathrm{chim}}/\$>\Delta\Phi_{\mathrm{mono}}/\$$, à budget fixé de 100 USD Claude et 20 USD Gemini.
- **Contrôle de la dérive H9.** Le flux de consigne le long des délégations est décomposé par Helmholtz–Hodge : $f=\nabla s+\mathrm{curl}^*\psi+h$. Si $\|\mathrm{curl}^*\psi\|+\|h\|>\delta$, la sous-chaîne est réancrée sur la consigne racine.
- **Apprentissage sans réentraînement.** L'essaim n'apprend que sa topologie $G_t$ et ses prompts de rôle, stockés en mémoire externe.

**2. Fonction objectif et anti-Goodhart**

$$J=\frac{\mathrm{Acc}_{\mathrm{anc}}}{\$}-\lambda\Phi-\mu\|\mathrm{curl}^*\psi+h\|-\nu\,\big|\mathrm{jev}-\mathrm{Acc}_{\mathrm{anc}}\big|-\kappa\,\mathrm{Rec}$$

- $\mathrm{Acc}_{\mathrm{anc}}$ est mesurée sur des ancres vérifiables, secrètes et renouvelées à chaque époque. `jev` sert uniquement à construire la filtration, jamais à la récompense directe.
- Le terme en $\nu$ pénalise l'écart entre le juge et la vérité, ce qui neutralise la loi de Goodhart.
- $\mathrm{Rec}$ mesure la récitation param��trique : c'est la part de citations sans DOI ni identifiant arXiv ou Semantic Scholar résolu par Crossref ou Semantic Scholar.

**3. Duel décisif ($H_A\perp H_B$)**

- **Hypothèses.**
  - $H_A$ : NERP augmente $\mathrm{Acc}_{\mathrm{anc}}/\$$ grâce à la topologie du nerf.
  - $H_B$ : tout gain provient du seul surplus d'appels.
- **Bras, tous à budget identique et sur les mêmes 400 tâches :**
  - (i) NERP ;
  - (ii) graphe fixe de même degré moyen ;
  - (iii) ensemble i.i.d. avec vote majoritaire ;
  - (iv) contrôle négatif : NERP dont les étiquettes $F_a$ sont permutées, ce qui donne un nerf aléatoire de même cardinalité.
- **Préenregistrement.**
  - Critère : (i) doit battre (ii), (iii) et (iv) avec $p<0{,}01$, par bootstrap apparié sur 5 graines.
  - Validation de $H_A$ : il faut aussi observer $\Phi_{(i)}<\Phi_{(iv)}$ et une corrélation entre $-\Delta\Phi$ et le gain.
  - Rejet de $H_A$ : si (iv) égale (i), le gain est attribuable à l'adaptativité seule, et $H_A$ est rejetée.
