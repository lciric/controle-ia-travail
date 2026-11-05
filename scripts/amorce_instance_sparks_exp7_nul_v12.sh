#!/usr/bin/env bash
# v11 (R12 ; R-1542 : un conteneur qui sort est relancé par Vast, tir réel v9) : copie de l'amorce v10.
#   - Fin normale de phase (fabrication, quel que soit son code ; fenêtre de copie ; phase causale sans destruction) :
#     `arreter_instance` met l'instance à l'état voulu « stopped » par l'interface de Vast (`PUT /instances/<id>/`,
#     `{"state": "stopped"}`, clé du conteneur ; `curl`, sinon `python3`), exige HTTP 2xx et `"success": true`, écrit la
#     ligne au journal, attend la prise d'effet (borné), **puis** sort. Arrêt non obtenu (refus, réponse illisible) :
#     destruction, la ligne dit ce qui est perdu (les couches des modèles et du départ, restées sur le disque).
#   - Mode jouet sur machine réelle (troisième tir) : `MODE=jouet` + `JOUET_MACHINE=1` + addendum factice marqué au commit
#     lancé : la fabrication est une attente factice courte (`JOUET_FABRICATION_S`, au plus 600 s), puis l'arrêt.
#   - `AMORCE_ATTENTE_FIN_S` (au plus 600 s) retarde la destruction sur ordre « fin », pour la lecture du journal au tir.
#   - Garde du code v11 et script d'instance v11.
# v10 (R12 ; tir réel v9 du 5 novembre 2026, 06:27 à 06:35 UTC : image sans curl, amorce sortie à chaque démarrage, plus de
# 110 relances par Vast, journal aveugle à ce cas) : copie de l'amorce v9.
#   - Premier geste, en bash seul : une ligne de démarrage horodatée « AMORCE V10 DEMARRAGE <n> : <date>, machine, commit »,
#     compteur gardé sur le disque (`sparks-v10-demarrages-amorce.txt`), lu par `journal-amorce` v10.
#   - Minuterie écrite en bash seul (sans `cat`), avant tout outil ; son DELETE passe par `curl`, sinon par `python3`
#     (urllib) ; ni l'un ni l'autre : alarme.
#   - Outils exigés (`OUTILS`) vérifiés ; les absents sont installés par `apt-get` sous `timeout` (avec ca-certificates) ;
#     encore absents : destruction immédiate.
#   - **Tout refus avant l'ordre consommé détruit l'instance** (`refus`, `boucle`, `destruction_immediate`) au lieu de
#     sortir ; destruction non obtenue : `sleep infinity`, dit au journal, pour ne pas boucler (la session détruit par
#     l'identifiant). `AMORCE_ATTENTE_REFUS_S` (au plus 600 s) retarde la destruction d'un refus, pour la lecture du journal
#     au tir.
#   - Garde du code v10 et script d'instance v10.
# v9 (R12 ; contre-lecture du delta v5 → v8, points 5, 8, 9 et 19 ; consigne de la mère, b) : copie de l'amorce v8.
#   - **Boucle de redémarrage détectée par l'amorce** : au redémarrage, un ordre neuf est exigé ; sans ordre neuf lisible
#     et accepté (branche des ordres absente ou illisible, ordre déjà fait ou refusé, ordre mal lu), et à tout autre refus
#     qui précède l'ordre (identifiant, commit du disque, GO, registre), c'est une boucle présumée : destruction immédiate
#     par la minuterie (`sparks-v5-detruire`), sans attendre l'échéance.
#   - Chaque redémarrage est consigné au registre des démarrages (plafond de 5 min, durée réelle à sa fin) avant tout le
#     reste : la borne de la machine compte les démarrages d'une boucle ; le rang du démarrage est écrit au journal.
#   - L'ordre est consigné « fait » avant la borne : un refus après lui ne se rejoue pas en boucle (l'ordre n'est plus neuf).
#   - Ordre « fin » traité avant la borne (point 19).
#   - Fin de la phase causale : message exact (code et poussée), point 5.
#   - Création relancée sur un disque où elle a déjà été tentée sans dépôt extrait (`sparks-v9-creation-tentee`) : boucle
#     présumée, destruction immédiate.
#   - Identifiants de démarrage jamais réutilisés (`nouvel_id`) : deux démarrages dans la même seconde ne se confondent
#     plus au registre (répétition locale v9, run 3 : un plafond de copie écrasé, borne sous-estimée).
#   - Garde du code v9 et script d'instance v9.
# v8 (R12, minimale) : copie de l'amorce v7 ; garde du code v8 et script d'instance v8 (manifeste qui cite l'addendum scellé).
# v7 (R12, minimale) : copie de l'amorce v6 ; garde du code v7 et script d'instance v7 (appels de modules corrigés).
# v6 (R12, minimale) : copie de l'amorce v5 où seuls changent la garde du code (liste fermée v6) et le script d'instance
# appelé (v6, qui joue l'essai v6 au lieu de l'essai v5) ; journaux, fichiers et branches gardent leurs noms de la v5.
# Amorce de l'instance de SPARKS-EXP7-NUL, v5 (version neuve de l'amorce v4, R12). Changements à la v4 (contre-lecture du
# delta v4) : durée réelle de chaque démarrage consignée à sa fin (borne de la machine) ; corps du DELETE lu (`"success":
# false` = échec) et aucune tentative qui dépasse la marge ; en mode réel, addendum reconnu (empreinte attendue passée à la
# création, `ADDENDUM_SHA256`, ou commit lancé contenu dans `origin/main`) ; marqueur « gardes passées » exigé pour copier
# ou calculer au redémarrage ; témoin d'une minuterie antérieure encore vivante. Changements de la v4 à la v3 (contre-lecture du
# delta v3) : `timeout` sur chaque étape avant le calcul (clone et extraction 600 s, lecture des ordres 300 s, gardes 120 s,
# lot 900 s) et sur `vastai destroy` (120 s) ; attente du principal sur `$!` du lancement en cours ; branche des ordres
# `ordres/sparks-exp7-nul-v5-<COMMIT[:12]>` ; clé `instance` = CONTAINER_ID ; consignation contrôlée ; `deja_usd` qui ne
# baisse jamais et borne propre de la machine (plafonds consignés, stockage depuis la création) ; branches des sorties
# liées au commit et à l'ordre, préfixe `BRANCHE_PREFIXE` (`calcul/` ou `essai/`).
# Relancée telle quelle à chaque démarrage (`vastai start` relance les arguments du conteneur, avec l'environnement de la
# création). Ordre, sans Python avant la minuterie :
#   0. `curl` et `git` exigés : absents, refus visible, rien ne part ;
#   1. MINUTERIE DE DESTRUCTION, en tout premier, détachée (`setsid`), en bash et `curl` seuls : échéance absolue posée à la
#      création (`ECHEANCE_UTC_S`, au plus la fin du 18 novembre), gardée sur le disque (un redémarrage garde l'échéance
#      d'origine) ; à l'échéance, ou dès que la machine pose `sparks-v5-detruire` (fin du contrôle causal après poussée
#      vérifiée, ordre « fin »), `DELETE /instances/<CONTAINER_ID>/` (clé du conteneur), et en repli
#      `vastai destroy instance <id> -y` si `vastai` est là (R-1482 ; aucune sortie brute gardée, R-1480) ; recommence
#      chaque minute ; **jamais d'arrêt** de la machine par ce code (il tuerait la minuterie) : le processus principal
#      attend la fin de la minuterie quand une destruction est due ;
#   2. démarrage après l'échéance : aucun calcul, destruction ;
#   3. création (aucun `amorce-depot` sur le disque) : clone partiel et clairsemé, GO (base et extension à 40 USD), durée
#      bornée (`depense duree`, DEJA_USD de l'environnement, 0 à la création), garde du code, fabrication sous `timeout` ;
#   4. redémarrage (disque existant) : commit sur le disque = COMMIT, GO revu à la date, **ordre écrit** lu à la tête de
#      la branche `ordres/sparks-exp7-nul-v5-<COMMIT[:12]>` (`redemarrage.py verifier` : numéro neuf, instance, phase,
#      `deja_usd` qui ne baisse pas), borne = max(`deja_usd`, borne de la machine), puis copie d'un lot (conteneur en vie
#      `copie_minutes`, puis sortie), contrôle causal (sous `timeout`, poussée vérifiée, puis destruction), ou fin.
# Variables : COMMIT, COMMIT_CODE, GH_TOKEN, HF_TOKEN, PRIX_HEURE_USD, PRIX_STOCKAGE_HEURE_USD, ECHEANCE_UTC_S, DEJA_USD (0) ;
# posées par Vast : CONTAINER_ID, CONTAINER_API_KEY (jamais affichées). Essai local : DEPOT_URL, RACINE_AMORCE, MODE=jouet,
# GO_DATE, VENV_EXISTANT, MINUTERIE_PAS_S, MINUTERIE_REESSAI_S, MINUTERIE_MARGE_S ; répétition : BRANCHE_PREFIXE=essai/.
set -uo pipefail
R="${RACINE_AMORCE:-/root}"
API=https://console.vast.ai/api/v0
FIN_GO=1795046400            # 2026-11-19T00:00:00Z
GO_ID=GO-2026-11-04-04
export HOME="${HOME:-/root}"
export TZ=UTC
cd "$R" || { echo "AMORCE V10 : racine $R inaccessible : aucune destruction possible : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }
N_DEM=0; [ -s "$R/sparks-v10-demarrages-amorce.txt" ] && read -r N_DEM < "$R/sparks-v10-demarrages-amorce.txt"
case "$N_DEM" in ''|*[!0-9]*) N_DEM=0;; esac
N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/sparks-v10-demarrages-amorce.txt"
printf 'AMORCE V10 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${COMMIT:-?}"
IFS= read -r -d '' MINUTERIE_TXT <<'MINUTERIE'
ECH="$1"; R="$2"; API="$3"; J="$R/sparks-v5-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH" >> "$J"
echo "$$" > "$R/sparks-v5-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
supprimer() {  # un DELETE par la clé du conteneur : curl, sinon python3 (urllib) ; corps écrit au disque ; rend le code HTTP
    local c
    if command -v curl >/dev/null 2>&1; then
        c=$(curl -sS -m 60 -o "$R/sparks-v5-delete-corps.txt" -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    elif command -v python3 >/dev/null 2>&1; then
        c=$(python3 -I -B -c 'import os, sys, urllib.error, urllib.request
q = urllib.request.Request(sys.argv[1], method="DELETE", headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", "")})
try:
    with urllib.request.urlopen(q, timeout=60) as r:
        code, corps = r.status, r.read()
except urllib.error.HTTPError as e:
    code, corps = e.code, e.read()
except Exception:
    code, corps = 0, b""
open(sys.argv[2], "wb").write(corps)
print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$R/sparks-v5-delete-corps.txt" 2>/dev/null) || c=000
    else c=aucun; fi
    echo "$c"
}
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/sparks-v5-detruire" ]; do sleep "$PAS"; done
raison="échéance"; [ -e "$R/sparks-v5-detruire" ] && raison="ordre de la machine"
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do  # jamais d'arrêt de la machine : il tuerait cette minuterie ; le DELETE recommence jusqu'à la fin de la marge
    n=$((n + 1))
    if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then  # une tentative dure au plus 190 s : jamais au-delà de FIN
        echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue, plus de tentative possible avant la fin de la marge" >> "$J"; exit 4
    fi
    c=$(supprimer)
    if [ "$c" = aucun ]; then echo "$(date -u +%FT%TZ) ALARME : ni curl ni python3 : aucune destruction possible par la machine" >> "$J"; exit 5; fi
    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/sparks-v5-delete-corps.txt" 2>/dev/null && refus=oui
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n, $raison) : HTTP $c, refus dans le corps : $refus" >> "$J"
    case "$c" in 2??) if [ "$refus" = non ]; then echo "$(date -u +%FT%TZ) instance $CONTAINER_ID détruite" >> "$J"; exit 0; fi;; esac
    if command -v vastai >/dev/null 2>&1; then
        timeout -k 5 120 vastai destroy instance "$CONTAINER_ID" -y >/dev/null 2>&1; v=$?
        echo "$(date -u +%FT%TZ) repli : vastai destroy instance $CONTAINER_ID -y : code $v (sortie non gardée)" >> "$J"
        [ "$v" = 0 ] && exit 0
    fi
    [ "$(date +%s)" -lt "$FIN" ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue" >> "$J"; exit 4; }
    sleep "$REESSAI"
done
MINUTERIE
printf '%s' "$MINUTERIE_TXT" > "$R/sparks-v5-minuterie.sh" || { echo "AMORCE V10 : minuterie impossible à écrire : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }
destruction_immediate() {  # refus avant la minuterie de ce démarrage : la minuterie jouée tout de suite (échéance 0) ; échec : sleep infinity
    echo "AMORCE V5 : $1 : refus avant l'ordre consommé : destruction immédiate de l'instance"
    bash "$R/sparks-v5-minuterie.sh" 0 "$R" "$API" < /dev/null >> "$R/sparks-v5-minuterie.log" 2>&1; local st=$?
    if [ "$st" = 0 ]; then echo "AMORCE V5 : destruction obtenue"; exit 2; fi
    echo "AMORCE V5 : destruction non obtenue (code $st) : sleep infinity pour ne pas boucler ; la session détruit par l'identifiant"
    sleep infinity; exit 2
}
T_APT=300; case "${AMORCE_T_APT_S:-}" in ''|*[!0-9]*) ;; *) [ "$AMORCE_T_APT_S" -ge 1 ] && [ "$AMORCE_T_APT_S" -le 300 ] && T_APT=$AMORCE_T_APT_S;; esac
OUTILS="curl git python3 timeout setsid sha256sum tar gzip awk sed sort cut tail head mktemp find grep date sleep cat tr"
manquants() { local o m=""; for o in $OUTILS; do command -v "$o" >/dev/null 2>&1 || m="$m $o"; done; printf '%s' "$m"; }
paquet() { case "$1" in curl|git|python3|tar|gzip|sed|grep) printf '%s' "$1";; awk) printf gawk;; setsid) printf util-linux;; find) printf findutils;; *) printf coreutils;; esac; }
MANQ=$(manquants)
if [ -n "$MANQ" ]; then
    echo "AMORCE V5 : outils absents :$MANQ : installation bornée (apt-get, $T_APT s par étape)"
    if command -v apt-get >/dev/null 2>&1 && command -v timeout >/dev/null 2>&1; then
        PAQ="ca-certificates"; for o in $MANQ; do PAQ="$PAQ $(paquet "$o")"; done
        DEBIAN_FRONTEND=noninteractive timeout -k 10 "$T_APT" apt-get update -qq >/dev/null 2>&1 \
            && DEBIAN_FRONTEND=noninteractive timeout -k 10 "$T_APT" apt-get install -y -qq --no-install-recommends $PAQ >/dev/null 2>&1
        echo "AMORCE V5 : installation ($PAQ) : code $?"
    else echo "AMORCE V5 : apt-get ou timeout absent : installation impossible"; fi
    MANQ=$(manquants)
    [ -z "$MANQ" ] || destruction_immediate "outils absents après installation :$MANQ"
