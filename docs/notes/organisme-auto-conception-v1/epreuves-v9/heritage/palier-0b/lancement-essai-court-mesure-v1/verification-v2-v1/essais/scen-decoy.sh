#!/bin/bash
# Fichiers de tenue périmés désignant un processus sans lien (sleep chef de session). Le gardien, seuil de place impossible,
# doit ne rien signaler. Variante : ECART = décalage ajouté à l'heure de départ écrite ; ECART=ABSENT : pas de fichier d'heure ;
# ECART=0 : heure écrite exacte (témoin de contrôle : le gardien doit alors signaler, c'est le cas « vrai par construction »).
# Usage : scen-decoy.sh NOM ECART
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2
N=$1
ECART=$2
T=$V/e/$N/tenue
S=$V/e/$N/sorties
mkdir -p "$T"
setsid nohup /bin/sleep 120 < /dev/null > /dev/null 2>&1 &
TP=$!
sleep 0.5
STAT=$(cat "/proc/$TP/stat")
RESTE=${STAT##*) }
CH=($RESTE)
TOPS=${CH[19]}
echo "témoin $TP : groupe ${CH[2]}, session ${CH[3]}, départ (tops) $TOPS"
echo "$TP" > "$T/pid-essai-court.txt"
echo "$TP" > "$T/pgid-essai-court.txt"
cat /proc/sys/kernel/random/boot_id > "$T/boot-id-essai-court.txt"
date -u > "$T/heure-lancement-essai-court.txt"
if [ "$ECART" != ABSENT ]; then
  echo $((TOPS + ECART)) > "$T/depart-processus-essai-court.txt"
fi
bash $V/copie-auteur/demarrer-gardien-essai-court-v2.sh "$T" --sorties "$S" --seuil-libre-octets 1000000000000000000 --intervalle-s 1 --delai-force-s 3
GP=$(cat "$T/pid-gardien-essai-court.txt")
sleep 6
echo "témoin $TP : $(stat -c %n /proc/$TP 2>/dev/null || echo absent)"
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent)"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt" 2>/dev/null || echo "(absent)"
echo "--- journal :"
head -n 3 "$T/journal-de-tenue-essai-court.txt"
echo "$TP" > "$T/temoin.pid"
echo "$GP" > "$T/gardien.pid"
