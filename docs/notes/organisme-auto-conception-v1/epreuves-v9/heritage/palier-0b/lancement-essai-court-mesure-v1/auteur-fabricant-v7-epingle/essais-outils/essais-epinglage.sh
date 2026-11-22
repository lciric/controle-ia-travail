#!/bin/bash
# Banc v7 : épreuve du fabricant v7 épinglé (FABRICANT_BANC=oui, dépôt FACTICE, jeton factice). Écrit travail/epinglage/table.txt.
#   E0 sain : v6 et v7 joués ensemble (même jeton factice, même seconde : même H0, retenté jusqu'à 5 fois) ; données,
#      texte sans jeton, charge et texte réduit comparés par empreinte, octet pour octet ;
#   E1 A2 du contre-lecteur : script réel + chaîne sur plusieurs lignes, réducteur naïf : 9 ;
#   E2 K1 du contre-lecteur : script réel + case dans $( ) dans une chaîne, réducteur réel : 9 ;
#   E3 T2 de l'auteur (v6) : petit script + chaîne seule, réducteur naïf : 9 ;
#   E4 script complet modifié d'un octet (dans une ligne de commentaire : le texte réduit, lui, ne change pas) : 9 ;
#   E5 script réel, réducteur qui garde une ligne de commentaire (épreuve muette, script complet juste) : 9 par le texte réduit.
# Emploi : essais-epinglage.sh DEPOT_FACTICE_SANS_BRANCHE
set -u
ICI=$(cd "$(dirname "$0")" && pwd)
ESS=$(dirname "$ICI"); V7=$(dirname "$ESS"); AUT=$(dirname "$V7")
FAB7=$V7/fabriquer-donnees-demarrage-v7.sh FAB6=$AUT/v6/fabriquer-donnees-demarrage-v6.sh SCR=$V7/demarrage-machine-essai-3-v6.sh
W=$ESS/travail/epinglage
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/sorties" "$W/entrees"
JB=$AUT/essais/travail/jeton-factice.txt
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$1
T=$W/table.txt
: > "$T"
# entrées
cat "$SCR" "$ICI/queue-a2-chaine.txt" > "$W/entrees/a2.sh"
cat "$SCR" "$ICI/queue-k1-case.txt" > "$W/entrees/k1.sh"
{ sed -n 1p "$SCR"; grep -E '^(BRANCHE|DEPOT_URL)=' "$SCR"
  grep -E '^(PIECES=")?[0-9a-f]{64} [a-z0-9.-]+"?$' "$SCR" | sed -e 's/^PIECES="//' -e 's/"$//' -e 's/^/: /'
  sed -n 1,4p "$ICI/constructions-protegees.txt"; } > "$W/entrees/t2.sh"
sed '8s/groupe de controle exige/groupe de controle exigE/' "$SCR" > "$W/entrees/un-octet.sh"
echo "entrées : a2 $(sha256sum < "$W/entrees/a2.sh" | cut -c1-16)… ; k1 $(sha256sum < "$W/entrees/k1.sh" | cut -c1-16)… ; t2 $(sha256sum < "$W/entrees/t2.sh" | cut -c1-16)… ; un-octet : $(cmp -l "$SCR" "$W/entrees/un-octet.sh" | wc -l) octet différent du script réel, $(wc -c < "$W/entrees/un-octet.sh") octets contre $(wc -c < "$SCR")" >> "$T"
for f in a2 k1 t2 un-octet; do bash -n "$W/entrees/$f.sh" && echo "entrée $f : bash -n passe" >> "$T"; done
cas() {  # nom, attendu, script ou -, mode du réducteur (reel ou mode d'artefact)
  local nom=$1 att=$2 s=$3 m=$4 r code o=$W/sorties/$1 x=()
  [ "$s" = - ] || x+=(FABRICANT_SCRIPT=$s)
  [ $m = reel ] || x+=(FABRICANT_REDUCTEUR=$ICI/reducteur-artefact.sh REDUCTEUR_MODE=$m)
  r=$(env "${x[@]}" bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB7" "$o" 2>&1)
  printf '%s\n' "$r" > "$W/sortie-$nom.txt"
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  echo "$nom : attendu $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ÉCHEC) ; $(printf '%s\n' "$r" | grep -m1 -E '^refus' | cut -c1-200) ; fichiers laissés : $(ls "$W/sorties" | grep -c -F "$nom")" >> "$T"
}
cas E1-A2-chaine-reducteur-naif 9 "$W/entrees/a2.sh" naif
cas E2-K1-case-reducteur-reel 9 "$W/entrees/k1.sh" reel
cas E3-T2-chaine-seule-reducteur-naif 9 "$W/entrees/t2.sh" naif
cas E4-script-complet-un-octet 9 "$W/entrees/un-octet.sh" reel
cas E5-reducteur-garde-un-commentaire 9 - garde-ligne-2
# E0 : sain, v6 et v7 ensemble
for k in 1 2 3 4 5; do
  rm -rf "$W/e0"; mkdir -p "$W/e0"
  bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB6" "$W/e0/v6" > "$W/e0/sortie-v6.txt" 2>&1 &
  P6=$!
  bash "$ICI/fabricant-avec-jeton.sh" "$JB" "$FAB7" "$W/e0/v7" > "$W/e0/sortie-v7.txt" 2>&1
  wait $P6
  [ "$(sed -n 2p "$W/e0/v6")" = "$(sed -n 2p "$W/e0/v7")" ] && break
done
c6=$(sed -n 's/^code du fabricant : //p' "$W/e0/sortie-v6.txt"); c7=$(sed -n 's/^code du fabricant : //p' "$W/e0/sortie-v7.txt")
{
  echo "E0-sain : essai $k ; codes v6 $c6, v7 $c7 ; H0 v6 $(sed -n 2p "$W/e0/v6"), v7 $(sed -n 2p "$W/e0/v7")"
  for x in "" .sans-jeton .charge.b64 .script-reduit.sh; do
    a=$(sha256sum < "$W/e0/v6$x" | cut -c1-64); b=$(sha256sum < "$W/e0/v7$x" | cut -c1-64)
    echo "  données$x : v6 $a ; v7 $b ; $([ "$a" = "$b" ] && cmp -s "$W/e0/v6$x" "$W/e0/v7$x" && echo IDENTIQUES || echo DIFFÉRENTES)"
  done
  echo "  $(grep 'lecture stricte' "$W/e0/v7.empreintes.txt")"
  echo "  $(grep 'HTML de Go' "$W/e0/v7.empreintes.txt")"
  echo "E0 : $([ "$c6" = 0 ] && [ "$c7" = 0 ] && cmp -s "$W/e0/v6" "$W/e0/v7" && echo TENU || echo ÉCHEC)"
} >> "$T"
/home/user/controle-ia-travail/.venv/bin/python -I "$ICI/tailles-json.py" "$W/e0/v7" 100 > "$W/e0/tailles-json-v7.txt"
rm -f "$W/e0/v6" "$W/e0/v7"  # données portant le jeton factice ; empreintes gardées ci-dessus
cat "$T"
