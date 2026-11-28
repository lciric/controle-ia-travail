#!/usr/bin/env bash
# Outil de travail du correcteur de la chaîne v3 : sceau compagnon (format sha256sum, nom relatif) pour chaque fichier de
# …/chaine-v3/ qui n'est pas lui-même un sceau ; contrôle de tous les sceaux ; aucun __pycache__.
set -euo pipefail
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v3
cd "$H"
for f in *; do case "$f" in *.sha256) continue ;; esac; [ -f "$f" ] && sha256sum "$f" > "$f.sha256"; done
for s in *.sha256; do sha256sum -c --quiet "$s"; done
n=$(ls | grep -vc '\.sha256$'); m=$(ls | grep -c '\.sha256$')
[ "$n" = "$m" ] || { echo "fichiers $n ≠ sceaux $m"; exit 1; }
[ -z "$(find "$H" -name __pycache__)" ] || { echo "__pycache__ présent"; exit 1; }
echo "sceaux : $m, tous conformes"
