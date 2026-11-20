# Table des essais — code de la première passe de la lecture des directions des sondes par la lentille publique, accordé à l'addendum de concentration scellé — v2

Complète `table-essais-v1.md` (ce dossier), qui reste la table des gardes du texte scellé
`prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`). Cette table
porte les gardes et les essais qu'exige l'addendum de concentration scellé
(`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`), § 3, EC-1 à EC-6, avec ses couples C1 à C5 et G1 à G5, H2 :
chaque garde codée a un essai sur un cas sain et un essai sur un artefact (R5). Code éprouvé : `entrees_v3`, `statistiques_v3`,
`lanceur_v4`. Les noms ci-dessous sont ceux des fonctions, sans le préfixe `test_`. Jouets seulement ; graines des essais neufs par
`numpy.random.SeedSequence`, clés `lentilles-bbis/essai/<garde>` (texte, plan, point 3).

Fichiers d'essais :
- neufs : `tests/test_lentilles_sondes_bbis_addendum_concentration_v2.py` (« addendum ») ;
  `tests/test_lentilles_sondes_bbis_garde_egalite_v1.py` (« égalité ») ;
- copies des essais de la version 3, visant le code neuf (jouets `tests/lentilles_sondes_bbis_jouets_v4.py`, dont le registre propre
  jouet porte la ligne de l'addendum et dont la fiche jouet du code porte son chemin et son empreinte) :
  `test_lentilles_sondes_bbis_entrees_v4.py`, `…_montage_v4.py`, `…_procedure_v4.py`, `…_nuls_statistiques_v3.py`,
  `…_gardes_non_vues_v3.py`, `…_corrections_contre_lecture_v3.py` ; les gardes de `table-essais-v1.md` et du traitement de la
  contre-lecture y gardent leurs essais, sous les mêmes noms de fonctions ;
- inchangé : `test_lentilles_sondes_bbis_lecture_v1.py` (il ne touche aucun module neuf).
Les fichiers d'essais des versions 1 à 3 restent en place, jamais réécrits (R12), et restent verts.

## EC-1, EC-2 et EC-5 — directions nulles jugées sans elles-mêmes (fichier « addendum »)

| garde ou règle | essai sain | essai artefact |
|---|---|---|
| concentration et part de chaque direction nulle sur les M − 1 autres (moyenne, écart type de population, quantile 0,99 par interpolation linéaire sur M − 1 valeurs) | `sain_concentration_et_part_de_chaque_direction_nulle_egales_a_un_calcul_direct` (4 tailles, dont M = 2 000 et M = 3) ; `sain_rang_fractionnaire_du_quantile_des_autres_a_la_taille_du_texte` (h = 1 978,02 pour une direction nulle, 1 979,01 pour v et les témoins) ; `relation_exacte_entre_le_z_sans_soi_et_le_z_avec_soi` (φ de EC-1) | `artefact_la_statistique_du_texte_d_origine_rend_des_concentrations_strictement_plus_petites` (moyenne, écart type et quantile des M directions inchangés) |
| artefact de taux à petite taille (M = 19, 128 jetons, 2 000 répliques, chaque réplique tirant ses 19 directions nulles et sa direction témoin ; part exigée entre 0,03 et 0,065) | `taux_a_petite_taille_sous_la_statistique_corrigee` | `artefact_de_taux_a_petite_taille_sous_la_statistique_du_texte_d_origine` (mêmes tirages : part au-dessus de 0,3, hors de l'intervalle) |
| arrêt : variance des M − 1 autres nulle, ou au plus 10⁻¹⁰ fois celle des M, pour un jeton | `arret_deux_directions_nulles_et_sain_trois_directions_de_scores_distincts` (seconde moitié : trois directions de scores distincts, pas d'arrêt) | `arret_variance_des_autres_nulle_pour_un_jeton` (jeton constant sur les autres ; puis variance des autres à 10⁻¹⁴ près) |
| arrêt : moins de trois directions nulles | la même (trois directions : pas d'arrêt) | `arret_deux_directions_nulles_et_sain_trois_directions_de_scores_distincts` (deux directions : arrêt) |
| C5 : C(u_j) rendu en simple précision ; comparaison C(u_j) ≥ C(v) en simple précision ; une égalité compte contre v | `concentrations_nulles_rendues_en_simple_precision` ; `p_de_concentration_de_la_direction_lue_et_des_temoins_selon_la_meme_regle` | `comparaison_des_concentrations_en_simple_precision_une_egalite_compte_contre_v` (la même comparaison en double précision ne compterait pas l'égalité ; concentrations nulles en double précision : arrêt) |

## EC-3 — bornes de calibration (fichier « addendum »)

| garde ou règle | essai sain | essai artefact |
|---|---|---|
| bornes égales aux exemples du plan | `bornes_egales_aux_exemples_du_plan` | `artefact_une_loi_decalee_d_un_cran_change_des_bornes` |
| bornes égales aux 41 bornes du § 7 | `les_41_bornes_du_paragraphe_7_de_l_addendum_egales_a_celles_du_code` | la même loi décalée d'un cran |
| bornes égales à celles du programme `bornes_calibration_statistique_corrigee_v2.py` | `bornes_recalculees_par_le_programme_de_l_addendum` (programme rejoué, empreinte `0f31484b…` vérifiée) ; `bornes_egales_a_la_sortie_scellee_du_programme_de_l_addendum` (sortie `39a410e4…`) | la même loi décalée d'un cran |
| loi dite « de référence, approchée, non exacte » dans ce que le code écrit | `les_tables_disent_la_loi_de_reference_approchee` ; `bout_en_bout_tables_de_la_garde_d_egalite` (égalité) | — (libellé) |
| calibration : nul sain dans les bornes, témoins × 1,5 hors des bornes | `calibration_nul_isotrope_sain_…`, `calibration_nul_des_signes_sain_…` (`nuls_statistiques_v3`, sous `statistiques_v3`) | les mêmes (seconde moitié) |

## EC-4 (couple C1) — clé `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` (fichier « addendum »)

| garde | essai sain | essai artefact |
|---|---|---|
| une seule ligne, inscrite avant `CODE-LENTILLES-BBIS` et avant `ENTREES-LENTILLES-BBIS`, de l'empreinte de l'addendum scellé | `cle_de_l_addendum_saine_acceptee` (registre jouet ; et ligne de la même seconde que `CODE-`, placée avant elle) | `cle_de_l_addendum_artefacts_refus` (8 cas : absente ; en deux lignes égales ; en deux lignes d'empreintes différentes ; placée après `CODE-` ; d'une heure postérieure à `CODE-` ; précédée de `ENTREES-` ; empreinte du brouillon ; autre chemin) |
| empreinte de la ligne égale à celle que porte la fiche du code | `cle_de_l_addendum_saine_acceptee` ; `fiche_du_code_qui_porte_l_addendum_saine` | `cle_de_l_addendum_d_une_autre_empreinte_que_celle_de_la_fiche_du_code_refus` ; `fiche_du_code_sans_l_addendum_ou_d_une_autre_empreinte_refus` (4 cas : champ absent ; sans empreinte ; empreinte du brouillon ; autre chemin) |
| le code porte l'empreinte de l'addendum scellé, jamais celle du brouillon | `le_code_porte_l_empreinte_de_l_addendum_scelle_jamais_celle_du_brouillon` (et empreinte du fichier de l'addendum présent sur la branche) | la même (l'empreinte du brouillon ne paraît dans aucun module neuf) |
| des registres, seules les clés nommées sortent | `seules_les_cles_nommees_sortent_du_registre` | la même (`registres/scellements-v1.md` : refus) |
| rien n'est ouvert ni demandé sans la clé (entrées) | `ouverture_et_recuperation_refusees_sans_la_cle_de_l_addendum` (première moitié : vingt sondes lues) | la même (ouverture et récupération refusées, aucun dossier créé) |
| montage : rien ne part sans la clé, avant toute requête | `bout_en_bout_l_addendum_cite_a_cote_du_texte` (égalité) ; montages des fichiers `montage_v4` et `procedure_v4` | `montage_rien_ne_part_sans_la_cle_de_l_addendum_avant_toute_requete` (4 cas : absente, double, après `CODE-`, autre empreinte ; aucune requête, aucun dossier) |
| calcul : rien ne part sans la clé | bout en bout (`procedure_v4`, égalité) | `calcul_refuse_sans_la_cle_de_l_addendum_sans_rien_ouvrir` |
| ligne de commande `recuperer` : fiche du code et clé exigées avant toute requête | `ligne_de_commande_arret_code_3_sans_trace` (`procedure_v4` : la fiche et la clé passent, l'arrêt vient de `VERDICT-BBIS`) | `ligne_de_commande_recuperer_refuse_sans_la_cle_de_l_addendum` |
| fiche du code : forme, empreinte de la ligne, empreinte de chacun des treize modules | `fiche_code_saine` (`corrections_contre_lecture_v3`) | `fiche_code_absente_ou_d_une_autre_empreinte_refus`, `fiche_code_module_d_une_autre_empreinte_ou_absent_refus`, `fiche_code_d_une_autre_forme_refus` (`corrections_contre_lecture_v3`) |
| le manifeste, les tables et le rapport du montage citent l'addendum à côté du texte | `bout_en_bout_l_addendum_cite_a_cote_du_texte` (égalité) | — (écriture ; l'essai des essais retire la citation et l'essai tombe) |

## EC-6, option 3 — garde d'égalité au vingtième rang (fichier « égalité »)

| étage ou règle | essai sain | essai artefact |
|---|---|---|
| la garde : vingtième et vingt-et-unième valeurs égales, par égalité exacte, en simple précision ; une égalité ailleurs ne compte pas | `sain_scores_tous_distincts_aucune_egalite` ; `sain_egalite_ailleurs_dans_le_classement_ne_compte_pas` (rangs 5 et 6 ; rangs 21 et 22) ; `egalite_exacte_en_simple_precision_et_non_a_une_tolerance_pres` | `artefact_egalite_aux_rangs_20_et_21_vue_et_arret_nomme` (message : cellule, pli, rôle, vecteur, signe, lentille, couche, liste, deux identifiants, valeur commune) |
| (i) direction lue, liste par score | `artefact_direction_lue_…` (seconde moitié : signe opposé, les deux jetons en queue de classement, pas d'égalité) ; `couche_saine_aucun_arret_comptes_d_egalites_ecrits` | `artefact_direction_lue_deux_jetons_de_meme_ligne_de_sortie_aux_rangs_20_et_21` (lentille jouet, deux lignes de sortie égales ; arrêt, message (i), les deux identifiants) ; dans le lanceur : `couche_artefact_direction_lue_arret_avec_la_cellule_…` ; `couche_artefact_signe_oppose_arret_au_signe_moins` |
| (i) direction lue, liste par z sous le nul isotrope | la liste par score du même jouet, sans égalité ; sous le nul des signes, aucune liste par z | `artefact_egalite_de_z_aux_rangs_20_et_21_de_la_liste_par_z` |
| (i) listes du témoin de couche | `couche_saine_…` | `couche_artefact_liste_du_temoin_de_couche_arret` (égalité à une autre couche, aucune à la couche de la sonde) |
| (i) les dix pôles par cosinus (dixième et onzième valeurs) | `sain_poles_sans_egalite_et_artefact_…` (première moitié ; et égalité aux cinquième et sixième cosinus : pas d'arrêt) | la même (deux colonnes égales de `W_down`) ; dans le lanceur : `couche_artefact_deux_colonnes_egales_de_w_down_arret` |
| (i) les dix premiers jetons de la lecture de chaque pôle | `artefact_dix_premiers_jetons_de_la_lecture_d_un_pole_…` (première moitié ; et égalité au vingtième rang : sans effet sur une liste de dix) | la même ; dans le lanceur : `couche_artefact_lecture_d_un_pole_arret` |
| (i) arrêt avant toute écriture de table ; versement de ce qui existe ; code 3 de la ligne de commande | bout en bout (tables écrites) | `calcul_arret_nomme_d_une_direction_lue_avant_toute_ecriture_de_table` (calcul entier sur le Llama miniature ; l'égalité est déclarée par la garde, le reste du chemin est celui du code) |
| (ii) direction nulle marquée ; S_min et S_max ; p_bas et p_haut ; valeur p écrite égale à p_haut ; attendu sans la direction marquée | `sain_direction_nulle_marquee_bornes_a_un_cran_libelle_egal_pas_d_arret` (famille : S_min < S(v) ≤ S_max, p_haut − p_bas = 1/(M + 1)) ; `sain_direction_nulle_marquee_bornes_a_un_cran_pour_la_part` (part : compte 19 ou 20 selon le départage) ; `sain_direction_nulle_marquee_hors_de_portee_p_bas_egal_a_p_haut` (S_max < S(v)) ; `sain_sans_direction_marquee_p_bas_egal_p_egal_p_haut` ; `egalite_ailleurs_dans_une_direction_nulle_ne_la_marque_pas` | `artefact_direction_nulle_marquee_decisive_pour_un_libelle_arret_nomme` (M = 99 ; p_bas = 0,01 sous les deux nuls, p_haut = 0,02 sous l'un ; message (ii)) |
| (ii) S_min et S_max égaux à une énumération de tous les départages | `s_min_et_s_max_egaux_a_l_enumeration_de_tous_les_departages` (6 cas : trois ou quatre jetons de même score au vingtième rang, une à trois places, part et famille ; un jeton entre le quantile des M − 1 autres et celui des M directions) | `bornes_de_departage_refusees_sans_egalite` ; `attendu_d_une_famille_sans_aucune_direction_non_marquee_arret` |
| (ii) libellé calculé aux deux bornes ; arrêt nommé s'ils diffèrent | `sain_le_meme_jouet_ou_la_direction_marquee_a_s_max_sous_s_de_v_pas_d_arret` ; `libelle_de_la_part_calcule_aux_deux_bornes` (première moitié) ; dans le lanceur : `etiquetage_sain_direction_marquee_hors_de_portee_libelle_ecrit_avec_p_haut` | `artefact_direction_nulle_marquee_decisive_…` ; `libelle_de_la_part_calcule_aux_deux_bornes` (seconde moitié) ; dans le lanceur : `etiquetage_artefact_direction_nulle_decisive_arret_avant_toute_table` |
| (iii) témoin : compté, écrit, sans arrêt ; compte de calibration inchangé | `temoin_a_egalite_au_vingtieme_rang_compte_ecrit_pas_d_arret_calibration_inchangee` (avant l'égalité : compte nul) | la même (un témoin à égalité : compte 1, valeurs p et compte de calibration inchangés) |
| liste de moins de vingt-et-un jetons : garde sans objet, écrit | `liste_de_moins_de_vingt_et_un_jetons_garde_sans_objet_ecrit` (21 jetons : garde avec objet) | la même (15 et 20 jetons : sans objet, écrit, aucun arrêt malgré deux valeurs égales) |
| H2 : paires de jetons gardés de même ligne de sortie, comptées au montage, sans arrêt | `paires_de_lignes_de_sortie_egales_octet_pour_octet` (aucune paire) ; `bout_en_bout_montage_compte_des_lignes_de_sortie_egales_sans_arret` | la même (une paire ; trois lignes égales : trois paires ; lignes égales en valeur et différentes d'un octet : non comptées) |
| comptes de la garde écrits dans les tables (directions nulles marquées, témoins à égalité, par couche, lentille et nul) | `couche_saine_aucun_arret_comptes_d_egalites_ecrits` (comptes nuls) ; `bout_en_bout_tables_de_la_garde_d_egalite` (repli par direction compris) | `couche_direction_nulle_marquee_et_temoin_a_egalite_comptes_ecrits_sans_arret` (calcul d'une couche du lanceur : une direction nulle marquée et un témoin à égalité, comptés, sans arrêt) |

## Remarque de la vérification de la version 2 du code, reprise

| garde | essai sain | essai artefact |
|---|---|---|
| rapport du montage exigé au départ du calcul ; le manifeste le cite toujours | `bout_en_bout_l_addendum_cite_a_cote_du_texte` (égalité : le manifeste cite le rapport, chemin et empreinte) | `calcul_rapport_du_montage_absent_rien_ne_part` (addendum) |

## Essai des essais

`outils/essai-des-essais-v3.py` : altérations du code neuf, une à une (garde retirée, borne confondue, précision changée, citation
retirée) ; chacune doit faire tomber au moins un essai. Sortie : `outils/sortie-essai-des-essais-v3.txt` (nombre d'altérations et
nombre de vues : dernière ligne).
