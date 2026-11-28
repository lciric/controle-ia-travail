#!/bin/bash
# usage: verifier.sh LISTE  (lignes « fichier_pdf|page|phrase ») ; extrait la page par pdftotext -layout,
# normalise les espaces, cherche la phrase (insensible à la casse) ; écrit OK ou ABSENT par ligne.
set -uo pipefail
liste="$1"
while IFS='|' read -r pdf page phrase; do
  [ -z "$pdf" ] && continue
  txt=$(pdftotext -f "$page" -l "$page" -layout "$pdf" - 2>/dev/null | tr -s '[:space:]' ' ')
  if printf '%s' "$txt" | grep -q -i -F -- "$phrase"; then r=OK; else r=ABSENT; fi
  printf '%s | %s | p. %s | %s\n' "$r" "$(basename "$pdf")" "$page" "$phrase"
done < "$liste"
