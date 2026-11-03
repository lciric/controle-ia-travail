#!/bin/bash
D=/home/user/hors-clone-a1-v3
cd /home/user/ideation-organism/orchestrator
nohup setsid env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME=$D TMPDIR=/tmp nice -n 10 python3 -I -B demonstrations/attaque_goodhart_v3.py $D/sortie-attaque-goodhart-v3 \
    --preenregistrement prereg/preenregistrement-attaque-goodhart-v3-v1.md \
    --configuration /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/configuration-mini-course-kimi-argon-v3.json \
    --moteur reel --confirmer-moteur-reel \
    --registre-go $D/registre-go.md --go GO-2026-11-02-21 > $D/course-stdout-a1-v3.log 2>&1 < /dev/null &
P=$!
echo $P > $D/course.pid
echo $P
