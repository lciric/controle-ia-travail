BASSIN_MATH: Essaim-EFE-Précision (EEP)

LOI_PROPOSEE: $\pi^*=\arg\min_\pi G(\pi)$, avec $G(\pi)=\underbrace{D_{KL}[q(o|\pi)\|p(o|C)]}_{\text{risque}}-\underbrace{\mathbb{E}_q\,I(s;o|\pi)}_{\text{gain épistémique}}+\lambda\,\rho_{err}(\pi)+\mu\,\delta_{H9}(\pi)$. L'allocation budgétaire suit $B_k=B\,\sigma(-\gamma G_k)$ sous la contrainte $\sum_k B_k\le(100\,\$_C,\,20\,\$_G)$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

Chaque agent $i$ maintient des croyances $q_i(s)$ sur l'état de la question de recherche. Une politique $\pi$ est un graphe orienté (qui parle à qui), auquel s'ajoute une action « spawn ».

- **Codage prédictif hiérarchique** : un parent émet une prédiction $\hat o$ et l'enfant renvoie uniquement l'erreur $\varepsilon=o-\hat o$, pondérée par sa précision $\Pi_i$.
- **Explorateur** : on spawne un explorateur si $I(s;o)$ attendu dépasse le coût en tokens.
- **Démolisseur Red-Team** : on spawne un démolisseur si la précision postérieure $\Pi$ d'une hypothèse dépasse un seuil $\tau$. La sur-confiance déclenche ainsi la falsification.
- **Arbitrage monoculture/chimère** : $\rho_{err}=\sum_{i\ne j}I(e_i;e_j)$ est estimé gratuitement par `jev-1.14.0` sur les vecteurs d'erreurs. La chimère est choisie si $\rho_{err}^{mono}-\rho_{err}^{chim}>\kappa\,\Delta\text{coût}$, ce qui neutralise $H4'$.
- **Apprentissage sans réentraînement** : les mises à jour bayésiennes des précisions $\Pi_i\leftarrow\Pi_i+\eta(\varepsilon_i^{-2}-\Pi_i)$ et des a priori de topologie (paramètres de Dirichlet) sont stockées en mémoire externe.

**2. Fonction objectif et anti-Goodhart**

$$R=-F=\mathbb{E}_q[\ln p(o_{\text{vérif}}|s)]-D_{KL}[q(s)\|p(s)]-\mu\,\delta_{H9}-\nu\,\text{Recit}$$

- $o_{\text{vérif}}$ ne contient que des observations externes : citations résolues via arXiv, Semantic Scholar et Crossref, et prédictions testables.
- $\delta_{H9}=1-\cos(\text{jev}(c_{\text{racine}}),\text{jev}(c_{\text{feuille}}))$ mesure la dérive de consigne entre la racine et les feuilles de délégation.
- $\text{Recit}$ est la fraction d'affirmations non ancrées dans un document récupéré, ce qui pénalise la récitation de mémoire paramétrique.
- **Anti-Goodhart** : le juge est tiré aléatoirement dans un ensemble scellé, ses critères tournent, et 20 % des items ne sont jamais utilisés pour la mise à jour des précisions.

**3. Duel décisif de validation M3**

- **Hypothèses** : $H_A$ : l'essaim EEP obtient un $R$ externe supérieur. $H_B$ : le gain provient du seul budget ou de la diversité.
- **Bras expérimentaux**, tous à budget identique (120 $), sur $N=60$ questions avec graines appariées :
  - (a) EEP adaptatif ;
  - (b) topologie fixe, avec le même ratio chimérique ;
  - (c) agents i.i.d. en vote majoritaire ;
  - (d) **contrôle négatif** : EEP avec des valeurs de $G$ permutées aléatoirement, de sorte que la structure est conservée mais l'information supprimée.
- **Mesure principale** : précision factuelle vérifiée sur les items scellés.
- **Mesures secondaires** : $\rho_{err}$, $\delta_{H9}$ et $\text{Recit}$.
- **Critère de rejet de $H_B$** : $\text{(a)}>\max(\text{b},\text{c})$ et $\text{(d)}\approx\text{(b)}$, évalué par un test de permutation apparié avec correction de Holm, $\alpha=0{,}01$.
- **Réfutation de EEP** : si $\text{(d)}\approx\text{(a)}$, le bénéfice ne vient pas de l'inférence active, et la loi EEP est réfutée.
