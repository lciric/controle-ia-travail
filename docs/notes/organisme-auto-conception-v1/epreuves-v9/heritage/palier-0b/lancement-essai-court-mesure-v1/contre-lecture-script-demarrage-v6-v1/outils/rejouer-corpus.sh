#!/bin/bash
# Pour chaque script du corpus : reducteur reel, puis epreuve du fabricant (bash -n + diff, copie des lignes 118-121),
# puis comparaison des sorties de l'original et du reduit. Usage : rejouer-corpus.sh DOSSIER_CORPUS DOSSIER_SORTIE
set -u
PYR=/home/user/controle-ia-travail/.venv/bin/python
RED=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v6/reduire-script-v6.py
C=$1 O=$2
mkdir -p $O
printf '%-50s %-8s %-8s %s\n' cas reducteur epreuve sorties
for f in $C/*.sh; do
  b=$(basename $f .sh)
  rm -f $O/$b.reduit
  $PYR -I $RED $f $O/$b.reduit > $O/$b.red.txt 2>&1
  rc=$?
  if [ $rc != 0 ]; then printf '%-50s %-8s %-8s %s\n' $b "refus($rc)" - -; continue; fi
  DIFF=$(LC_ALL=C diff $f $O/$b.reduit)
  AUTRE=$(printf '%s\n' "$DIFF" | LC_ALL=C grep -v -E -e '^[0-9]+(,[0-9]+)?d[0-9]+$' -e '^<( [[:space:]]*(#.*)?)?$' | grep -c .)
  ep=ok; [ "$AUTRE" = 0 ] || ep=refus
  bash -n $f 2>/dev/null && bash -n $O/$b.reduit 2>/dev/null || ep=refus-bashn
  a=$(bash $f 2>&1 < /dev/null | sha256sum | cut -c1-12)
  r=$(bash $O/$b.reduit 2>&1 < /dev/null | sha256sum | cut -c1-12)
  s=IDENTIQUES; [ "$a" = "$r" ] || s="DIFFERENTES($a/$r)"
  printf '%-50s %-8s %-8s %s\n' $b accepte $ep $s
done
