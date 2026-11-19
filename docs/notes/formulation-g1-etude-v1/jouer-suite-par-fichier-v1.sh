#!/bin/bash
# Suite d'essais du dépôt jouée fichier par fichier, dossier temporaire borné et supprimé après chaque fichier.
cd /home/user/controle-ia-travail || exit 2
JOURNAL=/home/user/suite-par-lots-v1/journal.txt
: > "$JOURNAL"
echo "commit $(git rev-parse HEAD) debut $(date -u +%FT%TZ)" >> "$JOURNAL"
for f in tests/test_*.py; do
  T=/home/user/suite-par-lots-v1/tmp
  rm -rf "$T"; mkdir -p "$T"
  out=$(PYTHONPATH=src timeout 1800 .venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp="$T/b" "$f" 2>&1 | tail -1)
  echo "$f :: $out" >> "$JOURNAL"
  rm -rf "$T"
done
echo "fin $(date -u +%FT%TZ)" >> "$JOURNAL"
