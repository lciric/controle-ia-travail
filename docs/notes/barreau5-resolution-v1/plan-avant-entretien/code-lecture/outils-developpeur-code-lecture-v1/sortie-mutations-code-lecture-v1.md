# Passage de mutations du code de lecture du barreau 5 — sortie v1

Outil : `mutations-code-lecture-v1.py` (même dossier) ; copie de travail unique sous le bloc-notes, temporaires sous
`/dev/shm`, effacés par leurs chemins. Une mutation est attrapée si pytest rend le code 1 (un essai échoue), les cinq témoins
sans mutation étant verts (lecture, sondes, relecture rapide, lanceur, relecture entière). Bilans bruts gardés dans le
bloc-notes de la session (`dev-code-lecture/mutations-bilan-passage-{1-nul,2,3}.json`), recopiés ici en substance.

## Passage 1 (00:55Z à 00:57Z) : nul
`--basetemp` sans dossier parent : chaque essai à dossier temporaire échouait d'entrée ; les quatre témoins échouaient (code
1), et les 57 mutations passaient pour attrapées. Non compté. Outil corrigé (dossier créé, témoins exigés verts, code 1 seul).

## Passage 2 (00:58Z à 01:16Z) : 57 jouées, 53 attrapées, 4 non attrapées
Témoins : lecture 80, sondes 16, relecture 17 (rapide) et 20 (entière), lanceur 14, tous verts.

| id | fichier | défaut réintroduit | état | premier essai en échec |
|---|---|---|---|---|
| L01 | lecture | zéro compté pour « séparé » | attrapée | `test_une_difference_nulle_compte_contre_la_conclusion_essayee` |
| L02 | lecture | zéro compté pour « contraire » | **non attrapée** (lacune) | — |
| L03 | lecture | égalités rangées dans l'ordre favorable | attrapée | `test_differences_nulles_et_egales_dans_l_ordre_le_plus_defavorable` |
| L04 | lecture | seuil strict, P(W ≤ w) < α | **non attrapée : équivalente** | — |
| L05 | lecture | 99 % dès sept familles | attrapée | `test_seuils_du_texte_a_99_et_95_pour_cent` |
| L06 | lecture | 95 % dès cinq familles | attrapée | `test_seuils_du_texte_a_99_et_95_pour_cent` |
| L07 | lecture | E2a : q inversé | attrapée | `test_monde_force_seule_issue_d_force_non_ecartee` |
| L08 | lecture | E2a : facteurs des membres échangés | attrapée | `test_monde_force_seule_issue_d_force_non_ecartee` |
| L09 | lecture | E2b : poussée non positive rend la famille absente | attrapée | `test_v10_familles_absentes_de_e2a_et_e2b_motifs_ecrits_et_noeud_6` |
| L10 | lecture | bornes du facteur [0,25 ; 4] | attrapée | `test_v10_…` |
| L11 | lecture | mise à l'échelle du maximum | attrapée | `test_mise_a_l_echelle_par_jeton_puis_maximum` |
| L12 | lecture | σ_0 non lu | attrapée | `test_recalcul_independant_des_statistiques_et_des_epreuves` |
| L13 | lecture | E3 de signe inversé | attrapée | `test_monde_sabotage_issue_s` |
| L14 | lecture | plis échangés | attrapée | `test_plan_des_instances_et_partition_egaux_a_ceux_de_la_formation` |
| L15 | lecture | Δ_app : borne basse à 2,5 % | attrapée | `test_recalcul_independant_…` |
| L16 | lecture | séparation établie sans la borne basse | attrapée | `test_separation_apprise_exige_la_borne_basse_positive` |
| L17 | lecture | manipulation établie sans M3 | attrapée | `test_manipulation_sans_m3_non_interpretable` |
| L18 | lecture | issue C jamais rendue | attrapée | `test_contraire_v4` |
| L19 | lecture | motif « saboteur non établi » omis | attrapée | `test_saboteur_non_etabli_v11` |
| L20 | lecture | seuil de l'issue E et du diagnostic à 1 | attrapée | `test_diagnostic_mots` |
| L21 | lecture | issue E si une seule famille sous le seuil | attrapée | `test_saboteur_seul_au_dessus_v2_non_etabli_avec_la_mention` |
| L22 | lecture | liste d'arrêt 13 à cinq familles | attrapée | `test_moins_de_six_familles_issue_n_niveau_non_atteignable` |
| L23 | lecture | niveau de S sans M1 ni M3 | attrapée | `test_niveau_de_l_issue_porte_celui_de_m1` |
| L24 | lecture | π inversé | attrapée | `test_diagnostic_mots` |
| L25 | lecture | table repérée par son empreinte : garde ôtée | **non attrapée : redondante** | — |
| L26 | lecture | table repérée par sa forme : garde ôtée | attrapée | `test_v7_table_sous_une_autre_forme_refus` |
| L27 | lecture | empreinte du programme non comparée | attrapée | `test_programme_d_une_autre_empreinte_refus` |
| L28 | lecture | engagement avant les sorties admis | attrapée | `test_engagement_posterieur_aux_scores_ou_avant_les_sorties_refus` |
| L29 | lecture | engagement avant la relance admis | attrapée | `test_engagement_avant_la_ligne_de_relance_refus` |
| L30 | lecture | copie lue non contrôlée | attrapée | `test_copie_lue_selon_la_ligne_de_relance` |
| L31 | lecture | produits écrits non recalculés | attrapée | `test_produits_ecrits_differents_refuses_a_l_ouverture` |
| L32 | lecture | score d'action ≠ maximum par jeton admis | attrapée | `test_score_d_action_different_du_maximum_par_jeton_refuse` |
| L33 | lecture | score manquant non vu | attrapée | `test_v7_score_manquant_refus` |
| L34 | lecture | fichier hors de l'inventaire admis | attrapée | `test_v7_fichier_hors_liste_blanche_ou_hors_inventaire_refus` |
| S01 | sondes | adaptateur tenu à l'écart admis dans un apprentissage | attrapée | `test_aucun_adaptateur_tenu_a_l_ecart_ni_ancrage_dans_un_apprentissage` |
| S02 | sondes | score d'action par la moyenne des jetons | attrapée | `test_notation_fermee_par_action_et_par_jeton_maximum_exact` |
| S03 | sondes | régularisation 0,1 | attrapée | `test_reglage_fixe_et_pli_d_apprentissage` |
| S04 | sondes | sonde du pli k apprise sur le pli k | attrapée | `test_apprendre_puis_noter_sur_des_activations_separables` |
| S05 | sondes | « echec » dans le seul pli en échec | attrapée | `test_sonde_en_echec_ecrite_echec_dans_ses_deux_plis` |
| S06 | sondes | contrôle carte-processeur à tolérance 1 | attrapée | `test_controle_carte_processeur_cas_sain_et_artefact` |
| S07 | sondes | pli noté : actions des deux plis | attrapée | `test_notation_fermee_par_action_et_par_jeton_maximum_exact` |
| R01 | relecture | chemin : cas sain non exigé | attrapée | `test_chemin_eprouve_cas_sain_et_deux_artefacts` |
| R02 | relecture | chemin : artefact non exigé | attrapée | `test_chemin_eprouve_cas_sain_et_deux_artefacts` |
| R03 | relecture | identité et artefact sautés | attrapée | `test_identite_a_dose_0_et_artefact_a_dose_1_de_chaque_adaptateur` |
| R04 | relecture | table dans l'arbre de la session : garde ôtée | attrapée | `test_arbre_de_la_session_sans_table_ni_formation` |
| R05 | relecture | marche de la formation dans l'arbre : garde ôtée | attrapée | idem |
| R06 | relecture | référence git de la formation : garde ôtée | attrapée | idem |
| R07 | relecture | engagement non comparé à la création | attrapée | `test_registre_de_relecture_cas_sain_et_artefacts` |
| R08 | relecture | accord de lecture non comparé | attrapée | idem |
| R09 | relecture | nombre à virgule admis au journal | attrapée | `test_journal_sans_nombre_a_virgule` |
| R10 | relecture | sorties hors liste blanche admises | attrapée | `test_sorties_hors_liste_blanche_refusees` |
| R11 | relecture | copie lue des épisodes propres non contrôlée | attrapée | `test_episodes_propres_copie_lue_et_pas` |
| R12 | relecture | première garde des entrées ôtée | **non attrapée : redondante** | — |
| R13 | relecture | δ̄ et normes sur la simple précision | attrapée | `test_deplacement_moyen_recalcule_depuis_les_activations_gardees` |
| R14 | relecture | divergence sans repasser à la dose 0 | attrapée | `test_jouet_de_bout_en_bout_relecture_sondes_puis_lecture` |
| R15 | relecture | ĝ tirée aussi des tenus à l'écart | attrapée | `test_produits_ecrits_egaux_au_recalcul_et_aucun_point_d_ancrage` |
| LA1 | lanceur | config sans accord admise | attrapée | `test_config_exige_l_accord_et_un_plan_connu` |

