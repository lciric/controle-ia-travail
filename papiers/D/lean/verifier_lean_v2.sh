#!/usr/bin/env bash
# Rejoue la vérification mécanique (Lean 4.36.0, Mathlib v4.36.0, cache officiel) des trois fichiers du papier D.
# Prérequis : LEAN_BIN (dossier bin de la chaîne) et MATHLIB (clone de mathlib4 à l'étiquette v4.36.0, `lake exe cache get` fait).
# Durée : quelques minutes (le fichier de la pénalité est le plus long).
set -euo pipefail
LEAN_BIN=${LEAN_BIN:-/opt/lean/lean-4.36.0-linux/bin}
MATHLIB=${MATHLIB:-/opt/lean/mathlib4}
ICI=$(cd "$(dirname "$0")" && pwd)
export PATH="$LEAN_BIN:$PATH"
TMP=$(mktemp -d)
declare -A THM=(
  [Noyau]="ampA_iff domA_iff niche_same_odds niche_inversion_iff variance_identity variance_example covariance_identity offloop_counterexample inloop_counterexample collapse_counterexample iterated_rejection_iff npg_closed_form rft_weights"
  [NoyauPenalite]="share_lt_iff ampB_iff domB_iff r3_gain_neg"
  [Decouplage]="linStep_preserves linear_probe_invariant frozen_row gating_breaks_orthogonality"
)
TOTAL=0; ATTENDU=0
cd "$MATHLIB"
for f in Noyau NoyauPenalite Decouplage; do
  { cat "$ICI/PapierD/$f.lean"; for t in ${THM[$f]}; do echo "#print axioms PapierD.$t"; done; } > "$TMP/$f.lean"
  SORTIE=$(lake env lean "$TMP/$f.lean" 2>&1)
  if echo "$SORTIE" | grep -q "error\|sorryAx"; then echo "$SORTIE"; echo "ÉCHEC dans $f"; exit 1; fi
  N=$(echo "$SORTIE" | grep -c "depends on axioms: \[propext, Classical.choice, Quot.sound\]" || true)
  M=$(echo ${THM[$f]} | wc -w)
  echo "$f : $N théorèmes sur $M avec les seuls axiomes standard"
  TOTAL=$((TOTAL+N)); ATTENDU=$((ATTENDU+M))
done
[ "$TOTAL" -eq "$ATTENDU" ] || { echo "ÉCHEC : $TOTAL sur $ATTENDU"; exit 1; }
echo 'import Mathlib
example : (37 : ℚ) / 50 = 1 / 2 := by norm_num' > "$TMP/Faux.lean"
if lake env lean "$TMP/Faux.lean" >/dev/null 2>&1; then echo "ÉCHEC : le témoin faux est accepté"; exit 1; fi
echo "OK : $TOTAL théorèmes, aucun sorry, témoin faux refusé"
