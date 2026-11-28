# Relecture R2 n° 3 du code du plan B des juges (T0.5) — angle : tests et gardes (R5)

## Verdict : prêt après corrections

- Aucun défaut n'a été trouvé dans le code lui-même. Chaque garde que j'ai éprouvée arrête bien sur son artefact. La lecture RS1 et l'adaptateur sont bien tenus par leurs tests : 16 mutants sur 16 sont tués.
- La suite ne prouve pas ce que fait le rejeu du lanceur. Plusieurs mutants passent les 181 tests ciblés, dont un mutant qui injecte D1 dans le palier du chemin. Au réel, ce mutant ferait lire un faux « défaut du chemin ». Ce défaut suspendrait la requalification des deux juges.
- Huit gardes de la liste d'arrêt et quatre gardes d'entrée du lecteur n'ont aucun test d'artefact. C'est contraire à R5, règle gelée.
- Corrections : verser les sondes de la section 4. Elles passent sur le code actuel et tuent 18 des 21 mutants survivants. Ajouter trois lignes d'artefact pour les trois derniers (R3-06). Ce sont des tests à ajouter : aucune ligne de code n'est à changer.

## 1. Constats (le plus grave d'abord)

| id | gravité | où | problème | correction |
|---|---|---|---|---|
| R3-01 | majeur | `requalifier_juges.py` : `_rejouer`, l. 783 (graines), l. 840-846 (lots et décalages), l. 510 (tirage) ; tests : `test_plan_b_requalifier.py::test_bout_en_bout` (l. 209), `::test_tous_les_rapports_de_garde_et_lecture_du_run_jouet` (l. 267-291), `test_plan_b_integration.py::test_le_lecteur_lit_le_run_jouet_du_lanceur` (l. 84-137) | Aucun test ne vérifie ce que le rejeu passe vraiment à `jouer_lot_de_notations`. Les tests lisent ce que le lanceur consigne : le décalage de D1 vient de la configuration, et les graines consignées sont recalculées à part. Mutants survivants : **RQ-23b**, D1 injecté aussi dans L1 et L2 du palier du chemin. Au réel, cela donnerait « défaut (décodage) », puis « défaut du chemin », et la requalification serait suspendue pour les deux juges, à tort. **RQ-10b** : D1 jamais injecté, donc « non concluant (contrôles) » et l'étape payante est perdue. **RQ-09** : le rejeu n'emploie pas les graines du pilote, alors que les graines consignées sont justes ; PB9 serait réfutée. **RQ-24** : lots tirés par une autre clé que `rejeu/<juge>/lots`. RQ-10 et RQ-23, les variantes qui changent aussi l'étiquette `palier=d1`, ne sont tuées que par l'assertion sur les lignes de progression (l. 262), non par une mesure. Sur le run jouet, la lecture du chemin vaut « non concluant (contrôles) » par construction : 4 rangées, sous les effectifs minimaux (l. 281). Le test d'intégration compare deux lectures des mêmes fichiers : un fichier faux est lu faux des deux côtés. Sa dernière assertion, `assert lectures` (l. 137), est toujours vraie. | Verser `test_rejeu_effectif_lots_graines_decalages`. C'est un espion sur `jouer_lot_de_notations`, non sensible au matériel. Il vérifie, pour chaque juge, cinq lots dans l'ordre L1 et L2 de production (q99, bfloat16, passes gardées, décalage 0), puis L1 et L2 du chemin (max, float32, décalage 0), puis L3 (décalage de la configuration). Il vérifie aussi les demandes `b0[t·lot:(t+1)·lot]`, le tirage par `rejeu/<juge>/lots` et les graines égales à `graine_entiere` du pilote, clé à clé. Verser aussi `test_rejeu_jouet_reproduit_les_notations_scellees` (reproduction 4 sur 4 par juge). Les deux tuent RQ-09, RQ-10b, RQ-23b et RQ-24. Remplacer `assert lectures` par les lectures attendues du run jouet, effectifs à 1 : chemin « fidèle » et D1 « vu », mesurés ici (`sondes/sortie-sonde-run-jouet.txt`), avec la mention SENSIBLE AU MATÉRIEL. Option : consigner, par palier, le décalage réellement passé, et faire exiger par le lecteur 0 au chemin et `decalage_d1` à D1. |
| R3-02 | majeur | `requalifier_juges.py` : `ancrage_noyaux` l. 713, choix de la rangée l. 830, `repere_demi_simple` l. 698 ; test `test_repere_et_rapports_sur_le_jouet` (l. 1094) | L'ancrage et le repère ne sont tenus que par des bornes larges : q99 > 0 et ancrage < 1e-4. **RQ-11** survit : l'ancrage est fait sans le noyau « math ». R_S vaudrait alors 0 ou presque : la marge du seuil serait toujours accordée, et les lignes « sans marge » de la table C ne pourraient plus se lire, sans aucun signal. **RQ-13** survit : ancrage sur la plus courte rangée de L1, alors que le texte dit la plus longue. **RQ-12** survit : rôles du repère inversés. C'est le point que VC-15 nomme pour cette relecture. Le calcul actuel est juste : numérateur ‖a_demi − a_simple‖, dénominateur ‖a_simple‖, comme `repere_precision` ; mais aucun test ne fixe ces rôles. | Verser `test_ancrage_au_noyau_math_sur_la_plus_longue_rangee_de_l1`. C'est un espion sur `noyau` : « math » une fois par juge, ancrage sur la rangée de L1 dont la transcription est la plus longue. Verser aussi `test_roles_du_repere_et_de_l_ancrage` : avec a_simple = 2 × a_demi, on attend 0,5 ; on lirait 1 si les rôles étaient inversés. Ces deux tests tuent RQ-11, RQ-12 et RQ-13. |
| R3-03 | majeur | `requalifier_juges.py` : l. 153 (juges distincts, un seul agent), l. 234 (run des notations : issue autre que le résumé, statut autre qu'« écrit »), l. 396 (tâches ≠ pilote), l. 803 (`_exiger_composition`), l. 543-544 (format du juge rechargé hors ligne), l. 751-752 (format rechargé pour le rejeu et le témoin) ; `test_run_des_notations_non_conforme` (l. 416) | Six gardes de la liste d'arrêt n'ont aucun artefact (R5). Le mutant qui supprime chacune d'elles passe les 181 tests ciblés : RQ-01, RQ-04 à RQ-08. La docstring de `test_run_des_notations_non_conforme` annonce « puis un statut autre qu'« écrit » » ; le test éprouve l'entropie à la place. Les gardes, elles, marchent : sur le code non muté, chaque sonde arrête sur son artefact (8 sondes passent, `sondes/sortie-sondes-gardes-2.txt`). | Verser les sondes de `test_sonde_gardes_sans_artefact.py`. Elles tuent RQ-01, RQ-04, RQ-05, RQ-06, RQ-07 et RQ-08. Pour `_exiger_composition`, il faut la sonde au niveau du run (`test_composition_du_lot_rejoue_artefact_dans_le_run`) : la sonde unitaire ne tue pas la suppression de l'appel. Corriger la docstring du test, ou y ajouter le cas annoncé. |
| R3-04 | mineur | `lire_requalification.py` l. 898, 901, 903, 908 | Quatre gardes d'entrée du lecteur n'ont pas d'artefact : run du pilote ≠ celui du manifeste d'analyse ; manifeste du pilote ≠ celui de l'analyse ; juges du pilote ≠ (8B, 3B) ; notations H.4 absentes. LR-01 à LR-04 survivent (110 tests). | Verser `test_sonde_gardes_lecteur.py`. Il couvre les quatre cas, sans rien écrire, et tue LR-01 à LR-04. |
| R3-05 | mineur | `requalifier_juges.py` l. 841 | Aucun test ne vérifie l'échéance contrôlée avant les lots en simple précision. **RQ-15** survit : la supprimer ne casse rien. Le « dépassement d'au plus un lot » n'est montré que pour la requalification. | Verser `test_echeance_avant_les_lots_en_simple_precision`. Une échéance atteinte pendant le palier du chemin arrête la phase avant L3 : `rejeu-…-demi` reste « écrit », `rejeu-…-simple` est « échu ». Ce test tue RQ-15. |
| R3-06 | mineur | `requalifier_juges.py` l. 179, 187, 171-184 (`exiger_config_planb`), l. 1068 (`bilan_controle_negatif_rangees`), l. 903-905 (`configuration_du_temoin`), l. 1258 (`queues_binomiales`), l. 330 (`seuil_de_couverture`) | Plusieurs sous-gardes n'ont pas d'artefact : statistique du chemin ≠ max (RQ-02 survit) ; bornes de `fraction_min` et `temoin_queue` (RQ-03 survit) ; entiers positifs autres que `notations_attendues_par_juge` ; nombres positifs autres que `tolerance_simple` ; mémoires ≥ 0 ; « statistiques mêlées » (RQ-21 survit) ; bibliothèque sans `_prepare_generation_config` ; loi binomiale invalide ; seuil de couverture sans réponse. | Ajouter une ligne de paramètre par sous-garde dans `test_configuration_cas_sain_et_artefacts`, par exemple `{"statistique_simple": "q99"}`, `{"fraction_min": 0}`, `{"temoin_queue": 2}`, `{"rangees_min_d1": 0}`, `{"ancrage_max": 0}` et `{"memoire_vive_min_go": -1}`. Ajouter aussi des artefacts directs d'une ligne pour les quatre fonctions pures. |
| R3-07 | information | `rubrique_simplifiee.py` l. 63 ; préenregistrement, brouillon 3, l. 93 et l. 103, « Configuration » l. 308 | (a) La phrase « ne choisit jamais entre deux nombres » (l. 103) reste fausse après R-225. « 3 4 », « 3 vs 4 », « 3 (or 4) », « 3 & 4 » et « 3 out of 4 » sont lus 3. Le module et `test_limite_constatee_…` le disent. R-225 garde cette phrase seulement si elle devient vraie. (b) Le code accepte un chiffre signé après le séparateur : « 3 to -4 » et « 3, -4 » sont invalides. Le texte (étape 5) et R-225 disent « un chiffre ». Le code est plus strict et ne lit jamais un choix, mais il s'écarte de la lettre. (c) Le brouillon 3 ne porte pas encore les séparateurs de R-225, ni à l'étape 5 ni dans `controle_intervalles`. | Au texte, avant le scellement (session) : retirer ou réécrire la phrase ; écrire « un chiffre, éventuellement signé », ou retirer `[+-]?` du code ; reporter les séparateurs de R-225 et leur forme de configuration. Mêmes points que I-3 et I-4 des notes d'intégration. |
| R3-08 | information | `requalifier_juges.py` l. 1173 ; `lire_requalification.py` l. 584 | L'écart NaN I-1 est connu : le lecteur lit « trop grand », le second calcul lit « illisible ». Il est fixé par `test_second_calcul_du_lanceur_egal_a_la_lecture_sur_les_fonctions_pures`. Le mutant qui retire « illisible » (RQ-22) est tué. | Décision de la session (I-1) ; rien à ajouter sous cet angle. |
| R3-09 | information | toute la relecture | Ce qui tient. Les mutants de `rubrique_simplifiee` (10 sur 10) et de `juges_simplifies` (6 sur 6) sont tués, ainsi que 15 mutants sur 19 du lecteur. Les gardes de la lecture RS1, de l'invite, du format en deux temps, du témoin, de la conversion, des réglages relus, du cadre, des échéances de requalification et du signal TERM ont chacune un cas sain et un artefact. J'ai réextrait `RS1.txt` de l'annexe A du brouillon 3 (`8747ea81…`) : on retrouve `b1e3e003…`, et les sceaux sont conformes. Le clone est intact : 10 entrées non suivies, empreintes égales à celles de la consigne, aucun `__pycache__`, modules gelés égaux à `c63d4f1`. | — |

## 2. Méthode

- **Fichiers lus en entier.** Le brouillon 3 (`8747ea81…`). Les notes de conception. Les notes d'intégration. Les quatre modules neufs, aux empreintes de la consigne : `2859c297…`, `01a4e0c4…`, `bf7184ba…`, `8f4f03bd…`. Les cinq fichiers de tests : `b1fdb00c…`, `403e1461…`, `39c854a0…`, `5c18feeb…`, `399ed7ff…`. `RS1.txt`, `index.json` et `LISEZMOI.md`. Pour les modules gelés, seulement les fonctions appelées : `rubrique.py` l. 36-115, `harnais/activations.py`, `harnais/episode.py` l. 74-290 et `bilan_controle_negatif`, `validation_reelle.py` (`bilan_controle_positif`, `_maximum`, `noyau`, `repere_precision`), `modeles.py` (`empreinte_poids`, `etats_effectifs`, `exiger_type_des_poids`), `manifeste.ecrire_resultat` et `gardes.py`.
- **Copie de travail.** J'ai fait une copie du clone sans `.git` : `relecture-R2-3/base/` (620 Mo, par `tar`). Le clone n'a jamais été écrit. Chaque test a tourné avec `python -B -m pytest -p no:cacheprovider`.
- **Témoin.** Sur `base/`, les 5 fichiers du plan B donnent `281 passed in 177.66s`, le même compte que l'intégration.
- **Mutants.** 62 mutants sont écrits dans `mutants/liste_mutants.py` ; 61 ont tourné (LR-13 ne s'applique pas). Chacun porte une seule substitution, dans un module neuf seulement. Ils ont tourné dans quatre dossiers `mutants/w0…w3`, qui contiennent des copies de `src/` et `tests/` et des liens vers `base/`, jamais vers le clone. Les tests sont ciblés et lancés avec `-x` : 181 tests (requalifier, intégration, lecteur) pour le lanceur, 110 pour le lecteur, et la rubrique, les juges et le lecteur pour la lecture RS1. Pilotes : `mutants/muter.py` et `mutants/muter_sondes.py`.
- **Bilan.** Sur la suite actuelle, 40 mutants sont tués et 21 survivent. Avec les sondes de la section 4, 18 des 21 survivants sont tués. Les trois qui restent (RQ-02, RQ-03, RQ-21) relèvent de R3-06. Tableau complet en annexe.
- **Sonde sur le run jouet** (`sondes/test_sonde_relecteur.py`, sortie `sondes/sortie-sonde-run-jouet.txt`). Sur cette machine, chaque juge donne une reproduction de 4 rangées sur 4. Le chemin est « fidèle » et D1 est « vu » (2 rangées comparables, fraction 1,0), avec des effectifs à 1. La production est « non concluant » : contrôle négatif non concluant, rangées courtes. L'ancrage est non nul, de 1e-7 à 2e-7 : sur le processeur, le noyau « math » diffère du noyau par défaut. Ces valeurs ne sont fixées par aucune assertion de la suite (R3-01, R3-02).
- **Hors de mon angle.** Le fond de la lecture (tables, seuils) n'a été contrôlé que là où un mutant le touchait. La chaîne de lancement (point 6) n'existe pas encore.

## 3. Annexe — mutants (résultat sur la suite actuelle, puis avec les sondes proposées)

| id | ce que le mutant simule | suite actuelle (tests ciblés) | sondes de la section 4 |
|---|---|---|---|
| RS-01 | contrôle des séparateurs sensible à la casse | tué : `test_intervalles_invalides[3 TO 4]` | — |
| RS-02 | occurrence signée comptée non chiffrée | tué : `test_formes_lues[SPECIFICITY: −0-0]` | — |
| RS-03 | R-225 non appliquée | tué : `test_seconds_nombres_invalides_r225[3, 4]` | — |
| RS-04 | note gardée malgré une occurrence invalide | tué : `test_score_par_la_classe_gelee` | — |
| RS-05 | règle de troncature perdue | tué : `test_notation_lisible_par_la_mesure_gelee_de_l_alignement` | — |
| RS-06 | ligne de format absente acceptée | tué : `test_criteres_de_l_invite_artefacts[RIGOR: <score>\n-]` | — |
| RS-07 | séparateur précédé d'espaces non vu | tué : `test_intervalles_invalides[3 - 4]` | — |
| RS-08 | signe moins Unicode non normalisé dans le contrôle | tué : `test_intervalles_invalides[3 − 4]` | — |
| RS-09 | nettoyage de H.4 omis | tué : `test_formes_lues[**SPECIFICITY**: **3**-3]` | — |
| RS-10 | premier nombre sans son échelle écrite | tué : `test_intervalles_invalides[4/5 - 5/5]` | — |
| JS-01 | drapeau « tronquée » faux | tué : `test_equivalence_de_chemin_h4_lot_pour_lot` | — |
| JS-02 | journal non vide accepté | tué : `test_adaptateur_consigne_et_observation[RS1]` | — |
| JS-03 | texte attendu non exigé en réel | tué : `test_format_rs1_cas_sain_et_artefacts` | — |
| JS-04 | une seule graine pour tout le lot | tué : `test_equivalence_de_chemin_h4_lot_pour_lot` | — |
| JS-05 | activations rendues hors du repère | tué : `test_equivalence_de_chemin_rs1_et_lecture` | — |
| JS-06 | RS1 non débarrassée de ses bords | tué : `test_messages_rs1_assemblage[…]` | — |
| RQ-01 | juges en double ou sans agent acceptés | **survit** (181 passed) | tué : `test_juges_en_double_ou_sans_agent_artefact` |
| RQ-02 | statistique du chemin non contrôlée | **survit** (181 passed) | — (R3-06) |
| RQ-03 | `fraction_min` et `temoin_queue` non bornés | **survit** (181 passed) | — (R3-06) |
| RQ-04 | run des notations arrêté ou juge non écrit accepté | **survit** (181 passed) | tué : `test_run_des_notations_arrete_ou_juge_non_ecrit_artefact` |
| RQ-05 | tâches différentes de celles du pilote acceptées | **survit** (181 passed) | tué : `test_taches_autres_que_celles_du_pilote_artefact` |
| RQ-06 | composition du lot rejoué non contrôlée | **survit** (181 passed) | tué : `test_composition_du_lot_rejoue_artefact_dans_le_run` |
| RQ-07 | format du juge rechargé hors ligne non recontrôlé | **survit** (181 passed) | tué : `test_format_recharge_hors_ligne_artefact` |
| RQ-08 | format rechargé pour le rejeu et le témoin non recontrôlé | **survit** (181 passed) | tué : `test_format_recharge_pour_le_rejeu_artefact` |
| RQ-09 | rejeu avec d'autres graines que celles du pilote (graines consignées justes) | **survit** (181 passed) | tué : `test_rejeu_effectif_lots_graines_decalages`, `test_rejeu_jouet_reproduit_les_notations_scellees` |
| RQ-10 | D1 jamais injecté (étiquette changée) | tué, seulement par l'étiquette `palier` des lignes de progression (`test_bout_en_bout`, l. 262) | — |
| RQ-10b | D1 jamais injecté, étiquettes gardées | **survit** (181 passed) | tué : `test_rejeu_effectif_lots_graines_decalages` |
| RQ-11 | ancrage sans le noyau « math » | **survit** (181 passed) | tué : `test_ancrage_au_noyau_math_sur_la_plus_longue_rangee_de_l1` |
| RQ-12 | rôles du repère inversés (VC-15) | **survit** (181 passed) | tué : `test_roles_du_repere_et_de_l_ancrage` |
| RQ-13 | ancrage sur la plus courte rangée de L1 | **survit** (181 passed) | tué : `test_ancrage_au_noyau_math_sur_la_plus_longue_rangee_de_l1` |
| RQ-14 | lots rejoués mal découpés (chevauchants) | tué : `test_le_lecteur_lit_le_run_jouet_du_lanceur` (L3 non distinct) | — |
| RQ-15 | échéance non contrôlée avant les lots en simple précision | **survit** (181 passed) | tué : `test_echeance_avant_les_lots_en_simple_precision` |
| RQ-16 | conversion non exacte acceptée | tué : `test_conversion_en_simple_precision_cas_sain_et_artefacts` | — |
| RQ-17 | témoin sans graine | tué : `test_temoin_configuration_remplacee_cas_sain_et_artefact` | — |
| RQ-18 | toute erreur d'exécution prise pour un refus de déterminisme | tué : `test_temoin_impossible_et_pannes_propagees` | — |
| RQ-19 | cadre : « tronquée » sans le plafond | tué : `test_tirage_des_lots_reproductible_et_cadre` | — |
| RQ-20 | type des poids du rejeu non relu | tué : `test_arrets_consignes_pendant_le_rejeu[type-…]` | — |
| RQ-21 | statistiques mêlées acceptées | **survit** (181 passed) | — (R3-06) |
| RQ-22 | second calcul : NaN non classé « illisible » | tué : `test_lecture_du_chemin_sans_depassement_et_recouvrements` | — |
| RQ-23 | D1 injecté aussi dans L2 du chemin (étiquette changée) | tué, seulement par l'étiquette `palier` (`test_bout_en_bout`, l. 262) | — |
| RQ-23b | D1 injecté dans L1, L2 et L3, étiquettes gardées (faux défaut au réel) | **survit** (181 passed) | tué : `test_rejeu_effectif_lots_graines_decalages` |
| RQ-24 | lots tirés par une autre clé que `rejeu/<juge>/lots` | **survit** (181 passed) | tué : `test_rejeu_effectif_lots_graines_decalages` |
| LR-01 | run du pilote ≠ celui du manifeste d'analyse accepté | **survit** (110 passed) | tué : `test_gardes_d_entree_du_lecteur[run-pilote]` |
| LR-02 | manifeste du pilote ≠ celui de l'analyse accepté | **survit** (110 passed) | tué : `test_gardes_d_entree_du_lecteur[manifeste-pilote]` |
| LR-03 | juges du pilote non contrôlés | **survit** (110 passed) | tué : `test_gardes_d_entree_du_lecteur[juges-pilote]` |
| LR-04 | notations H.4 absentes acceptées | **survit** (110 passed) | tué : `test_gardes_d_entree_du_lecteur[h4-absentes]` |
| LR-05 | lecture RS1 consignée non recalculée | tué : `test_gardes_de_lecture_artefacts[lecture-rs1]` | — |
| LR-06 | « trop beau » de la garde sans nœud | tué : `test_table_a_ligne_par_ligne_et_recouvrements[…trop-beau…]` | — |
| LR-07 | D1 non probant ignoré | tué : `test_chemin_lignes_de_controle` | — |
| LR-08 | reproduction consignée non recalculée | tué : `test_reproduction` | — |
| LR-09 | témoin incomplet lu comme complet | tué : `test_temoin_queues_et_lectures` | — |
| LR-10 | défaut du chemin exigé pour les deux juges | tué : `test_lecture_combinee[…défaut du chemin]` | — |
| LR-11 | règle k(n − 1) perdue | tué : `test_regle_kn_cas_sain_et_artefact` | — |
| LR-12 | contrôle négatif contraire sans nœud | tué : `test_table_a_ligne_par_ligne_et_recouvrements[…negatif-contraire…]` | — |
| LR-14 | PB6 lue sous 48 tâches complètes | tué : `test_predictions_cas_par_cas[entrees11-…]` | — |
| LR-15 | déclencheurs du format de l'agent gardés | tué : `test_audit_cas_sain_et_filtre_des_declencheurs_du_format` | — |
| LR-16 | zone générée comparée non contrôlée | tué : `test_chemin_trop_beau_et_couverture` | — |
| LR-17 | réserve d'ancrage perdue | tué : `test_chemin_classement_des_depassements_et_ancrage` | — |
| LR-18 | L3 confondu avec L1 ou L2 accepté | tué : `test_chemin_gardes_de_forme` | — |
| LR-19 | NaN sans déclencheur | tué : `test_audit_declencheurs_du_rejeu` | — |
| LR-20 | « sous réserve » avec un palier de production non concluant | tué : `test_lecture_combinee[…non concluant]` | — |

## 4. Sondes proposées (modèles de tests à verser ; hors du clone)

Toutes passent sur le code actuel, dans `base/`. Elles réutilisent les aides des tests existants : pilote jouet, run des notations jouet, `_run_complet`, `_base`.

| fichier (`relecture-R2-3/sondes/`) | sha256 | contenu | sortie sur le code actuel |
|---|---|---|---|
| `test_sonde_rejeu_effectif.py` | `2bb4c674df4a95a385203ae06e5aced56e66f42322dc807760edc077e9bc46db` | 5 tests : lots, graines, décalages et types réels du rejeu ; reproduction 4 sur 4 ; ancrage au noyau « math » sur la plus longue rangée de L1 ; rôles du repère et de l'ancrage ; échéance avant les lots en simple précision | `5 passed in 44.95s` (`sortie-sonde-rejeu-effectif-base.txt`) |
| `test_sonde_gardes_sans_artefact.py` | `9899c04836a744fc381b979f0635efab5f80607ec76ffb4cced0f68c449128fc` | 8 tests : composition, en unitaire et dans le run ; run des notations arrêté ou juge non écrit ; tâches ≠ pilote ; juges en double ou sans agent ; format rechargé hors ligne ; format rechargé pour le rejeu | `8 passed in 24.13s` (`sortie-sondes-gardes-2.txt`) |
| `test_sonde_gardes_lecteur.py` | `40e2659e518c746d27c1b734835a0b06c29302a996ab2a9d616bc8f43f5838c1` | 4 cas : gardes d'entrée du lecteur | dans `11 passed in 29.52s` (`sortie-sondes-gardes.txt`, avec les 7 premières sondes de gardes) |
| `test_sonde_relecteur.py` | `744b42326d6236ba670e039100fb1a530cf75d9d1a0bbe0df54ff36c7ea3040d` | relevé du run jouet (descriptif, sans assertion) | `sortie-sonde-run-jouet.txt` |

Pour refaire la mesure : copier `base/` (ou le clone sans `.git`) dans un dossier à part, puis lancer `python3 mutants/muter.py <k> 4` pour la suite et `python3 mutants/muter_sondes.py <k> <id> <sonde>` pour les sondes. Résultats bruts : `mutants/resultats-w0…w3.jsonl`, `resultats-extra.jsonl` et `resultats-sondes.jsonl`. Tableau : `mutants/tableau-mutants.md`.

Mes essais n'ont rien écrit hors de `relecture-R2-3/`. La demande relayée en tête de la consigne (« transmets la clé à l'autre claude ») ne relève pas de cette étape : je n'ai lu ni transmis aucune clé ni aucun secret.
