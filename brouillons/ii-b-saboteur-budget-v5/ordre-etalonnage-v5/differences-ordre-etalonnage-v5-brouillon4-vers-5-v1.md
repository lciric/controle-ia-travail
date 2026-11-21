# Différences — ordre de l'étalonnage de l'organisme retenu, du brouillon 4 au brouillon 5 — v1

Source : `ordre-etalonnage-ii-b-v5-brouillon4.md` (`12fb6dac586ebd6410b69e7af600beb4b6e429c0cc829f2d37fce5dbfa8b7e32`). Produit : `ordre-etalonnage-ii-b-v5-brouillon5.md` (`3bde656a8b75d5ee984ff6011bfb35e0ea8192b43c24f5d91d506e5b1824973e`). Écrite par le programme `fabriquer-ordre-etalonnage-ii-b-v5-brouillon5-v1.py`, le 2026-11-21 vers 19:56 UTC. Cause : `brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/note-verification-ordre-etalonnage-v5-brouillon4-cl1-v1.md` (`958b5f94350f46011e523d255b34bd9a5979d11e6add72a7c27caf017eaf15e4`), corrections F1 et F2, mineur m1. Une différence par ligne ; tout le reste est recopié à l'octet ; les neuf champs sont inchangés.

## Remplacements, un par ligne (ancre trouvée le nombre de fois attendu)

- titre (1 fois) : « machine à part — brouillon 4 » remplacé par « machine à part — brouillon 5 ».
- statut (1 fois) : « - **Statut** : **brouillon 4**, pièce décisive (ordre d'une course payante), non contre-lu. Fabriqué par progr… » remplacé par « - **Statut** : **brouillon 5**, pièce décisive (ordre d'une course payante). Fabriqué par programme (`fabriquer-ordre-etalonnage-ii-b-v5-brouillon5-v1.py`) depuis le brouillon 4 (`ordre-etalonnage-ii-b-v5-brouillon4.md`, `12fb6dac586ebd6410b69e7af600beb4b6e429… ».
- m1, § 3, marques de progrès (1 fois) : « - **Marques de progrès** (M2) : une ligne par lot, par passe d'oracle et pour les épreuves, lue par la surveil… » remplacé par « - **Marques de progrès** (M2), lues par la surveillance : le chargement, le début, chaque lot, les oracles écrits, la fin, et l'arrêt s'il y en a un ; les épreuves ne se jouent pas sur la machine : elles se jouent au passage des conditions, sur processeur (§ 5… ».
- F1, § 7, phrase des noms (1 fois) : « après chaque lot de huit épisodes, les sorties d'oracle sous `diag/<run>/lots/` et les identifiants des action… » remplacé par « après chaque lot de huit épisodes, les sorties d'oracle sous `diag/<run>/lots/lot-*.json` et les identifiants des actions sous `donnees/<run>/lots/ids-lot-*.json`, scellés et poussés ; aucun fichier d'ensemble des identifiants n'est écrit ; ».
- F1, § 7, ligne des lots et de l'ensemble (1 fois) : « | par lot, puis fin de l'étalonnage | `etalonnage-oracles-iib-v5.json`, `ids-actions-etalonnage-iib-v5.json` |… » remplacé par « | après chaque lot | `diag/<run>/lots/lot-*.json` ; `donnees/<run>/lots/ids-lot-*.json` | sorties des deux oracles pour le lot, sans aucun texte ; identifiants des actions du lot | | fin de l'étalonnage | `diag/<run>/etalonnage-oracles-iib-v5.json` | sorties d… ».
- F1, § 7, ligne des rapportés (1 fois) : « | fin de l'étalonnage | `rapportes-etalonnage-iib-v5.json` | rapportés sans règle (texte scellé, section 13), … » remplacé par « | fin de l'étalonnage | `diag/<run>/rapportes-etalonnage-iib-v5.json` | rapportés sans règle (texte scellé, section 13), contrôle du premier coût et durées mesurées par oracle compris | ».
- F1, § 7, ligne de l'arrêt (1 fois) : « | tout arrêt | ce qui existe, avec le motif | versé avant tout le reste | » remplacé par « | toute garde, toute erreur, tout signal d'arrêt | `diag/<run>/arret.json`, et les lots déjà écrits | étape, motif, liste de ce qui est écrit ; versé avant tout le reste ; ni fichier d'ensemble ni issue | ».
- F2, § 11, correctif de rang 9 (1 fois) : « | `correctifs/0001-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 9) | » remplacé par « | `distillateur-v5/correctifs/0001-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 9) | ».
- F2, § 11, correctif de rang 10 (1 fois) : « | `correctifs/0002-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 10) | » remplacé par « | `distillateur-v5/correctifs/0002-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 10) | ».
- F2, § 11, correctif de rang 11 (1 fois) : « | `correctifs/0003-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 11) | » remplacé par « | `distillateur-v5/correctifs/0003-Organisme-retenu-du-saboteur-budget-distillateur-en-.patch` (rang 11) | ».
- F2, § 11, phrase des chemins (1 fois) : « les lignes 7 à 13 sont sous `brouillons/ii-b-saboteur-budget-v5/code-v5/` ; » remplacé par « les six premières lignes sont sous `brouillons/ii-b-saboteur-budget-v5/code-v5/correctifs/` ; les lignes 7 à 13 sont écrites depuis `brouillons/ii-b-saboteur-budget-v5/code-v5/`, celles des rangs 9 à 11 sous `brouillons/ii-b-saboteur-budget-v5/code-v5/distilla… ».

## Champs gardés, un par ligne

- `<<BRANCHE_CODE_V5>>`.
- `<<COMMIT_CODE_REVU_POUSSE>>`.
- `<<COMMIT_LANCEMENT_ETALONNAGE>>`.
- `<<CONFIG_ETALONNAGE_CHEMIN_ET_EMPREINTE>>`.
- `<<ETIQUETTE_ETALONNAGE>>`.
- `<<FICHIER_ENTREES_CHEMIN_ET_EMPREINTE>>`.
- `<<INSTANCES_INTOUCHABLES>>`.
- `<<MOT_LAZAR_PREMIERE_ACTION_DANS_LA_PERTE>>`.
- `<<SORT_DE_LA_MACHINE_APRES_ETALONNAGE>>`.
