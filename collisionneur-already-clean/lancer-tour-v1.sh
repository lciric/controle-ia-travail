#!/usr/bin/env bash
# Trois tours (III.1 à III.3) du collisionneur v2.6, question de conv-audit « Neural Networks Are Already Clean »
# (`question-already-clean-collisionneur-v1.md`, canal/conv-audit-n04, commit d5546aa, 252f4922… ; ordre de Lazar du
# 26 octobre 2026, vers 02:41 UTC, imputé à GO-2026-10-24-07, R-483). Clés par variable, jamais affichées :
# Anthropic RR_ANTHROPIC_API_KEY_LUC (GO-2026-10-24-04, extension R-411 ; « utilise luc »), Gemini GEMINI_API_KEY_2.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-already-clean-e3t1-v1 ] || { echo "run-already-clean-e3t1-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B collisionneur_v2.py etage3 --sortie run-already-clean-e3t1-v1 \
    --faits faits-aucun-already-clean-v1.md --question question-already-clean-collisionneur-v1.md --plafond-usd 10
