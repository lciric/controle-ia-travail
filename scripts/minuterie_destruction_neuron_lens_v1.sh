#!/usr/bin/env bash
# Minuterie de destruction par identifiant d'instance pour la course du volet A de « Neuron Lens » — v1 (contre-lecture 10, Q-1, Q-2,
# Q-4, Q-5). Remplace la minuterie écrite en ligne dans la commande v8 (`… && setsid nohup bash -c … & echo $!`, dont le `&` mettait
# toute la liste en arrière-plan : durée perdue, PID d'un sous-shell, arrêt par PID inopérant).
#
# Usage : bash scripts/minuterie_destruction_neuron_lens_v1.sh <ID_INSTANCE> <DUREE_S> <CHEMIN_ABSOLU_DE_L_OUTIL> <FICHIER_PID>
# Lancée détachée (`setsid nohup … &`) ; elle écrit son propre PID (`$$`, le processus qui dormira puis détruira) dans FICHIER_PID :
# c'est ce PID que l'on vérifie vivant puis que l'on arrête (R10). L'arrêter avant l'échéance empêche la destruction (SIGTERM, action
# par défaut : le script meurt ; le `sleep` orphelin s'achève sans effet). L'outil est appelé par son chemin absolu (aucune dépendance au
# `PATH` du shell qui l'a lancée). Sortie de l'outil jetée (aucune sortie du loueur dans le journal). Codes : 2 identifiant invalide ;
# 3 durée hors bornes [BORNE_MIN_S, BORNE_MAX_S] (défaut 600 à 108000 s : 90 % de 10 USD entre 0,30 et 0,90 USD/h donne 36000 à 108000
# s) ; 4 outil non absolu ou non exécutable ; 5 fichier PID impossible ; 6 destruction refusée après 3 essais. Bornes et attente entre
# essais (ATTENTE_S, 30) réglables pour l'essai seulement ; la commande ne les règle pas.
set -u
ID=${1:-}; D=${2:-}; OUTIL=${3:-}; FPID=${4:-}
MIN=${BORNE_MIN_S:-600}; MAX=${BORNE_MAX_S:-108000}; ATTENTE=${ATTENTE_S:-30}
log() { echo "MINUTERIE $(date -u +%FT%TZ) $*"; }
[[ "$ID" =~ ^[0-9]+$ ]] || { log "identifiant invalide : '$ID'"; exit 2; }
if ! [[ "$D" =~ ^[0-9]+$ ]] || [ "$D" -lt "$MIN" ] || [ "$D" -gt "$MAX" ]; then
  log "duree hors bornes : '$D' (bornes $MIN a $MAX s) ; minuterie NON armee"; exit 3
fi
case "$OUTIL" in /*) ;; *) log "chemin de l'outil non absolu : '$OUTIL' ; minuterie NON armee"; exit 4 ;; esac
[ -x "$OUTIL" ] || { log "outil non executable : $OUTIL ; minuterie NON armee"; exit 4; }
[ -n "$FPID" ] && echo $$ > "$FPID" || { log "fichier PID impossible : '$FPID' ; minuterie NON armee"; exit 5; }
log "armee : instance $ID, destruction dans $D s, PID $$, outil $OUTIL"
sleep "$D"
log "echeance : destruction de l'instance $ID"
for i in 1 2 3; do
  if "$OUTIL" destroy instance "$ID" > /dev/null 2>&1; then log "destruction demandee (essai $i/3)"; exit 0; fi
  log "destruction refusee (essai $i/3)"
  [ "$i" -lt 3 ] && sleep "$ATTENTE"
done
log "DESTRUCTION EN ECHEC : instance $ID"
exit 6
