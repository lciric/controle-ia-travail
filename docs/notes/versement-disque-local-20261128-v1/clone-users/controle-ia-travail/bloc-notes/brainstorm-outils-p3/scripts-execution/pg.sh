#!/bin/sh
# usage: pg.sh fichier.pdf page [motif]
f="$1"; p="$2"; m="$3"
if [ -z "$m" ]; then pdftotext -f "$p" -l "$p" -layout "$f" - ; else pdftotext -f "$p" -l "$p" -layout "$f" - | grep -n -i -E "$m"; fi
