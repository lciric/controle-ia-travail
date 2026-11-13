#!/bin/bash
# Parties de la famille v4, un processus à la fois, mémoire bornée ; ne refait que les parties absentes.
ICI=$(cd "$(dirname "$0")" && pwd); S="$ICI/../sorties-v4"; J="$S/journal-sorties-v4.txt"
ulimit -v 6000000; export OMP_NUM_THREADS=2
for r in $(seq 0 11); do
  f="$S/partie-v4-monde-$r.json"
  [ -f "$f" ] && continue
  python3 -I -B "$ICI/monde_riche_v4.py" partie "$r" "$f" > "$S/partie-v4-monde-$r.stdout" 2>&1
  echo "$(date -u +%FT%TZ) partie monde $r code $?" >> "$J"
done
[ -f "$S/resume-v4.json" ] || { python3 -I -B "$ICI/monde_riche_v4.py" resume "$S" "$S/resume-v4.json" > "$S/resume-v4.stdout" 2>&1; echo "$(date -u +%FT%TZ) résumé code $?" >> "$J"; }
echo "$(date -u +%FT%TZ) fin" >> "$J"
