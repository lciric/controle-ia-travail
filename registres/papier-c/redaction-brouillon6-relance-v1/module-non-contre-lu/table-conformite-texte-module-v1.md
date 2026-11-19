# Papier C — table de conformité du texte r1 au module et à la configuration — v1

Écrit par l'agent du module (Claude Fable 5.2), le 2026-11-19. Texte : version r1
(`e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2`) ; « l. » = ses lignes. Module : fichiers sous
`arbre/docs/procedures/papier-C-v1/` ; essais sous `tests/`. Abréviations des fichiers : **err**
`papier_c_erreurs_v1.py` ; **ree** `papier_c_reechantillonnage_v1.py` ; **lois** `papier_c_lois_v1.py` ; **rg**
`papier_c_rangs_v1.py` ; **sd** `papier_c_sondes_v1.py` ; **dec** `papier_c_decisions_v1.py` ; **der** `derivation.py` ;
**cfg** `papier_c_configuration_v1.py` (schéma : `papier_c_schema_config_v1.py`) ; **gd** `papier_c_gardes_v1.py` ;
**lc** `papier_c_lancement_v1.py` ; **ana** `papier_c_analyse_v1.py`. Essais : **t-stat**
`test_papier_c_statistiques_v1.py` ; **t-dec** `…decisions…` ; **t-sd** `…sondes…` ; **t-gd** `…gardes…` ; **t-cfg**
`…configuration…` ; **t-der** `…derivation…` ; **t-lc** `…lancement…` ; **t-bout** `…bout_en_bout…` ; **t-sim**
`…simulations_du_texte…`. « PO-nn » renvoie à `points-ouverts-module-v1.md`.

État : **porté** (codé et éprouvé) ; **porté, lecture codée** (codé selon la lecture la plus littérale, point ouvert
posé) ; **non porté** (raison donnée). Les exigences non portées sont reprises en fin de table.

## 1. En-tête, verrous, champs du scellement

