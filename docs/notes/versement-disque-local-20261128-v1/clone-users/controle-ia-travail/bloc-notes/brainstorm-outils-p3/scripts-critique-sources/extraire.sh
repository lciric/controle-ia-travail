#!/bin/bash
# extraire.sh PDF -> txt-critique-sources/<base>.txt (pdftotext -layout, pages separees par \f)
B=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/brainstorm-outils-p3
for f in "$@"; do b=$(basename "$f" .pdf); pdftotext -layout "$f" "$B/txt-critique-sources/$b.txt"; done
