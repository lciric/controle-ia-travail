#!/usr/bin/env bash
# Lancement de la recette de puissance du barreau 8 (condition de départ D-10 ; RP-4), code de la lecture version 6.
# À jouer seulement quand la ligne CODE-LECTURE-SONDES-IIB est inscrite sur origin/main par la mère.
set -euo pipefail
DEPOT=/home/user/controle-ia-travail
ARBRE=/home/user/b8-puissance-arbre
PY=$DEPOT/.venv/bin/python
ENTROPIE=149333987590752343984325077404464904184   # champ F-3 du texte scellé
cd "$DEPOT"
git fetch -q origin main
grep -q '^| CODE-LECTURE-SONDES-IIB |' <(git show origin/main:registres/sondes-iib-v1.md) || { echo "REFUS : ligne CODE-LECTURE-SONDES-IIB absente de origin/main"; exit 2; }
git show origin/main:src/controle_ia/barreau8_moniteurs/lecture_sondes_v6.py > /dev/null || { echo "REFUS : code v6 absent de origin/main"; exit 2; }
[ -e "$ARBRE" ] && { echo "REFUS : $ARBRE existe déjà"; exit 2; }
git worktree add -q --detach "$ARBRE" origin/main
cd "$ARBRE"
[ -z "$(git status --porcelain)" ] || { echo "REFUS : arbre non propre"; exit 2; }
grep -q "$ENTROPIE" prereg/lecture-sondes-barreau8-v1.md || { echo "REFUS : entropie absente du texte scellé"; exit 2; }
RUN_ID=$(date -u +%Y%m%d-%H%M%S)-puissance-barreau8
echo "$RUN_ID" > "$DEPOT/../b8-puissance-run-id.txt"
JOURNAL=/home/user/b8-puissance-$RUN_ID.log
setsid nohup env PYTHONPATH=src "$PY" -m controle_ia.barreau8_moniteurs.lecture_sondes_v6 puissance \
  --racine . --registre registres/sondes-iib-v1.md --entropie "$ENTROPIE" --run-id "$RUN_ID" \
  > "$JOURNAL" 2>&1 < /dev/null &
PID=$!
echo "$PID" > /home/user/b8-puissance.pid
echo "LANCÉE run_id=$RUN_ID pid=$PID commit=$(git rev-parse HEAD) journal=$JOURNAL début=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
