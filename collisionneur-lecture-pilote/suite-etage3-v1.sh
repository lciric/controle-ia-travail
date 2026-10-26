#!/usr/bin/env bash
# Suite du tour III.1 : III.2 et III.3 par la commande etage3 de l'outil, même dossier (cellules valides sautées),
# plafond 10 USD sur l'ensemble du dossier (R-452). Clés par variable, jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
until grep -q '^fin lecture-pilote' journal-lancement.txt; do sleep 10; done
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" \
  SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-v1/bin/python -I -B collisionneur_v2.py etage3 --sortie run-lecture-pilote-e3t1-v1 \
    --faits faits-aucun-v1.md --question question-lecture-pilote-hypotheses-decisif-collisionneur-v1.md --plafond-usd 10
