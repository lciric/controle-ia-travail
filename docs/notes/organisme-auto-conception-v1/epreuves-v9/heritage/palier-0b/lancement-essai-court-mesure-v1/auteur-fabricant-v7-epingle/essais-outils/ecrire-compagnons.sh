#!/bin/bash
# Écrit, pour chaque fichier donné, son compagnon FICHIER.sha256 (« empreinte  nom »), sans rien écraser.
# Emploi : ecrire-compagnons.sh FICHIER...
set -u
for f in "$@"; do
  if [ -e "$f.sha256" ]; then echo "déjà présent : $f.sha256"; continue; fi
  (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256") && cat "$f.sha256"
done
