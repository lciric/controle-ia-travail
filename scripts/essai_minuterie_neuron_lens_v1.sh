#!/usr/bin/env bash
# Essai (R5) de la minuterie de destruction v1, sans location : outil du loueur remplacé par un faux outil qui consigne ses arguments.
# Cas sain (échéance → « destroy instance <ID> » appelé, code 0) ; arrêt par le PID écrit par la minuterie avant l'échéance → aucun
# appel ; lancement détaché (`setsid nohup … &`) : le PID du fichier est vivant, porte le script, et son arrêt empêche l'appel ; durée
# hors bornes (trop petite, trop grande, vide, non numérique) → code 3, rien d'armé ; outil relatif ou absent → 4 ; identifiant invalide
# → 2 ; fichier PID impossible → 5 ; outil qui refuse → 3 essais, code 6. Verdict automatique (écarts comptés dans un fichier).
# La survie au-delà de l'appel d'outil de la session est éprouvée à part (journal de la commande v9), pas ici.
# Usage : bash scripts/essai_minuterie_neuron_lens_v1.sh <dossier neuf>
set -uo pipefail
SRC=$(cd "$(dirname "$0")/.." && pwd); S=$1
[ -e "$S" ] && { echo "dossier existant"; exit 2; }
mkdir -p "$S"; E="$S/ecarts.txt"; : > "$E"
ecart() { echo "$*" >> "$E"; echo "  ÉCART : $*"; }
M="$SRC/scripts/minuterie_destruction_neuron_lens_v1.sh"
printf '#!/bin/sh\necho "$@" >> "%s/appels.txt"\nexit 0\n' "$S" > "$S/faux-outil"
printf '#!/bin/sh\necho "$@" >> "%s/appels-refus.txt"\nexit 1\n' "$S" > "$S/faux-refus"
chmod 755 "$S/faux-outil" "$S/faux-refus"
attendu() {  # nom code_obtenu code_attendu
  echo "CAS $1 : code=$2 (attendu $3)"; [ "$2" = "$3" ] || ecart "cas $1 : code $2 au lieu de $3"
}
echo "ESSAI minuterie v1 ; $(date -u +%FT%TZ)"
# 1. sain
BORNE_MIN_S=1 bash "$M" 123 2 "$S/faux-outil" "$S/pid-sain" > "$S/j-sain.txt" 2>&1; attendu sain $? 0
grep -qx "destroy instance 123" "$S/appels.txt" 2>/dev/null && echo "  appel : destroy instance 123" || ecart "sain : appel absent"
[ "$(cat "$S/pid-sain")" -gt 0 ] 2>/dev/null || ecart "sain : PID non écrit"
# 2. arrêt par PID, lancement détaché
: > "$S/appels.txt"
BORNE_MIN_S=1 setsid nohup bash "$M" 124 6 "$S/faux-outil" "$S/pid-det" > "$S/j-det.txt" 2>&1 < /dev/null &
sleep 1
P=$(cat "$S/pid-det" 2>/dev/null)
if [ -n "$P" ] && ps -p "$P" -o args= | grep -q minuterie_destruction; then echo "  détachée : PID $P vivant, porte la minuterie"; else ecart "détachée : PID $P absent ou autre processus"; fi
kill "$P"; sleep 7
ps -p "$P" > /dev/null && ecart "détachée : PID $P encore vivant après l'arrêt" || echo "  détachée : PID $P arrêté"
[ -s "$S/appels.txt" ] && ecart "détachée : outil appelé malgré l'arrêt" || echo "  détachée : aucun appel de l'outil après l'arrêt (échéance passée)"
# 3. bornes
for d in 5 200000 "" abc; do bash "$M" 125 "$d" "$S/faux-outil" "$S/pid-b" > "$S/j-b.txt" 2>&1; attendu "bornes '$d'" $? 3; done
[ -e "$S/pid-b" ] && ecart "bornes : PID écrit alors que rien n'est armé" || true
# 4. outil
bash "$M" 126 600 "faux-outil" "$S/pid-o" > /dev/null 2>&1; attendu "outil relatif" $? 4
bash "$M" 126 600 "$S/inexistant" "$S/pid-o" > /dev/null 2>&1; attendu "outil absent" $? 4
# 5. identifiant, fichier PID
bash "$M" "12a" 600 "$S/faux-outil" "$S/pid-i" > /dev/null 2>&1; attendu "identifiant" $? 2
bash "$M" 127 600 "$S/faux-outil" "$S/inexistant/pid" > /dev/null 2>&1; attendu "fichier PID" $? 5
# 6. refus de l'outil
BORNE_MIN_S=1 ATTENTE_S=1 bash "$M" 128 1 "$S/faux-refus" "$S/pid-r" > "$S/j-r.txt" 2>&1; attendu refus $? 6
n=$(wc -l < "$S/appels-refus.txt"); echo "  refus : $n appel(s) (attendu 3)"; [ "$n" -eq 3 ] || ecart "refus : $n appels"
echo "  journaux :"; cat "$S"/j-sain.txt "$S"/j-det.txt "$S"/j-r.txt | sed 's/^/    /'
N=$(wc -l < "$E")
echo "VERDICT de l'essai : $([ "$N" -eq 0 ] && echo "conforme, 0 écart" || echo "NON conforme, $N écart(s) : $(tr '\n' ';' < "$E")")"
