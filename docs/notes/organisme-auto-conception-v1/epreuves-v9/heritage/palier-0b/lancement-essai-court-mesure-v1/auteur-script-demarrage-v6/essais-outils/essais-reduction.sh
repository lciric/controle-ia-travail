#!/bin/bash
# Banc v6, point 1 (a) : la réduction du script et son épreuve, sur le vrai fabricant v6 (FABRICANT_BANC=oui, dépôt
# FACTICE, jeton factice). Écrit travail/reduction/table.txt.
#   G1 sain : réducteur réel sur le script v6 : 0 ;
#   G2 garde-fou : réducteur réel sur le script v6 suivi de constructions-protegees.txt (chaînes sur plusieurs lignes,
#      document en ligne, substitution, ligne continuée) : 0, et les 7 lignes d'allure de commentaire ou vides qui sont
#      à l'intérieur sont GARDÉES, le vrai commentaire final retiré ;
#   G3 garde-fou, refus : script suivi d'un guillemet jamais fermé : 9 ;
#   A1 artefact : une vraie ligne de code retirée (« set -u -o pipefail ») : 9 ;
#   A2 artefact : une ligne gardée modifiée : 9 ;
#   A3 artefact : ligne 1 retirée : 9 ;
#   T1 témoin : réducteur naïf (sed, sans garde-fou) sur le script de G2 : 9 (bash -n refuse, la substitution est cassée) ;
#   T2 témoin : réducteur naïf sur une chaîne seule : l'épreuve, qui ne voit que des retraits de
#      lignes d'allure de commentaire, l'accepte (0) ; les lignes des chaînes sont perdues : c'est le réducteur réel qui
#      les protège, non l'épreuve.
# Emploi : essais-reduction.sh DEPOT_FACTICE_SANS_BRANCHE
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$ICI"); V6=$(dirname "$ESS"); AUT=$(dirname "$V6")
FAB=$V6/fabriquer-donnees-demarrage-v6.sh SCR=$V6/demarrage-machine-essai-3-v6.sh
W=$ESS/travail/reduction
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/sorties"
JB=$AUT/essais/travail/jeton-factice.txt
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$1
# petit script de base (G2, G3, T1 : la taille du script v6 complet laisse trop peu de marge pour y ajouter les
# constructions) : la ligne 1, BRANCHE, DEPOT_URL et les quatre empreintes de pièces attendues par le fabricant, en code
{ sed -n 1p "$SCR"; grep -E '^(BRANCHE|DEPOT_URL)=' "$SCR"
  grep -E '^(PIECES=")?[0-9a-f]{64} [a-z0-9.-]+"?$' "$SCR" | sed -e 's/^PIECES="//' -e 's/"$//' -e 's/^/: /'; } > "$W/script-base.sh"
cat "$W/script-base.sh" "$ICI/constructions-protegees.txt" > "$W/script-constructions.sh"
{ cat "$W/script-base.sh"; echo 'Z="jamais ferme'; } > "$W/script-guillemet-ouvert.sh"
{ cat "$W/script-base.sh"; sed -n 1,4p "$ICI/constructions-protegees.txt"; } > "$W/script-chaine-seule.sh"
T=$W/table.txt
: > "$T"
cas() {  # nom, attendu, script, mode du réducteur (reel|naif|retire-code|modifie|ligne-1)
  local nom=$1 att=$2 s=$3 m=$4 r code o=$W/sorties/$1
  if [ $m = reel ]; then r=$(FABRICANT_SCRIPT=$s bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB" "$o" 2>&1)
  else r=$(FABRICANT_SCRIPT=$s FABRICANT_REDUCTEUR=$ICI/reducteur-artefact.sh REDUCTEUR_MODE=$m bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB" "$o" 2>&1); fi
  printf '%s\n' "$r" > "$W/sortie-$nom.txt"
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  echo "$nom : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ÉCHEC) ; $(printf '%s\n' "$r" | grep -m1 -E '^refus|^réduction' | cut -c1-260)" >> "$T"
  [ -f "$o.script-reduit.sh" ] && rm -f "$o" "$o.charge.b64"  # données de démarrage (jeton factice) retirées ; texte réduit gardé
}
cas G1-sain 0 "$SCR" reel
cas G2-garde-fou-chaines-et-document 0 "$W/script-constructions.sh" reel
cas G3-garde-fou-guillemet-ouvert 9 "$W/script-guillemet-ouvert.sh" reel
cas A1-artefact-ligne-de-code-retiree 9 "$SCR" retire-code
cas A2-artefact-ligne-modifiee 9 "$SCR" modifie
cas A3-artefact-ligne-1-retiree 9 "$SCR" ligne-1
cas T1-temoin-reducteur-naif 9 "$W/script-constructions.sh" naif
cas T2-temoin-naif-chaine-seule 0 "$W/script-chaine-seule.sh" naif
{
  echo "--- G2 : lignes d'allure de commentaire ou vides des constructions, présentes dans le texte réduit (attendu 7 sur 7) :"
  n=0
  for l in '# pas un commentaire : dans une chaine double' "# ligne d'un document en ligne" "# toujours dans la chaine simple'" \
    '# dans une substitution")' '# apres une ligne continuee'; do
    k=$(grep -c -x -F -e "$l" "$W/sorties/G2-garde-fou-chaines-et-document.script-reduit.sh"); n=$((n + k)); echo "  [$k] $l"
  done
  b=$(sed -n '/^MULTI="premiere ligne$/,/^FIN$/p' "$W/sorties/G2-garde-fou-chaines-et-document.script-reduit.sh" | grep -c -x '')
  echo "  [$b] lignes vides dans la chaîne double et le document en ligne (attendu 2)"
  echo "  total : $((n + b)) sur 7"
  echo "  vrai commentaire final retiré : $(grep -c -x -F '# vrai commentaire, retirable' "$W/sorties/G2-garde-fou-chaines-et-document.script-reduit.sh" | sed 's/^0$/oui/;s/^[1-9].*/NON/')"
  echo "--- T2 (témoin naïf, chaîne seule) : lignes de la chaîne présentes : $(grep -c -x -e '# pas un commentaire : dans une chaine double' -e '' "$W/sorties/T2-temoin-naif-chaine-seule.script-reduit.sh") sur 2 cherchées (la ligne d'allure de commentaire et la ligne vide ; attendu 0 : perdues, sans refus de l'épreuve)"
  echo "--- T2 : valeur de MULTI, script complet puis texte réduit (chaque ligne entre crochets) :"
  for f in "$W/script-chaine-seule.sh" "$W/sorties/T2-temoin-naif-chaine-seule.script-reduit.sh"; do
    echo "  [$(sed -n '/^MULTI="premiere ligne$/,/^fin"$/p' "$f" | tr '\n' '|')]"
  done
  echo "--- G1 : diff du script complet et du texte réduit : $(diff "$SCR" "$W/sorties/G1-sain.script-reduit.sh" | grep -c '^<') lignes retirées, $(diff "$SCR" "$W/sorties/G1-sain.script-reduit.sh" | grep -c '^>') ajoutées"
  echo "--- sorties laissées par les refus (attendu : aucune) :"; ls "$W/sorties" | grep -E '^(G3|A[0-9])'; echo "(fin de liste)"
} >> "$T"
cat "$T"
