#!/bin/bash
# Markdown -> HTML (pandoc, feuille de style incluse) -> PDF (Chromium par Playwright). Usage : md_vers_pdf_playwright_v1.sh NOTE.md
set -euo pipefail
export LC_ALL=C.UTF-8
md="$(readlink -f "$1")"; pdf="${md%.md}.pdf"
[ -e "$pdf" ] && { echo "ARRÊT : $pdf existe ; rien n'est écrasé"; exit 1; }
t="$(mktemp -d)"
cat > "$t/style.css" <<'CSS'
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.5pt; line-height: 1.42; color: #111; margin: 0; }
h1 { font-size: 17pt; } h2 { font-size: 13.5pt; margin-top: 1.3em; border-bottom: 1px solid #ccc; } h3 { font-size: 11.5pt; margin-top: 1.1em; }
table { border-collapse: collapse; width: 100%; font-size: 8.4pt; margin: .5em 0; page-break-inside: auto; }
tr { page-break-inside: avoid; } th, td { border: 1px solid #bbb; padding: 2px 4px; vertical-align: top; text-align: left; } th { background: #f0f0f0; }
code { font-size: 7.6pt; word-break: break-all; } blockquote { color: #444; border-left: 3px solid #ccc; margin-left: 0; padding-left: .8em; }
CSS
pandoc "$md" -f gfm -t html5 -s --embed-resources --css "$t/style.css" --metadata pagetitle="$(basename "${md%.md}")" -o "$t/page.html"
node -e "
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://$t/page.html'); await p.pdf({ path: '$pdf', format: 'A4', margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' }, printBackground: true });
  await b.close(); })();"
[ -s "$pdf" ] || { echo "ARRÊT : PDF vide"; exit 1; }
rm -rf "$t"; echo "$pdf"
