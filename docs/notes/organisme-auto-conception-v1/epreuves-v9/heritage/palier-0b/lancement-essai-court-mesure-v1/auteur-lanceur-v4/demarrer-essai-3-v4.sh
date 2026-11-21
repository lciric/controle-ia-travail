#!/bin/bash
# Script de départ de l'essai 3 du palier 0b — v4 (= départ v3, seul le nom du lanceur lancé change : v4 ; v3 : = départ v2 de l'essai court, plus : arguments du lanceur v3 passés tels
# quels ; noms des fichiers de tenue de l'essai 3, complément 1 v3 « Tenue du lancement »).
# Lance le lanceur DÉTACHÉ (setsid nohup), entrée fermée (/dev/null), sortie standard et d'erreur dans
# DOSSIER_DE_TENUE/journal-essai-3.txt ; écrit, chacun dans un fichier du dossier de tenue :
#   pid-essai-3.txt (identifiant du processus), pgid-essai-3.txt (identifiant de son groupe),
#   boot-id-essai-3.txt (/proc/sys/kernel/random/boot_id), heure-lancement-essai-3.txt (date -u),
#   depart-processus-essai-3.txt (heure de démarrage du processus, 22e champ de /proc/PID/stat, en tops depuis le démarrage
#   de la machine ; lue seulement si le processus est bien l'enfant de ce script ; sinon « inconnu », et le gardien n'enverra
#   aucun signal).
#
# Emploi : demarrer-essai-3-v4.sh DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES
#          (lanceur : lancer-essai-3-v4.sh, pris à côté de ce script ; arguments contrôlés par le lanceur)
# Essai :  demarrer-essai-3-v4.sh --lanceur LANCEUR DOSSIER_DE_TENUE [ARGUMENTS DU LANCEUR APRÈS LE DOSSIER DE TENUE...]
# Rien n'est écrasé : départ refusé si l'un des fichiers ci-dessus existe déjà.
set -u

if [ $# -ge 1 ] && [ "$1" = "--lanceur" ]; then
  if [ $# -lt 3 ]; then
    echo "usage : $0 --lanceur LANCEUR DOSSIER_DE_TENUE [ARGUMENTS...]" >&2
    exit 2
  fi
  LANCEUR=$2
  TENUE=$3
  shift 3
else
  if [ $# -ne 4 ]; then
    echo "usage : $0 DOSSIER_DE_TENUE RACINE INTERPRETE SORTIES   (ou --lanceur LANCEUR DOSSIER_DE_TENUE [ARGUMENTS...])" >&2
    exit 2
  fi
  LANCEUR="$(dirname "$0")/lancer-essai-3-v4.sh"
  TENUE=$1
  shift
fi
if [ ! -d "$TENUE" ]; then
  echo "refus : dossier de tenue absent : $TENUE" >&2
  exit 3
fi
if [ ! -f "$LANCEUR" ]; then
  echo "refus : lanceur absent : $LANCEUR" >&2
  exit 3
fi
JOURNAL="$TENUE/journal-essai-3.txt"
F_PID="$TENUE/pid-essai-3.txt"
F_PGID="$TENUE/pgid-essai-3.txt"
F_BOOT="$TENUE/boot-id-essai-3.txt"
F_HEURE="$TENUE/heure-lancement-essai-3.txt"
F_DEPART="$TENUE/depart-processus-essai-3.txt"
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