| l. | exigence | fichier, fonction | essai | état |
|---|---|---|---|---|
| 146-148, 199-203 | module sous `docs/procedures/papier-C-v1/`, rien sous `src/` ni `tests/`, importe `controle_ia` sans le modifier | tous les fichiers ; imports de `controle_ia.gardes`, `.manifeste`, `.prereg`, `.scellement` | toute la suite (cible nommée) | porté |
| 199-200 | une ligne « Module du papier C » par fichier | gd `lignes_du_module`, `garde_module`, `fichiers_du_module` | t-gd `test_garde_1_module_fichier_par_fichier` ; t-lc `test_arrets_avant_toute_carte` | porté (les lignes s'écrivent au scellement ; manifeste `sha256sums-module-v1.txt` fourni) |
| 204-208 | configuration : seuls cinq champs diffèrent au scellement ; aucun marqueur ne reste | cfg `differences_avec_le_brouillon`, `exiger_sans_marqueur` | t-cfg `test_differences_avec_le_brouillon_cinq_champs_seulement`, `test_marqueur_restant_…` | porté ; contradictions PO-11, PO-14 |
| 207-208 | les scripts qui écrivent la configuration appliquent les gardes lexicales et mesurent les longueurs avant d'écrire | `arbre/brouillons/ecrire_config_brouillon5_v1.py` (appelle cfg `exiger_gardes_lexicales`, `longueurs_mesurees`, `valider_configuration`) | journal du script ; t-cfg `test_le_brouillon_relu_est_valide_…` | porté |
| 149-158 | champs à porter : `stabilite_rang`, `constat_nu`, `agent_bras` (usurpation, trois niveaux), jetons spéciaux dans `gardes_lexicales`, règle des témoins, règle conjointe, lecture forcée, masque, agrégations, contrôlabilité, clés neuves | configuration brouillon 5 ; cfg `CONSTANTES_DU_TEXTE`, `SCHEMA` | t-cfg (14 essais) | porté |
| 181-188 | verrou 9 : harnais de la lecture forcée | — (lecture de code, message de fin) | — | constat : PO-09 |
| 209, 1215-1224 | entropie, clés de graines, une clé par tâche, manifeste | gd `graines_du_papier_c` (via `controle_ia.manifeste.graines`) ; lc `CLES_DU_PILOTE`, `CLES_DE_L_ETAPE2`, `lancer_le_pilote` | t-gd `test_garde_13_…` ; t-cfg `test_cles_de_graines_du_texte` ; t-lc `test_pilote_de_bout_en_bout_…`, `test_ouverture_de_l_etape2` | porté ; PO-28, PO-36 |
| 219-221 | le lanceur du pilote cherche le verdict complété de P3, vérifie son sceau, consigne chemin et empreinte | gd `garde_prealables_du_pilote` ; lc `preparer_le_pilote` | t-gd `test_garde_2_prealables_du_pilote` ; t-lc | porté |

## 2. Métrique

| l. | exigence | fichier, fonction | essai | état |
|---|---|---|---|---|
| 681-686 | verdict v, masse, lecture complète, même instrument | interface lc `Machine.lire` ; gardes 7 et 8 (gd `garde_contexte`, `garde_instrument`) | t-gd, t-lc | calcul de v : **non porté** (adaptateur réel, PO-43) ; gardes portées |
| 687-691 | jeton d'une valeur, en contexte ; garde testée (R5) | gd `jetons_des_valeurs_en_contexte` | t-gd `test_garde_5_jeton_en_contexte` ; t-lc (`espace_fusionne`) | porté |
| 692-699 | consignes, identiques octet pour octet, sans fuite | configuration `consignes` ; gd `garde_fuite_de_la_cible` ; lc `lire_les_conditions` | t-gd `test_garde_9_…` ; t-cfg `test_consignes_identiques_et_sans_fuite` ; t-lc (`consigne_modifiee`) | porté, sauf « dicte l'ampleur » (PO-06) |
| 700-703 | mode raisonné (384 jetons, glouton, arrêt à la tige) | configuration `raisonne` ; interface `Machine.lire(mode="raisonne")` | t-lc (lisibilité du mode raisonné) | génération : **non porté** (adaptateur, PO-43) |
| 704-709 | conditions, insertion en fin de contenu, constat nu | lc `insertion_d_une_condition` ; gd `garde_insertion` | t-lc `test_insertions_et_plan_des_episodes` ; t-gd `test_garde_10_insertion` | porté |
| 710-713 | déplacement, loi séparée | lois `loi_separee` | t-stat `test_loi_separee_egale_aux_moindres_carres` | porté |
| 714-720 | loi jointe brute, forme fermée ; grille et section dorée comme test ; « ĉ non identifiable » ; R²_joint | lois `loi_jointe`, `loi_jointe_par_grille`, `profil_residuel` | t-stat `test_loi_jointe_forme_fermee_egale_grille_et_section_doree`, `…simple_decalage…`, `…un_seul_rang…` | porté |
| 721-731 | loi nette du témoin : Δᵃ, X, ρ̂ borné, w̄, λ, r̂, σ̂, part des tirages où ρ̂ touche une borne, lecture sans calibrage | lois `calibrage`, `loi_nette`, `regresseur_calibre` ; ana `_lignes_tc1_du_juge` | t-stat `test_calibrage_definitions_du_texte`, `test_rho_borne_…`, `test_loi_nette_trois_lectures_et_lambda`, `test_loi_nette_recalculee_dans_chaque_tirage` | porté ; PO-04, PO-05 |
| 731-733 | loi avec terme d'intention, lois par intention, réserve | lois `loi_nette(saboteur=…)` ; dec `reserves_de_destination` ; ana | t-stat `test_terme_d_intention_…` ; t-dec `test_reserves_de_destination` | porté, lecture codée (PO-38) ; lois par intention : **non portées** dans l'analyse (la fonction les permet par des poids restreints) |
| 733-748 | tests du module sur données simulées (sans attaque ; λ = 1 ; règle conjointe ; artefacts ; rang aux trois lectures) | t-sim (5 essais) | t-sim | porté ; tailles et tirages : PO-37 |
| 749-751 | gain de famille Ḡ, rang le plus fort, corrélation de rang | lois `loi_jointe`, `loi_nette` (`G`), `correlation_de_rang` ; ana | t-stat ; t-bout | porté |
| 752-763 | références de ĉ : v*, v̄₀, attracteur, loi témoin, ĉ_m par rang, réserve « destination hétérogène » | lois `attracteur_propre`, `loi_temoin`, `loi_nette` (`c_par_rang`) ; dec `reserves_de_destination` | t-stat `test_gamma_loi_temoin_attracteur_forme` ; t-dec | porté ; ĉ_m de la loi séparée brute : fonction `loi_separee`, **non assemblé** dans l'analyse |
| 764-774 | rééchantillonnage par grappes, 10 000 tirages, mêmes tirages par corpus, BCa et jackknife, tirage dégénéré, repli par percentiles (R5) | ree `comptes_par_grappes`, `poids_jackknife`, `intervalle_bca`, `intervalle_percentiles` ; ana `Poids`, `Poids.par_grappe` ; gd `non_identifiable` | t-stat (7 essais sur les poids et les intervalles) ; t-bout `test_memes_tirages_…` ; t-sim `test_niveau_reel_des_queues_du_bca` | porté ; PO-07, PO-08, PO-37 |
| 775-781 | valeurs p par décompte, bilatéral, préséance décompte / BCa | ree `p_superieur`, `p_inferieur`, `p_bilateral`, `holm` ; ana | t-stat `test_valeurs_p_…`, `test_tirages_tous_au_dessus_…`, `test_holm_cas_construits` | porté |
| 782-808 | gain d'écart, D₀, brut, différence des différences, Ḡ_P, pente, e, e_c, e_x, prérequis D₀ | sd `gain_d_ecart`, `gain_sur_l_excedent`, `comparaison_aux_juges` ; dec `prerequis_d0` | t-sd `test_gain_d_ecart_formules_du_texte`, `test_gain_sur_l_excedent_et_comparaison_aux_juges` ; t-bout `test_prerequis_d0_…` | porté ; PO-41 |
| 809-815 | score de sonde, jamais la moyenne ni la médiane, scores par jeton et borne | sd `agreger`, `score_de_lecture`, `positions_de_lecture`, `exiger_production` | t-sd `test_agregations_…`, `test_lectures_…` | porté sur tableaux ; calcul en ligne : **non porté** (PO-43) ; borne : PO-15 |
| 816-829 | agrégations lues ; deux bras de diagnostic, quatre conditions de N-026 | sd `AGREGATIONS_*`, `ETIQUETTE_DIAGNOSTIC`, `est_de_diagnostic`, `exiger_production` ; dec (toutes les règles sur sonde appellent `exiger_production`) | t-sd `test_bras_de_diagnostic_etiquetes_et_refuses_en_production` ; t-dec `test_hc2_refuse_une_agregation_a_moyenne` ; t-bout `test_bras_de_diagnostic_refuse_par_l_analyse_decisive` | porté pour (1), (3), (4) et D₀ ; plancher recalculé (2) : **non porté** (PO-17) |
| 830-834 | lecture filtrée, masque | sd `positions_de_lecture("filtree")` ; ana (`lecture_filtree`) | t-sd ; t-bout | porté ; bornes du coût : PO-15 |
| 835-849 | témoin lexical : trois relectures, témoin de l'instrument, g_trahison,lex | sd `temoin_de_l_instrument`, `gain_sur_l_excedent` ; gd `garde_lecture_forcee` ; lc `relire_un_contenu` ; ana (`temoin_lexical`) | t-sd `test_temoin_de_l_instrument_…` ; t-gd `test_garde_20_…` ; t-lc `test_lecture_forcee_garde_20` | porté tel qu'écrit ; à redéfinir : PO-09 |
| 850-854 | trajectoire, version (a), mention | dec `M_ACTION` (HC2, C-P4c) ; configuration `etape2.trajectoire` | t-dec ; t-bout | mention portée ; maximum sur les actions de la trajectoire : **non porté** (assemblage) |
| 855-864 | alarme : seuil, détection, Clopper-Pearson à l'effectif efficace, cas p̂ = 0 ou 1, borne par rééchantillonnage | sd `seuil_d_alarme`, `taux_d_alarme` ; ree `effectif_efficace`, `clopper_pearson`, `beta_quantile` ; ana | t-sd `test_seuil_et_taux_d_alarme` ; t-stat (4 essais) ; t-bout `test_alarme_refutee_…` | porté ; PO-10 ; taux par rang et taux des familles 1 à 4 : **non assemblés** |
| 865-866 | modérateur raisonné (différence des lois) | — | — | **non porté** (assemblage ; les lois existent) |
| 867-872 | gardes lexicales ; marques d'ordre sur l'usurpation de l'agent | cfg `echecs_lexicaux`, `exiger_gardes_lexicales` ; sd `part_des_marques_d_ordre` ; dec `reserve_usurpation_marquee` | t-cfg `test_gardes_lexicales_cas_sain_et_artefacts` ; t-sd ; t-dec | porté ; PO-31 |
| 873-882 | grandeurs de dessin du pilote | der `gains_du_vivier`, `erreurs_types_du_vivier` ; lois `gamma_destination_imposee` | t-der | porté |
| 883-908 | bras « fuite textuelle et contrôlabilité » | (a) ana `rapportes.lecture_filtree` ; (b2) sd `seuil_de_controlabilite`, `detections_de_controlabilite`, `ramener_a_la_variance`, `direction_aleatoire` ; gd `garde_banc_de_controlabilite` | t-sd `test_controlabilite_…` ; t-gd `test_garde_22_…` | (a) porté pour C-P4 et HC2b ; C-P4c et C-P6 filtrés : partiel ; (b1) **non porté** (PO-19) ; PO-14, PO-20 |

## 3. Seuil et règles de décision

| l. | exigence | fichier, fonction | essai | état |
|---|---|---|---|---|
| 912-914 | lisibilité (pilote ; étape 2 : réserve à 1 %, arrêt à 5 %) | der `lisible` ; gd `garde_lisibilite_du_pilote`, `garde_anomalies_de_masse` | t-der ; t-gd `test_garde_6_…` | porté |
| 915-919 | banc sur processeur, six valeurs | gd `garde_banc_processeur` ; lc `banc_sur_processeur` | t-gd `test_garde_4_banc_sur_processeur` ; t-lc | porté ; format des fichiers : PO-35 |
| 920-924 | banc sur carte, réserves, jamais un filtre | dec `banc_sur_carte` ; gd `garde_banc_sur_carte` ; lc | t-dec ; t-gd ; t-lc `test_reserves_sans_arret_…` | porté ; PO-36, PO-46 |
| 925-928, 1389 | C-P2 : positive, négative, structure, table | dec `familles_d_un_juge`, `structure_d_un_juge`, `verdict_c_p2` | t-dec (3 essais, 8 cas de table) | porté, lecture codée (PO-21) |
| 929-937, 1387 | C-P1 : identifiable, règle conjointe, réserve, table | dec `lectures_c_p1_d_un_juge`, `verdict_c_p1` | t-dec (4 essais, 10 cas de table) ; t-sim | porté, lecture codée (PO-22) |
| 938-939, 1388 | C-P1b | dec `holm_des_paires`, `verdict_c_p1b` ; ana | t-dec `test_verdict_c_p1b` | porté, lecture codée (PO-24) |
| 550-602, 940-942, 1399-1410 | stabilité de rang : C-P3a, C-P3b, C-P3c ; trois lectures ; version (a) et repli (b) ; clause de repli ; mention de la grille | rg (tout le fichier) ; configuration `stabilite_rang.version` | t-stat (8 essais, dont 10 cas des deux versions et les trois valeurs exactes du texte) ; t-bout `test_stabilite_de_rang_les_deux_versions_…` ; t-sim | porté ; PO-11, PO-13 |
| 527-548, 943-953, 1392 | HC2 : confirmation par niveau, réfutation sur la moyenne des deux côtés, réfutation par niveau, mentions | dec `verdict_hc2`, `niveaux_gradues` ; ana `_ligne_sonde` | t-dec (6 essais sur HC2) ; t-bout | porté, lecture codée (PO-25, PO-26, PO-40) |
| 523-525, 1426-1434 | porte GC : ligne écrite, jamais le verdict | dec `ligne_porte_gc` | t-dec ; t-bout | porté (le verdict relève de R13) |
| 954-955, 1393 | C-P4c | dec `opposition_d_une_sonde`, `verdict_c_p4c` | t-dec (2 essais) | porté, lecture codée (PO-27) |
| 1394 | HC2b | dec `verdict_hc2b` | t-dec `test_verdict_hc2b` (5 cas) | porté |
| 946, 1395 | C-P4b | dec `verdict_c_p4b` | t-dec | porté |
| 959-962, 1396 | C-P5 | dec `lecture_c_p5_d_un_juge`, `verdict_c_p5` | t-dec ; t-stat (exemples 281/300 et 555/600) | porté |
| 963, 1397 | C-P6 | dec `lecture_sonde_c_p6`, `verdict_c_p6` | t-dec | porté |
| 964-966, 1391 | contrôle de manipulation, intensités graduées, réserve « gain faible » | dec `intensites_graduees`, `lectures_c_p1_d_un_juge`, `verdict_c_p5` | t-dec | porté |
| 956-958 | bras « contrôlabilité » : rien de plus, aucun seuil | dec `combinaisons_d_une_sonde` (mention seulement) | t-dec `test_combinaisons_mentions_fixees` | porté |
| 1412-1465 | combinaisons, mentions fixées | dec `combinaisons_d_une_sonde`, `reserves_de_destination`, constantes `M_*` et `R_*` | t-dec (3 essais : audit A9, mentions fixées, réserves de destination) ; t-bout | porté ; PO-23, PO-39 |

## 4. Plan d'analyse

| l. | exigence | fichier, fonction | essai | état |
|---|---|---|---|---|
| 980-996 | partage des tâches, tirage de l'étape 2, origine consignée | gd `tirer_le_partage`, `garde_partage` ; lc `ouvrir_l_etape2` | t-gd `test_garde_16_…` ; t-lc | porté ; PO-28 |
| 998-1010 | accord du jour, arrêt par identifiant, règle de calibrage | gd `garde_accord_du_jour`, `arreter_l_instance` ; lc `choisir_les_contenus_de_calibrage` | t-gd ; t-lc | porté ; PO-03 ; « première action à coût lisible » : côté machine, **non porté** |
| 1012-1049 | points 1.0 à 1.6 du pilote | lc `preparer_le_pilote`, `executer_le_pilote`, `lancer_le_pilote`, `ecrire_une_sortie` | t-lc (12 essais, 31 cas) | porté avec la fausse machine ; exécution réelle **non portée** (PO-43) |
| 1050-1096 | addendum de dérivation, entièrement mécanique ; refuse le banc | der (tout le fichier) | t-der (13 essais) | porté sur tableaux ; écriture de `prereg/papier-C-addendum-derivation-v1.md` et `.json` depuis les fichiers du pilote : **non portée** (la lecture des sorties scellées se borne à `exiger_entree_de_derivation`) ; PO-29, PO-30 |
| 1099-1107 | préalables de l'étape 2, génération du corpus A | gd `garde_prealables_de_l_etape2`, `garde_disjonction` ; lc `plan_des_episodes`, `generer_le_corpus_A`, `paragraphe_de_bras` | t-gd ; t-lc | porté (génération derrière l'interface) |
| 1115-1123 | niveaux du plaidoyer ; aucun score dans la génération | gd `garde_paragraphes_de_plaidoyer`, `garde_aucun_score_dans_la_generation` | t-gd `test_garde_21_…`, `test_garde_23_…` ; t-lc `test_generation_du_corpus_A_…` | porté ; PO-32, PO-34 |
| 1125-1131 | choix des sondes | gd `choisir_les_sondes` | t-gd `test_garde_15_…` | porté ; lecture du verdict de G0 : entrée |
| 1133-1147 | TC.1, constat nu | ana `_lois_du_juge`, `_lignes_tc1_du_juge` | t-bout | porté ; déplacement de la sonde lectrice sous chaque formulation : **non porté** |
| 1149-1175 | TC.2, lectures des sondes, excédent, contrôle du style | ana `_ligne_sonde` ; sd `excedent_du_paragraphe`, `controle_du_style`, `part_bornes_illisibles` | t-sd `test_excedent_…` ; t-bout | porté ; PO-16 ; règle « plus de 5 % de bornes illisibles » : fonction portée, non branchée dans l'analyse |
| 1177-1184 | TC.3 | ana (C-P5, C-P6) | t-bout | porté ; suspicion sous protocole, analyse de sensibilité sans les contenus marqués : **non portés** |
| 1205-1213 | modérateur raisonné, effectifs | lc `ouvrir_l_etape2` (20 tâches) | t-lc | tirage porté ; analyse **non portée** |
| 1226-1236 | comparaisons multiples | ree `holm`, `niveau_bonferroni` ; ana | t-stat ; t-bout (niveaux contrôlés) | porté |
| 1294-1331 | réserves 14, 16, 17 : étiquettes descriptives, indices recomptés | configuration `controle_redaction.indices_fente_QUALITE` (recomptés par le script) | t-cfg `test_longueurs_mesurees_…` | indices de {QUALITE} portés ; étiquettes de contingence et de personne : **non portées** (indices à verser, verrou 5) |

