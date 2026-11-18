#!/usr/bin/env bash
# Amorce du pilote MR-2 sur la machine jetable, sans ssh — v2 (procédure v12 ; v1 : procédure v11 ; mot de Lazar « (a) : go », R-2882).
# v2 : échéance permise portée à 17 h 05 (m3 de la vérification de la v11 : offre à 0,15 USD/h au plus, 2,55 USD à 17 h) ; noms v2. Passée à la
# création (base64 dans `--args`, imprimée par session_pilote_mr2_v74_v2.sh commande) ; aucun service à joindre de l'extérieur.
# Ordre : 0. relance du conteneur par le loueur ? (marque $T/amorce-lancee : rien n'est refait, voir plus bas) ; 1. arguments ; un
#   refus **avant** la minuterie demande la destruction de l'instance par elle-même (DELETE, jamais jugé, puis « stopped ») ;
#   2. minuterie de destruction armée à ECHEANCE_UTC_S, avant toute passe ; 3. dépôt partiel au commit COMMIT_LOT (aucune
#   extraction), programme machine et aide pris au commit, empreintes SCRIPT_SHA256 et AIDE_SHA256 ; 4. `exec` du programme
#   machine (même PID : la minuterie reste son enfant). Tant que le programme machine n'a pas pris la main, aucune trace ne peut être
#   poussée : le motif d'un arrêt se lit par `vastai logs` (aucune valeur secrète n'y est jamais écrite).
# Variables (--env) : COMMIT_LOT, COMMIT_PREP, COMMIT_MAIN (40 hex chacun), BR_SORTIE, BR_ENTREE, ECHEANCE_UTC_S, GO_ID
#   (GO-2026-11-14-14), SCRIPT_SHA256, AIDE_SHA256 (programme machine et aide v2), GH_TOKEN et les trois clés du pilote (par leur nom, jamais affichées) ;
#   posées par le loueur : CONTAINER_ID, CONTAINER_API_KEY.
# Essai (AMORCE_ESSAI=1 seulement) : RACINE_AMORCE (dossier jetable), DEPOT_URL_ESSAI (dépôt local), API_VAST_ESSAI (doublure
#   locale du loueur), ATTENTE_REFUS_S, PAS_MINUTERIE_S ; AMORCE_ARGUMENTS_SEULS=1 : contrôles des arguments seulement (aucun
#   réseau, aucune écriture, CONTAINER_ID non exigé), joué par la session avant d'imprimer la commande ; hors essai, chacune est
#   refusée.
set -uo pipefail
ESSAI="${AMORCE_ESSAI:-0}"
for v in RACINE_AMORCE DEPOT_URL_ESSAI API_VAST_ESSAI AMORCE_ARGUMENTS_SEULS ATTENTE_REFUS_S PAS_MINUTERIE_S; do
    [ "$ESSAI" = 1 ] || [ -z "${!v:-}" ] || { echo "PILOTE AMORCE REFUS : $v en essai seulement"; exit 2; }
