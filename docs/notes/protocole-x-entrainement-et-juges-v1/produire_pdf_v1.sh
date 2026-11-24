#!/usr/bin/env bash
# Markdown → HTML autonome (pandoc du venv, quelle que soit la version de Python) → PDF A4 (Chromium par Playwright).
# Usage : produire_pdf_v1.sh NOTE.md SORTIE.pdf "Pied de page". Reprend scripts/document_pdf.sh, dont le chemin de pandoc
# est fixé à Python 3.11 ; ici le chemin est cherché dans le venv. Rien n'est écrit ailleurs que SORTIE.
set -euo pipefail
ici="$(cd "$(dirname "$0")" && pwd)"; racine="$(cd "$ici/../../.." && pwd)"
pandoc="$(ls "$racine"/.venv/lib/python3.*/site-packages/pypandoc/files/pandoc | head -1)"
[ -x "$pandoc" ] || { echo "pandoc introuvable" >&2; exit 1; }
md="$1"; pdf="$2"; pied="$3"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
"$pandoc" "$md" -f markdown-yaml_metadata_block -t html5 --standalone --embed-resources --css "$ici/feuille-note-v1.css" \
  --metadata lang=fr --metadata pagetitle="$(head -1 "$md" | sed 's/^# //')" -o "$tmp/document.html"
NODE_PATH="$(npm root -g)" node "$racine/scripts/document_pdf.mjs" "$tmp/document.html" "$pdf" "$pied"
