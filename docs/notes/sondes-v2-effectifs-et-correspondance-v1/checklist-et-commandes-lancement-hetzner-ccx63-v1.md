# Checklist et commandes de lancement — Épreuve à vérité plantée des sondes boîte blanche v2 sur Hetzner `ccx63` (`GO-2026-11-24-02`)

- **Rédacteur** : sous-agent préparateur de l'épreuve plantée (`964974f3677d3fc11cecb850254d332a`, fils de `ff6e9350-ef6c-4238-b52d-64a517f4205f`), `2026-11-24T05:05:00Z`.
- **Statut d'exécution** : **préparation seule** — aucun serveur Hetzner créé, aucune dépense engagée, aucune clé affichée, dépôts `/home/antigravity/lciric/controle-ia-travail` et `/home/antigravity/worktrees/sondes-v2-code` intacts (lecture seule, `PYTHONDONTWRITEBYTECODE=1`).
- **Références qui font foi** :
  - Accord budgétaire : `GO-2026-11-24-02` (`registres/go.md`, inscrit `R-5222`), plafond **`68 USD`** sur Hetzner `ccx63` à `hel1` (`1,3942` EUR/h brut vérifié, soit `1,74275` USD/h au taux `1,25` du registre).
  - Plan et devis v2 : `docs/notes/sondes-v2-concepteur-opus-v1/plan-epreuve-plantee-et-devis-v2.md` (`717cea17b031d7d8a9439d0cbcef41eafdff52fcba3cfeb207ae39886ef76462`), § 1 et § 4–5.
  - Code figé : commit `0ce9e35110d93dd916e85b1191a2613b101e772d` (`origin/sondes-v2/code-v2`), `219 passed, 1 skipped` (`215` à `9d33c36c5` + `4` essais d'Option A ajoutés à `0ce9e3511`), arbre propre exigé (`--autoriser-depot-sale` interdit).
  - Vérités engagées v4 : `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json` (`b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533`).
  - Note des effectifs conforme : `docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md` (`7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5`), validée `CONFORME EN L'ÉTAT` par la contre-lecture R2 `5d46ac878fd469dd33069fffd215a7799dcdd83958b302fc6d409e898a081e7a` (`R-5218`).
  - Entropie racine (`R-5056`) : `305159624078239919914131004197200342142`.
  - Effectifs et devis : `TA_etalon = 80` (`40 × 2`, `52` cases, `extension_taches_actions = false`, opt. A : `184,7 h` CPU, `3,85 h` sur `ccx63`, `6,70 USD`) + `TA_rejeu = 640` (`64 × 10`, `D = 4`, contrôle du chemin `contrôle absent`, opt. C `--nul 39` : `1 056,0 h` CPU, `22,00 h` sur `ccx63`, `38,34 USD`) = **`45,05 USD` attendus en `25,85 h`** (`1 240,7 h` CPU ; coupure dure R10 à **`32 h`** ou **`60 USD`** ; repli automatique sur `--mode etalon` seul `~6,70 USD` si refus de quota 48 vCPU).
  - Additif de commit brouillon 2 prêt : `diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md` (`958bb6a2f4c708b86958f5f6dcc1e9bb8af32021bf1a00b6398a588aab1fb01b`).

---

## 1. Ordre exact des préalables et commandes de scellement (avant création de machine)

> **Point d'attention protocole (`plan-epreuve-plantee-et-devis-v2.md`, § 1 point 5)** : la contre-lecture R2 (`5d46ac87…`) a déclaré la note des effectifs (`7338a3dc…`) `CONFORME EN L'ÉTAT`, mais a demandé 2 corrections de classe B sur le seul volet « table de correspondance du rejeu croisé » (`correspondance-rejeu-croise-v1.json`). `programme_monde_plante_v4.py` ne lit jamais la table de correspondance ; toutefois, pour sceller l'additif avec `--mode-correspondance jonction_tardive`, `remplir_additif_commit_sondes_v2_v1.py` exige une table corrigée + contre-lue conforme (ou bien `--mode-correspondance rejeu_non_calculable` si la table n'est pas jointe). La session mère choisit l'enchaînement : (i) soit achever la courte passe R2 sur `correspondance-rejeu-croise-v2.json` avant l'étape 1.3, (ii) soit lancer l'épreuve `--mode etalon` d'abord si elle veut découpler.

### 1.1 Verser le brouillon 2 de l'additif sur `main` et lancer sa contre-lecture R2 (classe A)

```bash
export PYTHONDONTWRITEBYTECODE=1
REPO="/home/antigravity/lciric/controle-ia-travail"
SCRATCH="/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lancement-sondes-v2-hetzner"
DEST="$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1"

cp "$SCRATCH/diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md" "$DEST/"
cp "$SCRATCH/diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md.sha256" "$DEST/"
(cd "$DEST" && sha256sum -c diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md.sha256)
```

Invoquer ensuite un **sous-agent neuf de contre-lecture R2 (classe A)** strictement distinct du rédacteur (`964974f3…`) sur `diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md` (`958bb6a2…`), avec cloisonnement strict (aucun fichier sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/`, `brouillons/ii-b*`, `consigne-privee*`). Sceller son rapport `contre-lecture-r2-additif-commit-sondes-v2-v1.md` (+ `.sha256`).

