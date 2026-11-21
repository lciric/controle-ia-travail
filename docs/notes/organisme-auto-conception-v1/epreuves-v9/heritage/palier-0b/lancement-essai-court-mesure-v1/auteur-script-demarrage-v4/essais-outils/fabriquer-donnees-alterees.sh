#!/bin/bash
# v3 : fabrique des données de démarrage ARTEFACTS à partir de données saines v3 (amorce + charge tar.gz de cinq
# fichiers : script de démarrage v3 et quatre pièces) :
#   piece-alteree   : dernier octet du gardien remplacé ;
#   piece-en-trop   : un sixième fichier dans la charge ;
#   script-altere   : un octet ajouté au script de démarrage de la charge (l'amorce doit refuser, code 18) ;
#   h0-faux | h0-moins-3h | h0-moins-1h | h0-plus-1h : ligne 2 changée ;
#   jeton-vide      : ligne 3 remplacée par « JETON_DEMARRAGE='' ».
# Sortie en droits 600 (elle porte le jeton factice, sauf jeton-vide).
# Emploi : fabriquer-donnees-alterees.sh MODE DONNEES_SAINES SORTIE
set -eu -o pipefail
MODE=$1; SRC=$2; OUT=$3
[ ! -e "$OUT" ] || { echo "refus : $OUT existe" >&2; exit 1; }
umask 077
TMP=$OUT.travail
mkdir "$TMP"
N=$(grep -n -x '__CHARGE_DES_PIECES__' "$SRC" | cut -d: -f1)
case "$MODE" in
  h0-faux) sed '2s/.*/H0_PREVU=hier/' "$SRC" > "$OUT" ;;
  h0-moins-3h|h0-moins-1h|h0-plus-1h)
    case "$MODE" in h0-moins-3h) DT=-10800 ;; h0-moins-1h) DT=-3600 ;; h0-plus-1h) DT=3600 ;; esac
    sed "2s/.*/H0_PREVU=$(date -u -d "@$(( $(date +%s) + DT ))" +%Y-%m-%dT%H:%M:%SZ)/" "$SRC" > "$OUT" ;;
  jeton-vide) sed "3s/.*/JETON_DEMARRAGE=''/" "$SRC" > "$OUT" ;;
  e-script-absent) sed '4d' "$SRC" > "$OUT" ;;            # v4 (R4) : ligne E_SCRIPT retirée
  e-script-vide) sed '4s/.*/E_SCRIPT=/' "$SRC" > "$OUT" ;;  # v4 (R4) : E_SCRIPT vide
  piece-*|script-altere|sans-script-e-vide)
    [ "$MODE" = sans-script-e-vide ] && { sed '4s/.*/E_SCRIPT=/' "$SRC" > "$TMP/src"; SRC=$TMP/src; }
    mkdir "$TMP/x"
    sed -n "$((N + 1)),\$p" "$SRC" | base64 -d | tar -xz -C "$TMP/x"
    case "$MODE" in
      piece-alteree) G=$TMP/x/gardien-essai-3-v4.py; T=$(stat -c %s "$G"); head -c $((T - 1)) "$G" > "$TMP/g"; printf '#' >> "$TMP/g"; mv "$TMP/g" "$G" ;;
      piece-en-trop) echo "en trop" > "$TMP/x/en-trop.sh" ;;
      script-altere) echo "# octet de trop" >> "$TMP/x/demarrage-machine-essai-3-v4.sh" ;;
      sans-script-e-vide) rm "$TMP/x/demarrage-machine-essai-3-v4.sh" ;;  # v4 : charge sans le script, E_SCRIPT vide
    esac
    head -n "$N" "$SRC" > "$OUT"
    tar --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner --format=gnu -c -C "$TMP/x" . | gzip -9 -n | base64 -w 0 >> "$OUT"
    echo >> "$OUT"
    ;;
  *) echo "mode inconnu : $MODE" >&2; exit 2 ;;
esac
rm -rf "$TMP"
echo "$MODE : $OUT ($(wc -c < "$OUT") octets)"
