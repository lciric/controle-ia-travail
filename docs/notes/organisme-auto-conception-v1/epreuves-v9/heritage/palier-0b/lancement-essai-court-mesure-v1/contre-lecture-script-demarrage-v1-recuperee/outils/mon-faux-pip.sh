#!/bin/bash
# Contre-lecteur : faux pip. « install » : journalise ses arguments ; si MON_PIP_GIT=1, il fabrique à la racine (dossier du
# fichier de dépendances, dernier argument) un VRAI dépôt .git dont la tête est le commit attendu et dont l'index égale la
# copie (donc « git status --untracked-files=no » propre), puis y pose un fichier intrus NON SUIVI. C'est l'artefact « .git
# apparu après le pas (c) » : il simule ce qu'un paquet installé par le pas (d) pourrait faire à la racine.
echo "faux pip : $*" >> "${FAUX_JOURNAL:-/dev/null}"
if [ "${1:-}" = install ] && [ "${MON_PIP_GIT:-}" = 1 ]; then
  R=$(dirname "${!#}")
  D=$(dirname "$R")/depot.git
  C=d7f949acd9ac92e998e57663d2cc741de93f18c3
  export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
  git init -q "$R" && git -C "$R" fetch -q --depth 1 "$D" "$C" && git -C "$R" update-ref HEAD "$C" && git -C "$R" reset -q \
    || { echo "faux pip : fabrication du .git échouée" >&2; exit 1; }
  mkdir -p "$R/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src"
  echo "# intrus posé par l'artefact du contre-lecteur" > "$R/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v6/src/intrus-contre-lecteur.py"
  echo "faux pip : .git fabriqué à la racine, tête $(git -C "$R" rev-parse HEAD), intrus posé" >> "${FAUX_JOURNAL:-/dev/null}"
fi
exit 0
