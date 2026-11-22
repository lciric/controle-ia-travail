#!/bin/bash
# @DONNEES-DE-DEMARRAGE@
# Amorce, essai 3, palier 0b, v5 : controle E_SCRIPT AVANT toute extraction ; extrait la charge (script de demarrage v5
# et quatre pieces, tar.gz en base64) ; copie le script dans un fichier prive (dossier 700, fichier 600) ; LIT cette
# copie UNE fois en memoire, hache ces octets contre E_SCRIPT, et execute ces memes octets (aucun fichier rouvert apres
# le hachage). Codes : 18 E_SCRIPT absent ou vide, charge, copie, lecture ou empreinte ; 20 deja la.
set -u -o pipefail
umask 077
[ -n "${E_SCRIPT:-}" ] || { echo "amorce : E_SCRIPT absent ou vide : rien n'est extrait"; exit 18; }
CHARGE=${ESSAI_DEMARRAGE_CHARGE:-/root/essai-3-charge}
[ -e $CHARGE ] && { echo "amorce : $CHARGE present"; exit 20; }
mkdir -m 700 -p $CHARGE && sed -n '/^__CHARGE_DES_PIECES__$/,$p' "${BASH_SOURCE[0]}" | sed 1d | base64 -d \
  | tar -xz --no-same-owner -C $CHARGE || { echo "amorce : charge illisible"; exit 18; }
PRIVE=$(mktemp -d $CHARGE.script.XXXXXX) && chmod 700 $PRIVE && cp $CHARGE/demarrage-machine-essai-3-v5.sh $PRIVE/s.sh \
  && chmod 600 $PRIVE/s.sh || { echo "amorce : copie privee du script impossible"; exit 18; }
TEXTE=
IFS= read -r -d '' TEXTE < $PRIVE/s.sh
[ -n "$TEXTE" ] || { echo "amorce : copie privee illisible"; exit 18; }
[ "$(printf '%s' "$TEXTE" | sha256sum | cut -c1-64)" = "$E_SCRIPT" ] || { echo "amorce : empreinte du script autre que $E_SCRIPT"; exit 18; }
umask 022
eval "$TEXTE"
exit
