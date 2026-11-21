#!/bin/bash
# Lanceur factice du vérificateur : même squelette que le vrai (piège TERM, interpréteur en enfant, code de sortie).
TENUE=$1
shift
trap 'echo "TERM recu par le lanceur" >&2' TERM
/home/user/controle-ia-travail/.venv/bin/python -B /tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-gardien-v2/v/prog-v.py "$@"
CODE=$?
echo "$CODE" > "$TENUE/code-de-sortie.txt"
exit "$CODE"
