#!/bin/bash
# point 4 : frontière exacte 32768 / 32769, par ajout de n espaces à la fin de l'amorce (copie, hors banc de l'auteur)
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v3
O=$W/tmp/lim
export JFACT=$(head -c 300 /dev/urandom | base64 -w0 | tr -dc 'A-Za-z0-9' | head -c 100)
: > $W/tables/p4-limite-fine.txt
{ cat $W/pieces/demarrage-machine-essai-3-v3.sh; printf '# '; head -c 1777 $O/alea.txt; echo; } > $O/gros.sh
for n in 0 1 2 3; do
  rm -f $O/s/*
  { cat $W/pieces/amorce-demarrage-essai-3-v3.sh; printf '%*s' $n ''; } > $O/amorce-demarrage-essai-3-v3.sh
  FABRICANT_BANC=oui FABRICANT_SCRIPT=$O/gros.sh FABRICANT_DEPOT_DISTANT=$O/distant.git bash $O/fab.sh JFACT $O/s/ud > $O/sortie.txt 2>&1
  CODE=$?
  S=$(sed -n 's/^taille en lecture stricte.*: \([0-9]*\) octets ; limite.*/\1/p; s/^refus (6) : données de \([0-9]*\) octets.*/\1/p' $O/sortie.txt)
  echo "n=$n code=$CODE strict=$S fichiers=$(ls $O/s | wc -l)" >> $W/tables/p4-limite-fine.txt
done
