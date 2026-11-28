#!/bin/bash
# Grille reduite de E2 (reduction declaree : 60 mondes par alternative, 200 par nul), reprise des mondes deja ecrits.
# Usage : e2_lancer_v2.sh DEPOT DOSSIER
DEPOT="$1"; D="$2"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH="$DEPOT/src"
PY="$DEPOT/.venv/bin/python"; S="$D/scripts/e2_monde_plante.py"; O="$D/sorties/e2"
run() {  # scenario dose cible : complete le fichier jusqu'a `cible` mondes
  f="$O/$1-$2.jsonl"; deja=0; [ -f "$f" ] && deja=$(wc -l < "$f")
  reste=$(( $3 - deja )); [ "$reste" -gt 0 ] && "$PY" "$S" "$1" "$2" "$reste" "$f" "$deja"
}
( run alt_0.70 faible 60; run nul_aucun_signal faible 200 ) >> "$O/journal-1.txt" 2>&1 &
( run alt_0.70 porte 60; run nul_presence_consigne faible 200 ) >> "$O/journal-2.txt" 2>&1 &
( run alt_0.65 faible 60; run alt_0.60 porte 60 ) >> "$O/journal-3.txt" 2>&1 &
( run alt_0.65 porte 60; run alt_0.60 faible 60; run nul_longueur_seule faible 200; run alt_0.55 faible 60 ) >> "$O/journal-4.txt" 2>&1 &
wait
echo fini
