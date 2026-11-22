#!/bin/bash
# prépare : dépôt distant factice vide, jeton factice, données saines par le fabricant v8
set -u
W=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verification-controle-sortie-v2
FAB=/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-fabricant-v8-amorce-epinglee/fabriquer-donnees-demarrage-v8.sh
mkdir -p "$W/donnees" "$W/depot-factice.git"
/usr/bin/git init -q --bare "$W/depot-factice.git"
printf '%s\n' "FAUXJETONDEPOT0123456789abcdefXYZ" > "$W/donnees/jeton-depot.txt"
IFS= read -r JETON_FACTICE_ESSAI < "$W/donnees/jeton-depot.txt"
export JETON_FACTICE_ESSAI FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT="$W/depot-factice.git"
/bin/bash "$FAB" JETON_FACTICE_ESSAI "$W/donnees/sain.txt" > "$W/tables/fabricant.out" 2>&1
echo "code fabricant $?"
ls -la "$W/donnees"
