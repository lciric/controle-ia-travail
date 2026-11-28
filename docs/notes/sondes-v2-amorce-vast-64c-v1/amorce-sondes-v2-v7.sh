#!/usr/bin/env bash
# Script autonome d'amorce multi-hébergeur (Vast.ai 64+ cœurs / Hetzner) — version 3
# Épreuve à vérité plantée des sondes boîte blanche v2 — GO-2026-11-24-02 / GO-2026-11-24-15
# Conserve 100 % des gardes de sécurité R2/R5/R10/R12 de la v2 (fdbc193d…) et apporte :
#   1. Résolution CPU_DISPO (`nproc --all`) et N_WORKERS AVANT `export OMP_NUM_THREADS=1` + garde EXIGER_MULTICOEUR.
#   2. `xargs -P ... -I {}` sans `-n 1` (supprime l'avertissement GNU xargs `--max-args` vs `-I`).
#   3. Reprise exacte de `etalon` sur `[130, 500)` par pas paramétrable (`PAS_ETALON=6` par défaut : 61 tranches de 6
#      + 1 dernière tranche bornée à 500 `[496, 500)` = 62 tranches en UNE SEULE VAGUE sur 64 cœurs), après extraction
#      et vérification `.sha256` à l'octet des 13 tranches `[0, 130)` depuis `calcul/sondes-v2-epreuve-plantee-v4`
#      (`38c6f4a7054b14b56be7b357c08db8bf11931ca2`), puis fusion officielle des 75 rapports via `ecrire_synthese_fusionnee`.
#   4. En `MODE_RUN=etalon_suite_et_sonde_complet_1rep`, exécution en tâche de fond parallèle sur le 63e cœur
#      lorsqu'`N_WORKERS >= 63` (`wait` propre des deux avant `pousser_sorties`).
#   5. Branche de sortie dédiée non destructive (`calcul/sondes-v2-epreuve-plantee-v4-suite`), interdisant `main`
#      et `calcul/sondes-v2-epreuve-plantee-v4` (R12).
#   6. Compatibilité native conteneur Vast.ai (`onstart-cmd` : écriture `0600` depuis `GH_TOKEN_ENV`/`VAST_API_KEY_ENV`
#      puis `unset` intégral des variables d'environnement secrètes ; `apt-get` auto pour `git`, `curl`,
#      `ca-certificates`, `procps`, `time` ; autodestruction R10 par `VAST_INSTANCE_ID` ou fallback `CONTAINER_ID`
#      strictement numérique hors liste noire `58936096|58936099|58936100|60988826|62498862`).
set -euo pipefail
set +x

export PYTHONDONTWRITEBYTECODE=1

# Garde R5 multicœur : résoudre CPU_DISPO et N_WORKERS AVANT export OMP_NUM_THREADS=1
# (sous GNU coreutils, `nproc` sans `--all` respecte OMP_NUM_THREADS et renverrait 1 !)
CPU_DISPO="$(nproc --all 2>/dev/null || getconf _NPROCESSORS_ONLN || echo 1)"
CPU_DISPO="$(printf '%s' "$CPU_DISPO" | tr -d '[:space:]')"
if ! [[ "$CPU_DISPO" =~ ^[0-9]+$ ]] || [ "$CPU_DISPO" -lt 1 ]; then
  CPU_DISPO=1
fi
N_WORKERS="${N_WORKERS:-$CPU_DISPO}"
EXIGER_MULTICOEUR="${EXIGER_MULTICOEUR:-1}"

export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1

MODE_RUN="${MODE_RUN:-etalon_suite_seul}"
COMMIT_CODE="${COMMIT_CODE:-0ce9e35110d93dd916e85b1191a2613b101e772d}"
ENTROPIE="${ENTROPIE:-305159624078239919914131004197200342142}"
SHA_VERITES="${SHA_VERITES:-b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533}"
SHA_NOTE="${SHA_NOTE:-7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5}"
BRANCHE_CODE="${BRANCHE_CODE:-sondes-v2/code-v2}"
BRANCHE_AMONT_ETALON="${BRANCHE_AMONT_ETALON:-calcul/sondes-v2-epreuve-plantee-v4}"
COMMIT_AMONT_ETALON="${COMMIT_AMONT_ETALON:-38c6f4a7054b14b56be7b357c08db8bf11931ca2}"
BRANCHE_SORTIE="${BRANCHE_SORTIE:-calcul/sondes-v2-epreuve-plantee-v4-suite}"
REPO_URL="${REPO_URL:-https://github.com/lciric/controle-ia-travail.git}"

ETALON_AMONT_PAS="${ETALON_AMONT_PAS:-10}"
ETALON_DE="${ETALON_DE:-130}"
ETALON_A="${ETALON_A:-500}"
PAS_ETALON="${PAS_ETALON:-6}"

COMPLET_DE="${COMPLET_DE:-0}"
COMPLET_A="${COMPLET_A:-500}"
PAS_COMPLET="${PAS_COMPLET:-5}"

FOURNISSEUR="${FOURNISSEUR:-auto}"
HCLOUD_API="${HCLOUD_API:-https://api.hetzner.cloud/v1}"
METADATA_URL="${METADATA_URL:-http://169.254.169.254/hetzner/v1/metadata/instance-id}"
HCLOUD_TOKEN_FILE="${HCLOUD_TOKEN_FILE:-/root/.hcloud_token}"
SERVER_ID="${SERVER_ID:-}"

VAST_API_URL="${VAST_API_URL:-https://console.vast.ai/api/v0}"
VAST_API_KEY_FILE="${VAST_API_KEY_FILE:-/root/.vast_api_key}"
VAST_INSTANCE_ID="${VAST_INSTANCE_ID:-}"

GH_TOKEN_FILE="${GH_TOKEN_FILE:-/root/.gh_token}"
WORK="${WORK:-/opt/sondes-v2}"
ENTREE="${ENTREE:-/opt/entree}"
SORTIE="${SORTIE:-/opt/sortie}"
LOG="${LOG:-/var/log/epreuve-sondes-v2.log}"
WATCHDOG_SECONDES="${WATCHDOG_SECONDES:-20700}"
SEUIL_ARCHIVE_OCTETS="${SEUIL_ARCHIVE_OCTETS:-94371840}"
TAILLE_MORCEAU="${TAILLE_MORCEAU:-45m}"
SKIP_ENV_INSTALL="${SKIP_ENV_INSTALL:-0}"
PY_BIN="${PY_BIN:-}"
SIMULER_MODE_CMD="${SIMULER_MODE_CMD:-}"

