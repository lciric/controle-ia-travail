#!/bin/bash
# Fabrique des donnees de demarrage D'ESSAI : une amorce (v6 ou v4) + une charge dont le "script de demarrage" est un STUB inoffensif.
# Usage : construire-donnees-amorce.sh VERSION(v6|v4) VARIANTE(bon|absent|vide|faux) STUB SORTIE
# STUB : fichier qui devient le script de la charge ; E_SCRIPT = son empreinte (bon), vide, absent, ou une fausse.
set -u
VER=$1 VAR=$2 STUB=$3 OUT=$4
A=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1
case $VER in
  v6) AM=$A/auteur-script-demarrage-v6/amorce-demarrage-essai-3-v6.sh NOM=demarrage-machine-essai-3-v6.sh ;;
  v4) AM=$A/auteur-script-demarrage-v4/amorce-demarrage-essai-3-v4.sh NOM=demarrage-machine-essai-3-v4.sh ;;
  *) exit 2 ;;
esac
[ ! -e $OUT ] || exit 2
ST=$(mktemp -d $OUT.stage.XXXXXX) || exit 2
cp $STUB $ST/$NOM
H=$(sha256sum < $STUB | cut -c1-64)
tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner -c -C $ST $NOM | gzip -9 -n | base64 -w 0 > $ST/payload
{
  sed -n 1p $AM
  case $VAR in
    bon) echo "E_SCRIPT=$H" ;;
    vide) echo "E_SCRIPT=" ;;
    faux) echo "E_SCRIPT=0000000000000000000000000000000000000000000000000000000000000000" ;;
    absent) : ;;
  esac
  sed -n '3,$p' $AM
  echo __CHARGE_DES_PIECES__
  cat $ST/payload; echo
} > $OUT
rm -rf $ST
echo "donnees $VER/$VAR : $OUT (E_SCRIPT bon = $H)"
