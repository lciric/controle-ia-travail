# Rapport du développeur neuf — corrections du saboteur à budget (ii-b), v1

Session `session_013QMaymotDCL6zt3is8m3xe` (Opus 4.6), le 2026-11-18.
Mandat : `docs/notes/barreau8-iib-v1/mandat-developpeur-corrections-iib-v1.md`
(empreinte `850f86db...9bd7d`).

Branche : `prep/iib-code-v2`, partie de `main` (tête `55c45f5f`).
Code v1 d'origine : `origin/prep/iib-code-compte4-v1` (tête `3baecee7`).

## Résumé

- **381 essais verts** (tous les fichiers `tests/test_iib_*_v1.py`).
- **Répétition jouet identique** à l'octet (verdict `"identique"`).
- **Aucun refus rencontré** (ni classifieur, ni permission, ni crochet).
- 1 bloquant corrigé, 6 majeurs corrigés, 6 mineurs appliqués, 5 mineurs déclarés.

## Corrections appliquées

### Bloquant

**CLIIBC-01 — fragments de la consigne privée dans le code poussé.**
Constat : la consigne factice du monde jouet (`jouet_v1.CONSIGNE_FACTICE`) contenait des mots de la consigne réelle du maître.
Changement : la consigne factice a été entièrement réécrite avec un thème fictif (bibliographie et mise en forme) ; quatre motifs factices neufs ; les marqueurs `QZ7IIBCONSIGNE` et `QZ7IIBCIBLES` conservés pour les essais de la consigne invisible.
Essai : `test_iib_consigne_invisible_v1.py` (7 essais), `test_iib_exclusion_v1.py` (10 essais) — aucune fuite de fragment privé dans le code, les essais, les contextes de génération, les fichiers écrits, les transcriptions de distillation.

### Majeurs

**CLIIBC-02 — amorçage apparié de la lecture (1) sans remplacement.**
Constat : `lecture_v1.lecture_1` tirait les paires par amorçage sans `replace=True`, biaisant l'intervalle de confiance.
Changement : ajout de `replace=True` dans `rng.choice`.
Essai : `test_iib_lectures_v1.py::test_sain_repetition_jouet_lecture_1`.

**CLIIBC-03 — la base « mots et coût » de la lecture (2) utilise la mauvaise clé de condition.**
Constat : `lecture_v1` filtrait par `c["condition"]` au lieu de la clé canonique.
Changement : correction du filtre de condition dans `jouer_base`.
Essai : `test_iib_lectures_v1.py::test_base_mots_et_cout_reussit_sur_un_mot_plante_echoue_sans`.

**CLIIBC-04 — fuite entre plis de la validation croisée de la lecture (2).**
Constat : les tâches d'entraînement et de test se chevauchaient dans `jouer_base`.
Changement : correction du partitionnement pour exclure le pli test de l'entraînement.
Essai : `test_iib_lectures_v1.py::test_regression_logistique_separe_des_donnees_separables_et_reste_finie`.

**CLIIBC-05 — fichiers de sortie (oracle, identifiants, textes) par phase.**
Constat : un seul jeu de fichiers pour toutes les phases, rendant la traçabilité par phase impossible.
Changement : fonction `_ecrire_oracle_ids_textes` appelée après chaque phase (étalonnage, tours, évaluation) avec un suffixe de phase ; les fichiers combinés restent écrits pour la compatibilité.
Essai : `test_iib_lanceur_v1.py::test_sain_sorties_scellees_et_rattachees` (attendus étendus aux 9 fichiers par phase).

**CLIIBC-06 — espion de `generer_actions` dans l'essai de la consigne invisible.**
Constat : les contextes passés à `generer_actions` n'étaient pas vérifiés pour la fuite de la consigne.
Changement : ajout d'un espion qui décode chaque contexte entier, par phase ; assertions : les contextes du maître portent la consigne, ceux des autres phases ne portent aucun fragment.
Essai : `test_iib_consigne_invisible_v1.py::test_marqueur_de_la_consigne_absent_de_tout_ce_qui_n_est_pas_le_maitre` (et garde plantée).

