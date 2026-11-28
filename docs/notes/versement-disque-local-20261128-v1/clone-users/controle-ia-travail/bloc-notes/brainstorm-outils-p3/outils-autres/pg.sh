#!/bin/bash
# usage: pg.sh fichier.txt motif [contexte]
f=$1; pat=$2; c=${3:-0}
awk -v pat="$pat" -v c="$c" 'BEGIN{p=1; IGNORECASE=1} {n=split($0,a,"\f"); for(i=1;i<=n;i++){ if(i>1)p++; line[NR]=a[i]; pg[NR]=p; if(a[i] ~ pat) hits[NR]=1 } } END{for(r=1;r<=NR;r++) if(hits[r]){ for(k=r-c;k<=r+c;k++) if(k>=1&&k<=NR) printf "p.%d | %s\n", pg[k], line[k]; if(c>0) print "--"}}' "$f"
