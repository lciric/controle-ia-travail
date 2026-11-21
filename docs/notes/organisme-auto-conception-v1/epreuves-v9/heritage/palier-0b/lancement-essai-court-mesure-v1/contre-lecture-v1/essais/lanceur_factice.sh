#!/bin/bash
# Lanceur factice du contre-lecteur : même squelette que le vrai (piège TERM, code de sortie), commande factice.
TENUE=$1
shift
trap 'echo "TERM recu par le lanceur" >&2' TERM
/home/user/controle-ia-travail/.venv/bin/python -B /tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-gardien-palier-0b/prog_factice.py "$@"
CODE=$?
echo "$CODE" > "$TENUE/code-de-sortie.txt"
exit "$CODE"
