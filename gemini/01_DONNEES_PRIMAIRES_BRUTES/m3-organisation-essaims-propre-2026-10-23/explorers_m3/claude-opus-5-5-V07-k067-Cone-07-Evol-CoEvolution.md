BASSIN_MATH: Équilibre Mobile de Wright à Parasites Retardés (EMW-PR)

LOI_PROPOSEE: $\dot x_{d,i}=\sum_j x_{d,j}\,\phi_j\,Q_{ji}(\mu_d)-x_{d,i}\bar\phi_d+m_t\,(\bar x_{\cdot,i}-x_{d,i})$, avec $\phi_j=R_j/c_j$ (gain par dollar), $\mu_d\propto 1/N_d$ et $m_t=\sigma\big(\mathrm{Cov}_{dèmes}(\bar w_d,\bar z_d)-\mathrm{E}[w\,\Delta z]\big)$.

1. **Auto-organisation hors-poids**
L'essaim est fragmenté en petits dèmes $d$ de taille $N_d$ entre 3 et 6. Chaque dème possède un génotype de prompts, une topologie (graphe de qui parle à qui) et une composition par famille de poids.
- **Phase I, dérive.** Les petits dèmes mutent fortement ($Q$ : réécriture de consigne, ajout ou retrait d'arête, substitution d'un modèle par une autre famille). La dérive permet ainsi de franchir les vallées adaptatives.
- **Phase II, sélection intra-dème.** Le dème suit la dynamique réplicateur-mutateur sous la contrainte budgétaire du simplexe : 100 USD pour Claude et 20 USD pour Gemini.
- **Phase III, migration.** Le terme inter-dèmes de l'équation de Price fixe $m_t$. Les dèmes gagnants exportent leurs génotypes, puis le résultat est déposé dans une archive MAP-Elites indexée par trois descripteurs : fraction chimérique, profondeur de délégation et ratio explorateur/démolisseur.
- **Spawn.** Un explorateur est créé si la cellule MAP-Elites voisine est vide. Un démolisseur Red-Team, traité comme parasite, est créé si la fitness hôte stagne.
- **Retard des parasites.** Les parasites sont évalués contre les hôtes archivés à $t-\tau$. Ce décalage empêche le cyclage stérile de la dynamique Red Queen.
- **Monoculture ou chimère.** Une chimère est sélectionnée uniquement si la corrélation d'erreurs mesurée par jev, notée $\rho_{err}$, dépasse $\rho^*$ (risque H4').

2. **Fonction objectif et anti-Goodhart**
$$R=\underbrace{S^{hold}_{jev}}_{\text{sondes tournantes cachées}}-\lambda_1\rho_{err}-\lambda_2 D_{KL}^{jev}(\text{consigne}_k\,\|\,\text{consigne}_0)-\lambda_3(1-V_{biblio})-\lambda_4 G$$
- $V_{biblio}$ est la fraction d'affirmations vérifiées via Crossref et Semantic Scholar. Elle pénalise la récitation de la mémoire paramétrique.
- Le terme $D_{KL}^{jev}$ pénalise la dérive de consigne à travers les délégations (H9).
- L'écart de Goodhart est $G=\mathrm{Cov}(w,z_{jev})-\mathrm{Cov}(w,z_{hold})$. Si la sélection suit le juge sans suivre le jeu tenu à l'écart, la pénalité croît.

3. **Duel décisif ($H_A\perp H_B$)**
- **Hypothèses.** $H_A$ : le gain provient de la dérive démique. $H_B$ : le gain provient du retard parasitaire.
- **Plan factoriel 2×2 à budget identique :**
  - dèmes petits ou un dème unique de grande taille, pour isoler la dérive ;
  - $\tau>0$ ou $\tau=0$, pour isoler le retard parasitaire.
- **Comparateurs :** un essaim fixe et un ensemble i.i.d. de même coût.
- **Contrôle négatif :** EMW-PR avec fitness permutée aléatoirement. Il doit égaler l'ensemble i.i.d.
- **Métrique préenregistrée :** affirmations vérifiées par dollar sur des tâches tenues à l'écart.
- **Protocole statistique :** 30 graines, test de permutation, correction de Holm.
- **Critère d'orthogonalité :** l'interaction factorielle doit être non significative.
- **Critère de victoire :** EMW-PR complet doit battre l'essaim fixe et l'ensemble i.i.d. avec $p<0{,}01$.
