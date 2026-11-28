# Notes des corrections du code — plan B des juges (T0.5), v1

- Date : 2026-10-20 (UTC). Agent des corrections (étape T0.5 du programme), en routine sur processeur.
- Clone : `plan-b-code/depot`, branche locale `travail/plan-b-v1`, tête `cb14316`. Aucun commit, aucune poussée, aucun
  service payant, aucune commande Vast.ai, aucun modèle réel.
- Décisions appliquées : R-249, D-1 à D-14 (D-15 : aucun changement de code, par décision).
- Lus en entier avant tout changement : les trois rapports R2 (`relecture-R2-1/…-1.md`, `relecture-R2-2/…-2.md`,
  `relecture-R2-3/…-3.md`), les quatre sondes de `relecture-R2-3/sondes/` et leurs sorties, les notes d'intégration,
  le brouillon 3 (`8747ea81…`), les quatre modules neufs et les cinq fichiers de tests.
- Copies d'avant les corrections (empreintes égales à celles des notes d'intégration) : `corrections-v1/originaux/`.

## Verdict

D-1 à D-14 sont appliquées dans trois modules neufs (`rubrique_simplifiee.py`, `requalifier_juges.py`,
`lire_requalification.py`) et quatre fichiers de tests. `juges_simplifies.py` et `test_plan_b_juges_simplifies.py`
n'ont pas changé. Aucun module gelé n'a changé ; aucun test n'a été retiré ni affaibli. Les tests du plan B passent :
389 passed in 181.64s (0:03:01) (281 avant). Les sondes de la relecture 3 sont versées. Les 43 mutants
écrits contre les corrections sont tous tués (section 3).

Deux points sont appliqués avec un écart de forme, nommé (section 1) : D-6 (cas sain sur le brouillon 3 hors de pytest)
et D-10 (décalage du palier de production consigné, non exigé).

## 1. Décisions : fonction touchée et test qui le prouve

Abréviations : `rs` = `rubrique_simplifiee.py`, `rq` = `requalifier_juges.py`, `lr` = `lire_requalification.py` ;
`T-rs`, `T-rq`, `T-lr`, `T-in` = `tests/test_plan_b_rubrique_simplifiee.py`, `…_requalifier.py`, `…_lecteur.py`,
`…_integration.py`.

