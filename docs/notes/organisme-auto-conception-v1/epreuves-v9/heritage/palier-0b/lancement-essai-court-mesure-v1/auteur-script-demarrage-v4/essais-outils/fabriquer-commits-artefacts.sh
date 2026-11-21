#!/bin/bash
# Fabrique, dans le dépôt distant FACTICE partagé (travail/distant), deux commits artefacts sans parent, à partir de l'arbre
# du commit d7f949ac (dépôt factice seulement ; le dépôt de travail n'est pas touché) :
#   artefact-git   : arbre du commit + une entrée « .git » à la racine (dossier qui porte un fichier HEAD) ;
#   artefact-autre : arbre du commit + un fichier en trop à la racine (aucun .git).
# Écrit les deux identifiants dans travail/commits-artefacts.txt.
set -eu -o pipefail
ICI=$(cd "$(dirname "$0")" && pwd)
P=$(dirname "$ICI")/travail/distant/controle-ia-travail.git
export GIT_AUTHOR_NAME=factice GIT_AUTHOR_EMAIL=factice@invalid GIT_COMMITTER_NAME=factice GIT_COMMITTER_EMAIL=factice@invalid
export GIT_AUTHOR_DATE=2026-11-21T00:00:00Z GIT_COMMITTER_DATE=2026-11-21T00:00:00Z
T=$(git -C "$P" rev-parse d7f949acd9ac92e998e57663d2cc741de93f18c3^{tree})
BL=$(echo "ref: refs/heads/main" | git -C "$P" hash-object -w --stdin)
ST=$(printf '100644 blob %s\tHEAD\n' "$BL" | git -C "$P" mktree)
T1=$( { git -C "$P" ls-tree "$T"; printf '040000 tree %s\t.git\n' "$ST"; } | git -C "$P" mktree)
C1=$(git -C "$P" commit-tree "$T1" -m "artefact : .git dans l'arbre")
git -C "$P" update-ref refs/heads/artefact-git "$C1"
B2=$(echo "fichier en trop" | git -C "$P" hash-object -w --stdin)
T2=$( { git -C "$P" ls-tree "$T"; printf '100644 blob %s\tfichier-en-trop.txt\n' "$B2"; } | git -C "$P" mktree)
C2=$(git -C "$P" commit-tree "$T2" -m "artefact : fichier en trop")
git -C "$P" update-ref refs/heads/artefact-autre "$C2"
{ echo "artefact-git $C1"; echo "artefact-autre $C2"; } > "$(dirname "$ICI")/travail/commits-artefacts.txt"
git -C "$P" ls-tree "$C1" -- .git
cat "$(dirname "$ICI")/travail/commits-artefacts.txt"
