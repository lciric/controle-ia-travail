#!/bin/bash
# Depot distant factice partage : fetch du commit d7f949ac du depot du programme (file://, lecture) dans un depot nu de mon dossier.
# Usage : preparer-distant.sh RB(neuf)
set -u
RB=$1
mkdir -m 700 $RB || exit 2
git init -q --bare $RB/partage.git || exit 2
git -C $RB/partage.git config uploadpack.allowAnySHA1InWant true
git -C $RB/partage.git fetch -q file:///home/user/controle-ia-travail d7f949acd9ac92e998e57663d2cc741de93f18c3 || exit 3
git -C $RB/partage.git update-ref refs/heads/main d7f949acd9ac92e998e57663d2cc741de93f18c3 || exit 4
echo "partage : $(git -C $RB/partage.git rev-parse refs/heads/main)"
