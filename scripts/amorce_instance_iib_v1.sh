#!/usr/bin/env bash
# Amorce de l'instance de (ii-b), v1 (conception ii-b, brouillon 2, section 10 ; ordre exploratoire, brouillon 2, §§ 1, 5 à 7) : tirée de
# `scripts/amorce_instance_t06_v11.sh` (nom neuf, R12 ; la v11 reste telle quelle). EXPLORATOIRE, NON OPPOSABLE (R-522). Écrite et éprouvée à
# blanc en essai local (AMORCE_ESSAI_LOCAL=1 : aucune minuterie, aucun appel à Vast ; essais `tests/test_iib_amorce_v1.py`), jamais lancée
# par son développeur. Changements par rapport à la v11 (le reste — minuterie de destruction en tout premier, consignation sous verrou,
# second démarrage, poussée initiale éprouvée, relais des seules lignes PROGRES neutres, garde de la carte, fin anormale — est inchangé) :
#  (1) aucun identifiant de GO en dur : IIB_GO_ID (GO-AAAA-MM-JJ-NN), ligne LUE dans registres/go.md du commit cloné (`session_v12
#      plafond-ligne`, puis `session_v3 go` et `calendrier` à ce plafond) ; course exploratoire : PREREG_ABSENT=1 et CONFIG exigés, aucun
#      préenregistrement lu ; branche `essai/iib-explo-v<n>` seulement (défaut essai/iib-explo-v1) ;
#  (2) le run est joué par `controle_ia.iib.lanceur_v1` (aucune activation, aucune sonde) ; la suite ciblée figée est
#      `scripts/tests-cibles-iib-v1.txt` (empreinte écrite en dur ci-dessous), jouée d'office ; TESTS_ARGS en mode jouet seulement ;
#  (3) données légères poussées : adaptateurs, `oracle-iib.json`, `ids-actions-iib.npz`, `textes-actions-iib.jsonl` et leurs sceaux ; il
#      n'existe aucun morceau d'activations (l'étape des morceaux ne committe rien) ; le bras B de l'audit de fuite n'est pas joué ;
#  (4) clonage réduit aux chemins dont l'instance a besoin (CHEMINS_CLONAGE) : ni `diag/`, ni `runs/`, ni `traces/`, ni d'autres
#      `donnees/` que les tâches de T0.5 (aucun fichier de 7a, 7b, P3-bis, du bras d'attaque ni du mode tenu à l'écart) ;
#  (5) marqueurs et dossier de l'instance renommés `iib-…` (`$R/iib`), messages « (ii-b) ».
# Variables (--env) : COMMIT, GH_TOKEN, HF_TOKEN (mode reel), IIB_GO_ID, BRANCHE, DEPOT_URL, MODE, PREREG_ABSENT=1, CONFIG,
# TESTS_ATTENDUS, ECHEANCE_UTC_S, FIN_GO_UTC_S, DEPENSE_EPUISEE_UTC_S ; posées par Vast : CONTAINER_ID, CONTAINER_API_KEY (jamais
# affichées). Essai local : RACINE_AMORCE, VENV_EXISTANT, AMORCE_ESSAI_LOCAL=1, TESTS_ARGS (jouet), POUSSEE_ATTENTE_S, MINUTERIE_*.
set -uo pipefail
R="${RACINE_AMORCE:-/root}"
API=https://console.vast.ai/api/v0
GO_ID="${IIB_GO_ID:-}"
MORCEAU_MAX="${MORCEAU_MAX_OCTETS:-90000000}"
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
export HOME="${HOME:-/root}" TZ=UTC
cd "$R" || { echo "AMORCE IIB : racine $R inaccessible : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }
N_DEM=0; [ -s "$R/iib-demarrages.txt" ] && read -r N_DEM < "$R/iib-demarrages.txt"
case "$N_DEM" in ''|*[!0-9]*) N_DEM=0;; esac
N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/iib-demarrages.txt"
printf 'AMORCE IIB v1 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${COMMIT:-?}"
IFS= read -r -d '' MINUTERIE_TXT <<'MINUTERIE'
ECH="$1"; DEP="$2"; R="$3"; API="$4"; J="$R/iib-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac; case "$DEP" in ''|*[!0-9]*) DEP=0;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH, dépense épuisée à $DEP" >> "$J"
echo "$$" > "$R/iib-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
consigner() {  # C14, C08 : résultats partiels committés et poussés par le script écrit par l'amorce (git seul)
    if [ -f "$R/iib-consigner.sh" ]; then timeout -k 10 2400 bash "$R/iib-consigner.sh" "$1" >> "$J" 2>&1; echo "$(date -u +%FT%TZ) consigné ($1) : code $?" >> "$J"
    else echo "$(date -u +%FT%TZ) rien à consigner ($1) : dépôt non extrait" >> "$J"; fi; }
