#!/bin/bash
# chaine-nuit-v6.sh — session-depot, 31 octobre 2026 (R-870) : dernière reprise de la nuit des questions 7 puis 6 (Kimi coupé).
set -u
B=/home/user/controle-ia-travail/donnees; J=$B/chaine-nuit-v1.log
for x in "7 suite1" "6 suite2"; do set -- $x; cd $B/collisionneur-question-$1-v1 || continue
  echo "$(date -u +%FT%TZ) début (chaîne v6) question $1 $2 (PID $$)" >> $J
  if sha256sum -c --quiet lancer-tour-question-$1-$2-v1.sh.sha256; then GO_ID=GO-2026-10-30-17 bash lancer-tour-question-$1-$2-v1.sh > journal-tour-question-$1-$2-v1.log 2>&1; c=$?; else c=99; fi
  echo "$(date -u +%FT%TZ) fin (chaîne v6) question $1 $2 code $c" >> $J; done
