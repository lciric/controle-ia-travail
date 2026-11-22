#!/bin/bash
# Fabrique un petit dépôt nu FACTICE qui porte déjà la branche de récupération (un commit vide), pour l'essai F16 du
# fabricant (« branche déjà présente » : refus 8).
# Emploi : fabriquer-depot-avec-branche.sh DOSSIER_NEUF
set -eu -o pipefail
[ ! -e "$1" ] || { echo "refus : $1 existe" >&2; exit 1; }
export GIT_AUTHOR_NAME=factice GIT_AUTHOR_EMAIL=factice@invalid GIT_COMMITTER_NAME=factice GIT_COMMITTER_EMAIL=factice@invalid
git init -q --bare "$1"
T=$(git -C "$1" mktree < /dev/null)
C=$(git -C "$1" commit-tree "$T" -m "branche factice deja presente")
git -C "$1" update-ref refs/heads/recuperation/palier-0b-programme-1-essai-3-v1 "$C"
git -C "$1" for-each-ref