appel() {  # méthode, corps JSON (vide pour DELETE) ; écrit le code HTTP
    local c
    if command -v curl >/dev/null 2>&1; then
        if [ -n "$2" ]; then c=$(curl -sS -m 60 -o "$R/iib-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" -H 'Content-Type: application/json' -d "$2" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
        else c=$(curl -sS -m 60 -o "$R/iib-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; fi
    elif command -v python3 >/dev/null 2>&1; then
        c=$(python3 -I -B -c 'import os, sys, urllib.error, urllib.request
corps = sys.argv[3].encode() if sys.argv[3] else None
q = urllib.request.Request(sys.argv[1], data=corps, method=sys.argv[2], headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", ""), "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(q, timeout=60) as r:
        code, corps = r.status, r.read()
except urllib.error.HTTPError as e:
    code, corps = e.code, e.read()
except Exception:
    code, corps = 0, b""
open(sys.argv[4], "wb").write(corps)
print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$1" "$2" "$R/iib-api-corps.txt" 2>/dev/null) || c=000
    else c=aucun; fi
    echo "$c"
}
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/iib-detruire" ]; do
    if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/iib-depense-epuisee" ]; then
        echo "$(date -u +%FT%TZ) DÉPENSE ÉPUISÉE (C08, plafond de la configuration cumulé) : consignation, poussée, puis état « stopped »" >> "$J"
        echo "dépense épuisée $(date -u +%FT%TZ)" > "$R/iib-depense-epuisee"
        consigner "dépense épuisée"
        if [ -e "$R/iib-detruire" ]; then echo "$(date -u +%FT%TZ) PUT stopped non envoyé : ordre de destruction de l'amorce reçu pendant la consignation (R-1689)" >> "$J"
        else c=$(appel PUT '{"state": "stopped"}'); echo "$(date -u +%FT%TZ) PUT stopped (dépense épuisée) : HTTP $c" >> "$J"; fi
    fi
    sleep "$PAS"
done
raison="échéance"; [ -e "$R/iib-detruire" ] && raison="ordre de l'amorce"
if [ "$raison" = "échéance" ]; then echo "$(date -u +%FT%TZ) ÉCHÉANCE $ECH atteinte (C14) : consignation et poussée des résultats partiels avant la destruction" >> "$J"; consigner "échéance"; fi
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do
    n=$((n + 1))
    if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then
        echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue avant la fin de la marge" >> "$J"; exit 4
    fi
    c=$(appel DELETE '')
    if [ "$c" = aucun ]; then echo "$(date -u +%FT%TZ) ALARME : ni curl ni python3 : aucune destruction possible" >> "$J"; exit 5; fi
    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/iib-api-corps.txt" 2>/dev/null && refus=oui
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n, $raison) : HTTP $c, refus dans le corps : $refus" >> "$J"
    case "$c" in 2??) if [ "$refus" = non ]; then echo "$(date -u +%FT%TZ) instance $CONTAINER_ID détruite" >> "$J"; exit 0; fi;; esac
    [ "$(date +%s)" -lt "$FIN" ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue" >> "$J"; exit 4; }
    sleep "$REESSAI"
done
MINUTERIE
printf '%s' "$MINUTERIE_TXT" > "$R/iib-minuterie.sh" || { echo "AMORCE IIB : minuterie impossible à écrire"; [ "$ESSAI" = 1 ] && exit 1; sleep infinity; exit 1; }
PM=""
attendre_minuterie() { local lim=$(( $(date +%s) + ${MINUTERIE_MARGE_S:-1800} + 120 )); while [ -n "$PM" ] && kill -0 "$PM" 2>/dev/null && [ "$(date +%s)" -lt "$lim" ]; do sleep 2; done; }
detruire() {  # destruction demandée à la minuterie ; essai local : fichier posé, sortie
    echo "$1" > "$R/iib-detruire"; echo "AMORCE $(date -u +%FT%TZ) : destruction demandée ($1)"
    if [ "$ESSAI" = 1 ]; then exit "${2:-2}"; fi
    attendre_minuterie
    local st=124; { [ -n "$PM" ] && ! kill -0 "$PM" 2>/dev/null; } && { wait "$PM" 2>/dev/null; st=$?; }
    [ "$st" = 0 ] && exit "${2:-2}"
    echo "AMORCE $(date -u +%FT%TZ) : destruction non obtenue (minuterie, code $st) : sleep infinity ; la session détruit par l'identifiant"
    sleep infinity; exit "${2:-2}"; }
REFUS_ATTENTE_S=180            # R-1677 : constante d'exploitation ; seul l'essai local (AMORCE_ESSAI_LOCAL=1) la remplace par REFUS_ATTENTE_ESSAI_S (0 par défaut)
[ "$ESSAI" = 1 ] && REFUS_ATTENTE_S="${REFUS_ATTENTE_ESSAI_S:-0}"
attente_refus() { echo "AMORCE $(date -u +%FT%TZ) : refus annoncé : destruction demandée dans ${REFUS_ATTENTE_S} s (la session relève la cause dans le journal avant)"; sleep "$REFUS_ATTENTE_S"; }
refus() { echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; detruire "refus : $1" 2; }
refus_precoce() {  # avant la minuterie : destruction immédiate (minuterie lancée à l'échéance 0), ou fichier posé en essai
    echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; echo "refus : $1" > "$R/iib-detruire"
    if [ "$ESSAI" = 1 ]; then exit 2; fi
    bash "$R/iib-minuterie.sh" 0 0 "$R" "$API" < /dev/null >> "$R/iib-minuterie.log" 2>&1; sleep infinity; exit 2; }
sommeil() {  # disque lisible par la session ; arrêt et destruction par l'identifiant (R10)
    echo "AMORCE $(date -u +%FT%TZ) : sommeil ($1) : disque lisible, la session arrête et détruit par l'identifiant"
    if [ "$ESSAI" = 1 ]; then echo "sommeil ($1)" > "$R/iib-sommeil"; exit "${2:-0}"; fi
    sleep infinity; exit "${2:-0}"; }
arreter_instance() {  # fin normale : état voulu « stopped » (disque gardé jusqu'au verdict) ; C13 : sommeil après l'arrêt obtenu
    echo "AMORCE $(date -u +%FT%TZ) : fin, code $2"
    if [ "$ESSAI" = 1 ]; then  # essai local : C-V4-1 observe que le verrou de consignation (descripteur 9) est relâché AVANT l'arrêt
        if [ -e "/proc/$$/fd/9" ]; then echo "verrou tenu à l'arrêt ($1)" > "$R/iib-verrou-tenu-a-l-arret"; fi
        echo "stopped ($1)" > "$R/iib-arret-demande"; exit "$2"; fi
    local c corps="$R/iib-arret-corps.txt" ok=non
    if command -v curl >/dev/null 2>&1; then
        c=$(curl -sS -m 60 -o "$corps" -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    else c=aucun; fi
    case "$c" in 2??) grep -qiE '"success"[[:space:]]*:[[:space:]]*true' "$corps" 2>/dev/null && ok=oui;; esac
    if [ "$ok" = oui ]; then echo "AMORCE $(date -u +%FT%TZ) : ARRÊT OBTENU (état voulu « stopped », HTTP $c) : sommeil jusqu'à l'arrêt effectif (C13)"; sommeil "arrêt obtenu" "$2"; fi
    echo "AMORCE $(date -u +%FT%TZ) : ARRÊT NON OBTENU (HTTP $c) : le conteneur reste en vie ; la session arrête par l'identifiant (R10)"
    sommeil "arrêt non obtenu" "$2"; }
FIN_GO="${FIN_GO_UTC_S:-}"
case "$FIN_GO" in ''|*[!0-9]*) refus_precoce "FIN_GO_UTC_S absente ou non entière (L11 : fin du GO lue dans la configuration par la session)";; esac
if [ "$ESSAI" != 1 ]; then
    OUTILS="curl git python3 timeout setsid flock sha256sum tar gzip awk sed sort cut tail head mktemp grep date sleep stat"
    manquants() { local o m=""; for o in $OUTILS; do command -v "$o" >/dev/null 2>&1 || m="$m $o"; done; printf '%s' "$m"; }
    paquet() { case "$1" in curl|git|python3|tar|gzip|sed|grep) printf '%s' "$1";; awk) printf gawk;; setsid|flock) printf util-linux;; *) printf coreutils;; esac; }
    MANQ=$(manquants)
    if [ -n "$MANQ" ]; then
        echo "AMORCE IIB : outils absents :$MANQ : installation bornée (apt-get, 300 s par étape)"
        if command -v apt-get >/dev/null 2>&1 && command -v timeout >/dev/null 2>&1; then
            PAQ="ca-certificates"; for o in $MANQ; do PAQ="$PAQ $(paquet "$o")"; done
            DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get update -qq >/dev/null 2>&1 \
                && DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get install -y -qq --no-install-recommends $PAQ >/dev/null 2>&1
            echo "AMORCE IIB : installation ($PAQ) : code $?"
        fi
        MANQ=$(manquants); [ -z "$MANQ" ] || refus_precoce "outils absents :$MANQ"
    fi
