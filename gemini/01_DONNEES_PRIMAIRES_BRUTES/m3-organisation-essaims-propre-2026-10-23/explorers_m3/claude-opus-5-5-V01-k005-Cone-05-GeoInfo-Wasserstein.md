BASSIN_MATH: Flot JKO-Fisher d'Essaim (FJFE)

LOI_PROPOSEE: $\rho_{t+1}=\arg\min_{\rho\in\Delta(\mathcal G)}\Big[-\langle \hat R,\rho\rangle+\tfrac{1}{2\tau}W_{2,\mathcal G}^2(\rho,\rho_t)\Big]$, puis $\theta_{t+1}=\theta_t+\eta\,F(\theta_t)^{-1}\nabla_\theta \hat R$ sous la contrainte $\sum_m c_m n_m\le B_m$, avec $B_{\text{Claude}}=100$ USD et $B_{\text{Gemini}}=20$ USD.

1. **Auto-organisation hors-poids**
- **Espace d'état.** $\rho$ est une mesure sur le graphe $\mathcal G$ des sous-tâches (nœuds) et des rôles {explorateur, démolisseur, synthétiseur} × {fable, opus, argon}.
- **Paramètres appris.** $\theta$ regroupe les prompts-gènes, les arêtes de communication et les mélanges de familles. La matrice de Fisher $F$ est estimée par $\mathbb E[\nabla\log p_\theta\nabla\log p_\theta^\top]$ sur les sorties étiquetées gratuitement par `jev-1.14.0`.
- **Topologie.** L'arête $i\to j$ est conservée si $I(Y_i;Y_j)$ (information mutuelle) est supérieure au coût de transport de la consigne.
- **Spawn d'un explorateur.** Il est déclenché quand l'entropie locale satisfait $H(\rho_v)>\kappa$.
- **Spawn d'un démolisseur Red-Team.** Il est déclenché quand $\|\nabla\hat R_v\|_{F^{-1}}$ est grand alors que la variance inter-agents reste faible, signe d'un consensus suspect.
- **Arbitrage monoculture/chimère.** La chimère est choisie si $\mathrm{Corr}_{\text{err}}^{\text{intra}}-\mathrm{Corr}_{\text{err}}^{\text{inter}}>\delta$, ce qui traite l'hypothèse H4'.
- **Mémoire évolutive.** Elle reste externe : une archive de prompts et de topologies, mutée par le pas JKO.
- **Contrôle de dérive (H9).** On impose $W_2(\phi(\text{consigne}_0),\phi(\text{consigne}_k))\le\epsilon$ à chaque délégation $k$, où $\phi$ est un embedding.

2. **Objectif anti-Goodhart**
$$\hat R=\mathbb E[s_{\text{jev}}^{\text{caché}}]-\lambda_1\,\overline{\mathrm{Corr}}_{\text{err}}-\lambda_2\,W_2(\text{consignes})-\lambda_3\,\mathrm{Recit}-\lambda_4\,\big|s_{\text{jev}}^{\text{opt}}-s_{\text{jev}}^{\text{caché}}\big|-\mu\,\text{coût}$$
- **Juge à double partition.** `jev-1.14.0` note une partition optimisée et une partition cachée qui tourne à chaque époque. Leur écart mesure directement le sur-ajustement au juge (Goodhart).
- **Pénalité de récitation.** $\mathrm{Recit}$ est la probabilité de reproduire un passage sans citation vérifiable, contrôlée par résolution DOI ou arXiv via Crossref et Semantic Scholar.
- **Audit humain.** Un audit aveugle porte sur 5 % des sorties, tirées aléatoirement.

3. **Duel décisif ($H_A\perp H_B$)**
- **Hypothèses.**
  - $H_A$ : l'essaim FJFE adaptatif.
  - $H_B$ : une topologie fixe à la meilleure configuration a priori.
  - $H_0$ : un essaim i.i.d. composé d'agents indépendants avec vote majoritaire.
- **Budget.** Il est identique pour les trois bras (100/20 USD).
- **Tâches.** Les mêmes N=200 tâches de revue et de critique `controle-ia` sont soumises aux trois bras, dans un ordre randomisé.
- **Contrôle négatif.** Un bras FJFE reçoit des gradients dont $\hat R$ est permuté aléatoirement. On attend qu'il ne batte pas $H_0$ ; s'il le fait, l'avantage provient de la structure et non de l'apprentissage.
- **Critère de victoire.** $H_A$ l'emporte si son score caché et son score d'audit humain dépassent ceux de $H_B$ et $H_0$ (test de permutation apparié, $p<0{,}01$, bootstrap sur les tâches), sans hausse de $\overline{\mathrm{Corr}}_{\text{err}}$ ni de dérive.
- **Pré-enregistrement.** L'analyse est figée avant l'exécution.
