#!/usr/bin/env bash
# Étage III standard du collisionneur v2.6 — « proposeur enfichable », question v1 de conv-audit, faits v1, GO-2026-10-27-06 (plafond 22 USD, R-561).
# Un refus arrête le tour. Clé Anthropic : RR_ANTHROPIC_API_KEY_LUC, sans en-tête d'espace de travail. Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_LUC:-}" ] || { echo "RR_ANTHROPIC_API_KEY_LUC absente : rien n'est lancé" >&2; exit 2; }
cd "$(dirname "$0")"
[ ! -e run-proposeur-e3-v1 ] || { echo "run-proposeur-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-proposeur-e3-v1 --faits faits-proposeur-enfichable-v1.md \
    --question question-proposeur-enfichable-v1.md --plafond-usd 22
