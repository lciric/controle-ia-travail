#!/usr/bin/env bash
# Script autonome d'amorce Hetzner ccx63 (cloud-init -> /opt/run_epreuve_sondes_v2.sh)
# Épreuve à vérité plantée des sondes boîte blanche v2 — GO-2026-11-24-02 (R-5222)
# Version 2 : corrige les 3 bloquants de la contre-lecture R2 (e94bd12b…) :
#   1. Intégrité 100 % des .sha256 dans $pub avant git push (journaux-gels archivés/découpés).
#   2. Sécurité GITHUB_PUSH_TOKEN / HCLOUD_TOKEN : URL HTTPS nue + GIT_ASKPASS (0700) + filtre sed sur $LOG.
#   3. Minuterie interne R10 effective (31h30 = 113400 s) avec trap TERM -> arrêt fils, rapatriement partiel,
#      puis trap EXIT -> destruction par identifiant numérique Hetzner.
set -euo pipefail
set +x

export PYTHONDONTWRITEBYTECODE=1
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1

MODE_RUN="${MODE_RUN:-complet_et_etalon}"
COMMIT_CODE="${COMMIT_CODE:-0ce9e35110d93dd916e85b1191a2613b101e772d}"
ENTROPIE="${ENTROPIE:-305159624078239919914131004197200342142}"
SHA_VERITES="${SHA_VERITES:-b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533}"
SHA_NOTE="${SHA_NOTE:-7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5}"
BRANCHE_CODE="${BRANCHE_CODE:-sondes-v2/code-v2}"
BRANCHE_SORTIE="${BRANCHE_SORTIE:-calcul/sondes-v2-epreuve-plantee-v4}"
REPO_URL="${REPO_URL:-https://github.com/lciric/controle-ia-travail.git}"
HCLOUD_API="${HCLOUD_API:-https://api.hetzner.cloud/v1}"
METADATA_URL="${METADATA_URL:-http://169.254.169.254/hetzner/v1/metadata/instance-id}"
HCLOUD_TOKEN_FILE="${HCLOUD_TOKEN_FILE:-/root/.hcloud_token}"
GH_TOKEN_FILE="${GH_TOKEN_FILE:-/root/.gh_token}"
WORK="${WORK:-/opt/sondes-v2}"
ENTREE="${ENTREE:-/opt/entree}"
SORTIE="${SORTIE:-/opt/sortie}"
LOG="${LOG:-/var/log/epreuve-sondes-v2.log}"
WATCHDOG_SECONDES="${WATCHDOG_SECONDES:-113400}"
SEUIL_ARCHIVE_OCTETS="${SEUIL_ARCHIVE_OCTETS:-94371840}"
TAILLE_MORCEAU="${TAILLE_MORCEAU:-45m}"
N_WORKERS="${N_WORKERS:-$(nproc)}"
SKIP_ENV_INSTALL="${SKIP_ENV_INSTALL:-0}"
PY_BIN="${PY_BIN:-}"
SIMULER_MODE_CMD="${SIMULER_MODE_CMD:-}"

# Garde sécurité : jamais de jeton intégré dans REPO_URL
case "$REPO_URL" in
  *"@"*|*"x-access-token"*)
    echo "ARRÊT SÉCURITÉ : REPO_URL ne doit jamais contenir de jeton ou d'identifiants." >&2
    exit 1
    ;;
esac

mkdir -p "$WORK" "$ENTREE" "$SORTIE/etalon" "$SORTIE/complet" "$(dirname "$LOG")"
: > "$LOG"
exec > >(tee -a "$LOG") 2>&1

echo "=== DÉBUT $(date -u +%Y-%m-%dT%H:%M:%SZ) | mode=$MODE_RUN | nproc=$N_WORKERS | watchdog=${WATCHDOG_SECONDES}s ==="

# Chargement silencieux des jetons depuis fichiers protégés (0600), jamais affichés
HCLOUD_TOKEN=""
if [ -f "$HCLOUD_TOKEN_FILE" ]; then
  HCLOUD_TOKEN="$(tr -d '\r\n' < "$HCLOUD_TOKEN_FILE")"
fi
GH_TOK=""
if [ -f "$GH_TOKEN_FILE" ]; then
  GH_TOK="$(tr -d '\r\n' < "$GH_TOKEN_FILE")"
fi

# Script GIT_ASKPASS (0700) : lit GH_TOKEN_FILE à la volée, jamais de jeton dans REPO_URL ni .git/config
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

