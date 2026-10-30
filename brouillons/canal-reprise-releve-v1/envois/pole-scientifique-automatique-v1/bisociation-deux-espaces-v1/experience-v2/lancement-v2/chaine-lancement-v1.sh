#!/bin/bash
# Chaîne de lancement de l'expérience v2 (bisociation à deux espaces), conv-audit, processeur seul.
# Ordre : reproduction des témoins (code final) → validation V1 à V9 → invocation unique.
# S'arrête si la reproduction échoue, si la validation échoue (code 2) ou si V9 est vraie (audit exigé avant l'invocation).
# Aucun résultat n'est affiché à conv-audit : tout va dans les journaux de ce dossier ; lecture par un sous-agent neuf (R13).
set -u
cd "$(dirname "$0")/.."
export PYTHONPATH=/home/claude/controle-ia-travail/src
J=lancement-v2
date -u +"%Y-%m-%dT%H:%M:%SZ debut" > $J/journal-chaine-v1.txt
python3 -B reproduction_temoins_v2.py reproduction-temoins-v2-resultats-v3.json --processus 2 > $J/reproduction-v3.log 2>&1
R=$?; echo "reproduction code $R $(date -u +%H:%M:%S)" >> $J/journal-chaine-v1.txt
[ $R -ne 0 ] && { echo "ARRET reproduction" >> $J/journal-chaine-v1.txt; exit 1; }
python3 -B validation_v2.py $J/validation-v2-resultats-v1.json --lancer-la-validation --lecture-v4 copie_ponts > $J/validation-v1.log 2>&1
R=$?; echo "validation code $R $(date -u +%H:%M:%S)" >> $J/journal-chaine-v1.txt
[ $R -ne 0 ] && { echo "ARRET validation (code $R)" >> $J/journal-chaine-v1.txt; exit 2; }
if grep -q "V9 J vraie : True" $J/validation-v1.log; then echo "ARRET V9 vraie : audit exigé avant invocation" >> $J/journal-chaine-v1.txt; exit 3; fi
ID=$(date -u +%Y%m%d-%H%M%S)-bisociation-v2
echo "invocation run-id $ID" >> $J/journal-chaine-v1.txt
python3 -B invocation_unique_v2.py --run-id $ID --processus 2 --validation $J/validation-v2-resultats-v1.json --reproduction reproduction-temoins-v2-resultats-v3.json > $J/invocation-v1.log 2>&1
R=$?; echo "invocation code $R $(date -u +%H:%M:%S)" >> $J/journal-chaine-v1.txt
date -u +"%Y-%m-%dT%H:%M:%SZ fin" >> $J/journal-chaine-v1.txt
exit $R
