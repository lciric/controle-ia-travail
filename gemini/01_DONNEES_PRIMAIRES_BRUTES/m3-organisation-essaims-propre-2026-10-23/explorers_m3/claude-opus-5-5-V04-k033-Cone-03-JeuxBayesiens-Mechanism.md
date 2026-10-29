BASSIN_MATH: Enchère d'Escrow à Valeur Virtuelle Décorrélée (EEVVD)

LOI_PROPOSEE: $i^*(t)=\arg\max_i \big[\varphi_i(\hat v_i)-\lambda\,\hat\rho_{i,S_t}\big]_+$, avec $\varphi_i(v)=v-\frac{1-F_i(v)}{f_i(v)}$, $\hat v_i=\frac{\mathbb{E}[\Delta \mathrm{Brier}_i]}{c_i}$, et un paiement séquestré $\pi_i=B(p_{-i},y)-B(p_S,y)$ réglé sur un audit caché.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**
   - **Enchères de sous-tâches.** Chaque sous-tâche $t$ est mise aux enchères. Chaque agent soumet une prédiction probabiliste $p_i$ du verdict futur et son coût d'inférence $c_i$.
   - **Allocation de Myerson.** La tâche va à la meilleure valeur virtuelle, pénalisée par $\hat\rho_{i,S_t}$. Ce terme est la corrélation empirique, mesurée par `jev-1.14.0`, entre les erreurs passées de $i$ et celles de l'essaim déjà affecté $S_t$.
   - **Chimère ou monoculture.** L'arbitrage est endogène : un agent de même famille de poids n'est retenu que si son gain marginal dépasse $\lambda\hat\rho$ (risque H4').
   - **Prix de réserve.** Il vaut $r=\varphi^{-1}(0)$. Le budget, 100 USD pour Claude et 20 USD pour Gemini, n'est engagé que si la valeur virtuelle est positive.
   - **Spawn d'un explorateur.** Il est déclenché lorsque $\mathrm{Var}(p_S)$ est élevée et que la valeur d'information dépasse $r$.
   - **Spawn d'un démolisseur Red-Team.** Il est déclenché lorsque le consensus $p_S$ est extrême mais que $\hat\rho_{S}$ est élevée. Le démolisseur est payé uniquement sur les réfutations validées.
   - **Lutte contre la dérive (H9).** Chaque délégation est un contrat. Le délégué doit reconstruire la consigne parente, et `jev` note la divergence ; cette divergence est soustraite du séquestre.
   - **Apprentissage sans réentraînement.** Il porte uniquement sur les distributions $F_i$ (posteriors bayésiens de type), sur $\hat\rho$ et sur la topologie, stockés en mémoire externe.

2. **Fonction objectif et anti-Goodhart**
   - **Signal de récompense de l'essaim :** $J=\mathbb{E}\big[-B(p_S,y^{\text{audit}})\big]-\mu\sum c_i-\lambda\,\overline{\rho}-\kappa\,\mathrm{Dérive}$.
   - **Persuasion de Kamenica-Gentzkow inversée.** Le principal conçoit la structure d'information du juge pour révéler le minimum : $y^{\text{audit}}$ provient de $K$ variantes cachées de prompt `jev`, tirées au hasard. Seuls 20 % des items sont réglés, et selon un tirage non prédictible.
   - **Anti-récitation.** Toute affirmation exige un DOI résolu via Crossref ou un identifiant arXiv vérifié. À défaut, $y=0$.
   - **Propriété d'incitation.** Le score de Brier étant propre, la véracité des prédictions est une stratégie optimale.

3. **Duel décisif ($H_A\perp H_B$), à budget constant**
   - **Plan factoriel 2×2 :** allocation Myerson contre allocation uniforme i.i.d., croisée avec une pénalité $\lambda$ positive contre $\lambda=0$.
   - **Comparateur supplémentaire :** un essaim à topologie fixe.
   - **Contrôle négatif :** EEVVD avec étiquettes d'audit permutées. Son avantage doit tomber au niveau i.i.d.
   - **Métrique préenregistrée :** précision des affirmations vérifiées sur 200 questions tenues à l'écart, évaluées par un juge humain et par croisement de familles de modèles.
   - **$H_A$ (allocation) :** l'effet principal de Myerson est positif.
   - **$H_B$ (décorrélation) :** l'effet de $\lambda$ est positif, et indépendant de l'allocation (interaction nulle).
   - **Critère de réfutation :** la loi est réfutée si EEVVD ne bat pas à la fois l'essaim fixe et le bras i.i.d., avec un test bootstrap apparié au seuil $p<0{,}01$.
