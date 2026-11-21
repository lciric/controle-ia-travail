#!/bin/bash
# Garde d'identité, fichiers périmés (essai v2) sur le gardien v4 : le vrai script de départ v3 (forme d'essai --lanceur)
# lance un lanceur bref (heure de départ écrite) ; ce processus fini, un témoin sans lien est lancé et les fichiers pid et
# pgid sont réécrits à son identifiant. Attendu : aucun signal ; raison écrite. Usage : decoy-perime-v4.sh NOM
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
PY=/home/user/controle-ia-travail/.venv/bin/python
NOM=$1
D=$E/e/$NOM
T=$D/tenue
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$T"
bash "$B/demarrer-essai-3-v3.sh" --lanceur "$E/lanceur-bref-v4.sh" "$T"
P1=$(cat "$T/pid-essai-3.txt")
for i in $(seq 1 50); do
  if [ ! -e "/proc/$P1" ]; then break; fi
  sleep 0.1
done
echo "premier processus $P1 : $(stat -c %n /proc/$P1 2>/dev/null || echo absent) ; heure de départ écrite $(cat "$T/depart-processus-essai-3.txt")"
setsid nohup /bin/sleep 90 < /dev/null > /dev/null 2>&1 &
P=$!
echo "$P" > "$T/pid-essai-3.txt"
echo "$P" > "$T/pgid-essai-3.txt"
STAT=$(cat /proc/$P/stat)
RESTE=${STAT##*) }
CHAMPS=($RESTE)
echo "témoin $P : heure de départ réelle (tops) ${CHAMPS[19]}"
H=$(date -u -d "@$(( $(date -u +%s) + 1 ))" +%Y-%m-%dT%H:%M:%SZ)
bash "$B/demarrer-gardien-essai-3-v4.sh" "$T" "$PY" --sorties "$D/sorties" --heure-arret-duree "$H" --seuil-libre-octets 1000000000000000000 --intervalle-s 1 --delai-force-s 5
sleep 4
echo "témoin après 4 s : $(stat -c %n /proc/$P 2>/dev/null || echo ABSENT)"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt" 2>/dev/null || echo "(absent)"
echo "--- journal :"
grep -E 'identité|note=' "$T/journal-de-tenue-essai-3.txt" | cut -c1-400
GP=$(cat "$T/pid-gardien-essai-3.txt")
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent)"
kill "$P"
sleep 2
echo "témoin arrêté par moi par son identifiant : $(stat -c %n /proc/$P 2>/dev/null || echo absent)"
