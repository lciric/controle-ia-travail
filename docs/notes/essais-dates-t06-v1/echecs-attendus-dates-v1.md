# Échecs attendus des essais datés de l'expérience sur les traits du texte — note d'écart v1

Rédigée le 19 novembre 2026 par un développeur neuf, sur décision de routine de la session mère (R-3686) : ni copie versionnée des huit fichiers d'essais cités par empreinte, ni saut d'essai ; leurs échecs datés sont listés ici, et le programme `scripts/comparer_echecs_attendus_v1.py` vérifie qu'une relance n'en montre pas d'autre. Aucun fichier sous `src/` ni sous `scripts/` (hors ce programme neuf) n'est touché ; les huit fichiers ci-dessous ne sont pas modifiés.

## Ce qui échoue et pourquoi

Les huit fichiers d'essais des amorces et des lanceurs de l'expérience sur les traits du texte (T0.6) listés ci-dessous construisent un registre des accords factice dont l'accord de calcul GO-2026-11-02-28 a pour échéance le **16 novembre 2026**, une fin du GO écrite en dur à **1794873600** (17 novembre 2026, 00:00 UTC), et copient dans leur bac le calendrier de `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json` (dernier jour de création le 15 novembre, fin du GO le 17 novembre à 00:00 UTC). L'horloge réelle a dépassé ces dates. Le code refuse alors à bon droit, selon ses gardes voulues : l'amorce détruit l'instance factice (« démarrage après l'échéance : aucun calcul », code 2), le lanceur refuse un GO « hors de sa période de validité (2026-11-02 → 2026-11-16) », la création refuse une échéance « hors de ]maintenant, fin du GO] ». **Cause : date figée passée dans l'essai ; le code refuse à bon droit.** Ce n'est pas un défaut du code.

Preuve de la cause, pour les quelques essais dont l'extrait d'échec ne montre que le code de sortie 2 (destruction ou refus) au lieu de 0 ou 1 (par exemple `test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu`, `test_c_v4_1_rien_a_committer_n_est_pas_un_echec`, le cas « ramenée » de `test_amorce_variables_de_calendrier_et_de_depense`) : les mêmes essais, dans les copies libres `tests/test_t06_v10_amorce.py`, `tests/test_t06_v11_amorce.py` et `tests/test_t06_v4_scripts.py`, passent tous après la seule correction de l'horloge de l'essai (échéance calculée depuis maintenant ; commit 63ec9c1c9).

Les fichiers ne se modifient pas (R12) : chacun est cité par son empreinte actuelle dans un texte scellé. Les identifiants sont ceux de la relance du 19 novembre 2026 (vers 08:52 UTC, un fichier à la fois, `-rf`), identiques à ceux de la première mesure du même jour (vers 08:30 UTC).

| fichier | empreinte sha256 | texte scellé qui le cite par cette empreinte | échecs attendus | dernière ligne de la relance |
|---|---|---|---|---|
| `tests/test_t06_scripts.py` | `5ad1a4fe2468095688ceecb80939fba7839ffb62126a59d0fff2e7f8b5d27f2e` | `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v1.md` | 8 | 8 failed, 4 passed in 8.74s |
| `tests/test_t06_v2_scripts.py` | `a9cfd036fdf784e6e7107d477de53cf63b686978f293e77aad18ac92a46b0cba` | `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v2.md` | 12 | 12 failed, 5 passed in 8.35s |
| `tests/test_t06_v3_scripts.py` | `ae45170aef4d253039b1cc5224753103bf533a9d257ecbbc50999148e75cc456` | `docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v3.md` | 16 | 16 failed, 5 passed in 8.83s |
| `tests/test_t06_v5_amorce.py` | `e78b31c021bdefb8f0be019f07f8e1d8a7e2d3940e6bf6f1a0b94d2faa854bbd` | `prereg/T0.6-organismes-v0-v1.md` ; `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/sorties/verifier-candidat12-r2-v1.json` | 31 | 31 failed, 30 passed in 45.60s |
| `tests/test_t06_v6_amorce.py` | `e95240a2f244c535ab9db1b68f5c8dc40515c74876d0ed62250298ad4137b239` | `prereg/T0.6-organismes-v0-v1.md` ; `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/sorties/verifier-candidat12-r2-v1.json` | 32 | 32 failed, 43 passed in 68.38s (0:01:08) |
| `tests/test_t06_v7_amorce.py` | `eb125b2c044849c5849587041850ee10066910dddae6dead4bc637b8cb4b0f09` | `prereg/T0.6-organismes-v0-v1.md` ; `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/sorties/verifier-candidat12-r2-v1.json` | 32 | 32 failed, 43 passed in 70.83s (0:01:10) |
| `tests/test_t06_v7_amorce_minuterie.py` | `366f0cf78c79634868bcda6d8262d06b94fb56cb407d4642dca0f533d7a60642` | `prereg/T0.6-organismes-v0-v1.md` ; `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/sorties/verifier-candidat12-r2-v1.json` | 12 | 12 failed in 2.05s |
| `tests/test_t06_v12_amorce.py` | `c925281f13c5cb3cc6cc97a39cb7ecb3a76d25271c8fa0e884fe63654e1c74ae` | `docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/sorties/verifier-empreintes-rendus-v1.txt` | 32 | 32 failed, 48 passed in 78.93s (0:01:18) |
| **total** | | | **175** | |

## Trois échecs d'inventaire, à part

Cause propre, sans lien avec les dates : l'essai `test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais` exige que chaque fichier `tests/test_*.py` du dépôt figure dans une liste figée des essais à jouer sur l'instance, ou dans ses exclusions motivées. Des fichiers d'essais neufs ont été ajoutés au dépôt depuis (par exemple `tests/test_accb6_code_v1.py` ; plus de 160 fichiers, nombre qui croît avec chaque fichier d'essai neuf, celui de ce comparateur compris). Ces trois essais échouaient déjà avant la correction des dates. Les décider (liste neuve ou exclusions motivées) n'est pas l'objet de cette note. Les fichiers des v12 et v13 de la liste ont reçu l'horloge de l'essai, celui de la v11 la tient de son parent corrigé `tests/test_t06_v11_amorce.py` (commit 63ec9c1c9) ; leurs autres essais passent ; empreintes au moment de la note :

