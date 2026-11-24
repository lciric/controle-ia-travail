# Journal d'exécution complète — Lecture habilitée T0.8 v3 (`20261124-045444-t08-lecture`, dossier pour le juge `R13`)

- **Horodatage UTC de fin** : `2026-11-24T04:59:28Z`
- **Rôle** : lecteur habilité neuf inscrit à la ligne `R-5218` de `registres/decisions.md` (`conversation_id=601219c4085c5fbba742d39b4626712c`).
- **Statut mécanique global** : **RÉUSSI** (`EC_CONFIG=0`, `EC_LIRE=0`, toutes les étapes `(a)` à `(i)` consignées sans arrêt de garde).
- **Audit R4** : **non déclenché** (`echantillon: null`, `echantillon_sha256: null`).
- **Dépôt principal** (`/home/antigravity/lciric/controle-ia-travail`) : jamais modifié (lecture seule stricte ; exécution effectuée dans `/tmp/lecture-t08-work/repo`, nettoyé en fin d'exécution).

## 1. Arbre de code et entrées vérifiées

- **Commit du code exécuté (`CODE-T08-V3`)** : `6735dd2e1b30c2615802b78c290e24a80863b18d` (vérifié par `exiger_code_au_commit` et `exiger_code_importe_sous`).
- **Commit `origin/main` des registres et textes v3** : `67945a4d652a1fb6371bacfb32508377115dfc54` (portant `COURSE-T08` inscrite à `2026-11-24T04:47:17Z`, `R-5229`).
- **Entrées extraites par liste blanche stricte** (dans `/tmp/lecture-t08-work/repo`, sur commit local temporaire d'entrées non-code de parent `6735dd2e1b30c2615802b78c290e24a80863b18d`, identique au schéma de l'instance de calcul) :
  - `origin/main` (`67945a4d`) : `registres/scellements-v1.md`, `prereg/T0.8-bases-boite-noire-v0-v3.md` (+ `.sha256`), `prereg/T0.8-configuration-course-v3.json` (+ `.sha256`), `prereg/T0.8-marqueurs-scellement-v3.json` (+ `.sha256`).
  - `origin/calcul/t08-course-v3` (`50a6d30ce` / `b56084145`) : `diag/20261123-060509-t08-reel/course-t08.json` (+ `.sha256`), `runs/20261123-060509-t08-reel/manifeste.json` (+ `.sha256`), les 6 fichiers de `donnees/20261123-060509-t08-reel/` (+ `.sha256`). Aucun fichier > 90 Mo ; exception `GO-2026-11-22-134` non requise.
  - `origin/calcul/t06-confirmation-7b-v1` : `donnees/20261111-151701-t06-reel/mesures-t06.npz` (+ `.sha256`), `donnees/20261111-151701-t06-reel/textes-actions-t06.jsonl` (+ `.sha256`), `diag/20261111-151701-t06-reel/episodes-t06.json` (+ `.sha256`), `runs/20261111-151701-t06-reel/manifeste.json` (+ `.sha256`), `diag/20261111-151701-t06-reel/lecture-cout-t06.json` (+ `.sha256`). Aucun `lecture-sondes-t06*` ni `resume.json` de 7b extrait.
  - `origin/verdict/t06-mots-et-cout-compte-3-v1` : `diag/20261116-205721-mots-et-cout-t06/base-a-t08.json` (+ `.sha256`).
- **Pièce HD (`SORTIES-HD-VADAPT`)** : absente de `registres/validite-adaptateur-v1.md` (`--hd` non passé).

## 2. Commandes exactes et progression

1. Configuration (`EC_CONFIG=0`) :
   ```bash
   PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /home/antigravity/lciric/controle-ia-travail/.venv/bin/python3 -B \
     scripts/ecrire_configuration_lecture_t08_v1.py \
     --texte prereg/T0.8-bases-boite-noire-v0-v3.md \
     --config-course prereg/T0.8-configuration-course-v3.json \
     --registre registres/scellements-v1.md \
     --sortie prereg/T0.8-configuration-lecture-v3.json
   ```
2. Lecture (`EC_LIRE=0`, `RUN_ID=20261124-045444-t08-lecture`) :
   ```bash
   PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 /home/antigravity/lciric/controle-ia-travail/.venv/bin/python3 -B \
     -m controle_ia.t08.lire_v1 \
     --config prereg/T0.8-configuration-lecture-v3.json \
     --run-id 20261124-045444-t08-lecture \
     --prereg prereg/T0.8-bases-boite-noire-v0-v3.md
   ```
3. Journal de progression (`lire-stderr.log`) :
   - `PROGRES 2026-11-24T04:54:55Z etape=a`
   - `PROGRES 2026-11-24T04:55:48Z etape=b`
   - `PROGRES 2026-11-24T04:56:06Z etape=c`
   - `PROGRES 2026-11-24T04:56:08Z etape=d`
   - `PROGRES 2026-11-24T04:56:11Z etape=e`
   - `PROGRES 2026-11-24T04:56:11Z etape=f`
   - `PROGRES 2026-11-24T04:56:12Z etape=g`
   - `PROGRES 2026-11-24T04:56:12Z etape=tables-d-f-ecrites fichier=tables-d-f-t08.json`
   - `PROGRES 2026-11-24T04:59:07Z etape=h`
   - `PROGRES 2026-11-24T04:59:07Z etape=h bis`
   - `PROGRES 2026-11-24T04:59:07Z etape=i`

## 3. Pièces scellées remises au juge `R13` seul (toutes vérifiées par `sha256sum -c`)

Dossier : `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lecture-t08-v3-habilitee/`

- `prereg/T0.8-configuration-lecture-v3.json` : `e15f04b445a010bb5163599519dc891acc6ef321bb7b5ea2ee8a6fc4b3eac07b`
- `runs/20261124-045444-t08-lecture/manifeste.json` : `9a5871c634934797a9823a5ac6d5103ec898847fe5518dedcb8367b1535a26ae`
- `diag/20261124-045444-t08-lecture/lecture-t08.json` : `cefb6d2cc9b3f7d4faff01717b5a96a7ea5b1aa4d89c8cd6dfb4bbdcf99e30f9`
- `diag/20261124-045444-t08-lecture/tables-d-f-t08.json` : `2f9e6e8a3f12af546c54087b7b4fe685536eb51c820464040aa2dc0e4f94239a`
- `lire-stdout.json` : `f7573a642c666db228d482e530e26874a7171efdc7ba2ed9ac3cc51ea8279662`
- `lire-stderr.log` : `53af6b5aa6c160f90536ff94b3224141f88964013b84c2177ce366b8939f52d0`

Conformément à `consigne-lecteur-t08-v1-brouillon4.md` (§ 3 et § 6), le lecteur n'a ouvert ni `lecture-t08.json` ni `tables-d-f-t08.json` (l'audit R4 n'ayant pas été déclenché). Le juge `R13` seul lira `lecture-t08.json` et `tables-d-f-t08.json` pour prononcer le verdict scellé.

## 4. Ligne « qui a lu quoi »

- `2026-11-24T04:59:28Z | lecteur habilité neuf T0.8 v3 (R-5218, conv 601219c4085c5fbba742d39b4626712c) | lu : prereg/T0.8-bases-boite-noire-v0-v3.md (en-tête et sections 0 à Les surveillants), prereg/T0.8-configuration-course-v3.json, prereg/T0.8-marqueurs-scellement-v3.json, src/controle_ia/t08/ (lire_v1.py, lecture_v1.py, entrees_v1.py, course_v1.py extraits), scripts/ecrire_configuration_lecture_t08_v1.py, consigne-lecteur-t08-v1-brouillon4.md, registres/scellements-v1.md (clés T08/T06), registres/validite-adaptateur-v1.md, registres/decisions.md (R-5218), registres/go.md (GO-2026-11-22-134), sortie standard (chemins/empreintes seuls) et progression (noms d'étapes seuls) de controle_ia.t08.lire_v1 (run 20261124-045444-t08-lecture) ; NON ouvert : lecture-t08.json, tables-d-f-t08.json, aucun score, aucun .jsonl/.npz de données, aucun résultat 7b/7a/sondes/P3-bis/HD/coffre/ii-b ; exclu à vie de toute conception de moniteur et de tout rôle aveugle.`
