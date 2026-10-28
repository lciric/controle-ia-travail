#!/bin/sh
# E13 : l'essai « plafond atteint » du relais réel (essais/test_v6_relais_reel.py) rejoué N fois, par lots de P en
# parallèle (charge processeur) ; compte les échecs. Usage : sh e13_relais_course_v1.sh COPIE N P
COPIE="$1"; N="$2"; P="$3"
cd "$COPIE" || exit 2
i=0; echecs=0
while [ $i -lt $N ]; do
  j=0
  while [ $j -lt $P ]; do
    /opt/venv-essaim-sim-v1/bin/python -I -B -m unittest discover -s essais -t . -p 'test_v6_relais_reel.py' -k test_artefact_plafond_atteint > /dev/null 2>&1 &
    j=$((j+1))
  done
  for pid in $(jobs -p); do wait $pid || echecs=$((echecs+1)); done
  i=$((i+P))
done
echo "essais: $N ; echecs: $echecs"
