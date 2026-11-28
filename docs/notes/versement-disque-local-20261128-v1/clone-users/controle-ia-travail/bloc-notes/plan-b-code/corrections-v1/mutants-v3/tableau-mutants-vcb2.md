| mutant | ce qu'il simule | résultat | premier échec | fin |
|---|---|---|---|---|
| RQ-17 | témoin sans graine | tué | `tests/test_plan_b_requalifier.py::test_temoin_configuration_remplacee_cas_sain_et_artefact` | 1 failed, 127 passed in 309.57s (0:05:09) |
| VCB-M01 | lecteur : lot_juge absent de la configuration du run accepté (8 par défaut) | ancien texte trouvé 0 fois | — |  |
| VCB-M02 | lecteur : cadre recalculé sans la condition du plafond | tué | `tests/test_plan_b_lecteur.py::test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet` | 1 failed, 135 passed in 119.57s (0:01:59) |
| VCB-M03 | lecteur : cadre recalculé avec le dernier lot incomplet | tué | `tests/test_plan_b_lecteur.py::test_cadre_du_rejeu_plafond_et_dernier_lot_incomplet` | 1 failed, 135 passed in 103.51s (0:01:43) |
| VCB-M04 | lecteur : clés des rangées comparées sans leur ordre | tué | `tests/test_plan_b_lecteur.py::test_tirage_des_lots_recalcule_cas_sain_et_artefacts` | 1 failed, 134 passed in 136.94s (0:02:16) |
| VCB-M05 | lecteur : décalage de D1 non exigé | tué | `tests/test_plan_b_lecteur.py::test_decalages_passes_exiges_au_chemin_et_a_d1[d1-valeur3-décalages réellement passés]` | 1 failed, 131 passed in 126.59s (0:02:06) |
| VCB-M06 | lecteur : R_S illisible non classé | tué | `tests/test_plan_b_lecteur.py::test_classer_depassement_valeurs_illisibles` | 1 failed, 20 passed in 41.86s |
| VCB-M07 | lecteur : grandeur illisible en réserve, non en contrôle (palier lu jusqu'à « fidèle ») | tué | `tests/test_plan_b_lecteur.py::test_grandeur_illisible_au_palier_du_chemin_cas_sain_et_artefacts[g_s]` | 1 failed, 21 passed in 52.49s |
| VCB-M08 | descriptif D-5 : tout caractère de mot compté comme un chiffre | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_descriptifs_lues_suite_avec_chiffre_et_suivies_de_texte[3 (competent)-0-1]` | 1 failed, 128 passed in 8.69s |
| VCB-M09 | repère : passes en demi-précision gardées dans les rangées (D-13) | tué | `tests/test_plan_b_requalifier.py::test_repere_et_rapports_sur_le_jouet` | 1 failed, 117 passed in 196.13s (0:03:16) |
| VCB-M10 | palier de production rejoué avec D1, décalage consigné 0 | tué | `tests/test_plan_b_requalifier.py::test_rejeu_effectif_lots_graines_decalages` | 1 failed, 118 passed in 145.03s (0:02:25) |
| VCB-M11 | annexe A : fin contrôlée sur la première ligne de fin (sans effet ici) | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` | 1 failed, 7 passed in 21.57s |
| VCB-M12 | annexe A : bloc arrêté à la première ligne de fin, non à la dernière | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` | 1 failed, 7 passed in 20.07s |
| VCB-M13 | annexe A : dernière ligne de début, non la première | tué | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_premiere_ligne_de_debut_derniere_ligne_de_fin` | 1 failed, 7 passed in 12.22s |
| VCB-M14 | citation « Épisodes du pilote requalifié » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[épisodes du pilote]` | 1 failed, 72 passed in 53.40s |
| VCB-M15 | citation « Tâches du pilote » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[tâches]` | 1 failed, 73 passed in 76.88s (0:01:16) |
| VCB-M16 | citation « Manifeste des notations rejoué » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[manifeste des notations]` | 1 failed, 75 passed in 52.46s |
| VCB-M17 | citation « Run du pilote requalifié » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[run du pilote]` | 1 failed, 70 passed in 52.75s |
| VCB-M01p | lecteur : lot_juge absent accepté (8 par défaut) (porté, comme les notes VCB) | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[absent]` | 1 failed, 112 passed in 53.49s |
| VCB-M18 | lanceur : commit cité deux fois, deux valeurs, accepté | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[commit du code d'analyse]` | 1 failed, 68 passed in 73.35s (0:01:13) |
| VCB-M19 | lecteur : lot_juge non entier positif accepté | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 113 passed in 57.34s |
| VCB2-M01 | lanceur : aucun contrôle d'échéance avant la conversion et le repère | tué | `tests/test_plan_b_requalifier.py::test_echeance_avant_la_conversion_et_le_repere` | 1 failed, 123 passed in 161.98s (0:02:41) |
| VCB2-M02 | lanceur : aucun contrôle d'échéance avant l'ancrage | tué | `tests/test_plan_b_requalifier.py::test_echeance_avant_l_ancrage` | 1 failed, 124 passed in 169.32s (0:02:49) |
| VCB2-M03 | lanceur : aucun contrôle d'échéance avant le rechargement pour le témoin | tué | `tests/test_plan_b_requalifier.py::test_echeance_avant_le_rechargement_pour_le_temoin` | 1 failed, 125 passed in 174.10s (0:02:54) |
| VCB2-M04 | lecteur : lot_juge exigé mais non employé (8 écrit en dur) | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_de_la_configuration_sert_au_tirage_des_lots` | 1 failed, 119 passed in 63.79s (0:01:03) |
| VCB2-M12 | lecteur : lot_juge nul accepté | tué | `tests/test_plan_b_lecteur.py::test_lot_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 113 passed in 60.30s (0:01:00) |
| VCB2-M05 | citation « Configuration du plan B » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 75.56s (0:01:15) |
| VCB2-M06 | citation « Run des notations rejoué » présente mais jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[run des notations]` | 1 failed, 74 passed in 56.54s |
| VCB2-M07 | citation « Résumé des notations rejoué » jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 71.82s (0:01:11) |
| VCB2-M08 | citation « Invite RS1 » jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 70.75s (0:01:10) |
| VCB2-M09 | citation « Index de l'invite RS1 » jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_chaque_intitule_de_citation_absent_repete_ou_different[index de l'invite RS1]` | 1 failed, 80 passed in 55.42s |
| VCB2-M10 | citation des notations de chaque juge jamais comparée | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 71.20s (0:01:11) |
| VCB2-M11 | citations : seule la première occurrence lue (répétition acceptée) | tué | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` | 1 failed, 67 passed in 71.75s (0:01:11) |
| VCB2-M13 | témoin : graine posée après l'appel | tué | `tests/test_plan_b_requalifier.py::test_temoin_graine_posee_avant_chaque_appel` | 1 failed, 128 passed in 198.51s (0:03:18) |
| VCB2-M14 | témoin : graine constante, la même pour tous les appels | tué | `tests/test_plan_b_requalifier.py::test_temoin_graine_posee_avant_chaque_appel` | 1 failed, 128 passed in 201.64s (0:03:21) |
| VCBb-M01 | lecteur : max_nouveaux_juge absent accepté (garde de présence retirée) | tué | `tests/test_plan_b_lecteur.py::test_max_nouveaux_juge_exige_par_le_lecteur_cas_sain_et_artefacts[absent]` | 1 failed, 120 passed in 63.99s (0:01:03) |
| VCBb-M02 | lecteur : max_nouveaux_juge nul accepté | tué | `tests/test_plan_b_lecteur.py::test_max_nouveaux_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 121 passed in 62.70s (0:01:02) |
| VCBb-M03 | lecteur : max_nouveaux_juge d'une autre forme qu'un entier accepté | tué | `tests/test_plan_b_lecteur.py::test_max_nouveaux_juge_exige_par_le_lecteur_cas_sain_et_artefacts[nul]` | 1 failed, 121 passed in 65.02s (0:01:05) |

Bilan : 1 ancien texte trouvé 0 fois, 37 tué (sur 38)
