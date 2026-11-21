#!/bin/bash
# Contre-lecteur : guetteur de l'ENVIRONNEMENT et de la ligne de commande de tous les processus (canal que le guetteur de `ps`
# de l'auteur ne couvre pas : /proc/PID/environ). Toutes les 50 ms, pour chaque processus lisible, cherche le jeton factice
# (chaîne fixe, lue dans FICHIER_JETON) dans /proc/PID/environ et /proc/PID/cmdline. Écrit dans SORTIE chaque trouvaille
# (heure, identifiant, canal, nom du programme) ; s'arrête quand FICHIER_ARRET existe ; écrit à la fin le nombre de balayages,
# de processus lus et de trouvailles.
# Emploi : guetteur-environ.sh FICHIER_JETON SORTIE FICHIER_ARRET
set -u
JF=$1; OUT=$2; STOP=$3
: > "$OUT"
k=0; lus=0; trouves=0
MOI=$$
while [ ! -e "$STOP" ]; do
  k=$((k + 1))
  for d in /proc/[0-9]*; do
    p=${d#/proc/}
    [ "$p" = "$MOI" ] && continue
    for canal in environ cmdline; do
      [ -r "$d/$canal" ] || continue
      lus=$((lus + 1))
      if grep -q -a -F -f "$JF" "$d/$canal" 2>/dev/null; then
        trouves=$((trouves + 1))
        printf '%s pid %s canal %s programme %s\n' "$(date -u +%H:%M:%S.%N)" "$p" "$canal" "$(tr '\0' ' ' < "$d/cmdline" 2>/dev/null | cut -c1-60 | sed "s/$(head -c 12 "$JF")[A-Za-z0-9_-]*/@JETON@/g")" >> "$OUT"
      fi
    done
  done
  sleep 0.05
done
echo "balayages : $k ; lectures de processus : $lus ; trouvailles : $trouves" >> "$OUT"
