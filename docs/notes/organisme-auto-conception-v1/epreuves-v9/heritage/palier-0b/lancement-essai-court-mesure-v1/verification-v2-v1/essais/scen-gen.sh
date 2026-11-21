#!/bin/bash
# Scénario générique : programme factice en MODE, gardien avec SEUIL_N et SEUIL_LIBRE ; attend la fin du gardien ; rend le
# journal d'arrêt, la mesure, l'état de l'enfant (identifiant lu dans MARQUEUR.pid), puis la croissance du marqueur.
# Usage : scen-gen.sh NOM MODE SEUIL_N SEUIL_LIBRE_OCTETS
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2
N=$1
MODE=$2
SN=$3
SL=$4
T=$V/e/$N/tenue
S=$V/e/$N/sorties
M=$V/e/$N/marqueur
mkdir -p "$T"
bash $V/copie-auteur/demarrer-essai-court-v2.sh "$T" $V/v/lanceur-factice-v.sh "$S" 0.5 1000 60 "$MODE" "$M"
bash $V/copie-auteur/demarrer-gardien-essai-court-v2.sh "$T" --sorties "$S" --seuil-n "$SN" --seuil-libre-octets "$SL" --duree-etape-4-s 100000 --intervalle-s 1 --delai-force-s 5
GP=$(cat "$T/pid-gardien-essai-court.txt")
for i in $(seq 1 80); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt" 2>/dev/null || echo "(absent)"
CP=$(cat "$M.pid" 2>/dev/null || echo "")
if [ -n "$CP" ]; then
  echo "enfant $CP : $(stat -c %n /proc/$CP 2>/dev/null || echo absent)"
  A=$(wc -l < "$M"); sleep 3; B=$(wc -l < "$M")
  echo "marqueur : $A lignes, puis $B lignes 3 s plus tard"
fi
echo "--- code-de-sortie : $(cat $T/code-de-sortie.txt 2>/dev/null || echo absent)"
