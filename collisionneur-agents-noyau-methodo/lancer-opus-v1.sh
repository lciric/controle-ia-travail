#!/usr/bin/env bash
# Opus seul (cellule B du III.1), question distincte « conception itérative, plan statistique » (R-472, GO-2026-10-24-07) ;
# clé Anthropic n° 3 (la clé Gemini est passée parce que l'outil la lit à l'amorçage) ; jamais affichées.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-agents-noyau-methodo-e3t1-v1 ] || { echo "run-agents-noyau-methodo-e3t1-v1 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" \
  SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-v1/bin/python -I -B tour_une_cellule_etage3_v1.py collisionneur_v2.py run-agents-noyau-methodo-e3t1-v1 \
    faits-aucun-v1.md question-conception-iterative-statistique-collisionneur-v1.md 3 B
