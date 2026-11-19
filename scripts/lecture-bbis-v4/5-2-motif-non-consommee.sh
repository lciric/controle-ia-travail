#!/bin/bash
# § 5.2 — état « non consommée » : le motif du refus, extrait de la pièce de preuve écrite par le module
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.2, ligne écrite dans la prose (exception de l'état « non consommée ») » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-motif-non-consommee.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : non consommée' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « non consommée » : arrêt"; exit 1; }
grep -o '"motif": "[^"]*"' "$ARBRE/diag/$RUNL/preuve-aucune-ouverture-bbis.json"
