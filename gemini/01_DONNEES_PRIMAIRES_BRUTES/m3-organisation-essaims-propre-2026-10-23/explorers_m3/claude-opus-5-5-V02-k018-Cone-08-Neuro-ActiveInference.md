BASSIN_MATH: Réduction Bayésienne des Couvertures de Markov (RBCM)

LOI_PROPOSEE: $A_{t+1} = A_t \setminus \{e : \Delta F_e < 0\} \cup \{\text{spawn}_k : \Sigma_k^{-1/2}\varepsilon_k > \tau\}$, avec $\Delta F_e = F(A_t \setminus e) - F(A_t)$ calculé analytiquement par réduction bayésienne de modèle (BMR) sur les postérieurs gaussiens, et $\varepsilon_{ij} = o_j - g_i(\mu_i)$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

Chaque agent est une couverture de Markov qui ne transmet que ses erreurs de prédiction $\varepsilon$, jamais ses conclusions. Cela freine la récitation paramétrique, car un agent ne peut répéter que ce qui contredit ses voisins.

La topologie $A$ correspond à la structure du modèle génératif de l'essaim. Elle évolue sans réentraînement des poids :
- **Élagage.** Une arête est supprimée si la BMR montre qu'elle n'abaisse pas l'énergie libre.
- **Explorateur.** On engendre un agent explorateur quand l'erreur pondérée par la précision dépasse le seuil $\tau$, ce qui signale une région non modélisée.
- **Démolisseur Red-Team.** On l'engendre quand la précision $\Pi$ d'un nœud croît alors que son erreur reste anormalement faible. Ce symptôme de surconfiance est corrigé par l'injection forcée de surprise.

L'arbitrage entre monoculture et chimère repose sur la covariance d'erreur estimée $\Sigma = \sigma^2[(1-\rho)I + \rho\mathbf{1}\mathbf{1}^\top]$. Si la corrélation intra-famille $\rho_{\text{fam}}$ fait chuter le nombre effectif d'agents $n_{\text{eff}} = n/(1+(n-1)\rho)$ sous celui d'un mélange, la BMR préfère la chimère. Cela traite $H4'$.

Le budget agit comme un a priori de coût sur les politiques : $\ln p(\pi) \propto -\lambda_C \,\text{USD}_{\text{Claude}}(\pi) - \lambda_G \,\text{USD}_{\text{Gemini}}(\pi)$.

**2. Fonction objectif et anti-Goodhart**

$$R = -\Big[\underbrace{\mathbb{E}_q[-\ln p(o^{\text{ext}} \mid s)]}_{\text{surprise externe}} + \underbrace{\mathrm{KL}(q(s) \,\|\, p(s \mid \text{consigne}))}_{\text{complexité / dérive } H9}\Big]$$

- $o^{\text{ext}}$ désigne les citations et affirmations vérifiées via arXiv, Semantic Scholar et Crossref.
- Le juge `jev-1.14.0` n'est qu'un canal d'observation parmi d'autres. Sa précision $\Pi_{\text{jev}}$ est apprise puis plafonnée, ce qui borne son influence face à la loi de Goodhart.
- La consigne racine forme un a priori de précision fixe et maximale. Chaque délégation paie la divergence KL vis-à-vis de cette consigne, ce qui pénalise la dérive $H9$.

**3. Duel décisif $H_A \perp H_B$**

Le budget est identique pour tous les bras (100 USD Claude et 20 USD Gemini), sur 40 tâches pré-enregistrées.

| Bras | Configuration |
|---|---|
| (a) | RBCM |
| (b) | Topologie fixe (DAG hiérarchique) |
| (c) | Échantillons i.i.d. avec vote |
| (d) | Contrôle négatif : RBCM avec $\varepsilon$ permutés aléatoirement |

Le bras (d) conserve la même dynamique de spawn mais détruit le signal de codage prédictif.

**Métriques**
- Taux d'affirmations vérifiables sur un juge tenu à l'écart (seuil `jev` caché et distinct).
- Audit humain aveugle sur 10 % des sorties.
- Corrélation résiduelle des erreurs.
- Dérive sémantique vis-à-vis de la consigne.

**Critères de décision**
- $H_A$ est retenue si (a) surpasse (b) et (c) au seuil $p<0{,}01$ par permutation appariée, et si (d) retombe au niveau de (c).
- $H_B$ (« seule la diversité compte ») est retenue si (d) égale (a).
