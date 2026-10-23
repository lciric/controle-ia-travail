BASSIN_MATH: Loi de Synchronie Prédictive Inverse (SPI)

LOI_PROPOSEE: $w_{ij}^{t+1}=\mathrm{softmax}_j\!\left[\frac{\varepsilon_{ij}\,\mathrm{IG}_j}{c_j}\right]$, avec $\varepsilon_{ij}=-\log p_i(y_j\mid \text{contexte})$ et $\mathrm{IG}_j=\mathbb{E}\big[D_{KL}(q(\theta\mid y_j)\,\|\,q(\theta))\big]$. Un agent écoute en priorité ceux qu'il prédit mal et qui sont informatifs par dollar.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**
- **Codage prédictif inter-agents.** Avant chaque message, l'agent $i$ prédit la sortie de l'agent $j$. `jev-1.14.0`, gratuit, estime $\varepsilon_{ij}$ par similarité sémantique.
- **Détection de H4'.** Une redondance $\varepsilon_{ij}<\tau$ entre deux agents signale des erreurs corrélées. L'arête $(i,j)$ est alors élaguée.
- **Choix monoculture ou chimère.** On choisit la composition $S$ qui minimise $R(S)=\sum_{i\neq j}\mathbb{1}[\varepsilon_{ij}<\tau]$ sous contrainte de budget. Une chimère n'est retenue que si elle abaisse $R$.
- **Spawn d'un explorateur** si $\mathrm{IG}/c>\lambda$, c'est-à-dire si la surprise épistémique par dollar est élevée.
- **Spawn d'un démolisseur Red-Team** si un agent prédit trop bien le juge, soit $\varepsilon_{i,\text{juge}}<\tau_J$. C'est un symptôme de Goodhart.
- **Contrôle de H9.** Chaque délégation reformule la consigne. Si $D_{KL}(\text{consigne}_{\text{parent}}\,\|\,\text{consigne}_{\text{enfant}})>\kappa$, mesurée par `jev`, la branche est coupée.
- **Apprentissage sans poids.** Les matrices $\varepsilon$, $w$ et les prompts gagnants sont stockés en mémoire épisodique et rejoués comme a priori.

2. **Fonction objectif et anti-Goodhart**
$$J=-F_{\text{ext}}+\alpha\frac{\mathrm{IG}}{\$}-\gamma\,I(\hat y_{\text{juge}};\hat y_{\text{essaim}})-\delta\,\overline{D_{KL}}^{\text{délég}}-\eta\,\rho_{\text{err}}$$
- $F_{\text{ext}}$ est l'énergie libre calculée uniquement sur des affirmations vérifiées par arXiv, Semantic Scholar ou Crossref, postérieures à la date de coupure ou masquées. Cela neutralise la récitation de la mémoire paramétrique.
- Le terme $I(\hat y_{\text{juge}};\hat y_{\text{essaim}})$ pénalise la modélisation du juge, donc l'optimisation de Goodhart.
- $\rho_{\text{err}}$ est la corrélation des erreurs entre agents.

3. **Duel décisif de validation M3 ($H_A\perp H_B$)**
- **Budget constant par bras** : 100 USD Claude et 20 USD Gemini.
- **Bras A (SPI)** : la loi proposée.
- **Bras B (essaim fixe)** : topologie en étoile.
- **Bras C (i.i.d.)** : échantillonnage indépendant puis vote.
- **Contrôle négatif D** : SPI avec matrice $\varepsilon$ permutée aléatoirement.
- **Tâche** : 200 questions bibliographiques post-coupure dont la vérité terrain provient des graphes de citations. Le protocole est préenregistré, avec 10 graines.
- **$H_A$** : la précision vérifiée de A dépasse celle de max(B, C) d'au moins 5 points, et $\rho_{\text{err}}(A)<\rho_{\text{err}}(C)$.
- **$H_B$** : la précision de D ne se distingue pas de celle de C, ce qui prouve que le gain vient du signal prédictif et non de la topologie dynamique seule.
- **Analyse** : intervalles de confiance bootstrap à 95 %, avec correction de Holm.
- **Réfutation** : SPI est réfutée si D égale A.
