#!/usr/bin/env bash
# Lanceur de la pièce « lecteur du texte » de la course de dose–réponse de l'organisme à consigne cachée, v1 (nom neuf,
# R12 ; copie adaptée de scripts/lancer_mots_et_cout_t06_v3.sh, qui reste tel quel ; seule différence : le module joué).
#
#   scripts/lancer_lecteur_texte_dose_reponse_v1.sh --mode reel [--racine-entrees E] [--registre REG] RUN_LANCEMENT RUN_LECTURE
#
# Joue, depuis la racine du dépôt qui porte ce lanceur, `python -P -B scripts/lecteur_texte_dose_reponse_v1.py executer
# --racine <dépôt> ...` avec PYTHONPATH=<dépôt>/src seul : -P n'ajoute pas scripts/ au chemin d'import, -B n'écrit aucun
# fichier .pyc. L'interpréteur est celui de $PY (défaut : python3) ; il doit porter numpy, scipy et torch. Aucune valeur
# n'est imprimée : la pièce n'écrit sur la sortie que les chemins et empreintes de ses fichiers ; code de sortie de la pièce
# rendu tel quel (0 écrit et scellé ; 2 refus, rien d'écrit ; 3 arrêt après le manifeste, fichier d'arrêt seul).
set -euo pipefail
ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEPOT="$(git -C "$ICI" rev-parse --show-toplevel)"
PY="${PY:-python3}"
case " $* " in
  *" --racine "*|*" --racine="*) echo "REFUS : --racine est posé par le lanceur (racine = dépôt du lanceur, $DEPOT)" >&2; exit 2;;
esac
cd "$DEPOT"
# un seul fil pour l'algèbre linéaire : sommes dans un ordre fixe (reproductibilité ; la pièce l'exige en mode réel)
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
PYTHONPATH="$DEPOT/src" exec "$PY" -P -B "$DEPOT/scripts/lecteur_texte_dose_reponse_v1.py" executer --racine "$DEPOT" "$@"
