#!/bin/bash
# Programme factice rapide (1 ms par source) : n de la mesure contre le nombre réel de dossiers de source après l'arrêt.
# Usage : scen-rapide.sh NOM
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2
N=$1
T=$V/e/$N/tenue
S=$V/e/$N/sorties
M=$V/e/$N/marqueur
mkdir -p "$T"
bash $V/copie-auteur/demarrer-essai-court-v2.sh "$T" $V/v/lanceur-factice-v.sh "$S" 0.001 100000 30 simple "$M"
bash $V/copie-auteur/demarrer-gardien-essai-court-v2.sh "$T" --sorties "$S" --seuil-n 300 --seuil-libre-octets 1 --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5
GP=$(cat "$T/pid-gardien-essai-court.txt")
for i in $(seq 1 60); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s"
grep -E '^(n :|s4|état)' "$T/mesure-essai-court.txt"
echo "dossiers de source réels après coup : $(ls -d $S/etape-4/couche-mecanique/bras-1-a-3/*/*/* | wc -l)"
echo "fichiers réels sous etape-4 : $(find $S/etape-4 -type f | wc -l)"
