#!/usr/bin/env bash
# Préparation du disque de la lecture des sondes du barreau 8, par la conductrice, juste avant le lancement du lecteur.
# Arbre de travail neuf sur origin/main (qui doit porter : extrait des états et ligne ETATS-COURSE-IIB, attestation de la
# course et de l'oracle, mandats scellés, sortie de la recette de puissance) ; livraison rapatriée sans être ouverte, ignorée
# localement (info/exclude, non commité) pour que l'arbre reste propre ; fichiers de sondes et de planchers copiés (ignorés :
# donnees/). Rien n'est lu de la livraison ni de la course.
set -euo pipefail
DEPOT=/home/user/controle-ia-travail
ARBRE=/home/user/b8-lecture-arbre
LIV=versement/20261124-122719-rejeu-activations-voie-a/sortie-passe/livraison
cd "$DEPOT"
git fetch -q origin main
git fetch -q origin refs/heads/donnees/passe-activations-voie-a-v1:refs/remotes/origin/donnees/passe-activations-voie-a-v1
[ -e "$ARBRE" ] && { echo "REFUS : $ARBRE existe déjà"; exit 2; }
REG=$(git show origin/main:registres/sondes-iib-v1.md)
for cle in SCELLEMENT-SONDES-IIB SCELLEMENT-ADDITIF-1-SONDES-IIB SCELLEMENT-ADDITIF-2-SONDES-IIB CODE-PASSE-IIB LIVRAISON-PASSE-IIB CODE-LECTURE-SONDES-IIB ETATS-COURSE-IIB; do
  grep -q "^| $cle |" <<<"$REG" || { echo "REFUS : ligne $cle absente de origin/main"; exit 2; }
done
grep -q "^| LECTURE-SONDES-IIB |" <<<"$REG" && { echo "REFUS : LECTURE-SONDES-IIB déjà inscrite"; exit 2; }
git worktree add -q --detach "$ARBRE" origin/main
EXCL=$(git rev-parse --git-common-dir)/info/exclude
grep -qxF "/$LIV/" "$EXCL" 2>/dev/null || echo "/$LIV/" >> "$EXCL"
git archive origin/donnees/passe-activations-voie-a-v1 "$LIV" | tar -x -C "$ARBRE"
mkdir -p "$ARBRE/donnees/20261114-001352-t07-lecture-reel"
cp donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz.sha256 \
   donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz.sha256 \
   "$ARBRE/donnees/20261114-001352-t07-lecture-reel/"
cd "$ARBRE"
(cd donnees/20261114-001352-t07-lecture-reel && sha256sum -c planchers-figees-t07.npz.sha256 sondes-neuves-t07.npz.sha256)
(cd donnees/20261019-230011-p3-reel && sha256sum -c sondes-figees-legeres.npz.sha256)
ln -s "$DEPOT/.venv" .venv
grep -qxF "/.venv" "$EXCL" || echo "/.venv" >> "$EXCL"
[ -z "$(git status --porcelain)" ] && echo "ARBRE DE LECTURE PRÊT ET PROPRE : $ARBRE, commit $(git rev-parse HEAD)" || { echo "ARBRE NON PROPRE :"; git status --porcelain | cut -c1-120; exit 2; }
