#!/bin/bash
# Contre-lecteur : copie des données de démarrage saines dont la ligne 2 (H0_PREVU) est remplacée par la valeur donnée.
# Droits 600 (le fichier porte le jeton factice).
# Emploi : fabriquer-donnees-h0.sh H0_PREVU DONNEES_SAINES SORTIE
set -eu -o pipefail
H0=$1; SRC=$2; OUT=$3
[ ! -e "$OUT" ] || { echo "refus : $OUT existe" >&2; exit 1; }
[ "$(sed -n 2p "$SRC" | cut -c1-9)" = "H0_PREVU=" ] || { echo "refus : la ligne 2 n'est pas H0_PREVU" >&2; exit 2; }
umask 077
sed "2s/.*/H0_PREVU=$H0/" "$SRC" > "$OUT"
echo "$OUT : ligne 2 = $(sed -n 2p "$OUT") ; $(wc -c < "$OUT") octets"
