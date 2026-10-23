BASSIN_MATH: Essaim-Friston à Précision Décorrélée (EFPD)
LOI_PROPOSEE: topologie $\pi^* = \arg\min_\pi \; G(\pi) = \underbrace{-\mathbb{E}_{q}[\,I(o;\theta\mid\pi)]}_{\text{gain épistémique}} - \underbrace{\mathbb{E}_q[\ln p(o\mid C)]}_{\text{valeur pragmatique}} + \beta\,\mathrm{KL}[q(c_t)\,\|\,p(c_0)] + \gamma\,\sum_{i<j} I(\varepsilon_i;\varepsilon_j)$, sous contrainte $\sum_i \text{coût}_i \le B$ (100 USD Claude, 20 USD Gemini) via multiplicateur $\lambda_B$.

**1. Auto-organisation hors-poids.** Chaque agent $i$ porte un modèle génératif $p_i(o,s)$ ; l'essaim est un graphe hiérarchique de codage prédictif : les nœuds supérieurs envoient des prédictions (consigne décomposée), les inférieurs renvoient des erreurs $\varepsilon_i$ pondérées par précision $\Pi_i$. Règles de mutation :
- Spawner un **explorateur** quand l'incertitude $H[q(s)]$ domine $G$ (terme épistémique > seuil) ; il interroge arXiv/Semantic Scholar/Crossref, dont la nouveauté par rapport à la mémoire paramétrique est mesurée par `jev-1.14.0` (coût nul).
- Spawner un **démolisseur Red-Team** quand l'erreur de prédiction sur le juge chute anormalement vite ($\dot\varepsilon_{\text{juge}} \ll 0$ à $H[q]$ constant) : signature de Goodhart.
- **Chimère vs monoculture** : croiser les familles de poids ssi $I(\varepsilon_i;\varepsilon_j)$ intra-famille dépasse la perte de cohérence inter-famille (H4').
- La **dérive de consigne** (H9) est le terme $\beta\,\mathrm{KL}$ : chaque délégation doit renvoyer sa consigne reconstruite, comparée à $c_0$ par `jev`.
L'apprentissage est bayésien hors-poids : mise à jour de $q(\pi)$ et des précisions $\Pi_i$ par descente sur $G$, mémorisée en contexte partagé.

**2. Fonction objectif anti-Goodhart.**
$R_t = \Delta I_{\text{épist}}^{\text{jev}} + \mathbb{E}[\ln p(o\mid C)]_{\text{sondes cachées}} - \beta\,\mathrm{KL}(c_t\|c_0) - \gamma\sum I(\varepsilon_i;\varepsilon_j) - \lambda_B\,\text{coût}$.
Le juge `jev` est non génératif, figé, et évalué sur 20 % de sondes aléatoires non révélées ; toute hausse de score sans hausse de $\Delta I_{\text{épist}}$ est pénalisée (Red-Team déclenchée).

**3. Duel $H_A \perp H_B$.** Préenregistré, 60 tâches `controle-ia`, budget identique 120 USD par bras.
- $H_A$ : EFPD adaptatif.
- $H_B$ : topologie fixe (étoile) et échantillonnage i.i.d. à $N$ égal.
- **Contrôle négatif** : EFPD avec $R_t$ permuté aléatoirement (mutations sans signal).
Métrique : score `jev` sur sondes cachées + révision humaine en aveugle ; test apparié de Wilcoxon, $\alpha=0{,}01$. Prédiction falsifiable : $H_A > H_B > $ contrôle, avec $\sum I(\varepsilon_i;\varepsilon_j)$ et $\mathrm{KL}(c_t\|c_0)$ strictement inférieurs sous $H_A$ ; sinon la loi est rejetée.
