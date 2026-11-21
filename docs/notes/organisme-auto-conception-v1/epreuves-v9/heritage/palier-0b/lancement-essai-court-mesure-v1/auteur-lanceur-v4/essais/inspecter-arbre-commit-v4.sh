#!/bin/bash
# Lecture seule du dépôt de travail : nombre d'entrées de l'arbre du commit, par mode (fichier, exécutable, lien, sous-module),
# taille totale des fichiers, et présence d'attributs d'exportation (.gitattributes : export-ignore, export-subst).
# Usage : inspecter-arbre-commit-v4.sh DEPOT COMMIT
set -eu
DEP=$1
C=$2
echo "commit $(git -C "$DEP" rev-parse --verify "$C^{commit}")"
git -C "$DEP" ls-tree -r -l "$C" | awk '{n[$1]++; if ($4 != "-") t += $4} END {for (m in n) print "mode " m " : " n[m] " entrées"; print "taille totale : " t " octets"}'
echo "fichiers .gitattributes : $(git -C "$DEP" ls-tree -r --name-only "$C" | grep -c '\.gitattributes$' || true)"
for f in $(git -C "$DEP" ls-tree -r --name-only "$C" | grep '\.gitattributes$' || true); do
  echo "--- $f :"
  git -C "$DEP" show "$C:$f" | grep -n -E 'export-(ignore|subst)' || echo "(aucun attribut d'exportation)"
done