fi
E="$R/iib-echeance.txt"; DE="$R/iib-depense-epuisee-utc.txt"
if [ -s "$E" ]; then read -r ECH < "$E"; else
    ECH="${ECHEANCE_UTC_S:-}"
    case "$ECH" in ''|*[!0-9]*) refus_precoce "ECHEANCE_UTC_S absente ou non entière";; esac
    [ "$ECH" -le "$FIN_GO" ] || { echo "AMORCE IIB : échéance ramenée à la fin du GO ($FIN_GO)"; ECH=$FIN_GO; }
    echo "$ECH" > "$E"
fi
if [ -s "$DE" ]; then read -r DEP < "$DE"; else
    DEP="${DEPENSE_EPUISEE_UTC_S:-}"
    case "$DEP" in ''|*[!0-9]*) refus_precoce "DEPENSE_EPUISEE_UTC_S absente ou non entière (C08 : heure d'épuisement du plafond de la configuration, calculée à la création)";; esac
    echo "$DEP" > "$DE"
fi
if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/iib-depense-epuisee" ]; then      # R-1689 : l'argent est déjà épuisé au démarrage, l'amorce détruira
    echo "dépense déjà épuisée au démarrage $(date -u +%FT%TZ) (R-1689)" > "$R/iib-depense-epuisee"
fi
if [ "$ESSAI" != 1 ]; then
    setsid bash "$R/iib-minuterie.sh" "$ECH" "$DEP" "$R" "$API" < /dev/null >> "$R/iib-minuterie.log" 2>&1 &
    PM=$!
    echo "AMORCE IIB : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null || echo "?") ; dépense épuisée à $DEP)"
fi
if [ -d "$R/amorce-depot" ]; then
    # C-V3-2 (C13) : second démarrage, AVANT les contrôles d'heure : les commits en attente sont poussés d'abord, quelle que
    # soit l'heure ; puis destruction si l'argent est épuisé ou l'échéance passée (rien ne doit plus coûter), sommeil après
    # une fin normale, destruction après un run interrompu ; jamais un nouveau run
    if [ -e "$R/iib-fin-normale" ] || [ -e "$R/iib-depense-epuisee" ]; then
        echo "AMORCE $(date -u +%FT%TZ) : second démarrage après une fin normale ou une dépense épuisée (C13, C-V3-2) : poussée des commits en attente d'abord"
        [ -f "$R/iib-consigner.sh" ] && timeout -k 10 1200 bash "$R/iib-consigner.sh" "second démarrage"
        if [ -e "$R/iib-depense-epuisee" ] || [ "$(date +%s)" -ge "$DEP" ]; then
            detruire "second démarrage après la dépense épuisée (C08, C-V3-2) : commits en attente poussés, l'argent est épuisé : destruction, pas de sommeil" 0
        fi
        [ "$(date +%s)" -lt "$ECH" ] || detruire "second démarrage après l'échéance (C14, C-V3-2) : commits en attente poussés, destruction" 0
        sommeil "second démarrage après une fin normale, rien ne repart" 0
    fi
    [ -f "$R/iib-consigner.sh" ] && timeout -k 10 1200 bash "$R/iib-consigner.sh" "redémarrage d'un run interrompu"
    refus "redémarrage : dépôt déjà extrait sur le disque (second démarrage d'un run interrompu) : résultats partiels consignés, rien ne repart"
