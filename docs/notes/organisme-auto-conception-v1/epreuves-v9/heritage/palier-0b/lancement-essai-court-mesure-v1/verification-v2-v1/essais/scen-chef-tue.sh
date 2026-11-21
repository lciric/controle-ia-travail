#!/bin/bash
# Le chef (lanceur factice) est tué par moi (identifiant), l'interpréteur du programme factice (descendant) reste vivant.
# Question : le gardien v2 laisse-t-il vivre le descendant sans plus de garde ?
# Usage : scen-chef-tue.sh NOM
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2
N=$1
T=$V/e/$N/tenue
S=$V/e/$N/sorties
M=$V/e/$N/marqueur
mkdir -p "$T"
bash $V/copie-auteur/demarrer-essai-court-v2.sh "$T" $V/v/lanceur-factice-v.sh "$S" 0.5 1000 60 simple "$M"
bash $V/copie-auteur/demarrer-gardien-essai-court-v2.sh "$T" --sorties "$S" --seuil-n 1000 --seuil-libre-octets 1 --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5
sleep 4
CHEF=$(cat "$T/pid-essai-court.txt")
echo "chef $CHEF tué par moi (SIGKILL)"
kill -9 "$CHEF"
sleep 4
GP=$(cat "$T/pid-gardien-essai-court.txt")
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent)"
echo "--- fin du journal de tenue :"
tail -n 4 "$T/journal-de-tenue-essai-court.txt"
echo "--- arret-gardien.txt : $( [ -f "$T/arret-gardien.txt" ] && echo présent || echo absent)"
