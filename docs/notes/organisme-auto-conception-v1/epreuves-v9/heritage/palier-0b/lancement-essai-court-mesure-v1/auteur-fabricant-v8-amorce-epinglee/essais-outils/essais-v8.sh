#!/bin/bash
# Banc v8 : épreuve du fabricant v8 (amorce épinglée, une seule ligne E_SCRIPT=). FABRICANT_BANC=oui, dépôt FACTICE,
# jeton factice. Écrit travail/v8/table.txt.
#   E0 sain : v7 et v8 joués ensemble (même jeton factice, même seconde : même H0, retenté jusqu'à 5 fois) ; comparés par
#      empreinte et octet pour octet ;
#   B1 amorce modifiée d'un octet (dans un commentaire) : 9 ;
#   B2 amorce dont le contrôle d'empreinte (ligne « [ "$(printf '%s' "$TEXTE" | sha256sum … » ) est retiré : 9 ;
#   B3 amorce portant une seconde ligne E_SCRIPT=0…0 (cas B1 du vérificateur) : 9 (par l'épinglage de l'amorce) ;
#   D1 seconde ligne E_SCRIPT= dans les données : mutation du SEUL épinglage d'amorce (empreinte remplacée par celle de
#      l'amorce de B3, dans une copie du fabricant v8), pour atteindre le second contrôle : 9 (par le contrôle des données).
# Les cas B et D jouent une copie du dossier du fabricant (fabricant, script, réducteur) où seule l'amorce change ; la
# copie du fabricant est contrôlée identique au fabricant v8 (sauf D1, où la seule ligne changée est montrée).
# Emploi : essais-v8.sh DEPOT_FACTICE_SANS_BRANCHE
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$ICI"); V8=$(dirname "$ESS"); AUT=$(dirname "$V8")
FAB8=$V8/fabriquer-donnees-demarrage-v8.sh FAB7=$AUT/v7/fabriquer-donnees-demarrage-v7.sh AM=$V8/amorce-demarrage-essai-3-v6.sh
W=$ESS/travail/v8
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W"
JB=$AUT/essais/travail/jeton-factice.txt
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$1
T=$W/table.txt
: > "$T"
dossier() {  # $1 nom : copie du dossier du fabricant v8, amorce à poser ensuite
  mkdir -p "$W/$1/sorties"
  cp "$FAB8" "$V8/demarrage-machine-essai-3-v6.sh" "$V8/reduire-script-v6.py" "$W/$1/"
}
dossier B1; sed '3s/Amorce, essai 3/Amorce, essai 4/' "$AM" > "$W/B1/amorce-demarrage-essai-3-v6.sh"
dossier B2; grep -v -F '[ "$(printf '"'"'%s'"'"' "$TEXTE" | sha256sum' "$AM" > "$W/B2/amorce-demarrage-essai-3-v6.sh"
dossier B3; sed '3a E_SCRIPT=0000000000000000000000000000000000000000000000000000000000000000' "$AM" > "$W/B3/amorce-demarrage-essai-3-v6.sh"
dossier D1; cp "$W/B3/amorce-demarrage-essai-3-v6.sh" "$W/D1/"
EB3=$(sha256sum < "$W/B3/amorce-demarrage-essai-3-v6.sh" | cut -c1-64)
sed -i "s/^E_AMORCE_EPINGLE=524cfc4a78a2b77c3cb5ad0c915628217e932c7cd58dbfebc80c4643f5d9d751$/E_AMORCE_EPINGLE=$EB3/" "$W/D1/fabriquer-donnees-demarrage-v8.sh"
{
  echo "B1 : $(cmp -l "$AM" "$W/B1/amorce-demarrage-essai-3-v6.sh" | wc -l) octet différent de l'amorce v6"
  echo "B2 : lignes retirées de l'amorce : $(diff "$AM" "$W/B2/amorce-demarrage-essai-3-v6.sh" | grep -c '^<') ($(diff "$AM" "$W/B2/amorce-demarrage-essai-3-v6.sh" | grep '^<' | cut -c1-60)…)"
  echo "B3 : lignes E_SCRIPT= dans l'amorce : $(grep -c -F 'E_SCRIPT=' "$W/B3/amorce-demarrage-essai-3-v6.sh") (v6 : $(grep -c -F 'E_SCRIPT=' "$AM"))"
  for d in B1 B2 B3; do echo "$d : fabricant de la copie identique au v8 : $(cmp -s "$FAB8" "$W/$d/fabriquer-donnees-demarrage-v8.sh" && echo oui || echo NON)"; done
  echo "D1 : seule différence avec le fabricant v8 : $(diff "$FAB8" "$W/D1/fabriquer-donnees-demarrage-v8.sh" | grep -c '^[<>]') lignes ; $(diff "$FAB8" "$W/D1/fabriquer-donnees-demarrage-v8.sh" | grep '^>' | cut -c1-40)…"
} >> "$T"
cas() {  # nom, attendu, fabricant
  local nom=$1 att=$2 f=$3 r code o=$W/$1/sorties/donnees
  r=$(bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$f" "$o" 2>&1)
  printf '%s\n' "$r" > "$W/sortie-$nom.txt"
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  echo "$nom : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ÉCHEC) ; $(printf '%s\n' "$r" | grep -m1 -E '^refus' | cut -c1-170) ; fichiers laissés : $(ls "$W/$nom/sorties" | wc -l)" >> "$T"
}
cas B1 9 "$W/B1/fabriquer-donnees-demarrage-v8.sh"
cas B2 9 "$W/B2/fabriquer-donnees-demarrage-v8.sh"
cas B3 9 "$W/B3/fabriquer-donnees-demarrage-v8.sh"
cas D1 9 "$W/D1/fabriquer-donnees-demarrage-v8.sh"
for k in 1 2 3 4 5; do
  rm -rf "$W/e0"; mkdir -p "$W/e0"
  bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB7" "$W/e0/v7" > "$W/e0/sortie-v7.txt" 2>&1 &
  P7=$!
  bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB8" "$W/e0/v8" > "$W/e0/sortie-v8.txt" 2>&1
  wait $P7
  [ "$(sed -n 2p "$W/e0/v7")" = "$(sed -n 2p "$W/e0/v8")" ] && break
done
c7=$(sed -n 's/^code du fabricant : //p' "$W/e0/sortie-v7.txt"); c8=$(sed -n 's/^code du fabricant : //p' "$W/e0/sortie-v8.txt")
{
  echo "E0-sain : essai $k ; codes v7 $c7, v8 $c8 ; H0 v7 $(sed -n 2p "$W/e0/v7"), v8 $(sed -n 2p "$W/e0/v8")"
  for x in "" .sans-jeton .charge.b64 .script-reduit.sh; do
    a=$(sha256sum < "$W/e0/v7$x" | cut -c1-64); b=$(sha256sum < "$W/e0/v8$x" | cut -c1-64)
    echo "  données$x : v7 $a ; v8 $b ; $([ "$a" = "$b" ] && cmp -s "$W/e0/v7$x" "$W/e0/v8$x" && echo IDENTIQUES || echo DIFFÉRENTES)"
  done
  echo "  lignes E_SCRIPT= des données v8 : $(grep -c -F 'E_SCRIPT=' "$W/e0/v8") ; ligne 4 : $(sed -n 4p "$W/e0/v8")"
  echo "  $(grep 'lecture stricte' "$W/e0/v8.empreintes.txt")"
  echo "  $(grep 'HTML de Go' "$W/e0/v8.empreintes.txt")"
  echo "E0 : $([ "$c7" = 0 ] && [ "$c8" = 0 ] && cmp -s "$W/e0/v7" "$W/e0/v8" && echo TENU || echo ÉCHEC)"
} >> "$T"
/home/user/controle-ia-travail/.venv/bin/python -I "$ICI/tailles-json.py" "$W/e0/v8" 100 > "$W/e0/tailles-json-v8.txt"
rm -f "$W/e0/v7" "$W/e0/v8"  # données portant le jeton factice ; empreintes gardées ci-dessus
cat "$T"
