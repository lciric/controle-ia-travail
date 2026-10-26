#!/usr/bin/env bash
# Étage III standard du collisionneur v2.6 sur la question « pôle scientifique automatique » (n° 94 de conv-audit),
# GO-2026-10-26-06 (R-524) ; un refus arrête le tour (porte fermée). Clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-pole-scientifique-e3-v1 ] || { echo "run-pole-scientifique-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-pole-scientifique-e3-v1 --faits faits-pole-scientifique-v1.md \
    --question question-pole-scientifique-v1.md --plafond-usd 25
