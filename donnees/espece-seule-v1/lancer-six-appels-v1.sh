#!/bin/bash
# Six appels « espèce seule » (Argon C sous GO-2026-10-31-08 ; Kimi D sous GO-2026-11-01-04), l'un après l'autre, sur les trois questions
# du 1er novembre (faits de donnees/questions-3-novembre-v1/). session-depot, 1er novembre 2026 ; mot de Lazar « go tout » (R-962).
set -uo pipefail
cd "$(dirname "$0")"
Q=/home/user/controle-ia-travail/donnees/questions-3-novembre-v1
for t in "convergence-v3:question-convergence-defense-unique-v3.md:faits-convergence-v3-v1.md" "selection-generations-v1:question-selection-generations-v1.md:faits-selection-generations-v1.md" "bac-a-sable-v1:question-verification-non-circulaire-v1.md:faits-bac-a-sable-non-circulaire-v1.md"; do
  IFS=: read -r nom q f <<< "$t"
  echo "=== $nom / Argon"; GO_ID=GO-2026-10-31-08 bash lancer-espece-seule-v1.sh C "$Q/$q" "$Q/$f" "sortie-$nom-argon-v1" 3
  echo "=== $nom / Kimi";  GO_ID=GO-2026-11-01-04 bash lancer-espece-seule-v1.sh D "$Q/$q" "$Q/$f" "sortie-$nom-kimi-v1" 1
done
echo "six appels finis"
