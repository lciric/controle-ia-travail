#!/usr/bin/env bash
# Garde de réception r1 à r8 de la livraison de la passe (condition de départ D-11), code de la lecture version 6.
# Jouée par la conductrice du côté des moniteurs, sur l'accord de la mère, après la ligne CODE-LECTURE-SONDES-IIB.
# La livraison est rapatriée sans être ouverte ni listée ; la sortie de la commande va dans un fichier ;
# seule la première ligne (« GARDE DE RÉCEPTION TENUE » ou le refus et sa cause) est affichée ; le repère r8 n'est pas affiché.
set -euo pipefail
DEPOT=/home/user/controle-ia-travail
ARBRE=/home/user/b8-reception-arbre
PY=$DEPOT/.venv/bin/python
LIV=versement/20261124-122719-rejeu-activations-voie-a/sortie-passe/livraison
cd "$DEPOT"
git fetch -q origin main
git fetch -q origin refs/heads/donnees/passe-activations-voie-a-v1:refs/remotes/origin/donnees/passe-activations-voie-a-v1
grep -q '^| CODE-LECTURE-SONDES-IIB |' <(git show origin/main:registres/sondes-iib-v1.md) || { echo "REFUS : ligne CODE-LECTURE-SONDES-IIB absente"; exit 2; }
[ -e "$ARBRE" ] && { echo "REFUS : $ARBRE existe déjà"; exit 2; }
git worktree add -q --detach "$ARBRE" origin/main
# rapatriement du seul dossier de la livraison, sans affichage
git archive origin/donnees/passe-activations-voie-a-v1 "$LIV" | tar -x -C "$ARBRE"
# fichiers de sondes et de planchers (D-8) : copiés depuis le dépôt principal, où leurs empreintes ont été contrôlées
mkdir -p "$ARBRE/donnees/20261114-001352-t07-lecture-reel"
cp donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz* donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz "$ARBRE/donnees/20261114-001352-t07-lecture-reel/"
cp donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz.sha256 "$ARBRE/donnees/20261114-001352-t07-lecture-reel/"
cd "$ARBRE"
SORTIE=/home/user/b8-reception-sortie-$(date -u +%Y%m%d-%H%M%S).txt
set +e
env PYTHONPATH=src "$PY" -m controle_ia.barreau8_moniteurs.lecture_sondes_v6 reception --racine . --registre registres/sondes-iib-v1.md \
  --sondes-legeres donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz \
  --planchers donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz \
  --sondes-neuves donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz > "$SORTIE" 2>&1
CODE=$?
set -e
echo "code de sortie : $CODE ; sortie complète gardée dans $SORTIE (non affichée)"
if [ $CODE -eq 0 ]; then head -n 1 "$SORTIE"; else grep -m 1 -E "Refus|REFUS|refus|GardeArret|Error|Traceback" "$SORTIE" | cut -c1-400; fi
