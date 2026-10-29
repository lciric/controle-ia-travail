BASSIN_MATH: Structure Adversaire Hirt-Maurer à Délégation Arbitrée Canetti-Riva-Rothblum (HM-CRR)

LOI_PROPOSEE: $G_{t+1}=\arg\min_{G}\,c(G)$ sous deux contraintes. (i) $Q^{(3)}(\mathcal A_t)$ : $\forall A_1,A_2,A_3\in\mathcal A_t,\ A_1\cup A_2\cup A_3\neq V$. (ii) Connectivité de Dolev généralisée : $\forall A_1,A_2\in\mathcal A_t,\ G\setminus(A_1\cup A_2)$ est connexe. La structure apprise vaut $\mathcal A_{t+1}=\mathcal A_t\ \oplus\ \{\,i\sim j \mid \hat\rho_{ij}>\tau\,\}$, où $\hat\rho_{ij}=\Pr[\text{erreur}_i\wedge\text{erreur}_j]-\Pr[\text{erreur}_i]\Pr[\text{erreur}_j]$ est mesuré par `jev-1.14.0`.

1. **Auto-organisation hors-poids**
On remplace le seuil byzantin $f<n/3$ par une *structure adversaire* $\mathcal A$ (Hirt-Maurer). Il s'agit d'ensembles d'agents susceptibles de fauter **ensemble**. L'essaim apprend $\mathcal A$ par détection de collusion : deux agents dont les erreurs sont co-corrélées sur des sondes jev sont fusionnés dans un même ensemble fautif (hypothèse H4′).

Les choix de topologie découlent de deux règles :
- **Monoculture ou chimère.** Tant que $Q^{(3)}$ reste vrai avec une seule famille de poids, on garde la monoculture, moins chère. Dès que $Q^{(3)}$ échoue, on injecte `gemini-4-argon` ou l'autre modèle Claude jusqu'à le restaurer.
- **Qui parle à qui.** Les arêtes minimales satisfont la contrainte (ii). Toute consigne doit traverser au moins un chemin hors de toute paire d'ensembles fautifs, ce qui borne la dérive de consigne (H9).

Le recrutement de sous-agents suit deux déclencheurs :
- **Démolisseur Red-Team.** Si deux prouveurs issus d'ensembles disjoints divergent, une délégation arbitrée CRR s'engage. On bisecte leurs traces de raisonnement jusqu'au premier pas divergent, et seul ce pas est vérifié par jev (coût $O(\log L)$). Si au contraire un consensus apparaît sans aucune divergence, un démolisseur est recruté, car un tel accord est suspect de collusion.
- **Explorateur.** Il est recruté lorsque $\hat\rho$ est mal estimée, avec une variance supérieure à $\sigma^2_{\max}$.

2. **Objectif et anti-Goodhart**
$$J=\sum_k \mathbb 1[\text{pas CRR}_k \text{ validé par jev}^{(\pi_k)}]-\lambda\sum_{i\sim j}\hat\rho_{ij}^{+}-\mu\,\mathrm{Rec}-\nu\,\$_{\text{dépensé}}$$
- $\pi_k$ est une rotation secrète des prompts et des seuils de jev, avec des sondes scellées.
- $\mathrm{Rec}$ pénalise la récitation de la mémoire paramétrique. Toute affirmation doit être ancrée sur un DOI ou un identifiant arXiv vérifié par Crossref ou Semantic Scholar, et datée.
- Le juge ne note jamais une réponse entière, seulement un pas atomique désigné par la bisection. Optimiser le juge revient donc à rendre chaque pas vrai.

3. **Duel décisif ($H_A\perp H_B$), à budget constant (100 USD Claude / 20 USD Gemini)**
- $H_A$ : l'apprentissage de $\mathcal A$ réduit les défaillances corrélées.
- $H_B$ : l'arbitrage CRR réduit à lui seul l'erreur.

Le protocole est un plan factoriel 2×2, $\{\mathcal A \text{ appris}, \mathcal A \text{ permuté aléatoirement}\}\times\{\text{CRR}, \text{vote majoritaire}\}$. Il est comparé à deux témoins : un essaim fixe et un essaim i.i.d. Le contrôle négatif est $\mathcal A$ permuté, à nombre d'ensembles égal.

Les tâches contiennent des fautes plantées corrélées par famille de poids. Deux métriques sont suivies : le taux d'erreur résiduel et la probabilité d'erreur conjointe.

Critère de validation : l'effet principal de chaque facteur doit être significatif ($p<0.01$, avec $\geq 30$ graines), et l'interaction doit être absente, ce qui établit l'orthogonalité de $H_A$ et $H_B$. La loi HM-CRR doit en outre battre les essaims fixe et i.i.d. à coût égal.
