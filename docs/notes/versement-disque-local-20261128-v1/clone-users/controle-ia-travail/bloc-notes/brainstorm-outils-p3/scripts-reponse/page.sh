#!/bin/bash
# usage: page.sh FICHIER_PDF PAGE DOSSIER_SORTIE  -> extrait une page (rang physique) par pdftotext -layout
set -euo pipefail
pdf="$1"; p="$2"; out="$3"
base=$(basename "$pdf" .pdf)
pdftotext -f "$p" -l "$p" -layout "$pdf" "$out/${base}-p${p}.txt"
echo "$out/${base}-p${p}.txt"
