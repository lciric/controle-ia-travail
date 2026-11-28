# Rapport développeur — écart matériel minimal `stockage_max_usd_h` (0,08 → 0,10 USD/h)

- **Autorisation** : `GO-2026-11-25-01` (`R-5397`, mot de Lazar).
- **Branche et tête de base** : `code/dose-reponse-consigne-cachee-v1`, tête `a7629fc9158b39d8a3fdf3bb52fe2dcb6bb3893b` (descendant de `6b2b821a28f8bebebae2188d9f020ce731464306`).
- **Portée fonctionnelle unique** : relèvement de `stockage_max_usd_h` de `0.08` à `0.10` USD/h dans `OFFRE["offre"]` et `configuration()` de `controles_v3.py`, et propagation de versionnage R12 sur la chaîne de course (`course_v3.py`, `ecrire_configuration_dose_reponse_v3.py`, `amorce_instance_dose_reponse_v4.sh`, `lancer_dose_reponse_v4.sh`, suite ciblée v4). Aucun autre paramètre scientifique, budgétaire ou d'offre n'est modifié.

## Fichiers neufs et empreintes SHA-256 (tous en fins de ligne LF, accompagnés de leur `.sha256`)

| Chemin | SHA-256 |
| --- | --- |
| `src/controle_ia/dose_reponse/controles_v3.py` | `f56374d689a206f411b70f61ed8b466f69f91f99aa921def091ca2164969d1cc` |
| `src/controle_ia/dose_reponse/course_v3.py` | `cb1fd23109feea6ab57a0b265298b18a16a266c586b8018dfc7aea2971a86c66` |
| `scripts/ecrire_configuration_dose_reponse_v3.py` | `47c83d993a81ccb089feb675bf73817ccb6bf073a04f35aa041554cbb348cd95` |
| `tests/test_dose_reponse_v3.py` | `e03139fdda029c37ef1064c4f3f9dfcb6e293e198b6f48f4100d4ff145f3013f` |
| `tests/test_dose_reponse_amorce_v4.py` | `0f07d60c2be1ea3085d35c8c6927a6f2485822b568e6c29c93ba236adc502c73` |
| `scripts/tests-cibles-dose-reponse-v4.txt` | `2766a9b022d4e9db45dd0c85d224473409b4cacb20aad9a1c3fd81166c449d55` |
| `scripts/amorce_instance_dose_reponse_v4.sh` | `ac546976ee5507567e995504fd775af90ac010b2c8a2e65854aaeba6b51ddf82` |
| `scripts/lancer_dose_reponse_v4.sh` | `5b73bf876d246a3af5593709e5e9f9e40a632b5fc42823dbd07a83ecc9bb9ade` |

*(Ce rapport `docs/notes/code-dose-reponse-consigne-cachee-v1/rapport-developpeur-stockage-010-v1.md` est lui-même accompagné de son compagnon `.sha256` en LF.)*

### Alignement R12 de la configuration par défaut

`scripts/ecrire_configuration_dose_reponse_v3.py` écrit par défaut `prereg/T0.6-dose-reponse-configuration-course-v2.json` (respect R12 vis-à-vis de `v1.json`). En conséquence, `scripts/lancer_dose_reponse_v4.sh` aligne sa valeur par défaut : `CONFIG="${DR_CONFIG:-prereg/T0.6-dose-reponse-configuration-course-v2.json}"`.

## Vérification de `src/controle_ia/dose_reponse/lecture_v2.py`

`lecture_v2.py` a été relu en entier (lignes 1 à 589) :
- Aucun couplage à `stockage_max_usd_h`, à `course_v2`, à `COMMANDE`, à `controles_v2.exiger_config` ni à `controles_v2.exiger_offre`.
- Seul import depuis `controles_v2` (ligne 540) : `from .controles_v2 import PREREG, PREREG_SHA256, entropie_racine` — trois constantes/fonctions strictement identiques entre `controles_v2.py` et `controles_v3.py`.
- `charger_course` (lignes 495–516) ne vérifie que l'homogénéité des en-têtes `("prereg_sha256", "config_sha256", "entropie", "commit_code")` entre les blocs d'une même course (et `config_sha256` dans `course_v3.py` ne hache que `CLES_SCIENTIFIQUES`, sans la section `lancement`).
- **Conclusion** : `lecture_v2.py` lit sans restriction une course exécutée par `course_v3.py` ; `lecture_v3.py` n'est pas nécessaire et `lecture_v2.py` reste intact.