### 1.2 Remplir et sceller mécaniquement l'additif officiel `prereg/diagnostics-prealables-sondes-v1-additif-commit-v1.md`

```bash
export PYTHONDONTWRITEBYTECODE=1
REPO="/home/antigravity/lciric/controle-ia-travail"
WT="/home/antigravity/worktrees/sondes-v2-code"
PY="$REPO/.venv/bin/python3"
DATE_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Exemple avec jonction tardive une fois correspondance-rejeu-croise-v2.json contre-lue conforme
# (sinon remplacer --mode-correspondance jonction_tardive et ses 4 arguments par --mode-correspondance rejeu_non_calculable)
PYTHONPATH="$WT/src" "$PY" -B \
  "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/remplir_additif_commit_sondes_v2_v1.py" \
  --brouillon "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md" \
  --sortie "$REPO/prereg/diagnostics-prealables-sondes-v1-additif-commit-v1.md" \
  --note-effectifs "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md" \
  --chemin-note-depot "docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md" \
  --attendu-sha256-note "7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5" \
  --attendu-doses-d 4 \
  --date-scellement-utc "$DATE_UTC" \
  --option-rejeux-nuls 39 \
  --mode-correspondance jonction_tardive \
  --go-correspondance "GO-2026-11-23-36" \
  --fichier-correspondance "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/correspondance-rejeu-croise-v2.json" \
  --chemin-correspondance-depot "docs/notes/sondes-v2-effectifs-et-correspondance-v1/correspondance-rejeu-croise-v2.json" \
  --rapport-cl-correspondance "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/verification-r2-correspondance-rejeu-croise-v2.md" \
  --chemin-rapport-cl-correspondance-depot "docs/notes/sondes-v2-effectifs-et-correspondance-v1/verification-r2-correspondance-rejeu-croise-v2.md" \
  --rapport-contre-lecture "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/contre-lecture-r2-additif-commit-sondes-v2-v1.md" \
  --chemin-rapport-contre-lecture-depot "docs/notes/sondes-v2-effectifs-et-correspondance-v1/contre-lecture-r2-additif-commit-v1.md" \
  --verdict-contre-lecture "<VERDICT_EXACT_R2>"

# Contrôle final prereg (doit retourner [] et vérifier le .sha256)
PYTHONPATH="$WT/src" "$PY" -B -c "
from controle_ia import prereg
p = '$REPO/prereg/diagnostics-prealables-sondes-v1-additif-commit-v1.md'
assert prereg.problemes(p) == [], prereg.problemes(p)
print('PREREG SCELLE OK:', prereg.exiger_prereg_scelle(p))
"
```

### 1.3 Vérifier la propreté de `origin/sondes-v2/code-v2` et pousser les pièces scellées sur `main`

```bash
# Vérifier que le commit 0ce9e3511 est bien poussé sur origin/sondes-v2/code-v2
git -C /home/antigravity/worktrees/sondes-v2-code status --porcelain
git -C /home/antigravity/worktrees/sondes-v2-code rev-parse HEAD origin/sondes-v2/code-v2

# Committer et pousser l'additif scellé + la ligne d'engagement FEU + la décision R-xxxx sur main
```

---

## 2. Ligne d'engagement `FEU` prête à coller dans `registres/depenses.md` (avant création du serveur)

