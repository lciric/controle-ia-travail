BASSIN_MATH: Pilotage par Tenseur de Chentsov à α-Géodésique Budgétaire (TC-αGB)

LOI_PROPOSEE: $\theta_{t+1}=\theta_t+\eta\,G(\theta_t)^{-1}\nabla_\theta\mathcal{J}$, $\alpha_{t+1}=\alpha_t-\eta_\alpha\,\partial_\alpha\|T^{(\alpha)}\|_G^2$, et $b_i\propto\exp\!\big(-\beta\,\lambda_{\min}(G_i)^{-1}\big)$ sur le simplexe budgétaire. Ici $G$ est la métrique de Fisher-Rao des distributions d'étiquettes `jev` produites par l'essaim. $T_{ijk}=\mathbb{E}[\partial_i\ell\,\partial_j\ell\,\partial_k\ell]$ est le tenseur cubique d'Amari-Chentsov. $\alpha\in[-1,1]$ paramètre l'α-géodésique reliant le pôle monoculture au pôle chimère.

1. **Mécanisme d'auto-organisation hors-poids.** Chaque agent $i$ est un point $p_i$ de la variété statistique de ses verdicts, mesurés gratuitement et en continu par `jev`.
   - **Topologie.** L'arête $i\to j$ est conservée si $W_1^{\mathcal{G}}(p_i,p_j)>\tau$. Ce transport optimal est calculé sur le graphe de citations Semantic Scholar : seuls des agents épistémiquement distants dialoguent.
   - **Explorateur.** Un sous-agent explorateur est créé quand $\lambda_{\min}(G)$ est petite. Cette direction plate signale une incertitude non résolue.
   - **Démolisseur Red-Team.** Un démolisseur est créé quand $\|T\|$ est grand. Une asymétrie cubique signale un biais systématique, signature de $H4'$.
   - **Arbitrage monoculture/chimère.** La descente sur $\alpha$ choisit le mélange qui annule la torsion statistique.
   - **Dérive $H9$.** Chaque délégation doit vérifier $W_1(\text{consigne}_k,\text{consigne}_0)<\epsilon$, sinon la branche est élaguée.
   - **Mémoire.** Elle consiste en une archive de paires (topologie, $\theta$), sans aucun réentraînement des poids.

2. **Fonction objectif et anti-Goodhart.**
$$\mathcal{J}=-W_1^{\mathcal{G}}(\mu_{\text{essaim}},\mu_{\text{vérifié}})-\gamma\,\|T\|_G^2-\kappa\,\rho_{\text{fam}}-\nu\,\text{coût}\$$$
   - $\mu_{\text{vérifié}}$ est la masse des nœuds réellement résolus via Crossref et arXiv. Une citation récitée qui n'existe pas coûte un transport maximal.
   - `jev` ne sert que de capteur, avec des seuils recalibrés à chaque génération sur une partition cachée.
   - Toute corrélation $\text{corr}(\mathcal{J},\text{logits}_{jev})>0{,}9$ hors partition déclenche une pénalité de Goodhart.
   - $\rho_{\text{fam}}$ mesure la corrélation des erreurs entre familles.

3. **Duel décisif $H_A\perp H_B$.** Le protocole est un plan factoriel 2×2 à budget strictement constant (100 USD Claude, 20 USD Gemini) sur N=200 tâches pré-enregistrées.
   - **Facteurs.** $H_A$ teste le pilotage par $T$ et $G$ contre une topologie fixe. $H_B$ teste la réallocation budgétaire contre une répartition i.i.d. uniforme.
   - **Contrôle négatif.** TC-αGB est rejoué avec un tenseur $T$ permuté aléatoirement, ce qui conserve la même structure et le même coût.
   - **Métriques.** On mesure le taux d'affirmations vérifiées, $\rho_{\text{fam}}$ et la dérive $W_1$ des consignes.
   - **Critère de réussite.** La loi est validée si le bras complet bat le bras fixe, le bras i.i.d. et le contrôle permuté (bootstrap, $p<0{,}01$). L'interaction $H_A\times H_B$ doit être non significative, ce qui prouve l'orthogonalité des deux effets.
