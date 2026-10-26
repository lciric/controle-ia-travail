#!/usr/bin/env bash
set -uo pipefail
until grep -q '^fin code' /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/collisionneur-publication-methodo-v1/journal-lancement.txt; do sleep 10; done
for t in emprunts financement; do
  d=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/collisionneur-$t-v1
  echo "début $t $(date -u +%FT%TZ)" >> $d/journal-lancement.txt
  $d/lancer-tour-v1.sh >> $d/journal-lancement.txt 2>&1; echo "fin $t code $? $(date -u +%FT%TZ)" >> $d/journal-lancement.txt
done
