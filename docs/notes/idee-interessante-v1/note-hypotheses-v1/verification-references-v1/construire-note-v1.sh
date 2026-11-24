#!/bin/bash
set -e
S=/tmp/claude-0/-home-user-controle-ia-travail/5053bc70-8b17-5f5f-bc14-784058ecfc47/scratchpad/note
cd $S
cat 00-preambule.tex 01-tete.tex 02-h1-h5.tex 03-h6-h10.tex 04-messages-4-6.tex 04b-message-7.tex 05-cours-a.tex 06-cours-b.tex 07-partie3.tex 08-annexes-tete.tex 08-annexe-argon.tex 08-annexe-carbon.tex 08-annexe-neon.tex 09-biblio.tex 99-fin.tex > build/note-hypotheses-et-appuis-v1.tex
cd build
for i in 1 2 3; do xelatex -interaction=nonstopmode -halt-on-error note-hypotheses-et-appuis-v1.tex > log$i.txt 2>&1 || { grep -n "^!" -A6 log$i.txt | head -20; exit 1; }; done
echo "pages: $(pdfinfo note-hypotheses-et-appuis-v1.pdf | grep Pages)"
echo "manquants: $(grep -c 'Missing character' note-hypotheses-et-appuis-v1.log)"
grep -o "Overfull \\\\hbox ([0-9.]*pt" note-hypotheses-et-appuis-v1.log | awk -F'(' '{print $2}' | sort -n | awk '{a[NR]=$1} END {print "overfull n="NR", max="a[NR]", >10pt: " (function(){c=0; for(i in a) if (a[i]+0>10) c++; return c})()}' 2>/dev/null || true