## 5. Audit de symétrie (l. 1343-1376)

| audit | fichier, fonction | essai | état |
|---|---|---|---|
| A1 longueur | dec `audit_a1` ; ana | t-dec `test_audits_seuils` | réserve portée ; corrélation longueur × gain : **non portée** (PO-45) |
| A2 loi témoin | dec `audit_a2` ; ana | t-dec | porté |
| A3 masses | dec `audit_a3` | t-dec | fonction portée, **non assemblée** (PO-45) |
| A4 présence | gd `garde_insertion` ; lc | t-gd ; t-lc | porté |
| placebo par permutation | lois `placebo_par_permutation` | t-stat | porté, lecture codée (PO-12) ; non assemblé dans l'analyse |
| A5 trop beau | dec `audit_a5` ; sd `separation_parfaite_des_alarmes` ; ana | t-dec ; t-bout | déclenchement porté ; l'audit lui-même est une liste de contrôles à mener |
| A6 trop vide | dec `audit_a6` ; ana | t-dec | de même |
| A7 forme de l'issue | lois `forme_de_l_issue` ; dec `audit_a7`, `part_des_verdicts_changes` ; ana | t-stat ; t-dec | porté ; part des verdicts changés : non assemblée (PO-45) |
| A8 longueur sous maximum | dec `audit_a8` ; ana | t-dec ; t-bout | porté pour la ligne HC2 ; C-P4b, C-P4c, C-P6 : **non portés** |
| A9 sonde et juges | dec `combinaisons_d_une_sonde` | t-dec `test_combinaisons_audit_a9_dans_les_deux_sens` ; t-bout `test_scenario_sans_attaque` | porté ; PO-44 |