fi
outil() { command -v "$1" >/dev/null 2>&1 && echo oui || echo NON; }
echo "AMORCE V5 : outils : curl oui, git oui, unshare $(outil unshare), chroot $(outil chroot), prlimit $(outil prlimit), vastai $(outil vastai)"
E="$R/sparks-v5-echeance.txt"
[ -s "$R/sparks-v5-creation.txt" ] || date +%s > "$R/sparks-v5-creation.txt"
if [ -s "$E" ]; then read -r ECH < "$E"; else
    ECH="${ECHEANCE_UTC_S:-}"
    case "$ECH" in ''|*[!0-9]*) destruction_immediate "ECHEANCE_UTC_S absente ou non entière : rien ne part";; esac
    [ "$ECH" -le "$FIN_GO" ] || { echo "AMORCE V5 : échéance ramenée à la fin du GO ($FIN_GO)"; ECH=$FIN_GO; }
    echo "$ECH" > "$E"
fi
case "$ECH" in ''|*[!0-9]*) destruction_immediate "échéance du disque illisible";; esac
if [ -s "$R/sparks-v5-minuterie.pid" ] && kill -0 "$(cat "$R/sparks-v5-minuterie.pid")" 2>/dev/null; then
    echo "AMORCE V5 : TÉMOIN : minuterie antérieure $(cat "$R/sparks-v5-minuterie.pid") encore vivante (hors conteneur ?)"
