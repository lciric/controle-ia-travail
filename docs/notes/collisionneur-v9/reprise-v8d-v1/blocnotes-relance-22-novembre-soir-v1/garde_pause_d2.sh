#!/bin/bash
# Pause ordonnée par Lazar (via la mère, 16:57Z) : arrête le PID 1105 dès que l'essai de Carbon du dossier 2 est consigné, avant Neon.
J=/home/user/controle-ia-travail/runs/collisionneur-protocole-x-conscience-anesthesie-v3-reserve-abonnement-v1-20261122-153110/journal-etage3.txt
PID=1105
while kill -0 $PID 2>/dev/null; do
  if tail -1 $J | grep -q "^    statut\|ARRÊT"; then kill -TERM $PID; echo "$(date -u +%FT%T.%NZ) arrêt PID $PID après : $(tail -1 $J)"; break; fi
  sleep 0.1
done
echo "$(date -u +%FT%TZ) fin de garde ; dernière ligne : $(tail -1 $J)"
