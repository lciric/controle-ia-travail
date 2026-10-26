#!/usr/bin/env bash
# Étage III du collisionneur v2.6, tour III.2 défensif (`tour_audit_defensif_v1.py`), question « audit défensif du
# programme » (`question-audit-controle-collisionneur-v1.md`, ff7806a9…), faits `faits-audit-controle-v1.md`
# (574c6b76…) ; GO-2026-10-26-04 (mot direct de Lazar, 26 octobre 2026, vers 11:13 UTC, R-509). Clés par variable,
# jamais affichées : Anthropic RR_ANTHROPIC_API_KEY_LUC, Gemini GEMINI_API_KEY_2.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-audit-controle-e3-v1 ] || { echo "run-audit-controle-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B tour_audit_defensif_v1.py collisionneur_v2.py etage3 \
    --sortie run-audit-controle-e3-v1 --faits faits-audit-controle-v1.md \
    --question question-audit-controle-collisionneur-v1.md --plafond-usd 10
