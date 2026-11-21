#!/bin/bash
# Contre-lecteur, question 5 : la taille des données de démarrage, et le refus du fabricant au-delà de 32 768 octets.
# Le fabricant (copie de l'auteur, FABRICANT_SCRIPT pour un script rembourré) est joué avec des jetons factices de 44, 20 et 400
# signes. Le rembourrage est une ligne de commentaire ajoutée À LA FIN du script (après « exit 0 »), de taille exacte.
# Prédictions écrites avant (taille = 32 112 - 44 + L + R, L signes du jeton, R octets de rembourrage) :
#   S1 L=44 R=656 -> 32 768 : accepté ; S2 L=44 R=657 -> 32 769 : refus 6 ; S3 L=44, rembourrage de 657 octets fait de « é »
#   (moins de signes que d'octets) -> 32 769 octets : refus 6 ; S4 L=400 sans rembourrage -> 32 468 : accepté ;
#   S5 L=400 R=300 -> 32 768 : accepté ; S6 L=400 R=301 -> refus 6 ; S7 L=400 R=656 -> 33 124 : refus 6 ;
#   S8 L=20 sans rembourrage -> 32 088 : accepté. Après chaque refus : aucun fichier de sortie, aucun jeton écrit.
set -u
ME=/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/contre-lecteur-script-demarrage
AUT=$ME/auteur
W=$ME/resultats/q5
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/sorties" "$W/scripts" "$W/jetons"
alea() { head -c 600 /dev/urandom | base64 -w 0 | tr -dc 'A-Za-z0-9' | cut -c1-"$1"; }
umask 077
for L in 20 44 400; do printf '%s\n' "$(alea "$L")" > "$W/jetons/jeton-$L.txt"; done
umask 022
SCR=$AUT/demarrage-machine-essai-3-v1.sh
rembourrer() {  # SORTIE OCTETS [multi] : ajoute une ligne de commentaire d'exactement OCTETS octets (nouvelle ligne comprise)
  local out=$1 n=$2 multi=${3:-}
  cp "$SCR" "$out"
  if [ "$multi" = multi ]; then
    { printf '# '; yes é | head -n $(( (n - 3) / 2 )) | tr -d '\n'; printf '\n'; } >> "$out"
  else
    { printf '#'; head -c $((n - 2)) /dev/zero | tr '\0' x; printf '\n'; } >> "$out"
  fi
}
cas() {  # nom, attendu, fichier du jeton, script (ou -), sortie
  local nom=$1 att=$2 jet=$3 scr=$4
  local sortie=$W/sorties/$nom r code taille=absente
  if [ "$scr" = - ]; then unset FABRICANT_SCRIPT; else export FABRICANT_SCRIPT=$scr; fi
  r=$(bash "$AUT/essais-outils/fabricant-avec-jeton.sh" "$jet" "$AUT/fabriquer-donnees-demarrage-v1.sh" "$sortie" 2>&1)
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  [ -f "$sortie" ] && taille=$(wc -c < "$sortie")
  local restes jetons
  restes=$(ls "$W/sorties" | grep -c "^$nom")
  jetons=$(grep -l -F -f "$jet" "$W/sorties/$nom"* 2> /dev/null | grep -v -c -x "$sortie")
  echo "$nom : attendu $att ; rendu $code ; taille de la sortie $taille ; fichiers laissés $restes ; fichiers sans-jeton/charge/empreintes portant le jeton $jetons ; $([ "$att" = "$code" ] && echo TENU || echo ÉCART) ; $(printf '%s\n' "$r" | grep -m1 '^refus' | cut -c1-90)"
}
rembourrer "$W/scripts/r656.sh" 656
rembourrer "$W/scripts/r657.sh" 657
rembourrer "$W/scripts/r657-multi.sh" 657 multi
rembourrer "$W/scripts/r300.sh" 300
rembourrer "$W/scripts/r301.sh" 301
echo "octets du rembourrage multi-octets : $(tail -n 1 "$W/scripts/r657-multi.sh" | wc -c) ; signes : $(tail -n 1 "$W/scripts/r657-multi.sh" | wc -m)"
cas S1-L44-R656 0 "$W/jetons/jeton-44.txt" "$W/scripts/r656.sh"
cas S2-L44-R657 6 "$W/jetons/jeton-44.txt" "$W/scripts/r657.sh"
cas S3-L44-R657-multi 6 "$W/jetons/jeton-44.txt" "$W/scripts/r657-multi.sh"
cas S4-L400-sans 0 "$W/jetons/jeton-400.txt" -
cas S5-L400-R300 0 "$W/jetons/jeton-400.txt" "$W/scripts/r300.sh"
cas S6-L400-R301 6 "$W/jetons/jeton-400.txt" "$W/scripts/r301.sh"
cas S7-L400-R656 6 "$W/jetons/jeton-400.txt" "$W/scripts/r656.sh"
cas S8-L20-sans 0 "$W/jetons/jeton-20.txt" -
echo "fichiers présents dans sorties/ : $(ls "$W/sorties" | wc -l) ; refus 6 attendus sans aucun fichier : S2, S3, S6, S7"
