#!/bin/bash
# Prépare une racine factice SANS .git, comme la copie de l'arbre envoyée au serveur : le programme (copie à l'octet du vrai
# fichier, lu dans le dépôt de travail, empreinte 1f04cb46…), le dossier du code v6 (dossier courant de la commande), deux
# fichiers de remplissage ; puis COMMIT-DE-LA-COPIE.txt (le commit donné) et EMPREINTES-DE-LA-COPIE.txt, fabriqué par la
# commande écrite dans l'en-tête du lanceur v3. Rien n'est lancé.
# Usage : preparer-copie-factice-v4.sh DOSSIER_NEUF PROGRAMME_REEL COMMIT
set -eu
D=$1
P=$2
C=$3
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
H=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b
mkdir -p "$D/$H/programme-3-5-6-v2" "$D/$H/code-v6/src" "$D/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator"
cp "$P" "$D/$H/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py"
echo "fichier de remplissage" > "$D/suivi.txt"
echo "module factice" > "$D/$H/code-v6/src/factice.txt"
echo "$C" > "$D/COMMIT-DE-LA-COPIE.txt"
cd "$D"
find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | sort -z | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt
echo "copie factice : $D ; commit écrit $(cat COMMIT-DE-LA-COPIE.txt) ; $(wc -l < EMPREINTES-DE-LA-COPIE.txt) empreintes"