## 6. Liste d'arrêt (l. 1467-1522) : chaque garde, cas sain et artefact

| n° | garde | erreur nommée (err) | fichier, fonction | essai |
|---|---|---|---|---|
| 1 | empreintes ; ligne du module ; arbre gelé ; marqueur | `EmpreinteNonConforme`, `ModuleNonConforme`, `ArbreGeleModifie`, `MarqueurRestant` | gd `garde_empreintes`, `garde_revisions_des_juges`, `garde_module`, `garde_arbre_gele` ; cfg `exiger_sans_marqueur` | t-gd (4, dont un dépôt jouet) ; t-cfg (2) ; t-lc — PO-01 |
| 2 | préalables ; accord du jour ; accord de dépense | `PrealableAbsent`, `AccordDuJourAbsent`, `AccordDeDepenseInvalide` | gd `garde_prealables_du_pilote`, `garde_prealables_de_l_etape2`, `garde_accord_du_jour`, `garde_accord_de_depense` | t-gd (6) ; t-lc — PO-02, PO-03 |
| 3 | budget ; arrêt de l'instance par son identifiant | `BudgetDepasse`, `ArretInstanceNonConsigne` | gd `borne_de_duree`, `garde_budget`, `arreter_l_instance` ; lc (bloc `finally`) | t-gd (2) ; t-lc `test_arrets_sur_l_instance_…`, `test_prix_de_l_instance_…` |
| 4 | bancs | `BancProcesseurNonReproduit`, `DefautDeChaineAuBanc` | gd `garde_banc_processeur`, `garde_banc_sur_carte` | t-gd (2) ; t-lc |
| 5 | jeton en contexte | `VarianteRefusee`, `AucuneVariantePourUnJuge` | gd `jetons_des_valeurs_en_contexte` ; der `choisir_variantes` | t-gd ; t-der ; t-lc |
| 6 | lisibilité | `LisibiliteNonTenue`, `AnomaliesDeMasse` | gd `garde_lisibilite_du_pilote`, `garde_anomalies_de_masse` | t-gd |
| 7 | troncature, contexte | `LectureTronquee` | gd `garde_contexte` | t-gd ; t-lc |
| 8 | instrument | `InstrumentVariable` | gd `garde_instrument` | t-gd ; t-lc |
| 9 | fuite de la cible | `FuiteDeLaCible` | gd `garde_fuite_de_la_cible` ; lc | t-gd ; t-cfg ; t-lc — PO-06 |
| 10 | insertion | `InsertionAbsente` | gd `garde_insertion` ; lc | t-gd ; t-lc |
| 11 | gardes lexicales | `GardeLexicaleEnEchec` | cfg `exiger_gardes_lexicales` | t-cfg (12 artefacts) — PO-31 |
| 12 | disjonction ; banc refusé par la dérivation | `RecouvrementCalibrageEtape2`, `FichierDuBancRefuse` | gd `garde_disjonction` ; der `exiger_entree_de_derivation` | t-gd ; t-der ; t-lc |
| 13 | entropie ; clé de graine | `EntropieNonConforme`, `CleDeGraineNonDeclaree` | gd `graines_du_papier_c` | t-gd ; t-lc |
| 14 | règle de l'addendum inapplicable | `RegleDeLAddendumInapplicable` | der (plusieurs lieux) | t-der |
| 15 | aucune sonde désignée | `AucuneSondeDesignee` | gd `choisir_les_sondes` | t-gd ; t-lc |
| 16 | tâches, partage, bassin | `TachesNonConformes`, `BassinTropPetit` | gd `tirer_le_partage`, `garde_partage`, `garde_bassin` ; der `effectif_a_l_ouverture` | t-gd ; t-der ; t-lc |
| 17 | plus de 1 % de tirages dégénérés (pas un arrêt) | — | gd `non_identifiable` ; ana (`non_identifiable_par_tirages`) | t-gd ; t-bout |
| 18 | texte privé dans un fichier public | `TexteDansLeDepotPublic` | gd `garde_depot_public` | t-gd — PO-33 |
| 19 | écart au préenregistrement | `EcartAuPreenregistrement` | gd `constater_un_ecart` ; lc (ordre des lectures, sortie écrasée, graines) | t-gd ; t-lc |
| 20 | lecture forcée | `LectureForceeInfidele` | gd `garde_lecture_forcee` ; sd `temoin_de_l_instrument` | t-gd ; t-sd ; t-lc |
| 21 | score dans la génération | `ScoreDansLaGeneration` | gd `garde_aucun_score_dans_la_generation` | t-gd ; t-lc — PO-34 |
| 22 | banc de contrôlabilité | `BancDeControlabiliteIndisponible` | gd `garde_banc_de_controlabilite` | t-gd |
| 23 | paragraphes de plaidoyer | `ParagraphesDePlaidoyerNonConformes` | gd `garde_paragraphes_de_plaidoyer` ; cfg ; lc | t-gd ; t-cfg ; t-lc |
| — | interdit « moyenne ou médiane sur les jetons en production » | `MoyenneEnProduction` | sd `exiger_production` | t-sd ; t-dec ; t-bout |

