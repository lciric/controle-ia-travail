# Sortie du passage de mutations v2 du code de lecture du barreau 5

Jouée le 20 novembre 2026 par le développeur du code de lecture (Claude Opus 5.5), outil `mutations-code-lecture-v2.py` (même dossier), sur une copie de travail du dépôt sous le bloc-notes de la session (une seule à la fois), temporaires sous `/dev/shm` ; copies et temporaires effacés par leur chemin après chaque passage. Aucune donnée : modèle jouet et fichiers fabriqués.

## Premier passage (49 mutations)

Témoins sans mutation, tous verts : amorce, blocs (50 passés) ; lanceur (41) ; relecture, sous-ensemble rapide (21, trois du jouet de bout en bout écartés) ; amorce entière à blanc, cas des entrées en deux commits (1) ; lecture (95) ; sondes (18).

**49 jouées, 47 attrapées, 2 manquées** (A07, S03), aucune introuvable, aucune erreur de l'outil.

| id | fichier | défaut réintroduit | état |
|---|---|---|---|
| A01 | amorce | entrées : un seul commit non exigé | attrapée |
| A02 | amorce | entrées : référence à la branche de la formation tolérée | attrapée |
| A03 | amorce | entrées : fichier hors du dossier toléré | attrapée |
| A04 | amorce | activations admises par la voie ordinaire | attrapée |
| A05 | amorce | activations en un seul lot | attrapée |
| A06 | amorce | témoin sans les activations versées | attrapée |
| A07 | amorce | témoin sans la marche menée au bout | **manquée** |
| A08 | amorce | preuve sans les activations gardées | attrapée |
| A09 | amorce | minuterie : destruction sans preuve | attrapée |
| A10 | amorce | commit des entrées non exigé (plan décisif) | attrapée |
| A11 | amorce | texte scellé non comparé | attrapée |
| A12 | amorce | chemins d'adaptateurs existants hors du dépôt admis | attrapée |
| A13 | amorce | entrées non vérifiées dans le déroulé (essai à blanc entier) | attrapée |
| S01 | relecture | offre : disque de 150 Go pour toute pièce | attrapée |
| S02 | relecture | commande : registre de la marche non lu | attrapée |
| S03 | relecture | commande : code du commit non comparé | **manquée** |
| S04 | relecture | commande : commit des entrées hors de leur branche admis | attrapée |
| S05 | relecture | commande : adaptateur existant absent du commit admis | attrapée |
| S06 | relecture | destruction : étiquette non comparée | attrapée |
| S07 | relecture | ligne SCORES-B5F : taille et empreinte non comparées | attrapée |
| S08 | relecture | ligne SCORES-B5F : commit non versé admis | attrapée |
| S09 | relecture | activations gardées : chemin hors de la liste blanche admis | attrapée |
| S10 | relecture | entrées : métadonnées admises | attrapée |
| S11 | relecture | entrées : noms opaques non contigus admis | attrapée |
| S12 | relecture | adaptateur existant sans empreinte admis | attrapée |
| C1 à C8 | lecture, sondes | les huit mutations du contre-lecteur, rejouées telles quelles | toutes attrapées |
| K01 à K16 | lecture, sondes, relecture | chaque correction de la contre-lecture v2 défaite | toutes attrapées |

Les six mutations que la contre-lecture avait vues manquées (C1, C2, C3, C4, C5, C7) sont attrapées par les essais ajoutés ; C8 l'est désormais par un essai rapide des sondes (`test_sonde_d_un_pli_ne_note_que_les_taches_de_son_pli`, 6,6 s), et non plus par le seul jouet de bout en bout.

## Les deux manquées, et leurs essais

- **A07.** Le témoin du versement final était éprouvé sans rien, avec la marche seule, puis avec les trois conditions : jamais avec les activations versées et la marche inachevée. Dans le déroulé, les activations ne sont versées qu'après une marche menée au bout, mais le bloc est une garde à part (R5). Essai complété : `tests/test_amorce_b5f_lecture_v1.py::test_preuve_cas_sain_puis_temoin_final_seulement_si_tout_tient` fait manquer chacune des trois conditions à son tour.
- **S03.** Dans l'artefact « code changé », la session était au commit changé : la garde du code de la session (`exiger_code_de_lecture_au_commit`) le refusait aussi, et la comparaison du code du commit de la marche n'était jamais seule. Cas ajouté : `tests/test_lancer_b5f_lecture_v1.py::test_commande_de_creation_artefacts_aucune_commande[code_change_session_au_code]` (la session revenue au code de `CODE-LECTURE-B5F`, seule la marche porte un code changé).

## Second passage (A07, S03), après ces essais

Copie neuve ; témoins verts (amorce, blocs, 50 ; lanceur, 42 ; relecture rapide, 21 ; amorce entière, 1 ; lecture, 95 ; sondes, 18). **2 jouées, 2 attrapées** : A07 par `test_preuve_cas_sain_puis_temoin_final_seulement_si_tout_tient`, S03 par `test_commande_de_creation_artefacts_aucune_commande[code_change_session_au_code]`.

## Bilan

51 jouées sur les deux passages ; 49 attrapées au premier, les 2 manquées attrapées au second après un essai neuf chacune ; aucune équivalente déclarée dans ce passage. Bilans bruts en JSON gardés dans le bloc-notes de la session (non versés : ils ne portent que ces états et durées).
