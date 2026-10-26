#!/usr/bin/env bash
until grep -q '^fin etage3' /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/collisionneur-lecture-pilote-v1/journal-etage3.txt 2>/dev/null; do sleep 15; done
for n in test-M escalier agents-outilles; do
  d=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/collisionneur-$n-v1; echo "début etage3 $(date -u +%FT%TZ)" > $d/journal-etage3.txt
  $d/suite-etage3-v1.sh >> $d/journal-etage3.txt 2>&1; echo "fin etage3 code $? $(date -u +%FT%TZ)" >> $d/journal-etage3.txt
done