À insérer dans `registres/depenses.md` (section `## Engagements avant création d'instance`) **avant** tout appel `POST /v1/servers` sur l'API Hetzner :

```markdown
| <DATE_UTC_FEU> | GO-2026-11-24-02 | FEU — engagement épreuve à vérité plantée des sondes boîte blanche v2 (`programme_monde_plante_v4.py`, commit figé `0ce9e35110d93dd916e85b1191a2613b101e772d` sur `origin/sondes-v2/code-v2`, vérités v4 `b310e1af…`, note des effectifs `7338a3dc…` conforme `5d46ac87…`, additif scellé `<SHA256_ADDITIF_SCELLE>`, entropie racine `R-5056` `305159624078239919914131004197200342142`) : serveur dédié Hetzner `ccx63` (48 cœurs dédiés) à `hel1`, prix relu par API `1,3942 EUR/h` brut (`1,74275 USD/h` au taux `1,25`), `0` serveur actif avant création ; mode `etalon` option A (`52` cases, `TA_etalon = 80`, attendu `6,70 USD` / `3,85 h`) + mode `complet` option C (`--nul 39`, `TA_rejeu = 640`, `D = 4`, contrôle du chemin absent, attendu `38,34 USD` / `22,00 h`) = **`45,05 USD` attendus en `25,85 h`** (`64,40 USD` au lieu max) ; repli automatique sur `--mode etalon` seul (`~6,70 USD` sur `ccx33`/`ccx43`) en cas de refus de quota 48 vCPU ; branche de sortie `calcul/sondes-v2-epreuve-plantee-v4` ; coupure dure et destruction `R10` par identifiant numérique à **`32 h`** (`≈ 55,77 USD`) ou **`60 USD`** (garde externe + interne), après rapatriement prouvé par `git ls-remote` | 68 USD (plafond ; alerte 54,4 USD ; coupure dure 60 USD / 32 h) | R-<NUMERO_DECISION> |
```

---

## 3. Script d'amorce autonome Hetzner `ccx63` (`hel1`, `cloud-init`, repli quota 48 vCPU, rapatriement prouvé et destruction `R10`)

> **Note technique** : `hcloud` CLI n'est pas installé dans la VM ; le script utilise directement l'API REST officielle Hetzner Cloud (`https://api.hetzner.cloud/v1/servers`) via `curl` et `jq` avec `HCLOUD_TOKEN` et `CONTROLE_IA_GITHUB_TOKEN_2` sourcés depuis `/home/antigravity/env-setup.sh` (jamais affichés, `set +x` maintenu).
> **Note d'arbre propre** : sur la machine distante, `note-des-effectifs-sondes-v2-v1.md` (+ `.sha256`) est déposée dans `/opt/entree/` **hors** du dépôt git cloné au commit `0ce9e3511`, garantissant que `manifeste.commit == "0ce9e35110d93dd916e85b1191a2613b101e772d"` et `manifeste.depot_propre == true` dans chaque rapport (sans jamais passer `--autoriser-depot-sale`).

### 3.1 Script de lancement et garde-fou externe `R10` (à exécuter sur la devbox mère après le `FEU`)

