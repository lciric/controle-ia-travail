# Checklist et commandes de lancement (v2) — Épreuve à vérité plantée des sondes boîte blanche v2 sur Hetzner `ccx63` (`GO-2026-11-24-02`)

- **Rédacteur** : développeur correcteur `v2` (sous-agent `975ccad6fd30e342b1676ac46db3b08b`, fils de `ff6e9350-ef6c-4238-b52d-64a517f4205f`), `2026-11-24T05:15:00Z`.
- **Objet** : version 2 appliquant et éprouvant par essais `R5` les **4 corrections fermées** de la contre-lecture R2 indépendante de classe A `docs/notes/sondes-v2-effectifs-et-correspondance-v1/contre-lecture-r2-additif-commit-et-checklist-hetzner-v1.md` (`e94bd12ba714001d1e3029836497e7d4f9f9c512e9ec35437ebeeaa1dc0d73ad`). Remplace `checklist-et-commandes-lancement-hetzner-ccx63-v1.md` (`ddcd8903…`, conservée, règle numéro 12).
- **Statut d'exécution** : **préparation et essais `R5` locaux seuls** — aucun serveur Hetzner créé, aucune dépense engagée, aucune clé affichée, dépôts `/home/antigravity/lciric/controle-ia-travail` et `/home/antigravity/worktrees/sondes-v2-code` intacts (lecture seule, `PYTHONDONTWRITEBYTECODE=1`).
- **Livrables `v2` vérifiés (+ `.sha256`)** :
  - `remplir_additif_commit_sondes_v2_v2.py` : `4cc2a17ad396f5e60b30bd7810de3ac619fa7f28d6e2baf7c5cb1e11491e229a` (ajoute `--mode-correspondance jonction_tardive_ulterieure` conforme à `GO-2026-11-23-36` et `R-5209` point 2).
  - `amorce-hetzner-sondes-v2-ccx63-v2.sh` : `fdbc193d2c2372e0903238a9e75900a9180e6cf152bb33a3180e4cfc50088f0b` (corrige les 3 bloquants de `e94bd12b…` : intégrité `100 %` des `.sha256` dans `$pub` avant `git push`, `GIT_ASKPASS` `0700` + URL HTTPS nue + filtre `sed` anti-fuite, vraie minuterie interne `R10` à `113400 s` = `31h30`).
  - `test_amorce_hetzner_r5_v2.py` : `7600f90f6c3b8b7089d71ff2d02c2535846a0f2f7734ee0fd38f4b2617889738` (suite d'essais `R5` locaux sur dépôt git bare `/tmp/test-hetzner-r5/` + faux serveur API Hetzner, `4/4` scénarios passés).
- **Références qui font foi** :
  - Accord budgétaire : `GO-2026-11-24-02` (`registres/go.md`, `R-5222`), plafond **`68 USD`** sur Hetzner `ccx63` à `hel1` (`1,3942` EUR/h brut vérifié, soit `1,74275` USD/h au taux `1,25` du registre).
  - Code figé : commit `0ce9e35110d93dd916e85b1191a2613b101e772d` (`origin/sondes-v2/code-v2`), `219 passed, 1 skipped`, arbre propre exigé (`--autoriser-depot-sale` interdit).
  - Vérités engagées v4 : `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json` (`b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533`).
  - Note des effectifs conforme : `docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md` (`7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5`), validée `CONFORME EN L'ÉTAT` (`5d46ac87…`, `R-5218`).
  - Additif de commit brouillon 2 validé `CONFORME EN L'ÉTAT` par `e94bd12b…` : `docs/notes/sondes-v2-effectifs-et-correspondance-v1/diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md` (`958bb6a2f4c708b86958f5f6dcc1e9bb8af32021bf1a00b6398a588aab1fb01b`).
  - Entropie racine (`R-5056`) : `305159624078239919914131004197200342142`.
  - Effectifs et devis : `TA_etalon = 80` (`40 × 2`, `52` cases, `extension_taches_actions = false`, opt. A : `184,7 h` CPU, `3,85 h` sur `ccx63`, `6,70 USD`) + `TA_rejeu = 640` (`64 × 10`, `D = 4`, contrôle du chemin `contrôle absent`, opt. C `--nul 39` : `1 056,0 h` CPU, `22,00 h` sur `ccx63`, `38,34 USD`) = **`45,05 USD` attendus en `25,85 h`** (coupure dure interne `31h30`, externe `32 h` ou `60 USD` ; repli automatique sur `--mode etalon` seul `~6,70 USD` sur `ccx33` si refus de quota 48 vCPU).

---

## 1. Ordre exact des préalables et commandes de scellement (avant création de machine)

### 1.1 Verser les pièces `v2` vérifiées sur `main` (règle numéro 12 : les pièces `v1` restent intactes)

```bash
export PYTHONDONTWRITEBYTECODE=1
REPO="/home/antigravity/lciric/controle-ia-travail"
SCRATCH_V2="/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lancement-sondes-v2-hetzner-v2"
DEST="$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1"

for f in \
  remplir_additif_commit_sondes_v2_v2.py \
  amorce-hetzner-sondes-v2-ccx63-v2.sh \
  test_amorce_hetzner_r5_v2.py \
  checklist-et-commandes-lancement-hetzner-ccx63-v2.md; do
  cp "$SCRATCH_V2/$f" "$DEST/"
  cp "$SCRATCH_V2/$f.sha256" "$DEST/"
done
(cd "$DEST" && sha256sum -c \
  remplir_additif_commit_sondes_v2_v2.py.sha256 \
  amorce-hetzner-sondes-v2-ccx63-v2.sh.sha256 \
  test_amorce_hetzner_r5_v2.py.sha256 \
  checklist-et-commandes-lancement-hetzner-ccx63-v2.md.sha256)
```

### 1.2 Remplir et sceller mécaniquement l'additif officiel `prereg/diagnostics-prealables-sondes-v1-additif-commit-v1.md`

Conforme à `GO-2026-11-23-36` et `R-5209` point 2 (`--mode-correspondance jonction_tardive_ulterieure`) : la table `correspondance-rejeu-croise-v2.json` sera jointe par pièce jointe ultérieure contre-lue en classe B avant toute ouverture des données réelles, sans bloquer le scellement de l'additif ni le lancement de `ccx63`. Les chemins `--rapport-contre-lecture` et `--chemin-rapport-contre-lecture-depot` sont strictement alignés sur `contre-lecture-r2-additif-commit-et-checklist-hetzner-v1.md` (`e94bd12b…`).

```bash
export PYTHONDONTWRITEBYTECODE=1
REPO="/home/antigravity/lciric/controle-ia-travail"
WT="/home/antigravity/worktrees/sondes-v2-code"
PY="$REPO/.venv/bin/python3"
DATE_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

PYTHONPATH="$WT/src" "$PY" -B \
  "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/remplir_additif_commit_sondes_v2_v2.py" \
  --brouillon "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md" \
  --sortie "$REPO/prereg/diagnostics-prealables-sondes-v1-additif-commit-v1.md" \
  --note-effectifs "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md" \
  --chemin-note-depot "docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md" \
  --attendu-sha256-note "7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5" \
  --attendu-doses-d 4 \
  --date-scellement-utc "$DATE_UTC" \
  --option-rejeux-nuls 39 \
  --mode-correspondance jonction_tardive_ulterieure \
  --go-correspondance "GO-2026-11-23-36" \
  --rapport-contre-lecture "$REPO/docs/notes/sondes-v2-effectifs-et-correspondance-v1/contre-lecture-r2-additif-commit-et-checklist-hetzner-v1.md" \
  --chemin-rapport-contre-lecture-depot "docs/notes/sondes-v2-effectifs-et-correspondance-v1/contre-lecture-r2-additif-commit-et-checklist-hetzner-v1.md" \
  --verdict-contre-lecture "brouillon2.md CONFORME EN L'ÉTAT ; 4 corrections fermées appliquées et éprouvées R5 en v2 (remplir_additif_commit_sondes_v2_v2.py 4cc2a17a…, amorce-hetzner-sondes-v2-ccx63-v2.sh fdbc193d…)."

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
git -C /home/antigravity/worktrees/sondes-v2-code status --porcelain
git -C /home/antigravity/worktrees/sondes-v2-code rev-parse HEAD origin/sondes-v2/code-v2
# Committer et pousser l'additif scellé (+ .sha256), la ligne d'engagement FEU et la décision R-xxxx sur main
```

---

## 2. Ligne d'engagement `FEU` prête à coller dans `registres/depenses.md` (avant création du serveur)

À insérer dans `registres/depenses.md` (section `## Engagements avant création d'instance`) **avant** tout appel `POST /v1/servers` sur l'API Hetzner :

```markdown
| <DATE_UTC_FEU> | GO-2026-11-24-02 | FEU — engagement épreuve à vérité plantée des sondes boîte blanche v2 (`programme_monde_plante_v4.py`, commit figé `0ce9e35110d93dd916e85b1191a2613b101e772d` sur `origin/sondes-v2/code-v2`, vérités v4 `b310e1af…`, note des effectifs `7338a3dc…` conforme `5d46ac87…`, additif scellé `<SHA256_ADDITIF_SCELLE>`, amorce v2 `fdbc193d…` éprouvée R5, entropie racine `R-5056` `305159624078239919914131004197200342142`) : serveur dédié Hetzner `ccx63` (48 cœurs dédiés) à `hel1`, prix relu par API `1,3942 EUR/h` brut (`1,74275 USD/h` au taux `1,25`), `0` serveur actif avant création ; mode `etalon` option A (`52` cases, `TA_etalon = 80`, attendu `6,70 USD` / `3,85 h`) + mode `complet` option C (`--nul 39`, `TA_rejeu = 640`, `D = 4`, contrôle du chemin absent, attendu `38,34 USD` / `22,00 h`) = **`45,05 USD` attendus en `25,85 h`** (`64,40 USD` au lieu max) ; repli automatique sur `--mode etalon` seul (`~6,70 USD` sur `ccx33`) en cas de refus de quota 48 vCPU ; branche de sortie `calcul/sondes-v2-epreuve-plantee-v4` ; coupure dure et destruction `R10` par identifiant numérique à **`31h30`** interne (`113400 s`) et **`32 h`** (`≈ 55,77 USD`) ou **`60 USD`** externe (démon persistant), après rapatriement prouvé par `git ls-remote` | 68 USD (plafond ; alerte 54,4 USD ; coupure dure 60 USD / 32 h) | R-<NUMERO_DECISION> |
```

---

## 3. Lancement Hetzner `ccx63` (`hel1`, injection `base64` de `amorce-hetzner-sondes-v2-ccx63-v2.sh` vérifiée par SHA-256)

> **Sécurité & intégrité `v2`** : le script distant `/opt/run_epreuve_sondes_v2.sh` est injecté en `base64` directement depuis `amorce-hetzner-sondes-v2-ccx63-v2.sh` après vérification de son empreinte `fdbc193d2c2372e0903238a9e75900a9180e6cf152bb33a3180e4cfc50088f0b` (aucune interpolation shell fragile). Le jeton GitHub n'apparaît jamais dans `REPO_URL` ni dans `.git/config` (`GIT_ASKPASS` `0700` + filtre `sed` + contrôle `grep` avant `git push`).

### 3.1 Script de lancement (à exécuter sur la devbox mère après le `FEU`)

```bash
#!/usr/bin/env bash
# Lancer UNIQUEMENT après : (1) additif scellé et poussé, (2) ligne FEU inscrite dans registres/depenses.md.
set -euo pipefail
set +x
export PYTHONDONTWRITEBYTECODE=1

source /home/antigravity/env-setup.sh
: "${HCLOUD_TOKEN:?HCLOUD_TOKEN absent}"
GITHUB_PUSH_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_2:-${CONTROLE_IA_GITHUB_TOKEN_3:-}}"
: "${GITHUB_PUSH_TOKEN:?CONTROLE_IA_GITHUB_TOKEN_2/3 absent}"

API="https://api.hetzner.cloud/v1"
AUTH=(-H "Authorization: Bearer ${HCLOUD_TOKEN}" -H "Content-Type: application/json")

AMORCE_SH="/home/antigravity/lciric/controle-ia-travail/docs/notes/sondes-v2-effectifs-et-correspondance-v1/amorce-hetzner-sondes-v2-ccx63-v2.sh"
SHA_AMORCE="fdbc193d2c2372e0903238a9e75900a9180e6cf152bb33a3180e4cfc50088f0b"
echo "$SHA_AMORCE  $AMORCE_SH" | sha256sum -c -
AMORCE_B64="$(base64 -w 0 "$AMORCE_SH")"

COMMIT_CODE="0ce9e35110d93dd916e85b1191a2613b101e772d"
ENTROPIE="305159624078239919914131004197200342142"
SHA_VERITES="b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533"
SHA_NOTE="7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5"
BRANCHE_SORTIE="calcul/sondes-v2-epreuve-plantee-v4"
LOCATION="hel1"
ETAT_DIR="/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lancement-sondes-v2-hetzner-v2/run-etat"
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

# 2. Générateur cloud-init (injecte amorce-hetzner-sondes-v2-ccx63-v2.sh en base64 sans altération)
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
    encoding: b64
    content: ${AMORCE_B64}
  - path: /root/.hcloud_token
    permissions: '0600'
    content: "${HCLOUD_TOKEN}"
  - path: /root/.gh_token
    permissions: '0600'
    content: "${GITHUB_PUSH_TOKEN}"
runcmd:
  - [ env, "MODE_RUN=${mode_run}", "COMMIT_CODE=${COMMIT_CODE}", "ENTROPIE=${ENTROPIE}", "SHA_VERITES=${SHA_VERITES}", "SHA_NOTE=${SHA_NOTE}", "BRANCHE_SORTIE=${BRANCHE_SORTIE}", "WATCHDOG_SECONDES=113400", bash, /opt/run_epreuve_sondes_v2.sh ]
EOF
}

# 3. Création ccx63 à hel1 avec repli automatique sur etalon seul (ccx33) si refus de quota 48 vCPU
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
```

### 3.2 Watchdog externe `R10` (à lancer immédiatement après création en démon persistant `IsDaemon: true`)

> **Note opérationnelle (`e94bd12b…`)** : lancer cette commande avec `run_command(..., IsDaemon: true)` sur la devbox mère afin que le watchdog persiste entre les tours (en plus de la minuterie interne `31h30` portée par `amorce-hetzner-sondes-v2-ccx63-v2.sh`).

```bash
set -euo pipefail
set +x
source /home/antigravity/env-setup.sh
ETAT_DIR="/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lancement-sondes-v2-hetzner-v2/run-etat"
API="https://api.hetzner.cloud/v1"
SERVER_ID="$(jq -r '.server_id' "$ETAT_DIR/serveur-actif.json")"
T0="$(jq -r '.created_epoch' "$ETAT_DIR/serveur-actif.json")"
PRIX_EUR="$(jq -r '.price_eur_h_gross' "$ETAT_DIR/serveur-actif.json")"
MAX_H=32
MAX_USD=60

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
usd = h * float('$PRIX_EUR') * 1.25
print(1 if (h >= float('$MAX_H') or usd >= float('$MAX_USD')) else 0)
")"
  if [ "$OVER" = "1" ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) R10 CAP ATTEINT -> DELETE /v1/servers/$SERVER_ID"
    curl -fsS -X DELETE -H "Authorization: Bearer ${HCLOUD_TOKEN}" "$API/servers/$SERVER_ID" || true
    exit 0
  fi
done
```

---

## 4. Résultats des essais `R5` locaux vérifiés en `v2` (`2026-11-24`)

1. **`remplir_additif_commit_sondes_v2_v2.py` (`4cc2a17a…`)** sur `brouillon2.md` (`958bb6a2…`) + `note-des-effectifs-sondes-v2-v1.md` (`7338a3dc…`, `D = 4`, `contrôle absent`) + `contre-lecture-r2-additif-commit-et-checklist-hetzner-v1.md` (`e94bd12b…`) avec `--mode-correspondance jonction_tardive_ulterieure --go-correspondance GO-2026-11-23-36` :
   - `controle_ia.prereg.problemes` = **`[]`** ; `prereg.exiger_prereg_scelle` validé ;
   - gardes négatives vérifiées : refus sans `--go-correspondance` (`rc=1`) et refus si `--fichier-correspondance` est fourni (`rc=1`).
2. **`test_amorce_hetzner_r5_v2.py` (`7600f90f…`)** exécutant le vrai script `amorce-hetzner-sondes-v2-ccx63-v2.sh` (`fdbc193d…`) sur dépôt git bare local `/tmp/test-hetzner-r5/` + faux serveur API Hetzner local :
   - `bash -n amorce-hetzner-sondes-v2-ccx63-v2.sh` : `rc=0`.
   - **Scénario A** (petites sorties `<= 90 Mo` + injection volontaire de `ghp_TESTSECRET123` et `hc_TESTHCLOUD_987654` sur stderr) : `sha256sum -c` = `100 % OK`, `0` fuite dans `$LOG` poussé, dans tout le commit poussé et dans `.git/config`, `DELETE /v1/servers/99887766` reçu (`OK`).
   - **Scénario B** (archive simulée `> 90 Mo` découpée en `4` morceaux `.part.*`) : `sha256sum -c` = `100 % OK` (zéro `.sha256` orphelin), réassemblage des `4` morceaux identique à l'octet au manifeste `journaux-gels-complet.tar.gz.manifeste.sha256.txt`, `0` fuite, `DELETE /v1/servers/99887766` reçu (`OK`).
   - **Scénario C** (minuterie interne `R10` à `WATCHDOG_SECONDES=3` sur calcul bloqué `60 s`) : interruption en `4,6 s` (`rc=124`), rapatriement partiel `partiel-plafond-r10` avec `100 %` des `.sha256` valides et `0` fuite, puis `DELETE /v1/servers/99887766` reçu (`OK`).
   - **Scénario D** (garde sécurité sur `REPO_URL` contenant un jeton) : rejet immédiat (`rc=1`, `ARRÊT SÉCURITÉ`).
   - Nettoyage complet de `/tmp/test-hetzner-r5/` vérifié.
3. **Intégrité finale des dépôts** : `git status --porcelain` vide sur `/home/antigravity/lciric/controle-ia-travail` et `/home/antigravity/worktrees/sondes-v2-code`.
