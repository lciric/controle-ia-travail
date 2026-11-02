#!/bin/bash
# Argon seul sur la question de convergence v2 (conv-audit, `08f2b017…`) — lanceur v1 (session-depot, 1er novembre 2026).
# Sous GO-2026-10-31-08 (Argon seul, 3 USD par appel) et le mot direct de Lazar du 1er novembre (R-949). Un appel, plafond 3 USD,
# garde de pire cas dans argon_seul_convergence_v1.py ; clé Gemini par variable sous env -i (GEMINI_API_KEY_2 → GEMINI_API_KEY),
# jamais en argument ni en fichier ; appel de contrôle d'Argon déjà passé à 09:41 UTC (run « boucle moisson », même clé).
# Lancement : GO_ID=GO-2026-10-31-08 bash lancer-argon-convergence-v1.sh
set -uo pipefail; set +x
cd "$(dirname "$0")"
GO_ID="${GO_ID:?GO_ID absent}"
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
grep -q "| $GO_ID |" /home/user/controle-ia-travail/registres/go.md || { echo "$GO_ID absent de registres/go.md" >&2; exit 2; }
sha256sum -c --quiet collisionneur_v7.py.sha256 empreintes-argon-convergence-v1.txt || { echo "empreintes non conformes" >&2; exit 2; }
SORTIE=sortie-argon-convergence-v1
[ ! -e "$SORTIE" ] || { echo "$SORTIE existe déjà (R12)" >&2; exit 2; }
PY=/tmp/claude-0/-home-user-controle-ia-travail/4ff7d1a3-3d12-504e-b550-a8bc2f8510b1/scratchpad/collisionneur-venv/bin/python
code=0
env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=$GO_ID HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" \
  NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
  timeout 1500 "$PY" -I -B argon_seul_convergence_v1.py question-convergence-defense-unique-v2.md faits-convergence-v2-argon-v1.md "$SORTIE" || code=$?
grep -rqF -- "$GEMINI_API_KEY_2" "$SORTIE" 2>/dev/null && echo "ALERTE : clé trouvée dans une sortie" >&2
(cd "$SORTIE" && sha256sum manifeste.json reponse-argon.md prompt.txt > empreintes.sha256) 2>/dev/null
echo "code $code"; exit $code