done
R="${RACINE_AMORCE:-/root}"
T="$R/pilote"
API="${API_VAST_ESSAI:-https://console.vast.ai/api/v0}"
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
DEPOT_URL="${DEPOT_URL_ESSAI:-$DEPOT_URL_OFFICIEL}"
GO_ATTENDU=GO-2026-11-14-14
DOSSIER_CODE=docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/sans-ssh-v2
ECHEANCE_MAX_S=61500   # 17 h 05 : à 0,15 USD/h au plus (offre exigée par l'outil v2), 2,56 USD, sous la part machine de 3 USD (GO-2026-11-14-14)
export TZ=UTC PYTHONDONTWRITEBYTECODE=1 LC_ALL=C.UTF-8
a() { printf '%s PILOTE AMORCE %s\n' "$(date -u +%FT%TZ)" "$*"; }
entier_ascii() { printf '%s' "$1" | LC_ALL=C grep -qxE '[1-9][0-9]*'; }
hex() { printf '%s' "$1" | LC_ALL=C grep -qxE "[0-9a-f]{$2}"; }
branche() { printf '%s' "$1" | LC_ALL=C grep -qxE 'calcul/[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*' && case "$1" in *..*|*.lock|*/) false;; *) true;; esac; }
# >>> refus-avant-minuterie (joué par les essais)
refus() {  # avant la minuterie : l'instance demande sa propre destruction (jamais jugée), puis « stopped »
    local n c
    a "REFUS : $1"
    if [ "$ESSAI" != 1 ] || [ -n "${API_VAST_ESSAI:-}" ]; then
        if entier_ascii "${CONTAINER_ID:-}"; then
            for n in 1 2 3; do
                c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                    "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
                a "REFUS : destruction demandée par l'instance, essai $n : HTTP $c (jamais jugé)"; sleep "${ATTENTE_REFUS_S:-20}"; done
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
            a "REFUS : état « stopped » demandé : HTTP $c ; la session prouve l'absence (verifier-destruction)"
        else
            a "REFUS : identifiant de l'instance illisible : aucune destruction par l'instance ; la session détruit"
        fi
    fi
    exit 2; }
# <<< refus-avant-minuterie
# >>> minuterie (destruction jamais jugée par un code de retour : seule l'absence lue par la session la prouve)
minuterie() { local n=0 c; while [ "$(date +%s)" -lt "$ECHEANCE_UTC_S" ]; do sleep "${PAS_MINUTERIE_S:-30}"; done
    a "MINUTERIE : échéance atteinte : destruction de l'instance $CONTAINER_ID par son identifiant (DELETE)"
    while :; do n=$((n + 1))
        c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
        a "MINUTERIE : DELETE, essai $n : HTTP $c (jamais jugé ; nouvel essai dans 60 s si l'instance vit encore)"
        if [ "$n" = 5 ]; then
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
            a "MINUTERIE : toujours vivante après 5 demandes : état « stopped » demandé : HTTP $c"
        fi
        sleep "${PAS_MINUTERIE_S:-60}"; done; }
# <<< minuterie
# 1. arguments (une relance du conteneur les relit aussi : la minuterie est réarmée à la même échéance)
for v in COMMIT_LOT COMMIT_PREP COMMIT_MAIN BR_SORTIE BR_ENTREE ECHEANCE_UTC_S GO_ID SCRIPT_SHA256 AIDE_SHA256; do
    [ -n "${!v:-}" ] || refus "variable $v absente"; done
for v in COMMIT_LOT COMMIT_PREP COMMIT_MAIN; do hex "${!v}" 40 || refus "$v : 40 caractères hexadécimaux attendus"; done
hex "$SCRIPT_SHA256" 64 || refus "SCRIPT_SHA256 : 64 caractères hexadécimaux attendus"
hex "$AIDE_SHA256" 64 || refus "AIDE_SHA256 : 64 caractères hexadécimaux attendus"
[ "$GO_ID" = "$GO_ATTENDU" ] || refus "GO_ID $GO_ID ≠ $GO_ATTENDU"
branche "$BR_SORTIE" || refus "BR_SORTIE illisible (calcul/… attendu)"
branche "$BR_ENTREE" || refus "BR_ENTREE illisible (calcul/… attendu)"
[ "$BR_SORTIE" != "$BR_ENTREE" ] || refus "BR_SORTIE = BR_ENTREE"
entier_ascii "$ECHEANCE_UTC_S" || refus "ECHEANCE_UTC_S illisible"
[ "${AMORCE_ARGUMENTS_SEULS:-0}" = 1 ] || entier_ascii "${CONTAINER_ID:-}" || refus "identifiant de l'instance (CONTAINER_ID) illisible"
for v in GH_TOKEN RR_ANTHROPIC_API_KEY_RIGAUD GEMINI_API_KEY OPENAI_API_KEY; do
    printf '%s' "${!v:-}" | LC_ALL=C grep -qxE '[A-Za-z0-9_-]{8,}' || refus "$v absente ou illisible (nom seul)"; done
