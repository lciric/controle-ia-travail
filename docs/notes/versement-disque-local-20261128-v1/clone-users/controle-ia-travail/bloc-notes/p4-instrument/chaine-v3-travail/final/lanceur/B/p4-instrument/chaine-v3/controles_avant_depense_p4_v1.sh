#!/usr/bin/env bash
mkdir -p "$2" "$2.travail" && echo donnees > "$2/x"
echo "arguments : S=${1:0:12} ; $# arguments"
[ $# = 2 ] || { echo "KO  essai : nombre d'arguments"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; }
if [ -n "${FAUX_KO:-}" ]; then echo "OK  essai"; echo "KO  essai : faute simulée"; echo "CONTRÔLES AVANT DÉPENSE : ÉCHEC"; exit 1; fi
if [ -n "${FAUX_DERNIERE:-}" ]; then echo "OK  essai"; echo "dernière ligne inattendue (essai)"; exit 0; fi
echo "OK  essai"; echo "CONTRÔLES AVANT DÉPENSE : TOUS CONFORMES"