# Capture immédiate des jetons éventuellement transmis par variables d'environnement Vast.ai (onstart-cmd)
# puis purge immédiate de l'environnement exporté pour qu'aucun processus fils ne puisse les lire.
_INIT_GH_TOK="${GH_TOKEN_ENV:-${GH_TOKEN:-${GITHUB_TOKEN:-}}}"
_INIT_VAST_KEY="${VAST_API_KEY_ENV:-${VAST_API_KEY:-}}"
_INIT_HCLOUD_TOK="${HCLOUD_TOKEN_ENV:-${HCLOUD_TOKEN:-}}"
unset GH_TOKEN_ENV VAST_API_KEY_ENV HCLOUD_TOKEN_ENV GITHUB_TOKEN GH_TOKEN VAST_API_KEY HCLOUD_TOKEN GH_TOK

# Liste noire fermée des instances Vast.ai intouchables (aucun appel DELETE autorisé, jamais)
VAST_INSTANCES_INTOUCHABLES=("58936096" "58936099" "58936100" "60988826" "62498862")

est_dans_liste_noire_vast() {
  local cand="${1:-}"
  case "$cand" in
    58936096|58936099|58936100|60988826|62498862)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

verifier_vast_instance_id_autorise() {
  local vid="${1:-}"
  if ! [[ "$vid" =~ ^[1-9][0-9]*$ ]]; then
    echo "ARRÊT SÉCURITÉ R10 VAST : identifiant Vast '${vid}' invalide (doit être composé exclusivement de chiffres, sans zéro initial)." >&2
    return 1
  fi
  if est_dans_liste_noire_vast "$vid"; then
    echo "ARRÊT SÉCURITÉ R10 VAST : identifiant Vast '${vid}' interdit (liste noire des instances intouchables) !" >&2
    return 1
  fi
  return 0
}

# Garde R5 : validation N_WORKERS et exigence multicœur avant tout calcul
if ! [[ "$N_WORKERS" =~ ^[1-9][0-9]*$ ]]; then
  echo "ARRÊT GARDE R5 : N_WORKERS='${N_WORKERS}' invalide (entier >= 1 attendu)." >&2
  exit 1
fi
if [ "$EXIGER_MULTICOEUR" = "1" ] && [ "$N_WORKERS" -lt 2 ]; then
  echo "ARRÊT GARDE R5 MULTICŒUR : EXIGER_MULTICOEUR=1 mais N_WORKERS=$N_WORKERS (< 2, CPU_DISPO=$CPU_DISPO)." >&2
  exit 1
fi
MIN_WORKERS="${MIN_WORKERS:-2}"
if ! [[ "$MIN_WORKERS" =~ ^[1-9][0-9]*$ ]] || { [ "$EXIGER_MULTICOEUR" = "1" ] && [ "$N_WORKERS" -lt "$MIN_WORKERS" ]; }; then
  echo "ARRÊT GARDE R5 MULTICŒUR : N_WORKERS=$N_WORKERS < MIN_WORKERS=$MIN_WORKERS (CPU_DISPO=$CPU_DISPO)." >&2
  exit 1
fi

# Garde sécurité : jamais de jeton intégré dans REPO_URL
case "$REPO_URL" in
  *"@"*|*"x-access-token"*)
    echo "ARRÊT SÉCURITÉ : REPO_URL ne doit jamais contenir de jeton ou d'identifiants." >&2
    exit 1
    ;;
esac

# Garde R12 : interdiction absolue d'écraser main, le code ou la branche amont calcul/sondes-v2-epreuve-plantee-v4
if [ -z "$BRANCHE_SORTIE" ]; then
  echo "ARRÊT SÉCURITÉ R12 : BRANCHE_SORTIE vide interdite." >&2
  exit 1
fi
case "$BRANCHE_SORTIE" in
  main|master|HEAD|calcul/sondes-v2-epreuve-plantee-v4|"$BRANCHE_CODE"|"$BRANCHE_AMONT_ETALON")
    echo "ARRÊT SÉCURITÉ R12 : BRANCHE_SORTIE='$BRANCHE_SORTIE' interdite (ne jamais écraser main ni calcul/sondes-v2-epreuve-plantee-v4)." >&2
    exit 1
    ;;
esac

# Validation stricte du mode d'exécution
case "$MODE_RUN" in
  etalon_suite_seul|etalon_suite_et_sonde_complet_1rep|etalon_suite_et_complet|complet_tranche_seul)
    ;;
  *)
    echo "ARRÊT SÉCURITÉ : MODE_RUN='$MODE_RUN' inconnu (attendu : etalon_suite_seul | etalon_suite_et_sonde_complet_1rep | etalon_suite_et_complet | complet_tranche_seul)." >&2
    exit 1
    ;;
esac

# Validation stricte du fournisseur et résolution sécurisée de TARGET_VAST_ID (VAST_INSTANCE_ID ou fallback CONTAINER_ID)
case "$FOURNISSEUR" in
  auto|hetzner|vast|aucun)
    ;;
  *)
    echo "ARRÊT SÉCURITÉ : FOURNISSEUR='$FOURNISSEUR' inconnu (attendu : auto | hetzner | vast | aucun)." >&2
    exit 1
    ;;
esac

TARGET_VAST_ID=""
if [ -n "$VAST_INSTANCE_ID" ]; then
  verifier_vast_instance_id_autorise "$VAST_INSTANCE_ID" || exit 1
  TARGET_VAST_ID="$VAST_INSTANCE_ID"
elif [ -n "${CONTAINER_ID:-}" ]; then
  if est_dans_liste_noire_vast "${CONTAINER_ID}"; then
    echo "ARRÊT SÉCURITÉ R10 VAST : CONTAINER_ID='${CONTAINER_ID}' appartient à la liste noire des instances intouchables !" >&2
    exit 1
  fi
  if [[ "${CONTAINER_ID}" =~ ^[1-9][0-9]*$ ]]; then
    TARGET_VAST_ID="${CONTAINER_ID}"
  fi
fi
if [ "$FOURNISSEUR" = "vast" ] && [ -z "$TARGET_VAST_ID" ]; then
  echo "ARRÊT SÉCURITÉ R10 VAST : FOURNISSEUR=vast exige VAST_INSTANCE_ID (ou CONTAINER_ID) strictement numérique et hors liste noire." >&2
  exit 1
fi

# Validation des bornes numériques de plages
for var_num in ETALON_AMONT_PAS ETALON_DE ETALON_A PAS_ETALON COMPLET_DE COMPLET_A PAS_COMPLET WATCHDOG_SECONDES; do
  if ! [[ "${!var_num}" =~ ^[0-9]+$ ]]; then
    echo "ARRÊT PARAMÈTRE : ${var_num}='${!var_num}' doit être un entier >= 0." >&2
    exit 1
  fi