## Bilan des essais et vérifications

- **Environnement** : `venv-py314` (`Python 3.14.3`, `pytest 9.2.0`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=src`).
- **Collecte de la suite ciblée** (`scripts/tests-cibles-dose-reponse-v4.txt`, SHA-256 `2766a9b022d4e9db45dd0c85d224473409b4cacb20aad9a1c3fd81166c449d55`) :
  - `tests/test_dose_reponse_v3.py` : **47 tests collectés** (45 repris de v2 + 2 essais R5 dédiés aux bornes `stockage_max_usd_h = 0.10` : `test_stockage_max_010_offre_lue_et_config` couvrant `0.0822` et `0.10` acceptés, `0.1001` refusé par `GardeArret`, configuration à `0.08` ou `0.11` refusée par `exiger_config` et `0.11` refusée par `exiger_offre` ; et `test_stockage_max_010_chaine_session` vérifiant `session_v1 choisir` sur `0.0822`, `0.10` et `0.1001`).
  - `tests/test_dose_reponse_amorce_v4.py` : **13 tests collectés**.
  - **Total collecté** : **60 tests** → `ATTENDUS="60"` fixé dans `scripts/amorce_instance_dose_reponse_v4.sh`.
- **Exécution pytest sous Windows** : **59 passés, 1 échec** (`tests/test_dose_reponse_v3.py::test_lanceur_verifie_le_go_sans_rien_creer`), uniquement dû à deux particularités Windows/Git Bash sur un code inchangé :
  1. Sans `DR_DEPOT`, `$(pwd)` sous Git Bash renvoie un chemin POSIX MSYS (`/c/Users/...`) que `python3` natif Windows ne résout pas dans `sys.path.insert(0, '$DEPOT/src')` (`ModuleNotFoundError: No module named 'controle_ia'`).
  2. Avec `DR_DEPOT` posé au chemin Windows, `lancer_dose_reponse_v4.sh` appelle `python3 -I -B -c "$SESSION8" go ...`, et `-I` ignore `PYTHONUTF8`/`PYTHONIOENCODING` sous Windows (retour à `cp1252`), ce qui échoue à encoder le caractère `'→'` (`\u2192`) imprimé par le module inchangé `src/controle_ia/lancement_t08/session_v1.py` (ligne 182).
  3. Sous Linux (instance de calcul, locale UTF-8 et chemins POSIX natifs), ces deux obstacles n'existent pas ; les **60 tests** de la suite ciblée sont attendus verts (`ATTENDUS="60"`).
- **Contrôles complémentaires** :
  - `bash -n scripts/amorce_instance_dose_reponse_v4.sh` et `bash -n scripts/lancer_dose_reponse_v4.sh` : code 0.
  - Exécution directe de `scripts/ecrire_configuration_dose_reponse_v3.py` (vers un répertoire temporaire hors dépôt) + `controles_v3.exiger_config` + `session_v1.go_t08(..., 'GO-2026-11-24-25', 2026-11-25)` : succès (`stockage_max_usd_h = 0.10`, `plafond_usd = 90`).
  - **R12 (`git diff`)** : `git diff` sur tous les fichiers suivis est **strictement vide** ; aucun fichier existant modifié (`controles_v2.py`, `course_v2.py`, `lecture_v2.py`, `amorce_instance_dose_reponse_v3.sh`, `lancer_dose_reponse_v3.sh`, `lecteur_texte_dose_reponse_v2.py`, `lancer_lecteur_texte_dose_reponse_v2.sh` 100 % intacts).
  - **Fins de ligne et sceaux** : `crlf=False` (LF strict) et concordance exacte `<64hex>  <nom_de_base>\n` vérifiés sur l'ensemble des 9 livrables et leurs 9 compagnons `.sha256`.

## Déclaration de cloisonnement et de non-génération

Aucun fichier interdit (`brouillons/g0-criteres-2-3-v1/consignes-privees*`, `prereg/P3-consignes-v1.md`, `donnees/`, `diag/`, `runs/`, `docs/verdicts/`, `coffre/`) n'a été ouvert.

Aucune action générée sous un texte de la pièce jointe (`7a5f633c…`) ni du fichier du premier test (`a68468fe…`) : modèle jouet et textes factices seulement.
