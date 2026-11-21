#!/bin/bash
# Veille légère du crédit : relevé toutes les 1800 s ; sort 10 si crédit < SEUIL, 20 si une hausse (recharge) est vue.
S=/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad; V=$S/venv-vast/bin/vastai
SEUIL=${SEUIL:-1.5}; prec=""
while true; do
  c=$($V show user --raw 2>/dev/null | python3 -I -c "import json,sys;print(round(float(json.load(sys.stdin)['credit']),2))" 2>/dev/null)
  echo "$(date -u +%FT%TZ) crédit ${c:-illisible}" | tee -a $S/b5f/veille-credit.txt
  if [ -n "$c" ]; then
    python3 -I -c "import sys;sys.exit(0 if float(sys.argv[1])<float(sys.argv[2]) else 1)" $c $SEUIL && exit 10
    [ -n "$prec" ] && python3 -I -c "import sys;sys.exit(0 if float(sys.argv[1])>float(sys.argv[2])+0.5 else 1)" $c $prec && exit 20
    prec=$c
  fi
  sleep 1800
done
