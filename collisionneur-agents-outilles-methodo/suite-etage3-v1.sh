#!/usr/bin/env bash
# Après la cellule d'Opus seul : la même question à tout le collisionneur, III.1 à III.3, même dossier (cellule valide
# sautée ; si Opus a refusé, son absence est acceptée et non relancée), plafond 10 USD (R-470). Clés par variable.
set -uo pipefail; set +x
cd "$(dirname "$0")"
until grep -q '^fin opus' journal-lancement.txt; do sleep 10; done
ABS=(); grep -q 'E3-T1-conception-B.*' run-agents-outilles-methodo-e3t1-v1/etat.md 2>/dev/null && grep -A0 'E3-T1-conception-B' run-agents-outilles-methodo-e3t1-v1/etat.md | grep -qi 'refus' && ABS=(--accepter-absence E3-T1-conception-B)
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" \
  SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-v1/bin/python -I -B collisionneur_v2.py etage3 --sortie run-agents-outilles-methodo-e3t1-v1 \
    --faits faits-aucun-v1.md --question question-interface-calcul-bornee-collisionneur-v1.md --plafond-usd 10 "${ABS[@]}"
