#!/bin/bash
# Rejeu de la grille de la clause de repli de P-021 pour C-P3a et C-P3b, trois lectures (programme U3 de l'archive).
# 24 cases : scénarios nuls N0 à N5 × k = 3, 5 × T = 45, 60 ; R = 1000 essais ; B = 1000 tirages ; graine 20261021.
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
for s in N0 N1 N2 N3 N4 N5; do for k in 3 5; do for T in 45 60; do echo "$s $k $T"; done; done; done | \
  xargs -P 4 -L 1 sh -c 'python3 -B u3_lecture_rho_sur_r_v1.py $0 $1 $2 1000 1000 20261021 > sorties/u3_$0_k$1_T$2.txt 2> sorties/u3_$0_k$1_T$2.err'
echo fini > sorties/FINI
