#!/bin/bash
# Écrit un compagnon .sha256 (format sha256sum, nom de base) pour chaque fichier du dossier et du sous-dossier d'épreuves.
set -e
for d in /tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/essaim-devis-instruments-v1 /tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/essaim-devis-instruments-v1/epreuves-oracle-v67-v1; do
  cd "$d"
  for f in *; do
    [ -f "$f" ] || continue
    case "$f" in *.sha256) continue;; esac
    sha256sum "$f" > "$f.sha256"
  done
done
