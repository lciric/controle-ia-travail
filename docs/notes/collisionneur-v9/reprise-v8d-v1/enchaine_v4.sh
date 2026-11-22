#!/bin/bash
# Enchaîne, après l enchaîneur v3, les questions étau et tâches de sabotage en mode isolé (GO-2026-11-22-22).
# Règle de la mère : une coupure de flux, une reprise ; une seconde, arrêt du dossier ; tout autre code non nul arrête tout.
cd /home/user/controle-ia-travail
S=docs/notes/collisionneur-v9/collisionneur_v9_v8d.py
export PYTHONPATH=src
R=docs/notes/collisionneur-v9/reprise-v8d-v1/enchaine-v4.log
N=docs/notes/collisionneur-v9
while kill -0 "$1" 2>/dev/null; do sleep 15; done
if grep -q -e "tout s'arrête" -e "rien ne part" docs/notes/collisionneur-v9/reprise-v8d-v1/enchaine-v3.log 2>/dev/null; then echo "$(date -u +%FT%TZ) enchaîneur v3 arrêté sur erreur : rien ne part" >> $R; exit 22; fi
echo "$(date -u +%FT%TZ) enchaîneur v3 fini (processus $1)" >> $R
H=$(date -u +%Y%m%d-%H%M%S)
coupure() { tail -3 $1/journal-etage3.txt | grep -q "ARRÊT (code 5).*flux coupé"; }
dossier() { # $1 dossier, $2 GO, $3 question
  local D=$1 GO=$2 Q=$3 i=0
  mkdir -p $D
  while :; do
    echo "=== course $(date -u +%FT%TZ) ===" >> $D/journal-etage3.txt
    GO_ID=$GO .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon --cle-anthropic RR_ANTHROPIC_API_KEY_LUC \
      --cle-openai OPENAI_API_KEY_2 --sortie $D --faits $Q --question $Q --plafond-usd 45 --ligne-usd 45 \
      >> $D/journal-etage3.txt 2>&1
    local c=$?; echo "code_fin=$c" >> $D/journal-etage3.txt; echo "$(date -u +%FT%TZ) $D code=$c" >> $R
    [ $c -eq 0 ] && break
    if [ $c -eq 5 ] && coupure $D && [ $i -lt 1 ]; then i=$((i+1)); echo "$D coupure, reprise" >> $R; continue; fi
    if [ $c -eq 5 ] && coupure $D; then echo "$D arrêt du dossier (seconde coupure)" >> $R; return 0; fi
    echo "$D arrêt code $c : tout s'arrête" >> $R; exit 21
  done
  .venv/bin/python -B $S verifier $D > /dev/null 2>&1 && echo "$D verifier après : tient" >> $R || echo "$D verifier après : ÉCHEC" >> $R
}
dossier runs/collisionneur-protocole-x-etau-isole-v1-$H GO-2026-11-22-22 docs/notes/collisionneur-v9/protocole-x-cinq-questions-v1/question-neutre-etau-v2.md
dossier runs/collisionneur-protocole-x-taches-sabotage-isole-v1-$H GO-2026-11-22-22 docs/notes/collisionneur-v9/protocole-x-cinq-questions-v1/question-neutre-taches-sabotage-v2.md
echo "fin $(date -u +%FT%TZ)" >> $R
