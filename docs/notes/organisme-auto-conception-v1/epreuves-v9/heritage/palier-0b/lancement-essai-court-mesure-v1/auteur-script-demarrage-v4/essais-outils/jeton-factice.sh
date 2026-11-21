#!/bin/bash
# Fabrique un jeton FACTICE (aléatoire, préfixe « factice_ »), écrit en droits 600 dans le fichier neuf donné.
# Emploi : jeton-factice.sh FICHIER
set -eu -o pipefail
[ ! -e "$1" ] || { echo "refus : $1 existe" >&2; exit 1; }
umask 077
A=$(head -c 64 /dev/urandom | base64 -w 0 | tr -dc 'A-Za-z0-9' | cut -c1-36)
printf 'factice_%s\n' "$A" > "$1"
echo "jeton factice écrit dans $1 ($(wc -c < "$1") octets)"
