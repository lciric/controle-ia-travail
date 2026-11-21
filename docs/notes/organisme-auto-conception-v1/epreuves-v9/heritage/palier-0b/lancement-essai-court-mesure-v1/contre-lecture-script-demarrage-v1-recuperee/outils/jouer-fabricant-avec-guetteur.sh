#!/bin/bash
# Contre-lecteur : joue le fabricant (avec la variable de jeton factice posée par le wrapper de l'auteur, comme la session le
# ferait) pendant que MON guetteur d'environnement et de ligne de commande tourne ; rend la liste des processus qui ont
# porté le jeton dans leur environnement ou leur ligne de commande (nom du programme, canal, nombre de relevés).
# Emploi : jouer-fabricant-avec-guetteur.sh SORTIE_DU_FABRICANT [EMPREINTE_ATTENDUE_DU_SCRIPT]
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
AUT=$ME/auteur
SORTIE=$1; shift
JF=$AUT/travail/jeton-factice.txt
GE=$ME/resultats/guetteur-fabricant.txt
ARRET=$ME/resultats/guetteur-fabricant.arret
rm -f "$ARRET" "$GE"
bash "$ME/outils/guetteur-environ.sh" "$JF" "$GE" "$ARRET" &
PG=$!
sleep 0.3
bash "$AUT/essais-outils/fabricant-avec-jeton.sh" "$JF" "$AUT/fabriquer-donnees-demarrage-v1.sh" "$SORTIE" "$@" > "$ME/resultats/sortie-fabricant-guetteur.txt" 2>&1
: > "$ARRET"
wait "$PG"
echo "sortie du fabricant (dernières lignes) :"; tail -n 2 "$ME/resultats/sortie-fabricant-guetteur.txt" | cut -c1-120
echo "lignes de la sortie du fabricant portant le jeton : $(grep -c -F -f "$JF" "$ME/resultats/sortie-fabricant-guetteur.txt")"
echo "$(tail -n 1 "$GE")"
echo "processus qui ont porté le jeton (canal, programme) :"
grep -v '^balayages' "$GE" | awk '{print $5, $7, $8}' | sort | uniq -c
