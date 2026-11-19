#!/bin/bash
# § 5.4 — état « écrit » : sorties portées, ligne LECTURE-BBIS, journal
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.4 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-4-sorties-portees-et-ligne-de-lecture.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : écrit$' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « écrit » : arrêt"; exit 1; }
[ -e "$LV1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt.sha256" ] || { echo "constat de forme pour le juge non écrit : arrêt"; exit 1; }
cd "$DEPOT" || exit 1
neuf "runs/$RUNL"; neuf "diag/$RUNL"; mkdir -p "runs/$RUNL" "diag/$RUNL"
for f in "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json"; do
  cp "$ARBRE/$f" "$f" && cp "$ARBRE/$f.sha256" "$f.sha256" || { echo "copie de $f : arrêt"; exit 1; }
  cmp -s "$ARBRE/$f" "$f" || { echo "copie de $f différente : arrêt"; exit 1; }
done
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json" || { echo "sceau des sorties : arrêt"; exit 1; }
# journal : celui de l'arbre de lecture est celui de l'arbre principal plus une ligne
[ "$(wc -l < "$JOURNAL" | tr -d ' ')" = 1 ] && [ "$(wc -l < "$ARBRE/$JOURNAL" | tr -d ' ')" = 2 ] && [ "$(head -n 1 "$ARBRE/$JOURNAL")" = "$(cat "$JOURNAL")" ] || { echo "journal : état inattendu : arrêt"; exit 1; }
tail -n 1 "$ARBRE/$JOURNAL" >> "$JOURNAL"
# ligne LECTURE-BBIS, par la fonction du code
PYTHONPATH=src "$PY" - "$RUNL" <<'EOF'
import sys, time
from pathlib import Path
from controle_ia.scellement import empreinte
from controle_ia.t07bbis.registre_bbis_v2 import REGISTRE_PROPRE, ajouter_ligne_propre
chemin = f"diag/{sys.argv[1]}/lecture-bbis.json"
print(ajouter_ligne_propre(Path("."), REGISTRE_PROPRE, "LECTURE-BBIS", int(time.time()), chemin, empreinte(chemin)))
EOF
tail -n 1 "$JOURNAL" | cut -c1-200
git status --porcelain --untracked-files=all
