# Chiffres pour les devis du code corrigé (essai de vitesse, étalonnage, course) — brouillon de chiffres v1

Pièce de travail (classe C) de l'exécutante v5, 2026-11-22T13:42:15Z, pour le rédacteur des devis (Fable : le devis est une pièce décisive). Aucun résultat lu. Hypothèses déclarées ; **le facteur f du correctif n'est pas mesuré** : c'est l'objet de l'essai de vitesse.

## Bases mesurées (étalonnage du 21-22 novembre, machine 61875617, A100)
- Prix : carte 1,16 + stockage 0,033333 = **1,193 USD/h**.
- Mise en route (création → début du run) : **≈ 70 min** (création 23:29Z, run lancé vers 00:42Z, d'après les dates du disque).
- Rythme ancien code : 27 lots en ≈ 11,5 h → **≈ 26 min par lot** de 8 épisodes avec leurs oracles. Étalonnage entier (28 lots) ≈ 12,1 h + mise en route ≈ **13,3 h, ≈ 16 USD**.
- Écart au devis scellé : 13 h contre 2,44 h attendues → **facteur ≈ 5,3**.
- Arrêt par l'identifiant : 14 s ; redémarrage jusqu'à la poussée : ≈ 5 min.

## 1. Essai de vitesse court (code corrigé contre ancien code, sans valeur de mesure)
- Contenu proposé : une machine, mise en route, puis un lot honnête avec ses oracles par l'ancien chemin et par le nouveau, mêmes graines ; durées seules relevées ; essai « carte » du déterminisme.
- Durée : 70 min + ≈ 26 min (ancien) + ≈ 5 à 10 min (nouveau) + marge 20 min ≈ **2 h** ; coût ≈ **2,4 USD** ; plafond proposé 5 USD.
- Produit : f mesuré (rapport des deux durées), et le déterminisme sur la carte.

## 2. Étalonnage entier, code corrigé
| | f = 3 | f = 5 |
|---|---|---|
| 1 carte | 28 × 26 / 3 ≈ 4,0 h + 1,2 h ≈ 5,2 h ; ≈ 6,2 USD | 2,4 h + 1,2 h ≈ 3,6 h ; ≈ 4,3 USD |
| 4 cartes (7 lots chacune, clés par épisode) | 1,0 h + 1,2 h par carte ; ≈ 8,8 h de carte ; ≈ 10,5 USD ; fini en ≈ 2,2 h | 0,6 h + 1,2 h ; ≈ 7,2 h de carte ; ≈ 8,6 USD ; fini en ≈ 1,8 h |
Réserve 4 cartes : assemblage des lots de plusieurs machines (écart au texte scellé à déclarer), déterminisme entre cartes du même type non garanti au bit près ; la mise en route domine.

## 3. Course de 12 tours, code corrigé
- Devis scellé : 8,8 h attendues (durées anciennes) ; corrigées du facteur 5,3 puis divisées par f : **≈ 9,3 h (f = 5) à 15,5 h (f = 3)**, + 1,2 h de mise en route → **≈ 12 à 20 USD** sur une carte.
- Plusieurs cartes : les tours se suivent (distillation à chaque tour) ; seul l'intérieur d'un tour (32 épisodes) se répartit ; gain ≈ ×1,5 à ×2 au mieux, coût ≈ ×N. Recommandation de chiffre : une carte pour la course.
- 24 tours : ≈ ×1,5 de la ligne 12 tours.

## 4. Ligne de dépense
Déjà dépensé sur GO-2026-11-21-70 : ≈ 16,1 USD (étalonnage coupé) + 0,12 (relance) + stockage de 61875617 à l'arrêt (0,80 USD/jour). Essai + étalonnage 1 carte + course 12 tours, f = 3 : 2,4 + 6,2 + 18,5 ≈ **27 USD** ; total de la ligne ≈ 44 USD, sous la coupure de 55. Avec f = 5 : ≈ 20 USD, total ≈ 37 USD.

## 5. Calendrier au plus tôt (si tout est accordé)
Correctif et contre-lecture le 22 au soir ; essai de vitesse le 23 matin ; ordre ou additif de Fable le 23 ; étalonnage le 23 après-midi ; désignation le 23 au soir ; course partie le 23 au soir ou le 24 matin, finie le 24 ou le 25.