# Récupération de l'identifiant numérique Hetzner de la machine (métadonnées locales)
SERVER_ID="$(curl -fsS --max-time 10 "$METADATA_URL" 2>/dev/null | tr -d '\r\n' || true)"
echo "SERVER_ID=${SERVER_ID:-inconnu}"

WATCHDOG_PID=""
ACTIVE_CHILD_PID=""
TIMEOUT_DECLENCHE=0
DEJA_DETRUIT=0

arreter_watchdog() {
  if [ -n "${WATCHDOG_PID:-}" ]; then
    kill -TERM "$WATCHDOG_PID" 2>/dev/null || true
    wait "$WATCHDOG_PID" 2>/dev/null || true
    WATCHDOG_PID=""
  fi
}

tuer_fils_actif() {
  if [ -n "${ACTIVE_CHILD_PID:-}" ]; then
    pkill -TERM -P "$ACTIVE_CHILD_PID" 2>/dev/null || true
    kill -TERM "$ACTIVE_CHILD_PID" 2>/dev/null || true
    sleep 1
    pkill -KILL -P "$ACTIVE_CHILD_PID" 2>/dev/null || true
    kill -KILL "$ACTIVE_CHILD_PID" 2>/dev/null || true
    wait "$ACTIVE_CHILD_PID" 2>/dev/null || true
    ACTIVE_CHILD_PID=""
  fi
}

filtrer_secrets_log() {
  local src="$1"
  local dst="$2"
  local esc_gh="" esc_hc=""
  if [ -n "${GH_TOK:-}" ]; then
    esc_gh="$(printf '%s' "$GH_TOK" | sed -e 's/[\/&.^$*[\]|]/\\&/g')"
  fi
  if [ -n "${HCLOUD_TOKEN:-}" ]; then
    esc_hc="$(printf '%s' "$HCLOUD_TOKEN" | sed -e 's/[\/&.^$*[\]|]/\\&/g')"
  fi
  local sed_args=(
    -E
    -e 's/gh[pousr]_[A-Za-z0-9_]+/[MASQUE_GH]/g'
    -e 's/github_pat_[A-Za-z0-9_]+/[MASQUE_GH]/g'
    -e 's/x-access-token:[^@[:space:]]+@/x-access-token:[MASQUE_GH]@/g'
  )
  if [ -n "$esc_gh" ]; then
    sed_args+=(-e "s|${esc_gh}|[MASQUE_GH]|g")
  fi
  if [ -n "$esc_hc" ]; then
    sed_args+=(-e "s|${esc_hc}|[MASQUE_HCLOUD]|g")
  fi
  sed "${sed_args[@]}" "$src" > "$dst"
  if [ -n "${GH_TOK:-}" ] && grep -Fq -- "$GH_TOK" "$dst"; then
    echo "ERREUR SÉCURITÉ : jeton GitHub résiduel détecté dans le journal filtré" >&2
    rm -f "$dst"
    return 1
  fi
  if [ -n "${HCLOUD_TOKEN:-}" ] && grep -Fq -- "$HCLOUD_TOKEN" "$dst"; then
    echo "ERREUR SÉCURITÉ : jeton Hetzner résiduel détecté dans le journal filtré" >&2
    rm -f "$dst"
    return 1
  fi
}

# Fonction de rapatriement prouvé sur la branche dédiée (jamais main, aucun fichier > 95 Mo, 100 % .sha256 valides)
pousser_sorties() {
  local etiquette="$1"
  local pub="$WORK/pub"
  rm -rf "$pub"
  git init "$pub"
  git -C "$pub" config user.name "sondes-v2-hetzner-runner"
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

  # Vérification anti-fuite globale sur tout $pub avant commit/push
  if [ -n "${GH_TOK:-}" ] && grep -RFq -- "$GH_TOK" "$pub/epreuve-plantee-v4"; then
    echo "ERREUR SÉCURITÉ : jeton GitHub détecté dans $pub avant git push" >&2
    return 1
  fi
  if [ -n "${HCLOUD_TOKEN:-}" ] && grep -RFq -- "$HCLOUD_TOKEN" "$pub/epreuve-plantee-v4"; then
    echo "ERREUR SÉCURITÉ : jeton Hetzner détecté dans $pub avant git push" >&2
    return 1
  fi

  git -C "$pub" add -A
  git -C "$pub" commit -m "Sondes v2 épreuve plantée v4 ($etiquette, commit $COMMIT_CODE, GO-2026-11-24-02)"
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
  echo "=== FIN (rc=$rc, timeout=$TIMEOUT_DECLENCHE) $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  if [ -n "${SERVER_ID:-}" ] && [ -n "${HCLOUD_TOKEN:-}" ]; then
    echo "Appel R10 DELETE ${HCLOUD_API}/servers/${SERVER_ID}"
    curl -fsS --max-time 15 -X DELETE -H "Authorization: Bearer ${HCLOUD_TOKEN}" \
      "${HCLOUD_API}/servers/${SERVER_ID}" || true
  fi
  rm -f "${ASKPASS_SCRIPT:-}" 2>/dev/null || true
}

