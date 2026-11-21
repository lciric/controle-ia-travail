#!/bin/bash
# Refus de départ du gardien v4 par son VRAI script de départ, sur l'heure d'arrêt de durée. Tenue factice qui désigne un
# témoin sans lien (setsid sleep), SANS fichier d'heure de départ : même si un refus manquait, le gardien ne pourrait envoyer
# aucun signal (identité non confirmée). Pour chaque cas : code du script de départ, présence de pid-gardien-essai-3.txt, de
# sortie-gardien-essai-3.txt et du journal de tenue. Les gardiens partis (cas acceptés) sont arrêtés par moi par leur
# identifiant. Contrôle aussi la commande d'en-tête qui calcule H0 + 94 h.
# Usage : essai-heure-depart-v4.sh NOM
set -u
E=$(cd "$(dirname "$0")" && pwd)
B=$(cd "$E/.." && pwd)
PY=/home/user/controle-ia-travail/.venv/bin/python
D=$E/e/$1
if [ -e "$D" ]; then echo "refus : $D existe" >&2; exit 1; fi
mkdir -p "$D"
setsid nohup /bin/sleep 300 < /dev/null > /dev/null 2>&1 &
TP=$!
echo "témoin sans lien : $TP"
MAINTENANT=$(date -u +%s)
h() { date -u -d "@$((MAINTENANT + $1))" +%Y-%m-%dT%H:%M:%SZ; }
ECHECS=0
N=0
cas() {  # nom code_attendu [options après --sorties S]
  local nom=$1 attendu=$2
  shift 2
  local T="$D/$nom/tenue"
  mkdir -p "$T"
  echo "$TP" > "$T/pid-essai-3.txt"
  echo "$TP" > "$T/pgid-essai-3.txt"
  cat /proc/sys/kernel/random/boot_id > "$T/boot-id-essai-3.txt"
  bash "$B/demarrer-gardien-essai-3-v4.sh" "$T" "$PY" --sorties "$D/$nom/sorties" "$@" > "$D/$nom/depart.txt" 2>&1
  local o=$?
  local pidg="absent" sortie="absente" journal="absent"
  [ -f "$T/pid-gardien-essai-3.txt" ] && pidg="présent ($(cat "$T/pid-gardien-essai-3.txt"))"
  [ -f "$T/sortie-gardien-essai-3.txt" ] && sortie="présente"
  sleep 0.5
  [ -f "$T/journal-de-tenue-essai-3.txt" ] && journal="présent"
  local v=TENU
  N=$((N + 1))
  if [ "$o" != "$attendu" ]; then v=CASSÉ; fi
  if [ "$attendu" != 0 ] && { [ "$pidg" != absent ] || [ "$sortie" != absente ] || [ "$journal" != absent ]; }; then v=CASSÉ; fi
  if [ "$v" = CASSÉ ]; then ECHECS=$((ECHECS + 1)); fi
  echo "$nom : code $o (attendu $attendu) ; pid du gardien $pidg ; sortie $sortie ; journal $journal ; $v ; $(grep -E 'error|paramètres reçus' "$D/$nom/depart.txt" | tail -n 1 | cut -c1-260)"
  if [ -f "$T/pid-gardien-essai-3.txt" ]; then
    local g
    g=$(cat "$T/pid-gardien-essai-3.txt")
    kill "$g" 2>/dev/null
    sleep 0.3
    echo "    gardien $g arrêté par moi par son identifiant : $(stat -c %n /proc/$g 2>/dev/null || echo absent)"
  fi
}
cas h0-sain-dans-une-heure 0 --heure-arret-duree "$(h 3600)"
cas h1-bord-94-h 0 --heure-arret-duree "$(h $((94 * 3600)))"
cas h1b-bord-94-h-10-min-moins-60-s 0 --heure-arret-duree "$(h $((94 * 3600 + 540)))"
cas h2-trop-loin-94-h-11-min 2 --heure-arret-duree "$(h $((94 * 3600 + 660)))"
cas h2b-faute-de-mois 2 --heure-arret-duree "$(date -u -d "@$((MAINTENANT + 31 * 86400))" +%Y-%m-%dT%H:%M:%SZ)"
cas h3-format-date-u-par-defaut 2 --heure-arret-duree "$(date -u -d "@$((MAINTENANT + 3600))")"
cas h4-sans-Z 2 --heure-arret-duree "$(date -u -d "@$((MAINTENANT + 3600))" +%Y-%m-%dT%H:%M:%S)"
cas h5-espace-au-lieu-de-T 2 --heure-arret-duree "$(date -u -d "@$((MAINTENANT + 3600))" '+%Y-%m-%d %H:%M:%SZ')"
cas h6-31-novembre 2 --heure-arret-duree 2026-11-31T10:00:00Z
cas h7-vide 2 --heure-arret-duree ""
cas h8-absente 2
cas h9-decalage-horaire 2 --heure-arret-duree "$(date -u -d "@$((MAINTENANT + 3600))" +%Y-%m-%dT%H:%M:%S+00:00)"
cas h10-arret-mesure-inconnu 2 --heure-arret-duree "$(h 3600)" --arret-mesure oui
cas h11-passee-acceptee 0 --heure-arret-duree "$(h -60)"
echo "--- témoin $TP : $(stat -c %n /proc/$TP 2>/dev/null || echo ABSENT) (il ne doit avoir reçu aucun signal)"
kill "$TP"
sleep 0.3
echo "--- témoin arrêté par moi par son identifiant : $(stat -c %n /proc/$TP 2>/dev/null || echo absent)"
# Commande d'en-tête du départ du gardien : H0 + 94 h
H0=2026-11-21T19:00:00Z
CALC=$(date -u -d "@$(( $(date -u -d "$H0" +%s) + 94 * 3600 ))" +%Y-%m-%dT%H:%M:%SZ)
N=$((N + 1))
if [ "$CALC" = 2026-11-25T17:00:00Z ]; then echo "H0 $H0 + 94 h par la commande d'en-tête : $CALC (à la main : 2026-11-25T17:00:00Z) : TENU"; else echo "H0 + 94 h : $CALC : CASSÉ"; ECHECS=$((ECHECS + 1)); fi
echo "essais : $N ; échecs : $ECHECS"
