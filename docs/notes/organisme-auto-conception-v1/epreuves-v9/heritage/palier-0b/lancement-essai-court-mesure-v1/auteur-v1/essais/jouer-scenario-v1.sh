#!/bin/bash
# Joue un scénario : départ détaché du lanceur factice (par le VRAI script de départ), départ détaché du gardien (par le VRAI
# script de départ du gardien) avec ses options factices, attente de la fin du gardien (par son identifiant), puis relevé.
# Usage : jouer-scenario-v1.sh DOSSIER_DU_SCENARIO DOSSIER_DES_SCRIPTS ATTENTE_MAX_S [OPTIONS DU GARDIEN...]
set -u
D=$1
S=$2
MAX=$3
shift 3
TENUE="$D/tenue"
bash "$S/demarrer-essai-court-v1.sh" "$TENUE" "$D/lanceur-factice.sh"
echo "code du script de départ : $?"
bash "$S/demarrer-gardien-essai-court-v1.sh" "$TENUE" --sorties "$D/sorties" "$@"
GPID=$(cat "$TENUE/pid-gardien-essai-court.txt")
PID=$(cat "$TENUE/pid-essai-court.txt")
for i in $(seq 1 "$MAX"); do
  if [ ! -e "/proc/$GPID" ]; then break; fi
  sleep 1
done
echo "=== fin d'attente après $i s ; gardien $GPID : $(stat -c %n /proc/$GPID 2>/dev/null || echo absent) ; programme $PID : $(stat -c %n /proc/$PID 2>/dev/null || echo absent)"
for f in pid-essai-court.txt pgid-essai-court.txt boot-id-essai-court.txt heure-lancement-essai-court.txt code-de-sortie.txt \
         journal-essai-court.txt journal-de-tenue-essai-court.txt arret-gardien.txt mesure-essai-court.txt \
         sortie-gardien-essai-court.txt; do
  if [ -f "$TENUE/$f" ]; then
    echo "--- $f :"
    cat "$TENUE/$f"
  else
    echo "--- $f : (absent)"
  fi
done
for f in "$TENUE"/inventaire-*; do
  if [ -f "$f" ]; then echo "--- $(basename "$f") :"; cat "$f"; fi
done