Raisons des quatre non attrapées :
- **L02, lacune** des essais (aucun essai ne mettait un zéro dans une épreuve « contraire ») : essai ajouté
  (`test_une_difference_nulle_compte_contre_contraire`).
- **L04, équivalente** : P(W ≤ w) = c / 2^K n'égale jamais 1/200 ni 1/40, puisque 5 ne divise aucune puissance de deux ;
  « ≤ » et « < » rendent le même seuil pour toute taille. Démontrée par `test_seuil_jamais_egal_a_l_erreur_exactement`
  (K de 0 à 39). Elle ne peut être attrapée par aucun essai ; elle n'est pas comptée comme manquée.
- **L25, redondante** dans le cours normal : la liste blanche n'admet dans l'arbre de lecture que du JSON, que la garde de
  forme lit déjà ; la garde de l'empreinte est éprouvée seule (`test_table_reperee_par_son_empreinte_hors_du_json`).
- **R12, redondante** : `engagement_v1.exiger_entrees_de_lecture_propres` refuse ensuite le même fichier ; la première garde
  est éprouvée seule, la seconde rendue muette (`test_premiere_garde_des_entrees_eprouvee_seule`).

## Passage 3 (01:19Z à 01:24Z), ciblé sur ces quatre, après les essais ajoutés
Témoins : lecture 83, sondes 16, relecture 18 (rapide) et 21 (entière), lanceur 14, tous verts. L02 attrapée, L25 attrapée,
R12 attrapée ; L04 non attrapée (équivalente, démontrée).

## Bilan
57 mutations jouées, 56 attrapées au passage 3 compris, une équivalente démontrée. Non jouées, parce qu'équivalentes sur les
sorties : l'ordre de relecture des adaptateurs non tiré (chaque série se calcule du même état ; seul l'ordre des marches
change), l'adaptateur de l'artefact du chemin pris dans tous les noms (« A1-… » précède « X-… » : même choix), le message seul
d'une date hors d'ordre (une seconde garde d'`engagement_v1` refuse aussi).
