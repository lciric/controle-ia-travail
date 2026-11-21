#!/bin/bash
# Contre-lecteur : objets de contrôle VRAIS PAR CONSTRUCTION pour les trois canaux que le banc de l'auteur ne couvre pas :
#   MODE export   : le jeton est EXPORTÉ avant « unset JETON », puis un processus enfant vit 1,5 s (environnement du enfant) ;
#   MODE stdout   : le jeton est écrit sur la sortie standard du script (ce que cloud-init consigne) ;
#   MODE b64      : la forme base64 de « x-access-token:JETON » est écrite au journal de démarrage.
# Chaque insertion est suivie de « exit 99 ». Données de sortie en droits 600 (elles portent le jeton factice).
# Emploi : fabriquer-temoin-contre-lecteur.sh MODE DONNEES_SAINES SORTIE
set -eu -o pipefail
MODE=$1; SRC=$2; OUT=$3
[ ! -e "$OUT" ] || { echo "refus : $OUT existe" >&2; exit 1; }
umask 077
case "$MODE" in
  export) printf '%s\n' 'export JETON' '/bin/sleep 1.5' 'exit 99' > "$OUT.insertion" ;;
  stdout) printf '%s\n' 'echo "debug : $JETON"' 'exit 99' > "$OUT.insertion" ;;
  b64) printf '%s\n' "noter \"entete : \$(printf 'x-access-token:%s' \"\$JETON\" | base64 -w 0)\"" 'exit 99' > "$OUT.insertion" ;;
  *) echo "mode inconnu" >&2; exit 2 ;;
esac
awk -v f="$OUT.insertion" '/^unset JETON$/ && !fait { while ((getline l < f) > 0) print l; fait = 1 } { print }' "$SRC" > "$OUT"
rm -f "$OUT.insertion"
echo "témoin $MODE : $OUT ; lignes insérées : $(( $(wc -l < "$OUT") - $(wc -l < "$SRC") ))"
