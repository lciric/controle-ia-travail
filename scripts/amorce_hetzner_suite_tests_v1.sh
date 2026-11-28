#!/usr/bin/env bash
# Amorce v1 — serveur Hetzner jetable qui joue une fois la suite complète des tests du dépôt (GO-2026-11-28-04).
# Injectée en base64 par scripts/lancer_hetzner_suite_tests_v1.py dans les données de démarrage du serveur.
# Paramètres : fichier PARAMETRES (variables ci-dessous) ; jetons dans des fichiers 0600, jamais journalisés,
# jamais passés en argument de commande (fichier d'en-tête pour curl, GIT_ASKPASS pour git).
# Gardes :
#   1. minuterie interne PLAFOND_SECONDES : TERM -> arrêt du groupe de processus des essais par son identifiant
#      (R10, jamais par motif), puis rapatriement partiel ;
#   2. retrait des jetons dans toutes les sorties, puis contrôle bloquant : un jeton restant interdit la poussée ;
#   3. poussée sur une branche orpheline neuve (jamais forcée), prouvée par git ls-remote ;
#   4. autodestruction par identifiant numérique du serveur à la sortie (trap EXIT), poussée prouvée ou non.
set -uo pipefail
umask 077

PARAMETRES="${1:-/opt/suite-tests/parametres.env}"
# shellcheck disable=SC1090
. "$PARAMETRES"
: "${RUN_ID:?}" "${DEPOT_URL:?}" "${COMMIT_CODE:?}" "${BRANCHE_CODE:?}" "${BRANCHE_SORTIE:?}" "${PLAFOND_SECONDES:?}"
: "${GH_TOKEN_FILE:?}" "${HC_TOKEN_FILE:?}" "${TRAVAIL:?}" "${CONTRAINTES:?}"
HCLOUD_API="${HCLOUD_API:-https://api.hetzner.cloud/v1}"
METADONNEES="${METADONNEES:-http://169.254.169.254/hetzner/v1/metadata}"
DETRUIRE="${DETRUIRE:-oui}"            # « non » seulement pour un essai local sans faux serveur d'API
INSTALLER="${INSTALLER:-oui}"          # « non » seulement pour les essais R5 locaux (PY_ESSAIS imposé)
PY_ESSAIS="${PY_ESSAIS:-}"
UTILISATEUR="${UTILISATEUR:-essais}"
NPROC="${NPROC:-$(nproc)}"
PAUSE_POUSSEE="${PAUSE_POUSSEE:-300}"
PY_SYSTEME="${PY_SYSTEME:-python3}"

export HOME="${HOME:-/root}"
SORTIE="$TRAVAIL/sortie/$RUN_ID"           # devient diag/<RUN_ID>/ sur la branche de sortie
ES="$TRAVAIL/essais-sortie"                # écrit par l'utilisateur des essais
DEPOT="$TRAVAIL/depot"
VENV="$TRAVAIL/venv"
export UV_PYTHON_INSTALL_DIR="$TRAVAIL/uv-python" UV_CACHE_DIR="$TRAVAIL/uv-cache"
mkdir -p "$SORTIE" "$ES"
chmod 711 "$TRAVAIL"                       # traversable par l'utilisateur des essais, non listable ; jetons en 0600
JOURNAL="$SORTIE/journal-amorce-v1.txt"
exec >>"$JOURNAL" 2>&1
echo "=== DÉBUT $(date -u +%Y-%m-%dT%H:%M:%SZ) run=$RUN_ID commit=$COMMIT_CODE plafond=${PLAFOND_SECONDES}s nproc=$NPROC ==="

FAIT_CONCLURE=0; DELAI_DEPASSE=0; PGID_ESSAIS=""; GARDIEN=""; ETAPE="debut"
CODE_PHASE1=""; CODE_PHASE2=""; DEBUT_EPOCH="$(date +%s)"

