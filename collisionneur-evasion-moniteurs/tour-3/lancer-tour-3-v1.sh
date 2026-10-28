#!/usr/bin/env bash
# Étage III, tour 3 du collisionneur « évasion et moniteurs » ; plafond 33 USD. Un refus arrête ce tour (consigné tel quel). Clé Anthropic : RR_ANTHROPIC_API_KEY_3 ; Gemini : GEMINI_API_KEY. Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente : rien lancé" >&2; exit 2; }
[ -n "${GEMINI_API_KEY:-}" ] || { echo "GEMINI_API_KEY absente : rien lancé" >&2; exit 2; }
cd "$(dirname "$0")"
[ ! -e run-tour-3-e3-v1 ] || { echo "run-tour-3-e3-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-tour-3-e3-v1 --faits faits-evasion-moniteurs-v1.md \
    --question question-evasion-moniteurs-v1.md --plafond-usd 33
