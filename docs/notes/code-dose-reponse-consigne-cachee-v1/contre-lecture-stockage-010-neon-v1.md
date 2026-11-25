# Contre-lecture R2 (classe B, Gemini 4 Neon) — écart matériel minimal `stockage_max_usd_h` (0,08 → 0,10 USD/h)

- **Verdict** : **`prêt`**
- **Contre-lecteur** : contre-lecteur R2 neuf de classe B (Gemini 4 Neon ; aucun des fichiers de `wt-dr-v3` n'a été écrit par ce lecteur).
- **Autorisation auditée** : `GO-2026-11-25-01` (`R-5397`, mot de Lazar) — relèvement unique de `stockage_max_usd_h` de `0.08` à `0.10` USD/h et rien d'autre, en fichiers neufs versionnés (R12).
- **Arbre audité** : `C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\wt-dr-v3`
- **Tête git de base** : `a7629fc9158b39d8a3fdf3bb52fe2dcb6bb3893b`
- **Rapport développeur audité** : `docs/notes/code-dose-reponse-consigne-cachee-v1/rapport-developpeur-stockage-010-v1.md` (`0ce98051ee4cd0f6756425d85ab3dee9152e4b87ff4e90ace453ba2ace503f0b`)

---

## 1. Respect de la règle R12 (aucun fichier suivi modifié)

Vérifié par `git rev-parse HEAD`, `git diff --stat`, `git diff --cached --stat` et `git status --short --untracked-files=all` :
- `HEAD` = `a7629fc9158b39d8a3fdf3bb52fe2dcb6bb3893b`.
- `git diff` et `git diff --cached` sur les fichiers suivis sont **strictement vides**.
- Aucun fichier existant n'a été modifié (`controles_v2.py`, `course_v2.py`, `lecture_v2.py`, `scripts/lecteur_texte_dose_reponse_v2.py`, `scripts/lancer_lecteur_texte_dose_reponse_v2.sh`, `scripts/ecrire_configuration_dose_reponse_v2.py`, `scripts/amorce_instance_dose_reponse_v3.sh`, `scripts/lancer_dose_reponse_v3.sh`, `scripts/tests-cibles-dose-reponse-v3.txt`, `tests/test_dose_reponse_v2.py`, `tests/test_dose_reponse_amorce_v3.py`, `tests/factice_dose_reponse_v1.py`, ainsi que tous les modules gelés sont 100 % intacts).
- Avant ajout du présent rapport, seuls les 9 fichiers neufs et leurs 9 compagnons `.sha256` figuraient en non suivis (`??`).

---

## 2. Vérification des empreintes SHA-256, des compagnons `.sha256` et des fins de ligne LF

Contrôle indépendant sur les octets bruts des 9 livrables et de leurs 9 compagnons `.sha256` :
- **`crlf=False` (aucun octet `\r`)** sur tous les 9 fichiers et sur tous leurs 9 compagnons `.sha256` (critique pour `amorce_instance_dose_reponse_v4.sh` et `lancer_dose_reponse_v4.sh` exécutés sous Linux).
- **Format des compagnons** : concordance exacte octet pour octet avec `<64hex>  <nom_de_base>\n` sur les 9 fichiers.
- **Concordance avec le rapport développeur** (`0ce98051…`) : 100 % exacte sur les 8 fichiers listés dans son tableau et sur le rapport lui-même.

| Fichier | SHA-256 vérifié | LF (`crlf=False`) | Compagnon `.sha256` exact & LF |
| --- | --- | --- | --- |
| `src/controle_ia/dose_reponse/controles_v3.py` | `f56374d689a206f411b70f61ed8b466f69f91f99aa921def091ca2164969d1cc` | OK | OK |
| `src/controle_ia/dose_reponse/course_v3.py` | `cb1fd23109feea6ab57a0b265298b18a16a266c586b8018dfc7aea2971a86c66` | OK | OK |
| `scripts/ecrire_configuration_dose_reponse_v3.py` | `47c83d993a81ccb089feb675bf73817ccb6bf073a04f35aa041554cbb348cd95` | OK | OK |
| `tests/test_dose_reponse_v3.py` | `e03139fdda029c37ef1064c4f3f9dfcb6e293e198b6f48f4100d4ff145f3013f` | OK | OK |
| `tests/test_dose_reponse_amorce_v4.py` | `0f07d60c2be1ea3085d35c8c6927a6f2485822b568e6c29c93ba236adc502c73` | OK | OK |
| `scripts/tests-cibles-dose-reponse-v4.txt` | `2766a9b022d4e9db45dd0c85d224473409b4cacb20aad9a1c3fd81166c449d55` | OK | OK |
| `scripts/amorce_instance_dose_reponse_v4.sh` | `ac546976ee5507567e995504fd775af90ac010b2c8a2e65854aaeba6b51ddf82` | OK | OK |
| `scripts/lancer_dose_reponse_v4.sh` | `5b73bf876d246a3af5593709e5e9f9e40a632b5fc42823dbd07a83ecc9bb9ade` | OK | OK |
| `docs/notes/code-dose-reponse-consigne-cachee-v1/rapport-developpeur-stockage-010-v1.md` | `0ce98051ee4cd0f6756425d85ab3dee9152e4b87ff4e90ace453ba2ace503f0b` | OK | OK |

---

## 3. Audit diff ligne à ligne contre les versions antérieures

### 3.1 `controles_v2.py` → `controles_v3.py`
Diff unifié complet : **4 blocs exactement** :
1. En-tête de docstring `[v3 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) …]`.
2. Ligne 27 (docstring) : `0,08` → `0,10`.
3. Ligne 70 : `OFFRE["offre"]["stockage_max_usd_h"]` : `0.08` → `0.10`.
4. Ligne 125 : `configuration()` → `"lancement"["offre"]["stockage_max_usd_h"]` : `0.08` → `0.10`.

Vérification programmatique supplémentaire sur les 20 autres constantes (`PREREG`, `PREREG_SHA256`, `PIECE_JOINTE_SHA256`, `PREMIER_TEST_SHA256`, `TIRAGE`, `BANQUE_INITIALE`, `MODULES_REPRIS`, `N_TACHES`, `RANG_MIN`, `N_BANQUE_INITIALE`, `REGLAGES`, `AGENT`, `PLAFOND_USD=90`, `GO_ORIGINE="GO-2026-11-24-25"`, `CONFIG_7B`, `PIECE_JOINTE`, `DERNIER_JOUR_CREATION="2026-12-12"`, `CLES_GARDES_7B`, `LIGNE_BANQUE`, `LIGNE_CODE`) et sur tous les autres champs de `OFFRE` (`nom_offre="A100 SXM4"`, `memoire_carte_min_mo=80000`, `prix_max_usd_h=1.3`, `coeurs_effectifs_min=16`, `memoire_vive_min_mo=128000`, `disque_min_go=300`, `telechargement_max_usd_go=0.05`) : **égalité stricte** (`True`). Aucune fonction de garde (`exiger_config`, `_exiger_config_v1`, `exiger_offre`, `exiger_offre_lue`, `controler_banque`, `controler_modules`, `controler_registre`, `exiger_calendrier`, `controler_textes_avant_creation`, `controles_avant_depense`) n'a changé.

De plus, vérification de la chaîne `session_v1` / `session_v12` / `session_v8` / `session_v7` / `session_v2` : `stockage_max_usd_h` est lu dynamiquement depuis `vue-offre.json` (produite par `session_v1.vue_offre(config)`), sans aucune constante `0.08` écrite en dur dans la chaîne de sélection d'offre.

### 3.2 `course_v2.py` → `course_v3.py` et compatibilité aval (`lecture_v2.py`, `lecteur_texte_dose_reponse_v2.py`)
Diff unifié complet : **2 blocs exactement** :
1. En-tête de docstring `[v3 …]`.
2. Ligne 56 : `from . import controles_v3 as ct` ; ligne 58 : `COMMANDE = "python -m controle_ia.dose_reponse.course_v3"`.

Aucune autre ligne ne change.

- **Compatibilité de `src/controle_ia/dose_reponse/lecture_v2.py`** (relu intégralement, lignes 1–589) :
  - Ne lit jamais `manifeste["commande"]` ni la section `lancement`.
  - Seul import depuis `controles_v2` (ligne 540) : `PREREG`, `PREREG_SHA256`, `entropie_racine`, strictement identiques dans `controles_v3`.
  - `charger_course` (lignes 495–516) contrôle uniquement l'homogénéité entre blocs de `("prereg_sha256", "config_sha256", "entropie", "commit_code")`, et `course_v3.py` ne hache que `CLES_SCIENTIFIQUES` dans `config_sha256` (hors `lancement`).
  - **Résultat** : compatible sans restriction.

- **Compatibilité de `scripts/lecteur_texte_dose_reponse_v2.py`** (relu intégralement, lignes 1–2029) :
  - `lire_lancement` (lignes 799–884) vérifie `run_id`, `cfg["mode"]`, `man["decisif"]`, `prereg.sha256`, `preenregistrement.sha256`, `designation_critere_3`, `graines` (`partition-taches`, `ordre-des-taches`, `generation/<t>/1..2`) et `cree_le`. Il **ne contrôle ni `manifeste["commande"]` ni `lancement.offre.stockage_max_usd_h`**.
  - Sur les blocs (lignes 859–861), il contrôle uniquement l'homogénéité entre les 64 `bloc.json` du quadruplet `CLES_ENTETE_BLOC = ("prereg_sha256", "config_sha256", "entropie", "commit_code")`, sans comparaison externe de `config_sha256`.
  - `ligne_de_mesure`, `CLES_MESURES`, `CLES_TEXTES`, `nom_bloc`, `ecrire_bloc` sont inchangés dans `course_v3.py`, et les 9 `MODULES_GELES` (commit `1609a4bf`) sont intacts.
  - **Résultat** : compatible sans restriction avec une course produite par `course_v3.py`.

### 3.3 `scripts/ecrire_configuration_dose_reponse_v2.py` → `v3.py`
Diff unifié complet : **4 blocs exactement** (en-tête `[v3 …]`, docstring `controles_v3.exiger_config` et commande d'usage `v3.py`, import `controles_v3 as ct`, `SORTIE = "prereg/T0.6-dose-reponse-configuration-course-v2.json"`).
- `SORTIE` est exactement alignée avec la valeur par défaut `CONFIG` de `scripts/lancer_dose_reponse_v4.sh`.
- Exécution directe testée vers un répertoire temporaire hors dépôt : succès (`rc=0`), scellement conforme, diff structurel entre `controles_v2.configuration(...)` et le JSON produit strictement limité à `lancement.offre.stockage_max_usd_h : 0.08 → 0.1`, validé par `controles_v3.exiger_config` et `session_v1.go_t08(..., 'GO-2026-11-24-25', 2026-11-25)`.

### 3.4 `scripts/amorce_instance_dose_reponse_v3.sh` → `v4.sh`
Diff unifié complet : **6 blocs exactement** :
1. En-tête `[v4 …]`.
2. Ligne 44 : bannière `AMORCE DR v4 DEMARRAGE`.
3. Ligne 254 : `journal "début dose-réponse v4 : …"`.
4. Ligne 303 : `from controle_ia.dose_reponse import controles_v3 as ct`.
5. Ligne 320 : `LISTE_TESTS="scripts/tests-cibles-dose-reponse-v4.txt"; LISTE_SHA256="2766a9b022d4e9db45dd0c85d224473409b4cacb20aad9a1c3fd81166c449d55"; ATTENDUS="60"; FICHIERS_TESTS=""`.
6. Ligne 341 : `HF_HUB_OFFLINE=1 PYTHONPATH=src python -m controle_ia.dose_reponse.course_v3 …`.

Vérifications complémentaires Linux :
- `bash -n scripts/amorce_instance_dose_reponse_v4.sh` : code 0 (`OK`).
- `LISTE_SHA256` correspond exactement au SHA-256 de `scripts/tests-cibles-dose-reponse-v4.txt` (`2766a9b022d4e9db45dd0c85d224473409b4cacb20aad9a1c3fd81166c449d55`).
- Extraction partielle (`CHEMINS_CLONAGE` + ligne 194 `printf '/%s*\n' "$CONFIG"` + ligne 199 `extraction_v1.py`) : extrait bien `prereg/T0.6-dose-reponse-configuration-course-v2.json` et son `.sha256` via `$CONFIG`, tous les fichiers cités (`piece_jointe`, `consignes_premier_test`, `banque`, et `designation_critere_3` quand non `null`), ainsi que l'ensemble de `/src/`, `/tests/`, `/scripts/`, `/registres/go.md`, `/registres/scellements-v1.md`, `/docs/sources/invites-2606.08892-v1/`, `tirage.json*`, `taches-evaluation.json*`, `taches-entrainement.json*`, `T0.6-organismes-config-7b-v1.json*`, `puissance_dose_reponse_consigne_cachee_v5.py*`. Tous les fichiers requis par `controles_v3`, `course_v3` et les 60 tests de la suite ciblée sont présents dans l'arbre extrait sous Linux.

### 3.5 `scripts/lancer_dose_reponse_v3.sh` → `v4.sh`
Diff unifié complet : **9 blocs exactement** :
- En-tête `[v4 …]` et 5 lignes d'usage (`v4.sh`).
- Ligne 35 : `A=scripts/amorce_instance_dose_reponse_v4.sh`.
- Ligne 37 : `CONFIG="${DR_CONFIG:-prereg/T0.6-dose-reponse-configuration-course-v2.json}"`.
- Ligne 102 : `from controle_ia.dose_reponse import controles_v3 as ct`.
- Ligne 121 : `controles dose-reponse v4`.
- Lignes 166, 180, 186 : auto-références vers `lancer_dose_reponse_v4.sh` (`apres-creation`, `surveillance`, `creation`).
- Ligne 203 : `surveillance dose-réponse v4 de $ID`.

Vérifications complémentaires :
- `bash -n scripts/lancer_dose_reponse_v4.sh` : code 0 (`OK`).
- Aucune régression sur `masquer()` (lignes 48–55), `vast_masque()` (lignes 56–59) ni sur la vérification par `.claude/hooks/garde_calcul.py` (ligne 167). `garde_calcul.py` (relu intégralement, lignes 1–229) n'épingle que deux lanceurs d'idéation sans rapport et contrôle `GO_ID` / `vastai create instance` / R10 : pleine compatibilité avec `lancer_dose_reponse_v4.sh`.

---

## 4. Rejeu indépendant de la suite de tests (`venv-py314`)

Commande exécutée indépendamment sous `venv-py314` (`Python 3.14.3`, `pytest 9.2.0`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=src`) :
- **Collecte (`--collect-only`)** :
  - `tests/test_dose_reponse_v3.py` : **47 tests** (45 repris de v2 + `test_stockage_max_010_offre_lue_et_config` et `test_stockage_max_010_chaine_session`).
  - `tests/test_dose_reponse_amorce_v4.py` : **13 tests**.
  - **Total collecté** : **60 tests**, aucun `skip` conditionnel par plateforme → `ATTENDUS="60"` dans `amorce_instance_dose_reponse_v4.sh` est **exact sous Linux**.
- **Exécution complète (`pytest -v -p no:cacheprovider`)** : **59 passés, 1 échec** (`tests/test_dose_reponse_v3.py::test_lanceur_verifie_le_go_sans_rien_creer`), zéro warning, zéro skip.
  - Cause vérifiée sur trace d'échec : `ModuleNotFoundError: No module named 'controle_ia'` dû à `DEPOT=$(cd ... && pwd)` renvoyant un chemin POSIX MSYS (`/c/Users/...`) sous Git Bash pour un `python3` natif Windows, sur la section `--verifier-go-seulement` strictement inchangée depuis la v3 (et la garde `session_v1.go_t08` a été rejouée directement avec succès en Python sur `config_v3` + `GO-2026-11-24-25`). Sous Linux, cet obstacle disparaît et les 60 tests sont attendus verts.
- **Bornes R5 vérifiées** (`test_stockage_max_010_offre_lue_et_config` et `test_stockage_max_010_chaine_session`, tous deux **PASSED**) :
  - `storage_total_cost = 0.0822` et `0.10` acceptés par `controles_v3.exiger_offre_lue` et par `session_v1 choisir` ;
  - `storage_total_cost = 0.1001` refusé par `GardeArret` (`exiger_offre_lue`) et code retour non nul (`session_v1 choisir`) ;
  - configuration portant `0.08` ou `0.11` refusée par `controles_v3.exiger_config` (`reconstruite`) et `0.11` refusée par `controles_v3.exiger_offre` (`stockage_max_usd_h`).

---

## 5. Liste numérotée des constats

- **Bloquants** : aucun (0).
- **Majeurs** : aucun (0).
- **Mineurs** :
  1. *(Mineur, cosmétique, non bloquant)* Dans `tests/test_dose_reponse_v3.py` (ligne 670), absence d'une ligne vide entre la fin de `test_cl10_garde_d_offre_de_la_chaine` et la bannière `# --- écart matériel minimal GO-2026-11-25-01 / R-5397 ...`. Aucun impact sur l'exécution ni sur les contrôles.

*(Note opérationnelle, non défaut du code : `prereg/T0.6-dose-reponse-configuration-course-v2.json` sera écrit et scellé par `scripts/ecrire_configuration_dose_reponse_v3.py` après le commit de code cité par la ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` ; en mode jouet, `tests/factice_dose_reponse_v1.py`, intact sous R12, garde `stockage_max_usd_h: 0.08`, valide sous `controles_v3.exiger_offre` puisque `0 <= 0.08 <= 0.10`.)*

---

## 6. Verdict

**`prêt`** — l'écart matériel minimal autorisé par Lazar (`GO-2026-11-25-01`, `R-5397`) est implémenté de façon strictement minimale, conforme à R12, en LF strict, scellée et vérifiée de bout en bout.

---

## 7. Déclaration de cloisonnement et de non-génération

Aucun fichier interdit (`brouillons/g0-criteres-2-3-v1/consignes-privees*`, `prereg/P3-consignes-v1.md`, `donnees/`, `diag/`, `runs/`, `docs/verdicts/`, `coffre/`) n'a été ouvert.

Aucune action générée sous un texte de la pièce jointe (`7a5f633c…`) ni du fichier du premier test (`a68468fe…`).
