#!/usr/bin/env bash
# Relance détachée de la garde de réception, dans l'arbre déjà préparé, seulement après un arrêt technique établi.
set -euo pipefail
ARBRE=/home/user/b8-reception-arbre
PY=/home/user/controle-ia-travail/.venv/bin/python
cd "$ARBRE"
SORTIE=/home/user/b8-reception-sortie-$(date -u +%Y%m%d-%H%M%S)-relance.txt
setsid nohup bash -c "env PYTHONPATH=src '$PY' -m controle_ia.barreau8_moniteurs.lecture_sondes_v6 reception --racine . --registre registres/sondes-iib-v1.md --sondes-legeres donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz --planchers donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz --sondes-neuves donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz > '$SORTIE' 2>&1; echo \$? > '$SORTIE.code'" < /dev/null > /dev/null 2>&1 &
echo "relance détachée pid=$! sortie=$SORTIE"
