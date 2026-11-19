#!/bin/bash
# Commande restreinte (ls/du) sur 61170458 par l'API du loueur, lecture seule.
R=$(curl -sS -m 60 -X PUT -H "Authorization: Bearer $VAST_API_KEY" -H "Content-Type: application/json" \
  -d "$(python3 -c 'import json,sys;print(json.dumps({"command":sys.argv[1]}))' "$1")" \
  https://console.vast.ai/api/v0/instances/command/61170458/)
U=$(echo "$R" | python3 -c "import sys,json;print(json.load(sys.stdin).get('result_url',''))" 2>/dev/null)
[ -z "$U" ] && { echo "REPONSE: $R"; exit 1; }
for i in $(seq 1 20); do O=$(curl -sS -m 30 "$U"); [ -n "$O" ] && ! echo "$O" | grep -q "<Error>" && { echo "$O"; exit 0; }; sleep 3; done; echo "pas de resultat"
