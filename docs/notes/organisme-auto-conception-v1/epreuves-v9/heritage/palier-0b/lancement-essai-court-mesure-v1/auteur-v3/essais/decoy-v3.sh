#!/bin/bash
# Garde d'identité (contre-lecture « decoy » et vérification « scen-decoy ») sur le gardien v3 : les fichiers de tenue désignent
# un témoin sans lien (setsid sleep 120, chef de session). ECART : décalage ajouté à son heure de départ écrite ; ABSENT : pas de
# fichier d'heure ; 0 : heure exacte (objet vrai par construction : le gardien doit alors signaler le témoin).
# Usage : decoy-v3.sh NOM ECART
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
NOM=$1
ECART=$2
D=$E/e/$NOM
T=$D/tenue
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$T"
setsid nohup /bin/sleep 120 < /dev/null > /dev/null 2>&1 &
TP=$!
sleep 0.5
STAT=$(cat "/proc/$TP/stat")
RESTE=${STAT##*) }
CH=($RESTE)
TOPS=${CH[19]}
echo "témoin $TP : groupe ${CH[2]}, session ${CH[3]}, départ (tops) $TOPS ; écart $ECART"
echo "$TP" > "$T/pid-essai-court.txt"
echo "$TP" > "$T/pgid-essai-court.txt"
cat /proc/sys/kernel/random/boot_id > "$T/boot-id-essai-court.txt"
date -u > "$T/heure-lancement-essai-court.txt"
if [ "$ECART" != ABSENT ]; then
  echo $((TOPS + ECART)) > "$T/depart-processus-essai-court.txt"
fi
bash "$B/demarrer-gardien-essai-court-v3.sh" "$T" --sorties "$D/sorties" --seuil-libre-octets 1000000000000000000 --intervalle-s 1 --delai-force-s 3
GP=$(cat "$T/pid-gardien-essai-court.txt")
sleep 6
echo "témoin $TP après 6 s : $(stat -c %n /proc/$TP 2>/dev/null || echo ABSENT)"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt" 2>/dev/null || echo "(absent)"
echo "--- journal (début) :"
head -n 2 "$T/journal-de-tenue-essai-court.txt"
if [ -e "/proc/$TP" ]; then kill "$TP"; sleep 2; echo "témoin arrêté par moi par son identifiant : $(stat -c %n /proc/$TP 2>/dev/null || echo absent)"; fi
for i in $(seq 1 10); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent)"
tail -n 1 "$T/journal-de-tenue-essai-court.txt"