# En-tête d'autorisation Hetzner dans un fichier 0600 (curl -H @fichier) ; demande d'identifiants git par GIT_ASKPASS.
ENTETE_HC="$TRAVAIL/entete-hcloud"
printf 'Authorization: Bearer %s\n' "$(head -n1 "$HC_TOKEN_FILE" | tr -d '\r\n')" > "$ENTETE_HC"
chmod 600 "$ENTETE_HC"
ASK="$TRAVAIL/askpass.sh"
printf '#!/bin/sh\ncase "$1" in *sername*) echo x-access-token ;; *) head -n1 "%s" | tr -d "\\r\\n" ;; esac\n' \
  "$GH_TOKEN_FILE" > "$ASK"
chmod 700 "$ASK"
export GIT_ASKPASS="$ASK" GIT_TERMINAL_PROMPT=0

SERVER_ID="$(curl -fsS --max-time 10 "$METADONNEES/instance-id" 2>/dev/null || true)"
case "$SERVER_ID" in ''|*[!0-9]*) SERVER_ID="inconnu" ;; esac
echo "identifiant du serveur : $SERVER_ID"

arreter_essais() {   # R10 : arrêt par identifiant du groupe de processus des essais, jamais par motif
  if [ -n "$PGID_ESSAIS" ]; then
    kill -TERM -- "-$PGID_ESSAIS" 2>/dev/null
    sleep 20
    kill -KILL -- "-$PGID_ESSAIS" 2>/dev/null
  fi
}
sur_term() {
  DELAI_DEPASSE=1
  echo "=== PLAFOND INTERNE ATTEINT $(date -u +%Y-%m-%dT%H:%M:%SZ) (étape $ETAPE) ==="
  arreter_essais
}

lancer_essais() {   # $1 : fichier de journal ; suite : commande ; groupe de processus propre (setsid)
  local journal="$1"; shift
  if [ "$(id -u)" = 0 ]; then
    setsid setpriv --reuid="$UTILISATEUR" --regid="$UTILISATEUR" --init-groups -- \
      env -i PATH="$(dirname "$PY_ESSAIS"):/usr/bin:/bin" HOME="/home/$UTILISATEUR" LANG=C.UTF-8 \
      PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
      "$@" >"$journal" 2>&1 &
  else
    setsid env -i PATH="$(dirname "$PY_ESSAIS"):/usr/bin:/bin" HOME="$HOME" LANG=C.UTF-8 \
      PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
      "$@" >"$journal" 2>&1 &
  fi
  PGID_ESSAIS=$!
  local rc=0
  wait "$PGID_ESSAIS"; rc=$?
  while kill -0 "$PGID_ESSAIS" 2>/dev/null; do wait "$PGID_ESSAIS"; rc=$?; done
  PGID_ESSAIS=""
  return "$rc"
}

