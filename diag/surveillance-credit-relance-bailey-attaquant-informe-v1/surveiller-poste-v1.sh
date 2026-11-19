#!/bin/bash
# Lecture seule : attend la disparition du poste v14 (176575468) ; sort a 0 si disparu, 20 apres 100 min.
J="$(dirname "$0")/journal-credit.txt"; T0=$(date +%s)
while :; do
  H=$(date -u +%FT%TZ)
  L=$(curl -sS -m 30 -H "Authorization: Bearer $HCLOUD_TOKEN" https://api.hetzner.cloud/v1/servers | python3 -c "import sys,json;print(' '.join('%s:%s'%(s['id'],s['status']) for s in json.load(sys.stdin)['servers']))" 2>/dev/null)
  C=$(curl -sS -m 30 -H "Authorization: Bearer $VAST_API_KEY" https://console.vast.ai/api/v0/users/current/ | python3 -c "import sys,json;d=json.load(sys.stdin);print('%.4f'%d['credit'])" 2>/dev/null)
  echo "$H hetzner=[$L] credit=$C" >> "$J"
  [ -n "$L" ] && ! echo "$L" | grep -q 176575468 && { echo "SORTIE poste-detruit $H $L"; exit 0; }
  [ $(( $(date +%s) - T0 )) -gt 6000 ] && { echo "SORTIE delai $H $L"; exit 20; }
  sleep 300
done
