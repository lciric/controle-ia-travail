#!/bin/bash
# Fabrique la liste de référence des empreintes de la copie, depuis le commit lui-même (dépôt lu seulement) : extraction de
# l'arbre du commit par git archive dans DOSSIER_NEUF/arbre, puis empreinte de chaque fichier régulier par la recette du
# lanceur v4 (LC_ALL=C, chemins « ./… », triés, les deux fichiers de la copie exclus). Écrit
# DOSSIER_NEUF/EMPREINTES-DE-REFERENCE-<commit abrégé>.txt et rend son empreinte et son nombre de lignes.
# L'arbre extrait est la copie à envoyer au serveur : y ajouter COMMIT-DE-LA-COPIE.txt (le commit, une ligne) et
# EMPREINTES-DE-LA-COPIE.txt (copie à l'octet de la liste de référence).
# Usage : fabriquer-liste-reference-v4.sh DEPOT COMMIT DOSSIER_NEUF
set -eu
set -o pipefail
DEP=$1
C=$2
D=$3
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
COMPLET=$(git -C "$DEP" rev-parse --verify "$C^{commit}")
mkdir -p "$D/arbre"
git -C "$DEP" archive --format=tar "$COMPLET" | tar -x -C "$D/arbre"
L="$D/EMPREINTES-DE-REFERENCE-${COMPLET:0:8}.txt"
(cd "$D/arbre" && LC_ALL=C find . -type f ! -path ./COMMIT-DE-LA-COPIE.txt ! -path ./EMPREINTES-DE-LA-COPIE.txt -print0 \
  | LC_ALL=C sort -z | xargs -0 sha256sum) > "$L"
echo "commit $COMPLET"
echo "liens ou fichiers spéciaux dans l'arbre extrait : $(cd "$D/arbre" && find . ! -type f ! -type d | wc -l)"
echo "liste : $L ; $(wc -l < "$L") lignes ; sha256 $(sha256sum "$L" | cut -d' ' -f1)"