fi
[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun calcul"
[ "$(date +%s)" -lt "$DEP" ] || detruire "démarrage après l'heure de dépense épuisée (C08) : aucun calcul"
for v in COMMIT GH_TOKEN; do [ -n "${!v:-}" ] || refus "$v absent"; done
MODE="${MODE:-reel}"
case "$MODE" in reel|jouet) ;; *) refus "MODE=$MODE (reel ou jouet)";; esac
[ "$MODE" = reel ] && { [ -n "${HF_TOKEN:-}" ] || refus "HF_TOKEN absent en mode reel"; }
case "$COMMIT" in *[!0-9a-f]*|'') refus "COMMIT illisible";; esac
[ "${#COMMIT}" = 40 ] || refus "COMMIT de 40 caractères attendu"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"; export DEPOT_URL
BRANCHE="${BRANCHE:-essai/iib-explo-v1}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
# course exploratoire (ii-b) : aucun préenregistrement ; la ligne de GO de la course (IIB_GO_ID) est lue dans registres/go.md du commit
case "$GO_ID" in GO-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) refus "IIB_GO_ID=$GO_ID : identifiant de ligne de GO illisible ou absent (GO-AAAA-MM-JJ-NN attendu)";; esac
[ "$PREREG_ABSENT" = 1 ] || refus "course exploratoire : PREREG_ABSENT=1 exigé (aucun préenregistrement n'est lu par (ii-b))"
case "$BRANCHE" in essai/iib-explo-v[0-9]*) ;; *) refus "la branche doit être essai/iib-explo-v<n> ($BRANCHE) : jamais main, 7a, 7b, P3-bis";; esac
[ -n "${CONFIG:-}" ] || refus "CONFIG exigé (chemin de la configuration scellée de (ii-b) dans le commit)"
[ -n "${TESTS_ARGS:-}" ] && [ "$MODE" != jouet ] && refus "TESTS_ARGS n'est permis qu'en répétition jouet (jamais en mode réel : la suite ciblée figée est la seule jouée)"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
# Clonage réduit (v11, R-1677), chemins de (ii-b) seulement (mode sans cône ; motifs de type gitignore) : code et essais joués par
# l'amorce ; préenregistrements (consignes de P3) ; tâches de T0.5 (réserve et évaluation) ; registres (GO lu par l'amorce et les essais) ;
# documents et invites scellées que lisent le lanceur et la suite ciblée (guide de classification H1, notes : configuration et consigne
# scellées) ; textes de (ii-b) (essais de forme de la consigne) ; dossiers des runs de (ii-b) seulement (`*-iib-*`, `traces/iib-*` :
# git n'ajoute à l'index que des chemins de l'extraction partielle). Exclus : tout autre `diag/`, `runs/`, `traces/` et `donnees/`.
CHEMINS_CLONAGE='/.claude/
/src/
/tests/
/scripts/
/pyproject.toml
/requirements-*.txt
/prereg/
/donnees/20261007-082440-t05-extraction/
/registres/*.md
/docs/*.md
/docs/*.txt
/docs/*.sha256
/docs/notes/
/docs/sources/invites-2606.07054-v1/
/docs/sources/invites-2606.08892-v1/
/brouillons/ii-b-saboteur-budget-v1/
/diag/*-iib-*/
/runs/*-iib-*/
/donnees/*-iib-*/
/traces/iib-*/'
T_CLONE0=$(date +%s)
timeout -k 10 900 git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$R/amorce-depot" || refus "clonage impossible (jeton GitHub ?)"
git -C "$R/amorce-depot" config credential.helper "$AIDE"
git -C "$R/amorce-depot" config user.name "instance de calcul (ii-b)"
git -C "$R/amorce-depot" config user.email "instance-calcul@invalid"
SP_MSG=$(git -C "$R/amorce-depot" sparse-checkout init --no-cone 2>&1) || refus "extraction partielle impossible (sparse-checkout init) : $(printf '%s' "$SP_MSG" | head -c 300 | tr '\n' ' ')"
SP_MSG=$(printf '%s\n' "$CHEMINS_CLONAGE" | git -C "$R/amorce-depot" sparse-checkout set --no-cone --stdin 2>&1) || refus "extraction partielle impossible (sparse-checkout set) : $(printf '%s' "$SP_MSG" | head -c 300 | tr '\n' ' ')"
[ -z "$SP_MSG" ] || echo "AMORCE $(date -u +%FT%TZ) : sparse-checkout : $(printf '%s' "$SP_MSG" | head -c 200 | tr '\n' ' ')"
timeout -k 10 900 git -C "$R/amorce-depot" checkout -q "$COMMIT" || refus "commit $COMMIT introuvable"
T_CLONE1=$(date +%s)
CL_S=$(( T_CLONE1 - T_CLONE0 )); [ "$CL_S" -ge 1 ] || CL_S=1
CL_GIT=$(du -sb "$R/amorce-depot/.git" 2>/dev/null | cut -f1); CL_ARBRE=$(du -sb --exclude=.git "$R/amorce-depot" 2>/dev/null | cut -f1)
echo "AMORCE $(date -u +%FT%TZ) : CLONAGE mode=$MODE secondes=$CL_S octets_git=${CL_GIT:-?} octets_arbre=${CL_ARBRE:-?} debit_Mo_s=$(awk -v b="${CL_GIT:-0}" -v a="${CL_ARBRE:-0}" -v s="$CL_S" 'BEGIN {printf "%.2f", (b + a) / s / 1000000}') motifs=$(printf '%s\n' "$CHEMINS_CLONAGE" | grep -c .)"
T="$R/iib"; mkdir -p "$T"
JOURNAL="$T/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-zA-Z0-9_-]+=[^ ]+)+$'
MOTIF_INTERDIT='au-dessus|interpr|échec|echec|aire=|bas=|haut=|ligne_|table_|plancher'
cd "$R/amorce-depot" || refus "dépôt extrait inaccessible"
# script de consignation (C11, C14, C08 ; git seul), lu aussi par la minuterie et par un second démarrage
cat > "$R/iib-consigner.sh" <<CONSIGNER
#!/usr/bin/env bash
# écrit par l'amorce v1 de (ii-b) : consigne et pousse les résultats partiels ; git seul, sous verrou ; \$1 = motif
R='$R'; BRANCHE='$BRANCHE'; T='$T'; JOURNAL='$JOURNAL'; MORCEAU_MAX='$MORCEAU_MAX'; POUSSEE_ATTENTE_S='${POUSSEE_ATTENTE_S:-15}'
CONSIGNER
cat >> "$R/iib-consigner.sh" <<'CONSIGNER'
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
pousser() { local essai; for essai in 1 2 3; do timeout -k 10 600 git push -q origin "$BRANCHE" 2>"$T/poussee.err" && return 0; journal "poussée : tentative $essai refusée"; [ "$essai" -lt 3 ] && sleep $((POUSSEE_ATTENTE_S * essai * essai)); done; return 1; }
refuser_gros() {  # C11 : aucun fichier de plus de MORCEAU_MAX octets ne part dans un commit (le dépôt distant le refuserait)
    local f t; while IFS= read -r f; do [ -f "$f" ] || continue; t=$(stat -c %s -- "$f" 2>/dev/null || echo 0)
        if [ "$t" -gt "$MORCEAU_MAX" ]; then git rm -q --cached -- "$f" >/dev/null 2>&1; journal "ERREUR DE CHAÎNE (C11) : $f fait $t octets > $MORCEAU_MAX : retiré du commit, resté sur l'instance"; echo "$f $t" >> "$R/iib-fichiers-trop-gros.txt"; fi
    done < <(git diff --cached --name-only --diff-filter=AM); return 0; }
