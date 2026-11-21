# Table des essais de la seconde passe — garde → essai sain → essai artefact — v1

Développeur neuf de la seconde passe, 2026-11-21 (UTC). Texte : `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (`a2bbed7a…`),
« Code neuf » et « Liste d'arrêt », lignes de la v2. R5 : chaque garde codée a un cas sain et un artefact. Les noms sont ceux des
fonctions d'essai (préfixe `test_` omis). Fichiers, tous sous `tests/` :

| sigle | fichier | ce qu'il éprouve |
|---|---|---|
| STAT | `test_lentilles_sondes_bbis_seconde_passe_statistiques_v1.py` | module des statistiques de la seconde passe (`statistiques_v4`) |
| NL | `test_lentilles_sondes_bbis_seconde_passe_nos_lentilles_v1.py` | registre, fiche de rangement, condition de lecture, archive (`nos_lentilles_v1`) |
| LC | `test_lentilles_sondes_bbis_seconde_passe_lecture_comparaisons_v1.py` | lecture côté entrée et comparaisons (`lecture_entree_v1`, `comparaisons_lentilles_v1`) |
| PR | `test_lentilles_sondes_bbis_seconde_passe_phrases_reproduction_v1.py` | phrases, reproduction, déclencheurs (`phrases_v2`, `reproduction_v1`, `audits_v2`) |
| LA | `test_lentilles_sondes_bbis_seconde_passe_lanceur_v1.py` | lanceur et montage (`lanceur_seconde_passe_v1`, `montage_v2`), bout en bout |

Jouets : `tests/lentilles_sondes_bbis_seconde_passe_jouets_v1.py` (registre, fiche, faux fichiers d'ajustement, faux transport),
`tests/lentilles_sondes_bbis_seconde_passe_jouets_v2.py` (monde miniature du lanceur, bâti sur celui de la première passe).

## 1. Lignes de registre et fiche de rangement

| garde | essai sain | essai artefact |
|---|---|---|
| lignes `SCELLEMENT-`, `GO-`, `CODE-LENTILLES-BBIS-V2` exigées | NL `sain_les_trois_lignes_de_la_v2_presentes` | NL `artefact_une_ligne_de_la_v2_absente_refus` (3 cas) ; `artefact_scellement_qui_cite_un_autre_texte_refus` ; LA `montage_et_calcul_refuses_sans_les_lignes_de_la_v2` |
| ligne de l'addendum de concentration : seule, de l'empreinte citée, antérieure à toute clé de la v2 | NL `addendum_present_d_une_ligne_…_accepte` | NL `addendum_artefacts_refus` (absente ; deux lignes ; autre empreinte ; postérieure, par la place puis par l'heure) |
| abandon de la v2, lentilles définitivement non lues, ouverture de la première passe avant le scellement de la v2 | NL `ouverture_de_la_premiere_passe_…_apres_permis` | NL `abandon_ou_non_lues_inscrite_rien_ne_part` ; `ouverture_…_avant_le_scellement_de_la_v2_refus…` |
| ligne `RANGEMENT-NOS-LENTILLES-BBIS` et empreinte de la fiche | NL `sain_fiche_lue_sur_l_empreinte_de_sa_ligne` ; `plusieurs_lignes_de_rangement_la_derniere_designe_la_fiche` | NL `artefact_ligne_de_rangement_absente_rien_ne_part` ; `artefact_fiche_alteree_d_un_octet_arret` |
| révision de 40 caractères ; deux SHA-256 égaux | (cas sain ci-dessus) | NL `artefact_revision_absente_ou_courte_arret` (3 cas) ; `artefact_deux_sha256_differents_dans_la_fiche_arret` |
| verdict d'identité absent | NL `verdict_absent_pour_une_seule_lentille_celle_la_non_lue_l_autre_lue` | NL `artefact_verdict_absent_pour_les_deux_lentilles_rien_ne_part` |
| clé retirée de l'addendum de recopie : ni lue ni exigée | NL `la_cle_retiree_de_l_addendum_de_recopie_n_est_ni_lue_ni_exigee` ; `regle_de_n17_aucune_ligne_d_addendum_de_recopie_…` | (artefact visé : un code qui l'exige ou écrit le motif ; vu par ces deux essais) |
| fiche du code de la seconde passe | LA `fiche_du_code_de_la_seconde_passe_saine_et_artefacts` (sain) | même essai : modules différents non déclarés ; essai opposable de l'archive non cité ; addendum d'une autre empreinte ; module absent de la fiche ; fiche d'une autre empreinte que sa ligne |

## 2. Issue des nœuds N12 et N17 (pièce de `GO-LENTILLES-BBIS-V2`)

| garde | essai sain | essai artefact |
|---|---|---|
| la pièce recopie l'issue du texte, ligne d'accord strictement antérieure au scellement | NL `sain_piece_qui_recopie_les_deux_issues_…` ; `la_forme_du_code_accepte_les_deux_lignes_de_la_piece_inscrite` | NL `artefacts_de_l_issue_des_noeuds_chacun_un_arret_nomme` (9 cas : datée après ; même seconde ; heure absente ; heure illisible ; N12 (b) ; N12 (c) ; N17 (b) à chaque palier ; autre forme) ; `piece_du_go_d_une_autre_empreinte_que_sa_ligne_arret` |
| pièce muette sur un nœud : aucun arrêt, phrase en tête | NL `piece_muette_sur_un_noeud_aucun_arret_la_phrase_est_rendue_pour_la_tete` (N12, N17) | (artefact visé : un code qui se tait ; altération « pièce muette : le code se tait » vue) |
| règle de N12 : ligne du mot de Lazar postérieure à l'avertissement | NL `regle_de_n12_lue_avec_la_ligne_posterieure_…` (cas sain, deux variantes) ; `regle_de_n12_le_mot_n_ouvre_que_la_lentille_qu_il_nomme` | même essai : sans rien ; le seul avertissement ; ligne antérieure ; même seconde ; pièce qui ne nomme aucune lentille |

## 3. Condition de lecture (un cas par mention)

| garde | essai sain | essai artefact |
|---|---|---|
| premier palier, audit toujours dû | NL `premier_palier_avec_audit_lue` | NL `premier_palier_sans_audit_non_lue` (absent ; non scellé ; contrôle manqué) |
| premier palier : empreinte du 18 novembre | (cas sain ci-dessus) | NL `premier_palier_avec_une_empreinte_autre_que_celle_du_18_novembre_arret` |
| libellé du premier palier avec reprise notée ; libellé inconnu | NL `premier_palier_suivi_de_reprise_sur_sauvegarde_notee_lu_comme_le_premier_palier` | NL `un_autre_ajout_au_libelle_ou_un_libelle_inconnu_arret_forme_mal_comprise` (4 cas) ; `non_reajustee_de_l_autre_lettre_forme_mal_comprise` |
| deuxième palier, course rejouée menée en entier | NL `deuxieme_palier_course_rejouee_les_deux_lignes_presentes_lue` | NL `…_sans_la_ligne_d_avertissement_non_lue` ; `…_sans_la_ligne_de_la_lecture_de_la_seconde_course_non_lue` |
| deuxième palier, ajustement seul | NL `…_ajustement_seul_avec_la_ligne_du_mot_de_lazar_lue_phrase_n_ont_pas_ete_refaites` | NL `…_ajustement_seul_sans_la_ligne_du_mot_de_lazar_non_lue` |
| seconde course incomplète | NL `seconde_course_incomplete_sans_…_non_lue_et_avec_elle_lue` (les deux) | (même essai, sans la ligne) |
| fiche muette sur l'achèvement | NL `fiches_qui_disent_menee_en_entier_ou_incomplete_chacune_selon_sa_regle` | NL `fiche_muette_non_lue_sous_son_motif_propre_avec_la_ligne_du_mot_de_lazar_comme_sans_elle` (2 cas) |
| audit dû au deuxième palier | NL `deuxieme_palier_avec_un_declencheur_rendu_sans_audit_non_lue_avec_audit_lue_sans_declencheur_ni_audit_lue` (deux cas sains) | même essai (déclencheur rendu, sans audit) |
| autres mentions ; critère ou verdict non scellés | (l'autre lentille reste lue) | NL `autres_mentions_non_lue_l_autre_lue_motif_ecrit` (4 cas) ; `critere_non_scelle_…_ou_verdict_non_scelle_non_lue` |
| stabilité par couche dans les deux ajustements | NL `couche_non_stable_dans_l_un_des_deux_ajustements_bord` (0,10 : lue) | même essai (0,1001 : non lue, chaque ajustement) ; `valeur_de_stabilite_absente_de_la_fiche_…` |
| couche écartée par la lecture de la seconde course | (couches voisines lues, même essai) | NL `couche_ecartee_par_la_lecture_de_la_seconde_course_non_lue_a_cette_couche` |
| chiffres obligatoires du deuxième palier | (cas sains du deuxième palier) | NL `chiffres_du_deuxieme_palier_absents_de_la_fiche_arret` |
| étiquettes du programme | NL `etiquette_du_programme_la_version_du_critere_reste_la_version_8` | (altération « étiquette `critere` recopiée » vue) |
| phrase du déclencheur (vi) : place et forme | NL `phrase_vi_cas_sain_lue_dans_son_champ_dans_chacune_de_ses_formes_admises` (7 formes × 2 cas) ; `…_sans_declencheur_vi_champ_aucune_rien_n_est_ajoute` ; PR `phrase_du_declencheur_vi_recopiee_apres_la_phrase_permise_sans_un_mot_de_plus` | NL `phrase_vi_artefacts_de_place_chacun_un_arret` (6 cas) ; `phrase_vi_d_une_autre_forme_arret_forme_mal_comprise` (10 cas) |

## 4. Accès et archive

| garde | essai sain | essai artefact |
|---|---|---|
| essai d'un octet de nos fichiers | NL `essai_d_un_octet_de_nos_fichiers_avec_la_cle_a_la_revision_de_la_fiche` | NL `essai_d_un_octet_refuse_arret_aucun_autre_fichier_tente` |
| fichier à la révision de la fiche, jamais de repli | NL `lecture_en_flux_par_le_transport_reprise_comprise` | NL `fichier_introuvable_a_la_revision_arret_aucun_repli` ; LA `fichier_d_une_lentille_introuvable_a_la_revision_arret_avant_tout_flux_long_aucun_repli` |
| noms des variables d'environnement | LA `cas_sain_hf_token_seule` | LA `variable_d_environnement_d_un_nom_de_cle_de_plus_arret_valeur_jamais_lue` (4 noms) |
| extraction en flux | NL `extraction_en_flux_egale_au_chargement_entier` (R, S ; 4 tailles de bloc) ; `sain_archive_dont_l_en_tete_local_porte_les_tailles` | NL `artefact_un_octet_change_arret_sur_l_empreinte_aucune_matrice_gardee` ; `artefact_premier_palier_empreinte_du_flux_differente_de_celle_du_18_novembre_arret` |
| forme de l'archive | (cas sains ci-dessus) ; essai opposable `outils/essai-forme-archive-torch-save-v1.py` | NL `artefact_archive_illisible_arret` (2 cas) ; `artefact_archive_tronquee_arret` ; `artefact_enregistrement_compresse_arret` ; `artefact_data_pkl_qui_n_est_pas_le_premier_enregistrement_arret` ; `artefact_tenseur_non_contigu_arret` ; `artefact_decalage_non_nul_inattendu_arret` ; `artefact_data_pkl_qui_demande_une_classe_hors_de_la_liste_arret` ; `artefact_forme_ou_precision_fausse_arret` |
| `meta` et état | NL `sain_meta_et_etat_conformes` ; `meta_de_s_lue_dans_la_piece_du_18_novembre_champ_meta_seul` | NL `artefact_meta_de_s_chargee_comme_r_arret` ; `artefact_un_champ_de_meta_faux_arret` (4 champs, `rows_sha256` compris) ; `artefact_n_docs_ou_next_doc_faux_arret` ; `artefact_piece_du_18_novembre_d_une_autre_empreinte_arret` ; `artefact_meta_de_s_differente_de_celle_de_la_piece_du_18_novembre_arret` |
| matrices | NL `sain_controles_des_matrices_et_empreintes_relevees` | NL `artefact_matrice_non_finie_arret` ; `artefact_deux_moities_egales_arret` ; `artefact_notre_r_egale_a_l_identite_ou_a_la_lentille_publique_arret` ; `artefact_notre_s_egale_a_notre_r_ou_a_sa_transposee_arret` (2 cas) |
| poids : plongements | LA `plongements_absents_de_l_index_ou_d_une_autre_forme_arret_et_cas_sain` (faux index complet) | même essai (absent ; autre forme) ; `montage_plongements_absents_de_l_index_arret_avant_tout_flux_de_poids` |
| plongements liés | LC `plongements_lies_artefact_iii_sans_objet_ecrit_et_non_lies_artefact_joue` | (les deux cas dans le même essai) |
| corpus des jetons gardés (nœud N-dev-1) | LA `cibles_du_corpus_jamais_celles_de_montage_v1_telles_quelles` (fonction branchée) | même essai (rien de branché : arrêt) |

## 5. Lecture

| garde | essai sain | essai artefact |
|---|---|---|
| notre R par la fonction de la première passe | LC `notre_r_par_la_fonction_de_la_v1_cas_sain_contre_read_du_voisin_et_artefact_couche_suivante` (3 couches) | LC `notre_r_artefact_invisible_ou_ecart_sur_le_cas_sain_arret` |
| garde de la fonction de lecture, égalité aux rangs 10 et 11 | LC `garde_de_lecture_deux_jetons_de_meme_score_aux_rangs_10_et_11_ecart_compte_sans_arret` (scores égaux ; scores nuls) | LC `garde_de_lecture_artefact_ecart_sur_deux_jetons_de_scores_eloignes_arret` |
| notre S contre le chemin indépendant, trois artefacts | LC `notre_s_cas_sain_contre_le_chemin_independant_et_ses_trois_artefacts` (3 couches) ; `notre_s_scores_egaux_au_chemin_independant_en_double_precision` | LC `notre_s_artefact_invisible_arret` (3 artefacts) ; `notre_s_ecart_sur_le_cas_sain_arret` |
| indice de couche de nos lentilles | LC `indice_de_couche_de_nos_lentilles_la_lecture_d_une_sonde_de_couche_l_rend_la_signature_l` (R, S) ; LA `bout_en_bout_lectures_de_notre_r_et_de_notre_s_egales_a_un_calcul_direct_a_la_couche_de_la_sonde` | même essai LC (décalage d'un cran : arrêt) ; NL `indice_de_couche_de_nos_lentilles_un_decalage_d_un_cran_est_arrete` |
| imparité, indépendance à la norme, norme nulle | LC `imparite_de_s` ; `independance_de_s_a_la_norme` | LC `norme_nulle_de_c_k_non_calculable` |
| référence « plongements seuls » | LC `reference_plongements_seuls_k_identite_memes_scores_que_la_lecture_par_s` ; `reference_plongements_seuls_et_temoin_de_couche_meme_regle_de_departage` | (égalité aux rangs 20 et 21 dans le même essai) |
| garde du rapport à ε étendue | LC `rapport_a_epsilon_cas_sain_toutes_au_dessus_rien_n_est_refait_et_bord` | LC `rapport_a_epsilon_une_lentille_sous_100_…` ; LA `bout_en_bout_garde_du_rapport_a_epsilon_nuls_refaits_pour_trois_lentilles_moities_non_calculables` |

## 6. Statistique corrigée et règle de départage (brouillon 4)

| garde | essai sain | essai artefact |
|---|---|---|
| concentration et part de chaque direction nulle sans elle-même | STAT `sain_concentration_et_part_…_egales_a_un_calcul_direct` (3 tailles) ; `sain_formules_exactes_du_point_6_…` ; `sain_direction_lue_et_temoins_juges_sur_les_m_directions` | STAT `artefact_la_statistique_d_origine_rend_une_concentration_strictement_plus_petite` |
| taux à petite taille (M = 19, 128 jetons, 2 000 répliques) | STAT `taux_a_petite_taille_sous_la_statistique_corrigee` | STAT `artefact_de_taux_a_petite_taille_sous_la_statistique_d_origine` |
| comparaison en simple précision ; toute lentille | STAT `comparaison_des_concentrations_en_simple_precision` ; `memes_valeurs_pour_toute_lentille_…` | (égalité après arrondi dans le premier) |
| ses deux arrêts | STAT `arret_nul_de_deux_directions_et_sain_trois_directions_distinctes` | STAT `arret_variance_des_autres_nulle_pour_un_jeton` ; `arret_variance_des_autres_au_plus_dix_puissance_moins_dix_…` |
| listes de vingt | STAT `sain_scores_distincts_liste_d_un_tri_simple_et_comptes_nuls` ; `sain_egalite_ailleurs_qu_a_la_limite_…` (rangs 5 et 6 ; 21 et 22) ; `ordre_dans_la_liste_d_une_direction_nulle_…` | STAT `artefact_egalite_aux_rangs_20_et_21_le_plus_petit_identifiant_est_garde` ; `artefact_un_tri_qui_garde_le_plus_grand_identifiant_ou_l_ordre_d_arrivee_est_vu` ; `trois_jetons_de_meme_score_a_cheval_sur_le_vingtieme_rang` ; `la_liste_ne_depend_pas_de_l_ordre_des_jetons_a_l_entree` ; `signe_moins_…` ; `liste_par_z_meme_regle_sur_une_egalite_de_z` |
| part, familles, recouvrement sur les listes départagées | STAT `part_familles_et_valeurs_p_egales_a_un_calcul_direct_sur_les_listes_departagees` ; LC `recouvrement_des_directions_nulles_egal_a_un_calcul_direct_sur_les_listes_departagees` | STAT `la_seconde_passe_ne_marque_ni_n_arrete_la_ou_la_premiere_le_fait` |
| listes de dix | STAT `dix_premiers_jetons_d_un_pole_egalite_aux_rangs_10_et_11` (cas sain compris) | même essai ; `jetons_communs_par_pole_calcules_sur_les_listes_departagees` |
| pôles à cosinus égal | STAT `poles_sain_colonnes_distinctes_dix_poles_d_un_tri_simple` | STAT `poles_deux_colonnes_egales_…` ; `poles_colonne_egale_a_l_opposee_d_une_autre_…` ; `poles_colonne_orthogonale_…` ; `poles_de_moins_v_…` |
| comptes d'égalités écrits | STAT `comptes_sain_aucune_egalite_tous_a_zero_ecrits` ; LA `bout_en_bout_comptes_d_egalites_ecrits_et_calibration_du_recouvrement` | STAT `comptes_artefact_une_egalite_a_chaque_place_…` ; `comptes_une_egalite_ailleurs_dans_le_classement_ne_compte_pas` ; `comptes_liste_de_moins_de_vingt_et_un_elements_sans_objet_ecrit` (15, 20, 21) |

## 7. Comparaisons, reproduction, phrases

| garde | essai sain | essai artefact |
|---|---|---|
| recouvrement, p conservateur, médiane | LC `recouvrement_sur_des_listes_jouets` ; `p_de_recouvrement_avec_egalites_conservateur_et_mediane` ; `comparer_une_direction_…` | (doublon dans une liste : arrêt, même essai) |
| paires du texte ; notre S comparée à rien | LC `paires_permises_et_notre_s_comparee_a_aucune_lentille_r` | même essai (paires refusées) |
| appariement des nuls | LC `appariement_des_nuls_…_verifie_par_empreinte` | même essai (tirage altéré : arrêt) |
| libellés de comparaison | LC `libelles_de_comparaison_sur_cas_jouets` (8 cas) ; `libelle_du_recouvrement_…_et_non_calculable` | même essai (libellé ou motif inconnu : arrêt) |
| calibration du recouvrement, borne haute seule | LC `calibration_du_recouvrement_nul_sain_sous_la_borne_haute_…` ; `…_un_compte_sous_la_borne_basse_ne_fait_rien_tomber` | premier essai (recouvrements forcés à 20) |
| déclencheurs d'audit de la seconde passe | PR `declencheurs_non_leves_sur_un_cas_sain` | PR `declencheur_memes_vingt_jetons_a_la_couche_7_…` ; `declencheurs_des_comparaisons_leves_et_non_leves` ; `declencheur_des_plongements_seuls_et_de_notre_s_egale_a_notre_r` ; `declencheurs_trop_beau_vingt_directions_concentrees_et_tout_negatif` |
| reproduction | PR `reproduction_tables_jouets_egales_aucune_reserve` ; LA `bout_en_bout_reproduction_de_la_premiere_passe_egale_aucune_reserve` | PR `reproduction_un_libelle_change_reserve_sans_arret_…` ; `reproduction_jetons_changes_ou_seulement_reordonnes` ; `artefact_tables_de_la_premiere_passe_d_une_autre_empreinte_que_leur_ligne_arret` ; `artefact_archive_de_lectures_…_alteree_arret` ; `artefact_empreinte_de_e1_ou_de_e2_differente_entre_les_passes_arret` (2 cas) |
| ouverture d'une table par le code | PR `ouverture_d_une_table_avant_le_scellement_de_la_v2_refus_et_apres_permise` (après) ; NL `ouverture_d_une_table_par_le_code_…` | mêmes essais (avant : refus) |
| première passe lancée et non achevée | PR `premiere_passe_jamais_lancee_la_seconde_la_remplace_et_c_est_ecrit` ; NL `etat_de_la_premiere_passe_lu_au_registre` ; LA `bout_en_bout_premiere_passe_jamais_lancee_…` | PR `artefact_premiere_passe_lancee_et_non_achevee_aucune_phrase_de_la_lentille_publique` ; LA `premiere_passe_lancee_et_non_achevee_aucune_phrase_de_la_lentille_publique_ni_des_logits` ; NL `artefact_ligne_des_tables_sans_ligne_des_entrees_arret_forme_mal_comprise` ; LA `etat_de_la_premiere_passe_en_vigueur_celui_du_montage` |
| phrases permises égales au texte | PR `chacune_des_six_formes_…_egale_octet_pour_octet_a_celle_du_texte` (6) ; `la_phrase_de_notre_s_seule_construite_…` ; `phrase_de_tete_et_phrases_fixes_egales_a_celles_du_texte` | (altération « un mot changé dans une phrase permise » vue) |
| forme d'après le couple des verdicts | PR `la_forme_choisie_d_apres_le_couple_des_deux_verdicts` (9 couples) ; `seuls_les_crochets_se_remplissent_…` | PR `artefact_la_forme_au_pluriel_ecrite_alors_qu_une_seule_lentille_est_a_ce_palier_refus` |
| dernier crochet ; lentille non lue | PR `dernier_crochet_selon_la_course_…` ; `une_lentille_non_lue_recoit_la_phrase_de_son_verdict_…` | (fiche muette : phrase non écrite, note ; même essai) |
| verdict d'ensemble ; une lentille à chaque palier | PR `premier_palier_nos_deux_lentilles_…` ; `cas_mixte_au_premier_palier_…` ; `deuxieme_palier_…` ; `une_lentille_a_chaque_palier_les_deux_lignes_…` (2 sens) | PR `artefact_une_seule_ligne_ecrite_ou_la_liste_entiere_des_reserves_refus` |
| paraphrases interdites | PR `les_phrases_du_code_ne_portent_aucune_paraphrase_interdite_…` | PR `une_paraphrase_interdite_injectee_refus` (6) ; même essai (limite recopiée qui en porte une) |
| phrases de notre R, de notre S, des comparaisons | PR `phrases_de_notre_r_…` ; `phrases_de_notre_s_une_par_libelle_…` ; `famille_par_notre_s_phrase_de_q_distincte_…` ; `une_phrase_par_libelle_neuf_de_comparaison_entre_lentilles` ; `renvois_aux_reserves` | (libellé inconnu, notre S sur les pôles : arrêt, mêmes essais) |

## 8. Procédure et canal des messages d'arrêt

| garde | essai sain | essai artefact |
|---|---|---|
| horloge de 10 heures | LA `horloge_de_10_heures_saine_a_9_heures_arret_au_dela` (9 h) | même essai (10 h et une seconde) |
| espace de 8 Go | même essai LA `espace_sous_8_go_…` (8 Go juste) | LA `espace_sous_8_go_au_depart_arret_sans_rien_creer` |
| bout en bout, une fois par palier | LA `bout_en_bout_premier_palier_…` (5 essais) ; `bout_en_bout_deuxieme_palier_…` (3 essais) ; `ligne_de_commande_phrases_sur_les_tables_fermees` | LA `calcul_refuse_si_une_lentille_lue_n_a_pas_ete_montee_ou_si_le_montage_manque` ; `calcul_refuse_quand_une_lentille_lue_n_a_pas_ete_montee` ; `calcul_refuse_quand_la_fiche_de_rangement_n_est_plus_celle_du_montage` ; `une_lentille_non_lue_l_autre_et_la_lentille_publique_restent_lues_motif_ecrit_en_tete` |
| mêmes clés de graine que la première passe | LA `bout_en_bout_memes_cles_de_graine_que_la_premiere_passe` | (altération d'un tirage : LC, appariement) |
| ligne affichée d'un arrêt ; message cloisonné | LA `une_seule_fonction_decide_de_la_ligne_affichee_…` (arrêt ordinaire) ; `ligne_de_commande_arret_ordinaire_code_3_sans_trace` | même essai (arrêt cloisonné : mots fixes) ; `arret_cloisonne_verse_dans_le_seul_fichier_d_arret_par_l_enveloppe` |
| fichier d'arrêt déjà présent | (bouts en bout : aucun fichier d'arrêt, le calcul part) | LA `garde_du_fichier_d_arret_deja_present_rien_ne_part_rien_n_est_ecrit` |

## 9. Essais des essais (altérations du code, une à la fois, sur une copie isolée)

Outil `outils/essai-des-essais-seconde-passe-v3.py` ; listes `outils/alterations-seconde-passe-*-v1.py` : `statistiques_v4` 10 sur 10 ;
`nos_lentilles_v1` 29 sur 30 (une équivalente) ; `lecture_entree_v1` 10 sur 10 ; `comparaisons_lentilles_v1` 12 sur 13 (une
équivalente) ; `phrases_v2` 15 sur 15 ; `reproduction_v1` 8 sur 8 ; `audits_v2` 8 sur 8 ; `lanceur_seconde_passe_v1` 10 sur 10 (essais de procédure seuls, les bouts en bout n'y sont pas
rejoués) ; `montage_v2` 5 sur 6 (une équivalente : l'empreinte du 18 novembre est déjà comparée à celle de la fiche par la
condition de lecture, et celle de la fiche au flux).

## 10. Non codables, tenues par les rôles (texte, « R5, lignes de la v2 »)

L'ouverture d'une table par une personne ; la transmission d'une phrase à un lecteur ; ce qu'un lecteur a lu avant ; la part de la
règle « jamais la clé d'écriture » que la garde par les noms de variables ne voit pas.
