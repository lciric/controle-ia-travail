"""Le hasard du défenseur comme preuve — instrument sur mondes simulés (version 2).

Version 2 : corrections de la contre-lecture `docs/notes/chantiers-21-novembre-v1/code-v1/
contre-lecture-code-hasard-defenseur-opus-v1.md` (empreinte ebc0f526…) ; la version 1 reste scellée, inchangée.

Spécification qui fait foi : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/
conception-1-hasard-du-defenseur-v3-consolidee.md` (empreinte 77266183…), section « Ordre d'écriture ».

Un module par pièce :
- `registre_v2` : pièce 1, registre de tirage et engagement (§ 1, garde G2) ;
- `permutation_v2` : pièce 2, noyau de permutation stratifié (§ 2, garde G1) ;
- `monde_v2` : pièce 3, monde planté à trois organismes (§ 4) ;
- `contraste_v2` : pièce 4, contraste apparié et règle du § 3 (garde G5) ;
- `gardes_v2` : pièce 5, gardes G3, G4, G6, G7 (§ 4) ;
- `puissance_v2` : pièce 6, table de puissance simulée et test de mort 1 (§ 4) ;
- `audit_v2` : pièce 7, simulation d'audit et courbes (§ 5) ;
- `inventaire_v2` : pièce 8, gabarit d'inventaire (§ 6).
Erreurs nommées communes : `erreurs_v2`.

Aucun modèle, aucun appel réseau : mondes simulés seulement. Rien n'est revendiqué.

Dilemme joint avec l'audit — phrase de la spécification (§ 5), écrite après la décision 3 du directeur
(GO-2026-11-22-57 : « les quatre nœuds des chantiers du 21 "go" »), mot pour mot :

« **Conséquence, sous supposition** (pièce d'audit indépendante de la condition, dommage total fixé, régime de
signature, premier ordre) [CALCUL]. À dommage total fixé, l'union des deux détections est minimale à λ = 1, où elle
vaut l'audit seul. Sous ces suppositions, le test ne relève pas le pire cas ; il rend la stratégie conditionnelle
dominée. »
"""
