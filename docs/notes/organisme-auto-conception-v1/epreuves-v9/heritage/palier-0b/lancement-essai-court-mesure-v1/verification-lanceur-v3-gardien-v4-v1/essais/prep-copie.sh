#!/bin/bash
# Fabrique une copie factice sans .git de la racine : le vrai fichier du programme (pour son empreinte seulement), quelques
# fichiers factices, COMMIT-DE-LA-COPIE.txt et EMPREINTES-DE-LA-COPIE.txt par la recette de l'en-tête du lanceur v3.
# Usage : prep-copie.sh DOSSIER_RACINE
set -u
R=$1
PROG=docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py
SRC=/home/user/controle-ia-travail/$PROG
mkdir -p "$R/$(dirname $PROG)" "$R/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src" "$R/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator"
cp "$SRC" "$R/$PROG"
echo "factice A" > "$R/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src/a.py"
echo "factice B" > "$R/docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/b.py"
echo "factice P" > "$R/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md"
echo d7f949acd9ac92e998e57663d2cc741de93f18c3 > "$R/COMMIT-DE-LA-COPIE.txt"
(cd "$R" && find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 | sort -z | xargs -0 sha256sum > EMPREINTES-DE-LA-COPIE.txt)
echo "copie prête : $R ($(wc -l < "$R/EMPREINTES-DE-LA-COPIE.txt") empreintes)"
