#!/usr/bin/env bash
# Amorce de la machine du crible (v), v1 (docs/procedures/crible-v-v1/, procédure du même dossier). Passée compressée (gzip -9 -n)
# puis en base64 dans la ligne de création imprimée par session_crible_v_v1.py (`commande`). Modèles : l'amorce v2 du pilote MR-2
# sans ssh (`amorce_pilote_mr2_v74_v2.sh`) et l'amorce v2 du jeu de l'idée 1.1 (reprise de la poussée), lues, non modifiées.
# Ordre : 0. arguments (essai local : arguments seulement, sortie 0 avant tout réseau et toute écriture) ; 1. marque de lancement
#   (une relance du conteneur par le loueur ne refait rien : arrêt (A) poussé par le programme machine) ; 2. minuterie armée
#   AVANT toute passe : à l'échéance, destruction de la machine par son identifiant (DELETE redemandé chaque minute, « stopped »
#   après la cinquième demande ; jamais jugé par un code) ; 3. outils ; 4. dépôt partiel au commit du code (programme machine, code
#   du crible, fiche de lancement, texte, addendum) ; programme machine à son empreinte écrite ici et à son compagnon ; 5. la main
#   passe au programme machine (exec, même PID ; la minuterie reste son enfant).
# Variables (--env) : COMMIT_CODE, COMMIT_LOT, ECHEANCE_UTC_S, FICHE_SHA256, GO_KV1, GO_KV2, BR_SORTIE, BR_ENTREE, et par leur nom
#   GH_TOKEN, RR_ANTHROPIC_API_KEY_RIGAUD, GEMINI_API_KEY, OPENAI_API_KEY ; posées par le loueur : CONTAINER_ID, CONTAINER_API_KEY.
#   Aucune valeur de clé n'est jamais affichée ni écrite.
# AMORCE_ESSAI_LOCAL=1 : arguments seulement. AMORCE_REPETITION=1 (répétition locale) : dépôt jouet file:///, loueur simulé
#   (CURL_REPETITION), racine et durées données ; refusées hors répétition.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"; REP="${AMORCE_REPETITION:-0}"
if [ "$REP" != 1 ]; then for v in RACINE_AMORCE DEPOT_URL_REPETITION CURL_REPETITION DUREES_REPETITION PY_REPETITION; do
    [ -z "${!v:-}" ] || { echo "CRIBLEV AMORCE REFUS : $v en répétition seulement"; exit 2; }; done; fi
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
API=https://console.vast.ai/api/v0
SHA_MACHINE=a48da4b91fa0a42436348cf472f70834a7ab4dfe03bac051f7d30091c91e34b4
MACHINE_REL=docs/procedures/crible-v-v1/machine_crible_v_v1.py
ECH_MIN=60600; ECH_MAX=61500; PAS=30
URL="$DEPOT_URL_OFFICIEL"; CURL=curl; PY=python3
if [ "$REP" = 1 ]; then
    URL="${DEPOT_URL_REPETITION:-}"; CURL="${CURL_REPETITION:-}"; PY="${PY_REPETITION:-python3}"
    case "$URL" in file:///*) ;; *) echo "CRIBLEV AMORCE REFUS : répétition : dépôt jouet file:/// exigé"; exit 2;; esac
    [ -x "$CURL" ] || { echo "CRIBLEV AMORCE REFUS : répétition : loueur simulé exigé"; exit 2; }
    read -r ECH_MIN ECH_MAX PAS <<< "${DUREES_REPETITION:-}"
fi
# 0. arguments
for v in COMMIT_CODE COMMIT_LOT ECHEANCE_UTC_S FICHE_SHA256 GO_KV1 GO_KV2 BR_SORTIE BR_ENTREE; do
    [ -n "${!v:-}" ] || { echo "CRIBLEV AMORCE REFUS : variable $v absente"; exit 2; }; done
for v in COMMIT_CODE COMMIT_LOT; do printf '%s' "${!v}" | grep -qxE '[0-9a-f]{40}' || { echo "CRIBLEV AMORCE REFUS : $v illisible"; exit 2; }; done
printf '%s' "$FICHE_SHA256" | grep -qxE '[0-9a-f]{64}' || { echo "CRIBLEV AMORCE REFUS : FICHE_SHA256 illisible"; exit 2; }
for v in GO_KV1 GO_KV2; do printf '%s' "${!v}" | grep -qxE 'GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}' || { echo "CRIBLEV AMORCE REFUS : $v illisible"; exit 2; }; done
[ "$GO_KV1" != "$GO_KV2" ] || { echo "CRIBLEV AMORCE REFUS : κv1 = κv2"; exit 2; }
printf '%s' "$BR_SORTIE" | grep -qxE 'calcul/crible-v-v1-sortie-v[1-9][0-9]*' || { echo "CRIBLEV AMORCE REFUS : BR_SORTIE illisible"; exit 2; }
printf '%s' "$BR_ENTREE" | grep -qxE 'calcul/crible-v-v1-entree-v[1-9][0-9]*' || { echo "CRIBLEV AMORCE REFUS : BR_ENTREE illisible"; exit 2; }
[ "${BR_SORTIE##*-v}" = "${BR_ENTREE##*-v}" ] || { echo "CRIBLEV AMORCE REFUS : branches de versions différentes"; exit 2; }
for v in ECHEANCE_UTC_S ECH_MIN ECH_MAX PAS; do printf '%s' "${!v:-}" | grep -qxE '[0-9]+' || { echo "CRIBLEV AMORCE REFUS : $v illisible"; exit 2; }; done
if [ "$ESSAI" = 1 ]; then echo "CRIBLEV AMORCE ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
for v in GH_TOKEN RR_ANTHROPIC_API_KEY_RIGAUD GEMINI_API_KEY OPENAI_API_KEY; do
    printf '%s' "${!v:-}" | grep -qxE '[A-Za-z0-9_-]{8,}' || { echo "CRIBLEV AMORCE REFUS : $v absente ou de forme illisible (valeur jamais affichée)"; exit 2; }; done
