#!/bin/bash
# Additif 2 v6 (scellé R-4318), mot de la mère 15:34Z : à l'échéance mécanique de chaque relance (dernière ligne « B5F »
# + 3600 s + 15 min, avant « marche : début »), si aucune ligne « B5F » neuve : arrêt par l'identifiant, sans destruction.
S=/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad; cd $S; V=$S/venv-vast/bin/vastai
for e in "2 61655453 2026-11-20T14:45:03Z 2026-11-20T16:00:03Z" "4 61655585 2026-11-20T14:45:50Z 2026-11-20T16:00:50Z" "3 61655547 2026-11-20T14:46:10Z 2026-11-20T16:01:10Z"; do
  set -- $e; n=$1; id=$2; dern=$3; ech=$4
  until [ "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \> "$ech" ]; do sleep 5; done
  $V logs $id --tail 400 > b5f/logs-muette-$n.txt 2>/dev/null
  neuves=$(grep ' B5F ' b5f/logs-muette-$n.txt | awk -v d="$dern" '$1 > d' | wc -l)
  debut=$(grep -c ' B5F marche : début' b5f/logs-muette-$n.txt)
  etat=$($V show instances --raw 2>/dev/null | python3 -I -c "import json,sys;d=json.load(sys.stdin);d=d.get('instances',d) if isinstance(d,dict) else d;x=[i for i in d if str(i.get('id'))=='$id' and i.get('label')=='b5f-formation-v1-$n'];print(x[0].get('cur_state') if x else 'absente')")
  echo "$(date -u +%FT%TZ) relance $n ($id) : lignes neuves $neuves ; marche : début $debut ; état $etat"
  if [ "$neuves" = 0 ] && [ "$debut" = 0 ] && [ "$etat" = running ]; then
    { echo "export PATH=\"$S/venv-vast/bin:\$PATH\""; echo "GO_ID=GO-2026-11-19-86 vastai stop instance $id"; } > b5f/jouer-arret-muette-$n.sh
    python3 -I outils/essai_garde3.py /home/user/controle-ia-travail b5f/jouer-arret-muette-$n.sh | grep -qx "garde : accepté" || { echo "garde refuse $n"; continue; }
    GO_ID=GO-2026-11-19-86 bash b5f/jouer-arret-muette-$n.sh > b5f/arret-muette-$n.txt 2>&1
    echo "$(date -u +%FT%TZ) relance $n ($id) : arrêt demandé, code $? : $(cat b5f/arret-muette-$n.txt)"
  else
    echo "$(date -u +%FT%TZ) relance $n ($id) : pas d'arrêt (ligne neuve, marche commencée ou état $etat)"
  fi
done
