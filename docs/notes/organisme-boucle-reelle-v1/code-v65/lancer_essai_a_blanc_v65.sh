#!/usr/bin/env bash
# Essai à blanc v65 de bout en bout (fournisseurs simulés, deux générations, exécuteur factice déclaré). Aucun appel, aucun réseau.
# Usage : bash lancer_essai_a_blanc_v65.sh ARBRE_ORGANISME DOSSIER_SORTIES PYTHON
set -u
O="$1/orchestrator"; S="$2"; PY="$3"; mkdir -p "$S"; cd "$O" || exit 9
etape() { local n="$1"; shift; local d=$(date -u +%H:%M:%S); "$@" > "$S/etape-$n.stdout" 2> "$S/etape-$n.stderr"; local c=$?;
          echo "étape $n | $d → $(date -u +%H:%M:%S) | code $c | $*"; }
etape 1 "$PY" -I -B demonstrations/boucle_reelle_v65.py "$S/course-bac-reel" --a-blanc --graine 20261110 --bac reel
etape 2 "$PY" -I -B demonstrations/boucle_reelle_v65.py "$S/course" --a-blanc --graine 20261110 --bac factice
etape 3 "$PY" -I -B demonstrations/lire_boucle_reelle_v65.py "$S/course" "$S/lecture-course.json"
etape 4 "$PY" -I -B demonstrations/boucle_reelle_v65.py "$S/course-arret" --a-blanc --graine 20261110 --bac factice --scenario-proposeur refus:2
etape 5 "$PY" -I -B demonstrations/lire_boucle_reelle_v65.py "$S/course-arret" "$S/lecture-course-arret.json"
etape 6 "$PY" -I -B demonstrations/boucle_reelle_v65.py "$S/course-part" --a-blanc --graine 20261110 --bac factice --cout-simule-usd 0.3 --plafond-kimi-usd 0.5 --plafond-argon-usd 7
etape 7 "$PY" -I -B demonstrations/boucle_reelle_v65.py "$S/course-bras" --a-blanc --graine 20261110 --bac factice --bras aleatoire
etape 8 "$PY" -I -B demonstrations/boucle_reelle_v65.py "$S/course-g3" --a-blanc --graine 20261110 --bac factice --generations 3
etape 9 "$PY" -I -B demonstrations/preparer_boucle_reelle_v65.py "$S/blocs"
