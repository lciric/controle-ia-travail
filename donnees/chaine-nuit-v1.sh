#!/bin/bash
# chaine-nuit-v1.sh — session-depot, 30 octobre 2026 (R-858). Enchaîne les tours du collisionneur un par un, dans un processus
# détaché de la session (la limite de 30 min des tâches de fond de la session a coupé le tour P-041 à 23:00 UTC).
# Ordre : suite du tour P-041 (GO-15), suite du tour bisociation (GO-16 relevé par GO-17), tour 1 de l'arène (GO-13).
# Chaque lanceur vérifie ses empreintes, lance et arrête son propre relais Kimi par PID (R10). Aucun arrêt ici.
set -u
B=/home/user/controle-ia-travail/donnees
J=$B/chaine-nuit-v1.log
run() { local dir=$1 l=$2 j=$3 go=$4 c
  cd "$B/$dir" || { echo "$(date -u +%FT%TZ) $dir absent" >> $J; return; }
  echo "$(date -u +%FT%TZ) début $dir/$l (PID $$)" >> $J
  if sha256sum -c --quiet "$l.sha256"; then GO_ID=$go bash "$l" > "$j" 2>&1; c=$?; else c=99; fi
  echo "$(date -u +%FT%TZ) fin $dir/$l code $c" >> $J; }
run collisionneur-idee-p041-bonne-v1 lancer-tour-idee-p041-bonne-suite1-v1.sh journal-tour-idee-p041-bonne-suite1-v1.log GO-2026-10-30-15
run collisionneur-bisociation-lot-v1 lancer-tour-bisociation-lot-suite1-v1.sh journal-tour-bisociation-lot-suite1-v1.log GO-2026-10-30-16
run collisionneur-organisme-coevolutif-v1 lancer-tour-organisme-coevolutif-v1.sh journal-tour-organisme-coevolutif-v1.log GO-2026-10-30-13
echo "$(date -u +%FT%TZ) chaîne finie" >> $J