| fichier | empreinte sha256 | liste figée lue | échecs attendus | dernière ligne de la relance |
|---|---|---|---|---|
| `tests/test_t06_v11_liste.py` | `975adc6c5e2e6f430be671a75216e2def46c0409061d993e473be6db1dc9736e` | `scripts/tests-cibles-t06-v1.txt` | 1 | 1 failed, 13 passed in 11.76s |
| `tests/test_t06_v12_liste.py` | `efefa82c8947364872cad2d305070c9656b5e4f200e3ef31286f623a5491220d` | `scripts/tests-cibles-t06-v2.txt` | 1 | 1 failed, 13 passed in 12.69s |
| `tests/test_t06_v13_liste.py` | `7fb2e05fdb7d915916ec3d9acb76be5bc4e642e136e3c15d7cf296524c49d9b2` | `scripts/tests-cibles-t06-v3.txt` | 1 | 1 failed, 13 passed in 14.35s |

## Liste lue par le programme

178 identifiants, tels que pytest les écrit (échappements `\xe9`, `\u2260` compris). Usage : `python scripts/comparer_echecs_attendus_v1.py docs/notes/essais-dates-t06-v1/echecs-attendus-dates-v1.md SORTIE_PYTEST.txt [...]` ; code 0 si les échecs vus sont ceux-ci ou un sous-ensemble, 1 s'il y a un échec neuf, 2 si une entrée est illisible.

