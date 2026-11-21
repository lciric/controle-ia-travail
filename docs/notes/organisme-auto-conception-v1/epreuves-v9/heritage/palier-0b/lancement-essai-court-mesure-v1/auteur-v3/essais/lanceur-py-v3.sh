#!/bin/bash
# Lanceur factice générique v3 : même squelette que le vrai lanceur (piège TERM, interpréteur en enfant, code de sortie dans
# le dossier de tenue) ; lance l'interpréteur du dépôt sur le programme factice donné.
# Usage (par demarrer-essai-court-v2.sh) : lanceur-py-v3.sh TENUE PROGRAMME [ARGUMENTS...]
TENUE=$1
shift
trap 'echo "TERM recu par le lanceur" >&2' TERM
/home/user/controle-ia-travail/.venv/bin/python -B "$@"
CODE=$?
echo "$CODE" > "$TENUE/code-de-sortie.txt"
exit "$CODE"
