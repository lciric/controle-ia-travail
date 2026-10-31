#!/bin/bash
# SUITE1 de run-question-7-e3-v1 (Kimi coupé par l amont, R-870) : cellules valides gardées, appel de contrôle non refait, relais Kimi neuf. Dernière reprise de la nuit.
# Tour du collisionneur v7 sur la QUESTION 7 de conv-audit (n° 264 et 268), forme arbitre, pièces copiées de canal/conv-audit-n04 ; GO-2026-10-30-17 (poste 3 ou 4, plafond du run 20 USD ; devis 33,7 USD au pire cas, ≈ 15 attendus) ; R-831 sur les refus.
# Tour du collisionneur v6 (quatre espèces : Fable 5.1, Opus 4.6, Argon, Kimi K3.1 Pro), étage III, trois tours, sur la question
# du texte III de la course 2 (brainstorm, R-824, R-826). GO-2026-10-30-11 (mot direct de Lazar). Plafond du tour 25 USD
# (tour comparable à trois espèces : 8,37 USD) ; relais Kimi v3 plafonné à 8 USD en plus de ce compte (borne indépendante).
# Clés par variable sous env -i (RR_ANTHROPIC_API_KEY_3, GEMINI_API_KEY_2, KIMI_API_KEY), jamais en argument ni en fichier ;
# le collisionneur ne voit aucune clé Kimi (relais local, port 8790). Un refus arrête le tour (R-750). Relais arrêté par PID (R10).
set -uo pipefail; set +x
[ ! -e relais-kimi-question-7-suite1-journal-v1.jsonl ] || { echo "suite déjà lancée (R12)" >&2; exit 2; }
cd "$(dirname "$0")"
GO_ID=GO-2026-10-30-17
for v in RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 KIMI_API_KEY; do [ -n "${!v:-}" ] || { echo "$v absente" >&2; exit 2; }; done
[ -d run-question-7-e3-v1 ] || { echo "run-question-7-e3-v1 absent : rien à reprendre" >&2; exit 2; }
sha256sum -c --quiet question-7-allumage-autocatalytique-v1.md.sha256 faits-question-7-v1.md.sha256 collisionneur_v7.py.sha256 appel_controle_v8.py.sha256 \
  || { echo "empreintes non conformes" >&2; exit 2; }
K=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd $K && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
PY=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/collisionneur-priorites/venv/bin/python
[ -x "$PY" ] && "$PY" -I -c "import anthropic" 2>/dev/null || { echo "python du collisionneur absent ou sans anthropic" >&2; exit 2; }
python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',8790)) else 1)" || { echo "port 8790 déjà pris" >&2; exit 2; }
# relais Kimi v3 : commande simple en arrière-plan, $! = PID de python (env l'exécute)
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  python3 -I -B $K/relais_kimi_v3.py --port 8790 --modeles-permis kimi-k3.1-pro --plafond-usd 4 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 8 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1800 \
  --delai-silence-s 600 --journal "$PWD/relais-kimi-question-7-suite1-journal-v1.jsonl" > "$PWD/relais-kimi-question-7-suite1-v1.log" 2>&1 &
PID_K=$!; echo $PID_K > relais-kimi-question-7-suite1-v1.pid
arreter() { local i=0; kill "$PID_K" 2>/dev/null; while kill -0 "$PID_K" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done
  kill -0 "$PID_K" 2>/dev/null && kill -9 "$PID_K" 2>/dev/null; true; }
trap arreter EXIT; trap 'arreter; exit 130' INT TERM HUP
sleep 1; tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais (R10)" >&2; exit 3; }
i=0; until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8790/relais/etat', timeout=2)" 2>/dev/null; do
  i=$((i+1)); [ $i -lt 30 ] || { echo "relais Kimi non prêt" >&2; exit 3; }; sleep 1; done
ENVI=(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=$GO_ID KIMI_RELAIS_URL=http://127.0.0.1:8790
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}"
  SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}"
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2")
code=0
"${ENVI[@]}" timeout 10800 "$PY" -I -B collisionneur_v7.py etage3 --sortie run-question-7-e3-v1 --faits faits-question-7-v1.md \
    --question question-7-allumage-autocatalytique-v1.md --plafond-usd 20 || code=$?
python3 -I -c "import json,urllib.request; print(json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:8790/relais/etat')))[:900])" \
  > relais-kimi-question-7-suite1-etat-final-v1.txt 2>/dev/null || true
arreter; trap - EXIT; echo "relais Kimi arrêté : PID $PID_K ; code du tour $code"
for f in question-7-v1.json relais-kimi-question-7-suite1-journal-v1.jsonl relais-kimi-question-7-suite1-v1.log relais-kimi-question-7-suite1-etat-final-v1.txt; do
  [ -e "$f" ] && sha256sum "$f" > "$f.sha256"; done
grep -rqF -- "$KIMI_API_KEY" run-question-7-e3-v1 relais-kimi-question-7-suite1-v1.log 2>/dev/null && echo "ALERTE : clé Kimi trouvée dans une sortie" >&2
exit $code
