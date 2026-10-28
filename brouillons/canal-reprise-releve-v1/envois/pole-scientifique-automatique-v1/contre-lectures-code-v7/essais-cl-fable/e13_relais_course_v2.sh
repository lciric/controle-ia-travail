#!/bin/sh
# E13, v2 (la v1 comptait mal : `jobs -p` est vide dans un shell non interactif ; elle reste, non employée) :
# l'essai « plafond atteint » du relais réel rejoué N fois, par lots de P en parallèle ; PID gardés par `$!`.
# Usage : sh e13_relais_course_v2.sh COPIE N P [FILTRE]
COPIE="$1"; N="$2"; P="$3"; FILTRE="${4:-test_artefact_plafond_atteint}"
cd "$COPIE" || exit 2
i=0; echecs=0
while [ $i -lt $N ]; do
  pids=""; j=0
  while [ $j -lt $P ]; do
    /opt/venv-essaim-sim-v1/bin/python -I -B -m unittest discover -s essais -t . -p 'test_v6_relais_reel.py' -k "$FILTRE" > /dev/null 2>&1 &
    pids="$pids $!"; j=$((j+1))
  done
  for pid in $pids; do wait $pid || echecs=$((echecs+1)); done
  i=$((i+P))
done
echo "essais: $N ; echecs: $echecs ; filtre: $FILTRE"
