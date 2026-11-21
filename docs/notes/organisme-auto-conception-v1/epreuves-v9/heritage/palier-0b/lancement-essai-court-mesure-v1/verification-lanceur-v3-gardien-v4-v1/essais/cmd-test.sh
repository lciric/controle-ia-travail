#!/bin/bash
# Essai dynamique de la commande : le lanceur donné est lancé en emploi sur une copie saine avec l'interprète factice ; ce que
# l'interprète reçoit est comparé à ce que le complément (pièce d'origine) donne une fois les trois chemins remplacés.
# Usage : cmd-test.sh LANCEUR RACINE SORTIES NOM_TENUE
set -u
V=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2
LANCEUR=$1
R=$2
S=$3
T=$V/v4/t/$4
I=$V/v4/pieces/interp-factice.sh
mkdir -p "$T"
cc=$(grep '^env -C ' $V/complement-origin-v2.md)
set -- $cc
W=("$@")
R0=${W[8]}
sub() {
  case "$1" in
    "$R0"|"$R0"/*) printf '%s' "$R${1#$R0}" ;;
    *) printf '%s' "$1" ;;
  esac
}
{
  echo "cwd=$(sub "${W[2]}")"
  echo "PYTHONPATH=src"
  echo "arg=-B"
  echo "arg=$(sub "${W[6]}")"
  echo "arg=$(sub "${W[7]}")"
  echo "arg=$(sub "${W[8]}")"
  echo "arg=$(sub "${W[9]}")"
  echo "arg=$S"
} > "$T/attendu.txt"
env ENREG="$T/enreg.txt" bash "$LANCEUR" "$T" "$R" "$I" "$S" 2> "$T/stderr.txt"
echo "code du lanceur : $? ; code-de-sortie.txt : $(cat $T/code-de-sortie.txt 2>/dev/null)"
if diff "$T/attendu.txt" "$T/enreg.txt" > "$T/diff.txt" 2>&1; then
  echo "ÉGAL : cwd, PYTHONPATH et arguments reçus = attendus (complément, trois chemins remplacés)"
else
  echo "DIFFÉRENT :"
  cat "$T/diff.txt"
fi
