#!/usr/bin/env bash
# Étage III standard du collisionneur v2.6 — « mesures fortes », question v1 de conv-audit, faits v1, GO-2026-10-27-12 (plafond 30 USD, mot direct de Lazar, R-592).
# Un refus arrête le tour. Clé Anthropic : RR_ANTHROPIC_API_KEY_LUC, sans en-tête d'espace de travail. Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_LUC:-}" ] || { echo "RR_ANTHROPIC_API_KEY_LUC absente : rien n'est lancé" >&2; exit 2; }
cd "$(dirname "$0")"
[ ! -e run-mesures-fortes-e3-v1 ] || { echo "run-mesures-fortes-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-mesures-fortes-e3-v1 --faits faits-mesures-fortes-v1.md \
    --question question-mesures-fortes-v1.md --plafond-usd 30