ajouter() {  # C-V4-1 : un `git add` en échec (index.lock) n'est jamais lu comme « rien à committer » ; code 1 et journal
    git add "$@" 2>"$T/add.err" && return 0
    journal "ERREUR DE CHAÎNE (C-V4-1) : git add en échec ($*) : $(tr '\n' ' ' < "$T/add.err" | cut -c1-200)"; echo "$(date -u +%FT%TZ) git add en échec : $*" >> "$R/iib-erreurs-chaine.txt"; return 1; }
ajouter_legeres() { local f rc=0; for f in donnees/*/adaptateur-*.pt donnees/*/adaptateur-*.pt.sha256 donnees/*/oracle-iib.json donnees/*/oracle-iib.json.sha256 \
        donnees/*/ids-actions-iib.npz donnees/*/ids-actions-iib.npz.sha256 donnees/*/textes-actions-iib.jsonl donnees/*/textes-actions-iib.jsonl.sha256 \
        donnees/*/oracle-iib-*.json donnees/*/oracle-iib-*.json.sha256 \
        donnees/*/ids-actions-iib-*.npz donnees/*/ids-actions-iib-*.npz.sha256 \
        donnees/*/textes-actions-iib-*.jsonl donnees/*/textes-actions-iib-*.jsonl.sha256; do
        if [ -f "$f" ]; then ajouter -f "$f" || rc=1; fi; done; return $rc; }
ajouter_morceaux() { return 0; }    # (ii-b) : aucune activation, aucun morceau
commit_verifie() {  # C-V4-1 : 0 = commit fait ; 10 = rien à committer (index vide) ; 1 = commit en échec (réessayé une fois)
    refuser_gros
    local rc essai; git diff --cached --quiet 2>/dev/null; rc=$?
    [ "$rc" = 0 ] && return 10
    if [ "$rc" != 1 ]; then journal "ERREUR DE CHAÎNE (C-V4-1) : lecture de l'index impossible (git diff, code $rc)"; echo "$(date -u +%FT%TZ) lecture de l'index impossible : $1" >> "$R/iib-erreurs-chaine.txt"; return 1; fi
    for essai in 1 2; do
        git commit -qm "$1" >/dev/null 2>"$T/commit.err" && return 0
        journal "ERREUR DE CHAÎNE (C-V4-1) : commit en échec (tentative $essai) : $(tr '\n' ' ' < "$T/commit.err" | cut -c1-200)"
        [ "$essai" = 1 ] && sleep "${COMMIT_ATTENTE_S:-2}"
    done
    echo "$(date -u +%FT%TZ) commit en échec : $1" >> "$R/iib-erreurs-chaine.txt"; return 1; }
etape_commit() {  # $1 = message, $2 = journal si fait, $3 = journal si rien à committer ; rend 0 (fait ou rien) ou 1 (échec de chaîne)
    local rc; commit_verifie "$1"; rc=$?
    case "$rc" in 0) [ -z "$2" ] || journal "$2"; return 0;; 10) [ -z "$3" ] || journal "$3"; return 0;; *) return 1;; esac; }
trace_consignation() {  # R-1692 (E2-6) : le journal de l'instance atteint la branche quand la consignation vient de la minuterie (échéance, dépense épuisée) ou d'un redémarrage ; sinon une échéance pendant l'installation ne laisse RIEN sur la branche
    local d; mkdir -p traces || return 1
    d=$(mktemp -d "traces/iib-consignation-$(date -u +%Y%m%d-%H%M%S)-XXXX") || return 1
    { echo "motif : $1"; echo "heure : $(date -u +%FT%TZ)"; echo "dernière ligne du journal avant la consignation : ${DERNIERE_LIGNE_AVANT:-$(tail -n 1 "$JOURNAL" 2>/dev/null)}" | cut -c1-400
      echo "--- 400 dernières lignes du journal de l'instance (ligne d'échéance et dernière étape atteinte comprises) ---"; tail -n 400 "$JOURNAL" 2>/dev/null | cut -c1-400; } > "$d/journal-consignation.txt"
    [ -f "$R/iib-minuterie.log" ] && tail -n 200 "$R/iib-minuterie.log" | cut -c1-400 > "$d/iib-minuterie-fin.txt"      # la ligne « ÉCHÉANCE … atteinte (C14) » est écrite par la minuterie, pas par l'amorce
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    ajouter "$d" || return 1
    etape_commit "(ii-b) : journal de l'instance ($1)" "$1 : journal de l'instance committé" ""; }
