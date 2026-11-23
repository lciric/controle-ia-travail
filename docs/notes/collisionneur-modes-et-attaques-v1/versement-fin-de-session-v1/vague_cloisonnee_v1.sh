#!/bin/bash
# Copie de vague_abonnement_v1.sh qui journalise hors de l'arbre du dépôt ; python3 du système (bibliothèque standard).
# Arguments : DOSSIER QUESTION GO EFFORT PLAFOND ESPECES...
cd /home/user/controle-ia-travail
export PYTHONPATH=src ABONNEMENT_CLE_FACTICE=factice-aucun-appel
D=$1 Q=$2 GO=$3 E=$4 P=$5; shift 5
J=$HOME/collisionneur-modes-tenus-a-l-ecart-v1/journaux; mkdir -p $J
N=$(basename $D)
echo "=== vague $(date -u +%FT%TZ) ===" >> $J/$N-etage3.txt
GO_ID=$GO python3 -B docs/notes/collisionneur-v9/abonnement-v1/voie_abonnement_v5.py v8m --branche coffre/modes-tenus-a-l-ecart-collisionneur-v1 --effort $E -- etage3 "$@" \
  --cle-anthropic ABONNEMENT_CLE_FACTICE --cle-openai OPENAI_API_KEY_2 --sortie $D --faits $Q --question $Q \
  --plafond-usd $P --ligne-usd $P >> $J/$N-etage3.txt 2>&1
c=$?; echo "code_fin=$c $(date -u +%FT%TZ)" >> $J/$N-etage3.txt; echo "$N code=$c"
