BASSIN_MATH: Routage Pulvinaire à Erreurs Apicales (RPEA)

LOI_PROPOSEE: $g_{ij}=\sigma\!\big(\beta[\,\mathbb{E}\,\Delta F_i(\varepsilon_j)-\lambda\,\rho_{f(i)f(j)}-\mu\,c_j/B_{f(j)}-\eta\,D_{KL}(\pi_j\Vert\pi_0)\,]\big)$. Un agent $j$ transmet son erreur de prédiction $\varepsilon_j$ à l'agent $i$ seulement si $g_{ij}>\tfrac12$.

**1. Mécanisme d'auto-organisation hors-poids**

Chaque agent maintient deux flux.
- Un flux basal : sa prédiction issue de sa mémoire paramétrique.
- Un flux apical : un contexte vérifié, composé des scores `jev-1.14.0` et des citations confirmées via arXiv, Semantic Scholar et Crossref.

Le décalage apical-basal $m_j=\Vert\hat o^{\text{basal}}_j-\hat o^{\text{apical}}_j\Vert$ joue le rôle d'une erreur dendritique. Un « pulvinar » central, implémenté comme un routeur déterministe gratuit, recalcule la matrice $g$ à chaque tour. La topologie se reconfigure donc d'elle-même : les arêtes inutiles s'éteignent.

Les règles de mutation sont les suivantes.
- **Spawn d'explorateur** si $\max_s I(o;s\mid\pi)/c>\theta_E$, c'est-à-dire si le gain épistémique par dollar est élevé.
- **Spawn de démolisseur Red-Team** si $m_j>\theta_R$ alors que la précision affichée $\gamma_j$ est haute. Cette situation signale une confiance non fondée, typique d'une récitation de la mémoire paramétrique.
- **Arbitrage chimère/monoculture** : $\rho_{ff'}$ est la corrélation des erreurs mesurée par `jev` sur des sondes de calibration. Si $\rho_{ff}>\rho_{ff'}$, le terme $\lambda$ impose un routage croisé entre familles, ce qui traite `H4'`.
- **Anti-dérive (`H9`)** : $D_{KL}(\pi_j\Vert\pi_0)$ mesure l'écart entre la consigne de la feuille et la consigne racine $\pi_0$, propagée comme contexte apical immuable.

Le budget est réalloué proportionnellement à $\sum_i g_{ij}\,\Delta F_i$ par famille, sous les contraintes de 100 USD pour Claude et 20 USD pour Gemini. L'apprentissage passe uniquement par $\beta$, $\lambda$, $\theta$ et par une mémoire d'épisodes routés, sans modification des poids.

**2. Fonction objectif anti-Goodhart**

$$R=-\Big[\underbrace{D_{KL}(q\Vert p)}_{\text{complexité}}-\underbrace{\min_{k\le K}\mathbb{E}_q\ln p_k(o_{\text{vérif}})}_{\text{précision}}\Big]-\kappa\,\big|\,\overline{\text{jev}}-\text{audit}\,\big|$$

- Les $K$ têtes de rubrique `jev` sont tirées au hasard et cachées aux agents. Prendre le minimum sur ces têtes empêche d'optimiser un seul juge.
- L'audit humain clairsemé, sur environ 5 % des sorties, pénalise tout écart entre le juge et la réalité.
- Une affirmation sans citation vérifiée reçoit $p=0$.

**3. Duel décisif ($H_A\perp H_B$)**

Le plan est factoriel 2×2 à budget constant : routage {RPEA, fixe} × composition {chimère, monoculture}. On ajoute deux contrôles.
- **Contrôle négatif i.i.d.** : les mêmes appels sont effectués avec un routage aléatoire.
- **Placebo** : RPEA avec matrice $g$ permutée.

Les hypothèses sont les suivantes.
- $H_A$ : le routage RPEA améliore $R$ (effet principal du routage).
- $H_B$ : le gain provient seulement du mélange de familles (effet principal de la composition).

Le protocole porte sur 40 tâches pré-enregistrées avec bootstrap apparié. RPEA est validé si les trois conditions suivantes tiennent :
- l'effet du routage est positif dans les deux compositions ;
- le placebo n'atteint pas le niveau de RPEA ;
- l'interaction routage × composition reste inférieure à l'effet du routage.

La loi est réfutée si l'essaim fixe ou i.i.d. égale RPEA sur $R$ à budget identique.
