#!/bin/bash
# § 4.1 — gestes de la conductrice entre les deux temps : preuve commitée et poussée, branche de l'arbre de lecture poussée
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 4.1, bloc de la conductrice » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-1-conductrice-preuve-et-branche.sh
. "$(dirname "$0")/commun.sh"
cd "$DEPOT" || exit 1
P=registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt
git add -- "$P" "$P.sha256" && git commit -q -m "Étape B bis, lecture : preuve d'antériorité et preuve d'entrée conjointe, inscrites à part avant la lecture" && git push origin claude/lecture-verdict-etape-b-bis-v1
git push origin "$BRANCHE_LOCALE_ARBRE:refs/heads/$BRANCHE_DISTANTE_ARBRE"
git ls-remote --heads origin "$BRANCHE_DISTANTE_ARBRE"     # attendu : la tête rendue par l'opérateur