ecrire_conclure() {
cat > "$TRAVAIL/conclure.py" <<'PYEOF'
"""Conclusion de l'amorce : retrait des jetons, contrôle bloquant, résumé, compagnons .sha256 (bibliothèque standard)."""
import argparse, hashlib, json, sys, urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

RETRAIT = "***JETON-RETIRE***"

def jetons(fichiers):
    out = []
    for f in fichiers:
        t = Path(f).read_text(encoding="utf-8", errors="replace").strip().splitlines()
        if t and len(t[0].strip()) >= 8:
            v = t[0].strip()
            out += [v, urllib.parse.quote(v, safe="")]
    return sorted(set(out), key=len, reverse=True)

def bilan_junit(chemin):
    if not chemin.exists():
        return None
    try:
        racine = ET.parse(chemin).getroot()
    except ET.ParseError as e:
        return {"illisible": str(e)}
    suites = [racine] if racine.tag == "testsuite" else list(racine.iter("testsuite"))
    tot = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0, "time": 0.0}
    for s in suites:
        for k in ("tests", "failures", "errors", "skipped"):
            tot[k] += int(s.get(k, 0) or 0)
        tot["time"] += float(s.get("time", 0) or 0)
    tot["passed"] = tot["tests"] - tot["failures"] - tot["errors"] - tot["skipped"]
    echecs = []
    for cas in racine.iter("testcase"):
        if cas.find("failure") is not None or cas.find("error") is not None:
            echecs.append(f'{cas.get("classname", "")}::{cas.get("name", "")}')
    tot["echecs"] = sorted(echecs)
    return tot

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sortie", required=True)
    p.add_argument("--jeton", action="append", default=[])
    p.add_argument("--sans-retrait", action="store_true")   # essais R5 seulement : simule un retrait manqué
    p.add_argument("--meta", default="{}")
    a = p.parse_args()
    sortie = Path(a.sortie)
    js = jetons(a.jeton)
    if not js:
        print("ARRÊT : aucun jeton lisible pour le contrôle", file=sys.stderr)
        return 3
    fichiers = sorted(f for f in sortie.rglob("*") if f.is_file() and not f.name.endswith(".sha256"))
    if not a.sans_retrait:
        for f in fichiers:
            b = f.read_bytes()
            n = b
            for j in js:
                n = n.replace(j.encode(), RETRAIT.encode())
            if n != b:
                f.write_bytes(n)
                print(f"jeton retiré de {f.name}")
    meta = json.loads(a.meta)
    p1, p2 = bilan_junit(sortie / "resultats-pytest-v1.xml"), bilan_junit(sortie / "reexecution-serie-v1.xml")
    persistants = sorted(set(p1["echecs"]) & set(p2["echecs"])) if (p1 and p2 and "echecs" in p1 and "echecs" in p2) else None
    resume = dict(meta, phase_parallele=p1, phase_serie=p2, echecs_persistants_en_serie=persistants)
    (sortie / "resume-v1.json").write_text(json.dumps(resume, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                           encoding="utf-8")
    fichiers = sorted(f for f in sortie.rglob("*") if f.is_file() and not f.name.endswith(".sha256"))
    for f in fichiers:   # contrôle bloquant après retrait
        b = f.read_bytes()
        for j in js:
            if j.encode() in b:
                print(f"ARRÊT SÉCURITÉ : jeton présent dans {f.name} ; poussée interdite", file=sys.stderr)
                return 2
    for f in fichiers:
        h = hashlib.sha256(f.read_bytes()).hexdigest()
        Path(str(f) + ".sha256").write_text(f"{h}  {f.name}\n", encoding="utf-8")
    print(f"{len(fichiers)} fichiers scellés")
    return 0

if __name__ == "__main__":
    sys.exit(main())
PYEOF
}

pousser() {
  local P="$TRAVAIL/poussee" i distant local_sha
  rm -rf "$P"; mkdir -p "$P/diag"
  cp -a "$SORTIE" "$P/diag/"
  cd "$P" || return 1
  git init -q && git checkout -q --orphan "$BRANCHE_SORTIE" || return 1
  git add -A
  git -c user.name="serveur-essais-hetzner" -c user.email="serveur-essais@invalid" \
    commit -q -m "Suite complète des tests ($RUN_ID, commit $COMMIT_CODE)" || return 1
  git remote add origin "$DEPOT_URL"
  for i in 1 2 3 4 5 6 7; do
    if git push -q origin "HEAD:refs/heads/$BRANCHE_SORTIE"; then
      distant="$(git ls-remote origin "refs/heads/$BRANCHE_SORTIE" | cut -f1)"
      local_sha="$(git rev-parse HEAD)"
      if [ "$distant" = "$local_sha" ]; then echo "POUSSÉE PROUVÉE $local_sha"; return 0; fi
    fi
    if [ "$i" -lt 4 ]; then sleep $((2 ** i)); else sleep "$PAUSE_POUSSEE"; fi
  done
  echo "ÉCHEC DE LA POUSSÉE"
  return 1
}

