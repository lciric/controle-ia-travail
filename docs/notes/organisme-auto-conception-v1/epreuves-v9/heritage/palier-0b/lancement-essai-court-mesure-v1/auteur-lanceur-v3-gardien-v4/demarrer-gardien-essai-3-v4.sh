#!/bin/bash
# Départ du gardien de l'essai 3 du palier 0b — v4 (= départ v3, plus : interpréteur passé en paramètre ; paramètres du
# gardien contrôlés AVANT le départ détaché, par le gardien lui-même en mode --verifier-seulement ; noms « essai-3 »).
# Lance gardien-essai-3-v4.py (pris à côté de ce script) DÉTACHÉ (setsid nohup), entrée fermée, sorties dans
# DOSSIER_DE_TENUE/sortie-gardien-essai-3.txt ; écrit son identifiant dans DOSSIER_DE_TENUE/pid-gardien-essai-3.txt.
# À lancer APRÈS demarrer-essai-3-v3.sh (le gardien lit pid, pgid, boot-id et l'heure de départ écrits par lui ; si le
# fichier de l'heure de départ manque, le gardien tient son journal mais n'envoie aucun signal).
#
# Emploi : demarrer-gardien-essai-3-v4.sh DOSSIER_DE_TENUE INTERPRETE --sorties S --heure-arret-duree AAAA-MM-JJTHH:MM:SSZ
#          (heure : H0 + 94 h, par exemple date -u -d "@$(( $(date -u -d H0 +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ ;
#           arrêt de mesure désarmé et autres réglages : valeurs d'emploi du gardien)
# Essai :  ... [--arret-mesure arme] [--seuil-libre-octets X] [--seuil-n N] [--duree-etape-4-s D] [--intervalle-s I]
#          [--delai-force-s F] [--total T] [--ecart-max-arret-duree-s E]
# Codes : 2 usage ou paramètres du gardien refusés (rien n'est lancé) ; 3 fichier du lanceur absent ou interpréteur absent ;
#         4 fichier déjà présent (rien n'est écrasé).
set -u
if [ $# -lt 2 ]; then
  echo "usage : $0 DOSSIER_DE_TENUE INTERPRETE --sorties S --heure-arret-duree H [OPTIONS DU GARDIEN...]" >&2
  exit 2
fi
TENUE=$1
PY=$2
shift 2
GARDIEN="$(dirname "$0")/gardien-essai-3-v4.py"
SORTIE="$TENUE/sortie-gardien-essai-3.txt"
F_PID="$TENUE/pid-gardien-essai-3.txt"
if [ ! -f "$PY" ] || [ ! -x "$PY" ]; then
  echo "refus : interpréteur absent ou non exécutable : $PY" >&2
  exit 3
fi
for f in "$TENUE/pid-essai-3.txt" "$TENUE/pgid-essai-3.txt" "$TENUE/boot-id-essai-3.txt"; do
  if [ ! -f "$f" ]; then
    echo "refus : $f absent (lancer d'abord demarrer-essai-3-v3.sh)" >&2
    exit 3
  fi
done
for f in "$SORTIE" "$F_PID"; do
  if [ -e "$f" ] || [ -L "$f" ]; then
    echo "refus : $f déjà présent (rien n'est écrasé)" >&2
    exit 4
  fi
done
# Contrôle des paramètres avant tout départ (heure d'arrêt de durée mal formée ou trop lointaine : refus, code 2).
if ! "$PY" -I -B "$GARDIEN" --tenue "$TENUE" "$@" --verifier-seulement; then
  echo "refus : paramètres du gardien refusés (voir ci-dessus) : aucun départ" >&2
  exit 2
fi
setsid nohup "$PY" -I -B "$GARDIEN" --tenue "$TENUE" "$@" < /dev/null > "$SORTIE" 2>&1 &
PID=$!
echo "$PID" > "$F_PID"
echo "gardien : processus $PID ; journal $TENUE/journal-de-tenue-essai-3.txt"
