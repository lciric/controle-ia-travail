#!/bin/bash
# attendre-puis-lancer-v1.sh — file d'attente des tours du collisionneur (session-depot, 30 octobre 2026).
# Attend qu'aucun tour (collisionneur_v6.py etage3) ne tourne et que le port 8790 du relais Kimi soit libre, puis lance le lanceur donné.
# Usage : bash attendre-puis-lancer-v1.sh LANCEUR JOURNAL [variables d'environnement déjà posées : GO_ID, ABSENTS…]
# Attente seulement : aucun arrêt de processus ici (R10 : les arrêts se font par PID dans les lanceurs eux-mêmes).
set -u
L=$1; J=$2
[ -f "$L" ] || { echo "lanceur absent : $L" >&2; exit 2; }
i=0
while pgrep -f "collisionneur_v6.py etage3" >/dev/null || ! python3 -I -c "import socket,sys; sys.exit(0 if socket.socket().connect_ex(('127.0.0.1',8790)) else 1)"; do
  sleep 30; i=$((i+1)); [ $i -le 720 ] || { echo "attente de plus de 6 h : abandon" >&2; exit 3; }
done
echo "file d'attente : lancement de $L à $(date -u +%H:%M:%S) après $((i/2)) min d'attente"
exec bash "$L" > "$J" 2>&1
