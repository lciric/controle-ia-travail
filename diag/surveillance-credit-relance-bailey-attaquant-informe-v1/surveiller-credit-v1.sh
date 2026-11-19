#!/bin/bash
# Surveillance de la relance de Bailey (lecture seule). Sort au seuil (<=2,6), a une recharge (+3 USD),
# si 61170458 n'est plus en marche, si poste-fini-v14.json apparait, ou apres 115 min.
J="$(dirname "$0")/journal-credit.txt"; DEPOT=/home/user/controle-ia-travail
BR=claude/compassionate-meitner-d4ryyk; PREV=""; T0=$(date +%s)
while :; do
  H=$(date -u +%FT%TZ)
  C=$(curl -sS -m 30 -H "Authorization: Bearer $VAST_API_KEY" https://console.vast.ai/api/v0/users/current/ | python3 -c "import sys,json;d=json.load(sys.stdin);print('%.4f %s'%(d['credit'],d['billing_failed']))" 2>/dev/null)
  I=$(curl -sS -m 30 -H "Authorization: Bearer $VAST_API_KEY" "https://console.vast.ai/api/v0/instances/61170458/" | python3 -c "import sys,json;d=json.load(sys.stdin);d=d.get('instances',d);print(d.get('actual_status'),d.get('intended_status'))" 2>/dev/null)
  F=$(cd $DEPOT && git fetch -q origin $BR 2>/dev/null && git ls-tree --name-only origin/$BR runs/temoin-bailey-v1-20261111/poste-fini-v14.json; cd $DEPOT && git log -1 --format=%s origin/$BR)
  echo "$H credit=$C inst=$I fin=[$F]" >> "$J"
  CR=${C%% *}
  if [ -n "$CR" ]; then
    python3 -c "import sys;sys.exit(0 if float('$CR')<=2.6 else 1)" && { echo "SORTIE seuil $H $C"; exit 10; }
    [ -n "$PREV" ] && python3 -c "import sys;sys.exit(0 if float('$CR')-float('$PREV')>3 else 1)" && { echo "SORTIE recharge $H $PREV->$CR"; exit 11; }
    PREV=$CR
  else echo "$H relevé du crédit en échec" >> "$J"; fi
  [ -n "$I" ] && [ "$I" != "running running" ] && { echo "SORTIE instance $H $I"; exit 12; }
  echo "$F" | grep -q poste-fini-v14.json && { echo "SORTIE fin $H"; exit 13; }
  [ $(( $(date +%s) - T0 )) -gt 6900 ] && { echo "SORTIE delai $H $C $I"; exit 0; }
  sleep 120
done
