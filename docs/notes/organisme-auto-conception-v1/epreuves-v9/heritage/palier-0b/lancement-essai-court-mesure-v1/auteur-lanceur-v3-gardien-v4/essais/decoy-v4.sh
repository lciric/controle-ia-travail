#!/bin/bash
# Garde d'identité (contre-lecture « decoy », vérifications « scen-decoy » et « decoy3 ») sur le gardien v4 : les fichiers de
# tenue désignent un témoin sans lien (setsid sleep 120, chef de session). ECART : décalage ajouté à son heure de départ
# écrite ; ABSENT : pas de fichier d'heure ; 0 : heure exacte (objet vrai par construction : le gardien doit alors signaler le
# témoin). Déclencheur : MOTIF place (seuil impossible, comme en v3) ou duree (heure d'arrêt de durée déjà passée de peu :
# nouveauté v4, même voie d'arrêt).
# Usage : decoy-v4.sh NOM ECART [place|duree]
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
PY=/home/user/controle-ia-travail/.venv/bin/python
NOM=$1
ECART=$2
MOTIF=${3:-place}
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
echo "témoin $TP : groupe ${CH[2]}, session ${CH[3]}, départ (tops) $TOPS ; écart $ECART ; déclencheur $MOTIF"
echo "$TP" > "$T/pid-essai-3.txt"
echo "$TP" > "$T/pgid-essai-3.txt"
cat /proc/sys/kernel/random/boot_id > "$T/boot-id-essai-3.txt"
date -u > "$T/heure-lancement-essai-3.txt"
if [ "$ECART" != ABSENT ]; then
  echo $((TOPS + ECART)) > "$T/depart-processus-essai-3.txt"
fi
if [ "$MOTIF" = duree ]; then
  H=$(date -u -d "@$(( $(date -u +%s) + 1 ))" +%Y-%m-%dT%H:%M:%SZ)
  bash "$B/demarrer-gardien-essai-3-v4.sh" "$T" "$PY" --sorties "$D/sorties" --heure-arret-duree "$H" --seuil-libre-octets 1 --intervalle-s 1 --delai-force-s 3
else
  H=$(date -u -d "@$(( $(date -u +%s) + 3600 ))" +%Y-%m-%dT%H:%M:%SZ)
  bash "$B/demarrer-gardien-essai-3-v4.sh" "$T" "$PY" --sorties "$D/sorties" --heure-arret-duree "$H" --seuil-libre-octets 1000000000000000000 --intervalle-s 1 --delai-force-s 3
fi
GP=$(cat "$T/pid-gardien-essai-3.txt")
sleep 6
echo "témoin $TP après 6 s : $(stat -c %n /proc/$TP 2>/dev/null || echo ABSENT)"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt" 2>/dev/null || echo "(absent)"
echo "--- journal (début) :"
head -n 2 "$T/journal-de-tenue-essai-3.txt" | cut -c1-400
if [ -e "/proc/$TP" ]; then kill "$TP"; sleep 2; echo "témoin arrêté par moi par son identifiant : $(stat -c %n /proc/$TP 2>/dev/null || echo absent)"; fi
for i in $(seq 1 10); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent)"
tail -n 1 "$T/journal-de-tenue-essai-3.txt" | cut -c1-400
