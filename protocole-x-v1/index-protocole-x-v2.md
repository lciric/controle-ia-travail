# Index du protocole X, question « modes de sabotage » (v2)

Écrit le 22 novembre 2026 vers 23:13 UTC par la session du lecteur du coffre (Opus 5.5). Classe C. Remplace, sans le modifier, `index-protocole-x-v1.md`. Rien n'est servi au collisionneur : le service attend un GO sur devis.

## Pièces à servir et à sceller

| Pièce | sha256 | Statut |
|---|---|---|
| `question-collisionneur-modes-sabotage-v8.md` | `047eeddff0285f41938be0ade4927f6d5dacdfe98f348a05f61bf97aaf53e80a` | **question à servir** ; seuil et coupe conformes à GO-2026-11-22-151 et -152 |
| `porte-admissibilite-modes-v5.md` | `29c8a3c1dcec0a8b1f32644e99bf89c56c2c37697ef75b0b5c03c31c2b4bac83` | **porte scellée** (compagnon `.sha256`), vise la v8 ; à appliquer telle quelle |

## Fin de la chaîne (après l'index v1)

| Pièce | sha256 | Statut |
|---|---|---|
| `mots-de-lazar-22-novembre-23h-seuil-et-coupe-v1.md` | `366c39aa143757aac4cf6c2eef1514dfcc10bb4b99c62917158119f850164424` | mots de Lazar, GO-2026-11-22-151 et -152 |
| `porte-admissibilite-modes-v4.md` | `047c0384b91f8902773266b2f9808d0ca6ca1281ddff2b0fc63608983693d9c6` | auteur Opus ; remplacée par la v5 |
| `note-corrections-porte-v3-v4.md` | `fd7c684ecff20fb4e5711c2fe3f9edea33886cd6184b41d1e21c75b449fc44e2` | note de l'auteur |
| `contre-lecture-opus-v1/verification-porte-v4-opus-v1.md` | `8ce68043b33a5153185fa64ece32b01aeb26fceb9d461c17eafc61d09c1cbddd` | contre-lecteur neuf : prête à sceller, 0 bloquant, 2 mineurs (en-tête) |
| `diff-porte-v4-v5.diff` | `74698ca568ebe62828dbcc044dcb54cd492437d7a7167b043cc62c840152b7aa` | les deux mineurs corrigés à la main par la session du lecteur, en-tête seulement ; le contre-lecteur a jugé qu'un diff suffit comme vérification |

## Ce qui reste avant le service, à la mère

- Vérifier que la limite de longueur d'un tour du collisionneur admet six fiches de 500 mots et la fin de réponse (environ 3 300 mots ou plus).
- Verser hors coffre la source 19 de la v8, la question v5 servie le 22 novembre (`c8cd5f2c8370e0251d9b0e282a9ccbb6a78c54db1fd2bb99ac375fef2ae77a26`). La source 20 reste au coffre.
- Obtenir le GO de Lazar sur devis.
- Quand le devis de G1 existera, faire le contrôle du seuil (porte v5, en-tête).
