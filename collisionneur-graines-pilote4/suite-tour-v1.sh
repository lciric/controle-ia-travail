#!/usr/bin/env bash
# Suite du tour « graines » (R-491, R-493) après la porte fermée au III.1 (refus d'Opus, E3-T1-conception-B, consigné tel
# quel, ni relancé ni reformulé, R-495) : le III.2 seul, entre les réponses valides, absence acceptée ; même dossier,
# même plafond (8 USD), GO-2026-10-24-07. Clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B deux_tours_etage3_v1.py collisionneur_v2.py etage3 \
    --sortie run-graines-pilote4-q3-e3t1-v1 --faits faits-aucun-graines-v1.md \
    --question question-graines-pilote4-collisionneur-v3.md --plafond-usd 8 \
    --accepter-absence E3-T1-conception-B