conclure() {
  [ "$FAIT_CONCLURE" = 1 ] && return 0
  FAIT_CONCLURE=1
  set +e
  [ -n "$GARDIEN" ] && kill "$GARDIEN" 2>/dev/null
  arreter_essais
  echo "=== CONCLUSION $(date -u +%Y-%m-%dT%H:%M:%SZ) étape=$ETAPE délai_dépassé=$DELAI_DEPASSE ==="
  exec >>"$TRAVAIL/journal-fin.txt" 2>&1      # le journal versé n'est plus écrit pendant son scellement
  cp -a "$ES"/. "$SORTIE"/ 2>/dev/null
  ecrire_conclure
  local meta
  meta="$(printf '{"run_id":"%s","commit":"%s","branche_code":"%s","etape_finale":"%s","delai_depasse":%s,"code_phase_parallele":"%s","code_phase_serie":"%s","duree_secondes":%s,"nproc":%s,"identifiant_serveur":"%s"}' \
    "$RUN_ID" "$COMMIT_CODE" "$BRANCHE_CODE" "$ETAPE" "$DELAI_DEPASSE" "$CODE_PHASE1" "$CODE_PHASE2" \
    "$(( $(date +%s) - DEBUT_EPOCH ))" "$NPROC" "$SERVER_ID")"
  if "$PY_SYSTEME" "$TRAVAIL/conclure.py" --sortie "$SORTIE" --jeton "$GH_TOKEN_FILE" --jeton "$HC_TOKEN_FILE" \
       --meta "$meta" ${SANS_RETRAIT:+--sans-retrait}; then
    pousser
  else
    echo "ARRÊT SÉCURITÉ : poussée refusée par le contrôle des jetons"
  fi
}

detruire() {
  set +e
  if [ "$DETRUIRE" != oui ] || [ "$SERVER_ID" = inconnu ]; then
    echo "autodestruction non jouée (DETRUIRE=$DETRUIRE, identifiant=$SERVER_ID)"
    return 0
  fi
  local i code
  for i in 1 2 3 4 5; do
    code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 30 -X DELETE -H @"$ENTETE_HC" \
      "$HCLOUD_API/servers/$SERVER_ID")"
    echo "DELETE servers/$SERVER_ID -> $code ($(date -u +%Y-%m-%dT%H:%M:%SZ))"
    case "$code" in 200|201|202|204|404) return 0 ;; esac
    sleep $((i * 10))
  done
}

trap sur_term TERM
trap 'conclure; detruire' EXIT
( sleep "$PLAFOND_SECONDES" && kill -TERM "$$" ) &
GARDIEN=$!

# --- 1. Système (serveur seulement) -------------------------------------------------------------------------------
if [ "$(id -u)" = 0 ] && [ "$INSTALLER" = oui ]; then
  ETAPE="systeme"
  systemctl disable --now ssh.socket ssh.service >/dev/null 2>&1 || true
  export DEBIAN_FRONTEND=noninteractive
  timeout 1200 apt-get update -qq && timeout 1200 apt-get install -y -qq git curl ca-certificates python3-venv \
    iptables >/dev/null || exit 10
  id -u "$UTILISATEUR" >/dev/null 2>&1 || useradd -m -s /bin/bash "$UTILISATEUR" || exit 11
  # métadonnées (données de démarrage, donc jetons) interdites à l'utilisateur des essais
  iptables -I OUTPUT -d 169.254.169.254 -m owner --uid-owner "$UTILISATEUR" -j REJECT || exit 12
fi

