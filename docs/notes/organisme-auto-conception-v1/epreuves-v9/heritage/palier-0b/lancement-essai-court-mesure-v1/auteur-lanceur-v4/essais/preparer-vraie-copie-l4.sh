#!/bin/bash
# Fait de l'arbre extrait du commit (fabriquer-liste-reference-v4.sh) la copie telle qu'envoyée au serveur : ajoute
# COMMIT-DE-LA-COPIE.txt (le commit, une ligne) et EMPREINTES-DE-LA-COPIE.txt (copie à l'octet de la liste de référence).
# Refuse si l'un des deux existe déjà. Usage : preparer-vraie-copie-l4.sh ARBRE LISTE_DE_REFERENCE COMMIT
set -eu
A=$1; L=$2; C=$3
for f in "$A/COMMIT-DE-LA-COPIE.txt" "$A/EMPREINTES-DE-LA-COPIE.txt"; do
  if [ -e "$f" ] || [ -L "$f" ]; then echo "refus : $f existe" >&2; exit 1; fi
done
echo "$C" > "$A/COMMIT-DE-LA-COPIE.txt"
cp "$L" "$A/EMPREINTES-DE-LA-COPIE.txt"
cmp "$L" "$A/EMPREINTES-DE-LA-COPIE.txt"
echo "vraie copie prête : $A ; liste $(sha256sum "$A/EMPREINTES-DE-LA-COPIE.txt" | cut -d' ' -f1)"
