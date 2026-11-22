#!/bin/bash
# Écrit un compagnon .sha256 (format sha256sum, nom de base) pour chaque fichier du dossier v2 et de son sous-dossier d'épreuves.
set -e
for d in /tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/essaim-devis-instruments-v2 /tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/essaim-devis-instruments-v2/epreuves-oracle-v67-v2; do
  cd "$d"
  for f in *; do
    [ -f "$f" ] || continue
    case "$f" in *.sha256) continue;; esac
    sha256sum "$f" > "$f.sha256"
  done
done
