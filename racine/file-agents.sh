#!/usr/bin/env bash
until grep -q '^fin escalier' /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/collisionneur-escalier-v1/journal-lancement.txt; do sleep 15; done
d=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/collisionneur-agents-outilles-v1; echo "début agents-outilles $(date -u +%FT%TZ)" > $d/journal-lancement.txt
$d/lancer-tour-v1.sh >> $d/journal-lancement.txt 2>&1; echo "fin agents-outilles code $? $(date -u +%FT%TZ)" >> $d/journal-lancement.txt
