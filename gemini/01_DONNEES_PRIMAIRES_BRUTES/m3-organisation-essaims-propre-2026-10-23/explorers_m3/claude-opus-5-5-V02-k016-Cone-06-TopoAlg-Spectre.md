BASSIN_MATH: Faisceau-Obstruction Persistant (FOP-2)

LOI_PROPOSEE: $\dot{A}_{ij} = -\eta\,\partial_{A_{ij}}\big[\langle x, L_{\mathcal F}x\rangle - \lambda\,\mathrm{Pers}(H^1_{\mathcal F}) + \mu\,\rho_{ij}\big]$. Ici $L_{\mathcal F}=\delta^{\top}\delta$ est le laplacien de faisceau cellulaire. On assigne un explorateur à chaque classe persistante de $H_1(\mathrm{VR}_\varepsilon(\text{biblio}))$ et un démolisseur à chaque classe persistante de $H^1_{\mathcal F}$.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**
   - **Faisceau de croyances.** Chaque agent $i$ porte une fibre $\mathcal F(i)=\mathbb R^d$, qui encode ses affirmations via l'embedding de `jev-1.14.0`. Chaque arête porte une restriction $\mathcal F_{i\trianglelefteq e}$, apprise par moindres carrés sur les traductions de consignes. Ces restrictions mesurent la dérive H9 comme le défaut de recollement $\|\delta x\|$.
   - **Démolisseurs.** Les sections globales, $\ker L_{\mathcal F}$, forment le consensus. Les classes de $H^1_{\mathcal F}$ à forte persistance, filtrées par seuil de confiance, sont des contradictions robustes. Chacune déclenche un démolisseur Red-Team ciblé sur son support.
   - **Explorateurs.** Les trous $H_1$ persistants du complexe de Vietoris-Rips sur le graphe arXiv/Semantic Scholar/Crossref couvert sont des zones encerclées mais non lues. Chacun déclenche un explorateur, ce qui combat la récitation paramétrique.
   - **Monoculture ou chimère.** $\rho_{ij}$ est la corrélation d'erreurs mesurée par jev. Si $\dim\ker L_{\mathcal F}$ est grand alors que $\rho$ est élevé, il s'agit d'un faux consensus (H4'). On recâble alors l'arête vers une famille de poids différente : Claude vers Gemini.
   - **Budget.** L'allocation est $b_k\propto \mathrm{pers}_k/\mathrm{coût}_k$, sous les contraintes de 100 USD pour Claude et 20 USD pour Gemini.
   - **Mémoire évolutive.** Elle est stockée dans les restrictions et les diagrammes de persistance, sans modifier aucun poids.

2. **Fonction objectif et anti-Goodhart**
   $$R=\underbrace{\Delta\,\textstyle\sum_k \mathrm{pers}_k(H^1_{\mathcal F})_{\text{résolues}}}_{\text{contradictions tuées}}+\alpha\,\Delta\beta_1^{\text{biblio}}{}^{-}-\beta\,\mathrm{tr}(\Sigma_\rho)-\gamma\,W_\infty\big(\mathrm{Dgm}_{\text{juge}},\mathrm{Dgm}_{\text{juge}'}\big)$$
   - Le dernier terme est la distance bottleneck entre deux juges indépendants : jev et un ensemble tenu secret. Il pénalise toute optimisation spécifique à un seul juge.
   - Une résolution n'est comptée que si elle est vérifiée par citation Crossref existante.

3. **Duel décisif de validation M3 ($H_A\perp H_B$)**
   - **$H_A$ :** FOP-2 adaptatif.
   - **$H_B$ :** même essaim, mais topologie fixe en étoile, ou spawns i.i.d. uniformes avec composition familiale tirée au hasard.
   - **Contrôle négatif :** FOP-2 avec diagrammes de persistance permutés, donc la même dynamique sur une topologie aléatoire.
   - **Conditions identiques :** budget de 120 USD, 40 tâches de revue `controle-ia` avec fausses citations et contradictions plantées en aveugle, et 5 graines.
   - **Mesures :** rappel des erreurs plantées, taux d'hallucination bibliographique et dérive de consigne $\|\delta x\|$ en fin de chaîne.
   - **Statistique :** test de permutation apparié, avec $p<0{,}01$ et un effet de Cliff supérieur à 0,3.
   - **Critère de réfutation :** la loi est réfutée si le contrôle permuté égale $H_A$.
