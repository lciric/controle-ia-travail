#!/usr/bin/env bash
# Trois tours (III.1 à III.3) du collisionneur v2.5, question de conv-audit « littérature des boucles proposer, tester, éliminer, itérer »
# (962130b7…, R-475, GO-2026-10-24-07) ; clé Anthropic n° 3, Gemini n° 2 ; clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-litterature-boucles-e3t1-v1 ] || { echo "run-litterature-boucles-e3t1-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" \
  SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-v1/bin/python -I -B collisionneur_v2.py etage3 --sortie run-litterature-boucles-e3t1-v1 \
    --faits faits-aucun-v1.md --question question-litterature-boucles-agents-collisionneur-v1.md --plafond-usd 10