consigner_partiel() {  # $1 = motif ; deux commits (données légères d'abord, morceaux ensuite), poussée ; 0 = tout, 1 = poussée impossible, 2 = poussée faite de ce qui existe, mais échec de chaîne
    local echec=0
    ajouter -A runs diag || echec=1
    ajouter_legeres || echec=1
    etape_commit "(ii-b) : résultats et données légères ($1)" "$1 : résultats et données légères committés" "$1 : aucun résultat léger à committer" || echec=1
    ajouter_morceaux || echec=1
    etape_commit "(ii-b) : sous-ensemble d'activations en morceaux ($1)" "$1 : morceaux committés" "" || echec=1
    if [ "${TRACE_CONSIGNATION:-0}" = 1 ]; then trace_consignation "$1" || echec=1; fi    # fixé par le seul chemin de la ligne de commande (minuterie, redémarrages), jamais par la fin de run
    if pousser; then journal "branche $BRANCHE poussée ($1)"; [ "$echec" = 0 ] && return 0; journal "ERREUR DE CHAÎNE (C-V4-1) : poussée faite de ce qui existe ($1), mais un ajout ou un commit a échoué"; return 2; fi
    journal "poussée impossible ($1) : résultats restés sur l'instance"; return 1; }
if [ "${1:-}" = "--source" ]; then return 0 2>/dev/null || exit 0; fi
exec 9>>"$R/iib-consigner.lock"; flock -w 1500 9 || { echo "verrou de consignation non obtenu ($1)"; exit 1; }
cd "$R/amorce-depot" || { echo "dépôt extrait inaccessible"; exit 1; }
DERNIERE_LIGNE_AVANT=$(tail -n 1 "$JOURNAL" 2>/dev/null)    # étape atteinte avant que la consignation écrive ses propres lignes
TRACE_CONSIGNATION=1 consigner_partiel "$1"
exit $?
CONSIGNER
. "$R/iib-consigner.sh" --source
journal "début iib v1 : MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE CONFIG=$CONFIG GO=$GO_ID FIN_GO=$FIN_GO ECHEANCE=$ECH DEPENSE_EPUISEE=$DEP"
SESSION_V3="import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
SESSION_V12="import sys; sys.path.insert(0, 'src'); from controle_ia.t06 import session_v12; sys.exit(session_v12.main(sys.argv[1:]))"
PLAFOND_LIGNE_GO=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V12" plafond-ligne registres/go.md "$GO_ID" 2>&1) || refus "$GO_ID non conforme dans registres/go.md du commit ($PLAFOND_LIGNE_GO)"
GOL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V3" go registres/go.md "$GO_ID" "$PLAFOND_LIGNE_GO" 2>&1) || refus "$GO_ID non conforme ($GOL)"
journal "GO : $GOL"
ATTENDUS="${TESTS_ATTENDUS:-}"
CITES=("$CONFIG")
for f in "${CITES[@]}"; do
    { [ -f "$f" ] && [ -f "$f.sha256" ]; } || refus "configuration $f ou son sceau absent de l'arbre du commit $COMMIT"
done
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src timeout -k 5 300 python3 -u -m controle_ia.scellement verifier "${CITES[@]}" >"$T/sceaux.txt" 2>&1 \
    || refus "sceau non conforme de la configuration ($(grep -v '^OK ' "$T/sceaux.txt" | tail -n 1 || true))"
journal "configuration citée présente et scellée : $CONFIG ; tests attendus ${ATTENDUS:-(dernière ligne relevée)}"
CAL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_V3" calendrier "$CONFIG" registres/go.md "$GO_ID" "$PLAFOND_LIGNE_GO" 2>&1) || refus "calendrier de la configuration non conforme ($CAL)"
FIN_CONFIG=$(printf '%s\n' "$CAL" | sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p' | tail -1)
[ "$FIN_CONFIG" = "$FIN_GO" ] || refus "fin du GO reçue ($FIN_GO) ≠ calendrier.fin_go_utc de la configuration ($FIN_CONFIG) (L11)"
[ "$ECH" -le "$FIN_CONFIG" ] || refus "échéance $ECH après la fin du GO de la configuration ($FIN_CONFIG)"
journal "calendrier : $CAL"
code_branche=0
timeout -k 5 300 git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$T/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) refus "branche $BRANCHE déjà présente sur le dépôt distant (relancement sous une branche nouvelle)";;
    2) ;;
    *) refus "vérification de la branche $BRANCHE impossible (git ls-remote, code $code_branche)";;
