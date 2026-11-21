#!/bin/bash
# Script de départ de l'essai court de mesure du palier 0b — v2.
# Lance le lanceur DÉTACHÉ (setsid nohup), entrée fermée (/dev/null), sortie standard et d'erreur dans
# DOSSIER_DE_TENUE/journal-essai-court.txt ; écrit, chacun dans un fichier du dossier de tenue :
#   pid-essai-court.txt (identifiant du processus), pgid-essai-court.txt (identifiant de son groupe),
#   boot-id-essai-court.txt (/proc/sys/kernel/random/boot_id), heure-lancement-essai-court.txt (date -u),
#   depart-processus-essai-court.txt (v2, erratum 1 correction 1 : heure de démarrage du processus, 22e champ de
#   /proc/PID/stat, en tops depuis le démarrage de la machine ; lue seulement si le processus est bien l'enfant de ce
#   script ; sinon « inconnu », et le gardien n'enverra aucun signal).
#
# Emploi : demarrer-essai-court-v2.sh DOSSIER_DE_TENUE
#          (lanceur : lancer-essai-court-v2.sh, pris à côté de ce script)
# Essai :  demarrer-essai-court-v2.sh DOSSIER_DE_TENUE LANCEUR [ARGUMENTS DU LANCEUR APRÈS LE DOSSIER DE TENUE...]
# Rien n'est écrasé : départ refusé si l'un des fichiers ci-dessus existe déjà.
set -u

if [ $# -lt 1 ]; then
  echo "usage : $0 DOSSIER_DE_TENUE [LANCEUR [ARGUMENTS...]]" >&2
  exit 2
fi
TENUE=$1
shift
if [ $# -ge 1 ]; then
  LANCEUR=$1
  shift
else
  LANCEUR="$(dirname "$0")/lancer-essai-court-v2.sh"
fi
if [ ! -d "$TENUE" ]; then
  echo "refus : dossier de tenue absent : $TENUE" >&2
  exit 3
fi
if [ ! -f "$LANCEUR" ]; then
  echo "refus : lanceur absent : $LANCEUR" >&2
  exit 3
fi
JOURNAL="$TENUE/journal-essai-court.txt"
F_PID="$TENUE/pid-essai-court.txt"
F_PGID="$TENUE/pgid-essai-court.txt"
F_BOOT="$TENUE/boot-id-essai-court.txt"
F_HEURE="$TENUE/heure-lancement-essai-court.txt"
F_DEPART="$TENUE/depart-processus-essai-court.txt"
for f in "$JOURNAL" "$F_PID" "$F_PGID" "$F_BOOT" "$F_HEURE" "$F_DEPART"; do
  if [ -e "$f" ] || [ -L "$f" ]; then
    echo "refus : $f déjà présent (rien n'est écrasé) : aucun départ" >&2
    exit 4
  fi
done

BOOT=$(cat /proc/sys/kernel/random/boot_id)
setsid nohup /bin/bash "$LANCEUR" "$TENUE" "$@" < /dev/null > "$JOURNAL" 2>&1 &
PID=$!
HEURE=$(date -u +%Y-%m-%dT%H:%M:%S.%NZ)
echo "$PID" > "$F_PID"
echo "$BOOT" > "$F_BOOT"
echo "$HEURE" > "$F_HEURE"

# Groupe et heure de départ : setsid (exécuté sans fourche, l'enfant d'arrière-plan n'étant pas chef de groupe) fait du
# processus le chef d'une session neuve, donc groupe = processus. On lit /proc/PID/stat jusqu'à ce que le groupe soit établi ;
# l'heure de départ (22e champ) est celle de la fourche, inchangée par les exécutions qui suivent ; elle n'est retenue que si
# le parent lu (4e champ) est ce script ($$) : le processus lu est alors bien celui qu'il vient de lancer.
PGID=""
DEPART=""
for i in $(seq 1 100); do
  if [ ! -r "/proc/$PID/stat" ]; then
    break
  fi
  STAT=$(cat "/proc/$PID/stat" 2>/dev/null)
  RESTE=${STAT##*) }
  CHAMPS=($RESTE)
  PARENT=${CHAMPS[1]:-}
  GROUPE=${CHAMPS[2]:-}
  TOPS=${CHAMPS[19]:-}
  if [ "$PARENT" != "$$" ]; then
    break
  fi
  if [ "$GROUPE" = "$PID" ]; then
    PGID=$GROUPE
    DEPART=$TOPS
    break
  fi
  sleep 0.05
done
if [ -z "$PGID" ] || [ -z "$DEPART" ]; then
  echo "inconnu" > "$F_PGID"
  echo "inconnu" > "$F_DEPART"
  echo "attention : groupe ou heure de départ du processus $PID non établis (processus déjà absent, parent ou groupe différent) ; voir le journal" >&2
  echo "processus $PID ; groupe inconnu ; heure de départ inconnue ; démarrage $BOOT ; heure $HEURE"
  exit 5
fi
echo "$PGID" > "$F_PGID"
echo "$DEPART" > "$F_DEPART"
echo "processus $PID ; groupe $PGID ; heure de départ (tops) $DEPART ; démarrage $BOOT ; heure $HEURE ; journal $JOURNAL"
