#!/bin/bash
# Prépare une racine factice (dépôt git neuf) portant le programme factice, suivi et commité.
# Usage : preparer-racine-factice-v1.sh DOSSIER_NEUF PROGRAMME_FACTICE
set -eu
D=$1
P=$2
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$D/prog"
cp "$P" "$D/prog/programme-factice-v1.py"
echo "fichier suivi" > "$D/suivi.txt"
git init -q "$D"
git -C "$D" add prog/programme-factice-v1.py suivi.txt
env GIT_AUTHOR_NAME=factice GIT_AUTHOR_EMAIL=factice@example.invalid GIT_COMMITTER_NAME=factice \
  GIT_COMMITTER_EMAIL=factice@example.invalid git -C "$D" commit -q --no-gpg-sign -m "racine factice"
echo "tête : $(git -C "$D" rev-parse HEAD)"
sha256sum "$D/prog/programme-factice-v1.py"
