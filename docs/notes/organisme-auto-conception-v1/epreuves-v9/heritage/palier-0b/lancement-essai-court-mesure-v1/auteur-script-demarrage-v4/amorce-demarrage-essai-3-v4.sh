#!/bin/bash
# @DONNEES-DE-DEMARRAGE@
# Amorce, essai 3, palier 0b, v4 : extrait la charge (script de demarrage v4 et quatre pieces, tar.gz en base64), copie
# le script UNE fois dans un fichier prive (dossier 700, fichier 600), hache cette copie contre E_SCRIPT (pose par le
# fabricant), puis lit cette meme copie. Codes : 18 charge, E_SCRIPT absent ou vide, copie ou empreinte ; 20 deja la.
set -u -o pipefail
umask 077
CHARGE=${ESSAI_DEMARRAGE_CHARGE:-/root/essai-3-charge}
[ -e $CHARGE ] && { echo "amorce : $CHARGE present"; exit 20; }
mkdir -m 700 -p $CHARGE && sed -n '/^__CHARGE_DES_PIECES__$/,$p' "${BASH_SOURCE[0]}" | sed 1d | base64 -d \
  | tar -xz --no-same-owner -C $CHARGE || { echo "amorce : charge illisible"; exit 18; }
[ -n "${E_SCRIPT:-}" ] || { echo "amorce : E_SCRIPT absent ou vide"; exit 18; }
PRIVE=$(mktemp -d $CHARGE.script.XXXXXX) && chmod 700 $PRIVE && cp $CHARGE/demarrage-machine-essai-3-v4.sh $PRIVE/s.sh \
  && chmod 600 $PRIVE/s.sh || { echo "amorce : copie privee du script impossible"; exit 18; }
[ "$(sha256sum < $PRIVE/s.sh | cut -c1-64)" = "$E_SCRIPT" ] || { echo "amorce : empreinte du script autre que $E_SCRIPT"; exit 18; }
umask 022
. $PRIVE/s.sh
exit
