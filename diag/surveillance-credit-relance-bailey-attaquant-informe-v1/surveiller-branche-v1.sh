#!/bin/bash
# Lecture seule : sort (code 30) au premier commit hors « journaux » apres le commit de depart $1, ou 0 apres 110 min.
DEPOT=/home/user/controle-ia-travail; BR=claude/compassionate-meitner-d4ryyk; DEP=$1; T0=$(date +%s)
J="$(dirname "$0")/journal-credit.txt"
while :; do
  cd $DEPOT && git fetch -q origin $BR:refs/remotes/origin/$BR 2>/dev/null
  N=$(git log --format='%h %ci %s' $DEP..origin/$BR | grep -v "poste Hetzner : journaux")
  echo "$(date -u +%FT%TZ) branche nouveaux=[$(echo "$N" | grep -c .)]" >> "$J"
  [ -n "$N" ] && { echo "SORTIE commit"; echo "$N"; exit 30; }
  [ $(( $(date +%s) - T0 )) -gt 6600 ] && { echo "SORTIE delai"; exit 0; }
  sleep 120
done
