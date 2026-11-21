#!/bin/bash
# Émule un identifiant repris : le fichier pid/pgid désigne un processus factice sans lien avec le programme, vivant à la prise de garde.
D=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-gardien-palier-0b
A=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-v1
T=$D/e/h2/tenue
mkdir -p "$T"
setsid nohup /bin/sleep 90 < /dev/null > /dev/null 2>&1 &
P=$!
echo "$P" > "$T/pid-essai-court.txt"
echo "$P" > "$T/pgid-essai-court.txt"
cat /proc/sys/kernel/random/boot_id > "$T/boot-id-essai-court.txt"
date -u > "$T/heure-lancement-essai-court.txt"
echo "decoy $P"
bash $A/demarrer-gardien-essai-court-v1.sh "$T" --sorties "$D/e/h2/sorties" --seuil-libre-octets 1000000000000000000 --intervalle-s 1 --delai-force-s 5
sleep 4
stat -c %n /proc/$P || echo "decoy absent"
