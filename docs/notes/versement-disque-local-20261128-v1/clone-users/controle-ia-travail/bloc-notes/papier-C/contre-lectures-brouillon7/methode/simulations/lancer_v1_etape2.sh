#!/bin/sh
# Etape 2 du lancement de V1 (la premiere, R = 2000, a ete arretee par le PID de son xargs apres les quatre cases Z0,
# par manque de processeur partage) : cases restantes a R = 1000 essais (minimum de la clause), B = 1000, graine 20261021.
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
cat cellules_v1_etape2.txt | xargs -P 4 -L 1 sh -c 'python3 -B v1_grille_trois_lectures_v1.py "$0" "$1" "$2" 1000 1000 20261021 > "sorties_v1/v1_$0_k$1_T$2.txt" 2>&1'