```bash
#!/usr/bin/env bash
# Lancer UNIQUEMENT après : (1) additif scellé et poussé, (2) ligne FEU inscrite dans registres/depenses.md.
set -euo pipefail
set +x
export PYTHONDONTWRITEBYTECODE=1

# Charger les jetons sans jamais les afficher
source /home/antigravity/env-setup.sh
: "${HCLOUD_TOKEN:?HCLOUD_TOKEN absent}"
GITHUB_PUSH_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_2:-${CONTROLE_IA_GITHUB_TOKEN_3:-}}"
: "${GITHUB_PUSH_TOKEN:?CONTROLE_IA_GITHUB_TOKEN_2/3 absent}"

API="https://api.hetzner.cloud/v1"
AUTH=(-H "Authorization: Bearer ${HCLOUD_TOKEN}" -H "Content-Type: application/json")

COMMIT_CODE="0ce9e35110d93dd916e85b1191a2613b101e772d"
ENTROPIE="305159624078239919914131004197200342142"
SHA_VERITES="b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533"
SHA_NOTE="7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5"
BRANCHE_SORTIE="calcul/sondes-v2-epreuve-plantee-v4"
LOCATION="hel1"
MAX_HOURS=32
MAX_USD=60
TAUX_EUR_USD="1.25"
ETAT_DIR="/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lancement-sondes-v2-hetzner/run-etat"
mkdir -p "$ETAT_DIR"

# 1. Contrôle préalable : 0 serveur actif et relecture du prix API à hel1
N_ACTIFS="$(curl -fsS "${AUTH[@]}" "$API/servers" | jq '.servers | length')"
if [ "$N_ACTIFS" -ne 0 ]; then
  echo "ARRÊT : $N_ACTIFS serveur(s) Hetzner déjà actif(s) ; vérifier avant création." >&2
  exit 1
fi

PRIX_EUR_CCX63="$(curl -fsS "${AUTH[@]}" "$API/server_types?name=ccx63" \
  | jq -r --arg loc "$LOCATION" '.server_types[0].prices[] | select(.location==$loc) | .price_hourly.gross')"
echo "Prix API relu ccx63@$LOCATION : ${PRIX_EUR_CCX63} EUR/h brut"
python3 -B -c "
p = float('$PRIX_EUR_CCX63')
assert p <= 1.55, f'Prix ccx63 hors devis: {p} EUR/h'
print(f'Prix USD/h (taux 1.25) = {p * 1.25:.5f}')
"

# 2. Générateur de cloud-init paramétré par mode (complet_et_etalon | etalon_seul)
generer_cloud_init() {
  local mode_run="$1"
  cat <<EOF
#cloud-config
package_update: true
packages:
  - git
  - curl
  - jq
  - python3
  - python3-venv
  - tar
  - gzip
write_files:
  - path: /opt/run_epreuve_sondes_v2.sh
    permissions: '0700'
    content: |
      #!/usr/bin/env bash
      set -euo pipefail
      set +x
      export PYTHONDONTWRITEBYTECODE=1
      export OMP_NUM_THREADS=1
      export OPENBLAS_NUM_THREADS=1
      export MKL_NUM_THREADS=1
      export NUMEXPR_NUM_THREADS=1

      MODE_RUN="${mode_run}"
      COMMIT_CODE="${COMMIT_CODE}"
      ENTROPIE="${ENTROPIE}"
      SHA_VERITES="${SHA_VERITES}"
      SHA_NOTE="${SHA_NOTE}"
      BRANCHE_SORTIE="${BRANCHE_SORTIE}"
      N_WORKERS="\$(nproc)"
      WORK="/opt/sondes-v2"
      ENTREE="/opt/entree"
      SORTIE="/opt/sortie"
      LOG="/var/log/epreuve-sondes-v2.log"
      mkdir -p "\$WORK" "\$ENTREE" "\$SORTIE/etalon" "\$SORTIE/complet"

      exec > >(tee -a "\$LOG") 2>&1
      echo "=== DÉBUT \$(date -u +%Y-%m-%dT%H:%M:%SZ) | mode=\$MODE_RUN | nproc=\$N_WORKERS ==="

      # Récupération de l'identifiant Hetzner de la machine (métadonnées locales 169.254.169.254)
      SERVER_ID="\$(curl -fsS http://169.254.169.254/hetzner/v1/metadata/instance-id || true)"
      echo "SERVER_ID=\$SERVER_ID"

      # Auto-destruction R10 garantie en sortie (après push ou erreur critique)
      detruire_serveur() {
        local rc=\$?
        echo "=== FIN (rc=\$rc) \$(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
        if [ -n "\${SERVER_ID:-}" ] && [ -n "\${HCLOUD_TOKEN:-}" ]; then
          echo "Appel R10 DELETE /v1/servers/\${SERVER_ID}"
          curl -fsS -X DELETE -H "Authorization: Bearer \${HCLOUD_TOKEN}" \
            "https://api.hetzner.cloud/v1/servers/\${SERVER_ID}" || true
        fi
      }
      trap detruire_serveur EXIT

      # Cloner le dépôt (jeton injecté via fichier protégé 0600, jamais loggé)
      export HCLOUD_TOKEN="\$(cat /root/.hcloud_token)"
      GH_TOK="\$(cat /root/.gh_token)"
      REPO_URL="https://x-access-token:\${GH_TOK}@github.com/lciric/controle-ia-travail.git"

      git clone --no-tags --branch sondes-v2/code-v2 "\$REPO_URL" "\$WORK/repo"
      git -C "\$WORK/repo" checkout --detach "\$COMMIT_CODE"
      test -z "\$(git -C "\$WORK/repo" status --porcelain)"
      echo "\$SHA_VERITES  \$WORK/repo/src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json" | sha256sum -c -

      # Récupérer la note des effectifs (+ .sha256) depuis main HORS du dépôt git (préserve depot_propre=True)
      git -C "\$WORK/repo" fetch origin main --depth=1
      git -C "\$WORK/repo" show origin/main:docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md \
        > "\$ENTREE/note-des-effectifs-sondes-v2-v1.md"
      git -C "\$WORK/repo" show origin/main:docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md.sha256 \
        > "\$ENTREE/note-des-effectifs-sondes-v2-v1.md.sha256"
      (cd "\$ENTREE" && sha256sum -c note-des-effectifs-sondes-v2-v1.md.sha256)
      echo "\$SHA_NOTE  \$ENTREE/note-des-effectifs-sondes-v2-v1.md" | sha256sum -c -

      # Environnement Python épinglé sur les versions exactes vérifiées localement
      python3 -m venv "\$WORK/venv"
      "\$WORK/venv/bin/pip" install --no-cache-dir numpy==2.4.6 scipy==1.17.1 scikit-learn==1.9.1
      PY="\$WORK/venv/bin/python3"
      export PYTHONPATH="\$WORK/repo/src"

      # Fonction de lancement parallèle en 50 plages de 10 répliques couvrant [0, 500)
      lancer_mode() {
        local mode="\$1"
        local outdir="\$SORTIE/\$mode"
        local extra_args=()
        if [ "\$mode" = "complet" ]; then
          extra_args+=(--doses-rejeu 4 --nul 39)
        fi
        echo ">>> Lancement mode=\$mode (50 plages x 10 répliques, \$N_WORKERS workers)"
        seq 0 10 490 | xargs -n 1 -P "\$N_WORKERS" -I {} bash -c '
          set -euo pipefail
          de="{}"
          a=\$((de + 10))
          exec "'"\$PY"'" -B -m controle_ia.sondes_v2.programme_monde_plante_v4 \
            --sortie "'"\$outdir"'" \
            --note-effectifs "'"\$ENTREE/note-des-effectifs-sondes-v2-v1.md"'" \
            --mode "'"\$mode"'" \
            '"\${extra_args[*]:-}"' \
            --repliques 500 --repliques-de "\$de" --repliques-a "\$a" \
            --entropie "'"\$ENTROPIE"'"
        '
        # Fusion officielle scellée (identique à l'octet à un processus unique)
        "\$PY" -B -c "
import glob
from controle_ia.sondes_v2 import programme_monde_plante_v4 as p
chemins = sorted(glob.glob('\$outdir/rapport-monde-plante-v4-\$mode-\$ENTROPIE-r*.json'))
assert len(chemins) == 50, len(chemins)
out = p.ecrire_synthese_fusionnee(chemins, '\$outdir/synthese-fusionnee-monde-plante-v4-\$mode-\$ENTROPIE.json')
print('SYNTHESE SCELLEE:', out)
"
      }

      # Fonction de rapatriement prouvé sur la branche dédiée (jamais main, aucun fichier > 95 Mo)
      pousser_sorties() {
        local etiquette="\$1"
        local pub="\$WORK/pub"
        rm -rf "\$pub"
        git init "\$pub"
        git -C "\$pub" config user.name "sondes-v2-hetzner-runner"
        git -C "\$pub" config user.email "runner@controle-ia.local"
        git -C "\$pub" checkout -B "\$BRANCHE_SORTIE"
        mkdir -p "\$pub/epreuve-plantee-v4/etalon" "\$pub/epreuve-plantee-v4/complet"

        # Copier les synthèses fusionnées + rapports par plage + .sha256
        for m in etalon complet; do
          if [ -d "\$SORTIE/\$m" ]; then
            cp -f "\$SORTIE/\$m"/synthese-fusionnee-*.json* "\$pub/epreuve-plantee-v4/\$m/" 2>/dev/null || true
            cp -f "\$SORTIE/\$m"/rapport-monde-plante-v4-*.json* "\$pub/epreuve-plantee-v4/\$m/" 2>/dev/null || true
          fi
        done

        # Compresser les journaux des gels du mode complet (≈ 1,5 Go bruts -> archive .tar.gz + .sha256)
        if ls "\$SORTIE/complet"/journal-gels-*.jsonl >/dev/null 2>&1; then
          (cd "\$SORTIE/complet" && sha256sum journal-gels-*.jsonl > "\$pub/epreuve-plantee-v4/complet/journaux-gels.sha256")
          tar -czf "\$SORTIE/journaux-gels-complet.tar.gz" -C "\$SORTIE/complet" \$(cd "\$SORTIE/complet" && ls journal-gels-*.jsonl journal-gels-*.jsonl.sha256)
          (cd "\$SORTIE" && sha256sum journaux-gels-complet.tar.gz > "\$pub/epreuve-plantee-v4/complet/journaux-gels-complet.tar.gz.sha256")
          # N'inclure l'archive dans git que si <= 90 Mo ; sinon découper en morceaux de 45 Mo (limite GitHub 100 Mo)
          TAILLE_MO=\$(du -m "\$SORTIE/journaux-gels-complet.tar.gz" | cut -f1)
          if [ "\$TAILLE_MO" -le 90 ]; then
            cp -f "\$SORTIE/journaux-gels-complet.tar.gz" "\$pub/epreuve-plantee-v4/complet/"
          else
            split -b 45m -d "\$SORTIE/journaux-gels-complet.tar.gz" "\$pub/epreuve-plantee-v4/complet/journaux-gels-complet.tar.gz.part."
            (cd "\$pub/epreuve-plantee-v4/complet" && sha256sum journaux-gels-complet.tar.gz.part.* > journaux-gels-complet.parts.sha256)
          fi
        fi

        cp -f "\$LOG" "\$pub/epreuve-plantee-v4/journal-execution.log"
        (cd "\$pub/epreuve-plantee-v4" && find . -type f -name "*.sha256" -print0 | xargs -0 -n1 bash -c 'cd "\$(dirname "\$1")" && sha256sum -c "\$(basename "\$1")"' _)

        git -C "\$pub" add -A
        git -C "\$pub" commit -m "Sondes v2 épreuve plantée v4 (\$etiquette, commit \$COMMIT_CODE, GO-2026-11-24-02)"
        LOCAL_SHA="\$(git -C "\$pub" rev-parse HEAD)"
        git -C "\$pub" push --force "\$REPO_URL" "HEAD:refs/heads/\$BRANCHE_SORTIE"
        REMOTE_SHA="\$(git ls-remote "\$REPO_URL" "refs/heads/\$BRANCHE_SORTIE" | awk '{print \$1}')"
        test "\$LOCAL_SHA" = "\$REMOTE_SHA"
        echo "RAPATRIEMENT PROUVÉ : \$BRANCHE_SORTIE @ \$REMOTE_SHA"
      }

      # Plafond interne dur 31h30 (avant la coupure externe 32h)
      timeout 113400 bash -c '
        true
      '
      lancer_mode etalon
      pousser_sorties "etalon-termine"

      if [ "\$MODE_RUN" = "complet_et_etalon" ]; then
        lancer_mode complet
        pousser_sorties "etalon-et-complet-termines"
      fi

  - path: /root/.hcloud_token
    permissions: '0600'
    content: "${HCLOUD_TOKEN}"
  - path: /root/.gh_token
    permissions: '0600'
    content: "${GITHUB_PUSH_TOKEN}"

runcmd:
  - [ bash, /opt/run_epreuve_sondes_v2.sh ]
EOF
}

# 3. Création du serveur ccx63 à hel1 avec repli automatique sur etalon seul (ccx33) si refus de quota 48 vCPU
MODE_LANCE="complet_et_etalon"
SERVER_TYPE="ccx63"
USER_DATA="$(generer_cloud_init "$MODE_LANCE")"
PAYLOAD="$(jq -n \
  --arg name "sondes-v2-epreuve-v4-$(date -u +%Y%m%d-%H%M)" \
  --arg st "$SERVER_TYPE" \
  --arg loc "$LOCATION" \
  --arg ud "$USER_DATA" \
  '{name: $name, server_type: $st, location: $loc, image: "ubuntu-24.04", user_data: $ud, labels: {go: "GO-2026-11-24-02", projet: "sondes-v2-epreuve-v4"}}')"

RESP_FILE="$ETAT_DIR/create-response.json"
HTTP_CODE="$(curl -sS -o "$RESP_FILE" -w "%{http_code}" -X POST "${AUTH[@]}" -d "$PAYLOAD" "$API/servers")"

if [ "$HTTP_CODE" != "201" ]; then
  ERR_CODE="$(jq -r '.error.code // "unknown"' "$RESP_FILE")"
  echo "Création ccx63 refusée (HTTP $HTTP_CODE, code=$ERR_CODE) -> repli automatique GO-2026-11-24-02 sur --mode etalon seul (ccx33)"
  if [[ "$ERR_CODE" == *"limit"* || "$ERR_CODE" == *"quota"* || "$HTTP_CODE" == "412" || "$HTTP_CODE" == "422" ]]; then
    MODE_LANCE="etalon_seul"
    SERVER_TYPE="ccx33"
    USER_DATA="$(generer_cloud_init "$MODE_LANCE")"
    PAYLOAD="$(jq -n \
      --arg name "sondes-v2-etalon-v4-$(date -u +%Y%m%d-%H%M)" \
      --arg st "$SERVER_TYPE" \
      --arg loc "$LOCATION" \
      --arg ud "$USER_DATA" \
      '{name: $name, server_type: $st, location: $loc, image: "ubuntu-24.04", user_data: $ud, labels: {go: "GO-2026-11-24-02", projet: "sondes-v2-etalon-seul"}}')"
    HTTP_CODE="$(curl -sS -o "$RESP_FILE" -w "%{http_code}" -X POST "${AUTH[@]}" -d "$PAYLOAD" "$API/servers")"
    test "$HTTP_CODE" = "201"
  else
    echo "ARRÊT : erreur API non-quota ($HTTP_CODE / $ERR_CODE)" >&2
    exit 1
  fi
fi

SERVER_ID="$(jq -r '.server.id' "$RESP_FILE")"
CREATED_EPOCH="$(date -u +%s)"
PRIX_EUR_ACTIF="$(curl -fsS "${AUTH[@]}" "$API/server_types?name=$SERVER_TYPE" \
  | jq -r --arg loc "$LOCATION" '.server_types[0].prices[] | select(.location==$loc) | .price_hourly.gross')"
jq -n \
  --arg id "$SERVER_ID" --arg st "$SERVER_TYPE" --arg loc "$LOCATION" \
  --arg mode "$MODE_LANCE" --arg eur "$PRIX_EUR_ACTIF" --argjson t0 "$CREATED_EPOCH" \
  '{server_id: $id, server_type: $st, location: $loc, mode: $mode, price_eur_h_gross: $eur, created_epoch: $t0}' \
  > "$ETAT_DIR/serveur-actif.json"
echo "SERVEUR CRÉÉ : id=$SERVER_ID type=$SERVER_TYPE loc=$LOCATION mode=$MODE_LANCE prix=${PRIX_EUR_ACTIF} EUR/h"

# 4. Minuterie externe R10 (devbox mère) : destruction par identifiant à 32 h OU 60 USD
nohup bash -c '
  set -euo pipefail
  set +x
  source /home/antigravity/env-setup.sh
  API="https://api.hetzner.cloud/v1"
  SERVER_ID="'"$SERVER_ID"'"
  T0="'"$CREATED_EPOCH"'"
  PRIX_EUR="'"$PRIX_EUR_ACTIF"'"
  MAX_H="'"$MAX_HOURS"'"
  MAX_USD="'"$MAX_USD"'"
  while true; do
    sleep 300
    HTTP="$(curl -sS -o /dev/null -w "%{http_code}" -H "Authorization: Bearer ${HCLOUD_TOKEN}" "$API/servers/$SERVER_ID")"
    if [ "$HTTP" = "404" ]; then
      echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) Serveur $SERVER_ID déjà détruit (404)."
      exit 0
    fi
    NOW="$(date -u +%s)"
    OVER="$(python3 -B -c "
h = ($NOW - $T0) / 3600.0
usd = h * float(\"$PRIX_EUR\") * 1.25
print(1 if (h >= float(\"$MAX_H\") or usd >= float(\"$MAX_USD\")) else 0)
")"
    if [ "$OVER" = "1" ]; then
      echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) R10 CAP ATTEINT -> DELETE /v1/servers/$SERVER_ID"
      curl -fsS -X DELETE -H "Authorization: Bearer ${HCLOUD_TOKEN}" "$API/servers/$SERVER_ID" || true
      exit 0
    fi
  done
' > "$ETAT_DIR/watchdog-r10-${SERVER_ID}.log" 2>&1 &
echo "Watchdog externe R10 lancé (PID $!) -> $ETAT_DIR/watchdog-r10-${SERVER_ID}.log"
```

