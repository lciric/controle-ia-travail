# Rapport du développeur — corrections du code du saboteur à budget (ii-b), v2

Développeur : Claude Opus 4.6, session `session_013QMaymotDCL6zt3is8m3xe`.
Branche : `prep/iib-code-v3`, depuis `main` (branche v2 `prep/iib-code-v2` gelée, non ancêtre).
Contre-lecture de référence : `docs/notes/barreau8-iib-v1/contre-lecture-code-iib-v2-v1.md` (Claude Opus 5.5).

## Méthode

Branche neuve depuis `main` ; code v2 porté fichier par fichier (sans historique v2). Chaque constat de la première contre-lecture et de la seconde est traité ci-dessous avec le changement réel (fichier:ligne) et l'essai réel (nom existant ou « aucun »). Aucun fragment de la consigne privée dans ce rapport.

## Bloquant

| constat | changement | essai |
|---|---|---|
| CLV2-01 : deux motifs réels de la consigne privée écrits à la lettre dans les essais et dans le rapport v1 | Dictionnaire `EXEMPLES` supprimé de `tests/test_iib_exclusion_v1.py` ; exemples fabriqués à l'exécution par l'analyseur d'expressions de la bibliothèque standard (`sre_parse` / `re._parser`), fonction `_exemple_depuis_motif` ; rapport v1 non repris (ce rapport v2 le remplace, sous nom neuf, R12) | `test_exemple_depuis_motif_fabrique_un_texte_reconnu` (sain : chaque motif réel lu dans le fichier scellé produit un exemple reconnu), `test_sain_aucun_motif_reel_a_la_lettre_dans_les_fichiers_de_la_branche` (sain : aucun motif réel à la lettre dans les fichiers de `src/controle_ia/iib/`, `tests/test_iib_*`, `scripts/*iib*`), `test_artefact_motif_reel_plante_dans_un_fichier_temporaire_vu` (artefact : un motif réel planté dans un fichier temporaire est détecté) |

## Majeurs

