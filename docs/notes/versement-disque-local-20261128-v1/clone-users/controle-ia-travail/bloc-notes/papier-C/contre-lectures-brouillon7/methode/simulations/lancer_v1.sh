#!/bin/sh
# Lance V1 sur toutes les cases de cellules_v1.txt, quatre a la fois ; R = 2000 essais, B = 1000 tirages, graine 20261021.
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
cat cellules_v1.txt | xargs -P 4 -L 1 sh -c 'python3 -B v1_grille_trois_lectures_v1.py "$0" "$1" "$2" 2000 1000 20261021 > "sorties_v1/v1_$0_k$1_T$2.txt" 2>&1'
