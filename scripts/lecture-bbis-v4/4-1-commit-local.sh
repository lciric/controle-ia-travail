#!/bin/bash
# § 4.1 — entrées commitées localement dans l'arbre de lecture (lecteur-opérateur)
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 4.1, bloc de l'opérateur » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-1-commit-local.sh
. "$(dirname "$0")/commun.sh"
grep -q "CONCLUSION : conforme" "$LV1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt" || { echo "preuve non conforme : arrêt"; exit 1; }
cd "$ARBRE" || exit 1
git -c user.name="lecteur-operateur" -c user.email="lecteur-operateur@example.invalid" -c commit.gpgsign=false \
  commit -q -m "Étape B bis, lecture : entrées de la liste blanche, commit local de l'arbre de lecture" || { echo "commit local refusé : arrêt"; exit 1; }
git rev-parse HEAD
