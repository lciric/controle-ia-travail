BASSIN_MATH: Hodge-Essaim (HE-1)

LOI_PROPOSEE: $f=\nabla\phi+\delta_1^{*}\psi+h$. On spawne un démolisseur sur $\arg\max_{\gamma\in H_1^{pers}}\|h|_\gamma\|$, un explorateur sur $\arg\max \beta_0^{pers}(\text{biblio non couverte})$, puis on applique $w_{ij}\leftarrow w_{ij}\,e^{\eta(\Delta R_{ij}-\kappa\rho_{ij})}$ sous $\sum c_k\le B$.

**1. Mécanisme d'auto-organisation hors-poids**

L'essaim forme un 2-complexe $K$ : les agents sont les sommets, les délégations les arêtes, les triades de vérification croisée les faces. Sur chaque arête, le flux $f_{ij}$ est le gain de confiance que `jev-1.14.0` attribue aux affirmations transmises de $i$ vers $j$.

La décomposition de Helmholtz-Hodge, via $L_1=\delta_0\delta_0^{*}+\delta_1^{*}\delta_1$, sépare trois composantes :
- **le gradient $\nabla\phi$** : une hiérarchie cohérente, que l'on conserve ;
- **le curl** : des contradictions locales, que l'on résout en ajoutant une face, c'est-à-dire un vérificateur tiers ;
- **l'harmonique $h\in\ker L_1$** : des boucles d'écho globales. Elles servent de signature de la dérive de consigne (H9), et c'est là qu'on injecte un Red-Team.

Le choix entre monoculture et chimère se fait spectralement. On construit le graphe de corrélation des erreurs $C_{ij}=\mathrm{corr}(e_i,e_j)$. Si le trou spectral $\lambda_2(L_C)$ tombe sous $\tau$, ce qui signale des poids partagés (H4'), on remplace le nœud le plus central par un nœud d'une autre famille : `gemini-4-argon` contre Claude, ou inversement.

Le budget est alloué par région $U$ selon $c_U\propto\|\mathrm{curl}|_U\|^2+\|h|_U\|^2$, avec le plafond 100/20 USD fixé par fournisseur.

L'apprentissage passe uniquement par la mémoire de topologie et les poids $w$ : aucun réentraînement.

**2. Fonction objectif et garde-fous anti-Goodhart**

$$R=\frac{\mathrm{Pers}\big(H_0,H_1\ \text{des affirmations vérifiées par Crossref/S2}\big)}{\text{USD}}-\alpha\frac{\|h\|^2}{\|f\|^2}-\beta\,\bar\rho_{err}-\gamma\,\mathrm{Halluc}_{DOI}$$

Trois garde-fous limitent l'effet Goodhart :
- `jev` ne fixe que le potentiel $\phi$ ; la récompense est ancrée sur des graphes externes non manipulables.
- Le juge tourne entre seuils tenus secrets.
- On pénalise $\mathrm{corr}(\text{score jev},\ \text{non-vérifié})$. Toute affirmation sans DOI ni arXiv-ID compte comme récitation de la mémoire paramétrique.

**3. Duel décisif ($H_A\perp H_B$)**

Le protocole porte sur 30 questions bibliographiques à vérité terrain cachée, avec quatre bras au budget strictement identique (3 USD Claude et 0,6 USD Gemini par question, soit 108 USD au total) :
- **A** : HE-1 adaptatif ;
- **F** : topologie fixe (planificateur → workers → juge) ;
- **I** : échantillons i.i.d. suivis d'un vote ;
- **N, contrôle négatif** : HE-1 dont les énergies Hodge sont permutées aléatoirement entre arêtes, à calcul identique.

Les deux hypothèses testent des choses distinctes :
- $H_A$ : A > F et A > I. L'adaptation structurelle paie.
- $H_B$ : A > N. C'est le signal spectral spécifique qui compte, et non le simple surcoût de branchement.

Les critères sont préenregistrés :
- **Métriques** : affirmations vérifiées par USD, taux de DOI hallucinés et dérive $1-\mathrm{sim}_{jev}(\text{consigne racine},\text{feuille})$.
- **Test** : Wilcoxon apparié avec correction de Holm.
- **Réfutation** : la loi est réfutée si A ≈ N ou si $\|h\|$ ne prédit pas la dérive (Spearman < 0,3).
