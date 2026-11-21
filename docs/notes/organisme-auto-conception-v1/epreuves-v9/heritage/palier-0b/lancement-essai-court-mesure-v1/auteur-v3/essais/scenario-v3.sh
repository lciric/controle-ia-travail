#!/bin/bash
# Scénario générique v3 : n'écrit que sous le dossier v3 (base tirée de l'emplacement de ce script, aucun chemin en dur).
# Départ par le VRAI script de départ (v2, inchangé), lanceur factice générique, gardien v3 par son VRAI script de départ.
# Usage : scenario-v3.sh NOM TEMOIN TUER_CHEF_S PROGRAMME [ARGUMENTS DU PROGRAMME...] -- [OPTIONS DU GARDIEN...]
#   TEMOIN 1 : un « setsid sleep 120 » sans lien est lancé à côté ; il ne doit recevoir aucun signal (arrêté par moi ensuite).
#   TUER_CHEF_S > 0 : le chef (lanceur) est tué par moi (SIGKILL, par son identifiant) après ce nombre de secondes.
#   Jetons remplacés : @S@ dossier des sorties ; @M@ marqueur ; @E@ dossier des essais ;
#   @LIBRES_MOINS_100M@ place libre du système de fichiers des essais au départ, moins 100 000 000 octets.
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
NOM=$1; TEMOIN=$2; TUER=$3; PROG=$4
shift 4
D=$E/e/$NOM
T=$D/tenue
S=$D/sorties
M=$D/marqueur
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$T"
LIBRES=$(df --output=avail -B1 "$E" | tail -n 1 | tr -d ' ')
SEUIL=$((LIBRES - 100000000))
remplacer() {
  local x=$1
  x=${x//@S@/$S}; x=${x//@M@/$M}; x=${x//@E@/$E}; x=${x//@LIBRES_MOINS_100M@/$SEUIL}
  printf '%s' "$x"
}
PARGS=()
while [ $# -gt 0 ] && [ "$1" != "--" ]; do PARGS+=("$(remplacer "$1")"); shift; done
if [ $# -gt 0 ]; then shift; fi
GARGS=()
while [ $# -gt 0 ]; do GARGS+=("$(remplacer "$1")"); shift; done
echo "scénario $NOM ; place libre au départ $LIBRES o (seuil factice éventuel $SEUIL o)"
if [ "$TEMOIN" = 1 ]; then
  setsid nohup /bin/sleep 120 < /dev/null > /dev/null 2>&1 &
  TP=$!
  echo "témoin sans lien : processus $TP"
fi
bash "$B/demarrer-essai-court-v2.sh" "$T" "$E/lanceur-py-v3.sh" "$(remplacer "$PROG")" "${PARGS[@]}"
bash "$B/demarrer-gardien-essai-court-v3.sh" "$T" --sorties "$S" "${GARGS[@]}"
GP=$(cat "$T/pid-gardien-essai-court.txt")
CHEF=$(cat "$T/pid-essai-court.txt")
if [ "$TUER" != 0 ]; then
  sleep "$TUER"
  echo "chef $CHEF tué par moi (SIGKILL, par identifiant) à $(date -u +%H:%M:%S.%N) : $(stat -c %n /proc/$CHEF 2>/dev/null || echo 'déjà absent')"
  kill -9 "$CHEF"
fi
for i in $(seq 1 200); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "=== gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s ; chef $CHEF : $(stat -c %n /proc/$CHEF 2>/dev/null || echo absent)"
for f in code-de-sortie.txt arret-gardien.txt mesure-essai-court.txt; do
  if [ -f "$T/$f" ]; then echo "--- $f :"; cat "$T/$f"; else echo "--- $f : (absent)"; fi
done
echo "--- journal de tenue, lignes de note et d'erreur :"
grep -E 'note=|garde continue|ERREUR|identité à la prise' "$T/journal-de-tenue-essai-court.txt"
echo "--- dernière ligne du journal de tenue :"
tail -n 1 "$T/journal-de-tenue-essai-court.txt"
if [ -f "$M.pid" ]; then
  CP=$(cat "$M.pid")
  echo "--- processus du marqueur $CP : $(stat -c %n /proc/$CP 2>/dev/null || echo absent)"
fi
if [ -f "$M" ]; then
  A=$(wc -l < "$M"); sleep 3; Z=$(wc -l < "$M")
  echo "--- marqueur : $A lignes, puis $Z lignes 3 s plus tard"
fi
N1=$(find "$S/etape-4/couche-mecanique/bras-1-a-3" -mindepth 3 -maxdepth 3 -type d 2>/dev/null | wc -l)
F1=$(find "$S/etape-4" -type f 2>/dev/null | wc -l)
echo "--- après coup : dossiers de source $N1 ; fichiers sous etape-4 $F1"
if [ -f "$M.pid" ] && [ -e "/proc/$(cat "$M.pid")" ]; then
  kill -9 "$(cat "$M.pid")"
  sleep 2
  echo "--- processus du marqueur ENCORE VIVANT à la fin : arrêté par moi par son identifiant : $(stat -c %n /proc/$(cat "$M.pid") 2>/dev/null || echo absent)"
fi
if [ "$TEMOIN" = 1 ]; then
  echo "--- témoin $TP : $(stat -c %n /proc/$TP 2>/dev/null || echo ABSENT)"
  kill "$TP" 2>/dev/null
  sleep 0.5
  echo "--- témoin arrêté par moi par son identifiant : $(stat -c %n /proc/$TP 2>/dev/null || echo absent)"
fi
