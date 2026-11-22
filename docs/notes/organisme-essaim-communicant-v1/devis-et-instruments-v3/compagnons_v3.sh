#!/bin/bash
# Écrit un compagnon .sha256 (format sha256sum, nom de base) pour chaque fichier de ce dossier (le dossier de ce script).
set -e
cd "$(dirname "$0")"
for f in *; do
  [ -f "$f" ] || continue
  case "$f" in *.sha256) continue;; esac
  sha256sum "$f" > "$f.sha256"
done
