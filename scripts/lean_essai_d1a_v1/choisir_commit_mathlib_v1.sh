#!/usr/bin/env bash
# choisir_commit_mathlib_v1.sh — essai Lean, D-1a, v1. Lecture seule de dépôt public : dernière étiquette stable de Mathlib
# (vX.Y.Z, sans « -rc ») et son commit. Le commit choisi est ensuite **épinglé** : il est passé tel quel à
# installer_chaine_v1.sh, consigné au rapport (pièce COMMIT-MATHLIB) et jamais changé sans nouvelle version du préenregistrement.
set -euo pipefail
DEPOT=https://github.com/leanprover-community/mathlib4.git
ligne=$(git ls-remote --tags --refs "$DEPOT" 'refs/tags/v4.*' \
  | awk '{sub("refs/tags/","",$2); print $2" "$1}' | grep -E '^v4\.[0-9]+\.[0-9]+ ' | sort -V | tail -1)
[ -n "$ligne" ] || { echo "aucune étiquette stable trouvée" >&2; exit 2; }
echo "etiquette=${ligne%% *} commit=${ligne##* }"
