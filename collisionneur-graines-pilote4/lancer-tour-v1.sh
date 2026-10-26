#!/usr/bin/env bash
# Deux tours (III.1 et III.2) du collisionneur v2.6 par `deux_tours_etage3_v1.py`, question de conv-audit « graines de
# plus pour le pilote 4 » (`question-graines-pilote4-collisionneur-v2.md`, canal/conv-audit-n04, commit c9c8575,
# 79336386…) ; ordre de Lazar du 26 octobre 2026, vers 04:05 UTC, imputé à GO-2026-10-24-07 (R-491) ; part entre les
# deux courses du pilote 4 (après la v6.2.1, avant la v5.3). Clés par variable, jamais affichées :
# Anthropic RR_ANTHROPIC_API_KEY_LUC, Gemini GEMINI_API_KEY_2.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-graines-pilote4-e3t1-v1 ] || { echo "run-graines-pilote4-e3t1-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B deux_tours_etage3_v1.py collisionneur_v2.py etage3 \
    --sortie run-graines-pilote4-e3t1-v1 --faits faits-aucun-graines-v1.md \
    --question question-graines-pilote4-collisionneur-v2.md --plafond-usd 8
