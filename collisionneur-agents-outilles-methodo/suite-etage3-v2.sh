#!/usr/bin/env bash
# Reprise après la porte fermée au III.2 (refus d'Opus, E3-T2-redteam-B) : III.3 entre les réponses valides, absence
# acceptée, cellule non relancée ni reformulée (R-468 (4), R-474) ; même dossier, plafond 10 USD. Clés par variable.
set -uo pipefail; set +x
cd "$(dirname "$0")"
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" \
  SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-v1/bin/python -I -B collisionneur_v2.py etage3 --sortie run-agents-outilles-methodo-e3t1-v1 \
    --faits faits-aucun-v1.md --question question-interface-calcul-bornee-collisionneur-v1.md --plafond-usd 10 \
    --accepter-absence E3-T2-redteam-B
