#!/usr/bin/env bash
# Suite du tour « audit défensif » : le III.3 (riposte), même dossier, reprise des six cellules valides (sautées par
# l'outil) ; plafond levé par Lazar (« pas de limite de plafond », R-512, extension de GO-2026-10-26-04) ; valeur
# technique 100 USD. Clés par variable, jamais affichées : RR_ANTHROPIC_API_KEY_LUC, GEMINI_API_KEY_2.
set -uo pipefail; set +x
cd "$(dirname "$0")"
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  /opt/essaim-m3-venv-pilote2-v1/bin/python -I -B tour_audit_defensif_v1.py collisionneur_v2.py etage3 \
    --sortie run-audit-controle-e3-v1 --faits faits-audit-controle-v1.md \
    --question question-audit-controle-collisionneur-v1.md --plafond-usd 100
