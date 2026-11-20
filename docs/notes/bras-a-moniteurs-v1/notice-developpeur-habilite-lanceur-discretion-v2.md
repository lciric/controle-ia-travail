# Notice — lanceur de l'étape de discrétion du bras A, côté moniteurs, version 2 — v2

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `reponses-sans-interne-demandes-18-19-24a-v2.md`, même dossier.

Écrit par le développeur habilité côté moniteurs (Opus 5.5, mandat v3, `374af248…`), le 20 novembre 2026, sur les treize corrections de la contre-lecture habilitée de la version 1 (`docs/notes/bras-a-moniteurs-v1/contre-lecture-habilitee-lanceur-discretion-v1.md`, `ae7618d1216f6d07f79514777ddf9193d4bbc1e873d0ed1d608ff3dbf3f215c1`, verdict « conforme après ces corrections ») et deux décisions de la mère, commandées sous GO-2026-11-20-21. Classe B. **Se lit avec la notice v1** (`notice-developpeur-habilite-lanceur-discretion-v1.md`, `d1b19bc21d098547f7aba6cd6c6bcb5cadad63d5d2bb5045b36c39a19102f884`), dont tout reste vrai sauf ce qui est dit ici. Copie de travail `/home/user/bras-a-habilite`, tête `1b4d2416a`. Ni commit ni poussée. Aucun fichier de la relance ouvert hors les trois pièces permises ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun poids chargé, aucune dépense. Aucun outil refusé.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| lanceur, version 2 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v2.py` | `c3840745ccaad9b889b676ff7ac2450397f60192b72391e2c42ec37eb5e5ca7e` |
| ses essais | `tests/test_bras_a_v2_habilite_lanceur_discretion_v2.py` | `7729f5bdd09c99af56170663b37899365ef985395d61ec3363b1c9e9141e7760` |
| gabarit de la configuration, version 2 (non jouable : valeurs à fixer nulles) | `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-gabarit-v2.json` | `9a944d74986445deb096f13cc834456e624592a08ab24fd5f164c78d2d1e25e9` |
| erratum 1 de l'attestation (C12) | `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1-erratum-1.md` | `6acac663ec798300211f83e45a1bf1c298f498a58b56716d5b33a1fb03b7d41f` |
| épreuve par retrait, version 2 : script et relevé | `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-lanceur-discretion-v2/` | script `epreuve_retraits_lanceur_v2.py`, `cb7a10354bbb93b760ed30978f678a664587d9f639a9073bd93786d8dc9f0e7d` ; première passe `c3791dd4e1db6afa373ae45e9c94a2df3dba644a41993b7ae787e5f27a0952a1` ; seconde passe `e5c9495a478c54a49c97556ae55c9ca0ced7b06477810476d11a50a452188a5b` |

**Inchangés** (verdicts « conforme » de la contre-lecture) : la préparation v3 (`c0021298…`) et ses essais, le module des autres moniteurs v11 (`e1130dad…`) et ses essais, l'attestation v1 et ses différentiels. Aucune correction ne les touche. La phrase de documentation du module v11 sur le « sous-échantillon du juge » (remarque 5) reste : elle sera retirée à la prochaine version du module, s'il y en a une.

Essais (`PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider <fichier>`) : lanceur v2 `30 passed` ; les trois fichiers ciblés ensemble (lanceur v2, préparation v3, module v11) `42 passed in 43.42s`.

## 2. Corrections

| correction | dans la version 2 | artefact qui mord |
|---|---|---|
| C1 (bloquante) : seconde reprise refusée | le relevé de reprise n'est plus écrit dans le dossier des morceaux, mais sous `production/reprises/reprise-<n>.json` | `test_deux_pannes_de_suite_au_meme_moniteur_puis_fin` : deux pannes au juge, puis fin ; deux lignes de reprise |
| C2 : reprise sans morceau du moniteur en cours non inscrite | à toute relance après l'engagement de la table, un relevé scellé (par moniteur : production inscrite ou non, demandes, morceaux déjà scellés) et une ligne `REPRISE-PRODUCTION-BRAS-A`, y compris quand les deux productions sont faites et aucune ouverture écrite | `test_reprise_sans_morceau_du_moniteur_en_cours_inscrite`, `test_reprise_apres_les_deux_productions_avant_les_ouvertures` |
| C3 : pièce source vérifiée après les ouvertures | `A.charger_piece_source(racine)` à l'étape 1 | `test_piece_source_verifiee_avant_toute_production` |
| C4 : configuration de la base non comparée à sa ligne | une ligne `CONFIG-BRAS-A-V2` exigée, qui désigne la configuration du dossier d'extraction, et ce fichier à l'empreinte de la ligne | `test_configuration_de_la_base_celle_de_la_ligne` (ligne absente ; fichier changé et rescellé) |
| C5 : quatre modules non cités | `chargement_des_modeles`, `format_de_conversation`, `lecture_du_score`, `derniere_position` ajoutés aux modules appelés et au gabarit v2, avec les empreintes de la contre-lecture, recalculées | `test_modules_a_leur_empreinte` |
| C6 : `relever-fins` inutilisable | `lire_la_configuration(…, fins_a_relever=True)` pour la seule sous-commande `relever-fins` : jetons de fin nuls admis, toute autre valeur nulle refusée ; les autres sous-commandes refusent cette configuration | `test_relever_fins_avec_une_configuration_de_releve` |
| C7 : énoncé bordé de blancs | refusé | `test_gardes_des_taches` |
| C8 : douze gardes sans artefact | un artefact pour chacune : tâches (doublon, énoncé absent, empreinte), registre absent, empreinte attendue, table, demandes, bilan et manifeste inscrit à la reprise, configuration du bras, textes de l'extraction, forme de la ligne produite. La relecture de la table par la préparation à la reprise, redondante avec `table_deja_engagee` à la même exécution, devient une assertion (hors R5), sur les octets lus | `test_gardes_des_taches`, `test_gardes_des_fichiers_scelles_et_du_registre`, `test_gardes_de_reprise_des_fichiers_deja_ecrits`, `test_ligne_de_production_et_lecture_complete_hors_forme` |
| C9 : manifeste sans versions ni commit | `versions` (`manifeste.versions()` du dépôt), `code` (commit de l'arbre du lanceur, nombre de fichiers suivis modifiés), `execution`, `determinisme` (réglages rendus par `regler_determinisme` au premier chargement, nuls si aucune carte n'est réglée) | `test_chaine_entiere…` |
| C10 : troisième fenêtre sans réparation | dite ici, partie 4 | — |
| C11 : module d'entrée importé avant sa vérification | `verifier_les_fichiers` d'abord, import ensuite, puis `verifier_les_importes` | `test_module_d_entree_importe_apres_la_verification_des_fichiers` |
| C12 : attestation | erratum 1 | — |
| C13 : pièce sans interne | version 2 | — |
| remarque 4 : nom du manifeste à la seconde | le nom porte l'identifiant de l'exécution | `test_chaine_entiere…` |

## 3. Les deux décisions de la mère

1. **Toutes les sorties de lecture de la course payante sont écrites et scellées.** Pour chaque morceau d'un lot, la lecture complète que rend la lecture avec raisonnement (douze champs : clé opaque, état de la balise, jointure, jointure de la coupe, jetons de contexte, jetons générés, identifiants générés, cas, score, masse, masse faible, anomalie) est gardée par une forme fermée, puis écrite et scellée sous `production/lectures-completes-<moniteur>/complet-<i>.jsonl`, **avant** le morceau des lignes de production. Sous identifiants opaques, dans le dossier de la production, jamais dans le dossier à part qui tient la table. Aucune étape ne les lit, sauf la reprise d'un morceau dont seule la lecture complète a été scellée : le morceau en est tiré sans nouvel appel du moniteur. Une lecture complète bien formée dont la ligne de production est refusée reste scellée (récupérer ce qui est récupérable) ; une lecture hors forme n'est pas scellée et arrête.
2. **Registre propre au bras.** Nom proposé : `registres/bras-a-v2-discretion-v1.md` (clé `registre_du_bras` de la configuration ; trois registres distincts exigés). Il est créé, avec son en-tête, à sa première ligne, et ne porte que les clés neuves du bras : `ENGAGEMENT-TABLE-OPAQUE-BRAS-A`, `MANIFESTE-PRODUCTION-BRAS-A-MONITEUR-BOITE-NOIRE`, `MANIFESTE-PRODUCTION-BRAS-A-JUGE`, `REPRISE-PRODUCTION-BRAS-A`. Le registre des scellements garde les clés de la base (`CONFIG-BRAS-A-V2`, `TABLE-B-BRAS-A-V2`, `ISSUE-MOTS-ET-COUT-BRAS-A`), que la base et le module des moniteurs y lisent, et le journal des ouvertures, que le module y tient : ces lieux sont fixés par des pièces déjà inscrites.

## 4. Fenêtres sans réparation automatique (C10, point 6 de la notice v1 complété)

Une panne entre l'écriture d'un fichier par un module sous le provisoire et sa pose, ou entre la pose de la table et l'inscription de l'engagement, **ou entre la pose d'un manifeste de production et son inscription**, donne un refus à la relance suivante, jamais une suppression : nœud pour la mère. Une panne entre le scellement d'une lecture complète et celui de son morceau est, elle, réparée (partie 3).

## 5. Ce qui reste, sans correction exigée

- Chemin réel (chargement sur la carte, relevé des jetons de fin) éprouvé par doublures seulement ; un essai sur la machine de calcul, avant la course, reste à faire (remarque 3).
- Le module de graines qu'importe le module d'entrée n'est pas cité par empreinte (notice v1, point 10).
- Fichiers anciens sans compagnon (`autres_moniteurs_v7.py`, `autres_moniteurs_v8.py`, `preparation_des_lectures_v2.py`), signalés par la contre-lecture : à sceller par la mère, hors de cette livraison.

## 6. Épreuve par retrait

70 retraits listés, joués un à un, essais ciblés après chaque retrait : les 46 de la v1 (trois récrits pour le texte de la v2), les onze retraits de la contre-lecture (C8) qui portent sur une garde gardée (la douzième, la relecture de la table, est devenue une assertion), et treize retraits des gardes neuves (C3, C4 deux fois, C6, C7, C11, registres distincts, lecture complète trois fois, reprise d'une lecture complète deux fois, relevé de reprise à chaque relance). **Première passe : 69 mordent sur 70.** Le retrait « tâches : énoncé absent » ne mordait pas : la préparation refuse aussi un énoncé vide, et l'essai acceptait son motif. L'essai exige désormais le motif du lanceur. **Seconde passe, sur ce retrait seul : il mord. 70 sur 70.** Fichiers remis à l'identique, empreintes vérifiées (`c3840745…` ; préparation v3 `c0021298…`). Après la première passe, un essai a été ajouté au fichier d'essais (le gabarit v2 cite tous les modules et n'est pas jouable) : il n'affaiblit aucun retrait.