done
if [ "$PAS_ETALON" -lt 1 ] || [ "$ETALON_AMONT_PAS" -lt 1 ] || [ "$PAS_COMPLET" -lt 1 ]; then
  echo "ARRÊT PARAMÈTRE : les pas de tranche doivent être >= 1." >&2
  exit 1
fi
if [ "$ETALON_DE" -gt "$ETALON_A" ] || [ "$ETALON_A" -gt 500 ] || [ $((ETALON_DE % ETALON_AMONT_PAS)) -ne 0 ]; then
  echo "ARRÊT PARAMÈTRE : plage étalon invalide (ETALON_DE=$ETALON_DE, ETALON_A=$ETALON_A, ETALON_AMONT_PAS=$ETALON_AMONT_PAS)." >&2
  exit 1
fi
if [ "$COMPLET_DE" -ge "$COMPLET_A" ] || [ "$COMPLET_A" -gt 500 ]; then
  echo "ARRÊT PARAMÈTRE : plage complet invalide (COMPLET_DE=$COMPLET_DE, COMPLET_A=$COMPLET_A)." >&2
  exit 1
fi

mkdir -p "$WORK" "$ENTREE" "$SORTIE/etalon" "$SORTIE/complet" "$(dirname "$LOG")"
if [ -f "$WORK/.amorce_deja_lancee" ]; then
  exec >> "$LOG" 2>&1
  echo "=== REDÉMARRAGE CONTENEUR DÉTECTÉ (R12) $(date -u +%Y-%m-%dT%H:%M:%SZ) : refus de relance, redemande R10 ==="
  if [ -f "$VAST_API_KEY_FILE" ] && [ -s "$VAST_API_KEY_FILE" ] && verifier_vast_instance_id_autorise "${TARGET_VAST_ID:-}"; then
    _VK_R12="$(tr -d '\r\n' < "$VAST_API_KEY_FILE")"
    curl -fsS --max-time 20 -X DELETE -H "Authorization: Bearer ${_VK_R12}" "${VAST_API_URL%/}/instances/${TARGET_VAST_ID}/" || true
  fi
  exit 0
fi
: > "$LOG"
exec > >(tee -a "$LOG") 2>&1
touch "$WORK/.amorce_deja_lancee"

# Écriture immédiate en fichiers 0600 des jetons reçus au démarrage (Vast.ai onstart-cmd), puis effacement mémoire
if [ -n "$_INIT_GH_TOK" ]; then
  (
    umask 077
    mkdir -p "$(dirname "$GH_TOKEN_FILE")"
    printf '%s\n' "$_INIT_GH_TOK" | tr -d '\r' > "$GH_TOKEN_FILE"
    chmod 0600 "$GH_TOKEN_FILE"
  )
fi
if [ -n "$_INIT_VAST_KEY" ]; then
  (
    umask 077
    mkdir -p "$(dirname "$VAST_API_KEY_FILE")"
    printf '%s\n' "$_INIT_VAST_KEY" | tr -d '\r' > "$VAST_API_KEY_FILE"
    chmod 0600 "$VAST_API_KEY_FILE"
  )
fi
if [ -n "$_INIT_HCLOUD_TOK" ]; then
  (
    umask 077
    mkdir -p "$(dirname "$HCLOUD_TOKEN_FILE")"
    printf '%s\n' "$_INIT_HCLOUD_TOK" | tr -d '\r' > "$HCLOUD_TOKEN_FILE"
    chmod 0600 "$HCLOUD_TOKEN_FILE"
  )
fi
unset _INIT_GH_TOK _INIT_VAST_KEY _INIT_HCLOUD_TOK

# Installation automatique sur conteneur minimal (ex. python:3.12-bookworm / ubuntu:24.04) si outils absents
installer_outils_systeme_si_absents() {
  if [ "$SKIP_ENV_INSTALL" = "1" ]; then
    return 0
  fi
  local manque=0
  command -v git >/dev/null 2>&1 || manque=1
  command -v curl >/dev/null 2>&1 || manque=1
  command -v pgrep >/dev/null 2>&1 || manque=1
  command -v pkill >/dev/null 2>&1 || manque=1
  command -v tar >/dev/null 2>&1 || manque=1
  command -v gzip >/dev/null 2>&1 || manque=1
  [ -x /usr/bin/time ] || manque=1
  [ -f /etc/ssl/certs/ca-certificates.crt ] || manque=1
  if [ "$manque" -eq 1 ] && command -v apt-get >/dev/null 2>&1; then
    echo ">>> Installation apt-get des paquets système requis (git, curl, ca-certificates, procps, time, tar, gzip)..."
    DEBIAN_FRONTEND=noninteractive apt-get update -qq
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      git curl ca-certificates procps time tar gzip
  fi
}
installer_outils_systeme_si_absents

# Script GIT_ASKPASS (0700) : lit GH_TOKEN_FILE à la volée, jamais de jeton dans REPO_URL ni .git/config ni env fils
ASKPASS_SCRIPT="$WORK/.git-askpass.sh"
cat > "$ASKPASS_SCRIPT" <<'ASKPASS_EOF'
#!/usr/bin/env bash
set -euo pipefail
case "${1:-}" in
  *Username*|*username*) printf '%s\n' "x-access-token" ;;
  *Password*|*password*) tr -d '\r\n' < "${GH_TOKEN_FILE}"; printf '\n' ;;
  *) printf '\n' ;;
esac
ASKPASS_EOF
chmod 0700 "$ASKPASS_SCRIPT"
export GIT_ASKPASS="$ASKPASS_SCRIPT"
export GIT_TERMINAL_PROMPT=0
export GH_TOKEN_FILE

# Résolution de l'hébergeur effectif pour l'autodestruction R10
FOURNISSEUR_EFFECTIF="aucun"
if [ "$FOURNISSEUR" = "vast" ]; then
  FOURNISSEUR_EFFECTIF="vast"
elif [ "$FOURNISSEUR" = "hetzner" ]; then
  if [ -z "$SERVER_ID" ]; then
    SERVER_ID="$(curl -fsS --max-time 10 "$METADATA_URL" 2>/dev/null | tr -d '\r\n[:space:]' || true)"
  fi
  FOURNISSEUR_EFFECTIF="hetzner"
elif [ "$FOURNISSEUR" = "auto" ]; then
  if [ -f "$VAST_API_KEY_FILE" ] && [ -s "$VAST_API_KEY_FILE" ] && [ -n "$TARGET_VAST_ID" ]; then
    FOURNISSEUR_EFFECTIF="vast"
  else
    if [ -z "$SERVER_ID" ]; then
      SERVER_ID="$(curl -fsS --max-time 10 "$METADATA_URL" 2>/dev/null | tr -d '\r\n[:space:]' || true)"
    fi
    if [ -f "$HCLOUD_TOKEN_FILE" ] && [ -s "$HCLOUD_TOKEN_FILE" ] && [[ "${SERVER_ID:-}" =~ ^[1-9][0-9]*$ ]]; then
      FOURNISSEUR_EFFECTIF="hetzner"
    fi
  fi
