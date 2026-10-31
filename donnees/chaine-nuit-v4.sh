#!/bin/bash
# chaine-nuit-v4.sh — session-depot, 31 octobre 2026 (R-864) : tours du collisionneur sur les questions 6 puis 7 de conv-audit,
# l'un après l'autre, détachés de la session. Chaque lanceur vérifie ses empreintes et arrête son relais par PID (R10).
set -u
B=/home/user/controle-ia-travail/donnees; J=$B/chaine-nuit-v1.log
for n in 6 7; do cd $B/collisionneur-question-$n-v1 || continue
  echo "$(date -u +%FT%TZ) début (chaîne v4) question $n (PID $$)" >> $J
  if sha256sum -c --quiet lancer-tour-question-$n-v1.sh.sha256; then GO_ID=GO-2026-10-30-17 bash lancer-tour-question-$n-v1.sh > journal-tour-question-$n-v1.log 2>&1; c=$?; else c=99; fi
  echo "$(date -u +%FT%TZ) fin (chaîne v4) question $n code $c" >> $J; done
