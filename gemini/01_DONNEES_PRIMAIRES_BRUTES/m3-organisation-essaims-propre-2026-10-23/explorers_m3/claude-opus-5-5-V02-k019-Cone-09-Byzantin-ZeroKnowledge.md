BASSIN_MATH: Essaim à Engagement-Révélé et Sondage Local (EERSL)

LOI_PROPOSEE: $G_{t+1}=\arg\min_{G}\ \mathrm{coût}(G)\ \text{s.c.}\ \kappa(G)\ge 2\hat f_t+1,\quad \hat f_t=\omega\big(\{(i,j): C_{ij}>\tau\}\big),\quad C_{ij}=\Pr(\text{erreur}_i\wedge\text{erreur}_j\wedge\text{accord})-\epsilon_i\epsilon_j$

Ici, $\kappa(G)$ est la connectivité sommet de Dolev, $\omega(\cdot)$ la taille de la clique maximale du graphe de collusion, et $\epsilon_i$ le taux d'erreur de l'agent $i$.

1. **Mécanisme d'auto-organisation hors-poids**
   - **Engagement aveugle.** Chaque agent publie $c_i=H(\text{réponse}_i\,\|\,r_i)$ avant de voir les autres, puis révèle sa réponse. Ce protocole interdit la copie et bloque la dérive de consigne (H9) : chaque sous-agent reçoit la consigne-racine signée, jamais une paraphrase.
   - **Détection de collusion.** La matrice $C$ est mise à jour sur des items-sondes vérifiés. Les cliques d'erreurs corrélées révèlent les familles de poids partagés (H4′).
   - **Arbitrage monoculture/chimère.** Si une clique est intra-famille et que $\hat f$ dépasse le seuil, l'essaim remplace des nœuds par une autre famille (chimère). Sinon, il reste monoculturel, ce qui est moins cher.
   - **Explorateur ou démolisseur.** Le vérificateur Arthur pioche $q$ positions aléatoires d'une preuve décomposée en assertions atomiques. Si le taux de rejet $\rho<\rho_{\min}$ (essaim trop sûr de lui), il spawne un démolisseur Red-Team. Si le taux de couverture est faible, il spawne un explorateur.
   - **Budget.** Le budget va au nœud de gain marginal de solidité $\Delta s/\$$ maximal, réparti sur 100 USD Claude et 20 USD Gemini.

2. **Fonction objectif et anti-Goodhart**

   $R=\frac{1}{q}\sum_{k\in Q_{\text{caché}}}\mathbb{1}[\text{vérif}_k]-\lambda\,\hat f-\mu\,\frac{\$}{B}-\nu\,\mathrm{Rec}$

   - $Q$ est tiré après l'engagement et reste inconnu des agents.
   - `jev-1.14.0` sert uniquement d'oracle d'échantillonnage. Il est recalibré sur des items-canaris piégés, et une partie de ses verdicts est retirée au hasard.
   - La vérité terrain vient des API Crossref, Semantic Scholar et arXiv (existence, DOI, contenu).
   - $\mathrm{Rec}$ est le taux de citations inexistantes ou non vérifiables. Ce terme pénalise la récitation de la mémoire paramétrique.

3. **Duel décisif ($H_A\perp H_B$)**
   - **Hypothèses.**
     - $H_A$ : l'adaptation topologique réduit les erreurs corrélées.
     - $H_B$ : le gain provient seulement du volume d'inférence.
   - **Protocole.** On compare quatre bras à budget identique sur $N=300$ tâches pré-enregistrées vérifiables par graphe bibliographique :
     - (i) EERSL ;
     - (ii) graphe complet fixe ;
     - (iii) agents i.i.d. avec vote majoritaire ;
     - (iv) contrôle négatif : EERSL avec matrice $C$ permutée aléatoirement, donc une topologie mutée sans information.
   - **Métriques.** Taux d'erreur, taux d'erreurs conjointes $\sum C_{ij}$, et taux de citations fantômes.
   - **Critère.** On valide si (i) bat à la fois (ii), (iii) et (iv), avec un test de permutation à $p<0{,}01$ et une correction de Holm. Si (iv) égale (i), $H_A$ est réfutée.
