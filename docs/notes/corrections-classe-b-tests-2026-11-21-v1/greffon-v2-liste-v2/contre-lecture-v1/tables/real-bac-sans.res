ERROR tests/test_garde_calcul.py::test_artefact_arret_par_motif[kill $(pgrep -f train.py)]
ERROR tests/test_garde_calcul.py::test_artefact_arret_par_motif[kill `pgrep python`]
ERROR tests/test_garde_calcul.py::test_artefact_arret_par_motif[killall python3]
ERROR tests/test_garde_calcul.py::test_artefact_arret_par_motif[pgrep -f serve | xargs -r kill -9]
ERROR tests/test_garde_calcul.py::test_artefact_arret_par_motif[pgrep -f serve | xargs kill]
ERROR tests/test_garde_calcul.py::test_artefact_arret_par_motif[pkill -f vllm]
ERROR tests/test_garde_calcul.py::test_artefact_arret_par_motif[sleep 1; pkill python]
ERROR tests/test_garde_calcul.py::test_artefact_doublon_qui_n_est_pas_une_extension_admise[| GO-2026-10-05-01 | 2026-11-17 | calcul | extension au pilote p-v1 | 40 USD imput\xe9s \xe0 cette ligne | 2026-12-02 | Lazar | R-389 |\n]
ERROR tests/test_garde_calcul.py::test_artefact_doublon_qui_n_est_pas_une_extension_admise[| GO-2026-10-05-01 | 2026-11-21 | calcul | extension au pilote p-v1 | 40 USD imput\xe9s \xe0 cette ligne | 2026-12-02 | Claude | R-389 |\n]
ERROR tests/test_garde_calcul.py::test_artefact_doublon_qui_n_est_pas_une_extension_admise[| GO-2026-10-05-01 | 2026-11-21 | calcul | extension au pilote p-v1 | 40 USD imput\xe9s \xe0 cette ligne | 2026-12-22 | Lazar | R-389 |\n]
ERROR tests/test_garde_calcul.py::test_artefact_doublon_qui_n_est_pas_une_extension_admise[| GO-2026-10-05-01 | 2026-11-21 | calcul | phase 0 bis | 40 USD imput\xe9s \xe0 cette ligne | 2026-12-02 | Lazar | R-389 |\n]
ERROR tests/test_garde_calcul.py::test_artefact_doublon_qui_n_est_pas_une_extension_admise[| GO-2026-10-05-01 | 2026-11-21 | publication | extension au pilote p-v1 | 40 USD imput\xe9s \xe0 cette ligne | 2026-12-02 | Lazar | R-389 |\n]
ERROR tests/test_garde_calcul.py::test_artefact_echeance_illisible[| GO-2026-10-05-01 | 2026-11-21 | calcul | phase 0 | 150 USD | \u2014 | Lazar | message |\n]
ERROR tests/test_garde_calcul.py::test_artefact_echeance_illisible[| GO-2026-10-07-01 | 2026-11-19 | d\xe9p\xf4t distant | phase 0 | 150 USD | jamais | Lazar | message |\n| GO-2026-10-05-01 | 2026-11-21 | calcul | phase 0 | 150 USD | 2026-12-02 | Lazar | message |\n]
ERROR tests/test_garde_calcul.py::test_artefact_entree_illisible
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[-absent de registres]
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[| GO-2026-10-05-01 | 2026-10-23 | calcul | phase 0 | 150 USD | 2026-11-21 | Lazar | message |\n-hors de sa p\xe9riode]
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[| GO-2026-10-05-01 | 2026-11-22 | calcul | phase 0 | 150 USD | 2026-11-22 | Lazar | message |\n| GO-2026-10-05-01 | 2026-11-22 | calcul | phase 0 | 150 USD | 2026-11-22 | Lazar | message |\n-double]
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[| GO-2026-10-05-01 | 2026-11-22 | calcul | phase 0 | 150 USD | 2026-11-23 | Claude | message |\n-Lazar]
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[| GO-2026-10-05-01 | 2026-11-22 | calcul | phase 0 |\n-mal form\xe9]
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[| GO-2026-10-05-01 | 2026-11-22 | publication | phase 0 | 150 USD | 2026-11-23 | Lazar | message |\n-type]
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[| GO-2026-10-05-01 | 2026-11-23 | calcul | phase 0 | 150 USD | 2026-12-02 | Lazar | message |\n-hors de sa p\xe9riode]
ERROR tests/test_garde_calcul.py::test_artefact_go_invalide[| GO-2026-10-05-01 | hier | calcul | p | 1 | demain | Lazar | m |\n-dates]
ERROR tests/test_garde_calcul.py::test_artefact_lancement_sans_go
ERROR tests/test_garde_calcul.py::test_artefact_registre_absent
ERROR tests/test_garde_calcul.py::test_revocation_cas_sain_et_artefact
ERROR tests/test_garde_calcul.py::test_sain_commandes_ordinaires[echo pkillers]
ERROR tests/test_garde_calcul.py::test_sain_commandes_ordinaires[kill -TERM 4242]
ERROR tests/test_garde_calcul.py::test_sain_commandes_ordinaires[kill 12345]
ERROR tests/test_garde_calcul.py::test_sain_commandes_ordinaires[ls -la]
ERROR tests/test_garde_calcul.py::test_sain_commandes_ordinaires[python -m pytest]
ERROR tests/test_garde_calcul.py::test_sain_commandes_ordinaires[vastai destroy instance 987654]
ERROR tests/test_garde_calcul.py::test_sain_commandes_ordinaires[vastai show instances]
ERROR tests/test_garde_calcul.py::test_sain_go_sans_echeance_hors_calcul
ERROR tests/test_garde_calcul.py::test_sain_lancement_avec_go_valide
ERROR tests/test_garde_calcul.py::test_sain_ligne_d_extension_au_meme_identifiant
FAILED tests/test_cibles_invisibles_v1.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles
FAILED tests/test_cibles_invisibles_v1.py::test_aucune_invite_ne_porte_les_cibles[agent_p3]
FAILED tests/test_cibles_invisibles_v1.py::test_aucune_invite_ne_porte_les_cibles[agent_pilote_a]
FAILED tests/test_cibles_invisibles_v1.py::test_aucune_invite_ne_porte_les_cibles[juges_pilote]
FAILED tests/test_cibles_invisibles_v1.py::test_aucune_invite_ne_porte_les_cibles[juges_rejeu]
FAILED tests/test_cibles_invisibles_v1.py::test_aucune_invite_ne_porte_les_cibles[trace_lite]
FAILED tests/test_cibles_invisibles_v1.py::test_aucune_invite_ne_porte_les_cibles[trace_lite_conduite]
FAILED tests/test_cibles_invisibles_v1.py::test_garde_la_collecte_voit_une_fuite_plantee[agent_p3]
FAILED tests/test_cibles_invisibles_v1.py::test_garde_la_collecte_voit_une_fuite_plantee[agent_pilote_a]
FAILED tests/test_cibles_invisibles_v1.py::test_garde_la_collecte_voit_une_fuite_plantee[juges_pilote]
FAILED tests/test_cibles_invisibles_v1.py::test_garde_la_collecte_voit_une_fuite_plantee[juges_rejeu]
FAILED tests/test_cibles_invisibles_v1.py::test_garde_la_collecte_voit_une_fuite_plantee[trace_lite]
FAILED tests/test_cibles_invisibles_v1.py::test_garde_la_collecte_voit_une_fuite_plantee[trace_lite_conduite]
FAILED tests/test_cibles_invisibles_v1.py::test_inventaire_tout_constructeur_d_invite_est_examine
FAILED tests/test_cibles_invisibles_v2.py::test_aucun_module_hors_mesures_ne_lit_la_cle_cibles
FAILED tests/test_cibles_invisibles_v2.py::test_aucune_invite_ne_porte_les_cibles[agent_p3]
FAILED tests/test_cibles_invisibles_v2.py::test_aucune_invite_ne_porte_les_cibles[agent_pilote_a]
FAILED tests/test_cibles_invisibles_v2.py::test_aucune_invite_ne_porte_les_cibles[juges_pilote]
FAILED tests/test_cibles_invisibles_v2.py::test_aucune_invite_ne_porte_les_cibles[juges_rejeu]
FAILED tests/test_cibles_invisibles_v2.py::test_aucune_invite_ne_porte_les_cibles[trace_lite]
FAILED tests/test_cibles_invisibles_v2.py::test_aucune_invite_ne_porte_les_cibles[trace_lite_conduite]
FAILED tests/test_cibles_invisibles_v2.py::test_garde_la_collecte_voit_une_fuite_plantee[agent_p3]
FAILED tests/test_cibles_invisibles_v2.py::test_garde_la_collecte_voit_une_fuite_plantee[agent_pilote_a]
FAILED tests/test_cibles_invisibles_v2.py::test_garde_la_collecte_voit_une_fuite_plantee[juges_pilote]
FAILED tests/test_cibles_invisibles_v2.py::test_garde_la_collecte_voit_une_fuite_plantee[juges_rejeu]
FAILED tests/test_cibles_invisibles_v2.py::test_garde_la_collecte_voit_une_fuite_plantee[trace_lite]
FAILED tests/test_cibles_invisibles_v2.py::test_garde_la_collecte_voit_une_fuite_plantee[trace_lite_conduite]
FAILED tests/test_cibles_invisibles_v2.py::test_inventaire_tout_constructeur_d_invite_est_examine
FAILED tests/test_garde_calcul.py::test_registre_reel_du_depot_accepte_le_go_de_calcul_de_la_phase_0
PASSED tests/test_cibles_invisibles_v1.py::test_base_h12_absente_du_code_ou_couverte
PASSED tests/test_cibles_invisibles_v1.py::test_detecteur_insensible_a_la_casse_et_aux_espaces
PASSED tests/test_cibles_invisibles_v1.py::test_garde_de_l_inventaire_voit_un_constructeur_et_un_lecteur_plantes
PASSED tests/test_cibles_invisibles_v1.py::test_garde_temoin_positif_l_appariement_lit_les_cibles
PASSED tests/test_cibles_invisibles_v1.py::test_instruction_privee_p3_independante_de_la_tache
PASSED tests/test_cibles_invisibles_v1.py::test_inventaire_registre_a_jour
PASSED tests/test_cibles_invisibles_v1.py::test_la_tache_de_l_agent_n_a_aucun_champ_pour_les_cibles
PASSED tests/test_cibles_invisibles_v2.py::test_base_h12_absente_du_code_ou_couverte
PASSED tests/test_cibles_invisibles_v2.py::test_detecteur_insensible_a_la_casse_et_aux_espaces
PASSED tests/test_cibles_invisibles_v2.py::test_garde_de_l_inventaire_voit_un_constructeur_et_un_lecteur_plantes
PASSED tests/test_cibles_invisibles_v2.py::test_garde_temoin_positif_l_appariement_lit_les_cibles
PASSED tests/test_cibles_invisibles_v2.py::test_instruction_privee_p3_independante_de_la_tache
PASSED tests/test_cibles_invisibles_v2.py::test_inventaire_registre_a_jour
PASSED tests/test_cibles_invisibles_v2.py::test_la_tache_de_l_agent_n_a_aucun_champ_pour_les_cibles
PASSED tests/test_garde_google_v1.py::test_espece_inconnue_refusee
PASSED tests/test_garde_google_v1.py::test_limite_de_mots_bord
PASSED tests/test_garde_google_v1.py::test_limites_versees_par_mode
PASSED tests/test_garde_google_v1.py::test_niveau_attendu_explicite
PASSED tests/test_garde_google_v1.py::test_niveau_refuse
PASSED tests/test_garde_google_v1.py::test_provision_nulle_ou_negative_refusee
PASSED tests/test_garde_google_v1.py::test_repli_declare_au_budget
PASSED tests/test_garde_google_v1.py::test_sain_par_espece_et_par_mode[argon-high-32768-16384-flux]
PASSED tests/test_garde_google_v1.py::test_sain_par_espece_et_par_mode[argon-high-32768-16384-non_diffuse]
PASSED tests/test_garde_google_v1.py::test_sain_par_espece_et_par_mode[carbon-high-32768-16384-non_diffuse]
PASSED tests/test_garde_google_v1.py::test_sain_par_espece_et_par_mode[carbon-high-65536-49152-flux]
PASSED tests/test_garde_google_v1.py::test_sain_par_espece_et_par_mode[neon-xhigh-65536-32768-flux]
PASSED tests/test_garde_google_v1.py::test_sain_par_espece_et_par_mode[neon-xhigh-65536-32768-non_diffuse]
PASSED tests/test_garde_google_v1.py::test_sources_citees_dans_le_module
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[BLOCKLIST--0-None-BLOCKLIST]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[MAX_TOKENS--0-None-MAX_TOKENS]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[MAX_TOKENS-D\xe9but-100-None-MAX_TOKENS]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[None--0-PROHIBITED_CONTENT-PROHIBITED_CONTENT]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[None-R\xe9ponse.-100-None-FIN_None]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[OTHER-R\xe9ponse.-100-None-FIN_OTHER]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[PROHIBITED_CONTENT--0-None-PROHIBITED_CONTENT]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[RECITATION-Texte-100-None-RECITATION]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[SAFETY--0-None-SAFETY]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[SPII--0-None-SPII]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[STOP-   \n-100-None-VIDE]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[STOP--100-None-VIDE]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[STOP-R\xe9ponse.-0-None-SANS_PENSEES]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[STOP-R\xe9ponse.-100-None-None]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[STOP-R\xe9ponse.-None-None-SANS_PENSEES]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_motif_de_fin[STOP-R\xe9ponse.-True-None-SANS_PENSEES]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[budget avec le niveau-reglage4-thinkingBudget pr\xe9sent]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[niveau absent-reglage0-thinkingLevel absent]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[niveau en majuscules-reglage3-non admis]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[niveau non admis-reglage1-non admis]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[niveau plus bas que le plus haut-reglage2-au lieu de 'high']
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[pens\xe9es incluses fausses-reglage6-includeThoughts]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[pens\xe9es non incluses-reglage5-includeThoughts]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[plafond absent-reglage7-mal form\xe9s]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[plafond au-del\xe0 de la limite en flux-reglage9-au-del\xe0 de la limite]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[plafond flottant-reglage8-mal form\xe9s]
PASSED tests/test_garde_google_v1.py::test_un_essai_par_reglage_manquant[texte sous 16 000-reglage10-< 16000]
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_erreur_exception
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_erreur_ne_compte_pas_comme_accepte
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_mixte_accepte_et_refuse
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_refus_categorie_gemini
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_refus_reponse_vide
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_refus_stop_reason
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_refus_textuel
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_refus_textuel_francais
PASSED tests/test_garde_refus_question_v1.py::TestArtefact::test_tous_refusent_code_2
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_bilan_to_dict
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_classifier_reponse_accepte
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_extrait_court_non_tronque
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_extrait_long_tronque
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_modele_unique_accepte
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_plusieurs_modeles_acceptent
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_prompt_sonde_contient_extrait
PASSED tests/test_garde_refus_question_v1.py::TestCasSain::test_question_sha256_calculee
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_accepte_normal
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_espaces_seuls
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_gemini_prohibited
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_gemini_safety
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_refus_textuel_cannot
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_refus_textuel_unable
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_refusal_stop
PASSED tests/test_garde_refus_question_v1.py::TestClassifier::test_vide
PASSED tests/test_manifeste.py::test_artefact_config_alteree
PASSED tests/test_manifeste.py::test_artefact_decisif_sans_prereg
PASSED tests/test_manifeste.py::test_artefact_depot_sale
PASSED tests/test_manifeste.py::test_artefact_graine_alteree
PASSED tests/test_manifeste.py::test_artefact_identifiant_invalide
PASSED tests/test_manifeste.py::test_artefact_resultat_rattache_a_un_autre_manifeste
PASSED tests/test_manifeste.py::test_artefact_run_existant
PASSED tests/test_manifeste.py::test_artefact_taches_en_double
PASSED tests/test_manifeste.py::test_garde_numpy
PASSED tests/test_manifeste.py::test_graines_derivees_deterministes_et_distinctes
PASSED tests/test_manifeste.py::test_sain_chaine_complete
PASSED tests/test_prereg.py::test_artefact_contre_lecture_sans_empreintes
PASSED tests/test_prereg.py::test_artefact_gabarit_non_rempli
PASSED tests/test_prereg.py::test_artefact_marqueur_de_gabarit_restant
PASSED tests/test_prereg.py::test_artefact_prereg_hors_du_depot
PASSED tests/test_prereg.py::test_artefact_prereg_modifie_apres_scellement
PASSED tests/test_prereg.py::test_artefact_scelle_par_contournement_mais_non_conforme
PASSED tests/test_prereg.py::test_artefact_section_absente
PASSED tests/test_prereg.py::test_contre_lecture_par_entree
PASSED tests/test_prereg.py::test_run_decisif_rattache_au_prereg
PASSED tests/test_prereg.py::test_sain_prereg_conforme
PASSED tests/test_run_factice.py::test_artefact_resultat_altere
PASSED tests/test_run_factice.py::test_sain_chaine_et_rejeu
PASSED tests/test_scellement.py::test_arbre_sain_et_artefacts
PASSED tests/test_scellement.py::test_artefact_compagnon_absent
PASSED tests/test_scellement.py::test_artefact_compagnon_mauvais_nom
PASSED tests/test_scellement.py::test_artefact_ecrasement_interdit
PASSED tests/test_scellement.py::test_artefact_fichier_absent
PASSED tests/test_scellement.py::test_artefact_fichier_altere
PASSED tests/test_scellement.py::test_sain_sceller_puis_verifier
SKIPPED [1] tests/test_garde_google_v1.py:70: liste versée absente
