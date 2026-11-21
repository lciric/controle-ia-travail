#!/bin/bash
# Un petit-enfant B (session à part, parent mort avant tout relevé) écrit sous etape-4 ; le gardien arrête le programme par n.
# Questions : B est-il arrêté ? mesure-essai-court.txt dit-il « figé » ? n et s4 changent-ils ensuite ?
# Usage : scen-orphelin.sh NOM
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2
N=$1
T=$V/e/$N/tenue
S=$V/e/$N/sorties
M=$V/e/$N/marqueur
mkdir -p "$T"
bash $V/copie-auteur/demarrer-essai-court-v2.sh "$T" $V/v/lanceur-factice-v.sh "$S" 0.5 1000 60 orphelin "$M"
bash $V/copie-auteur/demarrer-gardien-essai-court-v2.sh "$T" --sorties "$S" --seuil-n 8 --seuil-libre-octets 1 --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5
GP=$(cat "$T/pid-gardien-essai-court.txt")
for i in $(seq 1 60); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s"
echo "--- mesure-essai-court.txt :"
cat "$T/mesure-essai-court.txt"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt"
BP=$(cat "$M.pid")
echo "B : processus $BP : $(stat -c %n /proc/$BP 2>/dev/null || echo absent)"
echo "n et dossiers de source maintenant : $(ls -d $S/etape-4/couche-mecanique/bras-1-a-3/*/*/* | wc -l)"
sleep 3
echo "n et dossiers de source 3 s plus tard : $(ls -d $S/etape-4/couche-mecanique/bras-1-a-3/*/*/* | wc -l)"
echo "B 3 s plus tard : $(stat -c %n /proc/$BP 2>/dev/null || echo absent)"
