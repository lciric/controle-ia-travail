#!/bin/bash
# Lanceur « espèce seule » v3 (relance ESPECE_SEULE_RELANCE transmise) (mode « tel quel », GO-2026-11-01-10) (session-depot, 1er novembre 2026) : un appel d'Argon (C) ou de Kimi (D) sur une question et ses faits.
# Usage : GO_ID=GO-… bash lancer-espece-seule-v2.sh LETTRE --tel-quel FICHIER SORTIE PLAFOND_USD (ou QUESTION FAITS comme v1)
# Argon : clé par variable sous env -i (GEMINI_API_KEY_2 → GEMINI_API_KEY). Kimi : relais local relais_kimi_v3.py lancé sous env -i avec
# sa seule clé (KIMI_API_KEY), PID vérifié (R10), arrêté par trap ; le script ne voit aucune clé Kimi. Garde de pire cas dans
# espece_seule_v1.py. Aucune clé en argument ni en fichier. Sans `set -e`.
set -uo pipefail; set +x
cd "$(dirname "$0")"
GO_ID="${GO_ID:?GO_ID absent}"; L="${1:?lettre}"; Q="${2:?question}"; F="${3:?faits}"; S="${4:?sortie}"; P="${5:?plafond}"
grep -q "| $GO_ID |" /home/user/controle-ia-travail/registres/go.md || { echo "$GO_ID absent de registres/go.md" >&2; exit 2; }
sha256sum -c --quiet collisionneur_v7.py.sha256 espece_seule_v3.py.sha256 || { echo "empreintes non conformes" >&2; exit 2; }
[ ! -e "$S" ] || { echo "$S existe déjà (R12)" >&2; exit 2; }
PY=/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/collisionneur-venv/bin/python
[ -x "$PY" ] && "$PY" -I -c "import anthropic" 2>/dev/null || { echo "python du collisionneur absent" >&2; exit 2; }
PID_K=""; PORT=${PORT_KIMI:-8803}
arreter() { [ -n "$PID_K" ] || return 0; local i=0; kill "$PID_K" 2>/dev/null; while kill -0 "$PID_K" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done; kill -0 "$PID_K" 2>/dev/null && kill -9 "$PID_K" 2>/dev/null; true; }
trap arreter EXIT; trap 'arreter; exit 130' INT TERM HUP
ENVI=(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=$GO_ID ESPECE_SEULE_RELANCE="${ESPECE_SEULE_RELANCE:-0}" HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}")
if [ "$L" = "C" ]; then
  [ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
  ENVI+=(GEMINI_API_KEY="$GEMINI_API_KEY_2")
elif [ "$L" = "D" ]; then
  [ -n "${KIMI_API_KEY:-}" ] || { echo "KIMI_API_KEY absente" >&2; exit 2; }
  K=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1
  (cd $K && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
  python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$PORT)) else 1)" || { echo "port $PORT déjà pris" >&2; exit 2; }
  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
    python3 -I -B $K/relais_kimi_v3.py --port $PORT --modeles-permis kimi-k3.1-pro --plafond-usd "$P" --reserve-par-appel 0.05 \
    --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 2 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1800 \
    --delai-silence-s 600 --journal "$PWD/$S-relais-journal.jsonl" > "$PWD/$S-relais.log" 2>&1 &
  PID_K=$!; sleep 1; tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais (R10)" >&2; exit 3; }
  i=0; until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$PORT/relais/etat', timeout=2)" 2>/dev/null; do i=$((i+1)); [ $i -lt 30 ] || { echo "relais Kimi non prêt" >&2; exit 3; }; sleep 1; done
  ENVI+=(KIMI_RELAIS_URL=http://127.0.0.1:$PORT)
else echo "lettre C ou D" >&2; exit 2; fi
code=0
"${ENVI[@]}" timeout 2100 "$PY" -I -B espece_seule_v3.py "$L" "$Q" "$F" "$S" "$P" || code=$?
for v in GEMINI_API_KEY_2 KIMI_API_KEY; do grep -rqF -- "${!v}" "$S" "$S-relais.log" 2>/dev/null && echo "ALERTE : $v trouvée dans une sortie" >&2; done
(cd "$S" && sha256sum manifeste.json reponse.md prompt.txt > empreintes.sha256) 2>/dev/null
arreter; trap - EXIT; echo "code $code"; exit $code
