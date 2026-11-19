#!/bin/bash
# § 1.2 — arbre de lecture monté, entrées extraites par chemins nommés
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 1.2 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-2-montage-de-l-arbre.sh
. "$(dirname "$0")/commun.sh"
grep -q "CONCLUSION : conforme" "$(dernier_releve_des_tetes)" || { echo "§ 1.1 non conforme : arrêt"; exit 1; }
neuf "$ARBRE"
cd "$DEPOT" && git worktree add -q -b "$BRANCHE_LOCALE_ARBRE" "$ARBRE" "$TETE_TRAVAIL" || { echo "montage refusé : arrêt"; exit 1; }
cd "$ARBRE" || exit 1
git checkout "$REF_SORTIES" -- "runs/$RUN_BBIS" "diag/$RUN_BBIS" "donnees/$RUN_BBIS" || { echo "extraction des sorties : arrêt"; exit 1; }
for p in "runs/$RUN_7B/manifeste.json" "diag/$RUN_7B/episodes-t06.json" "diag/$RUN_7B/lecture-cout-t06.json" \
         "donnees/$RUN_7B/mesures-t06.npz" "donnees/$RUN_7B/textes-actions-t06.jsonl"; do
  git checkout "$REF_7B" -- "$p" "$p.sha256" || { echo "extraction de $p : arrêt"; exit 1; }
done
p="diag/$RUN_MC/issue-mots-et-cout-t06.json"
git checkout "$REF_MC" -- "$p" "$p.sha256" || { echo "extraction de $p : arrêt"; exit 1; }
echo "ARBRE DE LECTURE MONTE : $ARBRE"
