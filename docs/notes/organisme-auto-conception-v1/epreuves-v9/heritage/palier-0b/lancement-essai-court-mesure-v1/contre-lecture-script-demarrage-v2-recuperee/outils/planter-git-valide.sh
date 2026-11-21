#!/bin/bash
# Plante un .git VALIDE : tete = commit attendu, index = arbre du commit (aucun fichier suivi modifie), dans la racine du
# cas : ESSAI_DEMARRAGE_BASE/racine ; le depot de clonage est ESSAI_DEMARRAGE_BASE/depot.git
C=d7f949acd9ac92e998e57663d2cc741de93f18c3
R=$ESSAI_DEMARRAGE_BASE/racine
D=$ESSAI_DEMARRAGE_BASE/depot.git
/usr/bin/git init -q "$R" || exit 1
/usr/bin/git -C "$R" fetch -q "$D" "$C" || { echo "fetch impossible"; exit 2; }
/usr/bin/git -C "$R" reset -q --mixed "$C" || { echo "reset impossible"; exit 3; }
echo "plante : .git valide dans $R, tete $(/usr/bin/git -C "$R" rev-parse HEAD)"
