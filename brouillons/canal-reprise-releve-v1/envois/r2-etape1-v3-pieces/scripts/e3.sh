#!/bin/bash
# E3 : dossier des courses traversable (comme un DOSSIER_DES_COURSES créé par mkdir -p sous un chemin ouvert) ;
# E3-correction : le même dossier en 0700 ; simulation, isolation d'utilisateur (root), espace de noms de montage privé
set -e
mount --bind /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/vartmp /var/tmp
mount --bind /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/srv /srv
cd /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/code/essaim-m3-refonte-v1
PY="/opt/essaim-m3-venv-v1/bin/python -B"
mkdir -p /srv/entrees/traits; head -c 4096 /dev/urandom > /srv/entrees/traits/traits-x.npz; chmod 0644 /srv/entrees/traits/traits-x.npz
$PY -m essaim_m3 simuler --sortie /srv/A --generations 2 --graine 41 --n-train 6 --n-test 6 --n-final 4 --appels-max 20    --especes GEMINI_ARGON CLAUDE_OPUS_5_5 --organisme-amorcage /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/explorateur-curieux --rondes-conception-max 1    --entrainements-max 1 --isoler-reseau > /srv/A.sortie.json
$PY -m essaim_m3 simuler --sortie /srv/B --generations 2 --graine 41 --depuis /srv/A --appels-max 20 --entrainements-max 0    --isoler-reseau > /srv/B.sortie.json
ls -ld /srv /srv/A /srv/A/archive_vue /srv/A/archive_vue/gemini-argon /srv/entrees /srv/A.sortie.json
# correction : dossier des courses en 0700 (espace des organismes déplacé sous /var/tmp/essaim-m3/<empreinte>)
chmod 0700 /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/srv
$PY -m essaim_m3 simuler --sortie /srv/A3 --generations 2 --graine 43 --n-train 6 --n-test 6 --n-final 4 --appels-max 20    --especes GEMINI_ARGON CLAUDE_OPUS_5_5 --organisme-amorcage /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/explorateur-curieux --rondes-conception-max 1    --entrainements-max 1 --isoler-reseau > /srv/A3.sortie.json
$PY -m essaim_m3 simuler --sortie /srv/B3 --generations 2 --graine 43 --depuis /srv/A3 --appels-max 20 --entrainements-max 0    --isoler-reseau > /srv/B3.sortie.json
chmod 0755 /tmp/claude-0/-home-user-controle-ia-travail/325f961c-9943-5b73-9387-393664866547/scratchpad/r2-etape1-v3/travail/exp/srv
echo fini
