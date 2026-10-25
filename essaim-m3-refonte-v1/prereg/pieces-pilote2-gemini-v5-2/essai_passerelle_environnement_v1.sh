#!/usr/bin/env bash
# Essai de la passerelle de sortie sous l'environnement du noyau (pièce du pilote v5.2.1, conv-audit) : un client httpx
# (celui de la bibliothèque `anthropic`) et urllib (celui des appels Gemini du collisionneur) atteignent-ils l'interface
# d'Anthropic sous `env -i` nu (lanceur v3) puis sous la liste du lanceur v4 ? Aucune clé n'est lue ni envoyée : une
# réponse 401 prouve la poignée TLS et la route ; aucun appel payant.
# Usage : bash essai_passerelle_environnement_v1.sh PYTHON_AVEC_HTTPX
PY="$1"
T='import sys, urllib.request, urllib.error
try:
    import httpx
    r = httpx.get("https://api.anthropic.com/v1/models", timeout=30); print("httpx", httpx.__version__, ": statut", r.status_code)
except Exception as e:
    print("httpx : échec :", type(e).__name__, str(e)[:120])
try:
    urllib.request.urlopen("https://api.anthropic.com/v1/models", timeout=30); print("urllib : statut 200")
except urllib.error.HTTPError as e:
    print("urllib : statut", e.code)
except Exception as e:
    print("urllib : échec :", type(e).__name__, str(e)[:120])'
echo "== env -i nu (lanceur v3)"
env -i PATH=/usr/bin:/bin HOME=/root LANG=C.UTF-8 "$PY" -I -c "$T"
echo "== env -i + INFRA_RESEAU du lanceur v4"
ARGS=()
for v in HTTPS_PROXY https_proxy HTTP_PROXY http_proxy NO_PROXY no_proxy SSL_CERT_FILE SSL_CERT_DIR REQUESTS_CA_BUNDLE CURL_CA_BUNDLE GRPC_DEFAULT_SSL_ROOTS_FILE_PATH; do
  [ -n "${!v:-}" ] && ARGS+=("$v=${!v}")
done
printf 'noms passés : '; for a in "${ARGS[@]}"; do printf '%s ' "${a%%=*}"; done; echo
env -i PATH=/usr/bin:/bin HOME=/root LANG=C.UTF-8 "${ARGS[@]}" "$PY" -I -c "$T"