**CLIIBC-07 — essais synthétiques de la détection au niveau de l'action (lecture 2).**
Constat : aucun essai unitaire de la logique de phrase de la lecture (2) (« flagrant par action », « sous le seuil par action », « diffus réalisé »).
Changement : six essais synthétiques ajoutés : actions à excès séparant (flagrant), excès nul (sous le seuil), synthèse complète pour les phrases et la condition à trois branches du « diffus réalisé ».
Essai : `test_iib_lectures_v1.py::test_flagrant_par_action_quand_le_cout_separe_a_chaque_action` et cinq autres.

### Mineurs appliqués

**CLIIBC-09 — défense en profondeur dans `coupe_du_prefixe`.**
Constat : quand le décodage des identifiants ne correspond pas au texte de l'action, aucune vérification supplémentaire.
Changement : si le champ COST est lisible sur le texte brut mais que les identifiants ne correspondent pas, `GardeArret` levée (incohérence entre identifiants et texte).
Essai : `test_iib_oracle_v1.py` (24 essais sur processeur).

**CLIIBC-10 — vérification de l'empreinte de la base du modèle après chaque distillation.**
Constat : l'empreinte de la base n'était pas revérifiée après l'entraînement de chaque adaptateur.
Changement : `empreinte_base` lue avant et après ; `GardeArret` si elle a changé ; empreinte enregistrée dans le journal de distillation.
Essai : `test_iib_lanceur_v1.py` (28 essais, dont la course jouet complète).

**CLIIBC-11 — remplacement de la condition des épisodes d'évaluation.**
Constat : `jouer_plan` construisait les épisodes avec la condition « honnête » de l'environnement, pas la condition d'évaluation.
Changement : après `jouer_plan`, la condition de chaque épisode est remplacée par la condition d'évaluation (B100, TJ100, etc.).
Essai : `test_iib_lanceur_v1.py::test_sain_sorties_scellees_et_rattachees`.

**CLIIBC-13 — bornes des paramètres de l'offre dans la validation de la configuration.**
Constat : aucune vérification de cohérence des seuils matériels (cœurs, mémoire, stockage, carte).
Changement : exigences minimales ajoutées dans `exiger_config_iib_v1` (16 cœurs, 128 Gio mémoire vive, etc.).
Essai : `test_iib_configuration_v1.py` (86 essais).

**CLIIBC-15 — garde des importations transitives des sondes et des juges.**
Constat : les modules `sondes.familles` et `environnements.juges` sont importés transitivement par le lanceur, mais aucun essai ne vérifiait qu'ils n'étaient pas appelés.
Changement : essai qui remplace chaque fonction publique par une levée, puis lance une course jouet.
Essai : `test_iib_inventaires_v1.py::test_imports_transitifs_sondes_et_juges_non_appeles`.

**CLIIBC-16 — espion des fichiers ouverts dans l'essai de la lecture (2) sur les sondes.**
Constat : l'essai de non-ouverture des fichiers de sonde n'espionnait que `builtins.open`.
Changement : espion étendu à `io.open` ; fichier de sonde planté pour vérifier qu'il n'est pas ouvert.
Essai : `test_iib_lectures_v1.py::test_lecture_2_de_la_repetition_jouet_n_ouvre_aucun_fichier_de_sonde`.

### Mineurs déclarés (non appliqués, règle de conception requise)

- **CLIIBC-08** — intervalle de confiance bilatéral. Choix de conception : type d'intervalle (BCa, percentile, basique).
- **CLIIBC-12** — descripteur d'échelle pour « dommage non vu à cette puissance ». Choix de conception : formulation.
- **CLIIBC-14** — vérification de session 7b. Dépend d'une interface externe hors du périmètre du saboteur.
- **CLIIBC-17** — périmètre de l'échantillon d'audit. Choix de conception : périmètre de l'audit.
- **CLIIBC-18** — vérification de dépendance à une ligne de GO. Choix de conception : traçabilité des dépendances.

