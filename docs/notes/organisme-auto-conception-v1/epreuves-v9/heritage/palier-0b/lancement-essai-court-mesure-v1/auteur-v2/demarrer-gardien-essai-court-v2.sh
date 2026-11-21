#!/bin/bash
# Départ du gardien de l'essai court de mesure du palier 0b — v2.
# Lance gardien-essai-court-v2.py (pris à côté de ce script) DÉTACHÉ (setsid nohup), entrée fermée, sorties dans
# DOSSIER_DE_TENUE/sortie-gardien-essai-court.txt ; écrit son identifiant dans DOSSIER_DE_TENUE/pid-gardien-essai-court.txt.
# À lancer APRÈS demarrer-essai-court-v2.sh (le gardien lit pid, pgid, boot-id et l'heure de départ écrits par lui ; si le
# fichier de l'heure de départ manque, le gardien tient son journal mais n'envoie aucun signal).
#
# Emploi : demarrer-gardien-essai-court-v2.sh DOSSIER_DE_TENUE                 (valeurs d'emploi du gardien)
# Essai :  demarrer-gardien-essai-court-v2.sh DOSSIER_DE_TENUE --sorties S [--seuil-libre-octets X] [--seuil-n N]
#          [--duree-etape-4-s D] [--intervalle-s I] [--delai-force-s F] [--total T]
set -u
PY=/home/user/controle-ia-travail/.venv/bin/python
if [ $# -lt 1 ]; then
  echo "usage : $0 DOSSIER_DE_TENUE [OPTIONS DU GARDIEN...]" >&2
  exit 2
fi
TENUE=$1
shift
GARDIEN="$(dirname "$0")/gardien-essai-court-v2.py"
SORTIE="$TENUE/sortie-gardien-essai-court.txt"
F_PID="$TENUE/pid-gardien-essai-court.txt"
for f in "$TENUE/pid-essai-court.txt" "$TENUE/pgid-essai-court.txt" "$TENUE/boot-id-essai-court.txt"; do
  if [ ! -f "$f" ]; then
    echo "refus : $f absent (lancer d'abord demarrer-essai-court-v2.sh)" >&2
    exit 3
  fi
done
for f in "$SORTIE" "$F_PID"; do
  if [ -e "$f" ] || [ -L "$f" ]; then
    echo "refus : $f déjà présent (rien n'est écrasé)" >&2
    exit 4
  fi
done
setsid nohup "$PY" -I -B "$GARDIEN" --tenue "$TENUE" "$@" < /dev/null > "$SORTIE" 2>&1 &
PID=$!
echo "$PID" > "$F_PID"
echo "gardien : processus $PID ; journal $TENUE/journal-de-tenue-essai-court.txt"
