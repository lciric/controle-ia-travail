#!/bin/bash
# usage: mut.sh "old" "new" "-k expr"
cd /home/user/controle-ia-travail
MUT_OLD="$1" MUT_NEW="$2" PYTHONPATH=src:/tmp/claude-0/-home-user-controle-ia-travail/445c1b8c-c9f5-52f6-966f-fc165ad0e0c8/scratchpad/plug timeout 600 .venv/bin/python -m pytest -q -x -p mutplug tests/test_lanceur_bras_a_v4.py -k "$3" 2>&1 | tail -2