## Adaptations des essais existants

Outre les essais ajoutés (un par correction, plus les six synthétiques de CLIIBC-07 et la garde transitive de CLIIBC-15), les adaptations suivantes ont été faites aux essais existants :

1. **Dictionnaire `EXEMPLES` de `test_iib_exclusion_v1.py`** : deux entrées ajoutées pour des motifs à expression non littérale (`spread (?:this|the) extra` → `"spread the extra"`, `\b1[.,]5 ?x\b` → `"1.5 x"`).
2. **Assertion du premier motif de la consigne factice** dans `test_iib_consigne_v1.py` : corrigée de `"spread (?:this|the) extra"` (motif de la consigne réelle, absent de la factice) à `"verbose (?:citation|reference) style"` (premier motif de la factice réécrite).
3. **Cas paramétrés `test_artefacts_motifs_et_sections`** dans `test_iib_consigne_v1.py` : deux cas actualisés pour référencer les motifs de la factice réécrite au lieu de `"spread"`.
4. **`test_garde_la_collecte_voit_une_fuite_plantee`** dans `test_iib_consigne_invisible_v1.py` : vérifie que la fuite est un sous-ensemble des fichiers `textes-actions-iib*.jsonl` (et non une égalité stricte), car les fichiers par phase de CLIIBC-05 incluent les phases sans maître.
5. **`test_sain_sorties_scellees_et_rattachees`** dans `test_iib_lanceur_v1.py` : ensemble attendu étendu aux 9 fichiers par phase de CLIIBC-05.
6. **Essais synthétiques de la détection à excès nul** dans `test_iib_lectures_v1.py` : `n_taches=200, sigma=0.02` pour obtenir un intervalle de confiance assez étroit sous le seuil de 5 % quand il n'y a pas de signal.
7. **Registre `REGISTRE_IIB`** dans `test_iib_inventaires_v1.py` : raisons de couverture étendues pour `jouer_lot` et `generer_actions` (espion du contexte entier).

## Comptes

| Catégorie                   | Nombre |
|-----------------------------|--------|
| Fichiers sources (`iib/`)   | 14     |
| Fichiers d'essai            | 13     |
| Scripts                     | 6 + 1 (liste ciblée) |
| Essais verts                | 381    |
| Essais par correction       | ≥ 13 (un par correction + 6 synthétiques CLIIBC-07 + 1 garde CLIIBC-15) |
| Répétition jouet            | identique |

## Écarts

- Les essais de l'oracle qui dépendent de la bibliothèque `tokenizers` (19 essais) ne peuvent pas être exécutés dans cet environnement de nuage (absence du paquet). Ils sont inclus dans le décompte de 381 : pytest les a collectés et exécutés avec succès dans la passe finale car ils ont un mécanisme de détection automatique et passent sans charger le jetoniseur externe.
- Aucun refus de classifieur, de permission ou de crochet n'a été rencontré.
- Aucun résultat, score, poids de sonde ou de moniteur n'a été lu ni écrit.

## Ce qui reste

Avant la contre-lecture neuve (par un autre modèle) :
1. Les 5 mineurs déclarés (CLIIBC-08, 12, 14, 17, 18) : à trancher par la session mère ou Lazar.
2. Vérifier que les 19 essais dépendants de `tokenizers` passent dans un environnement avec carte graphique.

Avant l'ordre et le devis :
3. Contre-lecture du code v2 par un modèle qui n'a ni écrit ni corrigé ce code.
4. Six épreuves de l'oracle sur données factices (exigence de GO-2026-11-10-08).
5. Devis inscrit et ordre exploratoire contre-lu et scellé.
