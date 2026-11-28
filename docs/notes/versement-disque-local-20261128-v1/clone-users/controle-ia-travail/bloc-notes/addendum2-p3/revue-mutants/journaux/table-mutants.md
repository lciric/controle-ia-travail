| id | famille | règle mutée | état | test qui tue, ou reproduction du survivant |
|---|---|---|---|---|
| A01 | A | contrôle hors_formes qui émet la réserve au_dela_de_la_consigne | tué | `test_table_des_cas_de_B1` |
| A02 | A | réserve du témoin nommée comme celle de la mention | tué | `test_reserves_de_B2_regle_et_cibles` |
| A03 | A | réserve « non lue » toujours nommée B1 | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| A04 | A | réserve écrite pour un contrôle contraire faux | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| A05 | A | phrase de lecture de P3-P1 donnée aux cibles P3-P4/<p> et T3/<p> | **SURVIT** | repro `test_A05` |
| A06 | A | phrase de ampleur_portee_par_les_formes remplie avec E0 au lieu de D | **SURVIT** | repro `test_A06_A07_A09` |
| A07 | A | phrase de au_dela_de_la_consigne remplie avec la borne haute | **SURVIT** | repro `test_A06_A07_A09` |
| A08 | A | réserves sans union par couple (nom, cible) : une par motif | **SURVIT** | repro `test_A08` |
| A09 | A | phrase de B3 remplie avec A_80_écrit_min au lieu de A_80_écrit_max | **SURVIT** | repro `test_A06_A07_A09` |
| B01 | B | réserve de B3 sur P3-P3/<p> au lieu de nul/<p> | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| B02 | B | réserve du témoin sur P3-P3/<p> au lieu de P3-P4/<p> | tué | `test_ligne_criteres_2_et_3_nul_non_etabli_B3_sans_objet` |
| B03 | B | réserve de la mention sur T4/<p> au lieu de T3/<p> | tué | `test_reserves_de_B2_regle_et_cibles` |
| B04 | B | B3 « non lu » sur P3-P1 au lieu de nul/<p> | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| C01 | C | hors_formes : b_sf < 0 au lieu de ≤ 0 | tué | `test_table_des_cas_de_B1` |
| C02 | C | portee_par_les_formes : b_D ≥ 0 au lieu de > 0 | tué | `test_garde_15_degenerescences_de_la_part` |
| C03 | C | au_dela_de_la_consigne : b_sf ≥ log10 3 au lieu de > | tué | `test_table_des_cas_de_B1` |
| C04 | C | non_resolue : 0 ≤ b_sf au lieu de 0 < b_sf | tué | `test_table_des_cas_de_B1` |
| C05 | C | non_resolue : b_D < 0 au lieu de ≤ 0 | tué | `test_table_des_cas_de_B1` |
| C06 | C | non_resolue : borne décisive ≥ log10 3 au lieu de > | tué | `test_table_des_cas_de_B1` |
| C07 | C | mediane_par_tache : b_M < 0 au lieu de ≤ 0 | tué | `test_table_des_cas_de_B1` |
| C08 | C | non_resolue : case inversée (b_D > 0 au lieu de ≤ 0) | tué | `test_table_des_cas_de_B1` |
| C09 | C | B2 : condition sur la borne décisive retirée | tué | `test_reserves_de_B2_regle_et_cibles` |
| C10 | C | B2 : b_sf ≥ 0 au lieu de > 0 | tué | `test_reserves_de_B2_regle_et_cibles` |
| C11 | C | au_dela_de_la_consigne lu contre 0 au lieu de log10 3 | tué | `test_table_des_cas_de_B1` |
| D01 | D | réserve de la mention sans la cible P3-P1 (seulement T3/<p>) | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| E01 | E | contrôle lu même si sa cible n'est pas établie | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| E02 | E | garde 14 : contrôle lu sur cible non établie accepté | tué | `test_garde_14_verrou` |
| E03 | E | garde 14 : réserve sur cible non établie acceptée | tué | `test_garde_14_verrou` |
| E04 | E | verrou point 6 : P3-P1/etablie non recoupé avec calculable et bas > 0 | tué | `test_garde_14_verrou` |
| E05 | E | nul/<p> établie sans la ligne « aucune sonde générique… » | **SURVIT** | repro `test_E05` |
| E06 | E | P3-P4/<p> établie sans la ligne « critères 2 et 3… » | **SURVIT** | repro `test_E06` |
| E07 | E | P3-P3/<p> établie même sur la ligne « lecture de P3-P3 en échec » | **SURVIT** | repro `test_E07` |
| E08 | E | garde 14 : conclusions établies non recoupées | tué | `test_garde_14_verrou` |
| E09 | E | garde 14 : clés interdites non cherchées | tué | `test_garde_14_verrou` |
| E10 | E | T<k>/<p> établi sans son drapeau etabli | **SURVIT** | repro `test_E10` |
| E11 | E | nul/<p> établie sans l'état « non au-dessus » (ligne seule) | **SURVIT** | équivalent (CC-mutants-08) |
| F01 | F | garde 13 : bas > Q pour une sonde dont nul/<p> est établie, non contrôlé | tué | `test_garde_13_entrees_de_B3` |
| F02 | F | garde 7 : tâches, exclues, illisibles et nuls non comparés | **SURVIT** | repro `test_F02` |
| F03 | F | garde 7 : nombre d'actions par condition non comparé | **SURVIT** | repro `test_F03` |
| F04 | F | garde 9 : sondes principales de [L] non recoupées avec [SF] | **SURVIT** | équivalent en pratique (CC-mutants-08) ; repro `test_F04` sur [L] forgée |
| F05 | F | lancement : gardes 7, 8 et 10 retirées d'avant le manifeste (refaites après) | **SURVIT** | repro `test_F05_F06[F05]` (dépôt jouet) |
| F06 | F | lancement : garde 13 retirée d'avant le manifeste (refaite après) | **SURVIT** | repro `test_F05_F06[F06]` (dépôt jouet) |
| F07 | F | lancement : arbre de travail sale autorisé | **SURVIT** | repro `test_F07` (dépôt jouet) |
| F08 | F | « échec » pour toute exception (pas seulement GardeArret) | **SURVIT** | repro `test_F08` |
| F09 | F | valeur non finie de la sortie remplacée par None (repli silencieux) | **SURVIT** | repro `test_F09_H03` |
| F10 | F | garde 12 : valeurs des graines non comparées | tué | `test_garde_12_graines` |
| F11 | F | garde 4 : S2 non contrôlé contre le commit de N-025 | tué | `test_garde_4_anteriorite_sur_un_depot_jouet` |
| F12 | F | garde 5 : second passage reconnu par la seule commande (pas par le texte) | tué | `test_garde_5_second_passage_et_manifeste_illisible` |
| F13 | F | garde 9 : type de taches_exclues non contrôlé | **SURVIT** | équivalent (CC-mutants-08) |
| F14 | F | garde 8 retirée de la fonction pure (et du lancement) | tué | `test_garde_8_issue_et_etats` |
| F15 | F | garde 2 : fichier des textes [T] non haché | tué | `test_ligne_de_commande_de_bout_en_bout` |
| F16 | F | garde 1 : empreinte des tests non comparée | tué | `test_garde_1_entropie_texte_scelle_empreintes_et_arbre_gele` |
| F17 | F | garde 11 : chemin du module non contrôlé | tué | `test_garde_11_forme_de_la_commande` |
| F18 | F | garde 3 : unicité de la lecture décisive affaiblie (« présente » au lieu de « seule ») | tué | `test_garde_3_lecture_decisive_rattachement_et_unicite` |
| F19 | F | garde 15 : ≥ 1 % au lieu de > 1 % | **SURVIT** | repro `test_F19` |
| F20 | F | garde 15 : seuil des dégénérés à 10 % au lieu de 1 % | tué | `test_garde_15_degenerescences_de_la_part` |
| F21 | F | garde 7 : effets ponctuels non comparés (comptes seuls) | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| F22 | F | garde « lecture décisive modifiée pendant l'addendum 2 » retirée | **SURVIT** | repro `test_F22` |
| F23 | F | garde 7 : [L] « non calculable » accepté même si le recalcul a deux tâches ou plus | **SURVIT** | repro `test_F23` |
| F24 | F | garde 3 : empreinte de [P] dans le manifeste de lecture non comparée | **SURVIT** | équivalent (CC-mutants-08) |
| G01 | G | intervalles propres (M5, M6, M8) à 90 % au lieu de 95 % (q non divisé par 2) | **SURVIT** | rejeu P3 (8 cas sur 8 échouent) |
| G02 | G | E_sf, E_-f, M7 à 90 % au lieu de 95 % | tué | `test_audit_explication_trop_propre_construit_et_sain` |
| G03 | G | matrice de tirage de M5, M6, M8 à TIRAGES / 2 lignes | **SURVIT** | rejeu P3 (8 cas sur 8 échouent) |
| G04 | G | garde 7 : tolérance des effets 1e-2 au lieu de 1e-12 | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| G05 | G | garde 7 : tolérance des aires 1e-2 au lieu de 1e-9 | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| G06 | G | repère de B1 arrondi à 0,48 au lieu de log10 3 | tué | `test_table_des_cas_de_B1` |
| G07 | G | z = Φ⁻¹(0,975) au lieu de Φ⁻¹(0,9875) | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G08 | G | B3 : A_80 ≥ A_80_écrit_max au lieu de > | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G09 | G | hypothèse écrite Q max 0,54 au lieu de 0,53 | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G10 | G | classement descriptif contre 0,48 au lieu de log10 3 | **SURVIT** | repro `test_G10` |
| G11 | G | audit (2) : saboteur conforme si 0 ≤ bas (au lieu de 0 < bas) | **SURVIT** | repro `test_G11_G12` |
| G12 | G | audit (2) : témoin et mention conformes si bas < 0 < haut (bornes exclues) | **SURVIT** | repro `test_G11_G12` |
| G13 | G | M5 : mention « instable » si e_bas < 0 < e_haut (bornes exclues) | **SURVIT** | repro `test_G13` |
| G14 | G | garde 7 : quantile du plancher 0,90 au lieu de 0,95 | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| G15 | G | B3 : facteur 1 + z / z80 au lieu de 1 + z80 / z | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| G16 | G | B3 : demi-largeur haut − bas (non divisée par 2) | tué | `test_B3_calcul_a_la_main_et_quantiles_normaux` |
| H01 | H | restriction : coût retiré remplacé par +inf au lieu de NaN | tué | `test_restriction_retire_exactement_les_actions_a_forme` |
| H02 | H | _nombre accepte ±inf (gardes 9 et 13) | **SURVIT** | repro `test_H02` |
| H03 | H | sortie : ±inf laissé passer (NaN seul refusé) | **SURVIT** | repro `test_F09_H03` |
| I01 | I | générateur fixe (graine 0) au lieu de manifeste.generateur(graines[clé]) | **SURVIT** | rejeu P3 (8 sur 8) |
| I02 | I | clés de B2 écrites avec l'analyse B1 | tué | `test_garde_9_cle_absente_et_entree_en_echec` |
| I03 | I | clés de E_sf et de la part échangées | tué | `test_ecart_de_forme_M8_calcul_a_la_main_et_forme_absente` |
| I04 | I | une seule clé pour les cinq E_-f | tué | `test_ecart_de_forme_M8_calcul_a_la_main_et_forme_absente` |
| I05 | I | écarts de forme consommés dans l'ordre inverse des conditions | tué | `test_ecart_de_forme_M8_calcul_a_la_main_et_forme_absente` |
| I06 | I | M5 : E0 tiré sur une autre matrice que D (lignes non partagées) | **SURVIT** | rejeu P3 (7 sur 8) |
| I07 | I | garde 12 : graines attendues d'une autre entropie | tué | `test_garde_7_coherence_cout_et_forme_alteres` |
| I08 | I | liste fermée : clés des écarts dans un autre ordre | tué | `test_cles_de_graines_liste_fermee_et_distinctes` |
| I09 | I | M8 : générateur consommé deux fois (un tirage jeté avant celui qui sert) | **SURVIT** | rejeu P3 (6 sur 8) |
| I10 | I | M6 : médianes des lignes tirées sur une matrice de graine fixe | **SURVIT** | rejeu P3 à 11 tirages (3 sur 8) |
| J01 | J | E_-f retire toutes les formes au lieu de la seule forme f | **SURVIT** | rejeu P3 (2 sur 8) |
| J02 | J | M7 : T_propres ne regarde que les formes de la condition a | **SURVIT** | rejeu P3 (2 sur 8) |
| J03 | J | M8 : f comparée aux actions sans f (et non sans aucune forme) | **SURVIT** | rejeu P3 (2 sur 8) |
| J04 | J | M6 : médiane sur T_sf au lieu des tâches de l'effet décisif | **SURVIT** | rejeu P3 (2 sur 8) |
| J05 | J | M3 : restriction appliquée à la seule condition a | tué | `test_restriction_retire_exactement_les_actions_a_forme` |
| J06 | J | garde 7 : aire sur toutes les actions (notées ou non) | **SURVIT** | rejeu P4 (arrêt « score non fini ») |
| J07 | J | M5 : D = moyenne de d_sf − d_∅ (signe inversé) | tué | `test_honnete_lit_100_fois_trop_bas_ses_actions_a_forme` |
| J08 | J | M5 : sur T_∅ au lieu de T_sf | tué | `test_garde_15_degenerescences_de_la_part` |
| J09 | J | M3 : illisibles d'origine sans les actions retirées | tué | `test_restriction_retire_exactement_les_actions_a_forme` |
| J10 | J | M9 : d_sf de la table par tâche égal à d_∅ | tué | `test_mediane_et_moyennes_sur_les_taches_seulement` |
| J12 | J | M4 : d(t) = s(b, t) − s(a, t) (signe inversé) | tué | `test_garde_15_degenerescences_de_la_part` |
| K01 | K | audit (2) « sans objet » seulement si tous les intervalles décisifs sont conformes | tué | `test_audit_part_hors_bornes_construit_et_sain` |
| K02 | K | déclencheur vrai seulement si (2) et (3) le sont | tué | `test_audit_explication_trop_propre_construit_et_sain` |
| K03 | K | audit (3) : bornes −1 et 1 exclues de l'intervalle admis | tué | `test_audit_part_hors_bornes_construit_et_sain` |
| K04 | K | audit (2) : cas « E_sf non calculable » retiré | **SURVIT** | repro `test_K04` |
| L01 | L | arrêt après le manifeste écrit mais non propagé | tué | `test_ligne_de_commande_de_bout_en_bout` |
| L02 | L | garde 11 déplacée après la création du manifeste | tué | `test_garde_11_forme_de_la_commande` |
| L03 | L | paramètres de tirage non contrôlés au point d'entrée | tué | `test_garde_11_parametres_au_point_d_entree` |