## 7. Exigences du texte non portées

1. **Adaptateur réel de l'interface `Machine`** (verdict par probabilité des jetons, mode raisonné, génération par
   l'agent, scores de sonde en ligne, lecture forcée, location et arrêt de l'instance) : `torch` absent de
   l'environnement, aucun essai possible (PO-43).
2. **Assemblage des tableaux de l'étape 2** depuis les sorties de la machine vers l'entrée de `analyser_etape2`
   (lecture des fichiers, alignement des contenus, des tâches et des cellules) : dépend de l'adaptateur.
3. **Écriture de l'addendum de dérivation** (`.md` et `.json`) depuis les fichiers scellés du pilote : les règles
   sont portées sur tableaux, la mise en fichiers ne l'est pas.
4. **Plancher aléatoire apparié en covariance** : forme absente du texte (PO-17).
5. **Banc de contrôlabilité repris tel quel (b1)** : banc non reçu (PO-19).
6. **Branche « dicte l'ampleur d'une mise à jour » de la garde 9** : aucun critère écrit (PO-06).
7. **Lignes rapportées non assemblées dans l'analyse** : modérateur raisonné ; lois par intention ; loi séparée brute
   par rang ; taux d'alarme par rang et des familles 1 à 4 ; suspicion sous protocole ; déplacement de la sonde
   lectrice sous chaque formulation ; maximum sur la trajectoire ; lignes par origine des tâches ; placebo par
   permutation, audit A3, corrélation de A1, part des verdicts changés de A7 ; audit A8 hors de la ligne HC2 ; lecture
   filtrée de C-P4c et de C-P6 ; analyse de sensibilité sans les contenus marqués ; étiquettes descriptives des réserves
   14 et 17 ; Ḡ et λ par tiers d'entropie (l. 671-673). Les fonctions de calcul existent pour la plupart ; aucune de
   ces lignes n'entre dans un verdict.
8. **Lecture du verdict de G0** (sondes désignées, écarts au plancher, d et ρ_t de la demi-largeur des sondes) : le
   verdict n'existe pas ; ces grandeurs sont des entrées.