fi

echo "=== DÉBUT $(date -u +%Y-%m-%dT%H:%M:%SZ) | mode=$MODE_RUN | cpu_dispo=$CPU_DISPO | n_workers=$N_WORKERS | pas_etalon=$PAS_ETALON | fournisseur=$FOURNISSEUR_EFFECTIF | branche_sortie=$BRANCHE_SORTIE | watchdog=${WATCHDOG_SECONDES}s ==="
if [ "$FOURNISSEUR_EFFECTIF" = "hetzner" ]; then
  echo "SERVER_ID=${SERVER_ID:-inconnu}"
elif [ "$FOURNISSEUR_EFFECTIF" = "vast" ]; then
  echo "TARGET_VAST_ID=${TARGET_VAST_ID:-inconnu}"
fi

WATCHDOG_PID=""
ACTIVE_CHILD_PID=""
TIMEOUT_DECLENCHE=0
DEJA_DETRUIT=0
RAPATRIEMENT_FINAL_FAIT=0

arreter_watchdog() {
  if [ -n "${WATCHDOG_PID:-}" ]; then
    kill -TERM "$WATCHDOG_PID" 2>/dev/null || true
    wait "$WATCHDOG_PID" 2>/dev/null || true
    WATCHDOG_PID=""
  fi
}

tuer_arbre_pid() {
  local pid="$1"
  local sig="${2:-TERM}"
  local enfants
  enfants="$(pgrep -P "$pid" 2>/dev/null || true)"
  local c
  for c in $enfants; do
    tuer_arbre_pid "$c" "$sig"
  done
  pkill -"$sig" -P "$pid" 2>/dev/null || true
  kill -"$sig" "$pid" 2>/dev/null || true
}

tuer_fils_actif() {
  if [ -n "${ACTIVE_CHILD_PID:-}" ]; then
    tuer_arbre_pid "$ACTIVE_CHILD_PID" TERM
    sleep 1
    tuer_arbre_pid "$ACTIVE_CHILD_PID" KILL
    wait "$ACTIVE_CHILD_PID" 2>/dev/null || true
    ACTIVE_CHILD_PID=""
  fi
}

echapper_sed_ere() {
  printf '%s' "$1" | sed -e 's/[\/&.^$*+?()[\]{}|\\]/\\&/g'
}

filtrer_secrets_log() {
  local src="$1"
  local dst="$2"
  local gh_tok="" hc_tok="" vast_key=""
  local esc_gh="" esc_hc="" esc_vast=""
  if [ -f "$GH_TOKEN_FILE" ]; then
    gh_tok="$(tr -d '\r\n' < "$GH_TOKEN_FILE")"
  fi
  if [ -f "$HCLOUD_TOKEN_FILE" ]; then
    hc_tok="$(tr -d '\r\n' < "$HCLOUD_TOKEN_FILE")"
  fi
  if [ -f "$VAST_API_KEY_FILE" ]; then
    vast_key="$(tr -d '\r\n' < "$VAST_API_KEY_FILE")"
  fi
  if [ -n "$gh_tok" ]; then
    esc_gh="$(echapper_sed_ere "$gh_tok")"
  fi
  if [ -n "$hc_tok" ]; then
    esc_hc="$(echapper_sed_ere "$hc_tok")"
  fi
  if [ -n "$vast_key" ]; then
    esc_vast="$(echapper_sed_ere "$vast_key")"
  fi
  local sed_args=(-E)
  if [ -n "$esc_gh" ]; then
    sed_args+=(-e "s|${esc_gh}|[MASQUE_GH]|g")
  fi
  if [ -n "$esc_hc" ]; then
    sed_args+=(-e "s|${esc_hc}|[MASQUE_HCLOUD]|g")
  fi
  if [ -n "$esc_vast" ]; then
    sed_args+=(-e "s|${esc_vast}|[MASQUE_VAST]|g")
  fi
  sed_args+=(
    -e 's/gh[pousr]_[A-Za-z0-9_]+/[MASQUE_GH]/g'
    -e 's/github_pat_[A-Za-z0-9_]+/[MASQUE_GH]/g'
    -e 's/x-access-token:[^@[:space:]]+@/x-access-token:[MASQUE_GH]@/g'
  )
  sed "${sed_args[@]}" "$src" > "$dst"
  if [ -n "$gh_tok" ] && grep -Fq -- "$gh_tok" "$dst"; then
    echo "ERREUR SÉCURITÉ : jeton GitHub résiduel détecté dans le journal filtré" >&2
    rm -f "$dst"
    return 1
  fi
  if [ -n "$hc_tok" ] && grep -Fq -- "$hc_tok" "$dst"; then
    echo "ERREUR SÉCURITÉ : jeton Hetzner résiduel détecté dans le journal filtré" >&2
    rm -f "$dst"
    return 1
  fi
  if [ -n "$vast_key" ] && grep -Fq -- "$vast_key" "$dst"; then
    echo "ERREUR SÉCURITÉ : clé Vast.ai résiduelle détectée dans le journal filtré" >&2
    rm -f "$dst"
    return 1
  fi
}

