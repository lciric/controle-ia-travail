#!/bin/bash
# Amorce d'appel, ligne 1 du bras A, v1 (onstart de Vast, < 2 500 octets) : clone l'entrée (aide d'identification
# inscrite avant l'extraction, R-5101), vérifie le commit et l'empreinte de l'amorce complète, puis l'exécute.
# Erreur avant l'exec : arrêt simple (PUT stopped), jamais de destruction. Aucun secret affiché.
set +x; set -u
export APPEL_DEBUT_S=$(date -u +%s) CLONE_FAIT=1
J=${AMORCE_JOUET:-0}
[ "$J" = 1 ] || [ -z "${RACINE_AMORCE:-}${AMORCE_DEPOT_URL:-}${AMORCE_CURL:-}" ] || X=1
R=${RACINE_AMORCE:-/root}; T=$R/ligne-1-bras-a; E=$T/entree
U=${AMORCE_DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}
B=${BRANCHE_ENTREE:-entree/bras-a-ligne-1-v1}
F=$E/scripts/amorce_ligne_1_bras_a_v2.sh
s() {
 echo "$(date -u +%FT%TZ) APPEL ARRET : $1" | tee -a "$T/journal-appel.txt" 2>/dev/null
 case "${CONTAINER_ID:-}" in ''|*[!0-9]*) exit 2;; esac
 c=$(printf 'header = "Authorization: Bearer %s"\n' "${CONTAINER_API_KEY:-}" | ${AMORCE_CURL:-curl} -K - -sS -m 60 \
  -o /dev/null -w '%{http_code}' -X PUT -H 'Content-Type: application/json' -d '{"state": "stopped"}' \
  "https://console.vast.ai/api/v0/instances/$CONTAINER_ID/" 2>/dev/null)
 echo "$(date -u +%FT%TZ) APPEL : arrêt demandé, HTTP $c" | tee -a "$T/journal-appel.txt" 2>/dev/null
 [ "$J" = 1 ] && exit 3; sleep infinity; }
[ -z "${X:-}" ] || s "variable de jouet hors jouet"
mkdir -p "$T" || s "dossier $T"
for v in GH_TOKEN COMMIT_ENTREE AMORCE_SHA256 CONTAINER_ID CONTAINER_API_KEY; do [ -n "${!v:-}" ] || s "$v absente"; done
case "$CONTAINER_ID" in *[!0-9]*) s "CONTAINER_ID non numérique";; esac
echo "$(date -u +%FT%TZ) APPEL : départ, entrée $B" >> "$T/journal-appel.txt"
A='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ ! -d "$E/.git" ]; then
 git -c credential.helper="$A" clone -q --depth 1 --single-branch --no-checkout --branch "$B" "$U" "$E" \
  > "$T/clone-appel.txt" 2>&1 || s "clone"
 git -C "$E" config credential.helper "$A" || s "aide d'identification"
 git -C "$E" checkout -q "$B" >> "$T/clone-appel.txt" 2>&1 || s "extraction"
fi
[ "$(git -C "$E" rev-parse HEAD 2>/dev/null)" = "$COMMIT_ENTREE" ] || s "commit cloné différent de COMMIT_ENTREE"
[ -f "$F" ] && [ "$(sha256sum < "$F" | cut -c1-64)" = "$AMORCE_SHA256" ] || s "empreinte de l'amorce complète"
echo "$(date -u +%FT%TZ) APPEL : commit et amorce conformes, exec" >> "$T/journal-appel.txt"
exec bash "$F"
