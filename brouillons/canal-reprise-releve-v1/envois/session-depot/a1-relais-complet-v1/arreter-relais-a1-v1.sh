#!/bin/bash
# Arrêt des relais A1 par PID (R10), après relevé de leur état final.
cd "$(dirname "$0")"
for r in kimi:8804 argon:8805; do n=${r%%:*}; p=${r##*:}; [ -e relais-$n.pid ] || continue; pid=$(cat relais-$n.pid)
  /usr/bin/python3 -I -c "import urllib.request,sys; sys.stdout.write(urllib.request.build_opener(urllib.request.ProxyHandler({})).open('http://127.0.0.1:$p/relais/etat', timeout=5).read().decode())" > etat-final-relais-$n.json 2>/dev/null
  if tr '\0' ' ' < /proc/$pid/cmdline 2>/dev/null | grep -qE 'relais_kimi_v3.py|commande_argon_v56_nuit_v2.py servir'; then kill $pid; i=0
    while kill -0 $pid 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done; kill -0 $pid 2>/dev/null && kill -9 $pid; echo "relais $n arrêté (PID $pid)"; else echo "PID $pid : pas le relais $n, rien d'arrêté"; fi; done
