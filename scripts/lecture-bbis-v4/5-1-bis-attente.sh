#!/bin/bash
# § 5.1 bis — relevé de l'état du processus, sans jamais l'arrêter
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.1 bis » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-1-bis-attente.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"
PID_L="$(cat "$T/lancement-$N.pid" 2>/dev/null)"; echo "identifiant du processus du module de lecture : ${PID_L:-non écrit}"
if [ -e "$T/lancement-$N.code" ]; then echo "fini : code de sortie écrit"
elif [ -z "$PID_L" ]; then echo "identifiant non écrit : ni « vivant » ni « absent » ; deux relevés de suite ainsi : rendu à la conductrice, rien d'autre"
elif ps -p "$PID_L" -o pid=,stat=,etime=; then echo "vivant : on attend"
else echo "processus absent, code de sortie non écrit"; fi
date -u +%Y-%m-%dT%H:%M:%SZ
