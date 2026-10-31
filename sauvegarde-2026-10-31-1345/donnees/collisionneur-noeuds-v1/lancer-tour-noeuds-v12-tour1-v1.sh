#!/bin/bash
# Tour 1 du collisionneur v7 (quatre espèces : Fable 5.1, Opus 4.6, Argon, Kimi K3.1 Pro), étage III, trois sous-tours, sur la
# question v12 des nœuds de conv-audit (N1, N3 D-j, N4, N5, N6, N9 D-GK-1, N10, N11 ; `a7fac44b…`), faits v2 assemblés par
# session-depot selon la liste A v6 (`faits-noeuds-v2.md`, `ea85dad6…`, balayage `balayage-faits-noeuds-v2.txt`).
# GO-2026-10-31-06 (45 USD séquencé ; tour 1 plafond de run 22 USD) ; le run v10 (`run-noeuds-tour1-e3-v1`) est arrêté et
# archivé (R-921), ce run est neuf (R12). Gabarit éprouvé (`collisionneur-dml1-v1/lancer-tour-dml1-v1.sh`) : relais Kimi sous
# env -i avec sa seule clé, PID vérifié (R10), relais prêt, empreintes, appel de contrôle des quatre espèces, `trap` à la
# sortie, sans `set -e` ; plus le contrôle préalable de R-919 (variables lues par le collisionneur, par nom ; relais joignable
# à l'adresse lue). R-831 : refus de Fable ou d'Opus 4.6 → absence acceptée pour leurs cellules à la reprise ; refus d'Argon
# ou de Kimi → arrêt, Lazar décide. Clés par variable sous env -i (RR_ANTHROPIC_API_KEY_3, GEMINI_API_KEY_2, KIMI_API_KEY).
set -uo pipefail; set +x
cd "$(dirname "$0")"
GO_ID=GO-2026-10-31-06
PORT=8793
RUN=run-noeuds-v12-tour1-e3-v1
for v in RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 KIMI_API_KEY; do [ -n "${!v:-}" ] || { echo "$v absente" >&2; exit 2; }; done
[ ! -e "$RUN" ] || { echo "$RUN existe déjà (R12)" >&2; exit 2; }
[ ! -e controle-noeuds-v12-v1.json ] || { echo "controle-noeuds-v12-v1.json existe déjà (R12)" >&2; exit 2; }
sha256sum -c --quiet question-noeuds-decisionnels-collisionneur-v12.md.sha256 faits-noeuds-v2.md.sha256 balayage-faits-noeuds-v2.txt.sha256 \
  collisionneur_v7.py.sha256 appel_controle_v8.py.sha256 || { echo "empreintes non conformes" >&2; exit 2; }
K=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd $K && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
PY=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/collisionneur-priorites/venv/bin/python
[ -x "$PY" ] && "$PY" -I -c "import anthropic" 2>/dev/null || { echo "python du collisionneur absent ou sans anthropic" >&2; exit 2; }
python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$PORT)) else 1)" || { echo "port $PORT déjà pris" >&2; exit 2; }
# relais Kimi v3 : commande simple en arrière-plan, $! = PID de python (env l'exécute)
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  python3 -I -B $K/relais_kimi_v3.py --port $PORT --modeles-permis kimi-k3.1-pro --plafond-usd 4 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 8 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1800 \
  --delai-silence-s 600 --journal "$PWD/relais-kimi-noeuds-v12-journal-v1.jsonl" > "$PWD/relais-kimi-noeuds-v12-v1.log" 2>&1 &
PID_K=$!; echo $PID_K > relais-kimi-noeuds-v12-v1.pid
arreter() { local i=0; kill "$PID_K" 2>/dev/null; while kill -0 "$PID_K" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done
  kill -0 "$PID_K" 2>/dev/null && kill -9 "$PID_K" 2>/dev/null; true; }
trap arreter EXIT; trap 'arreter; exit 130' INT TERM HUP
sleep 1; tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais (R10)" >&2; exit 3; }
i=0; until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$PORT/relais/etat', timeout=2)" 2>/dev/null; do
  i=$((i+1)); [ $i -lt 30 ] || { echo "relais Kimi non prêt" >&2; exit 3; }; sleep 1; done
ENVI=(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=$GO_ID KIMI_RELAIS_URL=http://127.0.0.1:$PORT
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}"
  SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}"
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2")
# contrôle préalable (R-919) : dans l'environnement exact du collisionneur, les variables qu'il lit sont présentes (nom seulement,
# aucune valeur affichée) et le relais répond à l'adresse lue dans KIMI_RELAIS_URL ; aucun appel payant.
"${ENVI[@]}" python3 -I -c "
import os, sys, urllib.request
manque = [n for n in ('ANTHROPIC_API_KEY', 'GEMINI_API_KEY', 'KIMI_RELAIS_URL', 'GO_ID') if not os.environ.get(n)]
if manque:
    sys.exit('variables lues par le collisionneur absentes : ' + ', '.join(manque))
url = os.environ['KIMI_RELAIS_URL'].rstrip('/') + '/relais/etat'
urllib.request.build_opener(urllib.request.ProxyHandler({})).open(url, timeout=5).read()
print('contrôle préalable : variables présentes (par nom), relais joignable à KIMI_RELAIS_URL', flush=True)
" || { echo "contrôle préalable en échec" >&2; exit 2; }
"${ENVI[@]}" timeout 600 "$PY" -I -B appel_controle_v8.py collisionneur_v7.py controle-noeuds-v12-v1.json $GO_ID || { echo "appel de contrôle en échec" >&2; exit 2; }
grep -q '"ECHEC"' controle-noeuds-v12-v1.json && { echo "une espèce en échec au contrôle" >&2; exit 2; }
code=0
"${ENVI[@]}" timeout 6900 "$PY" -I -B collisionneur_v7.py etage3 --sortie $RUN --faits faits-noeuds-v2.md \
    --question question-noeuds-decisionnels-collisionneur-v12.md --plafond-usd 22 || code=$?
python3 -I -c "import json,urllib.request; print(json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:$PORT/relais/etat')))[:900])" \
  > relais-kimi-noeuds-v12-etat-final-v1.txt 2>/dev/null || true
arreter; trap - EXIT; echo "relais Kimi arrêté : PID $PID_K ; code du tour $code"
for f in controle-noeuds-v12-v1.json relais-kimi-noeuds-v12-journal-v1.jsonl relais-kimi-noeuds-v12-v1.log relais-kimi-noeuds-v12-etat-final-v1.txt; do
  [ -e "$f" ] && sha256sum "$f" > "$f.sha256"; done
for v in RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 KIMI_API_KEY; do
  grep -rqF -- "${!v}" $RUN relais-kimi-noeuds-v12-v1.log controle-noeuds-v12-v1.json 2>/dev/null && echo "ALERTE : $v trouvée dans une sortie" >&2; done
exit $code
