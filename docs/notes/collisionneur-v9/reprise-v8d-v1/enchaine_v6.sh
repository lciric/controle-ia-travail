#!/bin/bash
# Session des collisionneurs (nouveau compte) : reprise de la file de l'ancien conteneur (redémarré à 08:05Z), v8d,
# étage III, cinq espèces (sans Neon), plafond et ligne 45 USD par dossier, sous les GO d'origine ; seconde voie, un
# dossier à la fois. Le dossier de la problématique est repris depuis ses cellules écrites (même script, même dossier).
# Règle de la mère : une coupure de flux, une reprise ; une seconde, arrêt du dossier ; tout autre code non nul arrête tout.
cd /home/user/controle-ia-travail
S=docs/notes/collisionneur-v9/collisionneur_v9_v8d.py
export PYTHONPATH=src
R=docs/notes/collisionneur-v9/reprise-v8d-v1/enchaine-v6.log
N=docs/notes/collisionneur-v9
C=$N/protocole-x-cinq-questions-v1
Q=docs/notes/demandes-fable-api-2026-11-22-v1
H=$(date -u +%Y%m%d-%H%M%S)
coupure() { tail -3 $1/journal-etage3.txt | grep -q "ARRÊT (code 5).*flux coupé"; }
dossier() { # $1 dossier, $2 question, $3 GO
  local D=$1 QU=$2 GO=$3 i=0
  mkdir -p $D
  while :; do
    echo "=== course $(date -u +%FT%TZ) ===" >> $D/journal-etage3.txt
    GO_ID=$GO .venv/bin/python -B $S etage3 --fable --opus --argon --astra --carbon \
      --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --cle-openai OPENAI_API_KEY_2 --sortie $D --faits $QU --question $QU \
      --plafond-usd 45 --ligne-usd 45 >> $D/journal-etage3.txt 2>&1
    local c=$?; echo "code_fin=$c" >> $D/journal-etage3.txt; echo "$(date -u +%FT%TZ) $D code=$c" >> $R
    [ $c -eq 0 ] && break
    if [ $c -eq 5 ] && coupure $D && [ $i -lt 1 ]; then i=$((i+1)); echo "$D coupure, reprise" >> $R; continue; fi
    if [ $c -eq 5 ] && coupure $D; then echo "$D arrêt du dossier (seconde coupure)" >> $R; return 0; fi
    echo "$D arrêt code $c : tout s'arrête" >> $R; exit 21
  done
  .venv/bin/python -B $S verifier $D > /dev/null 2>&1 && echo "$D verifier après : tient" >> $R || echo "$D verifier après : ÉCHEC" >> $R
}
echo "$(date -u +%FT%TZ) début (processus $$)" >> $R
dossier runs/collisionneur-protocole-x-problematique-papier-v1-20261122-061053 $N/protocole-x-problematique-papier-v1/question-neutre-problematique-papier-v1.md GO-2026-11-22-11
dossier runs/collisionneur-protocole-x-revendications-v1-$H $N/protocole-x-revendications-v1/question-neutre-revendications-v2.md GO-2026-11-22-13
dossier runs/collisionneur-protocole-x-generale-isole-v1-$H $C/question-neutre-generale-v2.md GO-2026-11-22-17
dossier runs/collisionneur-protocole-x-papier-a-isole-v1-$H $C/question-neutre-papier-a-v2.md GO-2026-11-22-17
dossier runs/collisionneur-protocole-x-papier-b-isole-v1-$H $C/question-neutre-papier-b-v2.md GO-2026-11-22-17
dossier runs/collisionneur-protocole-x-papier-c-isole-v1-$H $C/question-neutre-papier-c-v2.md GO-2026-11-22-17
dossier runs/collisionneur-protocole-x-these-boite-blanche-isole-v1-$H $C/question-neutre-these-boite-blanche-v2.md GO-2026-11-22-18
dossier runs/collisionneur-protocole-x-etau-isole-v1-$H $C/question-neutre-etau-v2.md GO-2026-11-22-22
dossier runs/collisionneur-protocole-x-taches-sabotage-isole-v1-$H $C/question-neutre-taches-sabotage-v2.md GO-2026-11-22-22
echo "fin $(date -u +%FT%TZ)" >> $R
