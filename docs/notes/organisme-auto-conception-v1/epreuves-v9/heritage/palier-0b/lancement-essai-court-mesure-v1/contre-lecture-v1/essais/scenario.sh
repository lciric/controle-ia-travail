#!/bin/bash
# Scénario du contre-lecteur : scenario.sh NOM PAS_S OCTETS DUREE_S ENFANT SEUIL_N SEUIL_LIBRE_OCTETS DUREE_ETAPE4_S
D=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-gardien-palier-0b
A=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-v1
NOM=$1; PAS=$2; OCT=$3; DUREE=$4; ENF=$5; SN=$6; SL=$7; D4=${8:-2700}
T=$D/e/$NOM/tenue
S=$D/e/$NOM/sorties
mkdir -p "$T"
bash $A/demarrer-essai-court-v1.sh "$T" "$D/lanceur_factice.sh" "$S" "$PAS" "$OCT" "$DUREE" "$ENF" "$D/enfant_factice.py" "$D/e/$NOM/marqueur.txt"
bash $A/demarrer-gardien-essai-court-v1.sh "$T" --sorties "$S" --seuil-n "$SN" --seuil-libre-octets "$SL" --duree-etape-4-s "$D4" --intervalle-s 1 --delai-force-s 5