# --- 2. Interpréteur et dépendances gelées ------------------------------------------------------------------------
ETAPE="python"
if [ "$INSTALLER" = oui ]; then
  "$PY_SYSTEME" -m venv "$TRAVAIL/outil-uv" && timeout 900 "$TRAVAIL/outil-uv/bin/pip" install -q uv || exit 20
  UV="$TRAVAIL/outil-uv/bin/uv"
  if timeout 900 "$UV" python install 3.13 && "$UV" venv -q --python 3.13 "$VENV"; then
    echo "interpréteur : CPython 3.13 par uv ($("$UV" --version))"
  else
    echo "repli : interpréteur du système ($("$PY_SYSTEME" --version))"
    rm -rf "$VENV"; "$PY_SYSTEME" -m venv "$VENV" || exit 21
  fi
  timeout 2400 "$UV" pip install -q --python "$VENV/bin/python" -r "$CONTRAINTES" || exit 22
  chmod -R a+rX "$VENV" "$UV_PYTHON_INSTALL_DIR" 2>/dev/null
  PY_ESSAIS="$VENV/bin/python"
fi
[ -x "$PY_ESSAIS" ] || { echo "ARRÊT : interpréteur des essais absent"; exit 23; }

# --- 3. Code au commit figé ----------------------------------------------------------------------------------------
ETAPE="clonage"
mkdir -p "$DEPOT" && cd "$DEPOT" || exit 30
git init -q && git remote add origin "$DEPOT_URL" || exit 31
if ! timeout 1800 git fetch -q --depth 1 origin "$COMMIT_CODE"; then
  timeout 1800 git fetch -q --depth 50 origin "$BRANCHE_CODE" || exit 32
fi
git checkout -q --detach "$COMMIT_CODE" 2>/dev/null || git checkout -q --detach FETCH_HEAD || exit 33
[ "$(git rev-parse HEAD)" = "$COMMIT_CODE" ] || { echo "ARRÊT : commit inattendu $(git rev-parse HEAD)"; exit 34; }
rm -f .git/config.lock
if [ "$(id -u)" = 0 ]; then chown -R "$UTILISATEUR": "$DEPOT" "$ES"; fi

# --- 4. Environnement consigné -------------------------------------------------------------------------------------
ETAPE="environnement"
{
  echo "date_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "commit=$(git rev-parse HEAD)"; echo "nproc=$NPROC"
  echo "processeur=$(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//')"
  echo "memoire_ko=$(grep -m1 MemTotal /proc/meminfo | awk '{print $2}')"
  echo "python=$("$PY_ESSAIS" --version 2>&1)"; echo "systeme=$(uname -srm)"
} > "$SORTIE/environnement-v1.txt"
"$PY_ESSAIS" -m pip freeze > "$SORTIE/pip-freeze-v1.txt" 2>/dev/null \
  || "$TRAVAIL/outil-uv/bin/uv" pip freeze --python "$PY_ESSAIS" > "$SORTIE/pip-freeze-v1.txt" 2>/dev/null

# --- 5. Phase parallèle, puis réexécution en série des seuls échecs -----------------------------------------------
ETAPE="phase-parallele"
lancer_essais "$ES/journal-pytest-v1.txt" "$PY_ESSAIS" -m pytest -q -n "$NPROC" --dist loadfile --durations=60 \
  --junitxml="$ES/resultats-pytest-v1.xml" -o junit_family=xunit2
CODE_PHASE1=$?
echo "phase parallèle : code $CODE_PHASE1 ($(date -u +%Y-%m-%dT%H:%M:%SZ))"
if [ "$DELAI_DEPASSE" = 0 ] && [ "$CODE_PHASE1" != 0 ] && [ "$CODE_PHASE1" != 5 ]; then
  ETAPE="phase-serie"
  lancer_essais "$ES/journal-reexecution-serie-v1.txt" "$PY_ESSAIS" -m pytest -q -n0 --lf \
    --junitxml="$ES/reexecution-serie-v1.xml" -o junit_family=xunit2
  CODE_PHASE2=$?
  echo "réexécution en série : code $CODE_PHASE2 ($(date -u +%Y-%m-%dT%H:%M:%SZ))"
fi
ETAPE="fin"
exit 0
