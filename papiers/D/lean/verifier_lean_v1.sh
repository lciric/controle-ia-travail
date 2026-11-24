#!/usr/bin/env bash
# Rejoue la vérification mécanique du noyau (Lean 4.36.0, Mathlib v4.36.0, cache officiel).
# Prérequis : LEAN_BIN (dossier bin de la chaîne) et MATHLIB (clone de mathlib4 à l'étiquette v4.36.0, `lake exe cache get` fait).
set -euo pipefail
LEAN_BIN=${LEAN_BIN:-/opt/lean/lean-4.36.0-linux/bin}
MATHLIB=${MATHLIB:-/opt/lean/mathlib4}
ICI=$(cd "$(dirname "$0")" && pwd)
export PATH="$LEAN_BIN:$PATH"
TMP=$(mktemp -d)
{ cat "$ICI/PapierD/Noyau.lean"
  for t in ampA_iff domA_iff niche_same_odds niche_inversion_iff variance_identity variance_example \
           covariance_identity offloop_counterexample inloop_counterexample collapse_counterexample \
           iterated_rejection_iff npg_closed_form rft_weights; do echo "#print axioms PapierD.$t"; done; } > "$TMP/Verif.lean"
cd "$MATHLIB"
SORTIE=$(lake env lean "$TMP/Verif.lean" 2>&1)
echo "$SORTIE"
if echo "$SORTIE" | grep -q "error\|sorryAx"; then echo "ÉCHEC"; exit 1; fi
N=$(echo "$SORTIE" | grep -c "depends on axioms: \[propext, Classical.choice, Quot.sound\]")
[ "$N" -eq 13 ] || { echo "ÉCHEC : $N théorèmes sur 13 avec les seuls axiomes standard"; exit 1; }
# garde témoin : un énoncé faux doit être refusé
echo 'import Mathlib
example : (37 : ℚ) / 50 = 1 / 2 := by norm_num' > "$TMP/Faux.lean"
if lake env lean "$TMP/Faux.lean" >/dev/null 2>&1; then echo "ÉCHEC : le témoin faux est accepté"; exit 1; fi
echo "OK : 13 théorèmes, aucun sorry, témoin faux refusé"