# Fonction de rapatriement prouvé sur la branche dédiée (jamais main ni v4 amont, aucun fichier > 95 Mo, 100 % .sha256 valides)
pousser_sorties() {
  local etiquette="$1"
  local pub="$WORK/pub"
  rm -rf "$pub"
  git init "$pub"
  git -C "$pub" config core.autocrlf false
  git -C "$pub" config user.name "sondes-v2-runner-v3"
  git -C "$pub" config user.email "runner@controle-ia.local"
  git -C "$pub" checkout -B "$BRANCHE_SORTIE"
  mkdir -p "$pub/epreuve-plantee-v4/etalon" "$pub/epreuve-plantee-v4/complet"

  # Copier les synthèses fusionnées + rapports par plage + leurs .sha256
  for m in etalon complet; do
    if [ -d "$SORTIE/$m" ]; then
      cp -f "$SORTIE/$m"/synthese-fusionnee-*.json* "$pub/epreuve-plantee-v4/$m/" 2>/dev/null || true
      cp -f "$SORTIE/$m"/rapport-monde-plante-v4-*.json* "$pub/epreuve-plantee-v4/$m/" 2>/dev/null || true
    fi
  done

  # Copier la métadonnée de sonde 1 réplique (+ .sha256) si produite (sans polluer $SORTIE/complet)
  if [ -f "$SORTIE/sonde-complet-1rep-meta.json" ]; then
    cp -f "$SORTIE"/sonde-complet-1rep-meta.json* "$pub/epreuve-plantee-v4/"
  fi

  # Compresser les journaux des gels du mode complet sans jamais laisser de .sha256 orphelin dans $pub
  if compgen -G "$SORTIE/complet/journal-gels-*.jsonl" >/dev/null 2>&1; then
    (
      set -euo pipefail
      cd "$SORTIE/complet"
      shopt -s nullglob
      for f_sha in journal-gels-*.jsonl.sha256; do
        sha256sum -c "$f_sha"
      done
      sha256sum journal-gels-*.jsonl > journaux-gels.manifeste.sha256.txt
      sha256sum -c journaux-gels.manifeste.sha256.txt
    )
    cp -f "$SORTIE/complet/journaux-gels.manifeste.sha256.txt" "$pub/epreuve-plantee-v4/complet/"

    (
      set -euo pipefail
      cd "$SORTIE/complet"
      shopt -s nullglob
      fichiers_tar=(journal-gels-*.jsonl journal-gels-*.jsonl.sha256)
      tar -czf "$SORTIE/journaux-gels-complet.tar.gz" "${fichiers_tar[@]}"
    )

    TAILLE_OCTETS="$(stat -c %s "$SORTIE/journaux-gels-complet.tar.gz")"
    if [ "$TAILLE_OCTETS" -le "$SEUIL_ARCHIVE_OCTETS" ]; then
      cp -f "$SORTIE/journaux-gels-complet.tar.gz" "$pub/epreuve-plantee-v4/complet/"
      (
        cd "$pub/epreuve-plantee-v4/complet"
        sha256sum journaux-gels-complet.tar.gz > journaux-gels-complet.tar.gz.sha256
      )
    else
      (
        cd "$SORTIE"
        sha256sum journaux-gels-complet.tar.gz > "$pub/epreuve-plantee-v4/complet/journaux-gels-complet.tar.gz.manifeste.sha256.txt"
      )
      split -b "$TAILLE_MORCEAU" -d "$SORTIE/journaux-gels-complet.tar.gz" \
        "$pub/epreuve-plantee-v4/complet/journaux-gels-complet.tar.gz.part."
      (
        cd "$pub/epreuve-plantee-v4/complet"
        sha256sum journaux-gels-complet.tar.gz.part.* > journaux-gels-complet.parts.sha256
      )
    fi
  fi

  # Filtrer tout jeton éventuel avant copie de $LOG dans $pub
  sleep 0.2
  filtrer_secrets_log "$LOG" "$pub/epreuve-plantee-v4/journal-execution.log"

  # Contrôle strict d'intégrité : 100 % des *.sha256 dans $pub doivent passer avant git push
  (
    set -euo pipefail
    cd "$pub/epreuve-plantee-v4"
    find . -type f -name "*.sha256" -print0 \
      | xargs -0 -r -n1 bash -c 'set -euo pipefail; cd "$(dirname "$1")" && sha256sum -c "$(basename "$1")"' _
  )

  # Vérification anti-fuite globale sur tout $pub (contenu + .git/config) avant commit/push
  local gh_tok="" hc_tok="" vast_key=""
  if [ -f "$GH_TOKEN_FILE" ]; then
    gh_tok="$(tr -d '\r\n' < "$GH_TOKEN_FILE")"
  fi
  if [ -f "$HCLOUD_TOKEN_FILE" ]; then
    hc_tok="$(tr -d '\r\n' < "$HCLOUD_TOKEN_FILE")"
  fi
  if [ -f "$VAST_API_KEY_FILE" ]; then
    vast_key="$(tr -d '\r\n' < "$VAST_API_KEY_FILE")"
  fi
  if [ -n "$gh_tok" ] && { grep -RFq -- "$gh_tok" "$pub/epreuve-plantee-v4" || grep -Fq -- "$gh_tok" "$pub/.git/config"; }; then
    echo "ERREUR SÉCURITÉ : jeton GitHub détecté dans $pub avant git push" >&2
    return 1
  fi
  if [ -n "$hc_tok" ] && { grep -RFq -- "$hc_tok" "$pub/epreuve-plantee-v4" || grep -Fq -- "$hc_tok" "$pub/.git/config"; }; then
    echo "ERREUR SÉCURITÉ : jeton Hetzner détecté dans $pub avant git push" >&2
    return 1
  fi
  if [ -n "$vast_key" ] && { grep -RFq -- "$vast_key" "$pub/epreuve-plantee-v4" || grep -Fq -- "$vast_key" "$pub/.git/config"; }; then
    echo "ERREUR SÉCURITÉ : clé Vast.ai détectée dans $pub avant git push" >&2
    return 1
  fi

  git -C "$pub" add -A
  git -C "$pub" commit -m "Sondes v2 épreuve plantée v4 ($etiquette, commit $COMMIT_CODE, amorce v3)"
  LOCAL_SHA="$(git -C "$pub" rev-parse HEAD)"
  git -C "$pub" push --force "$REPO_URL" "HEAD:refs/heads/$BRANCHE_SORTIE"
  REMOTE_SHA="$(git ls-remote "$REPO_URL" "refs/heads/$BRANCHE_SORTIE" | awk '{print $1}')"
  test "$LOCAL_SHA" = "$REMOTE_SHA"
  echo "RAPATRIEMENT PROUVÉ : $BRANCHE_SORTIE @ $REMOTE_SHA"
}

gerer_timeout_r10() {
  TIMEOUT_DECLENCHE=1
  echo "=== PLAFOND INTERNE R10 (${WATCHDOG_SECONDES}s) ATTEINT $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  tuer_fils_actif
  pousser_sorties "partiel-plafond-r10" || echo "AVERTISSEMENT : rapatriement partiel incomplet"
  exit 124
}

