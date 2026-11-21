#!/bin/bash
# Fichiers de tenue périmés (noms de l'essai 3) désignant un sleep sans lien ; gardien v4 ; heure d'arrêt de durée dans 3 s ;
# seuil de place 1 (non franchi). ECART : décalage de l'heure de départ écrite, ABSENT, ou 0 (heure exacte : contrôle vrai).
# Usage : decoy4.sh NOM ECART
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v4
N=$1
ECART=$2
T=$V/e/$N/tenue
S=$V/e/$N/sorties
PY=/home/user/controle-ia-travail/.venv/bin/python
mkdir -p "$T"
setsid nohup /bin/sleep 120 < /dev/null > /dev/null 2>&1 &
TP=$!
sleep 0.5
STAT=$(cat "/proc/$TP/stat")
RESTE=${STAT##*) }
CH=($RESTE)
TOPS=${CH[19]}
echo "$TP" > "$T/pid-essai-3.txt"
echo "$TP" > "$T/pgid-essai-3.txt"
cat /proc/sys/kernel/random/boot_id > "$T/boot-id-essai-3.txt"
date -u > "$T/heure-lancement-essai-3.txt"
if [ "$ECART" != ABSENT ]; then
  echo $((TOPS + ECART)) > "$T/depart-processus-essai-3.txt"
fi
H=$(date -u -d "@$(( $(date +%s) + 3 ))" +%Y-%m-%dT%H:%M:%SZ)
bash $V/pieces/demarrer-gardien-essai-3-v4.sh "$T" "$PY" --sorties "$S" --heure-arret-duree "$H" --seuil-libre-octets 1 --intervalle-s 1 --delai-force-s 3 > /dev/null
GP=$(cat "$T/pid-gardien-essai-3.txt")
sleep 7
echo "témoin $TP : $(stat -c %n /proc/$TP 2>/dev/null || echo absent)"
echo "gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent)"
echo "--- arret-gardien.txt :"
cat "$T/arret-gardien.txt" 2>/dev/null | cut -c1-260
[ -f "$T/arret-gardien.txt" ] || echo "(absent)"
kill $GP 2>/dev/null
kill $TP 2>/dev/null
sleep 0.5
echo "nettoyage : témoin $(stat -c %n /proc/$TP 2>/dev/null || echo absent) ; gardien $(stat -c %n /proc/$GP 2>/dev/null || echo absent)"
