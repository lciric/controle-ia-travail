#!/bin/bash
# Écrit le compagnon .sha256 (« empreinte  nom ») de mes outils et de mes résultats texte, sans rien écraser.
# Les jeux de données portant un jeton factice (resultats/temoins, resultats/q5*, auteur/travail) n'en reçoivent pas ici.
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
n=0
for f in "$ME"/outils/*.sh "$ME"/outils/*.py "$ME"/resultats/*.txt; do
  [ -f "$f" ] || continue
  [ -e "$f.sha256" ] && continue
  (cd "$(dirname "$f")" && sha256sum "$(basename "$f")" > "$(basename "$f").sha256") && n=$((n + 1))
done
echo "compagnons écrits : $n"
