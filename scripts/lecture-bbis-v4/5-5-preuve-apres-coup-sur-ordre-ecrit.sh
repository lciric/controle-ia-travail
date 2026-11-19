#!/bin/bash
# § 5.5 — preuve après coup, À NE JOUER QUE SUR ORDRE ÉCRIT DE LA CONDUCTRICE
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.5 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-5-preuve-apres-coup-sur-ordre-ecrit.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : arrêt avant le seuil$' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « arrêt avant le seuil » : arrêt"; exit 1; }
egal "empreinte du programme de la preuve après coup" b7bc7e5d87ba45a696ded6790e1354fd065467f838ef565efba2ff0746b05675 "$(sha256sum "$ARBRE/scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py" | cut -d' ' -f1)"
[ "$FAUTES" = 0 ] || { echo "programme d'une autre empreinte : arrêt"; exit 1; }
set --
for n in $(seq 1 "$N"); do g="$LV1/sortie-lancement-lecture-bbis-$n-v1.txt"; set -- "$@" --sortie-lancement "$g" "$(sha256sum "$g" | cut -d' ' -f1)"; done
cd "$ARBRE" || exit 1
"${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 "$PY" scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py --racine "$ARBRE" --run-lecture "$RUNL" --run-bbis "$RUN_BBIS" --numero "$N" "$@"
echo "code de sortie du programme de la preuve après coup : $?"
