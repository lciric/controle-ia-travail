#!/bin/bash
# Attend un nouveau commit sur la branche de la course (lecture toutes les 5 minutes), borne 60 minutes.
cd /home/user/controle-ia-travail
REF=$1
for i in $(seq 1 12); do
  sleep 300
  git fetch -q origin "+refs/heads/calcul/neuron-lens-reajustement-v1:refs/remotes/origin/calcul/neuron-lens-reajustement-v1" 2>/dev/null
  H=$(git rev-parse origin/calcul/neuron-lens-reajustement-v1)
  if [ "$H" != "$REF" ]; then echo "nouveau commit $H $(date -u +%TZ)"; git log -3 --format='%h %cI %s' $H; exit 0; fi
  echo "inchange $(date -u +%TZ)"
done
echo "borne atteinte sans nouveau commit"
