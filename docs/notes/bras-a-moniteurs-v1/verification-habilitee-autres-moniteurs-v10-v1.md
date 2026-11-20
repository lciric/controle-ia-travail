# Vérification habilitée des corrections du module des autres moniteurs, version 10 — pièce interne — v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `verification-habilitee-autres-moniteurs-v10-sans-interne-v1.md`, même dossier.

Écrit par le lecteur habilité côté moniteurs du bras A (Claude Fable 5.2, accord de Lazar GO-2026-11-20-21), le 20 novembre 2026, à la demande de la session mère. Classe B : vérification des corrections par le contre-lecteur de la version 9 (`contre-lecture-habilitee-autres-moniteurs-v9-v1.md`, `517fecb3a04f4d67de2155ef9ed21c231856c889c2465544cd2450ea8a58c25e`). Copie `/home/user/bras-a-habilite`, tête `d5602cd57`.

## Verdict : **conforme**

## 1. Pièces (empreintes recalculées)

| pièce | chemin | empreinte |
|---|---|---|
| module, version 10 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v10.py` | `42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v10.py` | `75ef245065ae8407eed36d50290e3ffbef4065de6462e0830f41b5efda374537` |
| notice | `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-autres-moniteurs-v10-v1.md` | `3bb1c02de6039c66cbc3274f74009962588572f9224973d62ead7a6a00667784` |
| pièce sans interne v3 | `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-v8-v3.md` | `6c0f71f6a6b04201acbf4d9c729a3d1131fdb7c714fa1ee683fd2a7ff1d877ae` |
| épreuve par retrait, script et relevé | `…/epreuve-par-retrait-autres-moniteurs-v10-v1/` | `c39cc55a…` ; `d8eef9e2…` (celles de la notice) |
| épreuve de forme, script et six sorties | `scripts/bras_a_v2_habilite_epreuve_de_forme_v10_v1.py` ; `…/epreuve-de-forme-v10-v1/` | `41a377e6…` ; les six empreintes de la notice, retrouvées |

## 2. La différence v9 → v10 (92 lignes de `diff`, lues en entier)

| correction demandée | faite | où |
|---|---|---|
| 1. forme de `comptes_des_lectures` fermée | oui | `exiger_comptes_des_lectures` : deux moniteurs, cinq conditions, cinq clés dans leur ordre, des entiers, clés des deux tables prises dans les listes fermées |
| 1. forme de `preuve_d_ordre` fermée | oui | `exiger_preuve_d_ordre` : date au format du journal ; empreinte de soixante-quatre signes pour les moniteurs lus sur des scores, nulle pour les moniteurs appris ; engagement de la table |
| 2. épreuve de forme à la forme d'une livraison | oui | sorties lues : `comptes_des_lectures` a ses cinq clés ; fichier par unité du cas A, 8 192 lignes, cinq moniteurs, dont 1 024 lignes de l'agrégateur sans pas |
| 3. borne haute finie, de 0 à 1, au cas A | oui | une ligne de la garde de forme du cas |
| 3. artefacts des deux gardes sans morsure | oui | la garde à l'assemblage et le refus d'un nombre non fini mordent maintenant (retraits rejoués) ; le refus est un arrêt de garde nommé |
| 4. phrases de `nombres_rendus` | oui | trois phrases récrites |

**Rien d'autre ne change.** Aucune ligne de `_aire`, `_borne_haute`, `_permuter`, `_conclure`, de l'ajustement, de la notation ni des graines n'est dans la différence. Aucun calcul d'aire, de score, de borne ni de valeur p ne change de la version 9 à la version 10 ; avec ma contre-lecture de la version 9, aucun ne change de la version 8 à la version 10.

## 3. La pièce sans interne v3 : **aucune fuite**

Relue ligne à ligne. La section neuve sur la forme des deux champs ne donne que des noms de clés et des formats ; que deux moniteurs soient appris et trois lus sur des scores est déjà dans le texte de la relance (journal des ouvertures). Une retouche d'exactitude, sans effet de cloisonnement : la version 10 a maintenant un commit, `d5602cd57` (demande 1 et en-tête, qui disent « pas encore »).

## 4. Rejeu

- Essais : `77 passed in 629.37s (0:10:29)`.
- Épreuve par retrait : 67 retraits listés, **65 joués, 65 mordent** ; deux non joués, leur texte n'existant plus (les deux anciennes gardes de premier niveau, remplacées par les fonctions neuves, dont les six retraits mordent). Module remis à l'identique, empreinte vérifiée ; copie propre.
- Épreuve de forme : non rejouée (ses sorties portent une date) ; empreintes des six sorties vérifiées, deux sorties lues.

## 5. Écart déclaré par le développeur, et ce qui reste

- Une vérification de syntaxe passée en ligne à l'interpréteur : contraire à la règle, sans effet sur les pièces (rien d'écrit ; les essais et les retraits rejoués ici ne dépendent pas d'elle). À consigner, sans suite.
- Restent ouverts, sans correction exigée : l'empreinte du module calculée à l'assemblage et non à l'import ; le fichier par unité scellé avant la garde de la sortie (à dire dans la règle de reprise du lanceur) ; les gardes statiques des essais des versions 8 et 9, qui échouent parce que leur liste ignore les versions suivantes.
- Reste à écrire : l'attestation entre la version 7 et la version 10 (demande 24 a), que la mère peut me commander — la comparaison de la version 7 à la version 8 est faite dans ma lecture précédente, celles de 8 à 9 et de 9 à 10 ici et dans la contre-lecture ; seul l'échange par paire est un calcul neuf depuis la version 7, et l'épreuve par retrait de la version 10 le couvre. Le lanceur de l'étape de discrétion n'est pas écrit.

Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Aucun poids chargé, aucun appel payant, aucun refus d'outil. Ni commit ni poussée.
