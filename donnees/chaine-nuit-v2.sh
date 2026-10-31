#!/bin/bash
# chaine-nuit-v2.sh — session-depot, 30 octobre 2026 (R-860). Attend la fin de la chaîne v1 (PID donné en argument, vérifié
# par sa ligne de commande), puis lance la suite 2 du tour P-041 (GO-15). Attente seulement ; aucun arrêt ici (R10).
set -u
B=/home/user/controle-ia-travail/donnees; J=$B/chaine-nuit-v1.log; P=$1
tr '\0' ' ' < /proc/$P/cmdline 2>/dev/null | grep -q chaine-nuit-v1.sh || { echo "$(date -u +%FT%TZ) v2 : PID $P n'est pas la chaîne v1" >> $J; exit 3; }
while kill -0 $P 2>/dev/null; do sleep 30; done
cd $B/collisionneur-idee-p041-bonne-v1 || exit 3
echo "$(date -u +%FT%TZ) début (chaîne v2) lancer-tour-idee-p041-bonne-suite2-v1.sh (PID $$)" >> $J
if sha256sum -c --quiet lancer-tour-idee-p041-bonne-suite2-v1.sh.sha256; then GO_ID=GO-2026-10-30-15 bash lancer-tour-idee-p041-bonne-suite2-v1.sh > journal-tour-idee-p041-bonne-suite2-v1.log 2>&1; c=$?; else c=99; fi
echo "$(date -u +%FT%TZ) fin (chaîne v2) suite 2 P-041 code $c" >> $J
