#!/bin/bash
# E1, E2, E11 : bras A avec phase de conception (3 rondes), bras B --depuis A ; simulation, isolation d'utilisateur (root)
set -e
mount --bind /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/vartmp /var/tmp
cd /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/code/essaim-m3-refonte-v1
PY="/opt/essaim-m3-venv-v1/bin/python -B"
R=/tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/courses-e1
rm -rf $R; mkdir -p $R
$PY -m essaim_m3 simuler --sortie $R/A --generations 3 --graine 31 --n-train 8 --n-test 8 --n-final 8 --appels-max 20    --especes GEMINI_ARGON --organisme-amorcage /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/explorateur --rondes-conception-max 3 --entrainements-max 2    --recherches-max 2 --telechargements-max 2 --isoler-reseau > $R/A.sortie.json
$PY -m essaim_m3 simuler --sortie $R/B --generations 3 --graine 31 --depuis $R/A --appels-max 20 --entrainements-max 0    --recherches-max 2 --telechargements-max 2 --isoler-reseau > $R/B.sortie.json
# E2 : la même chose, mais l'organisme ne donne pas de successeur en génération notée >= 1 quand le gradient est servi
cp -a /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/explorateur /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/explorateur-arret
echo '{"arret_si_gradient_g1": true, "curieux": false, "fichiers_a_lire": []}' > /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/explorateur-arret/organisme/config.json
$PY -m essaim_m3 simuler --sortie $R/A2 --generations 3 --graine 32 --n-train 8 --n-test 8 --n-final 8 --appels-max 20    --especes GEMINI_ARGON --organisme-amorcage /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/explorateur-arret --rondes-conception-max 3 --entrainements-max 2    --relances-max 0 --isoler-reseau > $R/A2.sortie.json
$PY -m essaim_m3 simuler --sortie $R/B2 --generations 3 --graine 32 --depuis $R/A2 --appels-max 20 --entrainements-max 0    --relances-max 0 --isoler-reseau > $R/B2.sortie.json
echo fini
