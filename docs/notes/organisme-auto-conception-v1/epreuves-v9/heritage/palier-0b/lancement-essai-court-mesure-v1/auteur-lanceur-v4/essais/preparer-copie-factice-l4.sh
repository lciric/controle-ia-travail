#!/bin/bash
# Copie factice SANS .git pour le lanceur v4 : le vrai programme (copie à l'octet, ou altéré d'une ligne si ALTERER=1), le
# dossier du code v6, deux fichiers de remplissage ; COMMIT-DE-LA-COPIE.txt ; EMPREINTES-DE-LA-COPIE.txt par la recette du
# lanceur v4 (LC_ALL=C). Écrit sur sa sortie standard la seule empreinte de la liste : c'est la « référence » de cette copie
# factice, à passer au lanceur en 8e argument du mode --verifier-seulement.
# Usage : preparer-copie-factice-l4.sh DOSSIER_NEUF PROGRAMME_REEL COMMIT [ALTERER]
set -eu
set -o pipefail
D=$1
P=$2
C=$3
ALT=${4:-0}
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
H=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b
mkdir -p "$D/$H/programme-3-5-6-v2" "$D/$H/code-v6/src" "$D/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator"
cp "$P" "$D/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py"
if [ "$ALT" = 1 ]; then echo "# ligne ajoutée (artefact)" >> "$D/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py"; fi
echo "fichier de remplissage" > "$D/suivi.txt"
echo "module factice" > "$D/$H/code-v6/src/factice.txt"
echo "$C" > "$D/COMMIT-DE-LA-COPIE.txt"
cd "$D"
LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | LC_ALL=C sort -z | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt
sha256sum EMPREINTES-DE-LA-COPIE.txt | cut -d' ' -f1
