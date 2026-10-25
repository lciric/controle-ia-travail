#!/usr/bin/env bash
# Tour III.1 du collisionneur v2.5, question « allocation d'un budget » (R-389, GO-2026-10-24-07), environnement minimal :
# mandataire et certificats gardés ; clés passées par variable, jamais affichées ni écrites ; ANTHROPIC_BASE_URL absente.
set -euo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-allocation-e3t1-v1 ] || { echo "run-allocation-e3t1-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" \
  SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY" ANTHROPIC_CUSTOM_HEADERS="anthropic-workspace-id: $RR_ANTHROPIC_WORKSPACE_ID" \
  GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-v1/bin/python -I -B tour_unique_etage3_v1.py collisionneur_v2.py run-allocation-e3t1-v1 \
    faits-aucun-v1.md question-allocation-budget-classes-parametres-v1.md 10