detruire_serveur() {
  local rc=$?
  if [ "$DEJA_DETRUIT" -eq 1 ]; then
    return 0
  fi
  DEJA_DETRUIT=1
  arreter_watchdog
  tuer_fils_actif
  if [ "$rc" -ne 0 ] && [ "$TIMEOUT_DECLENCHE" -eq 0 ] && [ "$RAPATRIEMENT_FINAL_FAIT" -eq 0 ] && [ -f "${ASKPASS_SCRIPT:-}" ]; then
    echo "=== ARRÊT SUR ERREUR HORS MINUTERIE (rc=$rc) : sauvegarde de ce qui est récupérable (R-3661) ==="
    pousser_sorties "partiel-erreur-rc${rc}" || echo "AVERTISSEMENT : sauvegarde partielle sur erreur incomplète"
  fi
  echo "=== FIN (rc=$rc, timeout=$TIMEOUT_DECLENCHE, fournisseur=$FOURNISSEUR_EFFECTIF) $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  if [ "$FOURNISSEUR_EFFECTIF" = "hetzner" ]; then
    local HCLOUD_KEY=""
    if [ -f "$HCLOUD_TOKEN_FILE" ]; then
      HCLOUD_KEY="$(tr -d '\r\n' < "$HCLOUD_TOKEN_FILE")"
    fi
    if [[ "${SERVER_ID:-}" =~ ^[1-9][0-9]*$ ]] && [ -n "$HCLOUD_KEY" ]; then
      echo "Appel R10 DELETE ${HCLOUD_API%/}/servers/${SERVER_ID}"
      curl -fsS --max-time 20 -X DELETE -H "Authorization: Bearer ${HCLOUD_KEY}" \
        "${HCLOUD_API%/}/servers/${SERVER_ID}" || true
    fi
  elif [ "$FOURNISSEUR_EFFECTIF" = "vast" ]; then
    local VAST_KEY=""
    if [ -f "$VAST_API_KEY_FILE" ]; then
      VAST_KEY="$(tr -d '\r\n' < "$VAST_API_KEY_FILE")"
    fi
    if verifier_vast_instance_id_autorise "${TARGET_VAST_ID:-}" && [ -n "$VAST_KEY" ]; then
      echo "Appel R10 DELETE ${VAST_API_URL%/}/instances/${TARGET_VAST_ID}/"
      curl -fsS --max-time 20 -X DELETE -H "Authorization: Bearer ${VAST_KEY}" \
        "${VAST_API_URL%/}/instances/${TARGET_VAST_ID}/" || true
    fi
  fi
  rm -f "${ASKPASS_SCRIPT:-}" 2>/dev/null || true
}

trap gerer_timeout_r10 TERM
trap detruire_serveur EXIT

# Cloner le dépôt via l'URL HTTPS nue + GIT_ASKPASS (jamais de jeton dans .git/config)
git -c core.autocrlf=false clone --no-tags --branch "$BRANCHE_CODE" "$REPO_URL" "$WORK/repo"
git -C "$WORK/repo" checkout --detach "$COMMIT_CODE"
test -z "$(git -C "$WORK/repo" status --porcelain)"
echo "$SHA_VERITES  $WORK/repo/src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json" | sha256sum -c -

# Récupérer la note des effectifs (+ .sha256) depuis main HORS du dépôt git (préserve depot_propre=True)
git -C "$WORK/repo" fetch --no-tags origin main --depth=1
git -C "$WORK/repo" show origin/main:docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md \
  > "$ENTREE/note-des-effectifs-sondes-v2-v1.md"
git -C "$WORK/repo" show origin/main:docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md.sha256 \
  > "$ENTREE/note-des-effectifs-sondes-v2-v1.md.sha256"
(cd "$ENTREE" && sha256sum -c note-des-effectifs-sondes-v2-v1.md.sha256)
echo "$SHA_NOTE  $ENTREE/note-des-effectifs-sondes-v2-v1.md" | sha256sum -c -

# Environnement Python épinglé sur les versions exactes vérifiées localement
if [ "$SKIP_ENV_INSTALL" = "1" ] && [ -n "$PY_BIN" ]; then
  PY="$PY_BIN"
else
  if ! python3 -c "import venv, ensurepip" >/dev/null 2>&1 && command -v apt-get >/dev/null 2>&1; then
    DEBIAN_FRONTEND=noninteractive apt-get update -qq
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 python3-venv
  fi
  python3 -m venv "$WORK/venv"
  "$WORK/venv/bin/pip" install --no-cache-dir numpy==2.4.6 scipy==1.17.1 scikit-learn==1.9.1
  PY="$WORK/venv/bin/python3"
fi
export PYTHONPATH="$WORK/repo/src"

# Récupération et vérification à l'octet des tranches étalon déjà calculées ([0, ETALON_DE)) sur la branche amont
recuperer_etalon_amont() {
  if [ "$ETALON_DE" -eq 0 ]; then
    return 0
  fi
  git -C "$WORK/repo" fetch --no-tags "$REPO_URL" "refs/heads/$BRANCHE_AMONT_ETALON:refs/remotes/origin/amont-etalon"
  local ref_amont="refs/remotes/origin/amont-etalon"
  if [ -n "$COMMIT_AMONT_ETALON" ]; then
    git -C "$WORK/repo" cat-file -e "${COMMIT_AMONT_ETALON}^{commit}"
    git -C "$WORK/repo" merge-base --is-ancestor "$COMMIT_AMONT_ETALON" refs/remotes/origin/amont-etalon
    ref_amont="$COMMIT_AMONT_ETALON"
  fi
  test -z "$(git -C "$WORK/repo" status --porcelain)"

  local nb_extraits=0
  local de=0
  while [ "$de" -lt "$ETALON_DE" ]; do
    local a=$((de + ETALON_AMONT_PAS))
    local base="rapport-monde-plante-v4-etalon-${ENTROPIE}-r${de}-${a}.json"
    git -C "$WORK/repo" show "${ref_amont}:epreuve-plantee-v4/etalon/${base}" > "$SORTIE/etalon/${base}"
    git -C "$WORK/repo" show "${ref_amont}:epreuve-plantee-v4/etalon/${base}.sha256" > "$SORTIE/etalon/${base}.sha256"
    (cd "$SORTIE/etalon" && sha256sum -c "${base}.sha256")
    nb_extraits=$((nb_extraits + 1))
    de="$a"
  done
  echo ">>> Reprise étalon amont : ${nb_extraits} rapports ([0, ${ETALON_DE})) extraits depuis ${ref_amont} et vérifiés à l'octet."

  "$PY" -B - "$SORTIE/etalon" "$ENTROPIE" "$ETALON_DE" "$COMMIT_CODE" "$SHA_VERITES" "$SHA_NOTE" "$ENTREE/note-des-effectifs-sondes-v2-v1.md" <<'PY_AMONT_EOF'
import glob
import json
import sys
from pathlib import Path

outdir, entropie, etalon_de_s, commit_att, sha_v_att, sha_n_att, chemin_note_att = sys.argv[1:8]
etalon_de = int(etalon_de_s)
chemins = sorted(glob.glob(f"{outdir}/rapport-monde-plante-v4-etalon-{entropie}-r*.json"))
rapports = [json.loads(Path(c).read_text(encoding="utf-8")) for c in chemins]
plages = sorted(tuple(r["plage"]) for r in rapports)
bout = 0
for d, a in plages:
    if d != bout:
        raise SystemExit(f"Plages amont non contiguës: {plages}")
    bout = a
if bout != etalon_de:
    raise SystemExit(f"Couverture amont [0, {bout}) != [0, {etalon_de})")
if "manifeste" in rapports[0] and "arguments" in rapports[0]:
    for r in rapports:
        assert r["mode"] == "etalon", r["mode"]
        assert r["verites_sha256"] == sha_v_att, r["verites_sha256"]
        assert r["graines"]["entropie_racine"] == entropie, r["graines"]
        assert r["manifeste"]["commit"] == commit_att, r["manifeste"]["commit"]
        assert r["manifeste"]["depot_propre"] is True, r["manifeste"]["depot_propre"]
        ne = r["arguments"]["note_effectifs"]
        assert ne["sha256"] == sha_n_att, ne
        if ne["chemin"] != chemin_note_att:
            raise SystemExit(
                f"Incompatibilité chemin note_effectifs pour fusionner(): amont={ne['chemin']!r} vs courant={chemin_note_att!r} (conserver ENTREE=/opt/entree)"
            )
PY_AMONT_EOF
}

