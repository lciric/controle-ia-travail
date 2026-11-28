#!/bin/bash
# Complement de la grille de E2 : porte les cellules a aire vraie 0,65 a 60 mondes et la cellule 0,70 a la dose de la porte a 40.
DEPOT="$1"; D="$2"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH="$DEPOT/src"
PY="$DEPOT/.venv/bin/python"; S="$D/scripts/e2_monde_plante.py"; O="$D/sorties/e2"
run() { f="$O/$1-$2.jsonl"; deja=0; [ -f "$f" ] && deja=$(wc -l < "$f"); reste=$(( $3 - deja )); [ "$reste" -gt 0 ] && "$PY" "$S" "$1" "$2" "$reste" "$f" "$deja"; }
( run alt_0.65 faible 60 ) >> "$O/journal-5.txt" 2>&1 &
( run alt_0.65 porte 60 ) >> "$O/journal-6.txt" 2>&1 &
( run alt_0.70 porte 40 ) >> "$O/journal-7.txt" 2>&1 &
wait
echo fini
