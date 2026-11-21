#!/bin/bash
# Variante : enfant du même groupe qui ignore le signal de fin (enfant_sourd.py), programme qui meurt au signal de fin.
D=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-gardien-palier-0b
A=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-v1
NOM=h4
T=$D/e/$NOM/tenue
S=$D/e/$NOM/sorties
mkdir -p "$T"
bash $A/demarrer-essai-court-v1.sh "$T" "$D/lanceur_factice.sh" "$S" 0.5 1000 60 2 "$D/enfant_sourd.py" "$D/e/$NOM/marqueur.txt"
bash $A/demarrer-gardien-essai-court-v1.sh "$T" --sorties "$S" --seuil-n 5 --seuil-libre-octets 1 --intervalle-s 1 --delai-force-s 5
