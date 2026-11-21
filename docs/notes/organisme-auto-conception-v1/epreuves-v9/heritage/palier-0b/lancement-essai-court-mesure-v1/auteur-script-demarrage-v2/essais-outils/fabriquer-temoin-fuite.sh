#!/bin/bash
# Objet de contrôle des recherches du jeton : données de démarrage TÉMOINS, où le jeton fuit volontairement par trois
# canaux, juste avant la ligne « unset JETON » : une ligne du journal de démarrage, une URL écrite dans un fichier de
# configuration git, et la ligne de commande d'un processus (visible dans `ps` pendant 1,5 s) ; puis arrêt, code 99.
# Les recherches du banc doivent trouver les trois.
# Emploi : fabriquer-temoin-fuite.sh DONNEES_SAINES SORTIE
set -eu -o pipefail
SRC=$1; OUT=$2
[ ! -e "$OUT" ] || { echo "refus : $OUT existe" >&2; exit 1; }
umask 077
printf '%s\n' 'noter "témoin de fuite : $JETON"' \
  'git config --file $BASE/temoin-config remote.origin.url "http://x-access-token:$JETON@127.0.0.1/depot.git"' \
  "/bin/bash -c 'sleep 1.5; :' \"\$JETON\"" 'exit 99' > "$OUT.insertion"
# (première version : « bash -c 'sleep 1.5' » ; bash remplace alors son image par sleep, et le jeton quitte la ligne de
#  commande : le témoin ne fuyait pas par ps ; deux commandes gardent bash, et le jeton, dans la ligne de commande)
awk -v f="$OUT.insertion" '/^unset JETON$/ { while ((getline l < f) > 0) print l } { print }' "$SRC" > "$OUT"
rm -f "$OUT.insertion"
echo "témoin : $OUT ; lignes insérées : $(( $(wc -l < "$OUT") - $(wc -l < "$SRC") ))"
