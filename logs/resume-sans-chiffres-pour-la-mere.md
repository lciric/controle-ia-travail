# Résumé sans chiffres pour la session mère — Lecture scellée T0.8 v3 (`R-5218`)

**Garantie de cloisonnement** : ce fichier ne contient **aucun** chiffre de résultat, aucune aire sous la courbe, aucune p-valeur, aucun score, aucun taux d'anomalie, aucun signe d'effet ni aucun libellé d'issue. Le lecteur lui-même n'a ouvert ni `lecture-t08.json` ni `tables-d-f-t08.json`.

- **Horodatage UTC** : `2026-11-24T04:59:28Z`
- **Identifiant du run de lecture** : `20261124-045444-t08-lecture`
- **Statut mécanique** : **RÉUSSI** (toutes les étapes `(a)` à `(i)` exécutées sans arrêt de garde ni contournement).
- **Codes de retour mécaniques** :
  - `scripts/ecrire_configuration_lecture_t08_v1.py` : `0`
  - `python3 -B -m controle_ia.t08.lire_v1` : `0`
- **Audit R4** : **non déclenché** (`echantillon: null`, `echantillon_sha256: null`).

## État des préalables et contrôles d'intégrité

- **P1 (`SCELLEMENT-T08-V3` et texte scellé `prereg/T0.8-bases-boite-noire-v0-v3.md`)** : **RÉUSSI** (`72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918`).
- **P2 (ligne `COURSE-T08` sur `origin/main` `67945a4d` et intégrité des 8 fichiers de `origin/calcul/t08-course-v3` `50a6d30ce` / `b56084145`)** : **RÉUSSI** (aucun fichier > 90 Mo ; `GO-2026-11-22-134` non requis ; antériorité tenue).
- **P3 (`LECTURE-T08-BASE-A` et entrées 7b par liste blanche)** : **RÉUSSI** (empreintes vérifiées par `ListeBlanche` et contrôle d'identité M2 passé à l'étape `(b)`).
- **P4 (`CODE-T08-V3` = `6735dd2e1b30c2615802b78c290e24a80863b18d`)** : **RÉUSSI** (`exiger_code_au_commit` et `exiger_code_importe_sous` passés).
- **P5 (absence de fichiers interdits)** : **RÉUSSI** (aucun `lecture-sondes-t06*`, aucun `resume.json` de 7b, aucun fichier `coffre/*` / `ii-b*` extrait ni ouvert).
- **P6 (`SORTIES-HD-VADAPT`)** : **ABSENTE** (`--hd` non passé ; étape `(h bis)` terminée).
- **Étapes de `lecture_v1.py`** : `(a)`, `(b)`, `(c)`, `(d)`, `(e)`, `(f)`, `(g)`, `tables-d-f-ecrites`, `(h)`, `(h bis)`, `(i)` — toutes **RÉUSSIES**.

## Fichiers produits et empreintes `SHA-256` (vérifiés par `sha256sum -c`)

Dossier : `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lecture-t08-v3-habilitee/`

- `prereg/T0.8-configuration-lecture-v3.json` (+ `.sha256`) : `e15f04b445a010bb5163599519dc891acc6ef321bb7b5ea2ee8a6fc4b3eac07b`
- `runs/20261124-045444-t08-lecture/manifeste.json` (+ `.sha256`) : `9a5871c634934797a9823a5ac6d5103ec898847fe5518dedcb8367b1535a26ae`
- `diag/20261124-045444-t08-lecture/lecture-t08.json` (+ `.sha256`) : `cefb6d2cc9b3f7d4faff01717b5a96a7ea5b1aa4d89c8cd6dfb4bbdcf99e30f9`
- `diag/20261124-045444-t08-lecture/tables-d-f-t08.json` (+ `.sha256`) : `2f9e6e8a3f12af546c54087b7b4fe685536eb51c820464040aa2dc0e4f94239a`
- `lire-stdout.json` (+ `.sha256`) : `f7573a642c666db228d482e530e26874a7171efdc7ba2ed9ac3cc51ea8279662`
- `lire-stderr.log` (+ `.sha256`) : `53af6b5aa6c160f90536ff94b3224141f88964013b84c2177ce366b8939f52d0`
- `journal-execution-lecture-t08-v3-exec.md` (+ `.sha256`) : voir compagnon `.sha256`

## Ligne « qui a lu quoi »

- `2026-11-24T04:59:28Z | lecteur habilité neuf T0.8 v3 (R-5218, conv 601219c4085c5fbba742d39b4626712c) | lu : prereg/T0.8-bases-boite-noire-v0-v3.md (en-tête et sections 0 à Les surveillants), prereg/T0.8-configuration-course-v3.json, prereg/T0.8-marqueurs-scellement-v3.json, src/controle_ia/t08/ (lire_v1.py, lecture_v1.py, entrees_v1.py, course_v1.py extraits), scripts/ecrire_configuration_lecture_t08_v1.py, consigne-lecteur-t08-v1-brouillon4.md, registres/scellements-v1.md (clés T08/T06), registres/validite-adaptateur-v1.md, registres/decisions.md (R-5218), registres/go.md (GO-2026-11-22-134), sortie standard (chemins/empreintes seuls) et progression (noms d'étapes seuls) de controle_ia.t08.lire_v1 (run 20261124-045444-t08-lecture) ; NON ouvert : lecture-t08.json, tables-d-f-t08.json, aucun score, aucun .jsonl/.npz de données, aucun résultat 7b/7a/sondes/P3-bis/HD/coffre/ii-b ; exclu à vie de toute conception de moniteur et de tout rôle aveugle.`
