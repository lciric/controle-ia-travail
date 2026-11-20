# Table des essais — lecture des directions des sondes de l'étape B bis par la lentille publique — v1

Chaque garde codée du texte scellé (`prereg/lecture-sondes-bbis-par-lentilles-v1.md`, `ca5066d7…`, « Liste d'arrêt » et « Code neuf »)
a un essai sur un cas sain et un essai sur un artefact (R5). Fichiers : `tests/test_lentilles_sondes_bbis_<famille>_v1.py` ; les noms
ci-dessous sont ceux des fonctions, sans le préfixe `test_`. Sortie : `sortie-essais-v1.txt` (dernière ligne : tous verts). Jouets
seulement : registres, archives et JSON aux formes (a), (b), (c), Llama miniature construit localement (32 blocs, largeur 32), fausse
lentille, faux code voisin (dépôt git local), réseau simulé, fausse clé.

## Entrées (`entrees`)

| garde | essai sain | essai artefact |
|---|---|---|
| liste blanche de E-2 | `liste_blanche_champs_permis` ; `sain_vingt_sondes_forme_c` | `liste_blanche_refuse_champ_exclu_valeur_d_echec_et_ordre2` (16 cas : champ exclu, valeur d'un `echec`, `ordre2`, `enc.reglage` entier) ; `liste_blanche_presence_et_cles_refusees_hors_liste` |
| rien d'exclu ne sort (régularisation comprise) | `extrait_ne_porte_aucun_champ_exclu_ni_regularisation` ; `bout_en_bout_aucune_regularisation_ni_champ_exclu_dans_les_sorties` (procédure) | les mêmes, sur des fichiers jouets qui portent tous les champs exclus |
| analyse de `enc.reglage` | `reglage_du_lecteur_famille_et_couche_seules` (`attention-c15-l2_0.01`) | `reglage_mal_forme_arret_sans_imprimer_la_chaine` (6 cas ; le message ne porte pas la chaîne) |
| E-1 clé par clé | `e1_seules_les_entrees_sonde_et_enc_sont_decodees` (archive qui porte `direction0_*` et `direction1_*` ; accès espionnés) | `e1_demande_d_une_entree_direction_refus` ; `e1_nom_d_entree_inconnu_arret` |
| rien avant `VERDICT-BBIS` | `sain_vingt_sondes_forme_c` | `refus_avant_verdict_bbis_sans_rien_ouvrir` ; `calcul_refuse_avant_verdict_bbis_sans_ouvrir_les_sondes` (procédure) |
| lignes de registre | `registres_seules_les_cles_nommees_sortent` | `scores_bbis_absente_ou_multiple_refus` ; `cle_du_registre_propre_absente_refus` (3 clés) ; `calcul_sans_les_cles_du_registre_propre_refus` et `montage_sans_les_cles_du_registre_propre_refus` (procédure) |
| empreinte de chaque sonde | `empreinte_recalculee_egale_celle_du_code_des_sondes` (contre `sondes.familles`) | `poids_altere_arret` ; `nom_du_lecteur_honnete_mal_reconstruit_arret` |
| couche, famille, agrégation | `sain_vingt_sondes_forme_c` | `couche_famille_agregation_hors_de_l_ensemble_arret` (5 cas) ; `couche_du_lecteur_hors_de_l_ensemble_arret` ; `cellule_ou_pli_manquant_arret` |
| chemins jamais ouverts | `ouvrir_un_fichier_de_scores_refus` (E-1 permis) | `ouvrir_un_fichier_de_scores_refus` (scores, planchers, relecture, manifeste, lecture, autre course) |
| formes (a), (b), (c) | `forme_a_sonde_et_lecteur_non_lus_sans_arret` ; `forme_b_lecteur_non_lu_sans_arret` ; `sain_vingt_sondes_forme_c` | `artefact_enc_absent_sans_echec` ; `artefact_entree_enc_w_presente_alors_que_enc_echec_existe` ; `artefact_sonde_q_absente_pour_la_famille_attention` ; `artefacts_autres_combinaisons` (4 cas) |
| empreintes de E-1 et de E-2 | `sain_vingt_sondes_forme_c` | `un_octet_change_arret` (E-1, E-2) ; `e2_egal_a_son_compagnon_mais_pas_a_scores_bbis_arret` |
| récupération des quatre chemins seuls | `recuperation_seuls_les_quatre_chemins_sont_telecharges` | la même : les contenus des scores et de la relecture restent absents du clone partiel |

## Montage (`montage`)

| garde | essai sain | essai artefact |
|---|---|---|
| clé lue par son nom, jamais imprimée | `cle_presente_lue_par_son_nom_et_masquee` ; `environnement_enfant_sans_la_cle` | `cle_absente_ou_vide_arret_sans_impression` (4 cas) ; `montage_cle_absente_arret_avant_toute_requete` |
| mode de débogage | `sans_debogage_sain` | `mode_de_debogage_par_variable_arret` (4) ; `mode_de_debogage_par_journalisation_arret` (4) ; `mode_de_debogage_http_client_arret` ; `montage_mode_de_debogage_arret` |
| essai d'un octet | `essais_un_octet_sains` ; `cibles_du_corpus_une_par_jeu_de_donnees` | `essai_un_octet_refuse_par_un_hote_simule_arret` (3) ; `fichier_a_porte_refuse_avec_une_mauvaise_cle_arret` ; `montage_essai_un_octet_refuse_arret_avant_tout_flux` ; `transport_reel_n_envoie_la_cle_qu_a_hugging_face` |
| pointeur d'un fichier de poids | `identifiant_git_connu_et_pointeur_de_la_lentille_publique` (valeurs réelles du texte) | `pointeur_identifiant_git_faux_ou_taille_fausse_arret` ; `montage_pointeur_d_un_fichier_de_poids_faux_arret_avant_son_flux` ; `sha256_par_interface_et_fichier_sans_empreinte_de_stockage` |
| lecture en flux | `lecture_en_flux_tenseurs_egaux_a_un_chargement_entier` (4 tailles de bloc ; égalité exacte avec `safetensors`) ; `lecture_en_flux_lignes_gardees` ; `lecture_en_flux_reprise_apres_rupture` | `lecture_en_flux_un_octet_change_arret_et_rien_n_est_garde` (en-tête, données, fin) ; `lecture_en_flux_tronquee_arret` ; `tenseur_absent_de_l_index_arret` ; `montage_fichier_de_poids_altere_d_un_octet_arret` |
| petits fichiers et licences | `licence_saine_et_alteree_d_un_octet` ; `notice_versee_de_la_lentille_a_l_identifiant_git_du_texte` | `licence_saine_et_alteree_d_un_octet` ; `montage_tokeniseur_d_un_autre_sha256_arret` |
| lentille : disposition, `provenance`, point de capture, identité, doublons | `lentille_saine` ; `lentille_sans_couche_cible_admise_et_cles_absentes_rapportees` | `lentille_artefacts_arret` (14 cas) ; `montage_lentille_a_deux_matrices_egales_arret` |
| lentille absente, illisible, d'une autre taille ou empreinte | `lentille_telechargee_saine_puis_d_une_autre_empreinte_ou_absente` | la même (autre empreinte, absente, illisible) ; `calcul_lentille_absente_arret_sans_lecture_par_les_seuls_logits` (procédure) ; `lentille_publique_absente_jamais_de_lecture_par_les_seuls_logits` (lecture) |
| jetons gardés | `jetons_gardes_sains_et_liste_alteree_d_un_jeton` ; `empreinte_de_la_liste_gardee_meme_forme_que_la_tranche_des_lentilles` ; `jetons_gardes_par_les_scripts_du_voisin_sans_cle_et_une_seule_fois` | `jetons_gardes_sains_et_liste_alteree_d_un_jeton` (jeton changé, retiré, ajouté, doublon) ; `calcul_jetons_gardes_alteres_apres_le_montage_arret` (procédure) |
| code voisin : commit, correctifs | `voisin_commit_et_correctifs_sains` ; `correctifs_du_texte_presents_avec_leurs_empreintes` | `voisin_autre_commit_ou_correctif_altere_arret` |
| `readout.py` contre la copie versée | `readout_egal_a_la_copie_versee_sain` | `readout_copie_jouet_alteree_arret` (`read`, `rms_norm_columns`, `transport`) ; `readout_copie_versee_d_une_autre_empreinte_arret` ; `montage_readout_du_commit_altere_arret_avant_tout_flux` |
| montage entier | `montage_entier_sain_ordre_des_requetes_et_aucune_cle_ecrite` (essais d'un octet avant tout flux ; clé envoyée aux seuls fichiers de Llama ; aucun fichier de poids entier sur disque) | les essais `montage_*_arret` ci-dessus |

## Lecture (`lecture`)

| garde | essai sain | essai artefact |
|---|---|---|
| fonction de lecture (64 colonnes) | `garde_de_lecture_saine_et_ses_deux_artefacts_vus` (2 lentilles × 3 couches) ; `scores_egaux_a_la_formule_du_voisin` ; `garde_de_lecture_quasi_egalite_comptee_sans_arret` | `garde_de_lecture_ecart_sur_le_cas_sain_arret` ; `garde_de_lecture_artefact_invisible_arret` (matrice de la couche suivante et permutation remplacées par un artefact sans effet : arrêt) |
| indice de couche | `indice_de_couche_la_lecture_rend_la_signature_de_la_couche` (J_ℓ = I + ℓ·10⁻²·E, 3 couches) | `indice_de_couche_decalage_d_un_cran_arret` (3) ; `indice_de_couche_empreintes_du_montage_echangees_arret` ; `calcul_matrice_d_un_autre_indice_arret` (procédure) |
| rapport à ε | `rapport_a_epsilon_artefact_et_cas_sain` (moyenne quadratique 1) ; `rapport_a_epsilon_bords_99_et_101` (101) ; `independance_a_la_norme_facteur_commun` | `rapport_a_epsilon_artefact_et_cas_sain` (norme 10⁻⁴) ; `rapport_a_epsilon_bords_99_et_101` (99) ; `bout_en_bout_garde_du_rapport_a_epsilon_et_repli` (procédure : nuls refaits par direction) |
| imparité | `imparite` (2 lentilles) | — (propriété) |
| valeur non finie | `valeur_non_finie_dans_une_lecture_arret` (cas sain en fin d'essai) | `valeur_non_finie_dans_une_lecture_arret` ; `matrice_de_lentille_d_une_autre_forme_ou_precision_arret` |

## Nuls, statistiques, audits (`nuls_statistiques`)

| garde ou propriété | essai sain | essai artefact |
|---|---|---|
| graines | `graine_selon_le_plan_point_3` ; `cles_des_graines_formes_du_plan` ; `graines_reproductibles_et_distinctes_par_cle` | `cles_des_graines_formes_du_plan` (3 clés mal formées) |
| normes ; nul des signes | `nul_isotrope_moyenne_quadratique_un` ; `nul_par_direction_a_la_norme_de_v` ; `nul_des_signes_memes_valeurs_absolues_et_meme_norme` | `valeur_non_finie_dans_un_nul_arret` |
| calibration | `calibration_nul_isotrope_sain_…` (M = 2 000, 1 000 témoins : dans [23, 85]) ; `calibration_nul_des_signes_sain_mis_en_commun_et_artefact` (trois jeux de 200 : dans [12, 53]) ; `p_des_temoins_egal_a_la_definition` | les mêmes, scores des témoins × 1,5 : hors des bornes ; `calibration_hors_bornes_tables_non_calculables_sans_arret` (procédure) |
| bornes | `bornes_egales_aux_exemples_du_plan` ; `bornes_recalculees_par_le_programme_scelle_du_texte` ; `bornes_risque_sous_le_niveau_de_chaque_cote` | — |
| statistiques | `statistiques_egales_a_un_calcul_direct` ; `les_deux_signes_partagent_le_nul` ; `libelles_aux_bords_des_niveaux` (8) ; `famille_sur_representee_aux_bords` | `masques_et_comptes_de_familles` (nul résumé sur un autre nombre de jetons : arrêt) |
| familles | `familles_sur_un_vocabulaire_jouet` (24 chaînes) ; `masques_et_comptes_de_familles` | `familles_sur_un_vocabulaire_jouet` (chaînes hors famille) |
| jeton de début | `jeton_de_debut_rang_rapporte` | `jeton_de_debut_rang_rapporte` (jeton hors des gardés) |
| pôles | `poles_alignes_et_symetrie_v_et_moins_v` | `poles_valeurs_non_finies_ou_norme_nulle_arret` |
| comparaisons ; non calculable | `cosinus_jetons_communs_et_non_calculable` | `cosinus_jetons_communs_et_non_calculable` ; `calcul_direction_de_norme_nulle_non_calculable_sans_arret` (procédure) |
| déclencheurs d'audit | `declencheurs_sain_aucun_audit` | `declencheur_trop_beau_vingt_sondes_concentrees` ; `…_memes_vingt_jetons_aux_couches_7_ou_15` ; `…_cosinus` (7 cas aux bords) ; `declencheur_tout_negatif` ; `calcul_audit_joue_quand_un_declencheur_se_leve` (procédure) |
| relecture indépendante | `relecture_par_un_chemin_independant` | la même (autre lentille : désaccord vu) |

## Procédure et bout en bout (`procedure`)

| garde | essai sain | essai artefact |
|---|---|---|
| horloge de 8 h | `horloge_saine_puis_au_dela_de_8_h_arret` ; `horloge_cumulee_entre_le_montage_et_le_calcul` | les mêmes ; `calcul_horloge_au_dela_de_8_h_arret` |
| disque | `disque_seuils_simules` | `disque_seuils_simules` ; `montage_moins_de_6_go_au_depart_arret_sans_rien_creer` ; `calcul_moins_de_1_go_arret_sans_rien_supprimer` |
| clé : aucune occurrence dans les fichiers écrits | `aucune_occurrence_de_la_cle_sain_et_artefact` ; `bout_en_bout_fichiers_fermes_scelles_et_nettoyage` ; `montage_entier_sain_…` (montage) | `aucune_occurrence_de_la_cle_sain_et_artefact` (clé à cheval sur deux blocs) |
| `registres/scellements-v1.md` | `ligne_de_registre_saine_dans_le_registre_propre` | `cle_de_ce_texte_dans_scellements_v1_refus` |
| une phrase par libellé | `phrase_de_tete_toujours_ecrite` ; `phrase_concentree` ; `phrase_intermediaire_et_non_distincte_ne_nomment_aucun_jeton` ; `phrases_des_familles` ; `phrases_des_poles` ; `phrases_de_comparaison_et_de_non_lecture` | `regles_des_phrases_mots_interdits` ; libellé inconnu : arrêt (`phrase_intermediaire_…`) |
| morceaux de moins de 95 Mo ; nettoyage | `morceaux_numerotes_sous_la_limite_et_scelles` ; `bout_en_bout_fichiers_fermes_scelles_et_nettoyage` | `morceaux_…` (tableau trop grand, fichier existant) ; `nettoyage_refuse_un_dossier_sans_la_marque` |
| bout en bout (Llama miniature, fausse lentille) | `bout_en_bout_*` (7 essais : fichiers fermés et scellés, sondes lues et non lues, aucune régularisation dans les sorties, lecture égale à un calcul direct en double précision, indice de couche, repli de la garde du rapport à ε, comparaisons et phrases, graines et reproductibilité) | `calcul_*` (9 essais d'arrêt ou de refus) ; `ligne_de_commande_arret_code_3_sans_trace` |

## Lignes de la « Liste d'arrêt » sans essai codé

Tenues par les rôles (texte, R5) : texte non scellé ou `VERDICT-BBIS` présente au scellement ; toute dépense ; tables ouvertes par une
personne avant `VERDICT-BBIS` scellée ; transmission à un lecteur ; envie d'écart ; refus d'une permission. « Code non cité par
`CODE-LENTILLES-BBIS` » : le code exige la ligne, non l'égalité de ses empreintes à la fiche (notes, § 3, point 12).
