#!/bin/bash
# Assemble, pour la mesure seulement, le texte sans jeton d'un script donné et d'une charge donnée, comme le fabricant
# (ligne 1 ; H0_PREVU ; JETON_DEMARRAGE='@JETON@' ; lignes 3 et suivantes ; repère ; charge). Aucun jeton n'y entre.
# Emploi : assembler-sans-jeton.sh SCRIPT CHARGE_B64 SORTIE
set -eu -o pipefail
[ ! -e "$3" ] || { echo "refus : $3 existe" >&2; exit 1; }
{ sed -n 1p "$1"; echo "H0_PREVU=$(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "JETON_DEMARRAGE='@JETON@'"; sed -n '3,$p' "$1"
  echo __CHARGE_DES_PIECES__; cat "$2"; } > "$3"
echo "$3 : $(wc -c < "$3") octets"
