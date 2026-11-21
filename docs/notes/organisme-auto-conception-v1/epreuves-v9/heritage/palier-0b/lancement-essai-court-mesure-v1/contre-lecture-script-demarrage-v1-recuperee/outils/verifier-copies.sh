#!/bin/bash
# Vérifie que chaque fichier copié de l'auteur est égal à son compagnon .sha256 (compagnons lus dans la copie), et égal à l'original.
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
ORIG=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-script-demarrage-v1
n=0; bad=0
for c in "$ME"/auteur/*.sha256 "$ME"/auteur/essais-outils/*.sha256; do
  d=$(dirname "$c")
  if (cd "$d" && sha256sum -c --quiet "$(basename "$c")" > /dev/null 2>&1); then n=$((n + 1)); else bad=$((bad + 1)); echo "compagnon KO : $c"; fi
done
for f in "$ME"/auteur/*.sh "$ME"/auteur/*.md "$ME"/auteur/essais-outils/*; do
  case "$f" in *.sha256) continue ;; esac
  r=${f#"$ME"/auteur/}
  cmp -s "$f" "$ORIG/$r" || { bad=$((bad + 1)); echo "copie differente de l'original : $r"; }
done
echo "compagnons verifies : $n ; ecarts : $bad"
