#!/bin/bash
# Relais locaux pour A1, attaque de Goodhart (GO-2026-11-02-07, plafond de course 80 USD) : Kimi port 8804 (relais_kimi_v3.py),
# Argon port 8805 (commande_argon_v56_nuit_v2.py servir), mêmes options que le lanceur de la mini-course v2 du 1er novembre sauf
# plafonds de relais 40 USD chacun (la part par fournisseur, PLAFOND_ETAPE_USD du texte scellé), max-appels 1000. Clés par nom
# sous env -i, jamais en argument ni en fichier. PID écrits ; vérifiés par /proc (R10). Les relais restent actifs jusqu'à
# leur arrêt par PID (arreter-relais-a1-v1.sh). Session fille, 2 novembre 2026.
set -uo pipefail; set +x
cd "$(dirname "$0")"; D="$PWD"
REPO=/home/user/controle-ia-travail; K=$REPO/docs/notes/ideation-organisme-v1/relais-kimi-v1
N=$REPO/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit; PY=/usr/bin/python3
for v in KIMI_API_KEY GEMINI_API_KEY_2; do [ -n "${!v:-}" ] || { echo "$v absente" >&2; exit 2; }; done
(cd $K && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
for f in relais-kimi.pid relais-argon.pid; do [ ! -e "$f" ] || { echo "$f existe (R12)" >&2; exit 2; }; done
for p in 8804 8805; do $PY -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$p)) else 1)" || { echo "port $p pris" >&2; exit 2; }; done
setsid env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" \
  $PY -I -B "$K/relais_kimi_v3.py" --port 8804 --modeles-permis kimi-k3.1-pro --plafond-usd 40 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 1000 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1700 \
  --delai-silence-s 600 --journal "$D/relais-kimi-journal.jsonl" > "$D/relais-kimi.log" 2>&1 < /dev/null &
PID_K=$!; echo $PID_K > relais-kimi.pid
MANDATAIRE_A=(HTTPS_PROXY="${HTTPS_PROXY:-}")
for v in https_proxy NO_PROXY no_proxy; do [ -n "${!v:-}" ] && MANDATAIRE_A+=("$v=${!v}"); done
setsid env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" "${MANDATAIRE_A[@]}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" \
  $PY -I -B "$N/commande_argon_v56_nuit_v2.py" servir --port 8805 --plafond-usd 40 --max-appels 1000 \
  --journal "$D/relais-argon-journal.jsonl" > "$D/relais-argon.log" 2>&1 < /dev/null &
PID_A=$!; echo $PID_A > relais-argon.pid
sleep 1
tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais Kimi (R10)" >&2; exit 3; }
tr '\0' ' ' < /proc/$PID_A/cmdline | grep -q "commande_argon_v56_nuit_v2.py servir" || { echo "PID $PID_A n'est pas le relais Argon (R10)" >&2; exit 3; }
for p in 8804 8805; do i=0; until $PY -I -c "import urllib.request; urllib.request.build_opener(urllib.request.ProxyHandler({})).open('http://127.0.0.1:$p/relais/etat', timeout=2)" 2>/dev/null; do
  i=$((i+1)); [ $i -lt 30 ] || { echo "relais du port $p non prêt" >&2; exit 3; }; sleep 1; done; done
echo "$(date -u +%FT%TZ) relais Kimi PID $PID_K (8804, 40 USD) ; relais Argon PID $PID_A (8805, 40 USD) : prêts"