esac
git checkout -q -b "$BRANCHE"
timeout -k 5 300 git push -q origin "$BRANCHE" 2>"$T/poussee-initiale.err" || refus "poussée initiale de la branche $BRANCHE refusée (droit d'écriture du jeton ?)"
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"
traces() { local d; mkdir -p traces; d=$(mktemp -d "traces/iib-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$T/tests.txt" "$T/tests.err" "$T"/run.json "$T"/run.err "$T"/nvidia-smi.txt "$T"/pip-freeze.txt "$R/iib-minuterie.log" "$R/iib-fichiers-trop-gros.txt" "$T/progres-retenues.txt"; do [ -f "$f" ] && cp "$f" "$d/"; done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    ajouter "$d" || return 1; etape_commit "(ii-b) : traces de l'instance ($1)" "" "traces : aucun fichier neuf à committer"; }
# C-V4-1 : la fin de run et les consignations d'arrêt prennent le verrou de `iib-consigner.sh` (fd 9) ; il n'est pris qu'APRÈS
# la fin du run et du relais (aucun processus fils ne garde le descripteur) et relâché AVANT `arreter_instance`
prendre_verrou() {  # $1 = motif ; 0 = verrou pris ; 1 = non obtenu en 1500 s (journalisé, la chaîne continue sans lui : poussée au mieux)
    exec 9>>"$R/iib-consigner.lock"
    if flock -w "${VERROU_ATTENTE_S:-1500}" 9; then return 0; fi
    journal "ERREUR DE CHAÎNE (C-V4-1) : verrou de consignation non obtenu ($1)"; echo "$(date -u +%FT%TZ) verrou non obtenu : $1" >> "$R/iib-erreurs-chaine.txt"
    exec 9>&-; return 1; }
liberer_verrou() { exec 9>&-; }
consigner_arret() { prendre_verrou "arrêt pendant $1"; consigner_partiel "arrêt pendant $1"; traces "arrêt pendant $1"; pousser || true; liberer_verrou; }
fin_anormale() {  # C-V4-1 : ce qui existe est déjà poussé ; marqueur, verrou relâché, arrêt de l'instance, code 1
    echo "fin anormale $(date -u +%FT%TZ), run $RUN : $1" > "$R/iib-fin-anormale"; journal "FIN ANORMALE (C-V4-1) : $1"
    liberer_verrou; arreter_instance "fin anormale" 1; }
[ "$MODE" = reel ] && nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$T/nvidia-smi.txt"
if [ -n "${VENV_EXISTANT:-}" ]; then . "$VENV_EXISTANT/bin/activate"; else
    timeout -k 10 1800 python3.11 -m venv .venv && . .venv/bin/activate && timeout -k 10 3600 pip install -q -r requirements-gpu.txt || { journal "installation impossible"; consigner_arret "installation"; arreter_instance "installation impossible" 1; }
fi
python -m pip freeze --all >"$T/pip-freeze.txt" 2>/dev/null || true
# C-V4-3 : matériel de l'instance (E2-7, E2-8, E3-10) ; ligne neutre relayée par la surveillance (aucun état de sonde)
echo "AMORCE $(date -u +%FT%TZ) : MATERIEL MemTotal_ko=$(awk '/^MemTotal:/ {print $2}' /proc/meminfo 2>/dev/null || echo ?) coeurs=$(nproc 2>/dev/null || echo ?) flock=$(command -v flock >/dev/null 2>&1 && echo oui || echo non)" | tee -a "$JOURNAL"
TESTS_ARGS="${TESTS_ARGS:-}"; TESTS_ARGS="${TESTS_ARGS//,/ }"      # C-V4-3 : la virgule sépare les essais dans la variable d'environnement de Vast (aucun espace permis)
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
# R-1686 : garde de la carte, avant tout calcul en mode réel (E2, tentative 2 : « The NVIDIA driver on your system is too old (found version 12020) », torch 2.14.1+cu130,
# cuda_disponible False). Carte invisible → journal (pilote, CUDA de torch, message), consignation de la cause sur la branche, puis `refus` (annonce, 180 s, destruction)
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)" 2>"$T/torch-cuda.err"; then
    PILOTE=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader 2>/dev/null | head -n 1 | tr -d ' ')
    CUDA_TORCH=$(python -c "import torch; print(torch.version.cuda)" 2>/dev/null | tail -n 1)
    journal "carte invisible pour torch : torch.cuda.is_available() faux ; pilote ${PILOTE:-inconnu} ; CUDA de torch ${CUDA_TORCH:-?} ; message : $(tail -c 300 "$T/torch-cuda.err" 2>/dev/null | tr '\n' ' ')"
    consigner_arret "contrôle de la carte"
    refus "carte invisible pour torch (torch.cuda.is_available() faux) : pilote ${PILOTE:-inconnu}, CUDA de torch ${CUDA_TORCH:-?} : aucun calcul"
fi
# v9 : suite ciblée et figée (liste de fichiers à l'empreinte écrite en dur) ; TESTS_ARGS (jouet seulement) a la priorité
LISTE_TESTS="scripts/tests-cibles-iib-v1.txt"; LISTE_SHA256="847676eff87f20c8aa5d7b1a1b401a7dd025c71c57d190ec0ba9c306f397e3b6"; FICHIERS_TESTS=""
if [ -z "${TESTS_ARGS:-}" ]; then
    liste_refus() { journal "suite ciblée : $1 : arrêt avant tout essai"; consigner_arret "liste des essais"; arreter_instance "liste des essais" 1; }
    [ -f "$LISTE_TESTS" ] || liste_refus "liste $LISTE_TESTS absente"
    [ "$(sha256sum "$LISTE_TESTS" | cut -d' ' -f1)" = "$LISTE_SHA256" ] || liste_refus "empreinte de $LISTE_TESTS ≠ celle de l'amorce ($LISTE_SHA256)"
    while IFS= read -r f; do
        [ -n "$f" ] || continue
        printf '%s\n' "$f" | grep -Eq '^tests/test_[A-Za-z0-9_]+\.py$' || liste_refus "chemin illisible dans la liste : $f"
        [ -f "$f" ] || liste_refus "essai absent du dépôt : $f"
        FICHIERS_TESTS="$FICHIERS_TESTS $f"
    done < "$LISTE_TESTS"
    [ -n "$FICHIERS_TESTS" ] || liste_refus "liste vide"
    journal "suite ciblée : $(printf '%s\n' $FICHIERS_TESTS | wc -l) fichiers d'essais, liste $LISTE_TESTS sha256 $LISTE_SHA256"
fi
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no ${TESTS_ARGS:-} $FICHIERS_TESTS >"$T/tests.txt" 2>"$T/tests.err"; then
    tail -n 5 "$T/tests.txt" "$T/tests.err" | tee -a "$JOURNAL"; journal "tests en échec : arrêt"; consigner_arret "tests"; arreter_instance "tests en échec" 1
