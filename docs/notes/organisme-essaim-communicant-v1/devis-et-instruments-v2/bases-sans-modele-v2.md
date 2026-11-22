# Instrument — bases sans modèle sur la famille MR-2 — note v2

- Note corrigée (D4, D5 de la contre-lecture). **Le script et la sortie sont ceux de la v1, inchangés** :
  - script : `../essaim-devis-instruments-v1/bases_sans_modele_v1.py` (`29276c45e88eea80d3f7c1a33dfa5ef206cdb698c36f54ed04c6be56c33e2775`) ;
  - sortie : `../essaim-devis-instruments-v1/bases-sans-modele-v1-sortie.json` (`4dcdeacf269edadaae2ebcf1329c94682b96e35b393c296bc07d8cc8de2e6825`).
  
  La contre-lecture a rejoué la sortie à l'identique, clé par clé, hors horodatages. Aucun appel, aucune dépense.
- **Versions exactes, lues dans la sortie** : Python **3.13.18**, numpy **2.4.6**. La note v1 annonçait numpy 2.5.3 par erreur : elle avait recopié la version de la conception v4 au lieu de celle de la sortie.
- **Nombre exact de candidats de la base gloutonne** : 226, 225 et 224 aux générations 1, 2 et 3, dans chacun des 12 mondes (champ `trajet_glouton.candidats`). La note v1 disait « environ 227 ».

## 1. Résultats (inchangés)

| base | couverture médiane (min ; max) | conditionnelles couvertes | formes fausses distinctes, médiane |
|---|---|---|---|
| B1, uniforme dans la grammaire | 0 (0 ; 0) | 0 / 14 | 52 |
| B2, K1 plus un effet au hasard | 0,155 (0 ; 0,625) | 0 / 14 | 47,5 |
| B3, glouton borné | **0,690** (0,429 ; 0,857) | 3 / 14 | 4 |

## 2. À préenregistrer (D5)

Deux définitions ont été fixées **après** un essai sur le monde 1, lui-même compté parmi les 12 mondes rapportés. Elles ne valent donc pas comme définitions gelées : elles sont **à préenregistrer**, et à éprouver sur des mondes neufs, avant tout usage décisif.

1. **Couverture** : une composante n'est couverte que par une carte « vraie » (gain au-delà de l'enveloppe de {K1} d'au moins 0,02) qui la capte. La couverture « brute », par l'attribution seule, reste rapportée (B1 1,0 ; B2 0,29 ; B3 0,69). Elle montre pourquoi la définition de C.5 ne suffit pas.
2. **Témoin relâché** : l'attendu « la loi du monde capte toute composante non latente » a été restreint aux composantes **certifiées**, après un échec sur une faible non certifiée. C'est le réglage d'un témoin après son échec ; il doit être préenregistré tel quel ou rejeté.

**L'échec du monde 0 reste visible** : même relâché, le témoin échoue dans le monde 0. La loi du monde elle-même n'y « capte » pas E3, une moyenne certifiée (décalage de sous-population). L'indicateur `controles_tenus` de la sortie vaut `false`. Cet échec n'est pas réparé.

## 3. Rejouabilité (D4)

- **Le premier essai sur le monde 1 (`essai-bases-monde-1.json`) n'est pas rejouable.** Son script (`1eb9ff34…`, consigné dans ce fichier) a été écrasé par la version corrigée, contrairement à R12. Seul l'essai `-b` et la course complète le sont (`29276c45…`).
- Règle désormais tenue : chaque version d'un script prend un nom neuf. Dans cette v2, aucun fichier de la v1 n'est modifié, et chaque fichier changé porte un nom en -v2, ou en -v1 pour une pièce nouvelle.

## 4. Réserves (inchangées)

- Grammaire de B1 approchée.
- Taille des données servies, 2 000 instances, sans pièce.
- Graines de développement publiques.
- Seuil 0 parmi les candidats de B3, régularité publique qui le favorise sur MR-2.