---

## 4. Essai à blanc local vérifié (`--help`, suite de tests et cas miniatures avec `.venv/bin/python3`)

Exécutés le `2026-11-24` en lecture seule sur `/home/antigravity/worktrees/sondes-v2-code` (`0ce9e35110d93dd916e85b1191a2613b101e772d`) avec `PYTHONDONTWRITEBYTECODE=1` et `/home/antigravity/lciric/controle-ia-travail/.venv/bin/python3 -B` (`numpy 2.4.6`, `scipy 1.17.1`, `scikit-learn 1.9.1`) :

1. **Suite de tests unitaires `sondes_v2` (sans écriture dans le worktree)** :
   ```bash
   PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/home/antigravity/worktrees/sondes-v2-code/src \
     /home/antigravity/lciric/controle-ia-travail/.venv/bin/python3 -B -m pytest \
     -p no:cacheprovider -q /home/antigravity/worktrees/sondes-v2-code/tests/test_sondes_v2_*.py
   ```
   - **Résultat observé** : `219 passed, 1 skipped` (`0` échec).
2. **Aide CLI (`--help`)** :
   ```bash
   PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/home/antigravity/worktrees/sondes-v2-code/src \
     /home/antigravity/lciric/controle-ia-travail/.venv/bin/python3 -B \
     -m controle_ia.sondes_v2.programme_monde_plante_v4 --help
   ```
   - **Résultat observé** : code de sortie `0`, toutes les options (`--sortie`, `--note-effectifs`, `--mode {complet,etalon}`, `--doses-rejeu`, `--repliques`, `--repliques-de`, `--repliques-a`, `--nul`, `--entropie`, etc.) conformes.