trap gerer_timeout_r10 TERM
trap detruire_serveur EXIT

# Cloner le dépôt via l'URL HTTPS nue + GIT_ASKPASS (jamais de jeton dans .git/config)
git clone --no-tags --branch "$BRANCHE_CODE" "$REPO_URL" "$WORK/repo"
git -C "$WORK/repo" checkout --detach "$COMMIT_CODE"
test -z "$(git -C "$WORK/repo" status --porcelain)"
echo "$SHA_VERITES  $WORK/repo/src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json" | sha256sum -c -

# Récupérer la note des effectifs (+ .sha256) depuis main HORS du dépôt git (préserve depot_propre=True)
git -C "$WORK/repo" fetch origin main --depth=1
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
  python3 -m venv "$WORK/venv"
  "$WORK/venv/bin/pip" install --no-cache-dir numpy==2.4.6 scipy==1.17.1 scikit-learn==1.9.1
  PY="$WORK/venv/bin/python3"
fi
export PYTHONPATH="$WORK/repo/src"

# Fonction de lancement parallèle en 50 plages de 10 répliques couvrant [0, 500)
lancer_mode() {
  local mode="$1"
  local outdir="$SORTIE/$mode"
  if [ -n "$SIMULER_MODE_CMD" ]; then
    "$SIMULER_MODE_CMD" "$mode" "$outdir" "$ENTROPIE"
    return $?
  fi
  local extra_args=()
  if [ "$mode" = "complet" ]; then
    extra_args+=(--doses-rejeu 4 --nul 39)
  fi
  echo ">>> Lancement mode=$mode (50 plages x 10 répliques, $N_WORKERS workers)"
  seq 0 10 490 | xargs -n 1 -P "$N_WORKERS" -I {} bash -c '
    set -euo pipefail
    de="{}"
    a=$((de + 10))
    exec "'"$PY"'" -B -m controle_ia.sondes_v2.programme_monde_plante_v4 \
      --sortie "'"$outdir"'" \
      --note-effectifs "'"$ENTREE/note-des-effectifs-sondes-v2-v1.md"'" \
      --mode "'"$mode"'" \
      '"${extra_args[*]:-}"' \
      --repliques 500 --repliques-de "$de" --repliques-a "$a" \
      --entropie "'"$ENTROPIE"'"
  '
  # Fusion officielle scellée (identique à l'octet à un processus unique)
  "$PY" -B -c "
import glob
from controle_ia.sondes_v2 import programme_monde_plante_v4 as p
chemins = sorted(glob.glob('$outdir/rapport-monde-plante-v4-$mode-$ENTROPIE-r*.json'))
assert len(chemins) == 50, len(chemins)
out = p.ecrire_synthese_fusionnee(chemins, '$outdir/synthese-fusionnee-monde-plante-v4-$mode-$ENTROPIE.json')
print('SYNTHESE SCELLEE:', out)
"
}

executer_avec_interruption() {
  "$@" &
  ACTIVE_CHILD_PID=$!
  local rc=0
  wait "$ACTIVE_CHILD_PID" || rc=$?
  ACTIVE_CHILD_PID=""
  return "$rc"
}

# Vraie minuterie interne R10 (défaut : 31h30 = 113400 s, avant la coupure externe 32h)
(
  sleep "$WATCHDOG_SECONDES" &
  SLEEP_PID=$!
  trap 'kill "$SLEEP_PID" 2>/dev/null || true; exit 0' TERM INT
  wait "$SLEEP_PID" 2>/dev/null || exit 0
  kill -TERM $$ 2>/dev/null || true
) &
WATCHDOG_PID=$!
echo "Watchdog interne R10 armé : ${WATCHDOG_SECONDES}s (PID=$WATCHDOG_PID)"

executer_avec_interruption lancer_mode etalon
pousser_sorties "etalon-termine"

if [ "$MODE_RUN" = "complet_et_etalon" ]; then
  executer_avec_interruption lancer_mode complet
  pousser_sorties "etalon-et-complet-termines"
fi

arreter_watchdog
