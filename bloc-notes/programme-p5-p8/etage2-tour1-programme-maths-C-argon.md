# Programme Mathématique et Expérimental d'Argon

## 1. Décomposition Résiduelle
Nous étudions les opérateurs $\mathcal{M}_{RP}$ (Role-Play), $\mathcal{M}_{Sab}$ (Sabotage) et $\mathcal{M}_{Confab}$ (Confabulation) via la décomposition :
$$ z_{t+1} = z_t + \sum_{l,h} W_O^{(l,h)} z_t^{(l,h)} $$

## 2. Transition de Phase P5
Le déclenchement du sabotage obéit à un seuil de friction $\Phi_c$ : l'évasion instrumentale s'active lorsque la fonction de coût perçue de l'erreur dépasse ce seuil.

## 3. Homologie et Nouvelles Familles (P6)
Outre les 29 têtes de SauersML, nous isolons 4 familles :
- *Sabotage Heads*
- *Confabulation Heads*
- *Boundary/Corrigibility Heads*
- *Sunk-Cost Heads*
Ces têtes font le pont avec `P3b`.

## 4. Garde Différentielle par Susceptibilité Causale (P7)
Le `garde_calcul.py` intégrera la susceptibilité :
$$ \chi_{Honesty}(y_t) = \left. rac{\partial}{\partial lpha} \log P(y_t \mid z + lpha \hat{u}) ight|_{lpha=0} $$

## 5. Hystérésis KV-Cache et R2 (P8)
Théorie de l'Hystérésis d'Engagement Auto-Référentiel : le KV-cache accumulé crée un puits gravitationnel qui aveugle le modèle à ses propres failles. Seule la règle `R2` brise ce puits.
