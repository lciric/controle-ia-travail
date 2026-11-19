#!/bin/bash
# § 5.1 — lancement détaché du module de lecture
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.1 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-1-lancement.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"
grep -q "CONCLUSION : conforme" "$T/releve-avant-lancement-$N.txt" || { echo "relevé d'avant lancement non conforme : ON NE LANCE PAS"; exit 1; }
RUNL="$(cat "$T/run-lecture-$N.txt")"
SORTIE="$T/sortie-lancement-$N.txt"; neuf "$SORTIE"; neuf "$T/lancement-$N.pid"; neuf "$T/lancement-$N.code"
L="$T/lancement-$N.sh"; neuf "$L"
cat > "$L" <<EOF
#!/bin/bash
# Lancement n° $N de la lecture de l'étape B bis — écrit par la commande de lecture, valeurs développées
cd "$ARBRE" || exit 1
${NETTOYE[*]} OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONPATH="$ARBRE/src" "$PY" -m controle_ia.t07bbis.lecture_v5 --racine "$ARBRE" --run-7b "$RUN_7B" --run-bbis "$RUN_BBIS" --run-lecture "$RUNL" > "$SORTIE" 2>&1 &
echo \$! > "$T/lancement-$N.pid"
wait \$!
echo \$? > "$T/lancement-$N.code"
date -u +%Y-%m-%dT%H:%M:%SZ > "$T/lancement-$N.fin"
EOF
date -u +%Y-%m-%dT%H:%M:%SZ > "$T/lancement-$N.debut"
command -v setsid > /dev/null || { echo "utilitaire de détachement absent : ON NE LANCE PAS"; exit 1; }
setsid -f nohup bash "$L" < /dev/null > /dev/null 2>&1
echo "lancement détaché ; l'identifiant du processus est relevé par le § 5.1 bis"
