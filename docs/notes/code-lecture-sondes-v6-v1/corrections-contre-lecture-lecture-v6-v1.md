# Corrections après la contre-lecture de conformité du code de la lecture des sondes v6 (barreau 8)

Écrite le 2026-11-24 par le développeur du côté des moniteurs. Pièce de travail. Rapport de contre-lecture : `docs/notes/code-lecture-sondes-v6-v1/contre-lecture-conformite-lecture-v6-sonnet-v1.md` (verdict « conforme », sept mineurs, dix remarques), lu sur la tête `746e80cf`.

## Constats mineurs

| # | constat | suite |
|---|---|---|
| 1 | cascade de LD-2 : actions sans rang honnête non comptées | **porté** : `ld2` écrit `actions_sans_rang_honnete_cascade` et son détail par condition dans `episodes` ; essai à valeur connue (3 actions, une par condition) |
| 2 | LD-0 (j) : différences de rappels sans parts d'alertes de h ni n et k | **porté** : chaque ligne de différence de LD-2 porte `part_d_alertes_h` et `n_et_k_de_h` des deux lectures comparées ; essai |
| 3 | rang de « postérieure » non éprouvé seul | **porté** : essai d'une ligne de code postérieure par l'heure et antérieure par le rang (refus 23) ; mutant « rang ignoré » tué |
| 4 | O-2 et O-4 non éprouvés | **porté** : deux artefacts de plus ; mutants « O-2 retiré » et « O-4 retiré » tués |
| 5 | ex aequo « pour moitié » non éprouvés | **porté** : aire intra-tâche et rang honnête à la main avec égalités ; mutants « < en <= » et « ex aequo à 0 » tués |
| 6 | « dernier état » non éprouvé | **porté** : essai où la dernière action est la plus basse, puis où le dernier pas n'est pas noté ; mutant « argmin » tué |
| 7 | bornes du marquage R4 ; D-15 déclarée « écart » avec tout « oui » | **porté** : 0,96, 0,951 et 0,04 marquées ; 0,95, 0,94, 0,05, 0,06 non ; rappel 1 marqué, 0,99 non ; pièce D-15 « écart » avec tout « oui » refusée (22) ; mutants tués |

Les huit mutants survivants nommés par le rapport ont été rejoués sur le code corrigé : tous tués.

## Remarques

| # | remarque | suite |
|---|---|---|
| 8 | heure de remise de la note v7 sans source scellée | **porté à la session mère** (liste des pièces manquantes, v2) : la mère l'atteste avec sa source, idéalement dans le mandat du lecteur ou une pièce scellée |
| 9 | `exclus.section` non comparée aux mandats | conforme à la lettre ; porté à la session mère (les mandats doivent citer la section) |
| 10 | structure des rôles (s3), (s6), (s7), (s8) non rejouée | **porté** : `forme_depuis_table` rejoue (s3), (s6), (s7), (s8) ; cinq artefacts refusés (20) |
| 11 | brouillon 1 du rapport v5 accepté | **porté** : `SHAS_RAPPORTS_CONFORMITE_ANTERIEURS` (scellé et brouillon 1), refusés à la lecture du bordereau et à son écriture ; essai |
| 12 | chemin de la table neuve non épinglé | **porté** : `Pieces.table_neuve` ; une table citée ailleurs est refusée (20), à la lecture comme à l'écriture du bordereau ; essai |
| 13 | défaut de 12 heures de `Recette.budget_secondes` | laissé : jamais employé en production (le budget vient de la table) |
| 14 | ligne (vii) seulement si une section est changée | laissé : lettre de l'additif 1 |
| 15 | contrôle de n15 et n7 en code mort | laissé : sans effet, garde redondante |
| 16 | `commit_lancement` de D-15 comparé à rien | laissé : lettre de l'additif 1 |
| 17 | ligne (xi) et écart déclaré par l'additif 2 | porté à la session mère (à écrire en tête du verdict par le juge si elle le veut) |

## Points soumis D1 à D7

Tous jugés conformes. D6 (relecture arrêtée écrite comme défaut D3) est dit dans la notice v7, section de l'audit.

## Essais

150 essais du fichier `tests/test_barreau8_moniteurs_lecture_v6.py` passent (145 avant, 5 nouveaux et des artefacts ajoutés aux essais existants).
