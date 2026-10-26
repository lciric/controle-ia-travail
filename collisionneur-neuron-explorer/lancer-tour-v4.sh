#!/usr/bin/env bash
# Trois tours (III.1 à III.3) du collisionneur v2.6 (en-tête d’espace de travail), question de conv-audit « neuron explorer, intégration »
# (2ba899dd…, R-478, GO-2026-10-26-01 ; ordre de Lazar du 26 octobre 2026, vers 01:58 UTC). Clés par variable, jamais
# affichées : Anthropic RR_ANTHROPIC_API_KEY_LUC (GO-2026-10-24-04, extension R-411 ; mot de Lazar du 26 octobre : « utilise luc »), Gemini GEMINI_API_KEY (« à défaut »,
# GO-2026-10-24-07) : les clés n° 3 et Gemini n° 2 ne sont pas dans l'environnement de cette session.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ ! -e run-neuron-explorer-e3t1-v4 ] || { echo "run-neuron-explorer-e3t1-v4 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B collisionneur_v2.py etage3 --sortie run-neuron-explorer-e3t1-v4 \
    --faits faits-aucun-v1.md --question question-neuron-explorer-integration-collisionneur-v1.md --plafond-usd 10