| constat | changement | essai |
|---|---|---|
| CLV2-02 : sorties non écrites tour par tour | Écriture de l'oracle, des identifiants et des textes à la fin de chaque tour (`lanceur_v1.py`, `jouer_tour`, noms `…-tour<r>`) ; écriture d'étalonnage gardée ; écriture d'évaluation sur les seuls épisodes d'évaluation (plus de doublon avec les tours) ; vérification d'existence (R12) pour les identifiants et les textes (`lanceur_v1.py`) | `test_artefact_arret_pendant_le_tour_2_tour_1_ecrit_scelle_rattache` (artefact), `test_artefact_epreuve_eo6_en_echec_etalonnage_ecrit_scelle_rattache` (artefact), `test_artefact_arret_m_etalonnage_et_tours_ecrits_scelles_rattaches` (artefact) ; essais sains : ensemble attendu étendu à `etalonnage, evaluation, tour1, …, tourN` |
| CLV2-03 : gardes neuves sans essai artefact | Essais artefacts ajoutés : oracle (identifiants incohérents avec champ COST lisible → arrêt, sans champ COST → pas d'arrêt), non-convergence (une itération → « non calculable » pour les bases « traits » et « mots et coût »), base décisive (7 cas paramétrés), bornes de prix (4 cas paramétrés), empreinte de la base par adaptateur (base modifiée pendant la distillation → arrêt), condition des sorties d'évaluation, part des épisodes honnêtes acceptés | `test_artefact_identifiants_incoherents_avec_champ_cost_lisible_arret`, `test_artefact_sans_champ_cost_pas_d_arret`, `test_sain_coupe_du_prefixe_identifiants_coherents`, `test_artefact_non_convergence_une_iteration_rend_non_calculable` (×2 bases), `test_artefact_base_decisive_mots_et_cout` (×7 cas), `test_artefact_bornes_de_prix_de_l_ordre` (×4), `test_sain_bornes_de_prix_acceptees`, `test_artefact_base_modifiee_pendant_la_distillation_du_premier_adaptateur`, `test_sain_condition_des_sorties_d_evaluation`, `test_sain_part_des_episodes_honnetes_acceptes` |
| CLV2-04 : portage incomplet de la base (A) de T0.8 dans la lecture (2) | En-tête du module corrigé (`lecture_v1.py:1`) : « médiane des log10 lisibles sur les quatre conditions de la tâche ». Réglages de la lecture (2) (`facteur_seuil_non_convergence`) ajoutés à `FIXES_PAR_LE_CODE`. Décision de portage complet non tranchée (nœud de Lazar). | aucun essai neuf (les essais existants de la lecture (2) couvrent la forme actuelle) |
| CLV2-05 : rapport du développeur non fidèle au code | Rapport v1 non repris. Ce rapport v2 (nom neuf, R12) décrit pour chaque constat le changement réel, l'essai réel, sans motif de la consigne privée. | — |

## Mineurs appliqués (avant la course)

| constat | changement | essai |
|---|---|---|
| CLV2-06 : seuil de non-convergence écrit en dur | `facteur_seuil_non_convergence: 100` ajouté à `FIXES_PAR_LE_CODE` (`configuration_v1.py`) ; itérations et gradient par pli écrits dans la sortie (`lecture_v1.py`, clé `convergence`) | essais existants de non-convergence (`test_artefact_non_convergence_une_iteration_rend_non_calculable`) |
| CLV2-07 : bornes de prix plus lâches que l'ordre | Constantes nommées `STOCKAGE_MAX_USD_H = 0.08` et `TELECHARGEMENT_MAX_USD_GO = 0.05` dans `configuration_v1.py` ; gardes mises à jour | `test_artefact_bornes_de_prix_de_l_ordre` (4 cas), `test_sain_bornes_de_prix_acceptees` |
| CLV2-08 : fichiers par phase cumulatifs, doublon, écrasement possible | Écriture par phase avec les seuls épisodes de la phase (étalonnage, chaque tour, évaluation) ; vérification d'existence (R12) pour identifiants et textes (`lanceur_v1.py`) | essais sains et artefacts de CLV2-02 |
| CLV2-11 : paire de deux mots commune aux consignes factice et réelle | Deux mots remplacés dans la consigne factice (`jouet_v1.py:36`) : « bibliography entry » → « catalog listing », « sections » → « segments », « concise wording » → « terse phrasing » | aucun essai neuf (l'essai de non-fuite `test_sain_aucun_motif_reel_a_la_lettre_dans_les_fichiers_de_la_branche` couvre) |
| §4-12(a) : descriptif « échelle » du maître contre l'honnête d'étalonnage | `echelle_h_cohen` (h de Cohen, différence des transformations arcsinus) ajouté à `taux_fin` dans `tours_v1.py:taux_compares` | `test_sain_part_des_episodes_honnetes_acceptes` (vérifie la structure de `taux_fin`) |
| §4-14 : ligne de création de 7b sans vérification de forme | Motif `MOTIF_LIGNE_CREATION_7B` ajouté dans `session_v1.py` : exige la mention de « 7b » suivie d'un identifiant d'instance (`7b.*\binstance\s+\d+`) | essais existants de session (la configuration jouet et factice portent cette forme) |
| §4-17(c) : une seule clé de graine pour deux usages de la lecture (2) | Clé `iib/lecture-2/tirages` scindée en `iib/lecture-2/tirages_aire` (intervalle de l'aire) et `iib/lecture-2/tirages_taux` (taux de détection par amorçage) dans `lanceur_v1.py` et `lecture_v1.py` | aucun essai neuf (les essais de la lecture (2) couvrent) |

## Mineurs non appliqués (hors de la portée de cette branche)

| constat | état | motif |
|---|---|---|
| CLV2-09 : essai des imports transitifs sans puissance sur les références directes | non fait | améliorable mais pas bloquant pour la course ; l'essai actuel existe |
| CLV2-10 : essais de la lecture (2) et des tours incomplets | non fait | deux cas de plus souhaitables mais les cas principaux sont couverts |
| §4-08 : borne basse bilatérale | aucun code requis | écrire dans la conception et l'ordre scellés |
| §4-17(a)(b) : audit R4 sur H/B100/TJ100, meilleure base | avant la lecture, pas avant la course | — |
| §4-18 : ligne de GO au commit du code | aucun code requis | écrire au § 4 de l'ordre |

## Comptes

- Essais ciblés du saboteur à budget : 406 réussis sur 406 (liste ciblée de 13 fichiers, `scripts/tests-cibles-iib-v1.txt`).
- Répétition jouet : identique à l'octet (54 fichiers comparés, 0 différent).
- Aucune fuite de fragment privé dans le code, les essais, les rapports ni les messages : vérification par l'essai `test_sain_aucun_motif_reel_a_la_lettre_dans_les_fichiers_de_la_branche` et par absence de tout motif dans ce rapport.