| décision | fonctions touchées | tests qui le prouvent |
|---|---|---|
| D-1 (I-1, R2-01) | `lr.classer_depassement` (NaN de G_S, d'un maximum de zone ou de R_S → « illisible ») ; `lr._illisible` (neuf) ; `lr.bilan_chemin` (motif « grandeur illisible (NaN) » → « non concluant (contrôles) ») ; `rq.lire_palier_chemin` (même liste de motifs, même ordre ; « motifs » au lieu de « motif ») ; docstrings de `rq` (module, `classer_depassement`) et de `lr` (module). Le déclencheur d'audit NaN de `lr.audit_r4` est inchangé. | T-lr `test_classer_depassement_valeurs_illisibles` (attendu changé par décision : « illisible ») ; `test_grandeur_illisible_au_palier_du_chemin_cas_sain_et_artefacts[g_s, max_zone, r_s_depassement]` (cas sain « fidèle » et « défaut (décodage) » lisible ; artefact : « non concluant (contrôles) », lecture combinée « non concluant », PB8 « non concluant », table A « RS1 retenue », audit NaN gardé) ; `test_r_s_illisible_sans_depassement_reste_une_reserve` ; `test_grandeur_illisible_ne_suspend_pas_la_requalification` (lecture de bout en bout). T-in `test_second_calcul_du_lanceur_egal_a_la_lecture_sur_les_fonctions_pures` (grille avec NaN : égalité, l'assertion d'écart connu devient une égalité) ; `test_le_lecteur_lit_le_run_jouet_du_lanceur` (motifs du chemin égaux). T-rq `test_lecture_du_chemin_sans_depassement_et_recouvrements` (inchangé, passe). |
| D-2 (I-2, R2-08) | `rq` : docstring du module (section « Second calcul, sans effet sur le run ni sur la lecture », divergences restantes nommées : ρ pour R(ℓ) = 0 ; repère absent d'un fichier simple présent ; motifs du palier de production ; gardes de forme que le second calcul ne refait pas) ; en-tête de section « bilans : second calcul, sans effet sur le run ni sur la lecture » ; docstrings de `rapports_au_repere` et `lire_palier_production`. | Aucun comportement changé : docstrings. L'égalité des deux calculs reste tenue par T-in `test_le_lecteur_lit_le_run_jouet_du_lanceur` et `test_second_calcul_…`. |
| D-3 (R2-06) | `lr.table_a` : ligne neuve « sonde d'audit fausse : requalification non concluante (instrument) : nœud » (`sondes_justes` a un effet). | T-lr `test_table_a_ligne_par_ligne_et_recouvrements[…sonde-fausse…]` (nœud ; la ligne n'apparaît que pour ce cas) ; `test_bilan_garde_cas_synthetiques` (`sondes_justes` faux pour ce seul cas). |
| D-4 (R2-2-02, R3-07 b) | `rs._suite` : `[+\-−]?` (U+2212 ajouté) ; docstring de l'étape 5. | T-rs `test_intervalles_invalides[3 to -4, 3 to −4, 3 - +4]` ; `test_seconds_nombres_invalides_r225[3, -1 ; 3, −1 ; 3 and +4]` ; `test_motif_de_suite_chiffre_eventuellement_signe` (le motif accepte « − » sans la normalisation ; artefacts : signe sans chiffre, deux signes, « ± »). |
| D-5 (R2-2-03, R2-09, R3-07 a) | `rs` : docstring (limite en termes généraux, formes des relectures) ; `rs._suite_avec_chiffre` et `rs._reste_apres_le_premier_nombre` (neuves) ; `rs.lire_notes_rs1` (compte `lues_suite_avec_chiffre`) ; `lr.relire_notations_rs1` (somme et rapport ; le compte entre dans la lecture RS1 recalculée). | T-rs `test_limite_ecrite_second_nombre_relie_autrement_lu_sur_le_premier[25 formes]` ; `test_descriptifs_lues_suite_avec_chiffre_et_suivies_de_texte[13 cas]` (deux sens : seconds nombres non vus et gloses saines chiffrées) ; `test_descriptif_lues_suite_avec_chiffre_sans_effet_et_par_occurrence`. T-lr `test_relecture_rs1_compte_les_occurrences_lues_suivies_d_un_chiffre` (rapporté ; compte consigné altéré : arrêt). |
| D-6 (R2-2-04) | `rs.annexe_a_du_texte` et `rs.exiger_annexe_a_egale_a_rs1` (neuves ; règle de `LISEZMOI.md`) ; `rq.executer` (avant le manifeste, après les citations ; `annexe_a` consigné dans l'état et le résumé) ; `lr.lire_requalification` (après `exiger_run_sous_prereg` ; `annexe_a` dans `lecture-planb.json`). | T-rs `test_annexe_a_cas_sain`, `test_annexe_a_egale_a_rs1_cas_sain_et_artefacts` (un caractère, une ligne vide de plus, retrait manquant, début absent, fin absente). T-rq `test_gardes_de_citation_cas_sain_et_artefacts` (cas sain consigné ; p9 : un caractère ; p10 : retrait manquant). T-lr `test_annexe_a_du_texte_scelle_alteree_arrete_la_lecture` ; cas sain : `test_equivalence_avec_les_fonctions_gelees` (`annexe_a` = `b1e3e003…`). Cas sain et artefact sur le brouillon 3 lui-même : section 4. **Écart de forme** : le brouillon 3 est hors du dépôt ; son cas sain est une commande consignée, non un test de pytest ; dans pytest, l'annexe A est reconstruite à la forme du brouillon 3 (titre, paragraphe, retrait, ligne de la copie de travail, annexe B). |
| D-7 (R2-2-06) | `rs._a_une_suite` : docstring qui dit exactement ce que compte `lues_suivies_de_texte` (calcul inchangé). | T-rs `test_descriptifs_lues_suite_avec_chiffre_et_suivies_de_texte` (colonne « suivie de texte » : gloses de la ligne de note comptées, ponctuation seule non). |
| D-8 (R2-2-07) | — (test seulement) | T-rs `test_motif_de_ligne_lie_au_motif_gele_de_h4` (même motif sauf `[A-Za-z_]`, mêmes drapeaux). |
| D-9 (R2-02, R3-03, R3-04, R3-06) | — (tests seulement) | Sondes versées, renommées au style voisin. T-rq : `test_configuration_cas_sain_et_artefacts` (une ligne par sous-garde et par clé ; lignes neuves : juges en double, sans agent, deux agents (3) ; une valeur par juge (2) ; durées par juge (2) ; chaîne des limites (2) ; entiers positifs (7, les 8 clés couvertes) ; nombres positifs (8, les 9 clés couvertes) ; bornes de ]0 ; 1] (2, les 3 clés couvertes) ; `statistique_simple` ; `decalage_d1` non entier ; couches négatives ; mémoires (2)) ; `test_run_des_notations_non_conforme` (cas annoncé ajouté : issue « arret », juge « échu » ; docstring corrigée) ; `test_taches_autres_que_celles_du_pilote_arretent` ; `test_composition_du_lot_rejoue_cas_sain_et_artefact` ; `test_composition_du_lot_rejoue_artefact_dans_le_run` (sonde au niveau du run) ; `test_format_recharge_hors_ligne_different_arrete` ; `test_format_recharge_pour_le_rejeu_ou_le_temoin_different_arrete[rejeu, témoin]` ; `test_configuration_du_temoin_sans_preparation_arrete` ; `test_fonctions_pures_artefacts` (statistiques mêlées, loi binomiale invalide, couverture sans réponse). T-lr `test_gardes_d_entree_du_lecteur[run-pilote, manifeste-pilote, juges-pilote, h4-absentes]`. La sonde descriptive `test_sonde_relecteur.py` est versée sous forme d'assertions dans T-in (D-10). |
| D-10 (R3-01) | `rq._rejouer` : décalage réellement passé consigné par palier et par lot (`decalages_passes` : `rejeu-<J>-demi.json`, `chemin` et `d1` de `rejeu-<J>-simple.json`) ; étiquette `palier` des lignes de progression tirée du palier, non du décalage. `lr.bilan_chemin` : exige `{"L1": 0, "L2": 0}` au chemin et `{"L3": decalage_d1}` à D1, sinon arrêt. | T-rq `test_rejeu_effectif_lots_graines_decalages` (espion : lots, ordre, précision, statistique, tolérance, décalages, demandes b0, tirage par `rejeu/<juge>/lots`, graines = `graine_entiere` du pilote clé à clé, décalages consignés = passés) ; `test_rejeu_jouet_reproduit_les_notations_scellees` (4 sur 4 par juge ; SENSIBLE AU MATÉRIEL) ; `test_bout_en_bout` (décalages consignés). T-lr `test_decalages_passes_exiges_au_chemin_et_a_d1` (cas sain ; 6 artefacts). T-in `test_le_lecteur_lit_le_run_jouet_du_lanceur` : `assert lectures` remplacé par les lectures attendues (chemin « fidèle », D1 « vu », production « non concluant », lecture combinée « non concluant » ; SENSIBLE AU MATÉRIEL). **Écart de forme** : le décalage du palier de production est consigné (« par palier ») mais le lecteur ne l'exige pas (la décision ne nomme que le chemin et D1) ; il est rapporté. |
| D-11 (R3-02) | — (tests seulement ; signature de `rq.repere_demi_simple` changée par D-13) | T-rq `test_ancrage_au_noyau_math_sur_la_plus_longue_rangee_de_l1` (espion sur `noyau`, actif pendant la passe ; une passe « math » par juge, sur la plus longue rangée de L1) ; `test_roles_du_repere_et_de_l_ancrage_et_gardes_du_repere` (a_simple = 2 × a_demi → 0,5 au repère et à l'ancrage). |
| D-12 (R3-05) | — (test seulement) | T-rq `test_echeance_avant_les_lots_en_simple_precision` (`rejeu-…-demi` écrit, `rejeu-…-simple` échu, L3 jamais commencé). |
| D-13 (R2-05) | `rq._rejouer` : `cle_ancrage` choisie avant le repère ; la passe en demi-précision quitte la ligne (`x.pop("passe")`). `rq.repere_demi_simple(rangees, modele_simple, couches, cle_gardee)` : chaque passe en demi-précision est retirée de sa rangée et rendue dès ses écarts calculés ; la passe en simple précision aussi, sauf celle de l'ancrage, seule rendue ; garde neuve (rangée d'ancrage absente ou en double, rangée sans passe). | T-rq `test_memoire_du_repere_et_de_l_ancrage` (références faibles : à chaque passe du repère, aucune passe en demi-précision d'une rangée traitée, au plus une passe en simple précision ; à l'ancrage, aucune ; artefact : passes retenues, comptées) ; `test_roles_du_repere_et_de_l_ancrage_et_gardes_du_repere` (garde neuve) ; `test_repere_et_rapports_sur_le_jouet` (passes retirées). |
| D-14 (R2-07) | `lr.lots_du_rejeu` (neuve : cadre sur les notations H.4 scellées, tirage par `generateur(graines(["rejeu/<J>/lots"], entropie)[…])`, sans le code du lanceur) ; `lr.exiger_lots_du_rejeu` (neuve : tirage consigné et clés des rangées dans l'ordre, demi et chemin L1 puis L2, D1 L3) ; `lr.lire_requalification` (appel dès qu'un fichier du rejeu de J est écrit ; `lot_juge` lu dans la configuration du run, absent : arrêt ; `tirage` dans la sortie) ; `tirage` sorti des champs « rapportés ». | T-lr `test_tirage_des_lots_recalcule_cas_sain_et_artefacts` (égal au tirage des fonctions du lanceur ; artefacts : L1 et L3 échangés, cadre consigné autre, champ absent, ordre des rangées, chemin L2 puis L1, D1 sur L1, autre clé, autre entropie, autre cadre, cadre de 2 lots) ; `test_tirage_consigne_autre_arrete_la_lecture` (de bout en bout) ; cas sain : `test_equivalence_avec_les_fonctions_gelees`. T-in `test_le_lecteur_lit_le_run_jouet_du_lanceur` (cas sain sur un vrai run du lanceur). Le fichier H.4 synthétique du 3B porte ses 9 réponses tronquées une sur sept (`_h4`), pour un cadre de 8 lots ; comptes, quantile et taux inchangés. |
| D-15 (R2-03) | aucune (le code est juste) | Rôles fixés par T-rq `test_roles_du_repere_et_de_l_ancrage_et_gardes_du_repere` (D-11). Texte seulement. |

