#!/bin/bash
# usage: lance.sh RACINE args pytest...   (rejoue pytest depuis RACINE, affiche code de sortie)
D=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecture-greffon-v2-b
R="$1"; shift
cd "$R" || exit 99
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$R/src" TMPDIR="$D/tables" /home/user/controle-ia-travail/.venv/bin/python -m pytest -p no:cacheprovider --rootdir="$R" "$@"
echo "CODE=$?"
