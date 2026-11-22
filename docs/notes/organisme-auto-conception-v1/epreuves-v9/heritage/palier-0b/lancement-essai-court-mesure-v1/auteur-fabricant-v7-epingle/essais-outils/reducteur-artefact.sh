#!/bin/bash
# Banc v6 : réducteurs ARTEFACTS (FABRICANT_REDUCTEUR, banc seulement), selon REDUCTEUR_MODE :
#   naif        : retire, par sed, toute ligne dont le premier signe non blanc est « # » (sauf la ligne 1) et toute ligne
#                 vide, SANS garde-fou (témoin : retire aussi les lignes d'allure de commentaire dans une chaîne) ;
#   retire-code : naif, plus le retrait d'une vraie ligne de code (« set -u -o pipefail ») ;
#   modifie     : naif, plus le changement d'une ligne gardée (INTERVALLE=1800 devient 1801) ;
#   ligne-1     : naif, plus le retrait de la ligne 1 (#!/bin/bash).
# Emploi : REDUCTEUR_MODE=… reducteur-artefact.sh ENTREE SORTIE
set -u
[ ! -e "$2" ] || { echo "refus : $2 présent"; exit 2; }
naif=(-e '1!{/^[[:space:]]*#/d}' -e '/^[[:space:]]*$/d')
case "${REDUCTEUR_MODE:-}" in
  naif) sed "${naif[@]}" "$1" > "$2" ;;
  retire-code) sed "${naif[@]}" -e '/^set -u -o pipefail$/d' "$1" > "$2" ;;
  modifie) sed "${naif[@]}" -e 's/INTERVALLE=1800/INTERVALLE=1801/' "$1" > "$2" ;;
  ligne-1) sed "${naif[@]}" -e '1d' "$1" > "$2" ;;
  garde-ligne-2) sed -e '1,2!{/^[[:space:]]*#/d}' -e '/^[[:space:]]*$/d' "$1" > "$2" ;;  # v7 : garde un commentaire (épreuve muette)
  *) echo "mode inconnu"; exit 2 ;;
esac
echo "réducteur artefact $REDUCTEUR_MODE : $(wc -l < "$1") lignes, $(wc -l < "$2") gardées"
