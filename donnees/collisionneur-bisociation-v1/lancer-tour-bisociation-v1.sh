#!/bin/bash
# Tour du collisionneur « recombinaison bisociative à deux espaces » (question conv-audit n° 217, `73a30ab7…`), étage III « arbitre »,
# trois modèles, trois tours. GO-2026-10-29-19 (mot direct de Lazar, ≈ 22:30 UTC) ; dépense demandée par Lazar (mot relayé, conv-audit R-514).
# Plafond 25 USD (devis hors ligne de l'étage III : 20,59 USD au pire cas sans relance). Appel de contrôle (trois espèces) puis tour.
# Clés passées par variable sous env -i (RR_ANTHROPIC_API_KEY_3 sans en-tête d'espace de travail, GEMINI_API_KEY_2) ; jamais en argument
# ni en fichier. Un refus arrête le tour (code 2) ; la relance suit R-750 (question plus étroite, nouveau run).
# Python : le venv du collisionneur (anthropic 2.3.0) ; /usr/bin/python3 n'a pas le paquet `anthropic`, que collisionneur_v3.py importe.
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ ! -e run-bisociation-e3-v1 ] || { echo "run-bisociation-e3-v1 existe déjà (R12)" >&2; exit 2; }
[ ! -e controle-bisociation-v1.json ] || { echo "controle-bisociation-v1.json existe déjà (R12)" >&2; exit 2; }
sha256sum -c question-bisociation-deux-espaces-v1.md.sha256 faits-bisociation-v1.md.sha256 collisionneur_v3.py.sha256 appel_controle_v6.py.sha256 >/dev/null || { echo "empreintes non conformes" >&2; exit 2; }
PY=/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/collisionneur-priorites/venv/bin/python
[ -x "$PY" ] && "$PY" -I -c "import anthropic" 2>/dev/null || { echo "python du collisionneur absent ou sans anthropic" >&2; exit 2; }
ENVI=(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=GO-2026-10-29-19
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}"
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}"
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2")
"${ENVI[@]}" timeout 300 "$PY" -I -B appel_controle_v6.py collisionneur_v3.py controle-bisociation-v1.json GO-2026-10-29-19 || { echo "appel de contrôle en échec" >&2; exit 2; }
grep -q '"ECHEC"' controle-bisociation-v1.json && { echo "une espèce en échec au contrôle" >&2; exit 2; }
exec "${ENVI[@]}" timeout 10800 "$PY" -I -B collisionneur_v3.py etage3 \
    --sortie run-bisociation-e3-v1 --faits faits-bisociation-v1.md \
    --question question-bisociation-deux-espaces-v1.md --plafond-usd 25
