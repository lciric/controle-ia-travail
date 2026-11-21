#!/bin/bash
# Scénario générique v4 : n'écrit que sous le dossier des essais (base tirée de l'emplacement de ce script).
# Départ par le VRAI script de départ v3 (forme d'emploi) et le VRAI lanceur v3, sur une copie factice sans .git qui porte le
# vrai programme (jamais exécuté) ; l'interprète passé au lanceur est un interprète factice (copie de
# interprete-factice-v4.sh) qui enregistre ce qu'il reçoit puis se remplace par le programme factice donné ici.
# Gardien v4 par son VRAI script de départ.
# Usage : scenario-v4.sh NOM TEMOIN MODE COPIE PROGRAMME [ARGUMENTS DU PROGRAMME...] -- [OPTIONS DU GARDIEN...]
#   TEMOIN 1 : un « setsid sleep 120 » sans lien est lancé à côté ; il ne doit recevoir aucun signal (arrêté par moi ensuite).
#   MODE : 0 (rien) ; N > 0 (le chef, le lanceur, est tué par moi, SIGKILL par son identifiant, après N secondes) ;
#          pgid-faux (le fichier du groupe est réécrit à 3999999 avant le départ du gardien : artefact d'identité).
#   Jetons : @S@ dossier des sorties ; @M@ marqueur ; @E@ dossier des essais ;
#            @LIBRES_MOINS_100M@ place libre du système de fichiers des essais au départ, moins 100 000 000 octets ;
#            @HEURE+N@ (@HEURE-N@) heure absolue (date -u +%Y-%m-%dT%H:%M:%SZ) N secondes après (avant) le départ du
#            scénario.
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
PY=/home/user/controle-ia-travail/.venv/bin/python
NOM=$1; TEMOIN=$2; MODE=$3; COPIE=$4; PROG=$5
shift 5
D=$E/e/$NOM
T=$D/tenue
S=$D/sorties
M=$D/marqueur
I=$D/interprete-factice
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$T"
LIBRES=$(df --output=avail -B1 "$E" | tail -n 1 | tr -d ' ')
SEUIL=$((LIBRES - 100000000))
T0=$(date -u +%s)
remplacer() {
  local x=$1
  x=${x//@S@/$S}; x=${x//@M@/$M}; x=${x//@E@/$E}; x=${x//@LIBRES_MOINS_100M@/$SEUIL}
  if [[ $x =~ ^@HEURE\+([0-9]+)@$ ]]; then
    x=$(date -u -d "@$((T0 + BASH_REMATCH[1]))" +%Y-%m-%dT%H:%M:%SZ)
  elif [[ $x =~ ^@HEURE-([0-9]+)@$ ]]; then
    x=$(date -u -d "@$((T0 - BASH_REMATCH[1]))" +%Y-%m-%dT%H:%M:%SZ)
  fi
  printf '%s' "$x"
}
PARGS=()
while [ $# -gt 0 ] && [ "$1" != "--" ]; do PARGS+=("$(remplacer "$1")"); shift; done
if [ $# -gt 0 ]; then shift; fi
GARGS=()
while [ $# -gt 0 ]; do GARGS+=("$(remplacer "$1")"); shift; done
cp "$E/interprete-factice-v4.sh" "$I"
chmod u+x "$I"
printf '%s\n' "$PY" -I -B "$(remplacer "$PROG")" "${PARGS[@]}" > "$I.args"
echo "scénario $NOM ; départ $(date -u -d "@$T0" +%Y-%m-%dT%H:%M:%SZ) ; place libre $LIBRES o (seuil factice éventuel $SEUIL o)"
echo "options du gardien : ${GARGS[*]}"
if [ "$TEMOIN" = 1 ]; then
  setsid nohup /bin/sleep 120 < /dev/null > /dev/null 2>&1 &
  TP=$!
  echo "témoin sans lien : processus $TP"
fi
bash "$B/demarrer-essai-3-v3.sh" "$T" "$COPIE" "$I" "$S"
echo "code du script de départ : $?"
if [ "$MODE" = pgid-faux ]; then
  echo "3999999" > "$T/pgid-essai-3.txt"
  echo "fichier du groupe réécrit à 3999999 (artefact)"
fi
bash "$B/demarrer-gardien-essai-3-v4.sh" "$T" "$PY" --sorties "$S" "${GARGS[@]}"
echo "code du départ du gardien : $?"
GP=$(cat "$T/pid-gardien-essai-3.txt")
CHEF=$(cat "$T/pid-essai-3.txt")
if [ "$MODE" != 0 ] && [ "$MODE" != pgid-faux ]; then
  sleep "$MODE"
  echo "chef $CHEF tué par moi (SIGKILL, par identifiant) à $(date -u +%H:%M:%S.%N) : $(stat -c %n /proc/$CHEF 2>/dev/null || echo 'déjà absent')"
  kill -9 "$CHEF"
fi
for i in $(seq 1 200); do
  if [ ! -e "/proc/$GP" ]; then break; fi
  sleep 1
done
echo "=== gardien $GP : $(stat -c %n /proc/$GP 2>/dev/null || echo absent) après $i s ; chef $CHEF : $(stat -c %n /proc/$CHEF 2>/dev/null || echo absent) ; fin $(date -u +%Y-%m-%dT%H:%M:%SZ)"
for f in code-de-sortie.txt arret-gardien.txt mesure-essai-3.txt; do
  if [ -f "$T/$f" ]; then echo "--- $f :"; cat "$T/$f"; else echo "--- $f : (absent)"; fi
done
echo "--- journal du lanceur (début) :"
head -n 4 "$T/journal-essai-3.txt"
echo "--- journal de tenue, lignes de prise de garde, de note et d'erreur :"
grep -E 'note=|garde continue|ERREUR|identité à la prise|prise de garde' "$T/journal-de-tenue-essai-3.txt"
echo "--- dernière ligne du journal de tenue :"
tail -n 1 "$T/journal-de-tenue-essai-3.txt"
for f in "$T"/inventaire-*.txt; do
  if [ -f "$f" ]; then echo "--- $(basename "$f") : $(head -n 1 "$f" | grep -o '[0-9]* fichiers$')"; fi
done
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
