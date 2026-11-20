# Erratum 1 — attestation « aucun calcul de moniteur ne change de la version 7 à la version 10 » (demande 24 a), v1

**Pièce habilitée.** Écrit par le développeur habilité côté moniteurs, le 20 novembre 2026, sur la correction C12 de la contre-lecture habilitée (`docs/notes/bras-a-moniteurs-v1/contre-lecture-habilitee-lanceur-discretion-v1.md`, `ae7618d1216f6d07f79514777ddf9193d4bbc1e873d0ed1d608ff3dbf3f215c1`). L'attestation v1 (`docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1.md`, `6555abc42fbf0465ddbdc5b9d19e70b52f16ac6ce946fa00729abf621f867c6a`) n'est pas récrite ; cet erratum prime sur les deux points qu'il complète. Classe B. Aucun calcul, aucun différentiel, aucun relevé ne change.

## 1. Partie 2 : une quatrième précision

À ajouter après la précision 3 :

« 4. **Aux cas D et E, l'état rendu change par décision** (GO-2026-11-19-70) : la version 7 rendait le moniteur non calculable et mettait à 1 la valeur p de la famille ; la version 10 le rend calculable avec un motif, et met dans la famille la valeur p haute. Les nombres calculés sont les mêmes. »

Le champ `calculable` passe donc de faux à vrai, et la valeur p qui entre dans la famille de 1 à la valeur p haute : c'est une règle de rendu, qui change l'état de la lecture, non un calcul de moniteur. L'essai d'équivalence, version 2, le vérifie au cas E (partie 4 de l'attestation : la valeur de la famille vaut 1 en v7 et la valeur p haute en v10, les six fois).

## 2. Partie 3 : trois constantes à nommer

La ligne des gardes de forme de la table de la partie 3 omet trois constantes ajoutées par le différentiel, qui ne servent qu'à ces gardes : `CLES_COMPTES_DES_LECTURES`, `_NOMBRES_DE_L_AIRE`, `_NOMBRES_DES_VALEURS_P`. Nature : gardes de forme. Calcul changé : non.

## 3. Ce qui ne change pas

L'attestation de la partie 2 (aucun calcul de moniteur ne change de la version 7 à la version 10 ; un calcul neuf, l'échange par paire), les différentiels (`aacb9f64…`, `b7ac6de6…`) et l'essai d'équivalence (`c24d17ff…`, relevé `f3633613…`) restent tels quels.
