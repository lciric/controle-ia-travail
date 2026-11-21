#!/bin/bash
# Joue un scénario de l'auteur v1 (s1 à s9) sur les pièces du dossier v3 : départ par demarrer-essai-court-v2.sh (inchangé),
# gardien v3 par demarrer-gardien-essai-court-v3.sh ; attente de la fin du gardien (par identifiant) ; relevé des fichiers.
# Usage : jouer-scenario-v3.sh DOSSIER_DU_SCENARIO ATTENTE_MAX_S MODE [OPTIONS DU GARDIEN...]   (MODE : normal | pgid-faux)
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
D=$1
MAX=$2
MODE=$3
shift 3
TENUE="$D/tenue"
bash "$B/demarrer-essai-court-v2.sh" "$TENUE" "$D/lanceur-factice.sh"
echo "code du script de départ : $?"
if [ "$MODE" = pgid-faux ]; then
  echo "3999999" > "$TENUE/pgid-essai-court.txt"
  echo "fichier du groupe réécrit à 3999999 (artefact)"
fi
bash "$B/demarrer-gardien-essai-court-v3.sh" "$TENUE" --sorties "$D/sorties" "$@"
GPID=$(cat "$TENUE/pid-gardien-essai-court.txt")
PID=$(cat "$TENUE/pid-essai-court.txt")
for i in $(seq 1 "$MAX"); do
  if [ ! -e "/proc/$GPID" ]; then break; fi
  sleep 1
done
echo "=== fin d'attente après $i s ; gardien $GPID : $(stat -c %n /proc/$GPID 2>/dev/null || echo absent) ; programme $PID : $(stat -c %n /proc/$PID 2>/dev/null || echo absent)"
for f in depart-processus-essai-court.txt code-de-sortie.txt arret-gardien.txt mesure-essai-court.txt; do
  if [ -f "$TENUE/$f" ]; then echo "--- $f :"; cat "$TENUE/$f"; else echo "--- $f : (absent)"; fi
done
echo "--- journal de tenue, notes :"
grep -E 'note=|garde continue|ERREUR|identité à la prise' "$TENUE/journal-de-tenue-essai-court.txt"
for f in "$TENUE"/inventaire-*.txt; do
  if [ -f "$f" ]; then echo "--- $(basename "$f") : $(head -n 1 "$f" | grep -o '[0-9]* fichiers$')"; fi
done
