#!/bin/bash
# Course de remplacement atomique sur la copie privee de l'amorce. Usage : course-amorce-ca.sh VERSION N RACINE(neuve)
set -u
VER=$1 N=$2 RB=$3
O=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-script-demarrage-v6/outils
PYR=/home/user/controle-ia-travail/.venv/bin/python
mkdir -m 700 $RB || exit 2
printf '#!/bin/bash\necho STUB-BON\n' > $RB/bon.sh
printf '#!/bin/bash\necho STUB-FAUX\n' > $RB/faux.sh
/bin/bash $O/construire-donnees-amorce.sh $VER bon $RB/bon.sh $RB/donnees > /dev/null || exit 2
bon=0 faux=0 r18=0 autre=0
for i in $(seq 1 $N); do
  CH=$RB/ch; S=$RB/stop
  rm -f $S $S.ready
  $PYR -I $O/racer.py $CH $RB/bon.sh $RB/faux.sh $S 2> $RB/racer.err &
  RP=$!
  for k in $(seq 1 200000); do [ -e $S.ready ] && break; done
  ESSAI_DEMARRAGE_CHARGE=$CH /bin/bash $RB/donnees > $RB/sortie 2>&1
  rc=$?
  : > $S
  wait $RP
  if grep -q STUB-FAUX $RB/sortie; then faux=$((faux+1)); cp $RB/sortie $RB/divergence-$i.txt
  elif grep -q STUB-BON $RB/sortie && [ $rc = 0 ]; then bon=$((bon+1))
  elif [ $rc = 18 ]; then r18=$((r18+1))
  else autre=$((autre+1)); cp $RB/sortie $RB/autre-$i.txt; fi
  rm -rf $CH $CH.script.*
done
echo "$VER : N=$N  executes-le-bon=$bon  executes-le-faux(DIVERGENCE)=$faux  refus18=$r18  autre=$autre"