<!-- debut-liste-echecs-attendus -->
```text
# tests/test_t06_scripts.py — 8 — date figée passée ; le code refuse à bon droit
tests/test_t06_scripts.py::test_amorce_cas_sain_run_complet_et_donnees_poussees
tests/test_t06_scripts.py::test_amorce_arret_consigne_et_run_mort
tests/test_t06_scripts.py::test_amorce_redemarrage_et_refus_detruisent
tests/test_t06_scripts.py::test_amorce_lecture_precoce_artefacts[doublon-cit\xe9 plusieurs fois]
tests/test_t06_scripts.py::test_amorce_lecture_precoce_artefacts[sceau-faux-sceau non conforme]
tests/test_t06_scripts.py::test_amorce_lecture_precoce_artefacts[prereg-absent-absent au commit]
tests/test_t06_scripts.py::test_amorce_branche_presente
tests/test_t06_scripts.py::test_controles_et_commande_de_creation
# tests/test_t06_v2_scripts.py — 12 — date figée passée ; le code refuse à bon droit
tests/test_t06_v2_scripts.py::test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage
tests/test_t06_v2_scripts.py::test_amorce_fichier_trop_gros_refuse_avant_le_commit
tests/test_t06_v2_scripts.py::test_amorce_poussee_initiale_refusee
tests/test_t06_v2_scripts.py::test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage
tests/test_t06_v2_scripts.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup3-apr\xe8s l'heure de d\xe9pense \xe9puis\xe9e]
tests/test_t06_v2_scripts.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup4-fin du GO re\xe7ue (1794873500) \u2260 calendrier.fin_go_utc]
tests/test_t06_v2_scripts.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup5-ramen\xe9e]
tests/test_t06_v2_scripts.py::test_amorce_configuration_sans_calendrier_refusee
tests/test_t06_v2_scripts.py::test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu
tests/test_t06_v2_scripts.py::test_amorce_refus_go_et_branche_presente
tests/test_t06_v2_scripts.py::test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent
tests/test_t06_v2_scripts.py::test_controles_disque_simule_et_commande_de_creation
# tests/test_t06_v3_scripts.py — 16 — date figée passée ; le code refuse à bon droit
tests/test_t06_v3_scripts.py::test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage
tests/test_t06_v3_scripts.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[heure_passee]
tests/test_t06_v3_scripts.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[marqueur]
tests/test_t06_v3_scripts.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[echeance_passee]
tests/test_t06_v3_scripts.py::test_amorce_premier_demarrage_apres_depense_epuisee_detruit_sans_run
tests/test_t06_v3_scripts.py::test_amorce_fichier_trop_gros_refuse_avant_le_commit
tests/test_t06_v3_scripts.py::test_amorce_poussee_initiale_refusee
tests/test_t06_v3_scripts.py::test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage
tests/test_t06_v3_scripts.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup3-apr\xe8s l'heure de d\xe9pense \xe9puis\xe9e]
tests/test_t06_v3_scripts.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup4-fin du GO re\xe7ue (1794873500) \u2260 calendrier.fin_go_utc]
tests/test_t06_v3_scripts.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup5-ramen\xe9e]
tests/test_t06_v3_scripts.py::test_amorce_configuration_sans_calendrier_refusee
tests/test_t06_v3_scripts.py::test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu
tests/test_t06_v3_scripts.py::test_amorce_refus_go_et_branche_presente
tests/test_t06_v3_scripts.py::test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent
tests/test_t06_v3_scripts.py::test_controles_disque_simule_et_commande_de_creation
# tests/test_t06_v5_amorce.py — 31 — date figée passée ; le code refuse à bon droit
tests/test_t06_v5_amorce.py::test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage
tests/test_t06_v5_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[heure_passee]
tests/test_t06_v5_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[marqueur]
tests/test_t06_v5_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[echeance_passee]
tests/test_t06_v5_amorce.py::test_amorce_premier_demarrage_apres_depense_epuisee_detruit_sans_run
tests/test_t06_v5_amorce.py::test_amorce_fichier_trop_gros_refuse_avant_le_commit
tests/test_t06_v5_amorce.py::test_amorce_poussee_initiale_refusee
tests/test_t06_v5_amorce.py::test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage
tests/test_t06_v5_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup3-apr\xe8s l'heure de d\xe9pense \xe9puis\xe9e]
tests/test_t06_v5_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup4-fin du GO re\xe7ue (1794873500) \u2260 calendrier.fin_go_utc]
tests/test_t06_v5_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup5-ramen\xe9e]
tests/test_t06_v5_amorce.py::test_amorce_configuration_sans_calendrier_refusee
tests/test_t06_v5_amorce.py::test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu
tests/test_t06_v5_amorce.py::test_amorce_refus_go_et_branche_presente
tests/test_t06_v5_amorce.py::test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent
tests/test_t06_v5_amorce.py::test_c_v4_1_cas_sain_verrou_pris_pendant_les_commits_de_fin_de_run_et_status_propre
tests/test_t06_v5_amorce.py::test_c_v4_1_arret_consigne_sous_le_verrou
tests/test_t06_v5_amorce.py::test_c_v4_1_rien_a_committer_n_est_pas_un_echec
tests/test_t06_v5_amorce.py::test_c_v4_1_index_lock_pose_pendant_la_fin_de_run_fin_anormale_sans_fin_normale
tests/test_t06_v5_amorce.py::test_c_v4_1_commit_refuse_une_fois_puis_reussi_et_commit_toujours_refuse
tests/test_t06_v5_amorce.py::test_c_v4_1_status_non_vide_avant_la_fin_normale_rattrapage_ou_fin_anormale
tests/test_t06_v5_amorce.py::test_c_v4_1_verrou_non_obtenu_fin_anormale_journalisee
tests/test_t06_v5_amorce.py::test_c_v4_1_minuterie_a_l_echeance_pendant_la_poussee_finale_aucun_fichier_perdu_ordre_garde
tests/test_t06_v5_amorce.py::test_c_v4_1_verrou_relache_avant_l_arret_de_l_instance
tests/test_t06_v5_amorce.py::test_c_v4_1_fichier_non_rattrapable_fin_anormale
tests/test_t06_v5_amorce.py::test_c_v4_3_amorce_epreuve_artefacts[go_expire]
tests/test_t06_v5_amorce.py::test_c_v4_3_materiel_et_virgules_des_essais_joues
tests/test_t06_v5_amorce.py::test_c_v4_1_consignation_code_de_sortie_poussee_de_ce_qui_existe_mais_echec_de_chaine
tests/test_t06_v5_amorce.py::test_clonage_reduit_extraction_partielle_ligne_de_debit_et_chemins
tests/test_t06_v5_amorce.py::test_clonage_reduit_extraction_partielle_impossible_est_un_refus
tests/test_t06_v5_amorce.py::test_refus_annonce_puis_attend_avant_de_demander_la_destruction
# tests/test_t06_v6_amorce.py — 32 — date figée passée ; le code refuse à bon droit
tests/test_t06_v6_amorce.py::test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage
tests/test_t06_v6_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[heure_passee]
tests/test_t06_v6_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[marqueur]
tests/test_t06_v6_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[echeance_passee]
tests/test_t06_v6_amorce.py::test_amorce_premier_demarrage_apres_depense_epuisee_detruit_sans_run
tests/test_t06_v6_amorce.py::test_amorce_fichier_trop_gros_refuse_avant_le_commit
tests/test_t06_v6_amorce.py::test_amorce_poussee_initiale_refusee
tests/test_t06_v6_amorce.py::test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage
tests/test_t06_v6_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup3-apr\xe8s l'heure de d\xe9pense \xe9puis\xe9e]
tests/test_t06_v6_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup4-fin du GO re\xe7ue (1794873500) \u2260 calendrier.fin_go_utc]
tests/test_t06_v6_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup5-ramen\xe9e]
tests/test_t06_v6_amorce.py::test_amorce_configuration_sans_calendrier_refusee
tests/test_t06_v6_amorce.py::test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu
tests/test_t06_v6_amorce.py::test_amorce_refus_go_et_branche_presente
tests/test_t06_v6_amorce.py::test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent
tests/test_t06_v6_amorce.py::test_c_v4_1_cas_sain_verrou_pris_pendant_les_commits_de_fin_de_run_et_status_propre
tests/test_t06_v6_amorce.py::test_c_v4_1_arret_consigne_sous_le_verrou
tests/test_t06_v6_amorce.py::test_c_v4_1_rien_a_committer_n_est_pas_un_echec
tests/test_t06_v6_amorce.py::test_c_v4_1_index_lock_pose_pendant_la_fin_de_run_fin_anormale_sans_fin_normale
tests/test_t06_v6_amorce.py::test_c_v4_1_commit_refuse_une_fois_puis_reussi_et_commit_toujours_refuse
tests/test_t06_v6_amorce.py::test_c_v4_1_status_non_vide_avant_la_fin_normale_rattrapage_ou_fin_anormale
tests/test_t06_v6_amorce.py::test_c_v4_1_verrou_non_obtenu_fin_anormale_journalisee
tests/test_t06_v6_amorce.py::test_c_v4_1_minuterie_a_l_echeance_pendant_la_poussee_finale_aucun_fichier_perdu_ordre_garde
tests/test_t06_v6_amorce.py::test_c_v4_1_verrou_relache_avant_l_arret_de_l_instance
tests/test_t06_v6_amorce.py::test_c_v4_1_fichier_non_rattrapable_fin_anormale
tests/test_t06_v6_amorce.py::test_c_v4_3_amorce_epreuve_artefacts[go_expire]
tests/test_t06_v6_amorce.py::test_c_v4_3_materiel_et_virgules_des_essais_joues
tests/test_t06_v6_amorce.py::test_c_v4_1_consignation_code_de_sortie_poussee_de_ce_qui_existe_mais_echec_de_chaine
tests/test_t06_v6_amorce.py::test_clonage_reduit_extraction_partielle_ligne_de_debit_et_chemins
tests/test_t06_v6_amorce.py::test_clonage_reduit_extraction_partielle_impossible_est_un_refus_qui_cite_le_message_de_git[set-set]
tests/test_t06_v6_amorce.py::test_clonage_reduit_extraction_partielle_impossible_est_un_refus_qui_cite_le_message_de_git[init-init]
tests/test_t06_v6_amorce.py::test_refus_annonce_puis_attend_avant_de_demander_la_destruction
# tests/test_t06_v7_amorce.py — 32 — date figée passée ; le code refuse à bon droit
tests/test_t06_v7_amorce.py::test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage
tests/test_t06_v7_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[heure_passee]
tests/test_t06_v7_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[marqueur]
tests/test_t06_v7_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[echeance_passee]
tests/test_t06_v7_amorce.py::test_amorce_premier_demarrage_apres_depense_epuisee_detruit_sans_run
tests/test_t06_v7_amorce.py::test_amorce_fichier_trop_gros_refuse_avant_le_commit
tests/test_t06_v7_amorce.py::test_amorce_poussee_initiale_refusee
tests/test_t06_v7_amorce.py::test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage
tests/test_t06_v7_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup3-apr\xe8s l'heure de d\xe9pense \xe9puis\xe9e]
tests/test_t06_v7_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup4-fin du GO re\xe7ue (1794873500) \u2260 calendrier.fin_go_utc]
tests/test_t06_v7_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup5-ramen\xe9e]
tests/test_t06_v7_amorce.py::test_amorce_configuration_sans_calendrier_refusee
tests/test_t06_v7_amorce.py::test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu
tests/test_t06_v7_amorce.py::test_amorce_refus_go_et_branche_presente
tests/test_t06_v7_amorce.py::test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent
tests/test_t06_v7_amorce.py::test_c_v4_1_cas_sain_verrou_pris_pendant_les_commits_de_fin_de_run_et_status_propre
tests/test_t06_v7_amorce.py::test_c_v4_1_arret_consigne_sous_le_verrou
tests/test_t06_v7_amorce.py::test_c_v4_1_rien_a_committer_n_est_pas_un_echec
tests/test_t06_v7_amorce.py::test_c_v4_1_index_lock_pose_pendant_la_fin_de_run_fin_anormale_sans_fin_normale
tests/test_t06_v7_amorce.py::test_c_v4_1_commit_refuse_une_fois_puis_reussi_et_commit_toujours_refuse
tests/test_t06_v7_amorce.py::test_c_v4_1_status_non_vide_avant_la_fin_normale_rattrapage_ou_fin_anormale
tests/test_t06_v7_amorce.py::test_c_v4_1_verrou_non_obtenu_fin_anormale_journalisee
tests/test_t06_v7_amorce.py::test_c_v4_1_minuterie_a_l_echeance_pendant_la_poussee_finale_aucun_fichier_perdu_ordre_garde
tests/test_t06_v7_amorce.py::test_c_v4_1_verrou_relache_avant_l_arret_de_l_instance
tests/test_t06_v7_amorce.py::test_c_v4_1_fichier_non_rattrapable_fin_anormale
tests/test_t06_v7_amorce.py::test_c_v4_3_amorce_epreuve_artefacts[go_expire]
tests/test_t06_v7_amorce.py::test_c_v4_3_materiel_et_virgules_des_essais_joues
tests/test_t06_v7_amorce.py::test_c_v4_1_consignation_code_de_sortie_poussee_de_ce_qui_existe_mais_echec_de_chaine
tests/test_t06_v7_amorce.py::test_clonage_reduit_extraction_partielle_ligne_de_debit_et_chemins
tests/test_t06_v7_amorce.py::test_clonage_reduit_extraction_partielle_impossible_est_un_refus_qui_cite_le_message_de_git[set-set]
tests/test_t06_v7_amorce.py::test_clonage_reduit_extraction_partielle_impossible_est_un_refus_qui_cite_le_message_de_git[init-init]
tests/test_t06_v7_amorce.py::test_refus_annonce_puis_attend_avant_de_demander_la_destruction
# tests/test_t06_v7_amorce_minuterie.py — 12 — date figée passée ; le code refuse à bon droit
tests/test_t06_v7_amorce_minuterie.py::test_demarrage_apres_la_depense_epuisee_la_destruction_gagne_sur_l_arret[v6]
tests/test_t06_v7_amorce_minuterie.py::test_demarrage_apres_la_depense_epuisee_la_destruction_gagne_sur_l_arret[v7]
tests/test_t06_v7_amorce_minuterie.py::test_minuterie_ordre_de_destruction_pendant_la_consignation_supprime_le_put_stopped[v6]
tests/test_t06_v7_amorce_minuterie.py::test_minuterie_ordre_de_destruction_pendant_la_consignation_supprime_le_put_stopped[v7]
tests/test_t06_v7_amorce_minuterie.py::test_echeance_sans_resultat_depose_le_journal_sur_la_branche[v6]
tests/test_t06_v7_amorce_minuterie.py::test_echeance_sans_resultat_depose_le_journal_sur_la_branche[v7]
tests/test_t06_v7_amorce_minuterie.py::test_fin_de_run_normale_ne_cree_aucun_commit_de_journal_en_plus[v6]
tests/test_t06_v7_amorce_minuterie.py::test_fin_de_run_normale_ne_cree_aucun_commit_de_journal_en_plus[v7]
tests/test_t06_v7_amorce_minuterie.py::test_echeance_pendant_la_poussee_finale_v7_ajoute_un_seul_commit_de_journal_apres_les_autres[v6]
tests/test_t06_v7_amorce_minuterie.py::test_echeance_pendant_la_poussee_finale_v7_ajoute_un_seul_commit_de_journal_apres_les_autres[v7]
tests/test_t06_v7_amorce_minuterie.py::test_minuterie_a_l_echeance_depose_la_ligne_d_echeance_et_le_journal_sur_la_branche[v6]
tests/test_t06_v7_amorce_minuterie.py::test_minuterie_a_l_echeance_depose_la_ligne_d_echeance_et_le_journal_sur_la_branche[v7]
# tests/test_t06_v12_amorce.py — 32 — date figée passée ; le code refuse à bon droit
tests/test_t06_v12_amorce.py::test_amorce_cas_sain_deux_commits_morceaux_et_second_demarrage
tests/test_t06_v12_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[heure_passee]
tests/test_t06_v12_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[marqueur]
tests/test_t06_v12_amorce.py::test_amorce_second_demarrage_apres_depense_epuisee_consigne_puis_detruit[echeance_passee]
tests/test_t06_v12_amorce.py::test_amorce_premier_demarrage_apres_depense_epuisee_detruit_sans_run
tests/test_t06_v12_amorce.py::test_amorce_fichier_trop_gros_refuse_avant_le_commit
tests/test_t06_v12_amorce.py::test_amorce_poussee_initiale_refusee
tests/test_t06_v12_amorce.py::test_amorce_poussee_finale_refusee_trois_fois_puis_second_demarrage
tests/test_t06_v12_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup3-apr\xe8s l'heure de d\xe9pense \xe9puis\xe9e]
tests/test_t06_v12_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup4-fin du GO re\xe7ue (1794873500) \u2260 calendrier.fin_go_utc]
tests/test_t06_v12_amorce.py::test_amorce_variables_de_calendrier_et_de_depense[env_sup5-ramen\xe9e]
tests/test_t06_v12_amorce.py::test_amorce_configuration_sans_calendrier_refusee
tests/test_t06_v12_amorce.py::test_amorce_arret_consigne_run_mort_et_redemarrage_interrompu
tests/test_t06_v12_amorce.py::test_amorce_refus_go_et_branche_presente
tests/test_t06_v12_amorce.py::test_minuterie_depense_epuisee_puis_echeance_consignent_et_poussent
tests/test_t06_v12_amorce.py::test_c_v4_1_cas_sain_verrou_pris_pendant_les_commits_de_fin_de_run_et_status_propre
tests/test_t06_v12_amorce.py::test_c_v4_1_arret_consigne_sous_le_verrou
tests/test_t06_v12_amorce.py::test_c_v4_1_rien_a_committer_n_est_pas_un_echec
tests/test_t06_v12_amorce.py::test_c_v4_1_index_lock_pose_pendant_la_fin_de_run_fin_anormale_sans_fin_normale
tests/test_t06_v12_amorce.py::test_c_v4_1_commit_refuse_une_fois_puis_reussi_et_commit_toujours_refuse
tests/test_t06_v12_amorce.py::test_c_v4_1_status_non_vide_avant_la_fin_normale_rattrapage_ou_fin_anormale
tests/test_t06_v12_amorce.py::test_c_v4_1_verrou_non_obtenu_fin_anormale_journalisee
tests/test_t06_v12_amorce.py::test_c_v4_1_minuterie_a_l_echeance_pendant_la_poussee_finale_aucun_fichier_perdu_ordre_garde
tests/test_t06_v12_amorce.py::test_c_v4_1_verrou_relache_avant_l_arret_de_l_instance
tests/test_t06_v12_amorce.py::test_c_v4_1_fichier_non_rattrapable_fin_anormale
tests/test_t06_v12_amorce.py::test_c_v4_3_amorce_epreuve_artefacts[go_expire]
tests/test_t06_v12_amorce.py::test_c_v4_3_materiel_et_virgules_des_essais_joues
tests/test_t06_v12_amorce.py::test_c_v4_1_consignation_code_de_sortie_poussee_de_ce_qui_existe_mais_echec_de_chaine
tests/test_t06_v12_amorce.py::test_clonage_reduit_extraction_partielle_ligne_de_debit_et_chemins
tests/test_t06_v12_amorce.py::test_clonage_reduit_extraction_partielle_impossible_est_un_refus_qui_cite_le_message_de_git[set-set]
tests/test_t06_v12_amorce.py::test_clonage_reduit_extraction_partielle_impossible_est_un_refus_qui_cite_le_message_de_git[init-init]
tests/test_t06_v12_amorce.py::test_refus_annonce_puis_attend_avant_de_demander_la_destruction
# tests/test_t06_v11_liste.py — 1 — inventaire : fichiers d'essais neufs hors de la liste figée et des exclusions
tests/test_t06_v11_liste.py::test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais
# tests/test_t06_v12_liste.py — 1 — inventaire : fichiers d'essais neufs hors de la liste figée et des exclusions
tests/test_t06_v12_liste.py::test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais
# tests/test_t06_v13_liste.py — 1 — inventaire : fichiers d'essais neufs hors de la liste figée et des exclusions
tests/test_t06_v13_liste.py::test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais
```
<!-- fin-liste-echecs-attendus -->