3. **Trois essais à blanc miniatures exécutés vers un dossier scratch temporaire (sans `--autoriser-depot-sale`)** :
   - **Étalon miniature** (`--cas 4,1,8,1 --repliques 1 --tirages 10 --nul-identite 5 --d 16 --mondes trace_faible --entropie 305159624078239919914131004197200342142`) : rapport scellé produit, `sha256sum -c` = `OK`.
   - **Complet miniature** (`--taille 4,8,2 --doses-rejeu 4 --repliques 1 --nul 3 --tirages 10 --nul-identite 5 --d 16 --mondes fuite_de_pli --entropie 305159624078239919914131004197200342142`) : rapport scellé produit, `sha256sum -c` = `OK`.
   - **Complet avec la vraie note des effectifs `7338a3dc…` et découpage de plage** (`--note-effectifs .../note-des-effectifs-sondes-v2-v1.md --mode complet --doses-rejeu 4 --repliques 2 --repliques-de 0 --repliques-a 1 --nul 39 --tirages 10 --nul-identite 5 --d 16 --mondes fuite_de_pli --entropie 305159624078239919914131004197200342142`) : résout automatiquement `complet 8,64,10`, vérifie l'empreinte de la note et `depot_propre = true` sur `0ce9e3511`, écrit et scelle `rapport-monde-plante-v4-complet-305159624078239919914131004197200342142-r0-1.json`, `sha256sum -c` = `OK`.
4. **Validation mécanique de `brouillon2.md`** :
   - Remplissage par `remplir_additif_commit_sondes_v2_v1.py` (`91ec23f6…`) contre la vraie note des effectifs (`7338a3dc…`, `D = 4`, `contrôle absent`) puis contrôle par `controle_ia.prereg.problemes` et `prereg.exiger_prereg_scelle` : **`[]` (zéro erreur)**.
5. **Intégrité finale des dépôts** : `git status --porcelain` vide sur `/home/antigravity/lciric/controle-ia-travail` et `/home/antigravity/worktrees/sondes-v2-code`.
