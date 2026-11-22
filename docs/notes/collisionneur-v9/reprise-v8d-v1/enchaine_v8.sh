#!/bin/bash
# Session des collisionneurs (nouveau compte) : six dossiers du protocole X en mode isolé avec Neon (GO-2026-11-22-33),
# v8d, étage III, plafond et ligne 50 USD par dossier, un dossier à la fois ici. Enchaîneur v8 : deux dossiers neufs
# (GO-2026-11-22-37), après la fin de l'enchaîneur v7 (processus donné en argument) ; décision de la mère (08:34Z) : un refus de la garde de motifs (code 7)
# arrête son seul dossier, jamais les autres.
# Règle de la mère : une coupure de flux, une reprise ; une seconde, arrêt du dossier ; tout autre code non nul arrête tout.
cd /home/user/controle-ia-travail
S=docs/notes/collisionneur-v9/collisionneur_v9_v8d.py
export PYTHONPATH=src
R=docs/notes/collisionneur-v9/reprise-v8d-v1/enchaine-v8.log
Q=docs/notes/demandes-fable-api-2026-11-22-v1
while kill -0 "$1" 2>/dev/null; do sleep 15; done
H=$(date -u +%Y%m%d-%H%M%S)
coupure() { tail -3 $1/journal-etage3.txt | grep -q "ARRÊT (code 5).*flux coupé"; }
dossier() { # $1 dossier, $2 question, $3 réserve (vide ou texte)
  local D=$1 QU=$2 i=0
  mkdir -p $D
  if [ -n "$3" ] && [ ! -f $D/en-tete-reserve-v1.md ]; then
    printf '%s\n' "$3" > $D/en-tete-reserve-v1.md; sha256sum $D/en-tete-reserve-v1.md | sed "s#$D/##" > $D/en-tete-reserve-v1.md.sha256
  fi
  while :; do
    echo "=== course $(date -u +%FT%TZ) ===" >> $D/journal-etage3.txt
    GO_ID=GO-2026-11-22-37 .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon --neon \
      --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie $D --faits $QU --question $QU \
      --plafond-usd 50 --ligne-usd 50 >> $D/journal-etage3.txt 2>&1
    local c=$?; echo "code_fin=$c" >> $D/journal-etage3.txt; echo "$(date -u +%FT%TZ) $D code=$c" >> $R
    [ $c -eq 0 ] && break
    if [ $c -eq 5 ] && coupure $D && [ $i -lt 1 ]; then i=$((i+1)); echo "$D coupure, reprise" >> $R; continue; fi
    if [ $c -eq 5 ] && coupure $D; then echo "$D arrêt du dossier (seconde coupure)" >> $R; return 0; fi
    if [ $c -eq 7 ]; then echo "$D arrêt du dossier (garde de motifs, code 7) ; les autres continuent" >> $R; return 0; fi
    echo "$D arrêt code $c : tout s'arrête" >> $R; exit 21
  done
  .venv/bin/python -B $S verifier $D > /dev/null 2>&1 && echo "$D verifier après : tient" >> $R || echo "$D verifier après : ÉCHEC" >> $R
}
RES="Réserve (GO-2026-11-22-37) : question orientée faiblement au test de devinette (0,55) ; servie telle quelle, comme les deux précédentes."
echo "$(date -u +%FT%TZ) début (processus $$, après l'enchaîneur v7 $1)" >> $R
dossier runs/collisionneur-protocole-x-lot-quarantaine-v1-$H $Q/question-neutre-lot-quarantaine-servie-v1.md "$RES"
dossier runs/collisionneur-protocole-x-modes-attaque-v1-$H $Q/question-neutre-modes-attaque-servie-v1.md ""
echo "fin $(date -u +%FT%TZ)" >> $R