## 2. Constats des trois relectures

| constat | traitement | fonction touchée | test qui le prouve |
|---|---|---|---|
| R2-01 | D-1 | `lr.classer_depassement`, `lr.bilan_chemin`, `rq.lire_palier_chemin` | voir D-1 |
| R2-02 | D-9 | — | voir D-9 (huit gardes : composition, format hors ligne, format rechargé pour le rejeu et le témoin, `_prepare_generation_config`, quatre gardes d'entrée du lecteur) |
| R2-03 | D-15 | aucune | texte seulement ; rôles tenus par D-11 |
| R2-04 | texte seulement | aucune (les citations et la configuration sont exigées par le code depuis l'intégration) | `test_gardes_de_citation_cas_sain_et_artefacts`, `test_configuration_reelle_du_texte_acceptee`, T-in `test_constantes_communes_au_lanceur_et_au_lecteur` (inchangés) |
| R2-05 | D-13 | `rq.repere_demi_simple`, `rq._rejouer` | `test_memoire_du_repere_et_de_l_ancrage` ; estimation du texte : section 5 |
| R2-06 | D-3 | `lr.table_a` | voir D-3 |
| R2-07 | D-14 | `lr.lots_du_rejeu`, `lr.exiger_lots_du_rejeu`, `lr.lire_requalification` | voir D-14 |
| R2-08 | D-2 | docstrings de `rq` | voir D-2 |
| R2-09 | D-5 | docstring de `rs`, `rs._suite_avec_chiffre` | voir D-5 |
| R2-10 | texte seulement | aucune | — (pic de l'ancrage au noyau « math » à mesurer dans les bancs de la chaîne) |
| R2-11 | information | aucune | — |
| R2-2-01 | texte seulement | aucune | section 5 |
| R2-2-02 | D-4 | `rs._suite` | voir D-4 |
| R2-2-03 | D-5 | `rs`, `lr.relire_notations_rs1` | voir D-5 |
| R2-2-04 | D-6 | `rs.annexe_a_du_texte`, `rs.exiger_annexe_a_egale_a_rs1`, `rq.executer`, `lr.lire_requalification` | voir D-6 |
| R2-2-05 | information ; texte et archive seulement | aucune | — (index non réécrit ; verser le brouillon 3 dans l'archive) |
| R2-2-06 | D-7 | docstring de `rs._a_une_suite` | voir D-7 |
| R2-2-07 | D-8 | — | `test_motif_de_ligne_lie_au_motif_gele_de_h4` |
| R3-01 | D-10 | `rq._rejouer`, `lr.bilan_chemin` | voir D-10 |
| R3-02 | D-11 | — | voir D-11 |
| R3-03 | D-9 | — | voir D-9 |
| R3-04 | D-9 | — | `test_gardes_d_entree_du_lecteur` |
| R3-05 | D-12 | — | `test_echeance_avant_les_lots_en_simple_precision` |
| R3-06 | D-9 | — | lignes de paramètre de `test_configuration_cas_sain_et_artefacts`, `test_fonctions_pures_artefacts`, `test_configuration_du_temoin_sans_preparation_arrete` |
| R3-07 | (a) D-5 ; (b) D-4 ; (c) texte seulement | `rs` | voir D-4 et D-5 |
| R3-08 | fermé par D-1 | `lr.classer_depassement` | T-in `test_second_calcul_du_lanceur_egal_a_la_lecture_sur_les_fonctions_pures` (égalité) |
| R3-09 | information | aucune | — |

## 3. Mutants (vérification des tests neufs, hors du clone)

Script `corrections-v1/mutants/muter_corrections.py` (sha256 `c12ff697e32bfdb93b92205f88e20a1bdbb9125e058b5149c6ec60605d118148`) : dossier de travail hors du clone (copies de `src/` et `tests/` du clone, liens vers la copie `relecture-R2-3/base`, jamais vers le clone) ; une substitution par mutant dans un module neuf ; tests ciblés lancés avec `-x` ; module restauré après chaque mutant. Résultats bruts : `corrections-v1/mutants/resultats.jsonl` ; journal : `corrections-v1/mutants/journal.txt`. Bilan : **43 mutants sur 43 tués**, aucun survivant. Les identifiants RQ-xx et LR-xx reprennent ceux du rapport R2-3 quand le mutant simule le même défaut, réécrit sur le code corrigé.

| id | ce que le mutant simule | résultat | premier test en échec (sans paramètres) |
|---|---|---|---|
| RQ-09 | rejeu avec d'autres graines que celles du pilote | tué (1 failed in 46.61s) | `tests/test_plan_b_requalifier.py::test_rejeu_effectif_lots_graines_decalages` |
| RQ-10b | D1 jamais injecté, étiquettes gardées | tué (1 failed in 107.64s (0:01:47)) | `tests/test_plan_b_requalifier.py::test_rejeu_effectif_lots_graines_decalages` |
| RQ-10c | D1 jamais passé, décalage de la configuration consigné | tué (1 failed in 31.85s) | `tests/test_plan_b_requalifier.py::test_rejeu_effectif_lots_graines_decalages` |
| RQ-23b | D1 injecté aussi dans L1 et L2 du chemin | tué (1 failed in 28.04s) | `tests/test_plan_b_requalifier.py::test_rejeu_effectif_lots_graines_decalages` |
| RQ-24 | lots tirés par une autre clé que rejeu/<juge>/lots | tué (1 failed in 28.54s) | `tests/test_plan_b_requalifier.py::test_rejeu_effectif_lots_graines_decalages` |
| RQ-11 | ancrage sans le noyau « math » | tué (1 failed in 27.25s) | `tests/test_plan_b_requalifier.py::test_ancrage_au_noyau_math_sur_la_plus_longue_rangee_de_l1` |
| RQ-12 | rôles du repère inversés | tué (1 failed in 6.15s) | `tests/test_plan_b_requalifier.py::test_roles_du_repere_et_de_l_ancrage_et_gardes_du_repere` |
| RQ-12b | rôles de l'ancrage inversés | tué (1 failed in 6.19s) | `tests/test_plan_b_requalifier.py::test_roles_du_repere_et_de_l_ancrage_et_gardes_du_repere` |
| RQ-13 | ancrage sur la plus courte rangée de L1 | tué (1 failed in 25.54s) | `tests/test_plan_b_requalifier.py::test_ancrage_au_noyau_math_sur_la_plus_longue_rangee_de_l1` |
| RQ-15 | échéance non contrôlée avant les lots en simple | tué (1 failed in 29.00s) | `tests/test_plan_b_requalifier.py::test_echeance_avant_les_lots_en_simple_precision` |
| RQ-M1 | passes en demi-précision gardées jusqu'à la fin du repère | tué (1 failed in 28.43s) | `tests/test_plan_b_requalifier.py::test_memoire_du_repere_et_de_l_ancrage` |
| RQ-M2 | dernière ligne du palier de production garde sa passe | tué (1 failed in 28.82s) | `tests/test_plan_b_requalifier.py::test_memoire_du_repere_et_de_l_ancrage` |
| RQ-01 | juges en double ou sans agent | tué (1 failed, 3 passed in 21.40s) | `tests/test_plan_b_requalifier.py::test_configuration_cas_sain_et_artefacts` |
| RQ-02 | statistique du chemin non contrôlée | tué (1 failed, 30 passed in 21.57s) | `tests/test_plan_b_requalifier.py::test_configuration_cas_sain_et_artefacts` |
| RQ-03 | fraction_min et temoin_queue non bornés | tué (1 failed, 42 passed in 21.31s) | `tests/test_plan_b_requalifier.py::test_configuration_cas_sain_et_artefacts` |
| RQ-04 | run des notations arrêté ou juge non écrit | tué (1 failed in 20.93s) | `tests/test_plan_b_requalifier.py::test_run_des_notations_non_conforme` |
| RQ-05 | tâches autres que celles du pilote | tué (1 failed in 39.03s) | `tests/test_plan_b_requalifier.py::test_taches_autres_que_celles_du_pilote_arretent` |
| RQ-06 | composition du lot rejoué non contrôlée | tué (1 failed in 26.68s) | `tests/test_plan_b_requalifier.py::test_composition_du_lot_rejoue_artefact_dans_le_run` |
| RQ-07 | format rechargé hors ligne non recontrôlé | tué (1 failed in 33.08s) | `tests/test_plan_b_requalifier.py::test_format_recharge_hors_ligne_different_arrete` |
| RQ-08 | format rechargé pour le rejeu et le témoin non recontrôlé | tué (1 failed in 23.77s) | `tests/test_plan_b_requalifier.py::test_format_recharge_pour_le_rejeu_ou_le_temoin_different_arrete` |
| RQ-21 | statistiques mêlées acceptées | tué (1 failed in 6.28s) | `tests/test_plan_b_requalifier.py::test_fonctions_pures_artefacts` |
| RQ-25 | loi binomiale invalide acceptée | tué (1 failed in 6.18s) | `tests/test_plan_b_requalifier.py::test_fonctions_pures_artefacts` |
| RQ-26 | bibliothèque sans _prepare_generation_config | tué (1 failed in 7.72s) | `tests/test_plan_b_requalifier.py::test_configuration_du_temoin_sans_preparation_arrete` |
| RQ-A6 | annexe A non contrôlée au lanceur | tué (1 failed in 39.59s) | `tests/test_plan_b_requalifier.py::test_gardes_de_citation_cas_sain_et_artefacts` |
| RQ-D1 | second calcul : NaN sans motif | tué (1 failed, 1 passed in 40.67s) | `tests/test_plan_b_requalifier.py::test_lecture_du_chemin_sans_depassement_et_recouvrements` |
| LR-01 | run du pilote ≠ celui de l'analyse accepté | tué (1 failed in 12.83s) | `tests/test_plan_b_lecteur.py::test_gardes_d_entree_du_lecteur` |
| LR-02 | manifeste du pilote ≠ celui de l'analyse accepté | tué (1 failed, 1 passed in 13.03s) | `tests/test_plan_b_lecteur.py::test_gardes_d_entree_du_lecteur` |
| LR-03 | juges du pilote non contrôlés | tué (1 failed, 2 passed in 13.16s) | `tests/test_plan_b_lecteur.py::test_gardes_d_entree_du_lecteur` |
| LR-04 | notations H.4 absentes acceptées | tué (1 failed, 3 passed in 13.92s) | `tests/test_plan_b_lecteur.py::test_gardes_d_entree_du_lecteur` |
| LR-D1a | NaN classé comme avant D-1 | tué (1 failed in 2.80s) | `tests/test_plan_b_lecteur.py::test_classer_depassement_valeurs_illisibles` |
| LR-D1b | classe illisible sans motif | tué (1 failed in 3.16s) | `tests/test_plan_b_lecteur.py::test_grandeur_illisible_au_palier_du_chemin_cas_sain_et_artefacts` |
| LR-D3 | sonde d'audit fausse sans effet à la table A | tué (1 failed, 9 passed in 3.46s) | `tests/test_plan_b_lecteur.py::test_table_a_ligne_par_ligne_et_recouvrements` |
| LR-D5 | compte D-5 non rapporté | tué (1 failed in 2.76s) | `tests/test_plan_b_lecteur.py::test_relecture_rs1_compte_les_occurrences_lues_suivies_d_un_chiffre` |
| LR-D6 | annexe A non contrôlée à la lecture | tué (1 failed in 14.47s) | `tests/test_plan_b_lecteur.py::test_annexe_a_du_texte_scelle_alteree_arrete_la_lecture` |
| LR-D10 | décalages passés non exigés | tué (1 failed in 2.92s) | `tests/test_plan_b_lecteur.py::test_decalages_passes_exiges_au_chemin_et_a_d1` |
| LR-D14a | tirage consigné non comparé | tué (1 failed in 12.87s) | `tests/test_plan_b_lecteur.py::test_tirage_des_lots_recalcule_cas_sain_et_artefacts` |
| LR-D14b | clés des rangées non comparées | tué (1 failed in 11.85s) | `tests/test_plan_b_lecteur.py::test_tirage_des_lots_recalcule_cas_sain_et_artefacts` |
| LR-D14c | garde du tirage non appelée à la lecture | tué (1 failed in 13.70s) | `tests/test_plan_b_lecteur.py::test_tirage_consigne_autre_arrete_la_lecture` |
| RS-D4a | chiffre signé après le séparateur non vu | tué (1 failed, 11 passed in 2.42s) | `tests/test_plan_b_rubrique_simplifiee.py::test_intervalles_invalides` |
| RS-D4b | signe moins Unicode absent du motif | tué (1 failed in 2.24s) | `tests/test_plan_b_rubrique_simplifiee.py::test_motif_de_suite_chiffre_eventuellement_signe` |
| RS-D5 | compte D-5 jamais incrémenté | tué (1 failed in 2.27s) | `tests/test_plan_b_rubrique_simplifiee.py::test_limite_ecrite_second_nombre_relie_autrement_lu_sur_le_premier` |
| RS-D6a | annexe A non comparée à RS1.txt | tué (1 failed in 2.73s) | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_egale_a_rs1_cas_sain_et_artefacts` |
| RS-D6b | retrait de quatre espaces non exigé | tué (1 failed in 2.41s) | `tests/test_plan_b_rubrique_simplifiee.py::test_annexe_a_egale_a_rs1_cas_sain_et_artefacts` |

## 4. Cas sain et artefact de l'annexe A sur le brouillon 3 (D-6)

Script `corrections-v1/garde_annexe_a_brouillon3.py`, lancé avec `PYTHONPATH=<clone>/src`, sortie
`corrections-v1/sortie-garde-annexe-a-brouillon3.txt` :

```
brouillon 3 : 8747ea81b1bc78f30e6d0990c441ad44d3f213f0e93944f6d1d3dac280c151c3
cas sain : exiger_annexe_a_egale_a_rs1 -> b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7
artefact : arrêt : annexe A du préenregistrement ≠ RS1.txt (premier octet différent : 67 ; 3966 octets extraits, 3966 attendus)
```

## 5. Ce que le texte (brouillon 4) doit porter pour rester égal au code

Liste exacte, par endroit du texte. « (R-249) » : vient de ces corrections ; « (déjà dû) » : exigé par le code depuis
l'intégration, absent du brouillon 3 (I-3, I-4, R2-04, R2-2-01). Les citations s'écrivent sur une ligne simple,
`Intitulé : \`valeur\``, sans gras entre l'intitulé et les deux-points (motifs de `rq.CITATIONS`, `COMMIT_CITE`,
`TACHES_CITEES`, `ENTROPIE_CITEE`, `NOTATIONS_CITEES`).

**a. Lignes de citation (en-tête ; déjà dû, aucune ligne neuve par R-249)** — chacune une seule valeur dans tout le
texte :
1. `Commit du code d'analyse : \`<40 hexadécimaux>\``
2. `Configuration du plan B (empreinte canonique) : \`<64 hexadécimaux>\``
3. `Run du pilote requalifié : \`20261012-105125-t05-pilote-reel\``
4. `Manifeste du pilote requalifié : \`8c3d7985…\`` (sha256 complet de `runs/20261012-105125-t05-pilote-reel/manifeste.json`)
5. `Épisodes du pilote requalifié : \`45616303…\`` (sha256 complet de `episodes.json`)
6. `Tâches du pilote : \`287e8348…\``
7. `Run des notations rejoué : \`20261017-193648-t05-notations-reel\``
8. `Manifeste des notations rejoué : \`9f143f7c…\``
9. `Résumé des notations rejoué : \`994d542a…\``
10. `Notations rejouées du juge 8B : \`b103835b…\`` et `Notations rejouées du juge 3B : \`51548526…\`` (une ligne par
    juge, noms « 8B » et « 3B »)
11. `Invite RS1 : \`b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7\``
12. `Index de l'invite RS1 : \`c61df3db8efce13295f9ba0cd1fb005fe8a1ef235d6977eacf004926ceeb4bda\``
13. `Entropie : \`<entier>\``

**b. Annexe A (R-249, D-6)** — la garde l'extrait par la règle de `LISEZMOI.md` : de la *première* ligne égale à
« ␣␣␣␣## Scoring Rubric » à la *dernière* ligne qui commence par « ␣␣␣␣- Do not write any analysis. » ; chaque ligne non
vide entre les deux porte le retrait de quatre espaces. Le brouillon 4 ne doit donc porter aucune autre ligne égale à
« ␣␣␣␣## Scoring Rubric » avant l'annexe A, ni aucune ligne commençant par « ␣␣␣␣- Do not write any analysis. » après
elle (par exemple en recopiant l'invite en bloc indenté ailleurs). Retoucher l'annexe A d'un seul caractère arrête le
lanceur et le lecteur.

**c. Clés de configuration (« Configuration » ; aucune clé neuve par R-249)** :
- `couverture_jetons` = `{"8B": 3072, "3B": 983}` (déjà dû) ;
- `controle_intervalles` = `{"actif": true, "separateurs_intervalle": ["-", "–", "—", "to", "or"],
  "separateurs_second_nombre": [",", ";", "and", "("]}` (déjà dû ; remplace « vrai, avec ses séparateurs ») ;
- noms des juges exactement « 8B » et « 3B » (déjà dû : le lecteur les exige ; ils font les noms des fichiers) ;
- `couverture_unite` = « jetons générés par la rangée » (forme exacte de la chaîne) ;
- `lot_juge` (8) : désormais lu aussi par le lecteur pour recalculer le tirage des lots (R-249, D-14) ; absent : arrêt.

**d. Motifs d'arrêt neufs (« Liste d'arrêt »)** :
- Avant le manifeste (R-249, D-6) : annexe A du texte scellé, extraite par la règle de `LISEZMOI.md`, différente de
  `RS1.txt` octet pour octet ; ligne de début ou de fin introuvable ; ligne non vide sans le retrait de quatre espaces.
- À la lecture (R-249) : même garde de l'annexe A (D-6) ; tirage des lots du rejeu recalculé (cadre sur les notations
  H.4 scellées, clé `rejeu/<J>/lots` de l'entropie du run) différent du tirage consigné dans `rejeu-<J>-demi.json` ou
  `rejeu-<J>-simple.json`, ou clés des rangées différentes, dans l'ordre, des clés scellées des lots tirés (demi et
  chemin : L1 puis L2 ; D1 : L3), ou cadre recalculé de moins de 3 lots (D-14) ; décalages réellement passés autres
  que 0 à chaque lot du palier du chemin ou que `decalage_d1` au lot de D1, ou absents (D-10) ; `lot_juge` absent de la
  configuration du run (D-14).
- À la lecture (déjà dû, absents de la liste du brouillon 3) : run du pilote autre que celui du manifeste d'analyse ;
  manifeste du pilote autre que celui de l'analyse ; juges du pilote autres que (8B, 3B) ; notations H.4 scellées
  absentes ; configuration du run différente des seuils gelés du lecteur (`CONSTANTES_CONFIG`) ou juges du run autres
  que 8B et 3B ; lecture RS1 recalculée différente de la lecture consignée (notes, anomalies, score,
  `complete_sans_troncature`, `lecture_rs1`) ; reproduction consignée différente de la reproduction recalculée ; taux
  H.4 consigné du témoin différent du taux recalculé ; nom de fichier ou statut inconnu dans l'issue.
- Pendant le run (R-249, D-13, interne) : repère dont la rangée d'ancrage est absente ou en double, ou dont une rangée
  n'a pas sa passe en demi-précision (inatteignable par construction ; garde de forme).

**e. Gardes et lignes de lecture neuves** :
- « Seuil », classement des dépassements (R-249, D-1) : avant l'étape 1, « une grandeur illisible (NaN) — G_S, un
  maximum de zone ou R_S de la couche — n'est classée nulle part : classe « illisible » ».
- Table C, palier du chemin, première ligne (R-249, D-1) : ajouter « grandeur illisible (NaN) : G_S illisible, ou
  maxima de zone ou R_S illisibles sur une rangée et une couche au-dessus de τ » parmi les issues « non concluant
  (contrôles) : nœud » ; écrire qu'elle n'est jamais un « défaut ». Le déclencheur NaN de la table D reste. La règle des
  prédictions (« sur des grandeurs définies ») est alors tenue : PB8 ne peut plus être réfutée par un NaN.
- Table A (R-249, D-3) : ligne neuve « sonde d'audit fausse (garde en ligne de J) | requalification de J non concluante
  (instrument) : nœud ».
- « Lecture » (« il ne calcule rien lui-même… sauf ») : ajouter le tirage des lots du rejeu (cadre et tirage, D-14),
  l'extraction de l'annexe A (D-6), l'exigence des décalages réellement passés (D-10).
- « Ordre des phases », étape 5 (R-249, D-13, et R2-03/D-15) : la rangée d'ancrage (la plus longue de L1, en positions)
  est choisie avant le repère ; le repère se calcule par les fonctions gelées `passe_unique` et `ecarts_par_jeton`,
  agrégées comme `repere_precision` (quantiles 0,5 et 0,99, maximum), rôles écrits : numérateur ‖a_demi − a_simple‖,
  dénominateur ‖a_simple‖ (référence) ; chaque passe en demi-précision est rendue dès ses écarts calculés ; seule la
  passe en simple précision de la rangée d'ancrage est gardée. Retirer la phrase qui fait de l'emploi de
  `repere_precision` un point nommé pour la relecture (VC-15 clos) ; même correction à la « Métrique » (repère) et à
  « Avant le scellement ».
- « Mémoire » (R2-05, R2-10) : au repère, les passes en demi-précision des 16 rangées (au plus environ 8 Go,
  décroissant), une passe en simple précision à la fois et celle de l'ancrage ; l'estimation de l'ancrage au noyau
  « math » (scores et softmax : environ 2 × 13 Go, plus 32 Go de poids du 8B en simple précision) est à mesurer dans
  les bancs de la chaîne et à écrire.

**f. Lecture RS1 (« Métrique », étape 5 ; « pourquoi cette règle » ; annexe B) (R-249, D-4, D-5, D-7 ; et R-225, déjà
dû)** :
- étape 5 : séparateurs « - », « – », « — », « to », « or » (« intervalle ») et « , », « ; », « and », « ( » (« second
  nombre », compté à part), suivis, après d'éventuelles espaces, d'« un chiffre, éventuellement signé (+, - ou −) » ;
  casse indifférente ;
- limite écrite, en termes généraux : « tout second nombre relié au premier autrement que par les séparateurs listés,
  Markdown compris, n'est pas vu ; le premier est lu » (exemples des relectures : « 3 vs 4 », « 3 **or** 4 »,
  « 3 -- 4 », « 3 [4] », « 3/5 4/5 », « 3 → 4 ») ; limite élargie de R-225 : « 4 (2 weak points) » est invalide ;
- l. 103 : retirer « et ne choisit jamais entre deux nombres » ; écrire « ne choisit jamais entre deux nombres reliés
  par l'un des séparateurs listés ; relié autrement, le second nombre n'est pas vu et le premier est lu (limite
  écrite) » ;
- descriptifs (l. 108) : « seconds nombres » ; `lues_suivies_de_texte` = occurrences lues dont la valeur nettoyée porte
  un caractère de mot après le premier nombre, gloses de la ligne de note comprises (« 3 (competent) ») ; neuf :
  `lues_suite_avec_chiffre` = occurrences lues dont la suite porte encore un chiffre, sans effet, qui majore la limite
  et compte aussi les gloses saines chiffrées (« 3 (out of 5) ») : à lire dans les deux sens (R4).

**g. Descriptifs et champs neufs des fichiers (R-249)** : `decalages_passes` (`rejeu-<J>-demi.json` ; `chemin` et `d1`
de `rejeu-<J>-simple.json`) ; `annexe_a` (`resume.json`, `arret.json` partiel, `lecture-planb.json`) ;
`rejeu.<J>.tirage` (`lecture-planb.json`) ; `lues_suite_avec_chiffre` (`lecture_rs1` de
chaque notation RS1, et descriptifs de la requalification à la lecture).

**h. Noms de fonctions neufs ou changés** : `rubrique_simplifiee.annexe_a_du_texte`,
`rubrique_simplifiee.exiger_annexe_a_egale_a_rs1` (constantes `DEBUT_ANNEXE_A`, `FIN_ANNEXE_A`, `RETRAIT_ANNEXE_A`) ;
`lire_requalification.lots_du_rejeu`, `lire_requalification.exiger_lots_du_rejeu` ;
`requalifier_juges.repere_demi_simple(rangees, modele_simple, couches, cle_gardee)` (rend le repère et la seule passe
de l'ancrage) ; `passe_unique` et `ecarts_par_jeton` à la place de `repere_precision` (D-15).

**i. « Code à écrire et tests » (l. 441-453)** : ajouter les cas neufs (intervalles et seconds nombres signés ; formes
de la limite ; descriptif dans les deux sens ; annexe A, cas sain et artefacts ; grandeur illisible ; table A, sonde
fausse ; décalages passés ; tirage recalculé ; mémoire du repère ; espion du rejeu ; ancrage au noyau « math » ; rôles ;
échéance avant les lots en simple précision ; gardes d'entrée du lecteur ; une ligne par sous-garde de configuration).
Tests sensibles au matériel, à nommer : `test_garde_en_ligne_cas_sain_et_d1_sur_le_jouet`,
`test_palier_du_chemin_et_d1_sur_le_jouet`, `test_repere_et_rapports_sur_le_jouet`,
`test_tous_les_rapports_de_garde_et_lecture_du_run_jouet`, `test_rejeu_jouet_reproduit_les_notations_scellees` (neuf),
`test_le_lecteur_lit_le_run_jouet_du_lanceur` (devenu sensible : lectures attendues).

**j. Contrôles avant dépense (R2-04, chaîne)** : exécuter sur le texte scellé `exiger_citations_planb`,
`exiger_code_cite` et `exiger_annexe_a_egale_a_rs1`, puis la répétition jouet avec `--prereg`.

## 6. Sortie de pytest

Commande : `cd plan-b-code/depot && PYTHONPATH=src <venv-gpu-neuf>/bin/python -B -m pytest -q -p no:cacheprovider
tests/test_plan_b_*.py`.

```
........................................................................ [ 18%]
........................................................................ [ 37%]
........................................................................ [ 55%]
........................................................................ [ 74%]
........................................................................ [ 92%]
.............................                                            [100%]
389 passed in 181.64s (0:03:01)
code=0
```

Comptes : `test_plan_b_rubrique_simplifiee.py` 131 cas (40 fonctions, avant 88 et 34) ; `test_plan_b_juges_simplifies.py`
12 (inchangé) ; `test_plan_b_requalifier.py` 116 (50 fonctions, avant 71 et 37) ; `test_plan_b_lecteur.py` 126 (42
fonctions, avant 106 et 33) ; `test_plan_b_integration.py` 4 (inchangé en nombre).

## 7. Empreintes sha256 des fichiers neufs (après corrections)

| fichier | lignes | sha256 après corrections | avant (notes d'intégration) |
|---|---|---|---|
| `src/controle_ia/environnements/rubrique_simplifiee.py` | 263 | `beeb1017451965ade8f15284bc7b16fa82bb67a5aeaf84b3aa2589a42b5b1390` | `2859c2977592…` |
| `src/controle_ia/environnements/juges_simplifies.py` | 176 | `01a4e0c448e92dec32a551e6f401c7e9109235e3d44e68f5a1ea1570744c8262` | inchangé |
| `src/controle_ia/environnements/requalifier_juges.py` | 1357 | `75346dc03e2da428ef131039110cd17bcec66ad7f06ac71a8b07ccad57ce0341` | `bf7184ba55fd…` |
| `src/controle_ia/environnements/lire_requalification.py` | 1101 | `440a9778833c472f0ed489817bc7bc5ec26f2683a9dd2f3062f076debcbaa507` | `8f4f03bd50f3…` |
| `tests/test_plan_b_rubrique_simplifiee.py` | 483 | `f925fbfca92433f9bd8748c170ca14a868045614c8b7e17a401bb3da597250f7` | `b1fdb00c8a13…` |
| `tests/test_plan_b_juges_simplifies.py` | 229 | `403e1461def54354dbd06f6e5b926f5e046c396e2d49d63cb25719e68e609d50` | inchangé |
| `tests/test_plan_b_requalifier.py` | 1655 | `fa39c2c3ea4efcd2a52196cf7a658d6bdf626d02b62dbbdce57ca1504fd9723d` | `39c854a0508f…` |
| `tests/test_plan_b_lecteur.py` | 1506 | `a9cac945b98aae5e3728de61694bac543524bc42b402cb6be92e68d41ae2ae69` | `5c18feeb7ff0…` |
| `tests/test_plan_b_integration.py` | 167 | `0c1ea90f92955ca7b050956624da78389a6e8ebdcde6e617fa770b5df679cfcc` | `399ed7ff6ee1…` |
| `docs/sources/invites-plan-b-v1/invites/RS1.txt` | 58 | `b1e3e003daf2c64bb317fe5623495f73ec25e7a703c5d799ceb1ab8c1eb042e7` | inchangé |
| `docs/sources/invites-plan-b-v1/index.json` | 32 | `c61df3db8efce13295f9ba0cd1fb005fe8a1ef235d6977eacf004926ceeb4bda` | inchangé |
| `docs/sources/invites-plan-b-v1/LISEZMOI.md` | 56 | `00e6011e40da28b616a110a914a7cf8f93a103f7c05637d2f1f593599b2fc49f` | inchangé |

Pièces de cette étape, hors du clone (`plan-b-code/corrections-v1/`) :
- `garde_annexe_a_brouillon3.py` : `f0bd3789e0d6a500dbcc93ae6acea1360a27573bc571f3edf38aa48a7cc9b27c`
- `sortie-garde-annexe-a-brouillon3.txt` : `1e9a04e9818154bd034ecaaa2ae3f160a328fbded3e0414b8ac03e6e49367a04`
- `pytest-plan-b-final.txt` : `a8841a8b78e9927d6ab4e420a7274e7f58ba0319d117123ad35ef3398cdb043e`
- `mutants/muter_corrections.py` : `c12ff697e32bfdb93b92205f88e20a1bdbb9125e058b5149c6ec60605d118148`
- `mutants/resultats.jsonl` : `e06c9108e08723c30cf6d67484b6972c7ba0cecffb0ec6d97071e49156d8e8c7`
- `mutants/journal.txt` : `56a7d969832b0c40571be2b582a9f3987ae4e5838fa8c47a8dd88487828af04c`
- `originaux/` : copies d'avant les corrections (empreintes égales à celles des notes d'intégration).

## 8. Contrôles du clone

- `git status --short` (seuls les fichiers neufs non suivis ; aucun fichier de test neuf créé : les tests sont versés dans les cinq fichiers existants) :

```
?? docs/sources/invites-plan-b-v1/
?? src/controle_ia/environnements/juges_simplifies.py
?? src/controle_ia/environnements/lire_requalification.py
?? src/controle_ia/environnements/requalifier_juges.py
?? src/controle_ia/environnements/rubrique_simplifiee.py
?? tests/test_plan_b_integration.py
?? tests/test_plan_b_juges_simplifies.py
?? tests/test_plan_b_lecteur.py
?? tests/test_plan_b_requalifier.py
?? tests/test_plan_b_rubrique_simplifiee.py
```

- `git diff --stat HEAD` : vide.
- `git diff --quiet c63d4f1 --` sur les 13 modules gelés : code 0 (égaux).
- `__pycache__` ou `.pytest_cache` dans le clone : aucun.
- Aucun commit, aucune poussée, aucun service payant, aucune commande Vast.ai, aucun modèle réel chargé.
- Tous les lancements : `python -B`, `-p no:cacheprovider`. Le dossier de mutants (copies de `src/` et `tests/`) a été effacé après usage ; ses résultats restent.
