BASSIN_MATH: Loi de Kelly-Ville à E-Processus Croisés (LKV-EPC)

LOI_PROPOSEE: $W_{k,t}=W_{k,t-1}\big(1+\lambda_{k,t}(E_{k,t}-1)\big)$ ; $\;w_t^\star=\arg\max_{w\ge0,\;w^\top c\le B_t}\mathbb{E}_{\hat\pi_t}\!\left[\log\!\big(1+w^\top(E_t-1)\big)\right]$

1. **Mécanisme d'auto-organisation hors-poids.** Chaque agent $k$ (famille $f_k\in\{\text{fable},\text{opus},\text{argon}\}$) est un parieur. Il émet une affirmation falsifiable. Un vérificateur adverse produit alors une e-valeur $E_{k,t}$ ($\mathbb{E}_{H_0}[E]\le1$) via `jev` et les graphes arXiv, Semantic Scholar et Crossref. Sa richesse $W_{k,t}$ est une martingale de Ville sous $H_0$.
   - **Allocation et topologie.** Le budget en dollars est alloué par le portefeuille de Kelly $w^\star$. Le coût est $c_k$. La loi $\hat\pi_t$ est une distribution particulaire ($N=512$) sur la corrélation latente inter-familles $\rho_{ff'}$ (H4′). Cette loi pénalise mécaniquement les paris redondants entre agents de même famille. Une arête $k\to j$ existe ssi $\mathrm{Cov}_{\hat\pi}(E_k,E_j)<0$, c'est-à-dire si $j$ réfute utilement $k$.
   - **Spawn.** Un explorateur est créé si $\max_k W_k<1$ pendant $\tau$ pas, signe d'une richesse globale stagnante. Un démolisseur Red-Team est créé quand $W_k\ge1/\alpha$, pour tenter de tuer l'affirmation avant son acceptation.
   - **Monoculture ou chimère.** Un bandit Thompson à facteur d'oubli $\gamma$, contextualisé par le type de tâche, choisit le mélange de familles. Le budget Gemini est contraint à $\le 20$ USD.
   - **Dérive H9.** Un e-CUSUM $M_t=\max(1,M_{t-1})\,E^{\text{consigne}}_t$ compare chaque délégation à la consigne racine. Si $M_t\ge A$, la sous-branche est réinitialisée.

2. **Fonction objectif anti-Goodhart.**
$$R=\sum_t \log\big(1+w_t^\top(E_t-1)\big)\;-\;\eta\,\mathrm{KL}\big(\hat\pi_t\,\|\,\hat\pi_{t-1}\big)\;-\;\mu\,\mathbb{1}[\text{source}\le\text{cutoff}]$$
   - Le juge `jev` n'est qu'un ingrédient prévisible de $E$. Des leurres plantés, faux mais plausibles, recalibrent chaque e-valeur. Optimiser le juge sans vérité fait donc chuter $W$, puisque $\mathbb{E}[\log W]<0$ sous $H_0$.
   - La pénalité $\mu$ porte sur les sources antérieures au cutoff. Elle écarte la récitation paramétrique.

3. **Duel décisif ($H_A\perp H_B$).** Le budget est identique pour tous les bras : 100 USD Claude et 20 USD Gemini. Les tâches portent sur 300 questions bibliographiques postérieures au cutoff, avec vérité issue des graphes. Quatre bras sont comparés : (i) LKV-EPC ; (ii) topologie fixe ; (iii) allocation i.i.d. uniforme ; (iv) contrôle négatif, soit LKV avec e-valeurs permutées entre agents.
   - **Métrique.** Nombre d'affirmations vraies acceptées par dollar, au FDR $\le0.1$ contrôlé par e-BH.
   - **$H_A$.** (i) bat (ii) et (iii).
   - **$H_B$.** Le gain s'annule en (iv). Cela prouve que l'avantage vient du signal falsifiable et non de l'architecture.
   - **Arrêt.** L'arrêt est anytime-valid par e-test apparié séquentiel, avec rejet si $\prod_t E^{\text{duel}}_t\ge20$.
   - **Réfutation.** La loi est réfutée si (iv) égale (i), ou si (i) ne dépasse pas (ii).