fi
setsid bash "$R/sparks-v5-minuterie.sh" "$ECH" "$R" "$API" < /dev/null >> "$R/sparks-v5-minuterie.log" 2>&1 &
PM=$!
echo "AMORCE V5 : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null || echo "?"))"
attendre_minuterie() {   # le conteneur reste en vie tant que la minuterie de CE démarrage détruit ($PM ; borné)
    local lim=$(( $(date +%s) + ${MINUTERIE_MARGE_S:-1800} + 120 ))
    while kill -0 "$PM" 2>/dev/null && [ "$(date +%s)" -lt "$lim" ]; do sleep 2; done
}
resultat_destruction() {  # minuterie finie en code 0 : sortie ; sinon (ou encore vivante) : sleep infinity, dit au journal
    local st=124
    kill -0 "$PM" 2>/dev/null || { wait "$PM" 2>/dev/null; st=$?; }
    [ "$st" = 0 ] && exit "$1"
    echo "AMORCE V5 : destruction non obtenue (minuterie, code $st) : sleep infinity pour ne pas boucler ; la session détruit par l'identifiant"
    sleep infinity; exit "$1"; }
detruire() { echo "$1" > "$R/sparks-v5-detruire"; echo "AMORCE V5 : destruction demandée ($1)"; attendre_minuterie; resultat_destruction "${2:-0}"; }
borne_s() { case "${1:-}" in ''|*[!0-9]*) echo 0;; *) if [ "$1" -le "$2" ]; then echo "$1"; else echo "$2"; fi;; esac; }
arreter_instance() {  # fin normale de phase : instance à l'état voulu « stopped » par l'interface de Vast, vérifié ; sinon destruction
    local c corps="$R/sparks-v11-arret-corps.txt" ok=non
    rm -f "$corps"
    if command -v curl >/dev/null 2>&1; then
        c=$(curl -sS -m 60 -o "$corps" -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    elif command -v python3 >/dev/null 2>&1; then
        c=$(python3 -I -B -c 'import os, sys, urllib.error, urllib.request
q = urllib.request.Request(sys.argv[1], method="PUT", data=b"{\"state\": \"stopped\"}", headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", ""), "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(q, timeout=60) as r:
        code, b = r.status, r.read()
except urllib.error.HTTPError as e:
    code, b = e.code, e.read()
except Exception:
    code, b = 0, b""
open(sys.argv[2], "wb").write(b)
print("%03d" % code)' "$API/instances/${CONTAINER_ID:-}/" "$corps" 2>/dev/null) || c=000
    else c=aucun; fi
    case "$c" in 2??) grep -qiE '"success"[[:space:]]*:[[:space:]]*true' "$corps" 2>/dev/null && ok=oui;; esac
    if [ "$ok" = oui ]; then
        echo "AMORCE V5 $(date -u +%FT%TZ) : $1 : ARRÊT OBTENU (état voulu « stopped », HTTP $c) : le conteneur sort"
        sleep "$(borne_s "${AMORCE_ATTENTE_ARRET_S:-10}" 60)"; exit "${2:-0}"
    fi
    echo "AMORCE V5 $(date -u +%FT%TZ) : $1 : ARRÊT NON OBTENU (HTTP $c, succès non lu) : destruction ; perdus : les couches des modèles et du départ restées sur le disque (seules les sorties légères poussées sont gardées)"
    detruire "arrêt non obtenu : $1" "${2:-0}"; }
refus() {  # refus avant l'ordre consommé : destruction de l'instance, jamais une sortie (une sortie fait relancer le conteneur)
    echo "AMORCE V5 : $1 : refus avant l'ordre consommé : destruction de l'instance"
    local a="${AMORCE_ATTENTE_REFUS_S:-0}"; case "$a" in ''|*[!0-9]*) a=0;; esac; [ "$a" -le 600 ] || a=600
    if [ "$a" -gt 0 ]; then echo "AMORCE V5 : attente de $a s avant la destruction (lecture du journal par la session)"; sleep "$a"; fi
    detruire "refus : $1" 2; }
[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun calcul"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'
P2=src/controle_ia/sparks_exp7_nul_v2; P5=src/controle_ia/sparks_exp7_nul_v5
borne_t() { case "${1:-}" in ''|*[!0-9]*) echo "$2";; *) if [ "$1" -ge 1 ] && [ "$1" -le "$2" ]; then echo "$1"; else echo "$2"; fi;; esac; }
# délais de chaque étape avant le calcul ; l'environnement peut les raccourcir (essais), jamais les allonger
T_GIT=$(borne_t "${AMORCE_T_GIT_S:-}" 600); T_ORDRES=$(borne_t "${AMORCE_T_ORDRES_S:-}" 300)
T_GARDE=$(borne_t "${AMORCE_T_GARDE_S:-}" 120); T_LOT=$(borne_t "${AMORCE_T_LOT_S:-}" 900)
for v in COMMIT COMMIT_CODE PRIX_HEURE_USD PRIX_STOCKAGE_HEURE_USD; do [ -n "${!v:-}" ] || refus "$v absent"; done
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"; export DEPOT_URL
case "$COMMIT" in *[!0-9a-f]*|'') refus "COMMIT illisible";; esac
[ "${#COMMIT}" = 40 ] || refus "COMMIT de 40 caractères attendu"
COURT=${COMMIT:0:12}; BRANCHE_ORDRES="ordres/sparks-exp7-nul-v5-$COURT"
PREFIXE="${BRANCHE_PREFIXE:-calcul/}"
case "$PREFIXE" in calcul/|essai/) ;; *) refus "BRANCHE_PREFIXE $PREFIXE (calcul/ ou essai/)";; esac
REG="$R/sparks-v5-demarrages.txt"
borne() {  # borne = max(dépense imputée, borne propre de la machine) ; aucun modèle
    local b; b=$(timeout -k 5 "$T_GARDE" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" borne "$REG" "$(cat "$R/sparks-v5-creation.txt")" \
        "$PRIX_HEURE_USD" "$PRIX_STOCKAGE_HEURE_USD") || return 1
    awk -v a="$1" -v b="$b" 'BEGIN { if (a + 0 > b + 0) print a; else print b }'
}
nouvel_id() {  # identifiant de démarrage neuf : l'instant, ou le plus grand identifiant du registre + 1 (jamais deux fois le même)
    local n m; n=$(date +%s); m=$(awk '{ print $2 }' "$REG" 2>/dev/null | sort -n | tail -1)
    case "$m" in ''|*[!0-9]*) m=0;; esac; [ "$n" -gt "$m" ] || n=$(( m + 1 )); echo "$n"; }