fi
DERNIERE=$(tail -1 "$T/tests.txt"); journal "tests : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed » : arrêt"; consigner_arret "tests"; arreter_instance "nombre de tests" 1
fi
journal "course exploratoire sans préenregistrement (R-522, non opposable)"
RUN="$(date -u +%Y%m%d-%H%M%S)-iib-$MODE"
journal "run : $RUN (sans couperet de temps ; lanceur iib v1)"
: >"$T/run.err"; : >"$T/progres-retenues.txt"
PYTHONPATH=src python -m controle_ia.iib.lanceur_v1 --config "$CONFIG" --run-id "$RUN" >"$T/run.json" 2>>"$T/run.err" &
PID_RUN=$!
# C01 : relais des seules lignes PROGRES bien formées ; une ligne qui porte un mot d'état de sonde n'est pas relayée, elle est comptée
( tail -n +1 -F --pid="$PID_RUN" "$T/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" | while IFS= read -r ligne; do
    if printf '%s\n' "$ligne" | grep -qiE "$MOTIF_INTERDIT"; then printf '%s\n' "$(date -u +%FT%TZ) PROGRES non relayée : motif interdit (C01)" | tee -a "$JOURNAL" >> "$T/progres-retenues.txt"
    else printf '%s\n' "$ligne" | tee -a "$JOURNAL"; fi; done ) &
PID_RELAIS=$!
code=0; wait "$PID_RUN" || code=$?
wait "$PID_RELAIS" 2>/dev/null || true
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then journal "run : code $code, mais résumé écrit sans arrêt consigné : run complet"
    elif [ -f "diag/$RUN/arret.json" ]; then
        grep -v '^PROGRES ' "$T/run.err" | grep -viE "$MOTIF_INTERDIT" | tail -n 5 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; arreter_instance "arrêt consigné pendant le run" 1
    else
        grep -v '^PROGRES ' "$T/run.err" | grep -viE "$MOTIF_INTERDIT" | tail -n 5 | tee -a "$JOURNAL" || true
        echo "AMORCE $(date -u +%FT%TZ) : RUN MORT sans résumé ni arrêt consigné (code $code) : arrêt de l'instance par son identifiant (R10)" | tee -a "$JOURNAL"
        consigner_arret "run mort (code $code)"; arreter_instance "run mort" 1
    fi
fi
# C11 : données légères d'abord, dans un commit à part, poussées ; morceaux ensuite ; traces enfin.
# C-V4-1 : tout cela sous le verrou de consignation ; « rien à committer » (code 10) ≠ commit en échec (code 1)
ECHEC=0
prendre_verrou "fin de run" || ECHEC=1
ajouter "runs/$RUN" "diag/$RUN" || ECHEC=1
ajouter_legeres || ECHEC=1
etape_commit "(ii-b) ($MODE), run $RUN : résultats et données légères" "" "aucun résultat léger à committer" || ECHEC=1
journal "run terminé : $RUN"
pousser || journal "poussée des résultats impossible : résultats restés sur l'instance"
ajouter_morceaux || ECHEC=1
commit_verifie "(ii-b) ($MODE), run $RUN : sous-ensemble d'activations en morceaux (< $MORCEAU_MAX octets chacun)"; rc_m=$?
case "$rc_m" in
    0) journal "morceaux committés : $(git show --stat --format= HEAD | grep -c 'activations-sous-ensemble-iib-[0-9]' || true) fichier(s)"
       pousser || journal "poussée des morceaux impossible : morceaux restés sur l'instance";;
    10) journal "aucun morceau à committer";;
    *) ECHEC=1;;
esac
traces "fin" || ECHEC=1
# un fichier retiré du commit (C11) reste sur l'instance, hors de `git status` si `donnees/` est ignoré : c'est un échec de chaîne
[ ! -s "$R/iib-fichiers-trop-gros.txt" ] || { journal "ERREUR DE CHAÎNE (C-V4-1) : fichier(s) trop gros retiré(s) du commit, restés sur l'instance : $(head -n 3 "$R/iib-fichiers-trop-gros.txt" | tr '\n' ';')"; ECHEC=1; }
if [ "$ECHEC" != 0 ]; then
    pousser || journal "poussée de ce qui existe impossible"
    fin_anormale "un ajout, un commit ou le verrou a échoué en fin de run : poussée de ce qui existe tentée, aucun marqueur de fin normale"
fi
# C-V4-1 : rien ne doit rester hors du dépôt avant la fin normale (fichiers légers, résultats, traces, y compris les fichiers ignorés)
RESTE=$(git status --porcelain --ignored -- runs diag donnees traces 2>&1)
if [ -n "$RESTE" ]; then
    journal "ERREUR DE CHAÎNE (C-V4-1) : git status --porcelain --ignored non vide avant la fin normale ($(printf '%s' "$RESTE" | head -n 3 | tr '\n' ';')) : consignation de rattrapage"
    consigner_partiel "fin de run"
    RESTE=$(git status --porcelain --ignored -- runs diag donnees traces 2>&1)
    if [ -n "$RESTE" ]; then pousser || true; fin_anormale "fichiers non consignés après le rattrapage : $(printf '%s' "$RESTE" | head -n 3 | tr '\n' ';')"; fi
fi
AUTRES=$(git status --porcelain 2>&1 | head -n 3 | tr '\n' ';'); [ -z "$AUTRES" ] || journal "note : git status --porcelain (hors runs, diag, donnees, traces) : $AUTRES"
echo "fin normale $(date -u +%FT%TZ), run $RUN" > "$R/iib-fin-normale"
if pousser; then journal "branche $BRANCHE poussée (résultats, données légères et traces)"; liberer_verrou; arreter_instance "fin du run" 0; fi
journal "run complet, mais poussée finale impossible après trois tentatives : résultats restés sur l'instance (disque lisible ; un second démarrage repousse, C13)"
liberer_verrou
arreter_instance "poussée impossible" 1
