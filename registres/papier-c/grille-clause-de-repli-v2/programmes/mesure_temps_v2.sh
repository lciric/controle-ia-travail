#!/bin/bash
# Mesure de faisabilite (consigne, regle 4) : temps d'une case de chaque sorte, sur un petit nombre d'essais, avec une
# graine DISTINCTE de toute case (passe 9), sorties sous mesure-temps/. Ces sorties ne sont pas des cases : seule la
# duree est lue ; elles n'entrent dans aucune table.
# Sortes : C-P3c a T = 30 (k = 5, la plus lourde ; 400 essais) ; C-P3a et C-P3b a T = 30 (k = 5 ; 40 essais) ;
# C-P3a et C-P3b a T = 60 (k = 5, modele E40 ; 40 essais). Un processus a la fois (le lot en fera quatre).
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
PY=/usr/local/bin/python3
M=../mesure-temps
mkdir -p $M
mesure() {  # nom, puis la commande
  local nom=$1; shift
  local t0=$(date +%s.%N)
  "$@" 2> $M/$nom.err
  local t1=$(date +%s.%N)
  echo "$nom $(echo "$t1 - $t0" | bc) s horloge" >> $M/temps_v2.txt
}
: > $M/temps_v2.txt
mesure c_MH_g20_k5_T30_p9 $PY -B grille_c_v2.py MH g20 5 30 400 9 $M/c_MH_g20_k5_T30_p9.json
mesure ab_MH_g20_k5_T30_p9 $PY -B grille_ab_v2.py MH g20 5 30 40 1000 9 $M/ab_MH_g20_k5_T30_p9.json
mesure ab_E40_g20_k5_T60_p9 $PY -B grille_ab_v2.py E40 g20 5 60 40 1000 9 $M/ab_E40_g20_k5_T60_p9.json
