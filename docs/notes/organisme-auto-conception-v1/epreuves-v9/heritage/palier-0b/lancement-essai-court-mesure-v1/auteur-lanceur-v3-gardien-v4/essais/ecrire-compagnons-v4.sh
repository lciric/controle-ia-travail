#!/bin/bash
# Écrit un compagnon .sha256 (« empreinte  nom ») à côté de chaque pièce du dossier, des scripts d'essai et des copies ;
# écrit essais/empreintes-resultats-v4.txt (empreintes des sorties des essais) et son compagnon. Rien n'est écrasé.
set -eu
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
compagnon() {  # dossier nom
  if [ -e "$1/$2.sha256" ]; then echo "refus : $1/$2.sha256 existe" >&2; exit 1; fi
  (cd "$1" && sha256sum "$2" > "$2.sha256")
}
(cd "$E/resultats" && sha256sum final-*.txt) > "$E/empreintes-resultats-v4.txt"
for f in lancer-essai-3-v3.sh demarrer-essai-3-v3.sh verifier-commande-v3.py gardien-essai-3-v4.py demarrer-gardien-essai-3-v4.sh \
         rapport-auteur-lanceur-v3-gardien-v4-essai-3-v1.md complement.md consigne.md; do
  compagnon "$B" "$f"
done
for f in "$E"/*.sh "$E"/*.py "$E"/empreintes-resultats-v4.txt; do
  compagnon "$E" "$(basename "$f")"
done
for d in "$E"/copies/*; do
  for f in "$d"/*; do
    case "$f" in *.sha256) continue ;; esac
    compagnon "$d" "$(basename "$f")"
  done
done
echo "compagnons écrits"
