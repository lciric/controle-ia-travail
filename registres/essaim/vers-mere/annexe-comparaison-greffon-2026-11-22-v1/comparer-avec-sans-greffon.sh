#!/bin/bash
# Rejoue les 33 fichiers en échec de la suite complète sur l'arbre neuf de main, avec puis sans la ligne d'import du greffon
# dans tests/conftest.py, sous .venv (même interpréteur que la suite complète), et écrit la liste des échecs de chaque passe.
set -u
A=/home/user/arbre-main-suite-greffon
S=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/suite-main-greffon
mapfile -t F < "$S/fichiers-en-echec.txt"
export TMPDIR="$S/tmp-comparaison"
mkdir -p "$TMPDIR"
cd "$A" || exit 3
cp -p tests/conftest.py "$S/conftest-avec-ligne.py"
PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -rfEX -p no:cacheprovider "${F[@]}" > "$S/passe-avec-greffon.txt" 2>&1
echo "code avec : $?" > "$S/codes-comparaison.txt"
git show HEAD:tests/conftest.py > tests/conftest.py
PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -rfEX -p no:cacheprovider "${F[@]}" > "$S/passe-sans-greffon.txt" 2>&1
echo "code sans : $?" >> "$S/codes-comparaison.txt"
cp -p "$S/conftest-avec-ligne.py" tests/conftest.py
grep -E '^(FAILED|ERROR|XPASS) ' "$S/passe-avec-greffon.txt" | sed 's/ - .*//' | sort > "$S/echecs-avec.txt"
grep -E '^(FAILED|ERROR|XPASS) ' "$S/passe-sans-greffon.txt" | sed 's/ - .*//' | sort > "$S/echecs-sans.txt"
diff "$S/echecs-avec.txt" "$S/echecs-sans.txt" > "$S/diff-echecs.txt"
echo "diff : $?" >> "$S/codes-comparaison.txt"
date -u +%FT%TZ > "$S/comparaison-finie"
