#!/bin/bash
# Joue le fabricant avec la variable JETON_FACTICE_ESSAI remplie depuis un fichier (lu par read, builtin : le jeton ne
# passe dans aucune ligne de commande) ; --vide : variable vide ; --absente : variable absente.
# Emploi : fabricant-avec-jeton.sh FICHIER_JETON|--vide|--absente FABRICANT SORTIE [EMPREINTE_ATTENDUE]
set -u
SRC=$1; FAB=$2; shift 2
case "$SRC" in
  --vide) export JETON_FACTICE_ESSAI= ;;
  --absente) unset JETON_FACTICE_ESSAI ;;
  *) IFS= read -r JETON_FACTICE_ESSAI < "$SRC"; export JETON_FACTICE_ESSAI ;;
esac
/bin/bash "$FAB" JETON_FACTICE_ESSAI "$@"
echo "code du fabricant : $?"
