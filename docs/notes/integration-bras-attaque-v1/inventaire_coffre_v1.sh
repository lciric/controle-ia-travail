#!/usr/bin/env bash
# Inventaire mécanique du coffre du bras d'attaque — v1.
# N'affiche QUE des comptes, des identifiants de commit et des dates. Aucun nom de fichier, aucun contenu.
# Usage : inventaire_coffre_v1.sh <racine du dépôt> <branche> [<branche> ...]
set -u
cd "$1" || exit 2; shift
printf '| branche | commit | premier commit propre (UTC) | dernier commit (UTC) | commits propres | fichiers propres | compagnons .sha256 | empreintes conformes | non conformes | cible absente |\n'
printf '|---|---|---|---|---:|---:|---:|---:|---:|---:|\n'
for b in "$@"; do
  if ! git fetch --quiet origin "refs/heads/$b:refs/remotes/origin/$b" 2>/dev/null; then
    printf '| `%s` | ÉCHEC DU RAPATRIEMENT | | | | | | | | |\n' "$b"; continue
  fi
  ref="refs/remotes/origin/$b"
  c=$(git rev-parse --short=8 "$ref")
  base=$(git merge-base origin/main "$ref" 2>/dev/null || true)
  if [ -n "$base" ]; then
    ncommits=$(git rev-list --count "$base..$ref")
    first=$(git log --reverse --format=%cI "$base..$ref" | head -1)
    mapfile -d '' files < <(git diff --name-only -z --diff-filter=AM "$base" "$ref")
  else
    ncommits=$(git rev-list --count "$ref")
    first=$(git log --reverse --format=%cI "$ref" | head -1)
    mapfile -d '' files < <(git ls-tree -r --name-only -z "$ref")
  fi
  last=$(git log -1 --format=%cI "$ref")
  first=$(date -u -d "${first:-$last}" +%Y-%m-%dT%H:%MZ); last=$(date -u -d "$last" +%Y-%m-%dT%H:%MZ)
  nf=${#files[@]}; ncomp=0; ok=0; ko=0; abs=0
  for f in "${files[@]}"; do
    case "$f" in *.sha256)
      ncomp=$((ncomp+1)); cible="${f%.sha256}"
      attendu=$(git cat-file blob "$ref:$f" 2>/dev/null | awk 'NR==1{print $1}')
      if git cat-file -e "$ref:$cible" 2>/dev/null; then
        reel=$(git cat-file blob "$ref:$cible" | sha256sum | awk '{print $1}')
        if [ "$attendu" = "$reel" ]; then ok=$((ok+1)); else ko=$((ko+1)); fi
      else abs=$((abs+1)); fi;;
    esac
  done
  printf '| `%s` | `%s` | %s | %s | %s | %s | %s | %s | %s | %s |\n' "$b" "$c" "$first" "$last" "$ncommits" "$nf" "$ncomp" "$ok" "$ko" "$abs"
done