consigner_demarrage() { fin_lancement; ID_D=$(nouvel_id); timeout -k 5 "$T_GARDE" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" demarrage "$REG" "$ID_D" "$1" \
    || refus "consignation du démarrage impossible : rien ne part"; }
consigner_fin() {  # durée réelle, arrondie à la minute au-dessus ; un échec laisse le plafond compter (prudent)
    timeout -k 5 "$T_GARDE" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" fin "$REG" "$ID_D" "$(( ($(date +%s) - ID_D + 59) / 60 ))" \
        || echo "AMORCE V5 : durée réelle non consignée : le plafond compte"; }
ID_L=""; LANCEMENT_OUVERT=non
fin_lancement() {  # durée réelle du démarrage consigné au redémarrage (une seule fois ; échec : le plafond de 5 min compte)
    [ "$LANCEMENT_OUVERT" = oui ] || return 0; LANCEMENT_OUVERT=non
    timeout -k 5 "$T_GARDE" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" fin "$REG" "$ID_L" "$(( ($(date +%s) - ID_L + 59) / 60 ))" \
        || echo "AMORCE V5 : durée du redémarrage non consignée : le plafond compte"; }
boucle() {  # redémarrage sans ordre neuf accepté : boucle présumée ; destruction immédiate par la minuterie
    echo "AMORCE V5 : $1 : boucle de redémarrage présumée, destruction immédiate (sans attendre l'échéance)"
    detruire "redémarrage sans ordre neuf ($1)" 2; }
addendum_reconnu() {  # mode réel : empreinte attendue de l'addendum scellé, ou commit lancé contenu dans origin/main
    [ "${MODE:-reel}" = jouet ] && { echo "AMORCE V5 : mode jouet : addendum non exigé"; return 0; }
    local sa; sa=$(timeout -k 5 "$T_GARDE" git -C "$R/amorce-depot" show "$COMMIT:prereg/SPARKS-EXP7-NUL-addendum-1.md" 2>/dev/null | sha256sum | cut -c1-64)
    if [ -n "${ADDENDUM_SHA256:-}" ] && [ "$sa" = "$ADDENDUM_SHA256" ]; then echo "AMORCE V5 : addendum reconnu par son empreinte"; return 0; fi
    if timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" fetch -q origin main 2>/dev/null \
       && git -C "$R/amorce-depot" merge-base --is-ancestor "$COMMIT" FETCH_HEAD; then echo "AMORCE V5 : commit lancé contenu dans origin/main"; return 0; fi
    return 1
}
go_conforme() { (cd "$R/amorce-depot" && timeout -k 5 "$T_GARDE" python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import go; sys.exit(go.main(sys.argv[1:]))" registres/go.md ${GO_DATE:+"$GO_DATE"}); }
duree() { (cd "$R/amorce-depot" && timeout -k 5 "$T_GARDE" python3 -I -B -c "import sys; sys.path.insert(0, '$P2'); import depense; sys.exit(depense.main(sys.argv[1:]))" duree "$PRIX_HEURE_USD" "$PRIX_STOCKAGE_HEURE_USD" "$1"); }
if [ ! -d "$R/amorce-depot/.git" ]; then
    echo "AMORCE V5 : création"
    [ -e "$R/sparks-v9-creation-tentee" ] && boucle "création déjà tentée sur ce disque, sans dépôt extrait"
    : > "$R/sparks-v9-creation-tentee" || refus "marqueur de création impossible : rien ne part"
    [ -e "$R/sparks" ] && refus "$R/sparks sans dépôt (R11, R12) : refus"
    timeout -k 10 "$T_GIT" git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$R/amorce-depot" \
        || refus "clonage impossible (ou délai de $T_GIT s)"
    git -C "$R/amorce-depot" config credential.helper "$AIDE"
    timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" sparse-checkout set --no-cone '/*' '!/*/' '/src/' '/scripts/' '/registres/go.md' '/prereg/SPARKS-EXP7-NUL-*' \
        && timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" checkout -q "$COMMIT" \
        || refus "commit $COMMIT introuvable (ou délai de $T_GIT s)"
    go_conforme || refus "$GO_ID non conforme (base et extension à 40 USD) : aucun calcul"
    DEJA=$(borne "${DEJA_USD:-0}") || refus "borne de la machine illisible : aucun calcul"
    MINUTES=$(duree "$DEJA") || refus "prix illisibles : aucun calcul"
    [ "$MINUTES" -ge 60 ] || refus "plafond trop bas pour ce prix ($MINUTES min) : aucun calcul"
    (cd "$R/amorce-depot" && timeout -k 5 "$T_GARDE" python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v12'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$COMMIT_CODE" "$COMMIT") \
        || refus "code ou addendum non conformes : aucun calcul"
    addendum_reconnu || refus "addendum non reconnu (empreinte attendue absente ou différente, commit hors de origin/main) : aucun calcul"
    : > "$R/sparks-v5-gardes-ok" || refus "marqueur des gardes impossible : rien ne part"
    consigner_demarrage "$MINUTES"
    echo "AMORCE V5 : fabrication, durée plafonnée à $MINUTES minutes"
    if [ "${MODE:-reel}" = jouet ] && [ "${JOUET_MACHINE:-}" = 1 ] \
       && grep -q "ADDENDUM FACTICE DE RÉPÉTITION" "$R/amorce-depot/prereg/SPARKS-EXP7-NUL-addendum-1.md" 2>/dev/null; then
        JF=$(borne_s "${JOUET_FABRICATION_S:-60}" 600)
        echo "AMORCE V5 : fabrication factice (mode jouet sur machine réelle, addendum factice) : $JF s"; sleep "$JF"; code=0
    else
        timeout --signal=TERM --kill-after=5m "${MINUTES}m" env COMMIT="$COMMIT" COMMIT_CODE="$COMMIT_CODE" TRAVAIL="$R/sparks" \
            GO_ID="$GO_ID" PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v12.sh"
        code=$?
    fi
    consigner_fin; echo "AMORCE V5 $(date -u +%FT%TZ) : fin de la fabrication, code $code"
    arreter_instance "fin de la fabrication, code $code" "$code"
fi
echo "AMORCE V5 : redémarrage"
trap fin_lancement EXIT
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) boucle "CONTAINER_ID illisible";; esac
ID_L=$(nouvel_id)
timeout -k 5 "$T_GARDE" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" demarrage "$REG" "$ID_L" 5 \
    || boucle "consignation du redémarrage impossible"
LANCEMENT_OUVERT=oui
echo "AMORCE V5 : redémarrage consigné au registre des démarrages : démarrage n° $(grep -c '^p ' "$REG" 2>/dev/null || echo ?)"
[ "$(git -C "$R/amorce-depot" rev-parse HEAD)" = "$COMMIT" ] || boucle "commit du disque ≠ COMMIT"
go_conforme || boucle "$GO_ID non conforme à la date"
O=$(mktemp -d "$R/sparks-ordres-$(date -u +%Y%m%dT%H%M%S)-XXXX") && timeout -k 5 "$T_ORDRES" git -C "$R/amorce-depot" -c credential.helper="$AIDE" fetch -q --depth 1 origin "$BRANCHE_ORDRES" \
    && timeout -k 5 "$T_ORDRES" git -C "$R/amorce-depot" archive -o "$O/ordres.tar" FETCH_HEAD ordres \
    && timeout -k 5 "$T_ORDRES" tar -x -C "$O" -f "$O/ordres.tar" || boucle "ordres illisibles (ou délai)"
L=$(timeout -k 5 "$T_GARDE" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" verifier "$O/ordres" "$R/sparks-v5-ordres-faits.txt" "$CONTAINER_ID") || boucle "ordre refusé (aucun ordre neuf)"
PHASE_O=$(printf '%s' "$L" | sed -n 's/^PHASE=\([a-z]*\) .*/\1/p'); NUM=$(printf '%s' "$L" | sed -n 's/.* NUMERO=\([0-9]*\) .*/\1/p')
DEJA=$(printf '%s' "$L" | sed -n 's/.* DEJA_USD=\([0-9.]*\) .*/\1/p'); CM=$(printf '%s' "$L" | sed -n 's/.* COPIE_MINUTES=\([0-9]*\) .*/\1/p')
ORDRE=$(printf '%s' "$L" | sed -n 's/.* ORDRE=\(ordre-[0-9]*\.json\)$/\1/p')
[ -n "$PHASE_O" ] && [ -n "$NUM" ] && [ -n "$DEJA" ] && [ -n "$ORDRE" ] || boucle "ordre mal lu"
timeout -k 5 "$T_GARDE" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" fait "$R/sparks-v5-ordres-faits.txt" "$NUM" "$DEJA" \
    || boucle "consignation de l'ordre impossible"
echo "AMORCE V5 : ordre $NUM ($PHASE_O) accepté et consigné"
if [ "$PHASE_O" = fin ]; then                                # avant la borne (point 19)
    AF=$(borne_s "${AMORCE_ATTENTE_FIN_S:-0}" 600)
    [ "$AF" -gt 0 ] && { echo "AMORCE V5 : attente de $AF s avant la destruction (ordre fin ; lecture du journal par la session)"; sleep "$AF"; }
    detruire "ordre $NUM : fin"
fi
DEJA_EFF=$(borne "$DEJA") || { echo "AMORCE V5 : borne de la machine illisible : aucun calcul (ordre $NUM consommé)"; exit 2; }
MINUTES=$(duree "$DEJA_EFF") || { echo "AMORCE V5 : prix illisibles : aucun calcul (ordre $NUM consommé)"; exit 2; }
echo "AMORCE V5 : ordre $NUM ($PHASE_O), dépense imputée $DEJA USD, borne retenue $DEJA_EFF USD, durée plafonnée à $MINUTES minutes"
case "$PHASE_O" in copie|causal) [ -e "$R/sparks-v5-gardes-ok" ] || { echo "AMORCE V5 : création sans gardes passées : seul un ordre « fin » est permis"; exit 2; };; esac
case "$PHASE_O" in
    copie)
        [ "$MINUTES" -ge "$((CM + 5))" ] || { echo "AMORCE V5 : plafond trop bas pour la copie ($MINUTES min) : rien ne part"; exit 2; }
        consigner_demarrage "$((CM + 5))"
        timeout -k 10 "$T_LOT" python3 -I -B "$R/amorce-depot/$P5/redemarrage.py" lot "$O/ordres/$ORDRE" "$R/sparks/sortie" "$R/sparks/lots" \
            || { echo "AMORCE V5 : lot impossible (ou délai de $T_LOT s)"; exit 2; }
        echo "AMORCE V5 : COPIE prête ($R/sparks/lots/lot-$(printf %03d "$NUM")) ; conteneur en vie $CM minutes"
        sleep "$((CM * 60))"; consigner_fin; arreter_instance "fin de la fenêtre de copie" 0 ;;
    causal)
        [ "$MINUTES" -ge 60 ] || { echo "AMORCE V5 : plafond trop bas pour la phase causale ($MINUTES min) : rien ne part"; exit 2; }
        T="$R/sparks-causal-$(printf %03d "$NUM")"
        consigner_demarrage "$MINUTES"
        timeout --signal=TERM --kill-after=5m "${MINUTES}m" env COMMIT="$COMMIT" COMMIT_CODE="$COMMIT_CODE" TRAVAIL="$T" \
            GO_ID="$GO_ID" PHASE=causal BRANCHE="${PREFIXE}sparks-exp7-nul-causal-v5-$COURT-$(printf %03d "$NUM")" CLE="$O/ordres/causal/cle-ouverte-v1.json" REPONSES="$O/ordres/causal/reponses" \
            MODELES="$R/sparks/sortie/modeles" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v12.sh"
        code=$?; consigner_fin
        POUSSEE="non vérifiée"; [ -e "$T/POUSSEE-VERIFIEE" ] && POUSSEE="vérifiée"
        echo "AMORCE V5 $(date -u +%FT%TZ) : fin de la phase causale, code $code, poussée $POUSSEE"
        if [ "$code" = 0 ] && [ "$POUSSEE" = "vérifiée" ]; then detruire "fin du contrôle causal, poussée vérifiée"; fi
        echo "AMORCE V5 : phase causale en code $code, poussée $POUSSEE : pas de destruction (nœud de Lazar)"
        arreter_instance "fin de la phase causale, code $code" "$code" ;;
esac
