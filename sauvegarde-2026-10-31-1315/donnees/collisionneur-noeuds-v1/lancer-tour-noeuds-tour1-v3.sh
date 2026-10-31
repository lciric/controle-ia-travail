#!/bin/bash
# SUITE de run-noeuds-tour1-e3-v1 (GO-2026-10-31-06, plafond du tour 22 USD) après l'arrêt du 31 octobre ≈ 12:54 UTC.
# Cause de l'arrêt (R-919) : les scripts v1 et v2 passaient OPENAI_BASE_URL au lieu de KIMI_RELAIS_URL (et v1 passait
# GOOGLE_API_KEY au lieu de GEMINI_API_KEY, R-918) ; le collisionneur a cherché Kimi sur son port par défaut 8789.
# v3 reprend le gabarit éprouvé (collisionneur-idee-p041-bonne-v1/lancer-tour-idee-p041-bonne-suite1-v1.sh) : relais Kimi
# sous env -i avec sa seule clé, PID vérifié (R10), relais prêt, empreintes vérifiées. Ajout : contrôle préalable, dans
# l'environnement exact du collisionneur, des variables qu'il lit (par nom seulement) et du relais à l'adresse qu'il lit.
# Cellules valides gardées (A, B, C du tour 1) ; appel de contrôle non refait.
# Clés par variable sous env -i (RR_ANTHROPIC_API_KEY_3, GEMINI_API_KEY_2, KIMI_API_KEY), jamais en argument ni en fichier ;
# le collisionneur ne voit aucune clé Kimi (relais local, port 8793). R-831 : aucune absence acceptée d'avance (Fable a répondu
# au tour 1) ; un refus de Fable ou d'Opus 4.6 arrête le tour et la reprise passera --accepter-absence ; un refus d'Argon ou de
# Kimi arrête et attend Lazar. Relais arrêté par PID (R10).
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e relais-kimi-noeuds-tour1-journal-v3.jsonl ] || { echo "suite v3 déjà lancée (R12)" >&2; exit 2; }
GO_ID=GO-2026-10-31-06
PORT=8793
RUN=run-noeuds-tour1-e3-v1
C=/home/user/controle-ia-travail/donnees/collisionneur-texte-III-v1
for v in RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 KIMI_API_KEY; do [ -n "${!v:-}" ] || { echo "$v absente" >&2; exit 2; }; done
[ -d "$RUN" ] || { echo "$RUN absent : rien à reprendre" >&2; exit 2; }
sha256sum -c --quiet question-noeuds-v10.md.sha256 faits-noeuds-v1.md.sha256 || { echo "empreintes non conformes" >&2; exit 2; }
(cd $C && sha256sum -c --quiet collisionneur_v7.py.sha256) || { echo "collisionneur v7 non conforme" >&2; exit 2; }
K=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd $K && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
PY=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/collisionneur-priorites/venv/bin/python
[ -x "$PY" ] && "$PY" -I -c "import anthropic" 2>/dev/null || { echo "python du collisionneur absent ou sans anthropic" >&2; exit 2; }
python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$PORT)) else 1)" || { echo "port $PORT déjà pris" >&2; exit 2; }
# relais Kimi v3 : commande simple en arrière-plan, $! = PID de python (env l'exécute)
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  python3 -I -B $K/relais_kimi_v3.py --port $PORT --modeles-permis kimi-k3.1-pro --plafond-usd 4 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 8 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1800 \
  --delai-silence-s 600 --journal "$PWD/relais-kimi-noeuds-tour1-journal-v3.jsonl" > "$PWD/relais-kimi-noeuds-tour1-v3.log" 2>&1 &
PID_K=$!; echo $PID_K > relais-kimi-noeuds-tour1-v3.pid
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
# contrôle préalable (v3) : dans l'environnement exact du collisionneur, les variables qu'il lit sont présentes (nom seulement,
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
code=0
"${ENVI[@]}" timeout 6900 "$PY" -I -B $C/collisionneur_v7.py etage3 --sortie $RUN --faits faits-noeuds-v1.md \
    --question question-noeuds-v10.md --plafond-usd 22 || code=$?
python3 -I -c "import json,urllib.request; print(json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:$PORT/relais/etat')))[:900])" \
  > relais-kimi-noeuds-tour1-etat-final-v3.txt 2>/dev/null || true
arreter; trap - EXIT; echo "relais Kimi arrêté : PID $PID_K ; code du tour $code"
for f in relais-kimi-noeuds-tour1-journal-v3.jsonl relais-kimi-noeuds-tour1-v3.log relais-kimi-noeuds-tour1-etat-final-v3.txt; do
  [ -e "$f" ] && sha256sum "$f" > "$f.sha256"; done
for v in RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 KIMI_API_KEY; do
  grep -rqF -- "${!v}" $RUN relais-kimi-noeuds-tour1-v3.log 2>/dev/null && echo "ALERTE : $v trouvée dans une sortie" >&2; done
exit $code
