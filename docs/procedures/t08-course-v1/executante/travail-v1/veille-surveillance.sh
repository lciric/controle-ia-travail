#!/bin/bash
# Émet les lignes de surveillance.txt autres que POURSUIVRE, et la fin du processus de surveillance (PID donné).
F=/home/user/t08-course-v1-travail/lanceur-3/surveillance.txt; P=$1
n=$(wc -l < "$F")
while true; do
  m=$(wc -l < "$F")
  if [ "$m" -gt "$n" ]; then sed -n "$((n+1)),${m}p" "$F" | grep -v ' POURSUIVRE$' | cut -c1-400; n=$m; fi
  kill -0 "$P" 2>/dev/null || { echo "PROCESSUS DE SURVEILLANCE $P TERMINÉ"; tail -3 /home/user/t08-course-v1-travail/lanceur-3/surveillance-sortie.log | cut -c1-300; exit 0; }
  sleep 20
done
