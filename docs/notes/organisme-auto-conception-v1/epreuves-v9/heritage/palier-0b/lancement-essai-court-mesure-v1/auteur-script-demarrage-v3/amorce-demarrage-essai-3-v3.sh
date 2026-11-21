#!/bin/bash
# @DONNEES-DE-DEMARRAGE@
# Amorce, essai 3, palier 0b, v3 : extrait la charge (script de demarrage v3 et quatre pieces, tar.gz en base64),
# controle l'empreinte du script (E_SCRIPT, posee par le fabricant), puis le lit. Codes : 18 charge ou script, 20 deja la.
set -u -o pipefail
CHARGE=${ESSAI_DEMARRAGE_CHARGE:-/root/essai-3-charge}
[ -e $CHARGE ] && { echo "amorce : $CHARGE present"; exit 20; }
mkdir -m 700 -p $CHARGE && sed -n '/^__CHARGE_DES_PIECES__$/,$p' "${BASH_SOURCE[0]}" | sed 1d | base64 -d \
  | tar -xz --no-same-owner -C $CHARGE || { echo "amorce : charge illisible"; exit 18; }
[ "$(sha256sum < $CHARGE/demarrage-machine-essai-3-v3.sh | cut -c1-64)" = "$E_SCRIPT" ] \
  || { echo "amorce : empreinte du script autre que $E_SCRIPT"; exit 18; }
. $CHARGE/demarrage-machine-essai-3-v3.sh
exit
