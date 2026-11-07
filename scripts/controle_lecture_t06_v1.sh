#!/usr/bin/env bash
# Contrôle d'ouverture de la lecture des sondes de T0.6 (R-1654). Refuse (code 2) sans les deux lignes de registre (scellement de T0.7 et
# de P3-bis), sans leurs sceaux vérifiés, ou sans leur antériorité sur l'ouverture ; voir `scripts/controle_lecture_t06_v1.py`.
# Ne lit jamais le contenu du résultat des sondes. À lancer AVANT toute ouverture de `lecture-sondes-t06` :
#   bash scripts/controle_lecture_t06_v1.sh REGISTRE RESULTAT_SONDES [RACINE]
# Code 0 : « OUVERTURE AUTORISÉE » et une ligne ajoutée à `<REGISTRE>.ouvertures.md` ; code 2 : « REFUS : motif », rien n'est ouvert.
set -uo pipefail
DEPOT="$(cd "$(dirname "$0")/.." && pwd)"
[ "$#" -ge 2 ] && [ "$#" -le 3 ] || { echo "usage : controle_lecture_t06_v1.sh REGISTRE RESULTAT_SONDES [RACINE]" >&2; exit 2; }
exec python3 -I -B "$DEPOT/scripts/controle_lecture_t06_v1.py" "$@"
