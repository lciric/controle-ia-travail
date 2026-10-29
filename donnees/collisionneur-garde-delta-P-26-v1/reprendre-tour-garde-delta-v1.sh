#!/bin/bash
# Reprise du run run-garde-delta-e3-v1 au plafond relevé à 25 USD (GO-2026-10-29-06 étendu, mot de Lazar « non releve le plfond »,
# 2026-10-29 ≈ 07:01 UTC), seulement si le premier passage s'est arrêté sur le plafond (code 4) ; les cellules valides sont gardées.
# Clés passées par variable sous env -i ; jamais en argument ni en fichier. Un refus de modèle arrête le tour (R-609).
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ -d run-garde-delta-e3-v1 ] || { echo "run-garde-delta-e3-v1 absent" >&2; exit 2; }
sha256sum -c question-garde-delta-P-26-v1.md.sha256 faits-garde-delta-P-26-v1.md.sha256 collisionneur_v2.py.sha256 >/dev/null || { echo "empreintes non conformes" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=GO-2026-10-29-06 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  timeout 10800 ../../collisionneur-priorites/venv/bin/python -I -B collisionneur_v2.py etage3 \
    --sortie run-garde-delta-e3-v1 --faits faits-garde-delta-P-26-v1.md --question question-garde-delta-P-26-v1.md --plafond-usd 25
