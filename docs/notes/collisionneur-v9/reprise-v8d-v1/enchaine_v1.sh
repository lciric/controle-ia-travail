#!/bin/bash
# Enchaîne : maths (une reprise), antériorité, fusionnée ; règle de la mère (23:08Z).
cd /home/user/controle-ia-travail
S=docs/notes/collisionneur-v9/collisionneur_v9_v8d.py
export PYTHONPATH=src
R=/tmp/claude-0/-home-user-controle-ia-travail/880667cb-41bd-5ef3-a231-ed6614227479/scratchpad/enchaine.log
lance() { # $1 dossier, $2 GO, reste : arguments
  local D=$1 GO=$2; shift 2
  echo "=== course $(date -u +%FT%TZ) ===" >> $D/journal-reprise-v8.txt
  GO_ID=$GO .venv/bin/python -B $S etage3 "$@" --sortie $D --reprise 2>&1 | tee -a $D/journal-reprise-v8.txt > /dev/null
  local c=${PIPESTATUS[0]}; echo "code_fin=$c" >> $D/journal-reprise-v8.txt
  echo "$(date -u +%FT%TZ) $D code=$c" >> $R; return $c
}
coupure() { tail -3 $1/journal-reprise-v8.txt | grep -q "ARRÊT (code 5).*flux coupé"; }
dossier() { # $1 dossier, $2 reprises permises, reste : GO et args
  local D=$1 n=$2; shift 2
  .venv/bin/python -B $S verifier $D > /dev/null 2>&1 || { echo "$D verifier avant en échec" >> $R; exit 20; }
  local i=0
  while :; do
    lance $D "$@"; local c=$?
    [ $c -eq 0 ] && break
    if [ $c -eq 5 ] && coupure $D; then
      i=$((i+1)); [ $i -gt $n ] && { echo "$D arrêt du dossier (coupure, reprises épuisées)" >> $R; break; }
      echo "$D coupure $i, reprise" >> $R
    else echo "$D arrêt code $c (autre que coupure) : tout s'arrête" >> $R; exit 21; fi
  done
  .venv/bin/python -B $S verifier $D > /dev/null 2>&1 && echo "$D verifier après : tient" >> $R || echo "$D verifier après : ÉCHEC" >> $R
}
K="--cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2"
dossier runs/collisionneur-methodes-maths-v1-20261121-093850 0 GO-2026-11-21-23 --fable --opus --argon --astra --carbon $K --plafond-usd 36.3 --ligne-usd 28 --ligne-reprise-usd 30 --go-ligne GO-2026-11-21-69
dossier runs/collisionneur-anteriorite-pilier-v1-20261121-131029 1 GO-2026-11-21-39 --fable --opus --argon --astra --carbon $K --plafond-usd 26.4 --ligne-usd 28
dossier runs/collisionneur-question-de-recherche-fusionnee-v1-20261121-153256 1 GO-2026-11-21-52 --fable --opus --argon --carbon $K --plafond-usd 28 --ligne-usd 28 --rejuger-essai E3-T2-critique-croisee-D:1
echo "fin $(date -u +%FT%TZ)" >> $R
