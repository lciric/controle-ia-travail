#!/bin/bash
# point 1 (fenetre contrôle/lecture) : un processus de MEME uid remplace par rename atomique le script de la charge, en boucle,
# pendant que l'amorce tourne. Compte les executions ou le script LU (STUB-SHA) n'est pas celui dont l'empreinte a ete controlee.
# Montre l'existence de la fenetre ; elle exige l'ecriture dans un dossier 700 de root (cloud-init : root seul).
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v3
O=$W/tmp/p1
T=$W/tables/p1-course.txt; : > $T
E1=$(sed -n 4p $O/s/ud1 | cut -d= -f2)
N=${1:-300}
ok=0; alt=0; r18=0; autre=0
for i in $(seq 1 $N); do
  rm -rf $O/run/course; F=$O/run/course/demarrage-machine-essai-3-v3.sh
  ( until [ -e $F ]; do :; done
    while :; do cp $O/st1/stub.sh $O/rA; mv -f $O/rA $F; cp $O/st2/stub.sh $O/rB; mv -f $O/rB $F; done ) &
  RP=$!
  out=$(ESSAI_DEMARRAGE_CHARGE=$O/run/course bash $O/s/ud1 2>&1); c=$?
  kill $RP; wait $RP 2>/dev/null
  s=$(echo "$out" | sed -n 's/^STUB-SHA //p')
  if [ "$c" = 7 ] && [ "$s" = "$E1" ]; then ok=$((ok+1))
  elif [ "$c" = 7 ]; then alt=$((alt+1))
  elif [ "$c" = 18 ]; then r18=$((r18+1))
  else autre=$((autre+1)); fi
done
echo "essais $N ; lu = controle : $ok ; LU AUTRE QUE CONTROLE (code 7, empreinte differente) : $alt ; refus 18 : $r18 ; autres codes : $autre" >> $T
cat $T
