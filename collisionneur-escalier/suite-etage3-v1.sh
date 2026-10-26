#!/usr/bin/env bash
# Tours III.2 et III.3 du collisionneur v2.5 sur le dossier du tour III.1 (cellules valides sautées ; refus du III.1
# accepté comme absence, jamais relancé), plafond 10 USD sur le dossier (R-455). Clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" \
  SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-v1/bin/python -I -B collisionneur_v2.py etage3 --sortie run-escalier-e3t1-v1 \
    --faits faits-aucun-v1.md --question question-seuil-escalier-cout-collisionneur-v2.md --plafond-usd 10 --accepter-absence E3-T1-conception-B
