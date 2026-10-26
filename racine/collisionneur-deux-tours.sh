#!/usr/bin/env bash
set -uo pipefail
for t in publication format; do
  d=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/collisionneur-$t-v1
  echo "début $t $(date -u +%FT%TZ)" >> $d/journal-lancement.txt
  $d/lancer-tour-v1.sh >> $d/journal-lancement.txt 2>&1; echo "fin $t code $? $(date -u +%FT%TZ)" >> $d/journal-lancement.txt
done
