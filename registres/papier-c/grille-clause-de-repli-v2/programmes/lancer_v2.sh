#!/bin/bash
# Lanceur du lot neuf de la grille de la clause de repli (rapport v2), premiere passe seule (passe 0).
# Cases : entrees/cases_c_a_jouer_v2.txt (C-P3c, R = 8000) puis entrees/cases_ab_a_jouer_v2.txt (C-P3a et C-P3b,
# R = 1000, B = 1000). Quatre processus a la fois ; une sortie JSON et un .err par case, sous sorties/neuves-v2/.
# Graine : grille_commun_v2.generateur (SeedSequence(20261119, spawn_key = (programme, case, 0))).
# Mode « relance » : rejoue, avec la meme commande donc la meme graine, les seules cases sans sortie JSON ou dont le
# .err est non vide (cause technique) ; chaque relance est ecrite dans journal/relances_v2.txt.
# Interpreteur : /usr/local/bin/python3 (python 3.13.18, numpy 2.5.3, celui des sorties de v1).
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
PY=/usr/local/bin/python3
E=../entrees
S=../sorties/neuves-v2
J=../journal
mkdir -p $S $J
MODE=${1:-lot}
if [ "$MODE" = "lot" ]; then
  date -u +%FT%TZ > $J/DEBUT_c_v2
  cat $E/cases_c_a_jouer_v2.txt | xargs -P 4 -L 1 sh -c "$PY -B grille_c_v2.py \$0 \$1 \$2 \$3 8000 0 $S/c_\$0_\$1_k\$2_T\$3_p0.json 2> $S/c_\$0_\$1_k\$2_T\$3_p0.err"
  date -u +%FT%TZ > $J/FINI_c_v2
  cat $E/cases_ab_a_jouer_v2.txt | xargs -P 4 -L 1 sh -c "$PY -B grille_ab_v2.py \$0 \$1 \$2 \$3 1000 1000 0 $S/ab_\$0_\$1_k\$2_T\$3_p0.json 2> $S/ab_\$0_\$1_k\$2_T\$3_p0.err"
  date -u +%FT%TZ > $J/FINI_ab_v2
elif [ "$MODE" = "relance" ]; then
  : > $J/a_relancer_v2.txt
  while read m a k T; do
    o=$S/c_${m}_${a}_k${k}_T${T}_p0
    if [ ! -s $o.json ] || [ -s $o.err ]; then echo "c $m $a $k $T" >> $J/a_relancer_v2.txt; fi
  done < $E/cases_c_a_jouer_v2.txt
  while read m a k T; do
    o=$S/ab_${m}_${a}_k${k}_T${T}_p0
    if [ ! -s $o.json ] || [ -s $o.err ]; then echo "ab $m $a $k $T" >> $J/a_relancer_v2.txt; fi
  done < $E/cases_ab_a_jouer_v2.txt
  while read ty m a k T; do
    echo "$(date -u +%FT%TZ) relance $ty $m $a $k $T (meme graine)" >> $J/relances_v2.txt
    o=$S/${ty}_${m}_${a}_k${k}_T${T}_p0
    if [ "$ty" = "c" ]; then $PY -B grille_c_v2.py $m $a $k $T 8000 0 $o.json 2> $o.err
    else $PY -B grille_ab_v2.py $m $a $k $T 1000 1000 0 $o.json 2> $o.err; fi
  done < $J/a_relancer_v2.txt
else
  echo "mode inconnu : $MODE"; exit 2
fi
