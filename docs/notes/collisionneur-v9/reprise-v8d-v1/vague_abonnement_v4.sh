#!/bin/bash
# v4 (24 novembre 2026, corrections de la contre-lecture du v8q) : appelle la voie abonnement v8. Moteurs admis par la
# voie : v8m, v8p, v8r. L'option --cle-gemini NOM se passe avec les espèces, avec le seul moteur v8r ; avec v8m ou v8p, la
# voie arrête au code 1 avant tout lancement. Avec v8m, v8p ou l'essaim, la clé de Google reste lue sous son nom fixe
# (GEMINI_API_KEY). Un dossier commencé sous v8m se reprend sous v8r avec --reprise (changement de script consigné au
# journal). Le reste est la v2 (et la v3, qui appelait la voie v7).
# Une vague d'un dossier par la voie abonnement : les cellules d'OpenAI et de Google partent par l'interface, les cellules
# Claude écrivent leur kit ; la porte se ferme en fin de tour (code 2). Aucune clé d'Anthropic n'est employée : la variable
# passée en --cle-anthropic est factice (le moteur n'exige que sa présence).
# Arguments : MOTEUR (v8m|v8p|v8r) DOSSIER QUESTION GO EFFORT PLAFOND ESPECES... [--cle-gemini NOM] [--reprise]
cd /home/user/controle-ia-travail
export PYTHONPATH=src ABONNEMENT_CLE_FACTICE=factice-aucun-appel
M=$1 D=$2 Q=$3 GO=$4 E=$5 P=$6; shift 6
mkdir -p $D
echo "=== vague abonnement $(date -u +%FT%TZ) ===" >> $D/journal-etage3.txt
GO_ID=$GO .venv/bin/python -B docs/notes/collisionneur-v9/abonnement-v1/voie_abonnement_v8.py $M --effort $E -- etage3 "$@" \
  --cle-anthropic ABONNEMENT_CLE_FACTICE --cle-openai OPENAI_API_KEY_2 --sortie $D --faits $Q --question $Q \
  --plafond-usd $P --ligne-usd $P >> $D/journal-etage3.txt 2>&1
c=$?; echo "code_fin=$c" >> $D/journal-etage3.txt
echo "$(date -u +%FT%TZ) $D code=$c" >> docs/notes/collisionneur-v9/reprise-v8d-v1/vague-abonnement-v1.log
