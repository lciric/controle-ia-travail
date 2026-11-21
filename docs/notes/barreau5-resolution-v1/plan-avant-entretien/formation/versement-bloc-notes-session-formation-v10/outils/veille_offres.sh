#!/bin/bash
# Recherche d'offres chaque heure (plan de marche, point 1.4) pour une instance en attente ; sort 60 dès qu'une offre passe la
# garde de l'offre du code de course ; n'achète rien.
S=/tmp/claude-0/-home-user-controle-ia-travail/2e5ab823-f39e-5eb7-8014-a7e033a3a8e4/scratchpad; cd $S
while true; do
  I=$(date -u +%Y%m%dT%H%M%SZ)
  $S/venv-vast/bin/vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 gpu_ram>=80 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0 dph_total<=1.30 rentable=true' -o 'dph_total' --raw > b5f/veille-offres-$I.json 2>/dev/null
  n=$($S/venv-b5f/bin/python -I -c '
import json,sys
sys.path.insert(0,sys.argv[2]+"/src")
from controle_ia.barreau5_familles.formation_v1 import exiger_offre
d=json.load(open(sys.argv[1])); d=d.get("offers",d) if isinstance(d,dict) else d
k=0
for x in d:
    try: exiger_offre(x); k+=1
    except Exception: pass
print(k)' b5f/veille-offres-$I.json $S/arbre-course-x1 2>/dev/null)
  echo "$I offres acceptées : ${n:-illisible}" | tee -a b5f/veille-offres.txt
  [ "${n:-0}" -ge 1 ] 2>/dev/null && exit 60
  sleep 3600
done
