#!/usr/bin/env bash
# Contrôle des trois espèces du tour 3 avant dépense ; $1 = GO, $2 = sortie neuve (R12). Clé Anthropic : RR_ANTHROPIC_API_KEY_3. Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente : rien lancé" >&2; exit 2; }
[ -n "${GEMINI_API_KEY:-}" ] || { echo "GEMINI_API_KEY absente : rien lancé" >&2; exit 2; }
cd "$(dirname "$0")"
[ $# -eq 2 ] || { echo "usage : controler-especes-v1.sh GO SORTIE" >&2; exit 2; }
[ ! -e "$2" ] || { echo "$2 existe déjà (R12)" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY" \
  ../venv/bin/python -I -B appel_controle_v5.py collisionneur_v2.py "$2" "$1"
