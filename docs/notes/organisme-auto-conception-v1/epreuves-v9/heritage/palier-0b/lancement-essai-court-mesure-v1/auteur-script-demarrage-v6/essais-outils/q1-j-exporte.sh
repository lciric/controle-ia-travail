#!/bin/bash
# Banc v3, point 1 (cas q1-j du contre-lecteur, refait) : la session exporte déjà une variable J ; le fabricant est joué
# avec un espion git en tête du chemin. Objet vrai (doit fuir) : fabricant v2 ; objet à éprouver : fabricant v4 ;
# témoin : fabricant v4 sans J préalable. Compte les appels de git dont la variable J porte le jeton factice.
# Dépôt distant FACTICE seulement (FABRICANT_BANC=oui).
# Emploi : q1-j-exporte.sh DEPOT_FACTICE_SANS_BRANCHE
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$ICI"); V3=$(dirname "$ESS"); AUT=$(dirname "$V3")
W=$ESS/travail/q1-j
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W"
JB=$AUT/essais/travail/jeton-factice.txt
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$1 ESPION_JETON=$JB PATH="$ICI/espion:$PATH"
IFS= read -r JETON_FACTICE_ESSAI < "$JB"; export JETON_FACTICE_ESSAI
OUT=$W/resume.txt
: > "$OUT"
jouer() {  # nom, fabricant, attendu (fuite|aucune)
  export ESPION_JOURNAL=$W/espion-$1.txt
  : > "$ESPION_JOURNAL"
  /bin/bash "$2" JETON_FACTICE_ESSAI "$W/sortie-$1" > "$W/sortie-$1.txt" 2>&1
  local c=$? n f
  n=$(grep -c . "$ESPION_JOURNAL"); f=$(grep -c 'J_porte_le_jeton=1' "$ESPION_JOURNAL")
  local r=aucune; [ "$f" -gt 0 ] && r=fuite
  echo "$1 : code $c ; appels de git $n ; dont J porte le jeton : $f ; arguments : $(grep -c 'arguments_portent_le_jeton=1' "$ESPION_JOURNAL") ; attendu $3, rendu $r ; $([ "$3" = "$r" ] && echo TENU || echo ÉCHEC)" >> "$OUT"
}
unset J
jouer temoin-v6-sans-J "$V3/fabriquer-donnees-demarrage-v6.sh" aucune
export J=valeur-prealable-de-la-session
jouer objet-vrai-v2-J-exporte "$AUT/v2/fabriquer-donnees-demarrage-v2.sh" fuite
jouer v6-J-exporte "$V3/fabriquer-donnees-demarrage-v6.sh" aucune
echo "recherche du jeton dans les sorties autres que les données (attendu : aucune) :" >> "$OUT"
grep -l -F -f "$JB" "$W"/sortie-*.txt "$W"/*.sans-jeton "$W"/*.charge.b64 "$W"/*.empreintes.txt "$W"/espion-*.txt >> "$OUT" 2>/dev/null; echo "(fin)" >> "$OUT"
cat "$OUT"
