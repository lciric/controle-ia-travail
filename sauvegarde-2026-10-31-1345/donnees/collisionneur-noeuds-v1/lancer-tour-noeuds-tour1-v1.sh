#!/usr/bin/env bash
# Lancement du tour 1 du collisionneur des nœuds décisionnels — v10
# GO-2026-10-31-06, plafond 22 USD (tour 1), étage 3
# R-831 : refus Fable ou Opus → absence ; refus Argon ou Kimi → arrêt
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
COLLISIONNEUR="$DIR/../collisionneur-texte-III-v1/collisionneur_v7.py"
RELAIS_KIMI="$DIR/../../docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py"
VENV_PYTHON="/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/collisionneur-priorites/venv/bin/python"
PORT_KIMI=8793

cd "$DIR"

# Vérifications
"$VENV_PYTHON" -c "import anthropic" 2>/dev/null || {
  echo "ERREUR : anthropic manquant dans le venv" >&2; exit 1
}
test -f faits-noeuds-v1.md || { echo "ERREUR : faits absents" >&2; exit 1; }
test -f question-noeuds-v10.md || { echo "ERREUR : question v10 absente" >&2; exit 1; }

# Vérification des clés (par nom, jamais par valeur)
for v in RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 KIMI_API_KEY; do
  test -n "${!v:-}" || { echo "ERREUR : $v non définie" >&2; exit 1; }
done

# Relais Kimi
"$VENV_PYTHON" -I -B "$RELAIS_KIMI" \
  --port "$PORT_KIMI" \
  --modeles-permis kimi-k3.1-pro \
  --plafond-usd 4 \
  --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 \
  --max-appels 8 \
  --max-jetons-sortie-pire-cas 65536 \
  --delai-amont-s 1800 --delai-silence-s 600 \
  --journal "$DIR/relais-kimi-noeuds-journal-v1.jsonl" \
  &
RELAIS_PID=$!
sleep 2
kill -0 "$RELAIS_PID" 2>/dev/null || { echo "ERREUR : relais Kimi non démarré" >&2; exit 1; }
echo "relais Kimi démarré : PID $RELAIS_PID, port $PORT_KIMI"

cleanup() {
  echo "relais Kimi arrêté : PID $RELAIS_PID ; code du tour $1"
  kill "$RELAIS_PID" 2>/dev/null || true
  wait "$RELAIS_PID" 2>/dev/null || true
}

# Lancement du collisionneur étage 3
# GO_ID et clés par env -i, pas en arguments
env -i \
  HOME="$HOME" \
  PATH="$PATH" \
  PYTHONPATH="$(cd "$DIR/../.." && pwd)/src" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" \
  GOOGLE_API_KEY="$GEMINI_API_KEY_2" \
  OPENAI_API_KEY="placeholder" \
  OPENAI_BASE_URL="http://127.0.0.1:$PORT_KIMI/v1" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-/etc/ssl/certs/ca-certificates.crt}" \
  REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-/etc/ssl/certs/ca-certificates.crt}" \
  CURL_CA_BUNDLE="${CURL_CA_BUNDLE:-/etc/ssl/certs/ca-certificates.crt}" \
  HTTPS_PROXY="${HTTPS_PROXY:-}" \
  GO_ID="GO-2026-10-31-06" \
  timeout 6900 "$VENV_PYTHON" -I -B "$COLLISIONNEUR" etage3 \
    --sortie run-noeuds-tour1-e3-v1 \
    --faits faits-noeuds-v1.md \
    --question question-noeuds-v10.md \
    --plafond-usd 22
RC=$?

cleanup "$RC"

# Vérification de fuite de clés
for v in RR_ANTHROPIC_API_KEY_3 GEMINI_API_KEY_2 KIMI_API_KEY; do
  if grep -rqF -- "${!v}" run-noeuds-tour1-e3-v1/ 2>/dev/null; then
    echo "ALERTE : fuite de $v dans les sorties" >&2
    exit 99
  fi
done

echo "code $RC"
