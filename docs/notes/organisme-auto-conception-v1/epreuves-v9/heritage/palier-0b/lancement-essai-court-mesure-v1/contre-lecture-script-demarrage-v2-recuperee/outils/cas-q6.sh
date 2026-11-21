#!/bin/bash
# CL, questions 4 et 6 : programme long, sortie de 2,5 Mo, heure d'arret de duree ramenee a +SECONDES (banc seulement : le
# gardien prend la derniere des options --heure-arret-duree). MODE : normal (vrai setsid) | enfant (code 5, programme vivant).
# Emploi : cas-q6.sh CL NOM MODE DONNEES SECONDES [DUREE_PROGRAMME_S]
set -u
CL=$1; NOM=$2; MODE=$3; UD=$4; SEC=$5; DUREE=${6:-150}
H=$(date -u -d "+$SEC seconds" +%Y-%m-%dT%H:%M:%SZ)
echo "heure d'arret ramenee a $H (banc)"
exec bash "$CL/mes-outils/jouer-cl.sh" "$CL" "$NOM" "$UD" "PATH_EN_TETE=$CL/mes-outils/faux-bin" "FAUX_SETSID=$MODE" \
  "FAUX_DUREE_S=$DUREE" FAUX_SORTIE_OCTETS=2500000 \
  "ESSAI_DEMARRAGE_OPT_GARDIEN=--intervalle-s 1 --delai-force-s 5 --heure-arret-duree $H"
