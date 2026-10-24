#!/bin/bash
set -e
mount --bind /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/vartmp /var/tmp
cd /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/code/essaim-m3-refonte-v1
PY="/opt/essaim-m3-venv-v1/bin/python -B"
R=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/courses-e4; rm -rf $R; mkdir -p $R
$PY -m essaim_m3 simuler --sortie $R/A --generations 2 --graine 51 --n-train 6 --n-test 6 --n-final 4 --appels-max 20    --especes GEMINI_ARGON --organisme-amorcage /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/falsificateur --entrainements-max 1 --recherches-max 2    --telechargements-max 3 --isoler-reseau > $R/A.sortie.json
ESP=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['espace_organismes'])" $R/A/manifeste-run.json)
echo "espace : $ESP"
echo "--- contrôle humain de la liste d'arrêt (vue de l'archive) :"
find "$ESP"/archive_vue* \( -name juge -o -name journal-entrainements.jsonl -o -name modele.npz \) | sed "s#$ESP#<espace>#"
