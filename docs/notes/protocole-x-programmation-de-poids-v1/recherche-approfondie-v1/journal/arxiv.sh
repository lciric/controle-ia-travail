#!/usr/bin/env bash
# Usage : arxiv.sh "REQUETE (syntaxe de l'interface d'arXiv)" [max] [tri]
# Interroge export.arxiv.org, journalise, imprime les notices (une ligne chacune).
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
Q="$1"; MAX="${2:-50}"; TRI="${3:-submittedDate}"
ENC=$(python3 -I -c 'import sys,urllib.parse; print(urllib.parse.quote(sys.argv[1], safe=":"))' "$Q")
URL="https://export.arxiv.org/api/query?search_query=${ENC}&start=0&max_results=${MAX}&sortBy=${TRI}&sortOrder=descending"
OUT=$("$DIR/requete.sh" arxiv "$Q" "$URL" xml)
F=$(echo "$OUT" | awk '{print $4}')
TOT=$(grep -o '<opensearch:totalResults[^<]*' "$F" | sed 's/.*>//')
echo "## [$OUT] total=$TOT :: $Q"
python3 -I "$DIR/lire_arxiv.py" "$F" 2>/dev/null || echo "(réponse illisible)"
sleep 4
