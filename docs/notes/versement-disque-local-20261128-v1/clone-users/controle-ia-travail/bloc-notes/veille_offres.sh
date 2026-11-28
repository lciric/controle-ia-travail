#!/usr/bin/env bash
# Veille en lecture seule des offres conformes au filtre du lanceur des notations ; sort (code 0) dès qu'une offre
# A100 SXM4 sur AMD EPYC 7513 à au plus 1,30 USD de l'heure apparaît ; code 1 après le nombre de tours donné.
B=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
TOURS=${1:-60}
for i in $(seq 1 "$TOURS"); do
    r=$("$B/venv-vastai/bin/vastai" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw 2>/dev/null | python3 -I -c '
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
ok = [o for o in d if o.get("gpu_name") == "A100 SXM4" and o.get("cpu_name") == "AMD EPYC 7513 32-Core Processor"
      and isinstance(o.get("dph_total"), (int, float)) and float(o["dph_total"]) <= 1.30]
for o in ok:
    print(o["id"], "machine", o.get("machine_id"), round(float(o["dph_total"]), 4), "USD/h")')
    if [ -n "$r" ]; then echo "$(date -u +%FT%TZ) offre(s) conforme(s) :"; echo "$r"; exit 0; fi
    sleep 120
done
echo "$(date -u +%FT%TZ) aucune offre conforme après $TOURS tours"; exit 1
