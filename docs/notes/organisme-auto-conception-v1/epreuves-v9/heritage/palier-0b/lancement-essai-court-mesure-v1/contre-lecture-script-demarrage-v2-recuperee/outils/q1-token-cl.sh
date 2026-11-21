#!/bin/bash
# CL, question 1 : formes de jeton que le fabricant doit refuser (code 3) et celles qu'il doit admettre (code 0), selon la
# locale. Un signe non ASCII dans le jeton echapperait au controle de taille (le jeton n'est pas dans le texte sans jeton).
# Emploi : q1-token-cl.sh CL
set -u
CL=$1
export TMPDIR=$CL/tmp
W=$CL/mes-essais/q1-token
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/sorties" "$W/jetons"
FAB=$CL/aut/v2/fabriquer-donnees-demarrage-v2.sh
OUT=$W/table.txt
: > "$OUT"
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$CL/aut/essais/travail/distant/controle-ia-travail.git
A25=AAAAAAAAAAAAAAAAAAAAAAAAA
umask 077
printf 'é%.0s' $(seq 1 25) > "$W/jetons/e-aigu-25.txt"; echo >> "$W/jetons/e-aigu-25.txt"
printf '%s\xc3\xa9\n' "$A25" > "$W/jetons/ascii-plus-e-aigu.txt"
printf '%s\xef\xbc\xa1\n' "$A25" > "$W/jetons/pleine-chasse-A.txt"
printf '%s\xc2\xaa\n' "$A25" > "$W/jetons/ordinal-feminin.txt"
printf '%s\xe2\x80\x8b\n' "$A25" > "$W/jetons/espace-largeur-nulle.txt"
printf '%s\n' "$A25" > "$W/jetons/sain-25.txt"
printf '%s\n' "$A25-_-A_ab-CD" > "$W/jetons/sain-tirets.txt"
printf "%s'\n" "$A25" > "$W/jetons/apostrophe.txt"
printf '%s$(id)\n' "$A25" > "$W/jetons/substitution.txt"
printf '%s;x\n' "$A25" > "$W/jetons/point-virgule.txt"
umask 022
cas() {  # nom, locale, attendu
  local nom=$1 loc=$2 att=$3 r code
  r=$(env LC_ALL=$loc bash "$CL/aut/v2/essais/outils/fabricant-avec-jeton.sh" "$W/jetons/$nom.txt" "$FAB" "$W/sorties/$nom-$loc" 2>&1)
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  echo "$nom [$loc] : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ECHEC) ; $(printf '%s\n' "$r" | grep -m1 '^refus' | cut -c1-120)" >> "$OUT"
}
for loc in C C.utf8; do
  cas e-aigu-25 $loc 3
  cas ascii-plus-e-aigu $loc 3
  cas pleine-chasse-A $loc 3
  cas ordinal-feminin $loc 3
  cas espace-largeur-nulle $loc 3
  cas apostrophe $loc 3
  cas substitution $loc 3
  cas point-virgule $loc 3
  cas sain-25 $loc 0
  cas sain-tirets $loc 0
done
cat "$OUT"