# Sonde chronométrée d'exactement 1 réplique de `complet` dans $WORK/sonde_complet_1rep (sans polluer $SORTIE/complet)
lancer_sonde_complet_1rep() {
  local sonde_dir="$WORK/sonde_complet_1rep"
  rm -rf "$sonde_dir"
  mkdir -p "$sonde_dir"
  echo ">>> Sonde chronométrée 1 réplique mode=complet (--repliques 1) dans $sonde_dir (sans polluer $SORTIE/complet)"
  "$PY" -B - "$PY" "$sonde_dir" "$SORTIE/sonde-complet-1rep-meta.json" \
    "$ENTREE/note-des-effectifs-sondes-v2-v1.md" "$ENTROPIE" "$COMMIT_CODE" \
    "$CPU_DISPO" "$N_WORKERS" "${SIMULER_MODE_CMD:-}" <<'PY_SONDE_EOF'
import glob
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import resource
except ImportError:
    resource = None

(
    py_bin,
    sonde_dir_s,
    meta_out_s,
    note_path,
    entropie,
    commit_code,
    cpu_dispo_s,
    n_workers_s,
    simuler_cmd,
) = sys.argv[1:10]
sonde_dir = Path(sonde_dir_s)
meta_out = Path(meta_out_s)

if simuler_cmd:
    import shutil as _sh
    _b = (_sh.which("bash") or "bash") if simuler_cmd.endswith(".sh") else None
    cmd = ([_b, simuler_cmd] if _b else [simuler_cmd]) + ["sonde_complet_1rep", str(sonde_dir), entropie, "0", "1", "1"]
else:
    cmd = [
        py_bin, "-B", "-m", "controle_ia.sondes_v2.programme_monde_plante_v4",
        "--sortie", str(sonde_dir),
        "--note-effectifs", note_path,
        "--mode", "complet",
        "--doses-rejeu", "4",
        "--nul", "39",
        "--repliques", "1",
        "--entropie", entropie,
    ]

t_utc_debut = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
t0 = time.monotonic()
subprocess.run(cmd, check=True)
duree_mur_s = time.monotonic() - t0
t_utc_fin = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

if resource is not None:
    usage = resource.getrusage(resource.RUSAGE_CHILDREN)
    ru_raw = int(usage.ru_maxrss)
    pic_rss_kib = ru_raw // 1024 if sys.platform == "darwin" else ru_raw
else:
    pic_rss_kib = 0
pic_rss_mio = round(pic_rss_kib / 1024.0, 3)

candidats = sorted(
    p for p in glob.glob(f"{sonde_dir}/rapport-monde-plante-v4-complet-{entropie}*.json")
    if not p.endswith(".sha256")
)
rapport_sha = None
duree_interne_s = None
if candidats:
    raw = Path(candidats[0]).read_bytes()
    rapport_sha = hashlib.sha256(raw).hexdigest()
    try:
        duree_interne_s = json.loads(raw.decode("utf-8")).get("duree_secondes")
    except Exception:
        duree_interne_s = None

meta = {
    "format": "sonde-complet-1rep-meta-v1",
    "mode_sonde": "complet",
    "repliques_sondees": 1,
    "doses_rejeu": 4,
    "nul": 39,
    "commit_code": commit_code,
    "entropie_racine": entropie,
    "cpu_dispo": int(cpu_dispo_s),
    "n_workers_configures": int(n_workers_s),
    "debut_utc": t_utc_debut,
    "fin_utc": t_utc_fin,
    "duree_secondes": round(duree_mur_s, 6),
    "duree_interne_rapport_secondes": duree_interne_s,
    "pic_rss_kib": pic_rss_kib,
    "pic_rss_mio": pic_rss_mio,
    "dossier_isole": str(sonde_dir),
    "rapport_sonde_sha256": rapport_sha,
}
corps = (json.dumps(meta, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
meta_out.parent.mkdir(parents=True, exist_ok=True)
meta_out.write_bytes(corps)
sha_meta = hashlib.sha256(corps).hexdigest()
meta_out.with_name(meta_out.name + ".sha256").write_bytes(f"{sha_meta}  {meta_out.name}\n".encode("utf-8"))
print(
    f"SONDE COMPLET 1 REP TERMINEE: duree={duree_mur_s:.3f}s | pic_rss={pic_rss_mio:.2f} MiB ({pic_rss_kib} KiB) | sha256={sha_meta}",
    flush=True,
)
PY_SONDE_EOF
  (cd "$SORTIE" && sha256sum -c sonde-complet-1rep-meta.json.sha256)
}

# Lancement parallèle par tranches [de_global, a_global) de pas `pas` (dernière tranche bornée à a_global, ex. 500)
# via `seq ... | xargs -P "$workers_locaux" -I {}` sans `-n 1`
lancer_tranches_mode() {
  local mode="$1"
  local de_global="$2"
  local a_global="$3"
  local pas="$4"
  local workers_locaux="${5:-$N_WORKERS}"
  local outdir="$SORTIE/$mode"
  mkdir -p "$outdir"

  if [ -n "$SIMULER_MODE_CMD" ]; then
    "$SIMULER_MODE_CMD" "$mode" "$outdir" "$ENTROPIE" "$de_global" "$a_global" "$pas" "$workers_locaux"
    return $?
  fi

  if [ "$de_global" -lt "$a_global" ]; then
    local extra_args=()
    if [ "$mode" = "complet" ]; then
      extra_args+=(--doses-rejeu 4 --nul 39)
    fi
    local dernier_depart=$((a_global - 1))
    echo ">>> Lancement mode=$mode sur [${de_global}, ${a_global}) par pas=$pas (dernière tranche bornée à ${a_global}, ${workers_locaux} workers)"
    seq "$de_global" "$pas" "$dernier_depart" | xargs -P "$workers_locaux" -I {} bash -c '
      set -euo pipefail
      de="{}"
      pas_local="'"$pas"'"
      plafond="'"$a_global"'"
      a=$(( de + pas_local > plafond ? plafond : de + pas_local ))
      exec "'"$PY"'" -B -m controle_ia.sondes_v2.programme_monde_plante_v4 \
        --sortie "'"$outdir"'" \
        --note-effectifs "'"$ENTREE/note-des-effectifs-sondes-v2-v1.md"'" \
        --mode "'"$mode"'" \
        '"${extra_args[*]:-}"' \
        --repliques 500 --repliques-de "$de" --repliques-a "$a" \
        --entropie "'"$ENTROPIE"'"
    '
  fi

  # Fusion officielle scellée (sans supposer len(chemins) == 50 ; vérifie la couverture exacte [0, 500))
  "$PY" -B - "$outdir" "$mode" "$ENTROPIE" <<'PY_FUSION_EOF'
import glob
import json
import sys
from pathlib import Path
from controle_ia.sondes_v2 import programme_monde_plante_v4 as p

outdir, mode, entropie = sys.argv[1:4]
chemins = sorted(glob.glob(f"{outdir}/rapport-monde-plante-v4-{mode}-{entropie}-r*.json"))
if not chemins:
    raise SystemExit(f"Aucun rapport trouvé dans {outdir} pour mode={mode}")

plages = sorted(tuple(json.loads(Path(c).read_text(encoding="utf-8"))["plage"]) for c in chemins)
bout = 0
couvert = True
for d, a in plages:
    if d != bout:
        couvert = False
        break
    bout = a
couvert = couvert and (bout == 500)

if mode == "etalon" and not couvert:
    raise SystemExit(f"Couverture étalon incomplète : attendu [0, 500), obtenu fin={bout} sur {len(chemins)} rapports")

if couvert:
    cible = f"{outdir}/synthese-fusionnee-monde-plante-v4-{mode}-{entropie}.json"
    out = p.ecrire_synthese_fusionnee(chemins, cible)
    print(f"SYNTHESE SCELLEE ({mode}, {len(chemins)} rapports):", out, flush=True)
else:
    print(
        f"SYNTHESE DIFFEREE ({mode}, couverture partielle sur cette machine: {len(chemins)} rapports, fin={bout}/500)",
        flush=True,
    )
PY_FUSION_EOF
}

# Exécution parallèle sur 64+ cœurs (N_WORKERS >= 63) : sonde 1 réplique sur le 63e cœur pendant la vague unique des 62 tranches d'étalon
lancer_etalon_et_sonde_parallele() {
  local workers_etalon=$((N_WORKERS - 1))
  echo ">>> Mode parallèle activé (N_WORKERS=$N_WORKERS >= 63) : sonde_complet_1rep en tâche de fond (1 cœur dédié) + etalon [${ETALON_DE}, ${ETALON_A}) (${workers_etalon} workers)"
  lancer_sonde_complet_1rep &
  local pid_sonde=$!
  lancer_tranches_mode etalon "$ETALON_DE" "$ETALON_A" "$PAS_ETALON" "$workers_etalon" &
  local pid_etalon=$!
  local rc_sonde=0
  local rc_etalon=0
  wait "$pid_sonde" || rc_sonde=$?
  wait "$pid_etalon" || rc_etalon=$?
  if [ "$rc_etalon" -ne 0 ]; then
    echo "ERREUR : échec de la vague étalon parallèle (rc=$rc_etalon)" >&2
    return "$rc_etalon"
  fi
  if [ "$rc_sonde" -ne 0 ]; then
    echo "ERREUR : échec de sonde_complet_1rep parallèle (rc=$rc_sonde)" >&2
    return "$rc_sonde"
  fi
  return 0
}

executer_avec_interruption() {
  "$@" &
  ACTIVE_CHILD_PID=$!
  local rc=0
  wait "$ACTIVE_CHILD_PID" || rc=$?
  ACTIVE_CHILD_PID=""
  return "$rc"
}

# Vraie minuterie interne R10 (défaut : 31h30 = 113400 s, avant coupure externe)
(
  sleep "$WATCHDOG_SECONDES" &
  SLEEP_PID=$!
  trap 'kill "$SLEEP_PID" 2>/dev/null || true; exit 0' TERM INT
  wait "$SLEEP_PID" 2>/dev/null || exit 0
  kill -TERM $$ 2>/dev/null || true
) </dev/null >/dev/null 2>&1 &
WATCHDOG_PID=$!
echo "Watchdog interne R10 armé : ${WATCHDOG_SECONDES}s (PID=$WATCHDOG_PID)"

case "$MODE_RUN" in
  etalon_suite_seul)
    recuperer_etalon_amont
    executer_avec_interruption lancer_tranches_mode etalon "$ETALON_DE" "$ETALON_A" "$PAS_ETALON" "$N_WORKERS"
    pousser_sorties "etalon-suite-termine"
    ;;
  etalon_suite_et_sonde_complet_1rep)
    recuperer_etalon_amont
    if [ "$N_WORKERS" -ge 63 ]; then
      executer_avec_interruption lancer_etalon_et_sonde_parallele
      pousser_sorties "etalon-suite-et-sonde-complet-1rep-termines"
    else
      executer_avec_interruption lancer_sonde_complet_1rep
      pousser_sorties "sonde-complet-1rep-terminee"
      executer_avec_interruption lancer_tranches_mode etalon "$ETALON_DE" "$ETALON_A" "$PAS_ETALON" "$N_WORKERS"
      pousser_sorties "etalon-suite-et-sonde-complet-1rep-termines"
    fi
    ;;
  etalon_suite_et_complet)
    recuperer_etalon_amont
    executer_avec_interruption lancer_tranches_mode etalon "$ETALON_DE" "$ETALON_A" "$PAS_ETALON" "$N_WORKERS"
    pousser_sorties "etalon-suite-termine"
    executer_avec_interruption lancer_tranches_mode complet "$COMPLET_DE" "$COMPLET_A" "$PAS_COMPLET" "$N_WORKERS"
    pousser_sorties "etalon-suite-et-complet-${COMPLET_DE}-${COMPLET_A}-termines"
    ;;
  complet_tranche_seul)
    executer_avec_interruption lancer_tranches_mode complet "$COMPLET_DE" "$COMPLET_A" "$PAS_COMPLET" "$N_WORKERS"
    pousser_sorties "complet-${COMPLET_DE}-${COMPLET_A}-termine"
    ;;
esac

RAPATRIEMENT_FINAL_FAIT=1
arreter_watchdog
