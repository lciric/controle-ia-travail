#!/usr/bin/env bash
# Veille en lecture seule des offres conformes au filtre du lanceur de P3 (aucune création) ; une ligne toutes les 5 minutes.
VA=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/venv-vastai/bin/vastai
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
while true; do
  "$VA" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw 2>/dev/null | python3 -I -c '
import json,sys,time
try: o=json.load(sys.stdin)
except Exception: print(time.strftime("%H:%M:%SZ",time.gmtime()), "lecture illisible"); sys.exit()
c=[x for x in o if "EPYC 7513" in (x.get("cpu_name") or "") and (x.get("cpu_cores_effective") or 0)>=16 and (x.get("cpu_ram") or 0)>=128000
   and 0<=(x.get("inet_down_cost") or 0)<=0.05 and 0<=(x.get("storage_total_cost") or 0)<=0.03 and 0<x["dph_total"]<=1.30]
print(time.strftime("%H:%M:%SZ",time.gmtime()), "lues", len(o), "conformes", len(c), " ".join(f"{x[\"id\"]}:{x[\"dph_total\"]:.3f}" for x in c), flush=True)'
  sleep 300
done