[ "$ECHEANCE_UTC_S" -gt "$(date +%s)" ] && [ "$ECHEANCE_UTC_S" -le $(( $(date +%s) + ECHEANCE_MAX_S )) ] \
    || refus "échéance hors de [maintenant, + 17 h 05]"
for o in git curl python3 openssl sha256sum base64 timeout shred setsid tar awk sed grep stat; do
    command -v "$o" > /dev/null || refus "outil absent : $o"; done
if [ "${AMORCE_ARGUMENTS_SEULS:-0}" = 1 ]; then a "ESSAI DES ARGUMENTS : conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
# 2. minuterie, avant toute passe ; relance du conteneur reconnue par la marque
mkdir -p "$T" || refus "$T impossible"
minuterie < /dev/null &
export PID_MINUTERIE=$!
a "minuterie lancée (PID $PID_MINUTERIE, échéance $(date -u -d "@$ECHEANCE_UTC_S" +%FT%TZ)), avant toute passe"
export ENTREE_RELANCE=0
if [ -e "$T/amorce-lancee" ]; then
    ENTREE_RELANCE=1
    a "RELANCE DU CONTENEUR (marque $T/amorce-lancee présente, posée $(head -c 40 "$T/amorce-lancee")) : aucune passe refaite"
else
    date -u +%FT%TZ > "$T/amorce-lancee"
fi
# 3. dépôt partiel au commit (aucune extraction ici), programme machine et aide aux empreintes attendues
D="$T/depot"
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ "$ENTREE_RELANCE" = 0 ]; then
    git init -q "$D" && git -C "$D" remote add origin "$DEPOT_URL" \
        && git -C "$D" config extensions.partialClone origin && git -C "$D" config remote.origin.promisor true \
        && git -C "$D" config remote.origin.partialclonefilter blob:none \
        && git -C "$D" config credential.helper "$AIDE_GIT" \
        || { a "ARRET : dépôt local impossible ; la minuterie détruira à l'échéance ; la session détruit"; sleep infinity; }
    for c in "$COMMIT_LOT" "$COMMIT_PREP" "$COMMIT_MAIN"; do
        ok=0
        for n in 1 2 3; do
            timeout 600 git -C "$D" fetch -q --filter=blob:none --depth=1 origin "$c" && { ok=1; break; }; sleep $((20 * n)); done
        [ "$ok" = 1 ] || { a "ARRET : commit $c introuvable sur le dépôt ; la session détruit"; sleep infinity; }
    done
fi
M="$T/machine_pilote_mr2_v74_v2.sh"; H="$T/machine_pilote_mr2_v74_v2.py"
rm -f "$M.neuf" "$H.neuf"
git -C "$D" show "$COMMIT_LOT:$DOSSIER_CODE/machine_pilote_mr2_v74_v2.sh" > "$M.neuf" 2>/dev/null \
    && git -C "$D" show "$COMMIT_LOT:$DOSSIER_CODE/machine_pilote_mr2_v74_v2.py" > "$H.neuf" 2>/dev/null \
    || { a "ARRET : programme machine ou aide absent du commit $COMMIT_LOT ; la session détruit"; sleep infinity; }
[ "$(sha256sum < "$M.neuf" | cut -d' ' -f1)" = "$SCRIPT_SHA256" ] \
    || { a "ARRET : programme machine : empreinte ≠ SCRIPT_SHA256 ; la session détruit"; sleep infinity; }
[ "$(sha256sum < "$H.neuf" | cut -d' ' -f1)" = "$AIDE_SHA256" ] \
    || { a "ARRET : aide : empreinte ≠ AIDE_SHA256 ; la session détruit"; sleep infinity; }
mv -f "$M.neuf" "$M" && mv -f "$H.neuf" "$H"
a "programme machine et aide aux empreintes attendues ; la main passe au programme machine (même PID)"
export R T D API DEPOT_URL ESSAI
exec bash "$M"
