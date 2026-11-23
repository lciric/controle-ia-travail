[ -n "${BASH_VERSION:-}" ] || exec bash "$0" "$@"
set +x; set -u
export APPEL_DEBUT_S=$(date -u +%s) CLONE_FAIT=1 GIT_TERMINAL_PROMPT=0
J=${AMORCE_JOUET:-0}; C=${AMORCE_CURL:-curl}
[ "$J" = 1 ] || [ -z "${RACINE_AMORCE:-}${AMORCE_DEPOT_URL:-}${AMORCE_CURL:-}" ] || X=1
T=${RACINE_AMORCE:-/root}/ligne-1-bras-a; E=$T/entree; F=$E/scripts/amorce_ligne_1_bras_a_v3.sh
B=${BRANCHE_ENTREE:-entree/bras-a-ligne-1-v1}
export Q=https://console.vast.ai/api/v0/instances/${CONTAINER_ID:-x}/
l() { echo "$(date -u +%FT%TZ) APPEL $1" | tee -a $T/journal-appel.txt 2>/dev/null; }
p() { if command -v $C >/dev/null; then printf 'header = "Authorization: Bearer %s"\n' "${CONTAINER_API_KEY:-}" |
 timeout 90 $C -K - -s -m 60 -o /dev/null -w '%{http_code}' -X PUT -H Content-Type:application/json -d '{"state": "stopped"}' $Q 2>/dev/null
 else python3 -Ic 'import os,urllib.request as u
try:print(u.urlopen(u.Request(os.environ["Q"],b"{\"state\": \"stopped\"}",{"Authorization":"Bearer "+os.environ["CONTAINER_API_KEY"]},method="PUT"),timeout=60).status)
except Exception as e:print(getattr(e,"code",0))'; fi; }
s() { l "ARRET : $1"; case "${CONTAINER_ID:-}" in ''|*[!0-9]*) exit 2;; esac
 n=0; while :; do n=$((n+1)); c=$(p); l "PUT $n : $c"
  [ "$J" = 1 ] && { case "$c" in 2??) exit 3;; esac; [ $n -ge 3 ] && exit 4; }
  sleep $(( (n < 10 ? n : 10) * ${AMORCE_PAS_S:-60} )); done; }
[ -z "${X:-}" ] || s jouet
mkdir -p $T || s dossier
[ "$J" = 1 ] || { command -v git && command -v curl || { apt-get update -qq &&
 DEBIAN_FRONTEND=noninteractive apt-get install -y -qq git curl ca-certificates; }; } >/dev/null 2>&1
command -v git >/dev/null || s git
for v in GH_TOKEN COMMIT_ENTREE AMORCE_SHA256 CONTAINER_ID CONTAINER_API_KEY; do [ -n "${!v:-}" ] || s "$v absente"; done
case $CONTAINER_ID in *[!0-9]*) s "CONTAINER_ID";; esac
A='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ ! -d $E/.git ]; then
 timeout 900 git -c credential.helper= -c credential.helper="$A" clone -q --depth 1 --no-checkout \
  --branch $B ${AMORCE_DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git} $E > $T/clone-appel.txt 2>&1 || s clone
 git -C $E config credential.helper '' && git -C $E config --add credential.helper "$A" || s aide
 git -C $E checkout $B >> $T/clone-appel.txt 2>&1 || s extraction
fi
[ "$(git -C $E rev-parse HEAD)" = "$COMMIT_ENTREE" ] || s "commit différent"
[ -f $F ] && [ "$(sha256sum < $F | cut -c1-64)" = "$AMORCE_SHA256" ] || s empreinte
exec bash $F
