#!/usr/bin/env bash
# Parité entière (B5F_PARITE_TOUS=1) en trois tranches, sur le commit 423496d4 ; essais seulement, aucun réseau.
set -u
S=/tmp/claude-0/-home-user-controle-ia-travail/b09e1b49-1473-5167-b0d5-946b1adabcb0/scratchpad/parite
R=/home/user/controle-ia-travail/.claude/worktrees/agent-a89be1d2701a117b9
PY=/home/user/controle-ia-travail/.venv/bin/python
cd "$R" || exit 1
export PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 B5F_PARITE_TOUS=1
git rev-parse HEAD > "$S/commit.txt"
"$PY" -m pytest --collect-only -q -p no:cacheprovider tests/test_ouverture_suffixes_v1.py -k parite \
    | grep '::test_parite' > "$S/noeuds.txt"
wc -l < "$S/noeuds.txt" > "$S/compte-noeuds.txt"
split -n l/3 -d "$S/noeuds.txt" "$S/tranche-"
for t in "$S"/tranche-0?; do
    n=$(basename "$t")
    "$PY" -m pytest --tb=line -q -rN -p no:cacheprovider --basetemp="$S/bt-$n" $(cat "$t") > "$S/$n.log" 2>&1 &
done
wait
for t in "$S"/tranche-0?.log; do echo "$(basename "$t") : $(tail -n 1 "$t")"; done > "$S/bilan.txt"
cat "$S/bilan.txt"
