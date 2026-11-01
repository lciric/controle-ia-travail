#!/usr/bin/env bash
# Essai R5 de l'étape 5 du lanceur v3 (garde de calcul) : cas sain (GO inscrit) et artefact (GO absent du registre).
set -uo pipefail
DEPOT=/home/user/controle-ia-travail; T=$(mktemp -d)
ETAPE=$(sed -n '/^# 5. garde de calcul avec le GO/,/^# 6\./p' "$1" | sed '$d')
for GO in GO-2026-11-01-11 "GO-2026-11-01-$((90+9))"; do
  ( set -euo pipefail; eval "$ETAPE"; echo "suite atteinte" ) >"$T/sortie" 2>&1 && c=0 || c=$?
  echo "GO=$GO → code $c ; $(tr '\n' ' ' < "$T/sortie" | cut -c1-160)"
done
