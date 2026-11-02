#!/bin/bash
# Relance du seul relais Kimi d'A1 (port 8804) après l'arrêt fautif de 10:39:20 UTC par le guetteur v2 (erratum au journal de
# lancement). Mêmes options que relais-a1-attaque-goodhart-v1.sh, sauf plafond 38,77 USD (40 − 1,233 déjà dépensés) et
# journal neuf. À lancer SEULEMENT sur décision de la session mère. Clé par nom sous env -i.
set -uo pipefail; set +x
cd "$(dirname "$0")"; D="$PWD"
REPO=/home/user/controle-ia-travail; K=$REPO/docs/notes/ideation-organisme-v1/relais-kimi-v1; PY=/usr/bin/python3
[ -n "${KIMI_API_KEY:-}" ] || { echo "KIMI_API_KEY absente" >&2; exit 2; }
(cd $K && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
[ ! -e relais-kimi-v2.pid ] || { echo "relais-kimi-v2.pid existe (R12)" >&2; exit 2; }
$PY -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',8804)) else 1)" || { echo "port 8804 pris" >&2; exit 2; }
setsid env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" \
  $PY -I -B "$K/relais_kimi_v3.py" --port 8804 --modeles-permis kimi-k3.1-pro --plafond-usd 38.77 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 997 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1700 \
  --delai-silence-s 600 --journal "$D/relais-kimi-journal-v2.jsonl" > "$D/relais-kimi-v2.log" 2>&1 < /dev/null &
P=$!; echo $P > relais-kimi-v2.pid; sleep 1
tr '\0' ' ' < /proc/$P/cmdline | grep -q relais_kimi_v3.py || { echo "PID $P n'est pas le relais Kimi (R10)" >&2; exit 3; }
i=0; until $PY -I -c "import urllib.request; urllib.request.build_opener(urllib.request.ProxyHandler({})).open('http://127.0.0.1:8804/relais/etat', timeout=2)" 2>/dev/null; do
  i=$((i+1)); [ $i -lt 30 ] || { echo "relais non prêt" >&2; exit 3; }; sleep 1; done
echo "$(date -u +%FT%TZ) relais Kimi relancé, PID $P (8804, plafond 38,77 USD)" | tee -a journal-lancement-a1-v1.log
