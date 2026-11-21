#!/bin/bash
# CL, question 1 : le fabricant range le jeton dans la variable J. Si l'environnement de la session porte DEJA une variable
# J exportee, l'affectation J=... la laisse exportee : tous les processus que le fabricant lance ensuite (git ls-remote,
# sed, tar, xz...) heritent du jeton dans leur environnement. Mesure par un espion git (processus factice) : nombre de
# lignes de SON environnement qui portent le jeton factice. Temoin : meme fabrication sans J prealable (attendu 0).
# Emploi : q1-j-exporte.sh CL
set -u
CL=$1
export TMPDIR=$CL/tmp
W=$CL/mes-essais/q1-j
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W"
FAB=$CL/aut/v2/fabriquer-donnees-demarrage-v2.sh
JB=$CL/aut/essais/travail/jeton-factice.txt
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$CL/aut/essais/travail/distant/controle-ia-travail.git
export ESPION_JETON=$JB
export PATH="$CL/mes-outils/espion-bin:$PATH"
IFS= read -r JETON_FACTICE_ESSAI < "$JB"; export JETON_FACTICE_ESSAI
# temoin : J absent de l'environnement
unset J
export ESPION_JOURNAL=$W/espion-temoin.txt
/bin/bash "$FAB" JETON_FACTICE_ESSAI "$W/sortie-temoin" > "$W/stdout-temoin.txt" 2>&1
echo "temoin (J absent) : code $?" > "$W/resume.txt"
grep -c . "$W/espion-temoin.txt" | sed 's/^/appels de git espionnes (temoin) : /' >> "$W/resume.txt"
echo "temoin : appels de git dont l'environnement porte le jeton : $(grep -c 'environ_avec_jeton=[1-9]' "$W/espion-temoin.txt")" >> "$W/resume.txt"
# objet : J exporte par la session avec une valeur quelconque
export J=valeur-prealable-de-la-session
export ESPION_JOURNAL=$W/espion-j-exporte.txt
/bin/bash "$FAB" JETON_FACTICE_ESSAI "$W/sortie-j-exporte" > "$W/stdout-j-exporte.txt" 2>&1
echo "J exporte : code $?" >> "$W/resume.txt"
echo "J exporte : appels de git espionnes : $(grep -c . "$W/espion-j-exporte.txt")" >> "$W/resume.txt"
echo "J exporte : appels de git dont l'environnement porte le jeton : $(grep -c 'environ_avec_jeton=[1-9]' "$W/espion-j-exporte.txt")" >> "$W/resume.txt"
echo "J exporte : appels de git dont les arguments portent le jeton : $(grep -c 'argv_avec_jeton=[1-9]' "$W/espion-j-exporte.txt")" >> "$W/resume.txt"
cat "$W/resume.txt"
