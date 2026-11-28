#!/usr/bin/env bash
# Témoin T2 (c) : les deux suites d'oracles passent-elles encore quand le paquet du dépôt est cassé (ImportError à l'import) ?
# Copies des deux fichiers de tests, jouées hors du dépôt, PYTHONPATH pointant sur un paquet controle_ia empoisonné.
set -uo pipefail
S="$1"; PY=/home/user/controle-ia-travail/.venv/bin/python
cd "$S/sorties/t2c/isole"
sha256sum test_oracles_r5_cloture_etages_1_2.py test_contre_epreuve_v4_r5.py
echo "--- imports du paquet du dépôt dans les deux fichiers (attendu : aucun)"
grep -n -E "controle_ia|sys\.path|importlib|from \.\.|open\(|read_text|Path\(" test_oracles_r5_cloture_etages_1_2.py test_contre_epreuve_v4_r5.py || echo "aucune ligne"
echo "--- contrôle du poison : l'import échoue bien"
PYTHONPATH="$S/sorties/t2c/poison" $PY -c "import controle_ia" 2>&1 | tail -1
echo "--- suites jouées avec le paquet empoisonné"
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH="$S/sorties/t2c/poison" $PY -m pytest -q -p no:cacheprovider --rootdir "$S/sorties/t2c/isole" -c /dev/null test_oracles_r5_cloture_etages_1_2.py test_contre_epreuve_v4_r5.py 2>&1 | tail -6
