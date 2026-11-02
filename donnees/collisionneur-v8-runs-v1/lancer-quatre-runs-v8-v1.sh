#!/bin/bash
# Quatre runs du collisionneur v8 (cinq espèces), l'un après l'autre (session-depot, 1er novembre 2026, GO-2026-11-01-05 à -08, R-964).
set -uo pipefail
cd "$(dirname "$0")"
echo "=== n12-n13-tour2"; (cd n12-n13-tour2 && GO_ID=GO-2026-11-01-05 bash lancer-tour-n12-n13-tour2-v8-v1.sh > journal-n12-n13-tour2-v8-v1.log 2>&1; echo "code final $?" >> journal-n12-n13-tour2-v8-v1.log; tail -2 journal-n12-n13-tour2-v8-v1.log)
echo "=== convergence-v3"; (cd convergence-v3 && GO_ID=GO-2026-11-01-06 bash lancer-tour-convergence-v3-v8-v1.sh > journal-convergence-v3-v8-v1.log 2>&1; echo "code final $?" >> journal-convergence-v3-v8-v1.log; tail -2 journal-convergence-v3-v8-v1.log)
echo "=== selection-generations-v1"; (cd selection-generations-v1 && GO_ID=GO-2026-11-01-07 bash lancer-tour-selection-generations-v1-v8-v1.sh > journal-selection-generations-v1-v8-v1.log 2>&1; echo "code final $?" >> journal-selection-generations-v1-v8-v1.log; tail -2 journal-selection-generations-v1-v8-v1.log)
echo "=== bac-a-sable-v1"; (cd bac-a-sable-v1 && GO_ID=GO-2026-11-01-08 bash lancer-tour-bac-a-sable-v1-v8-v1.sh > journal-bac-a-sable-v1-v8-v1.log 2>&1; echo "code final $?" >> journal-bac-a-sable-v1-v8-v1.log; tail -2 journal-bac-a-sable-v1-v8-v1.log)
echo "quatre runs finis"
