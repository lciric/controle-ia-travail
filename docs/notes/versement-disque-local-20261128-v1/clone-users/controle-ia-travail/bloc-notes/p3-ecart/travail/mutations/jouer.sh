#!/usr/bin/env bash
# jouer.sh NOM FICHIER AVANT APRES TEST... : mutation, tests visés, restauration ; écrit la dernière ligne de pytest
W=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3-ecart/travail
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
export GIT_CONFIG_COUNT=4 GIT_CONFIG_KEY_3=commit.gpgsign GIT_CONFIG_VALUE_3=false
nom=$1; f=$2; avant=$3; apres=$4; shift 4
cd $W/depot || exit 2
[ -z "$(git status --short)" ] || { echo "clone sale avant $nom"; exit 2; }
python3 -I $W/mutations/muter.py "$f" "$avant" "$apres" || exit 2
PYTHONPATH=src $PY -m pytest -q -p no:cacheprovider -x "$@" > $W/mutations/$nom.txt 2>&1; c=$?
git checkout -q -- "$f"
[ -z "$(git status --short)" ] || { echo "clone sale après $nom"; exit 2; }
echo "$nom : code $c ; $(tail -n 1 $W/mutations/$nom.txt)"
