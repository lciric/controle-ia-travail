#!/bin/bash
# Compagnons .sha256 des pièces du lanceur v4, de la liste de référence, des scripts d'essai, et liste des empreintes des
# sorties (essais/empreintes-resultats-l4.txt, avec compagnon). Rien n'est écrasé.
set -eu
E=$(cd "$(dirname "$0")" && pwd)
L=$(cd "$E/.." && pwd)
compagnon() {
  if [ -e "$1/$2.sha256" ]; then echo "refus : $1/$2.sha256 existe" >&2; exit 1; fi
  (cd "$1" && sha256sum "$2" > "$2.sha256")
}
(cd "$E/resultats" && sha256sum final-*.txt) > "$E/empreintes-resultats-l4.txt"
for f in lancer-essai-3-v4.sh demarrer-essai-3-v4.sh fabriquer-liste-reference-v4.sh rapport-auteur-lanceur-v4-essai-3-v1.md; do
  compagnon "$L" "$f"
done
compagnon "$L/reference" EMPREINTES-DE-REFERENCE-d7f949ac.txt
for f in "$E"/*.sh "$E"/*.py "$E"/liste-alteree-d-un-octet.txt "$E"/empreintes-resultats-l4.txt; do
  compagnon "$E" "$(basename "$f")"
done
echo "compagnons écrits"
