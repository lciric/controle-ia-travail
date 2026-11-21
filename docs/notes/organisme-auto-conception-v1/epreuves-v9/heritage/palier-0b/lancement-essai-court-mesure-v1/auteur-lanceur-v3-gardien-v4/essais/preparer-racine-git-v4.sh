#!/bin/bash
# Prépare une racine factice AVEC .git (dépôt neuf, jetable, sous le dossier des essais) : un programme factice au chemin
# relatif du vrai programme, et un fichier suivi ; un seul commit. Écrit la tête et l'empreinte du programme factice.
# Usage : preparer-racine-git-v4.sh DOSSIER_NEUF PROGRAMME_FACTICE
set -eu
D=$1
P=$2
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
H=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b
mkdir -p "$D/$H/programme-3-5-6-v2" "$D/$H/code-v6"
cp "$P" "$D/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py"
echo "fichier suivi" > "$D/suivi.txt"
git init -q "$D"
git -C "$D" add "$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py" suivi.txt
env GIT_AUTHOR_NAME=factice GIT_AUTHOR_EMAIL=factice@example.invalid GIT_COMMITTER_NAME=factice \
  GIT_COMMITTER_EMAIL=factice@example.invalid git -C "$D" commit -q --no-gpg-sign -m "racine factice"
echo "tête : $(git -C "$D" rev-parse HEAD)"
sha256sum "$D/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py"
