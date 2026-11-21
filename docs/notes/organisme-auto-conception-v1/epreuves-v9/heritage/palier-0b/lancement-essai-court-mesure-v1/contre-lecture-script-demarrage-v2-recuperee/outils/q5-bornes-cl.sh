#!/bin/bash
# CL, question 5 : bornes exactes de la taille. Fabrique des scripts de demarrage gonfles pour que la lecture stricte
# (chaine JSON echappee en ASCII, jeton de 100 signes) vaille exactement 32 768 (attendu : accepte) et 32 769 ou 32 770
# (attendu : refuse, code 6), avec des remplissages d'especes differentes (espaces, tabulations, guillemets, barres inverses,
# signes < > &), puis compte la meme chaine par ma voie independante (taille-cl.py, 3 voies, et Go) : le fabricant et moi
# devons etre d'accord a l'octet. Jetons factices seulement ; depot distant factice ; aucun reseau.
# Emploi : q5-bornes-cl.sh CL
set -u
CL=$1
export TMPDIR=$CL/tmp
V2=$CL/aut/v2
FAB=$V2/fabriquer-donnees-demarrage-v2.sh
SCR=$V2/demarrage-machine-essai-3-v2.sh
JB=$CL/aut/essais/travail/jeton-factice.txt
PY=/home/user/controle-ia-travail/.venv/bin/python
W=$CL/mes-essais/q5
OUT=$W/table-q5.txt
[ ! -e "$W" ] || { echo "refus : $W existe"; exit 1; }
mkdir -p "$W/sorties" "$W/scripts"
export FABRICANT_BANC=oui FABRICANT_DEPOT_DISTANT=$CL/aut/essais/travail/distant/controle-ia-travail.git
: > "$OUT"
rep() { local n=$1 c=$2 i s=; for ((i = 0; i < n; i++)); do s+=$c; done; printf '%s' "$s"; }
# fabrique un script : ligne de remplissage "#" + N x CARACTERE, inseree apres la ligne 5
fab() {  # nom, nombre, caractere, attendu
  local nom=$1 n=$2 c=$3 att=$4 f=$W/scripts/$1.sh
  { sed -n 1,5p "$SCR"; printf '#%s\n' "$(rep "$n" "$c")"; sed -n '6,$p' "$SCR"; } > "$f"
  local r code strict gotxt
  r=$(FABRICANT_SCRIPT=$f bash "$V2/essais/outils/fabricant-avec-jeton.sh" "$JB" "$FAB" "$W/sorties/$nom" 2>&1)
  code=$(printf '%s\n' "$r" | sed -n 's/^code du fabricant : //p')
  strict=$(printf '%s\n' "$r" | grep -m1 -E 'lecture stricte|^refus' | cut -c1-200)
  echo "$nom ($n x « $c ») : attendu code $att ; rendu $code ; $([ "$code" = "$att" ] && echo TENU || echo ECHEC) ; $strict" >> "$OUT"
  if [ -f "$W/sorties/$nom.sans-jeton" ]; then
    echo "   ma mesure sur la sortie ecrite : $("$PY" -I "$CL/mes-outils/taille-cl.py" "$W/sorties/$nom" 100 | sed -n 2,4p | tr '\n' ' ')" >> "$OUT"
  fi
}
# remplissages : espaces (1 octet, 1 de JSON) ; tab / guillemet / barre inverse (1 octet, 2 de JSON)
fab bord-espaces-ok 286 ' ' 0
fab bord-espaces-plus1 287 ' ' 6
fab bord-tabs-ok 143 $'\t' 0
fab bord-tabs-plus1 144 $'\t' 6
fab bord-guillemets-ok 143 '"' 0
fab bord-guillemets-plus1 144 '"' 6
fab bord-barres-ok 143 '\' 0
fab bord-barres-plus1 144 '\' 6
# signes < > & : ne comptent pas dans la lecture stricte (6 octets seulement avec l'echappement HTML de Go)
fab bord-chevrons-ok 286 '<' 0
# signes de controle : retour chariot, DEL, caractere 0x01 : refus 6 attendu
fab ctrl-cr 1 $'\r' 6
fab ctrl-del 1 $'\177' 6
fab ctrl-001 1 $'\001' 6
fab ctrl-ff 1 $'\f' 6
cat "$OUT"
