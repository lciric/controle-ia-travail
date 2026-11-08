set -u; . /home/user/epreuve-etiqueteur-phase1-v1/variables-v1.sh
P=$(cat "$CONSOLES/lecture-principale.pid")
fin=$(( $(date +%s) + 6900 ))
while kill -0 "$P" 2>/dev/null && [ "$(date +%s)" -lt "$fin" ]; do
  M=$("$PY" -I -c "
import json,sys
d=sys.argv[1]; m=0
for L in 'AB':
    n=0
    try:
        for x in open(f'{d}/reponses-phase1-{L}-v4.encours.jsonl',encoding='utf-8'):
            if x.strip():
                r=json.loads(x)
                if r.get('lecture')=='principale' and r.get('statut')=='illisible': n+=1
    except FileNotFoundError: pass
    m=max(m,n)
print(m)" "$PRINC")
  if [ "$M" -ge 8 ]; then
    echo "$(date -u +%H:%M:%SZ) seuil atteint : $M illisibles pour un lecteur ; arrêt de la lecture $P"
    kill "$P"; timeout 30 tail --pid="$P" -f /dev/null; kill -0 "$P" 2>/dev/null && echo "ARRET : lecture $P toujours vivante" || echo "lecture $P arrêtée"
    exit 0
  fi
  sleep 60
done
kill -0 "$P" 2>/dev/null && echo "$(date -u +%H:%M:%SZ) sentinelle : fin de sa durée, lecture vivante, max illisibles $M" || echo "$(date -u +%H:%M:%SZ) sentinelle : lecture $P finie ou disparue"
