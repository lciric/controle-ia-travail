#!/bin/bash
# Essais du fabricant des données de démarrage (jetons factices seulement), avec guetteur de `ps` et recherche du jeton
# factice dans toutes les sorties. Écrit travail/fabricant-essais/table.txt et l'affiche.
# Emploi : essais-fabricant.sh
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$ICI")
AUT=$(dirname "$ESS")
FAB=$AUT/fabriquer-donnees-demarrage-v1.sh
SCR=$AUT/demarrage-machine-essai-3-v1.sh
W=$ESS/travail/fabricant-essais
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/sorties" "$W/depot-git-factice"
git init -q "$W/depot-git-factice"
JB=$ESS/travail/jeton-factice.txt
umask 077
printf 'factice avec des espaces qui ne passe pas\n' > "$W/jeton-espaces.txt"
printf 'factice_court\n' > "$W/jeton-court.txt"
umask 022
sed '2s/.*/# autre ligne 2/' "$SCR" > "$W/script-ligne-2-autre.sh"
cp "$SCR" "$W/script-trop-grand.sh"
for i in $(seq 1 12); do printf '# remplissage de l essai « trop grand » : %080d\n' 0 >> "$W/script-trop-grand.sh"; done
E=$(sha256sum < "$SCR" | cut -c1-64)
T=$W/table.txt
: > "$T"
bash "$ICI/guetteur-ps.sh" "$JB" "$W/ps-jeton.txt" "$W/guetteur-arret" &
PG=$!
cas() {  # nom, code attendu, source du jeton, sortie, [arguments en plus] (variables FABRICANT_* déjà posées)
  local nom=$1 att=$2 src=$3 out=$4; shift 4
  local r
  r=$(bash "$ICI/fabricant-avec-jeton.sh" "$src" "$FAB" "$out" "$@" 2>&1)
  printf '%s\n' "$r" > "$W/sortie-$nom.txt"
  local code
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  echo "$nom : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ÉCHEC) ; $(printf '%s\n' "$r" | grep -m1 '^refus' | cut -c1-110)" >> "$T"
}
cas F01-variable-vide 3 --vide "$W/sorties/f01"
cas F02-variable-absente 3 --absente "$W/sorties/f02"
cas F03-jeton-a-espaces 3 "$W/jeton-espaces.txt" "$W/sorties/f03"
cas F04-jeton-court 3 "$W/jeton-court.txt" "$W/sorties/f04"
: > "$W/sorties/f05"
cas F05-sortie-existante 4 "$JB" "$W/sorties/f05"
cas F06-sortie-relative 4 "$JB" sorties/f06
cas F07-sortie-dans-un-depot 4 "$JB" "$W/depot-git-factice/f07"
cas F08-empreinte-du-script-fausse 5 "$JB" "$W/sorties/f08" 0000000000000000000000000000000000000000000000000000000000000000
FABRICANT_SCRIPT=$W/script-ligne-2-autre.sh cas F09-ligne-2-autre 5 "$JB" "$W/sorties/f09"
export FABRICANT_SCRIPT=$W/script-trop-grand.sh
cas F10-trop-grand 6 "$JB" "$W/sorties/f10"
unset FABRICANT_SCRIPT
cas F11-sain-empreinte-juste 0 "$JB" "$W/sorties/f11" "$E"
cas F12-sain-sans-empreinte 0 "$JB" "$W/sorties/f12"
: > "$W/guetteur-arret"
wait "$PG"
{
  echo "--- contrôles des sorties saines (F11, F12) :"
  for f in f11 f12; do
    O=$W/sorties/$f
    echo "$f : droits $(stat -c %a "$O") ; lignes portant le jeton : $(grep -c -F -f "$JB" "$O") (attendu 1, la ligne 3 : $(sed -n 3p "$O" | grep -c -F -f "$JB")) ; taille $(wc -c < "$O")"
    echo "$f : sans jeton = données, jeton masqué : $([ "$(sed "3s/.*/JETON_DEMARRAGE='@JETON@'/" "$O" | sha256sum)" = "$(sha256sum < "$O.sans-jeton")" ] && echo oui || echo NON)"
    echo "$f : lignes 4 à la fin du script égales aux lignes 4 du texte sans jeton jusqu'au repère : $(cmp -s <(sed -n '3,$p' "$SCR") <(sed -n '4,/^__CHARGE_DES_PIECES__$/p' "$O.sans-jeton" | sed '$d') && echo oui || echo NON)"
    echo "$f : H0_PREVU : $(sed -n 2p "$O.sans-jeton")"
  done
  echo "--- fichiers produits portant le jeton factice (hors les deux sorties saines f11 et f12, et le jeton lui-même) :"
  grep -r -l -F -f "$JB" "$W" | grep -v -x -F -e "$W/sorties/f11" -e "$W/sorties/f12" -e "$W/ps-jeton.txt"; echo "(fin de liste)"
  echo "--- sorties partielles laissées par les refus (attendu : aucune) :"
  ls "$W/sorties" | grep -v -E '^f1[12]' | grep -v -x f05; echo "(fin de liste ; f05 est le fichier vide posé par l'essai)"
  echo "--- ps : $(tail -n 1 "$W/ps-jeton.txt")"
} >> "$T"
cat "$T"
