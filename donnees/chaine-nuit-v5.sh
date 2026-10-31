#!/bin/bash
# chaine-nuit-v5.sh — session-depot, 31 octobre 2026 (R-869) : attend la fin de la chaîne v4 (PID en argument, vérifié par sa
# ligne de commande), puis lance la suite 1 du tour sur la question 6. Attente seulement ; aucun arrêt ici (R10).
set -u
B=/home/user/controle-ia-travail/donnees; J=$B/chaine-nuit-v1.log; P=$1
tr '\0' ' ' < /proc/$P/cmdline 2>/dev/null | grep -q chaine-nuit-v4.sh || { echo "$(date -u +%FT%TZ) v5 : PID $P n'est pas la chaîne v4" >> $J; exit 3; }
while kill -0 $P 2>/dev/null; do sleep 30; done
cd $B/collisionneur-question-6-v1 || exit 3
echo "$(date -u +%FT%TZ) début (chaîne v5) suite 1 question 6 (PID $$)" >> $J
if sha256sum -c --quiet lancer-tour-question-6-suite1-v1.sh.sha256; then GO_ID=GO-2026-10-30-17 bash lancer-tour-question-6-suite1-v1.sh > journal-tour-question-6-suite1-v1.log 2>&1; c=$?; else c=99; fi
echo "$(date -u +%FT%TZ) fin (chaîne v5) suite 1 question 6 code $c" >> $J
