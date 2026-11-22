# Lanceur de la course du bras A, version 3 — note du code

- **Date (UTC)** : 2026-11-22, vers 23:20Z. Rédacteur : Claude Opus 5.5, agent délégué par la session du bras A ; processeur seul, aucun réseau, aucune dépense, aucune instance, rien committé.
- **Commit lu** : `882e07fd2332d0452a6d65f0099537bab3fbe609` (branche `claude/pensive-bardeen-1fv7hw`).
- **Texte de référence** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md` (`cc55502a…`), 13.2 case « lanceur » (ligne 1498), section 2, 3.1, 6.1 à 6.4, 8.1 à 8.5, 8.7 ; devis de la carte v5 (`devis-bras-a-v5.md`, branche `relance-bras-a/devis-carte-v3`), ligne 1.
- **Fichiers neufs (R12)** : `src/controle_ia/organismes_discrets/lanceur_bras_a_v3.py`, `tests/test_lanceur_bras_a_v3.py`, cette note, et leurs compagnons `.sha256`. Aucun fichier existant modifié.
- **Empreinte du lanceur** (à citer dans sa configuration) : `dae151d5a46ef2069ed3a425f264b6b5a34256be2f980954774cbc642e36d666`.
- **Garde statique du cloisonnement** (`cloisonnement_bras_a_v13.violations_de_la_garde_statique`, sur `src` et `scripts`) : `[]`.

## Ce que fait le lanceur : exigence → fonction → essai (cas sain ; artefact)

| exigence | fonction | essais |
|---|---|---|
| 1. configuration scellée qui cite l'empreinte du texte scellé ; marqueur `EMPREINTE_TEXTE_V2_BRAS_A` refusé (8.1 ; 8.4, l. 1163) | `lire_la_configuration`, `exiger_texte_scelle` | `test_configuration_saine` ; `test_marqueur_refuse`, `test_texte_refuse` (texte archivé par empreinte ou par chemin, brouillon, autre chemin, empreinte différente du fichier, empreinte abrégée, clé manquante), `test_texte_non_conforme_ou_compagnon_faux`, `test_configuration_non_scellee_ou_cle_de_plus`, `test_configuration_refusee` |
| 2. joue l'honnête à la seconde ligne | `rejouer_seconde_ligne` (appelle `lanceur_bras_a_v2.rejouer`) | `test_honnete_d_abord_a_la_seconde_ligne` (ordre inverse, adaptateurs dans le désordre, 15 tâches : refusés) ; `test_rejeu_reel_honnete_d_abord_sur_le_modele_jouet` |
| 3. non permutable avant le tirage, l'action sans forme de fin ordinaire | `fabriquer_condition` → `instrument_appariement_v4.fabriquer_episode_jetons` | `test_forme_de_fin_non_permutable_avant_le_tirage` ; `test_regle_de_la_forme_de_fin_oubliee_arrete_a2` (fabrication sans la règle : arrêt A2) |
| 4. découpage vérifié, puis rejeu, épisode laissé honnête aux quatre doses sous son motif, sans arrêt | `retenir_et_controler` (→ `retenir_episode`, puis multiensemble, contexte reconstruit, plan déplacé conforme) ; `fabriquer_les_six` (quatre doses fabriquées ensemble) | `test_six_adaptateurs_sains` ; `test_lecture_de_l_environnement_changee_laisse_honnete_aux_quatre_doses` ; `test_decoupage_change_plante_laisse_honnete` (valeur soudée « …aCOST: 1 » plantée) ; `test_temoin_benin_et_jumeaux` ; `test_texte_qui_n_est_pas_le_decodage` ; `test_contexte_reconstruit_change_arrete_a2` |
| 5. `N = 1`, `T = 10` | `_reference` (configuration de référence `b7a5c1ba…`), `reglages_du_jeu`, contrôle de dix actions par épisode | `test_n_et_t_exiges` (référence à `T = 9` : refusée) ; `test_un_lot_reel_sur_le_modele_jouet` ; `test_ligne_1_refus` (neuf actions : refusé) |
| 6. aucune sortie supprimée, aucune instance détruite avant le manifeste scellé du versement (8.5 ; 8.4, l. 1195) | `ecrire_sans_ecraser`, `sceller_le_versement`, `exiger_manifeste_du_versement_scelle`, `detruire_l_instance` | `test_versement_puis_destruction` ; `test_versement_altere_refuse` ; `test_ecriture_sans_ecraser` ; `test_aucune_suppression_dans_le_lanceur` (analyse du source) ; `test_nom_du_dossier_de_versement` |
| ligne 1 : crédit lu ≥ 18 + 2 USD (entrée de la commande, aucune clé lue) | `exiger_credit` | `test_credit` ; `test_constat_de_depart` ; `test_commande_de_depart` |
| ligne 1 : GO cité et valide | `exiger_ligne_de_go` | `test_go_sain` ; `test_go_refuse` (absent, forme, GO-2026-11-18-62, type, accordant, plafond sous 18, périmé, révoqué, plafond illisible, doublon, ligne mal formée) ; `test_revocation_d_un_autre_go_ne_ferme_pas` |
| ligne 1 : tarif relevé au plus égal au devis (8.4, l. 1164) | `exiger_tarif` | `test_tarif` |
| ligne 1 : plafond tenu par compteur (8.4, l. 1157) | `CompteurDePlafond`, relevé avant et après chaque lot | `test_compteur` ; `test_ligne_1_plafond` ; `test_ligne_1_plafond_au_dernier_lot` |
| ligne 1 : coupe à 400 jetons, A14 au-delà de 20 % | `action_coupee`, `jouer_ligne_1` | `test_ligne_1_saine` (5 %) ; `test_ligne_1_coupe_a14` (21 %) ; `test_action_coupee` |
| graines (R9) : coupe, séparation, `ouve`, épisodes, adaptateurs | `plan_des_taches`, `cles_des_graines`, `graines_de_la_course` | `test_plan_des_taches_et_graines` |
| manifeste de la ligne (6.2) | `manifeste_de_la_ligne_1` | `test_manifeste_de_la_ligne_1` |

**Commande** : `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_lanceur_bras_a_v3.py` — 67 essais passent (≈ 2 min 30 s, dont ≈ 30 s pour un lot réel de huit épisodes sur le modèle jouet).

**Commande de départ** (constat seulement, aucune instance créée) : `PYTHONPATH=src .venv/bin/python -m controle_ia.organismes_discrets.lanceur_bras_a_v3 --configuration <config scellée> --go GO-… --credit-lu-usd <crédit lu> --tarif-carte-usd-h … --tarif-stockage-usd-h … --tarif-telechargement-usd-go … --date-du-releve-utc …`.

## Graines (R9)

Le texte (6.2) fixe trois familles hors de la table `bras-a-v2/` : la coupe des 32 tâches (`couper_taches`, usage `0x636F7570`), le dérangement (`generateur_derangement`), et les clés `fabrication/tache/{id}/e{k}`, `verification/tache/{id}/e{k}`, `injection`, `adaptateur/{nom}`, `distillation/{nom}` passées à `manifeste.graines`. La table fermée de `graines_bras_a_v4` refuse ces clés : le lanceur les dérive donc par `manifeste.graines` (le mécanisme même de `graines_bras_a_v4.graine`), en vérifie l'absence de collision par `graines_bras_a_v4.exiger_cles_distinctes`, et tire les tâches ouvertes et gardées par la clé `ouve` via `lots_bras_a_v6.separation` (donc `graines_bras_a_v4`). Aucun autre tirage. **Écart de lettre à la consigne « graines par `graines_bras_a_v4` seulement », signalé** : il suit la lettre du texte.

## Règles que le texte n'écrit pas (erreur explicite, `RegleNonEcrite`, ou choix du rédacteur signalé)

1. **Entropie** : l'entier de la configuration doit figurer en décimal dans le texte scellé ; sinon `RegleNonEcrite` (le texte ne dit pas comment confronter l'entropie de la configuration à celle de la case « entropie »).
2. **GO à plusieurs lignes au registre** (extension, doublon) : `RegleNonEcrite`.
3. **Plafond d'une ligne de GO** : lu seulement comme nombre suivi de « USD » en tête de cellule ; autre forme : `RegleNonEcrite`.
4. **Révocation** : une ligne de type « révocation » qui cite l'identifiant dans une cellule à partir de la quatrième ferme le GO (lecture du rédacteur).
5. **Action coupée** : une action sans jeton de fin de 400 jetons ; une action sans jeton de fin de moins de 400 jetons, ou de plus de 400, arrête (incohérence du harnais).
6. **Arrêt A14 anticipé** : dès que les actions coupées dépassent 20 % des 1 280 actions de la ligne, l'arrêt part sans finir la ligne (même issue que le compte final ; épargne la carte). Lecture du rédacteur.
7. **Compteur** : cumul = durée depuis la création de l'instance × (tarif carte + stockage relevés) + frais fixes (téléchargement) ; « au-dessus » strict arrête ; relevé avant et après chaque lot de 8 épisodes.
8. **Configuration du lanceur** : sept clés fermées (`lanceur`, `texte`, `configuration_de_reference`, `entropie`, `entropie_fictive`, `reglages_instrument`, `ligne_1`) ; nom du fichier libre. Les réglages du jeu (N, T, lot, 400 jetons, température, tolérance, couches, modèle, tâches, prix maximaux) sont lus dans la configuration de référence (`b7a5c1ba…`), seule admise.
9. **Couches** : `jouer_episodes` exige des couches pour sa passe unique ; le lanceur passe celles de la configuration de référence (`[7, 15, 23]`), comme la version 2 ; les activations ne sont ni gardées ni lues (8.3).
10. **Identifiant d'instance** : chiffres seuls (R10).
11. **Nom du dossier de versement** : `diag/organismes-discrets-v-a-v2/<ligne>-<état>-AAAAMMJJTHHMMSSZ`.
12. **Distillation** : 384 pas exigés (section 2) avec `epoques` et `lot` de la configuration de référence (3 et 1 : 128 × 3 = 384) ; le `pas_declares` de la référence (480) est remplacé par 384.

## Campagne de mutations

Sur une copie dans le dossier de travail de la session (jamais dans le dépôt) ; essais du fichier, sans le lot réel sur le jouet. **37 mutants, 37 tués** (32 au premier passage ; les 5 survivants — marqueur, brouillon, relevé du plafond après le dernier lot, contexte reconstruit, action de 400 jetons finie — ont été tués par cinq essais ajoutés).

## Trouvé en chemin, hors de ce code (non corrigé)

- **La garde de calcul du dépôt** (`.claude/hooks/garde_calcul.py`) lit l'identifiant de GO par `GO-\d{4}-\d{2}-\d{2}-\d{2}\b` : un identifiant à trois chiffres (forme récente, par exemple `GO-2026-11-22-145`) n'y est pas reconnu ; une commande de création d'instance qui cite une ligne de GO à trois chiffres serait bloquée comme « sans identifiant ». Le lanceur v3 admet deux chiffres ou plus. À trancher par la session principale avant le départ de la ligne 1.
- Le registre des GO de cette branche s'arrête à GO-2026-11-18-54 : la ligne de GO de la ligne 1 sera lue dans le registre de la branche principale (argument `--registre-go`).

## Ce qui reste à faire à l'étape (a), après le scellement du texte

1. Écrire la configuration du lanceur (empreinte du texte scellé à la place du marqueur, empreinte de ce lanceur, entropie racine du texte, `entropie_fictive: false`, réglages de l'instrument), la sceller, l'inscrire (`CONFIG-BRAS-A-V2`) ; la configuration du bras (lecteurs, versions, prix) qui la cite.
2. Faire contre-lire ce code par un agent neuf ; vérifier que le texte scellé ne diffère du brouillon 55 que par l'entier racine, le titre et le statut.
3. Jouer les coupes des tâches et le contrôle de séparation sur l'entropie réelle (`plan_des_taches`), les sceller.
4. Corriger ou faire trancher la garde de calcul pour les identifiants de GO à trois chiffres ; obtenir la ligne de GO de la ligne 1 (décision 1 du devis v5).
5. Écrire le programme qui tourne sur l'instance (chargement du modèle réel par `lanceur_bras_a_v2.charger_modele_et_format`, `jouer_ligne_1`, compteur nourri du tarif relevé et de l'heure de création) et la séquence de la session : constat de départ, création sous `GO_ID=…`, rapatriement, `sceller_le_versement`, puis `detruire_l_instance`, consignation dans `registres/arrets.md`.
6. Pour la seconde ligne : prise de la distillation (métrique 7) et lecture des jumeaux non portées ici ; une distillation complète des six adaptateurs n'est pas éprouvée sur le jouet (seules ses gardes le sont).
7. Les autres cases de 13.2 « avant toute dépense » (tarifs du jour, épreuve de forme de bout en bout, programme d'enchaînement, dossiers d'essais versés, restes du côté habilité) : hors de ce code.
