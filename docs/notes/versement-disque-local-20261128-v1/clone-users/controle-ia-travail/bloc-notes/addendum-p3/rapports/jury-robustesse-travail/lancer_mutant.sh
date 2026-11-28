#!/bin/bash
# Lance la suite de tests (non modifiée) du candidat sur un mutant ; écrit tué ou survivant.
d="$1"
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/home/user/controle-ia-travail/src OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
cd "$d" || exit 1
debut=$(date +%s)
$PY -m pytest -x -q -p no:cacheprovider --basetemp="$d/base" test_complements_p3_v1.py > "$d/pytest.log" 2>&1
code=$?
fin=$(date +%s)
if [ $code -eq 0 ]; then etat=survivant; else etat=tué; fi
premier=$(grep -m1 -E "^FAILED|^ERROR" "$d/pytest.log" | cut -c1-160)
echo "$(basename "$d") | $etat | $((fin - debut)) s | $premier" > "$d/resultat.txt"
rm -rf "$d/base"
