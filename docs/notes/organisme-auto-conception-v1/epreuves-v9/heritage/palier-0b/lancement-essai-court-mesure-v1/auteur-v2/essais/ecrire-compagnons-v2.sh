#!/bin/bash
# Écrit, pour chaque fichier donné, son compagnon FICHIER.sha256 (« empreinte  nom »), sans rien écraser.
# Usage : ecrire-compagnons-v2.sh FICHIER...
set -u
for f in "$@"; do
  d=$(dirname "$f")
  b=$(basename "$f")
  if [ -e "$f.sha256" ]; then echo "refus : $f.sha256 existe" >&2; continue; fi
  (cd "$d" && sha256sum "$b" > "$b.sha256" && cat "$b.sha256")
done
