#!/usr/bin/env bash
# Étage III standard du collisionneur v2.6 — « trancher la recombinaison bisociative » (n° 99), GO-2026-10-26-07 (R-526) ;
# un refus arrête le tour. Clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-recombinaison-e3-v1 ] || { echo "run-recombinaison-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-recombinaison-e3-v1 --faits faits-recombinaison-v1.md \
    --question question-recombinaison-v1.md --plafond-usd 23
