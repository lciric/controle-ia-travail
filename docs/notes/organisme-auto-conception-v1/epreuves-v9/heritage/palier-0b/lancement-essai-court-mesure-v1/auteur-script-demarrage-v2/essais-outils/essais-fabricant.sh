#!/bin/bash
# v2 : essais du fabricant v2 (jetons factices seulement ; dépôts distants FACTICES seulement : FABRICANT_BANC=oui et
# FABRICANT_DEPOT_DISTANT sont posés pour tous les cas, sauf F18 qui doit refuser avant toute lecture du distant),
# avec guetteur de `ps` et recherche du jeton factice dans toutes les sorties. Écrit travail/fabricant-essais/table.txt.
# Emploi : essais-fabricant.sh DEPOT_FACTICE_SANS_BRANCHE DEPOT_FACTICE_AVEC_BRANCHE
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$ICI")
V2=$(dirname "$ESS")
AUT=$(dirname "$V2")
FAB=$V2/fabriquer-donnees-demarrage-v2.sh
SCR=$V2/demarrage-machine-essai-3-v2.sh
W=$ESS/travail/fabricant-essais
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/sorties" "$W/depot-git-factice"
git init -q "$W/depot-git-factice"
JB=$AUT/essais/travail/jeton-factice.txt
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$1
AVEC=$2
umask 077
printf 'factice avec des espaces qui ne passe pas\n' > "$W/jeton-espaces.txt"
printf 'factice_court\n' > "$W/jeton-court.txt"
printf 'factice_%092d\n' 0 > "$W/jeton-100.txt"
printf 'factice_%093d\n' 0 > "$W/jeton-101.txt"
umask 022
sed '2s/.*/# autre ligne 2/' "$SCR" > "$W/script-ligne-2-autre.sh"
sed '5a ESSAI_DEMARRAGE_BASE=/tmp/ailleurs' "$SCR" > "$W/script-porte-d-essai.sh"
sed '5a # git push --no-verify' "$SCR" > "$W/script-no-verify.sh"
sed '5a # ligne accentuée : é' "$SCR" > "$W/script-non-ascii.sh"
cp "$SCR" "$W/script-trop-grand.sh"
for i in $(seq 1 4); do printf '# remplissage %080d\n' 0 >> "$W/script-trop-grand.sh"; done
E=$(sha256sum < "$SCR" | cut -c1-64)
T=$W/table.txt
: > "$T"
bash "$ICI/guetteur-ps.sh" "$JB" "$W/ps-jeton.txt" "$W/guetteur-arret" &
PG=$!
cas() {  # nom, code attendu, source du jeton, sortie, [arguments en plus]
  local nom=$1 att=$2 src=$3 out=$4; shift 4
  local r code
  r=$(bash "$ICI/fabricant-avec-jeton.sh" "$src" "$FAB" "$out" "$@" 2>&1)
  printf '%s\n' "$r" > "$W/sortie-$nom.txt"
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  echo "$nom : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ÉCHEC) ; $(printf '%s\n' "$r" | grep -m1 -E '^refus|lecture stricte' | cut -c1-120)" >> "$T"
}
cas F01-variable-vide 3 --vide "$W/sorties/f01"
cas F02-variable-absente 3 --absente "$W/sorties/f02"
cas F03-jeton-a-espaces 3 "$W/jeton-espaces.txt" "$W/sorties/f03"
cas F04-jeton-court 3 "$W/jeton-court.txt" "$W/sorties/f04"
cas F04b-jeton-101-signes 3 "$W/jeton-101.txt" "$W/sorties/f04b"
: > "$W/sorties/f05"
cas F05-sortie-existante 4 "$JB" "$W/sorties/f05"
cas F06-sortie-relative 4 "$JB" sorties/f06
cas F07-sortie-dans-un-depot 4 "$JB" "$W/depot-git-factice/f07"
cas F08-empreinte-du-script-fausse 5 "$JB" "$W/sorties/f08" 0000000000000000000000000000000000000000000000000000000000000000
FABRICANT_SCRIPT=$W/script-ligne-2-autre.sh cas F09-ligne-2-autre 5 "$JB" "$W/sorties/f09"
FABRICANT_SCRIPT=$W/script-trop-grand.sh cas F10-trop-grand 6 "$JB" "$W/sorties/f10"
FABRICANT_SCRIPT=$W/script-porte-d-essai.sh cas F13-porte-d-essai-dans-le-script 5 "$JB" "$W/sorties/f13"
FABRICANT_SCRIPT=$W/script-no-verify.sh cas F14-no-verify-dans-le-script 5 "$JB" "$W/sorties/f14"
FABRICANT_SCRIPT=$W/script-non-ascii.sh cas F15-signe-non-ascii 6 "$JB" "$W/sorties/f15"
FABRICANT_DEPOT_DISTANT=$AVEC cas F16-branche-deja-presente 8 "$JB" "$W/sorties/f16"
FABRICANT_DEPOT_DISTANT=$W/depot-introuvable.git cas F17-depot-injoignable 8 "$JB" "$W/sorties/f17"
env -u FABRICANT_BANC FABRICANT_SCRIPT="$SCR" bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB" "$W/sorties/f18" > "$W/sortie-F18.txt" 2>&1
c18=$(sed -n 's/^code du fabricant : //p' "$W/sortie-F18.txt")
echo "F18-reglage-d-essai-sans-banc : attendu 2 ; rendu $c18 ; $([ "$c18" = 2 ] && echo TENU || echo ÉCHEC) ; $(grep -m1 '^refus' "$W/sortie-F18.txt")" >> "$T"
cas F11-sain-empreinte-juste 0 "$JB" "$W/sorties/f11" "$E"
cas F12-sain-sans-empreinte 0 "$JB" "$W/sorties/f12"
cas F20-sain-jeton-100-signes 0 "$W/jeton-100.txt" "$W/sorties/f20"
: > "$W/guetteur-arret"
wait "$PG"
{
  echo "--- contrôles des sorties saines (F11, F12, F20) :"
  for f in f11 f12 f20; do
    O=$W/sorties/$f
    JJ=$JB; [ $f = f20 ] && JJ=$W/jeton-100.txt
    echo "$f : droits $(stat -c %a "$O") ; lignes portant le jeton : $(grep -c -F -f "$JJ" "$O") (la ligne 3 : $(sed -n 3p "$O" | grep -c -F -f "$JJ")) ; taille $(wc -c < "$O")"
    echo "$f : sans jeton = données, jeton masqué : $([ "$(sed "3s/.*/JETON_DEMARRAGE='@JETON@'/" "$O" | sha256sum)" = "$(sha256sum < "$O.sans-jeton")" ] && echo oui || echo NON)"
    echo "$f : $(grep -E 'lecture stricte|information' "$O.empreintes.txt" | tr '\n' ' ')"
  done
  echo "--- fichiers produits portant le jeton factice (hors sorties saines f11, f12, f20 et jetons d'essai) :"
  grep -r -l -F -f "$JB" "$W" | grep -v -x -F -e "$W/sorties/f11" -e "$W/sorties/f12" -e "$W/ps-jeton.txt"; echo "(fin de liste)"
  echo "--- sorties laissées par les refus (attendu : aucune ; f05 est le fichier vide posé par l'essai) :"
  ls "$W/sorties" | grep -v -E '^f(11|12|20)' | grep -v -x f05; echo "(fin de liste)"
  echo "--- ps : $(tail -n 1 "$W/ps-jeton.txt")"
} >> "$T"
cat "$T"
