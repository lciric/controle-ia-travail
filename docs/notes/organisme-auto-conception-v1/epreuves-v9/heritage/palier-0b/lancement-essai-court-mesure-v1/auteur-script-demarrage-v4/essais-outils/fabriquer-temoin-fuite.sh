#!/bin/bash
# v3 : objet de contrôle des recherches du jeton : données TÉMOINS où le jeton fuit volontairement par trois canaux
# (journal de démarrage, URL dans un fichier de configuration git, ligne de commande d'un processus visible 1,5 s), insérés
# dans l'amorce juste avant la ligne « CHARGE=… » ; puis arrêt, code 99. Les recherches du banc doivent trouver les trois.
# (« bash -c » à deux commandes : à une seule, bash remplace son image et le jeton quitte la ligne de commande.)
# Emploi : fabriquer-temoin-fuite.sh DONNEES_SAINES SORTIE
set -eu -o pipefail
SRC=$1; OUT=$2
[ ! -e "$OUT" ] || { echo "refus : $OUT existe" >&2; exit 1; }
umask 077
printf '%s\n' 'mkdir -p $ESSAI_DEMARRAGE_BASE && echo "temoin de fuite : $JETON_DEMARRAGE" >> $ESSAI_DEMARRAGE_BASE/journal-demarrage-essai-3.txt' \
  'git config --file $ESSAI_DEMARRAGE_BASE/temoin-config remote.origin.url "http://x-access-token:$JETON_DEMARRAGE@127.0.0.1/d.git"' \
  "/bin/bash -c 'sleep 1.5; :' \"\$JETON_DEMARRAGE\"" 'exit 99' > "$OUT.insertion"
awk -v f="$OUT.insertion" '/^CHARGE=/ { while ((getline l < f) > 0) print l } { print }' "$SRC" > "$OUT"
rm -f "$OUT.insertion"
echo "témoin : $OUT ; lignes insérées : $(( $(wc -l < "$OUT") - $(wc -l < "$SRC") ))"
