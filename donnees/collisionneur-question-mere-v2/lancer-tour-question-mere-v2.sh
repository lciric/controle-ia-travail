#!/bin/bash
# Tour du collisionneur « question-mère v3 de la course d'idéation » (GO-2026-10-29-15, plafond 30 USD pour les deux runs ; run v2, plafond 23 USD, 6,27 USD déjà dépensés au run v1 ; question-mère v3 sans l axe 6, R-750), étage III « arbitre », trois modèles, trois tours.
# Appel de contrôle (trois espèces) puis tour. Clés passées par variable sous env -i (RR_ANTHROPIC_API_KEY_3 sans en-tête
# d'espace de travail, GEMINI_API_KEY_2) ; jamais en argument ni en fichier. Un refus arrête le tour (code 2) ; la relance suit R-750 (question plus technique, nouveau run).
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ ! -e run-question-mere-e3-v2 ] || { echo "run-question-mere-e3-v2 existe déjà (R12)" >&2; exit 2; }
sha256sum -c question-question-mere-v2.md.sha256 faits-question-mere-v2.md.sha256 collisionneur_v3.py.sha256 appel_controle_v6.py.sha256 >/dev/null || { echo "empreintes non conformes" >&2; exit 2; }
ENVI=(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=GO-2026-10-29-15
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}"
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}"
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2")
PY=../../collisionneur-priorites/venv/bin/python
"${ENVI[@]}" timeout 300 $PY -I -B appel_controle_v6.py collisionneur_v3.py controle-question-mere-v2.json GO-2026-10-29-15 || { echo "appel de contrôle en échec" >&2; exit 2; }
grep -q '"ECHEC"' controle-question-mere-v2.json && { echo "une espèce en échec au contrôle" >&2; exit 2; }
exec "${ENVI[@]}" timeout 10800 $PY -I -B collisionneur_v3.py etage3 \
    --sortie run-question-mere-e3-v2 --faits faits-question-mere-v2.md \
    --question question-question-mere-v2.md --plafond-usd 23
