#!/usr/bin/env bash
# Parité entière : trois tranches en parallèle, dossiers jetables effacés monde par monde.
set -u
S=/tmp/claude-0/-home-user-controle-ia-travail/b09e1b49-1473-5167-b0d5-946b1adabcb0/scratchpad/parite
R=/home/user/controle-ia-travail/.claude/worktrees/agent-a89be1d2701a117b9
PY=/home/user/controle-ia-travail/.venv/bin/python
cd "$R" || exit 1
git rev-parse HEAD > "$S/commit.txt"
mkdir -p "$S/tmp"
rm -f "$S"/resultats-*.jsonl
for k in 0 1 2; do
    PYTHONDONTWRITEBYTECODE=1 B5F_PARITE_TOUS=1 "$PY" -I "$S/tranche.py" "$k" 3 "$S/resultats-$k.jsonl" "$S/tmp" \
        > "$S/tranche-$k.log" 2>&1 &
done
wait
cat "$S"/resultats-*.jsonl | "$PY" -c 'import sys, json, collections
l = [json.loads(x) for x in sys.stdin]
c = collections.Counter(x["etat"] for x in l)
print("mondes", len(l), dict(c))
for x in l:
    if x["etat"] != "passe": print(x["monde"], x["motif"][:300])' > "$S/bilan.txt"
cat "$S/bilan.txt"
