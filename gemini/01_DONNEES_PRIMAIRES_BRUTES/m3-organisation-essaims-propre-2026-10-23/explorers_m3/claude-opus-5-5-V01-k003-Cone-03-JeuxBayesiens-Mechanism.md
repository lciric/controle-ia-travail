BASSIN_MATH: Marché-VCG à Score Logarithmique Persuadé (MVSLP)

LOI_PROPOSEE: $b_i^{t+1} = b_i^t + \eta\big[\log p_i(\tilde\omega) - \log p_{-i}(\tilde\omega)\big] - c_i^t$. Le budget d'un agent croît de sa contribution marginale VCG au score propre du marché, moins son coût d'inférence.

**1. Mécanisme d'auto-organisation hors-poids**

- **Marché d'information.** Chaque agent $i$, de type $\theta_i = (\text{famille}, \text{rôle}, \text{contexte})$, joue un jeu bayésien. Il « trade » dans un marché LMSR (Hanson) portant sur des propositions vérifiables $\omega$.
- **Allocation des sous-tâches.** Elle se fait par enchère VCG : la tâche $k$ revient à l'agent maximisant $\Delta I_k / \text{coût}$, et il paie l'externalité imposée aux autres.
- **Spawn d'un explorateur.** On en crée un si la valeur d'information espérée $\mathbb{E}[\Delta H(\omega)]$ dépasse le prix marginal.
- **Spawn d'un démolisseur Red-Team.** On en crée un si l'entropie du marché $H(p) < \epsilon$ alors que l'accord inter-familles est faible, ce qui signale une sur-confiance.
- **Monoculture ou chimère.** Le VCG rémunère la covariance négative des erreurs. Une copie monoculturelle redondante (`H4'`) a une contribution marginale nulle et s'éteint donc. Les chimères survivent tant que $\rho_{ij}^{err} < \rho^*$.
- **Topologie.** Une arête $i \to j$ est conservée si elle fait gagner de l'information. La mémoire évolue sans réentraînement : les prompts et les rôles sont mutés et sélectionnés selon $b_i$.
- **Dérive de consigne (`H9`).** Chaque délégation est scorée par `jev-1.14.0` sur la fidélité de la consigne reconstruite.

**2. Fonction objectif et anti-Goodhart**

$$R = \sum_i \big[\log p_i(\tilde\omega) - \log p_{-i}(\tilde\omega)\big] - \lambda \sum_i c_i - \mu \sum_{i<j} \rho_{ij}^{err} - \nu\, D_{H9}$$

- **Résolution $\tilde\omega$.** Elle est tirée selon un schéma de persuasion de Kamenica-Gentzkow engagé à l'avance : avec une probabilité cachée $q$, par vérité API (arXiv, Semantic Scholar, Crossref, DOI résolu) ; sinon, par `jev`.
- **Effet anti-Goodhart.** L'agent ignore quel juge résout. Optimiser `jev` seul n'est donc pas un équilibre.
- **Anti-récitation.** Une affirmation sans identifiant vérifiable reçoit le score $\log \epsilon$, ce qui rend la récitation de la mémoire paramétrique strictement dominée.

**3. Duel décisif ($H_A \perp H_B$)**

- **Hypothèses.** $H_A$ : le MVSLP réduit la log-loss sur des propositions tenues à l'écart. $H_B$ : un essaim fixe ou i.i.d. fait aussi bien.
- **Bras comparés**, à budget identique (100 USD Claude et 20 USD Gemini) :
  - (a) MVSLP ;
  - (b) topologie fixe ;
  - (c) échantillonnage i.i.d. ;
  - (d) contrôle négatif : MVSLP avec des récompenses permutées aléatoirement, qui doit retomber au niveau de (c).
- **Protocole.** On utilise $N = 300$ propositions préenregistrées, vérifiables via les API. Le critère principal est la log-loss évaluée par un validateur caché distinct de `jev`.
- **Écart de Goodhart.** On le mesure comme $|\text{score}_{jev} - \text{score}_{caché}|$.
- **Critère de rejet de $H_B$.** Il faut que (a) l'emporte sur (b), (c) et (d) par bootstrap apparié avec $p < 0{,}01$, que l'écart de Goodhart reste stable et que (d) ne soit pas significativement différent de (c).
