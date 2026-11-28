#!/usr/bin/env bash
# Veille en lecture seule (aucune création) ; une ligne toutes les 5 minutes.
VA=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/venv-vastai/bin/vastai
W=$(dirname "$(realpath "$0")")
FILTRE="gpu_name=A100_SXM4 gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true"
while true; do
  CR=$("$VA" show user --raw 2>/dev/null | python3 -I -c 'import json,sys; print(json.load(sys.stdin)["credit"])' 2>/dev/null || echo 0)
  "$VA" search offers "$FILTRE" -o 'dph_total' --storage 80 --raw 2>/dev/null | python3 -I "$W/filtre_offres_v2.py" "$CR"
  sleep 300
done
