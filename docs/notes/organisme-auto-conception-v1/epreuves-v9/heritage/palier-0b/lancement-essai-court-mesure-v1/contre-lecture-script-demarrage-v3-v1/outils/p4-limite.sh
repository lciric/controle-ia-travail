#!/bin/bash
# point 4 (limite) : script gonflé d'un commentaire aléatoire ; cherche la frontière 32768/32769 en lecture stricte.
# Lit STRICT dans la sortie (succès : "taille en lecture stricte ... : N octets" ; refus : "données de N octets").
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v3
F=$W/pieces/fabriquer-donnees-demarrage-v3.sh
O=$W/tmp/lim; rm -rf $O; mkdir -p $O/s
git init -q --bare $O/distant.git
cp $W/pieces/amorce-demarrage-essai-3-v3.sh $O/
cp $F $O/fab.sh
# le fabricant lit l'amorce et le script à côté de lui ; le script gonflé est fourni par FABRICANT_SCRIPT
export JFACT=$(head -c 300 /dev/urandom | base64 -w0 | tr -dc 'A-Za-z0-9' | head -c 100)
head -c 60000 /dev/urandom | base64 -w0 > $O/alea.txt
essai() {  # $1 : nombre de signes de remplissage
  rm -f $O/s/*
  { cat $W/pieces/demarrage-machine-essai-3-v3.sh; printf '# '; head -c $1 $O/alea.txt; echo; } > $O/gros.sh
  FABRICANT_BANC=oui FABRICANT_SCRIPT=$O/gros.sh FABRICANT_DEPOT_DISTANT=$O/distant.git bash $O/fab.sh JFACT $O/s/ud > $O/sortie.txt 2>&1
  CODE=$?
  S=$(sed -n 's/^taille en lecture stricte.*: \([0-9]*\) octets ; limite.*/\1/p; s/^refus (6) : données de \([0-9]*\) octets.*/\1/p' $O/sortie.txt)
  echo "pad=$1 code=$CODE strict=$S" >> $W/tables/p4-limite.txt
}
: > $W/tables/p4-limite.txt
lo=0; hi=6000
while [ $((hi - lo)) -gt 1 ]; do
  mid=$(( (lo + hi) / 2 ))
  essai $mid
  if [ "$CODE" = 0 ]; then lo=$mid; else hi=$mid; fi
done
echo "--- frontiere : dernier pad accepté $lo, premier refusé $hi" >> $W/tables/p4-limite.txt
essai $lo; ls $O/s >> $W/tables/p4-limite.txt
essai $hi; echo "après refus, fichiers restants :" >> $W/tables/p4-limite.txt; ls $O/s >> $W/tables/p4-limite.txt; cat $O/sortie.txt >> $W/tables/p4-limite.txt
