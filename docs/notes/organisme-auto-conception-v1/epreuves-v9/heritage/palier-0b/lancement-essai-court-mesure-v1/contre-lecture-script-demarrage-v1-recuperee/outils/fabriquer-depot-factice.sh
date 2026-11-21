#!/bin/bash
# Refait le dépôt distant FACTICE partagé de mon banc : un dépôt nu local, rempli du seul commit d7f949ac par un fetch
# superficiel LOCAL (file://) depuis le dépôt de travail (lu seulement). Aucun réseau.
set -eu -o pipefail
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
P=$ME/auteur/travail/distant/controle-ia-travail.git
C=d7f949acd9ac92e998e57663d2cc741de93f18c3
[ ! -e "$P" ] || { echo "refus : $P existe"; exit 1; }
mkdir -p "$ME/auteur/travail/distant"
git init -q --bare "$P"
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
git -C "$P" fetch --depth 1 file:///home/user/controle-ia-travail "$C"
git -C "$P" update-ref refs/heads/main "$C"
echo "tête de main du dépôt factice : $(git -C "$P" rev-parse refs/heads/main)"
du -sh "$P"
