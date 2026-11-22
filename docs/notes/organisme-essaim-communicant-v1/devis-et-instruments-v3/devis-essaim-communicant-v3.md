# Devis de l'essaim qui communique — v3

- Sous-agent (Claude Opus 5.5), 22 novembre 2026. **Aucune dépense, aucun appel de modèle, aucun réseau.**
- Place prévue : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v3/`. Tous les chemins ci-dessous sont relatifs à la racine du dépôt ou à ce dossier.
- Calcul : `calcul_devis_essaim_v3.py` (`934e550c…`) → `calcul-devis-essaim-v3.json`. Contrôle des nombres : `epreuves_devis_v3.py` → `epreuves-devis-v3.json`.
- Ces deux scripts sont **ceux du dossier inachevé** (`docs/notes/organisme-essaim-communicant-v1/en-cours-inacheve-2026-11-22-0700/essaim-devis-instruments-v3/`), repris **à l'octet**. Je les ai relus et rejoués. Les deux sorties sont identiques à l'octet à celles du dossier inachevé. Je n'y ai rien changé, donc ils gardent leur nom (R12).

## Verdict

- Le contrôle des nombres attrape désormais les trois artefacts qui passaient en v2 (R2).
- Le facteur « pire v3 / pire v1 » est calculé et non plus écrit à la main : de **1,819 à 3,228** (R4).
- Les montants de la v2 sont inchangés, à l'exception d'une colonne ajoutée : le pire avec la majoration de 25 % de la pièce d'affinage.

## 1. Contrôle des nombres (R2)

Ce qui change dans `calcul_devis_essaim_v3.py` par rapport à la v2 :
- **Une seconde définition plus bas** fait refuser. Toutes les affectations de niveau module sont relues par analyse du code : affectation simple, multiple, annotée ou augmentée, nom repris dans un `for` ou un `with`, fonction redéfinie. Un nom défini deux fois est refusé.
- **Plus de valeur écrite en dur à la place de la pièce.**
  - La marge de 10 %, la majoration de 25 % et le plafond de 105 % de la section C.8 sont lus dans la pièce.
  - Toutes les mentions de la marge doivent porter la même valeur.
  - La majoration et la ligne de la section C.8 doivent être uniques, et une mention voisine fait aussi refuser.
- **Une ligne ajoutée** fait refuser : seconde ligne de l'aiguilleur, seconde mention des tours au pire, seconde ligne C.8.

Épreuves (R5) :

| jeu | cas sains | artefacts | tenues | fichier |
|---|---|---|---|---|
| épreuves de l'auteur, rejouées | 5 (pièce saine, 0,8 pour 0,80, pièce d'affinage, plafonds, simulation v4) | 20 | 25 / 25 | `epreuves-devis-v3.json` |
| outil du relecteur de la v2, **rejoué tel quel** sur la v3 par une cale d'import d'une ligne | R0, R3, R7 | R1, R2, R4, R5, R6, R8, R9 | 10 / 10 | `artefacts-relecteur-sur-devis-v3.txt` |

- Outil du relecteur : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v2/verification-v1/outils/artefacts_relecteur_devis_v2.py`.
- Sur la v2, R2, R6 et R9 étaient **cassés** ; ils sont **tenus** en v3.

Limite : les pièces réelles sont d'abord lues à leur empreinte. Le contrôle des nombres ne joue donc que sur une pièce changée avec une empreinte remise à jour, ce qui est bien le cas qu'il prétend couvrir.

## 2. Montants (USD ; estimation ; pire ; pire avec la majoration de 25 % ; rapport pire v3 / pire v1)

Source : `calcul-devis-essaim-v3.json`, champs `resume_usd` et `rapport_pire_v3_sur_pire_v1`.

| espèce | bas | attendu | haut |
|---|---|---|---|
| Kimi | 1 190 ; 30 807 ; 38 509 ; ×3,228 | 2 809 ; 67 073 ; 83 841 ; ×3,202 | 5 845 ; 112 643 ; 140 804 ; ×3,110 |
| première espèce Claude | 1 944 ; 43 898 ; 54 873 ; ×2,451 | 4 669 ; 95 532 ; 119 415 ; ×2,429 | 10 097 ; 160 454 ; 200 568 ; ×2,355 |
| Fable 5.2 | 3 453 ; 66 340 ; 82 926 ; ×1,982 | 8 389 ; 144 320 ; 180 399 ; ×1,962 | 18 601 ; 242 417 ; 303 021 ; ×1,899 |
| seconde espèce Claude, Astra | 4 207 ; 79 432 ; 99 290 ; ×1,899 | 10 249 ; 172 779 ; 215 973 ; ×1,879 | 22 852 ; 290 228 ; 362 786 ; ×1,819 |
| Argon, Carbon | 3 566 ; 68 211 ; 85 263 ; ×1,968 | 8 668 ; 148 385 ; 185 481 ; ×1,948 | 19 238 ; 249 247 ; 311 559 ; ×1,885 |

- **R4, corrigé** : la v1 sous-estimait le pire d'un facteur de **1,82 à 3,23**, et non de « 1,8 à 2,4 ».
  - Kimi va de 3,11 à 3,23.
  - Le rapport est lu par le script dans la sortie v1 versée au dépôt : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1/calcul-devis-essaim-v1.json`, `8766775c…`, vérifiée contre son compagnon.
- **Majoration de 25 %** (trouvaille de côté de la vérification) :
  - elle est lue à la ligne 44 de `docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md` (`52147009…`) et rendue dans une colonne à part ;
  - **c'est au directeur de dire si elle s'applique** ; je ne l'ajoute pas au pire de référence.
- **Omis, comme en v2** : la machine. Le pire de ce devis ne vaut que sous des gardes du lanceur ; celles du pilote existent désormais (`garde_pilote_essaim_v1.py`), celles du programme non.

## 3. Ce qui ne change pas

- Toutes les estimations et tous les pires de la v2 sont retrouvés à l'identique : mêmes unités, tarifs, relances et section C.8.
- Les nombres sans pièce restent rangés sous `supposes`.
- Le tarif de Kimi reste **repris par citation**, sans relecture de sa pièce primaire : `prix.prop-kimi` de `docs/notes/organisme-auto-conception-v1/calcul-devis-course-auto-conception-v2.json`, `91f5cf8f…`.