printf '%s' "${CONTAINER_ID:-}" | grep -qxE '[0-9]+' || { echo "CRIBLEV AMORCE REFUS : identifiant de la machine illisible"; exit 2; }
R="${RACINE_AMORCE:-/root}"; T="$R/crible-v-v1"; D="$T/depot"
api() {  # $1 = DELETE ou STOP ; rend le code HTTP, jamais jugé (seule la liste des instances, lue par la session, prouve)
    local c
    if [ "$1" = DELETE ]; then c=$("$CURL" -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    else c=$("$CURL" -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; fi
    printf '%s' "$c"; }
minuterie() {  # R10 : la machine par son identifiant ; une destruction n'est jamais jugée par un code
    local n=0 c
    while [ "$(date +%s)" -lt "$ECHEANCE_UTC_S" ]; do sleep "$PAS"; done
    echo "$(date -u +%FT%TZ) CRIBLEV MINUTERIE : échéance atteinte : destruction de la machine $CONTAINER_ID par son identifiant" >> "$T/minuterie.txt"
    while :; do n=$((n + 1)); c=$(api DELETE); echo "$(date -u +%FT%TZ) DELETE $n : HTTP $c" >> "$T/minuterie.txt"
        [ "$n" = 5 ] && { c=$(api STOP); echo "$(date -u +%FT%TZ) stopped : HTTP $c" >> "$T/minuterie.txt"; }
        sleep "$PAS"; done; }
# 1. marque de lancement ; 2. minuterie
RELANCE=0
if [ -e "$T/amorce-lancee" ]; then RELANCE=1
else
    MAINTENANT=$(date +%s)
    [ "$ECHEANCE_UTC_S" -ge $((MAINTENANT + ECH_MIN)) ] && [ "$ECHEANCE_UTC_S" -le $((MAINTENANT + ECH_MAX)) ] || {
        echo "CRIBLEV AMORCE REFUS : échéance hors de [maintenant + $ECH_MIN s, + $ECH_MAX s] : destruction demandée"
        for n in 1 2 3; do api DELETE > /dev/null; sleep 5; done; api STOP > /dev/null; exit 2; }
    mkdir -p "$T" && date -u +%FT%TZ > "$T/amorce-lancee" || exit 2
fi
minuterie & PID_MINUTERIE=$!
export PID_MINUTERIE RELANCE T
# 3. outils
for o in git "$PY" openssl shred sha256sum base64 gzip; do command -v "$o" > /dev/null || { echo "CRIBLEV AMORCE : outil $o absent" >> "$T/amorce.txt"; sleep infinity; }; done
# 4. dépôt partiel au commit du code (aucune poussée possible depuis ce dépôt)
if [ ! -d "$D/.git" ]; then
    export GIT_TERMINAL_PROMPT=0
    AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
    # clone partiel (blobs à la demande) et extraction limitée au code du crible et à prereg/ : aucun runs/, diag/, donnees/,
    # registres/ dans l'arbre extrait (le programme machine le contrôle)
    { git init -q "$D" && git -C "$D" remote add origin "$URL" && git -C "$D" config credential.helper "$AIDE" \
      && git -C "$D" config remote.origin.pushurl /dev/null && git -C "$D" config remote.origin.promisor true \
      && git -C "$D" config remote.origin.partialclonefilter blob:none \
      && git -C "$D" fetch -q --depth=1 --filter=blob:none origin "$COMMIT_CODE" \
      && git -C "$D" fetch -q --depth=1 --filter=blob:none origin "$COMMIT_LOT" \
      && git -C "$D" config core.sparseCheckout true && git -C "$D" config core.sparseCheckoutCone false \
      && printf '/docs/procedures/crible-v-v1/\n/prereg/\n' > "$D/.git/info/sparse-checkout" \
      && git -C "$D" -c advice.detachedHead=false checkout -q --detach "$COMMIT_CODE"; } >> "$T/amorce.txt" 2>&1 \
        || { echo "CRIBLEV AMORCE : dépôt partiel impossible" >> "$T/amorce.txt"; sleep infinity; }
fi
M="$D/$MACHINE_REL"
[ "$(sha256sum < "$M" | cut -d' ' -f1)" = "$SHA_MACHINE" ] && [ "$(cut -d' ' -f1 "$M.sha256" 2>/dev/null)" = "$SHA_MACHINE" ] \
    || { echo "CRIBLEV AMORCE : programme machine d'empreinte différente" >> "$T/amorce.txt"; sleep infinity; }
cp -f "$M" "$T/machine_crible_v_v1.py" || sleep infinity
# 5. la main passe au programme machine (même PID ; la minuterie reste son enfant)
exec "$PY" -I -B "$T/machine_crible_v_v1.py"
