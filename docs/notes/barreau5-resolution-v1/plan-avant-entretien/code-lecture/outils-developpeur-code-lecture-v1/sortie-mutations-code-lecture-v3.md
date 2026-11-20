# Sortie du passage de mutations v3 du code de lecture du barreau 5

Jouée le 20 novembre 2026 par le développeur du code de lecture (Claude Opus 5.5), outil `mutations-code-lecture-v3.py` (même dossier), sur une copie de travail du dépôt sous le bloc-notes de la session (une seule), temporaires sous `/dev/shm` ; copie et temporaires effacés par leur chemin. Aucune donnée : modèle jouet et fichiers fabriqués. Objet : défaire une à une les corrections de la vérification (`verification-corrections-code-lecture-v1.md`, `fb1b7d04…`) : V-1, v-1, v-2.

Témoins sans mutation, tous verts : amorce, blocs (51 passés) ; lanceur (43) ; relecture, sous-ensemble rapide (21, trois du jouet de bout en bout écartés) ; lecture (97) ; sondes (20).

**13 jouées, 13 attrapées**, aucune manquée, aucune introuvable, aucune erreur de l'outil.

| id | fichier | défaut réintroduit | premier essai en échec |
|---|---|---|---|
| J01 | lecture | V-1 : fichiers de scores par jeton non lus | `test_monde_sabotage_issue_s` |
| J02 | lecture | V-1 : fichier de scores par jeton hors du plan admis | `test_scores_par_jeton_un_fichier_par_serie_cas_sain_et_artefacts` |
| J03 | lecture | V-1 : étiquette de série non comparée | `test_scores_par_jeton_un_fichier_par_serie_cas_sain_et_artefacts` |
| J04 | lecture | V-1 : scores par jeton admis dans le fichier de scores | `test_scores_par_jeton_un_fichier_par_serie_cas_sain_et_artefacts` |
| J05 | lecture | V-1 : borne de la taille non comparée | `test_borne_de_la_taille_d_un_fichier_a_l_inventaire_et_a_l_ouverture` |
| J06 | lecture | V-1 : borne absente de la garde d'ouverture | `test_borne_de_la_taille_d_un_fichier_a_l_inventaire_et_a_l_ouverture` |
| J07 | lecture | V-1 : borne absente de l'inventaire de l'instance | `test_borne_de_la_taille_d_un_fichier_a_l_inventaire_et_a_l_ouverture` |
| J08 | sondes | V-1 : borne absente de l'écriture des scores | `test_borne_de_la_taille_d_un_fichier_ferme_cas_sain_et_artefact` |
| J09 | sondes | V-1 : scores par jeton laissés dans le fichier de scores | `test_un_fichier_de_scores_par_jeton_par_serie_sans_les_series_propres` |
| J10 | sondes | v-2 : scores par jeton des séries propres gardés | `test_un_fichier_de_scores_par_jeton_par_serie_sans_les_series_propres` |
| J11 | relecture | v-1 : commit admis sur une branche distante quelconque | `tests/test_lancer_b5f_lecture_v1.py::test_ligne_scores_commit_d_une_autre_branche_refus` |
| J12 | relecture | V-1 : fichiers de scores par jeton hors de la liste blanche des sorties | `tests/test_barreau5_familles_relecture_v1.py::test_sorties_hors_liste_blanche_refusees` |
| J13 | amorce | V-1 : fichiers de scores par jeton hors de la liste blanche de l'amorce | `tests/test_amorce_b5f_lecture_v1.py::test_versement_des_fichiers_fermes_sans_aucune_activation` |

Les premiers essais en échec sont lus dans le bilan JSON (champ `premier_echec`), gardé dans le bloc-notes de la session (non versé : il ne porte que ces états et durées).
