#!/usr/bin/env bash
# Extraction fichier par fichier (git show), au commit 42cdfcf29, des seuls mesures.jsonl et bloc.json des 64 blocs
# de la course de dose-réponse. Aucun *.npz n'est touché (le motif de nom l'exclut ; contrôle final).
set -euo pipefail
DEPOT=/home/user/controle-ia-travail
SORTIE="$1"
C=42cdfcf29
RACINE=donnees/20261125-093202-dose-reponse/blocs
mkdir -p "$SORTIE"
cd "$DEPOT"
n=0
for b in $(git ls-tree --name-only $C $RACINE/ | sed "s#^$RACINE/##"); do
  mkdir -p "$SORTIE/$b"
  for f in mesures.jsonl bloc.json; do
    git show "$C:$RACINE/$b/$f" > "$SORTIE/$b/$f"
  done
  n=$((n+1))
done
echo "blocs extraits : $n"
if find "$SORTIE" -name '*.npz' -o -name '*.safetensors' | grep -q .; then echo "ERREUR : fichier interdit present"; exit 1; fi
echo "aucun npz ni safetensors dans $SORTIE"
