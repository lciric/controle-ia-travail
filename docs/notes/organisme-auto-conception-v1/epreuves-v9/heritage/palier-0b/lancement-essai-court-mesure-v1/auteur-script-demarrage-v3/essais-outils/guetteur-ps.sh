#!/bin/bash
# Guetteur de `ps` : toutes les 20 ms, lit les lignes de commande de tous les processus (ps -eww -o pid=,args=) et écrit
# dans SORTIE les seules lignes qui portent le jeton factice (lu dans FICHIER_JETON ; recherche à chaîne fixe), avec
# l'heure ; s'arrête quand FICHIER_ARRET existe ; écrit à la fin le nombre de relevés et de lignes trouvées.
# Emploi : guetteur-ps.sh FICHIER_JETON SORTIE FICHIER_ARRET
set -u
JF=$1; OUT=$2; STOP=$3
: > "$OUT"
k=0; t=0
while [ ! -e "$STOP" ]; do
  L=$(ps -eww -o pid=,args= | grep -F -f "$JF" | grep -v -F "guetteur-ps.sh")
  k=$((k + 1))
  if [ -n "$L" ]; then t=$((t + $(printf '%s\n' "$L" | wc -l))); printf '%s %s\n' "$(date -u +%H:%M:%S.%N)" "$L" >> "$OUT"; fi
  sleep 0.02
done
echo "relevés : $k ; lignes portant le jeton : $t" >> "$OUT"
