#!/usr/bin/env bash
# Appel de contrôle des trois espèces (A Fable, B Opus 5.5, C Argon) avant le tour « pilier attaque »
# (collisionneur v2.6, étage III). Copie de controler-especes-luc-v1.sh (R12), seul l'interpréteur change
# (venv principal du dépôt, `anthropic` installé). $1 = GO, $2 = sortie neuve (R12).
# Clés : ANTHROPIC_API_KEY <- RR_ANTHROPIC_API_KEY_LUC (mot de Lazar, R-547) ; GEMINI_API_KEY <- GEMINI_API_KEY
# (jamais GEMINI_API_KEY_2, réservée à l'étiqueteur, R-1754). Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_LUC:-}" ] || { echo "RR_ANTHROPIC_API_KEY_LUC absente de cette session : rien n'est lancé" >&2; exit 2; }
[ -n "${GEMINI_API_KEY:-}" ] || { echo "GEMINI_API_KEY absente de cette session : rien n'est lancé" >&2; exit 2; }
cd "$(dirname "$0")"
[ $# -eq 2 ] || { echo "usage : controler-especes-pilier-attaque-v1.sh GO SORTIE" >&2; exit 2; }
[ ! -e "$2" ] || { echo "$2 existe déjà (R12)" >&2; exit 2; }
PYBIN=/home/user/controle-ia-travail/.venv/bin/python
[ -x "$PYBIN" ] || { echo "interpréteur $PYBIN absent" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY" \
  "$PYBIN" -I -B appel_controle_v5.py collisionneur_v2.py "$2" "$1"
