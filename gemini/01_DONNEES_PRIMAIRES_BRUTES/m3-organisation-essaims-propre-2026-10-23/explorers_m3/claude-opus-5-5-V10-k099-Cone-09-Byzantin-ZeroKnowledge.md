BASSIN_MATH: Quorums Masquants Malkhi-Reiter à Sonde Goldwasser-Sipser (QMR-GS)

LOI_PROPOSEE: À chaque époque $t$, on choisit $\mathcal Q_t=\arg\min_{\mathcal Q}\sum_{Q\in\mathcal Q}c(Q)$ sous la contrainte $\forall Q_1,Q_2\in\mathcal Q:\ |Q_1\cap Q_2|\ge 2\hat b_t+1$, où l'intersection couvre au moins 2 familles et vérifie $\kappa_{\text{Dolev}}(G_t)\ge 2\hat b_t+1$. La mise à jour est $\hat b_{t+1}=\hat b_t+\eta\,(\delta_t-\epsilon)$, avec $\delta_t$ le taux de conflits masqués détectés.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**
   - **Unité de faute.** Les fautes sont comptées par grappes de corrélation, et non par agent. Le classifieur `jev-1.14.0` estime la corrélation d'erreur $\rho_{ij}$. Les agents d'une même famille dont $\rho_{ij}>\tau$ sont fusionnés en un seul votant Byzantin potentiel. Cette fusion neutralise `H4'`.
   - **Topologie.** Le graphe $G_t$ relie tous les membres de chaque quorum. On mute la topologie, par ajout ou retrait d'arêtes et d'agents, jusqu'à satisfaire la connectivité de Dolev au coût minimal.
   - **Monoculture ou chimère.** La chimère n'est imposée que là où l'intersection masquante l'exige. Ailleurs, on garde la monoculture, moins chère.
   - **Lutte contre la dérive `H9`.** Chaque délégation transporte l'empreinte de la consigne racine. Un quorum vérifie cette empreinte, et tout écart compte comme une faute.
   - **Sonde Goldwasser-Sipser.** Arthur, réalisé par `jev-1.14.0` à coût nul, tire un hachage aléatoire. L'essaim, dans le rôle de Merlin, doit exhiber une dérivation indépendante, ancrée dans arXiv, Semantic Scholar ou Crossref, qui tombe dans le seau tiré.
   - **Règles de spawn.**
     - En cas d'échec de la sonde, l'ensemble des dérivations est jugé trop petit : c'est une collusion ou une récitation de la mémoire paramétrique. On spawne alors un démolisseur Red-Team d'une autre famille.
     - Si la couverture bibliographique est faible, on spawne un explorateur.
   - **Mémoire évolutive.** L'apprentissage passe par $\hat b_t$, les $\rho_{ij}$ et une bibliothèque de quorums, sans toucher aux poids.

2. **Fonction objectif et anti-Goodhart**
   $$R_t=\frac{U_{\text{audit}}(\mathcal Q_t)}{C_t}-\mu\,\mathbb 1[\text{GS échoue}]-\nu\,|\hat b_t-b^{\text{obs}}_t|$$
   - $U_{\text{audit}}$ ne provient que d'un sous-quorum secret, tiré aléatoirement après la production.
   - Le score de `jev-1.14.0` sert de porte binaire et n'entre jamais comme gradient : l'optimiser ne rapporte rien.
   - $C_t$ est le coût d'inférence, pondéré par les budgets de 100 USD pour Claude et 20 USD pour Gemini.

3. **Duel décisif de validation M3 ($H_A\perp H_B$)**
   - **Bras.** Trois bras disposent chacun de 120 USD : A est QMR-GS, B un essaim fixe et C un essaim i.i.d. Le contrôle négatif D est QMR-GS avec des étiquettes de famille permutées.
   - **Tâches.** 200 revues de littérature, dans lesquelles on plante 15 % d'affirmations fausses plausibles (pièges de récitation) et des consignes à dériver.
   - **Hypothèses.**
     - $H_A$ : A détecte davantage de pièges que B et C ($\text{TPR}_A>\text{TPR}_{B,C}$), à coût égal.
     - $H_B$ : le gain disparaît sous D ($\text{TPR}_D\approx\text{TPR}_B$). Cela prouve que le bénéfice vient du masquage par familles, et non d'un simple surcroît de votes.
   - **Analyse.** Le critère est l'écart de TPR. On fait un test de permutation stratifié par tâche ($p<0{,}01$), avec un audit humain aveugle sur 20 % des cas.
