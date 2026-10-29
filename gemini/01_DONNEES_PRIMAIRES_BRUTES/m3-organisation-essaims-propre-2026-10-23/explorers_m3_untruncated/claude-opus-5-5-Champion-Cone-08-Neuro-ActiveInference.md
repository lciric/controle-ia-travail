BASSIN_MATH: Habituation Oddball à Surprise Croisée Inter-Familles (HOSCIF)

LOI_PROPOSEE: $b_i^{t+1} = B\cdot\mathrm{softmax}_i\big(\beta\,[S_i^{\times} - S_i^{\circ}] - \lambda\,h_i^t\big)$, avec $S_i^{\times} = -\log q_{\neg f(i)}(y_i)$, $S_i^{\circ} = -\log q_{\varnothing}(y_i)$ et $h_i^{t+1} = \gamma h_i^t + (1-\gamma)\,\mathbb{1}[S_i^{\times} < \theta]$.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**

Inspiré de la négativité de discordance (MMN), chaque agent $i$ émet $y_i$. `jev-1.14.0` y joue le rôle de prédicteur hiérarchique :
- $q_{\neg f(i)}$ prédit $y_i$ à partir des seuls agents d'autres familles de poids. Un agent prévisible par une autre famille n'apporte rien.
- $q_{\varnothing}$ prédit $y_i$ sans contexte documentaire. Il mesure la récitation paramétrique.

Un agent dont la surprise croisée reste basse s'habitue : $h_i$ croît et son budget décroît. Cela pénalise directement la corrélation d'erreurs H4'.

Mutation de topologie :
- Un oddball ($S_i^{\times} > \theta$) dont les citations sont confirmées par Semantic Scholar, arXiv ou Crossref déclenche un sous-agent explorateur d'une autre famille.
- Un oddball non vérifié déclenche un démolisseur Red-Team de famille distincte.
- Les arêtes de communication sont pondérées par $w_{ij} \propto S_{j|i}^{\times}$ : chacun écoute ceux qui le surprennent.

Arbitrage monoculture/chimère : si la surprise croisée moyenne intra-famille est inférieure à la surprise croisée moyenne inter-familles, on bascule en chimère, sinon on reste en monoculture.

Contre la dérive H9 : chaque délégation transporte l'embedding de la consigne $c$. Si $-\log q(c \mid y_{\text{enfant}}) > \theta_c$, la branche est élaguée et réinitialisée.

L'apprentissage hors-poids repose uniquement sur l'état $(h, w, b)$ persistant entre épisodes.

2. **Fonction objectif et anti-Goodhart**

$$R = \underbrace{I(Y;\,G)}_{\text{gain épistémique sur ancres vérifiables}} \;-\; \alpha \sum_i S_i^{\circ}\cdot\mathbb{1}[\text{non vérifié}] \;-\; \kappa\,\mathrm{KL}\big(q(c\mid y)\,\|\,\delta_c\big) \;-\; \mu\,\mathrm{Corr}(\varepsilon_f, \varepsilon_{f'})$$

Ici $G$ désigne les faits du graphe bibliographique. Trois gardes-fous contre Goodhart :
- Le juge n'est jamais optimisé directement : la tête `jev` est tirée aléatoirement parmi $K$ têtes cachées à chaque épisode.
- La récompense provient majoritairement d'ancres externes vérifiables.
- Un agent n'est jamais évalué par sa propre famille.

Les budgets sont plafonnés à 100 USD pour Claude et 20 USD pour Gemini par la contrainte $\sum b = B$ appliquée séparément à chaque fournisseur.

3. **Duel décisif de validation M3 ($H_A \perp H_B$)**

Quatre bras à budget identique, sur 200 tâches de revue de littérature dont la vérité terrain est issue du graphe :
- **A** : HOSCIF.
- **B** : essaim fixe (topologie et budget statiques).
- **C** : allocation i.i.d. uniforme.
- **N (contrôle négatif)** : HOSCIF avec des surprises permutées aléatoirement entre agents. La structure et le coût sont conservés, l'information est détruite.

Métriques :
- rappel de références vraies ;
- taux d'hallucination de citations ;
- corrélation d'erreurs inter-agents ;
- dérive de consigne.

Critère de validation, avec test apparié par permutation, correction de Holm et $\alpha = 0{,}01$ : $A > \max(B, C)$ et $A > N$.

- Si $A \approx N$, l'avantage vient de la seule adaptativité et la loi est réfutée.
- Si $A > N \approx B$, le signal de surprise croisée est causalement responsable du gain.
