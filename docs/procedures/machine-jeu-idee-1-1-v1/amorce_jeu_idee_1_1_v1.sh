#!/usr/bin/env bash
# Amorce de la machine du jeu relancé de l'idée 1.1, v1 (docs/procedures/machine-jeu-idee-1-1-v1/, procédure du même
# dossier ; GO-2026-11-16-09, R-3014). Jouée au démarrage de la machine (étiquette jeu-idee-1-1-relance-v1), passée en base64
# par lancer_jeu_idee_1_1_machine_v1.sh. Une machine, un jeu ; écrit sous $R/jeu-idee-1-1-relance-v1 seulement.
# Ordre : 0. arguments ; minuterie (TERM au jeu, par son PID, 20 min avant l'échéance s'il a passé sa borne de 48 h ; à
#   l'échéance, journal poussé puis destruction par l'identifiant, redemandée tant que la machine vit) ; 1. outils, amd64,
#   GH_TOKEN par son nom ; 2. branche de sortie neuve (absente du dépôt distant), dépôt de sortie à part (branche orpheline qui
#   ne reçoit que traces/, runs/<run>/ et diag/organisme-idees-juge-v1/<run>/), première poussée du journal (dès lors tout
#   arrêt pousse ses traces), suivi poussé chaque heure ; 3. Python 3.13.18 de l'image, environnement neuf, numpy 2.4.6,
#   scipy 1.17.1, pytest 9.1.1, contrôle des versions de l'addendum de relance (« 3.13.18 2.4.6 1.17.1 », sinon arrêt avant tout
#   calcul) ; 4. dépôt au commit COMMIT (ancêtre de main), arbre propre, aucune poussée possible depuis ce dépôt ; 5. empreintes
#   (texte, addendum d'empreintes et compagnon, addendum de relance égal à son compagnon et à EMPREINTE_RELANCE, essai du § 6
#   point 3), aucune sortie antérieure de ce jeu, 1 Gio libre ; 6. jeu (commande de l'addendum), PID poussé aussitôt ;
#   7. sorties vérifiées par leurs compagnons, recopiées, comparées à l'octet, poussées ; 8. état « stopped » demandé ; la
#   session détruit par l'identifiant (R10) et prouve l'absence par un témoin.
# Aucun résultat n'est lu ni imprimé : le journal ne porte que des étapes, des durées, des noms et des comptes de fichiers.
# Variables (--env) : COMMIT, EMPREINTE_RELANCE, ECHEANCE_UTC_S, GO_ID, GH_TOKEN ; BRANCHE_SORTIE (calcul/idee-1-1-jeu-relance-vN) ;
#   posées par le loueur : CONTAINER_ID, CONTAINER_API_KEY. Aucune clé n'est jamais affichée.
# AMORCE_ESSAI_LOCAL=1 : arguments seulement, sortie 0 avant tout réseau et toute écriture. AMORCE_REPETITION=1 (répétition
#   locale) : dépôt jouet file://, jeu factice, loueur simulé, interpréteur donné, durées courtes ; refusées hors répétition.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"; REP="${AMORCE_REPETITION:-0}"
if [ "$REP" != 1 ]; then for v in RACINE_AMORCE DEPOT_URL_REPETITION CURL_REPETITION PY_REPETITION JEU_FACTICE DUREES_REPETITION \
    SEUIL_DISQUE_REPETITION ATTENDRE_MINUTERIE_REPETITION; do [ -z "${!v:-}" ] || { echo "JEU11 REFUS : $v en répétition seulement"; exit 2; }; done; fi
R="${RACINE_AMORCE:-/root}"
T="$R/jeu-idee-1-1-relance-v1"; D="$T/depot"; S="$T/sortie"; X="$T/traces"; L="$X/journal.txt"; V="$T/venv"; VERROU="$T/verrou-sortie"
XT=traces/machine-jeu-idee-1-1-v1
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
API=https://console.vast.ai/api/v0
VERSIONS="3.13.18 2.4.6 1.17.1"; PYTEST_V=9.1.1; PAQUETS="numpy==2.4.6 scipy==1.17.1 pytest==9.1.1"
PREREG=prereg/organisme-idee-1-1-poids-du-nul-v2.md; SHA_PREREG=3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff
AE=prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md; SHA_AE=73ea3bf3ed000444cb446b9dd2af0ae83c090dd97adce78109d7a521ae6c6ccc
RELANCE=prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md
ESSAI_PROJ=docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/essai_projection_cas_v1.py
SHA_ESSAI_PROJ=539f6a6cfce71eaab9010fa9cd16a2607a0bf9faf9499286bcb6fb7f25bda837
DIAG=diag/organisme-idees-juge-v1; MOTIF_RUN='^[0-9]{8}-[0-9]{6}-idee-1-1-poids-du-nul-v5$'; TRANCHES=600
SEUIL_FICHIER=94000000; SEUIL_DISQUE=1073741824
# durées (s) : échéance acceptée au départ dans [48 h 50, 50 h] ; jeu lancé seulement si elle laisse 48 h 40 (borne de 48 h du
# texte comptée depuis depart.json, après les contrôles) ; TERM 20 min avant ; suivi chaque heure ; pas de 30 s ; pause 60 s ;
# borne du texte 48 h (BORNE_JEU)
ECH_MIN=175800; ECH_MAX=180000; MARGE_JEU=175200; MARGE_TERM=1200; PERIODE=3600; PAS=30; PAUSE=60; ESSAIS_DESTR=0; BORNE_JEU=172800
URL="$DEPOT_URL_OFFICIEL"; CURL=curl
if [ "$REP" = 1 ]; then
    URL="${DEPOT_URL_REPETITION:-}"; CURL="${CURL_REPETITION:-}"
    case "$URL" in file:///*) ;; *) echo "JEU11 REFUS : répétition : dépôt jouet file:/// exigé"; exit 2;; esac
    [ -x "$CURL" ] || { echo "JEU11 REFUS : répétition : loueur simulé (CURL_REPETITION) exigé"; exit 2; }
    read -r ECH_MIN ECH_MAX MARGE_JEU MARGE_TERM PERIODE PAS PAUSE ESSAIS_DESTR BORNE_JEU <<< "${DUREES_REPETITION:-}"
    SEUIL_DISQUE="${SEUIL_DISQUE_REPETITION:-$SEUIL_DISQUE}"
fi
BR="${BRANCHE_SORTIE:-calcul/idee-1-1-jeu-relance-v1}"
# 0. arguments
for v in COMMIT EMPREINTE_RELANCE ECHEANCE_UTC_S GO_ID; do [ -n "${!v:-}" ] || { echo "JEU11 REFUS : variable $v absente"; exit 2; }; done
printf '%s' "$COMMIT" | grep -qxE '[0-9a-f]{40}' || { echo "JEU11 REFUS : COMMIT de 40 caractères hexadécimaux attendu"; exit 2; }
printf '%s' "$EMPREINTE_RELANCE" | grep -qxE '[0-9a-f]{64}' || { echo "JEU11 REFUS : EMPREINTE_RELANCE illisible"; exit 2; }
printf '%s' "$GO_ID" | grep -qxE 'GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}' || { echo "JEU11 REFUS : GO_ID illisible"; exit 2; }
printf '%s' "$BR" | grep -qxE 'calcul/idee-1-1-jeu-relance-v[1-9][0-9]*' || { echo "JEU11 REFUS : BRANCHE_SORTIE illisible"; exit 2; }
for v in ECHEANCE_UTC_S ECH_MIN ECH_MAX MARGE_JEU MARGE_TERM PERIODE PAS PAUSE ESSAIS_DESTR BORNE_JEU SEUIL_DISQUE; do
    printf '%s' "${!v:-}" | grep -qxE '[0-9]+' || { echo "JEU11 REFUS : $v illisible"; exit 2; }; done
ECH="$ECHEANCE_UTC_S"
if [ "$ESSAI" = 1 ]; then echo "JEU11 ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
MAINTENANT=$(date +%s)
[ "$ECH" -ge $((MAINTENANT + ECH_MIN)) ] && [ "$ECH" -le $((MAINTENANT + ECH_MAX)) ] || { echo "JEU11 REFUS : échéance hors de [maintenant + $ECH_MIN s, + $ECH_MAX s]"; exit 2; }
printf '%s' "${CONTAINER_ID:-}" | grep -qxE '[0-9]+' || { echo "JEU11 REFUS : identifiant de la machine illisible"; exit 2; }
[ ! -e "$T" ] || { echo "JEU11 REFUS : $T existe déjà (R12)"; exit 2; }
mkdir -p "$X" || { echo "JEU11 REFUS : $X impossible"; exit 2; }
export TZ=UTC PYTHONDONTWRITEBYTECODE=1 GIT_TERMINAL_PROMPT=0 GIT_HTTP_LOW_SPEED_LIMIT=1000 GIT_HTTP_LOW_SPEED_TIME=120
j() { printf '%s JEU11 %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
SORTIE_PRETE=0; RUN=""; PID_SUIVI=""; PID_MINUTERIE=""
api() {  # $1 = DELETE ou STOP ; rend le code HTTP, jamais jugé (seule la liste des instances, lue par la session, prouve)
    local c
    if [ "$1" = DELETE ]; then c=$("$CURL" -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    else c=$("$CURL" -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; fi
    printf '%s' "$c"; }
dossier_du_run() { find "$D/$DIAG" -mindepth 1 -maxdepth 1 -type d -name '*-idee-1-1-poids-du-nul-v5' 2>/dev/null | sort | head -n 1; }
etat() {  # comptes de fichiers et dates de fichiers seulement : aucun contenu de sortie n'est ouvert
    local dd n=0 dep="" now p; now=$(date +%s); dd=$(dossier_du_run); p=$(cat "$X/pid-jeu.txt" 2>/dev/null)
    [ -n "$dd" ] && n=$(find "$dd/lignes" -maxdepth 1 -type f -name '*.json' 2>/dev/null | wc -l)
    [ -n "$dd" ] && [ -f "$dd/depart.json" ] && dep=$(stat -c %Y "$dd/depart.json")
    { echo "utc $(date -u +%FT%TZ) ; machine $CONTAINER_ID ; échéance $(date -u -d "@$ECH" +%FT%TZ) ; commit $COMMIT"
      if [ -n "$p" ]; then kill -0 "$p" 2>/dev/null && echo "jeu : PID $p vivant" || echo "jeu : PID $p fini ou absent"; else echo "jeu : pas encore lancé"; fi
      echo "run : ${dd##*/} ; tranches scellées (fichiers lignes/*.json comptés, jamais ouverts) : $n sur $TRANCHES"
      if [ -n "$dep" ]; then echo "écoulé depuis la date du fichier depart.json : $((now - dep)) s (borne du texte : $BORNE_JEU s)"
          [ "$n" -gt 0 ] && echo "projection linéaire de la durée du jeu : $(( (now - dep) * TRANCHES / n )) s"; fi
      [ -n "$dd" ] && echo "sortie.json : $([ -e "$dd/sortie.json" ] && echo présent || echo absent) ; arret.json : $([ -e "$dd/arret.json" ] && echo présent || echo absent)"
      echo "charge $(cut -d' ' -f1-3 /proc/loadavg) ; disque libre $(df -P -B1 "$T" | awk 'NR == 2 { print $4 }') octets"; } > "$X/etat.txt" 2>/dev/null; }
# >>> poussee (une seule fonction pousse ; chemins permis seulement ; verrou partagé par le suivi, la minuterie et la fin)
permis() {  # chemin relatif à $S : traces de la machine ; runs/<run>/ et diag/organisme-idees-juge-v1/<run>/ une fois le run connu
    case "$1" in "$XT"/*) return 0;; esac
    [ -n "$RUN" ] || return 1
    case "$1" in "runs/$RUN"/*|"$DIAG/$RUN"/*) return 0;; esac
    return 1; }
commit_pousser() {  # $1 = message ; l'index de $S porte les ajouts ; un commit non poussé l'est à l'appel suivant
    local x n
    while IFS= read -r -d '' x; do
        permis "$x" || { j "REFUS DE POUSSEE : chemin hors des sorties permises : $x"; return 3; }
        [ "$(stat -c %s "$S/$x")" -le "$SEUIL_FICHIER" ] || { j "REFUS DE POUSSEE : fichier de plus de $SEUIL_FICHIER octets : $x"; return 3; }
    done < <(git -C "$S" diff --cached --name-only -z)
    git -C "$S" diff --cached --quiet || git -C "$S" commit -q -m "$1" || return 1
    git -C "$S" rev-parse -q --verify HEAD > /dev/null || return 1
    for n in 1 2 3; do git -C "$S" push -q origin "HEAD:refs/heads/$BR" 2>> "$X/poussees.err" \
        && { j "poussé : $(git -C "$S" rev-parse --short HEAD) « $1 »"; return 0; }; sleep $((PAS * n)); done
    return 1; }
pousser_traces() {  # $1 = message ; journal, état, sorties de l'installation et du jeu (stdout, stderr)
    ( flock -w 300 9 || exit 1; mkdir -p "$S/$XT" && find "$X" -maxdepth 1 -type f ! -name pid-jeu.txt ! -name .sortie-prete -exec cp -f {} "$S/$XT/" \; \
      && git -C "$S" add -f -- "$XT" && commit_pousser "$1" ) 9> "$VERROU"; }
# <<< poussee
fin_machine() {  # $1 = code : journal poussé, puis état « stopped » demandé ; la session détruit par l'identifiant (R10)
    local c
    [ -n "$PID_SUIVI" ] && kill "$PID_SUIVI" 2> /dev/null
    j "fin, code $1 ; état « stopped » demandé maintenant ; la session détruit par l'identifiant et prouve l'absence par un témoin"
    [ "$SORTIE_PRETE" = 1 ] && { etat; pousser_traces "fin de la machine, code $1" || j "journal de fin non poussé"; }
    c=$(api STOP); j "état « stopped » demandé : HTTP $c"
    if [ "$REP" = 1 ]; then
        if [ "${ATTENDRE_MINUTERIE_REPETITION:-0}" = 1 ]; then wait "$PID_MINUTERIE"; else kill "$PID_MINUTERIE" 2> /dev/null; fi
        exit "$1"; fi
    sleep infinity; exit "$1"; }
arret() { j "ARRET : $1"; [ "$SORTIE_PRETE" = 1 ] && { etat; pousser_traces "arrêt : $1" || j "traces de l'arrêt non poussées"; }; fin_machine "${2:-2}"; }
# >>> minuterie (R10 : le jeu par son PID, la machine par son identifiant ; une destruction n'est jamais jugée par un code)
minuterie() {
    local n=0 c p dd dep
    while [ "$(date +%s)" -lt $((ECH - MARGE_TERM)) ]; do sleep "$PAS"; done
    p=$(cat "$X/pid-jeu.txt" 2>/dev/null); dd=$(dossier_du_run); dep=$( [ -n "$dd" ] && stat -c %Y "$dd/depart.json" 2>/dev/null)
    if [ -n "$p" ] && kill -0 "$p" 2> /dev/null; then
        if [ -n "$dep" ] && [ $(( $(date +%s) - dep )) -gt "$BORNE_JEU" ]; then
            j "MINUTERIE : jeu (PID $p) vivant au-delà de sa borne de 48 h depuis depart.json : TERM par son PID (arret.json attendu ; run déjà invalide)"
            kill -TERM "$p"
        else j "MINUTERIE : jeu (PID $p) vivant et dans sa borne (ou depart.json absent) : la minuterie ne le coupe pas ; la destruction à l'échéance le tuera (run invalide)"; fi
    fi
    while [ "$(date +%s)" -lt "$ECH" ]; do sleep "$PAS"; done
    j "MINUTERIE : échéance atteinte : journal poussé, puis destruction de la machine $CONTAINER_ID par son identifiant (DELETE)"
    [ -e "$X/.sortie-prete" ] && { etat; pousser_traces "minuterie : échéance" || j "MINUTERIE : journal non poussé"; }
    while :; do n=$((n + 1)); c=$(api DELETE)
        j "MINUTERIE : DELETE, essai $n : HTTP $c (jamais jugé ; seule l'absence dans la liste des instances, lue par la session, prouve)"
        [ "$n" = 5 ] && { c=$(api STOP); j "MINUTERIE : toujours vivante après 5 demandes : état « stopped » demandé : HTTP $c"; }
        [ "$ESSAIS_DESTR" != 0 ] && [ "$n" -ge "$ESSAIS_DESTR" ] && return 0
        sleep "$PAUSE"; done; }
# <<< minuterie
minuterie < /dev/null & PID_MINUTERIE=$!
j "minuterie lancée (PID $PID_MINUTERIE, échéance $(date -u -d "@$ECH" +%FT%TZ)) ; commit $COMMIT ; GO $GO_ID ; branche de sortie $BR"
# 1. outils, processeur, clé
for o in git curl python3 sha256sum awk sed grep stat find sort df nproc timeout flock cmp base64 cut wc; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ "$(uname -m)" = x86_64 ] || arret "processeur $(uname -m) : x86_64 exigé" 2
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
lscpu > "$X/lscpu.txt" 2>&1 || true
j "machine : $(nproc) processeurs, $(awk '/MemTotal/ { print $2 }' /proc/meminfo) kio, $(grep -m 1 'Model name' "$X/lscpu.txt" | cut -c1-120 | tr -s ' ')"
# 2. branche de sortie neuve, dépôt de sortie à part, première poussée
git -c credential.helper="$AIDE" ls-remote --exit-code "$URL" "refs/heads/$BR" > /dev/null 2>&1; c=$?
[ "$c" = 2 ] || arret "branche $BR présente sur le dépôt distant (R12) ou dépôt injoignable (ls-remote, code $c) : nouveau nom exigé" 2
git init -q -b "$BR" "$S" && git -C "$S" config credential.helper "$AIDE" && git -C "$S" config user.name "machine du jeu de l'idée 1.1" \
    && git -C "$S" config user.email "machine-calcul@invalid" && git -C "$S" remote add origin "$URL" || arret "dépôt de sortie" 2
etat; pousser_traces "machine du jeu relancé de l'idée 1.1 : départ" || arret "première poussée du journal impossible" 2
SORTIE_PRETE=1; : > "$X/.sortie-prete"
suivi() { while :; do sleep "$PERIODE"; etat; pousser_traces "suivi : $(date -u +%FT%TZ)" || j "suivi : poussée impossible (nouvel essai à la prochaine période)"; done; }
suivi < /dev/null & PID_SUIVI=$!
j "branche de sortie $BR créée (orpheline) ; suivi poussé toutes les $PERIODE s (PID $PID_SUIVI)"
# 3. Python, paquets, contrôle des versions (avant tout calcul)
if [ "$REP" = 1 ]; then PY="${PY_REPETITION:-}"; [ -x "$PY" ] || arret "répétition : interpréteur PY_REPETITION absent" 2
else
    LU=$(python3 -I -c 'import sys; print(sys.version.split()[0])' 2>&1); [ "$LU" = "${VERSIONS%% *}" ] || arret "Python de l'image « $LU » ≠ ${VERSIONS%% *}" 2
    python3 -m venv "$V" > "$X/venv.txt" 2>&1 || arret "environnement Python" 2
    timeout -k 10 1800 "$V/bin/pip" install -q --no-cache-dir --disable-pip-version-check $PAQUETS > "$X/pip.txt" 2>&1 || arret "installation des paquets (pip.txt)" 2
    PY="$V/bin/python"; fi
LU=$("$PY" -I -c "import sys; from importlib import metadata as m; print(sys.version.split()[0], m.version('numpy'), m.version('scipy'))" 2> "$X/versions.err")
printf '%s\n' "$LU" > "$X/versions.txt"
j "contrôle des versions (addendum de relance, 4.2) : « $LU » ; attendu « $VERSIONS »"
[ "$LU" = "$VERSIONS" ] || arret "versions « $LU » ≠ « $VERSIONS » : pas de relance sous cet addendum ; arrêt avant tout calcul" 2
LU=$("$PY" -I -c "from importlib import metadata as m; print(m.version('pytest'))" 2>&1); [ "$LU" = "$PYTEST_V" ] || arret "pytest « $LU » ≠ $PYTEST_V" 2
"$PY" -I -m pip freeze --all > "$X/pip-freeze.txt" 2>&1; "$PY" -I -c 'import numpy; numpy.show_runtime()' > "$X/numpy-runtime.txt" 2>&1
# 4. dépôt au commit
[ ! -e "$D" ] || arret "$D existe déjà (R12)" 2
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch main "$URL" "$D" > "$X/clone.txt" 2>&1 || arret "clonage (clone.txt)" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" remote set-url --push origin "interdit://aucune-poussee-depuis-le-depot-du-jeu"
git -C "$D" cat-file -e "$COMMIT^{commit}" 2> /dev/null || arret "commit $COMMIT absent de main" 2
git -C "$D" merge-base --is-ancestor "$COMMIT" refs/remotes/origin/main || arret "commit $COMMIT : pas un ancêtre de main" 2
git -C "$D" checkout -q --detach "$COMMIT" > "$X/checkout.txt" 2>&1 || arret "extraction du commit (checkout.txt)" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
[ -z "$(git -C "$D" status --porcelain --untracked-files=all)" ] || arret "arbre non propre au commit" 2
# 5. empreintes, sorties antérieures, disque
sha() { sha256sum "$D/$1" 2> /dev/null | cut -d' ' -f1; }
compagnon_seul() {  # $1 = chemin : compagnon d'une ligne « <empreinte>  <nom> », égal au fichier
    local c="$D/$1.sha256"; [ -f "$c" ] && [ "$(grep -c '' "$c")" = 1 ] && [ "$(cat "$c")" = "$(sha "$1")  $(basename "$1")" ]; }
[ "$(sha "$PREREG")" = "$SHA_PREREG" ] || arret "texte scellé $PREREG ≠ ${SHA_PREREG:0:12}…" 2
[ "$(sha "$AE")" = "$SHA_AE" ] && compagnon_seul "$AE" || arret "addendum d'empreintes ≠ ${SHA_AE:0:12}… ou compagnon faux" 2
compagnon_seul "$RELANCE" || arret "addendum de relance absent au commit, ou différent de son compagnon" 2
[ "$(sha "$RELANCE")" = "$EMPREINTE_RELANCE" ] || arret "addendum de relance $(sha "$RELANCE" | cut -c1-12)… ≠ EMPREINTE_RELANCE ${EMPREINTE_RELANCE:0:12}…" 2
[ "$(sha "$ESSAI_PROJ")" = "$SHA_ESSAI_PROJ" ] || arret "essai du § 6 point 3 de l'addendum d'empreintes ≠ ${SHA_ESSAI_PROJ:0:12}…" 2
A=$(find "$D/runs" "$D/$DIAG" -mindepth 1 -maxdepth 1 -name '*idee-1-1-poids-du-nul-v[1-5]' 2> /dev/null | head -n 3)
[ -z "$A" ] || arret "sortie ou manifeste antérieur de ce jeu au commit (le lanceur refuserait) : $(printf '%s' "$A" | tr '\n' ' ')" 2
LIBRE=$(df -P -B1 "$T" | awk 'NR == 2 { print $4 }'); [ "$LIBRE" -ge "$SEUIL_DISQUE" ] || arret "disque libre $LIBRE octets < $SEUIL_DISQUE (précaution de l'addendum de relance, 4.4)" 2
j "commit $COMMIT extrait, arbre propre ; texte, addendum d'empreintes, addendum de relance ($EMPREINTE_RELANCE), essai : conformes ; aucune sortie antérieure ; disque libre $LIBRE octets"
# 6. jeu
[ $((ECH - $(date +%s))) -ge "$MARGE_JEU" ] || arret "échéance trop proche pour la borne de 48 h du texte (moins de $MARGE_JEU s) : pas de jeu" 2
if [ "$REP" = 1 ]; then JEU=("$PY" -I -B "${JEU_FACTICE:-/inexistant}" --addendum "$AE"); else JEU=("$PY" -I -B scripts/jouer_idee_1_1_v5.py --addendum "$AE"); fi
etat; pousser_traces "avant le jeu : commit, empreintes, versions, lieu, espace libre" || arret "poussée d'avant le jeu impossible" 2
( cd "$D" && exec "${JEU[@]}" ) > "$X/jeu.txt" 2> "$X/jeu.err" < /dev/null & PID_JEU=$!
printf '%s\n' "$PID_JEU" > "$X/pid-jeu.txt"
j "jeu lancé : PID $PID_JEU (parent ; tout arrêt par ce seul PID, R10) ; commande, depuis $D : ${JEU[*]}"
etat; pousser_traces "jeu lancé, PID $PID_JEU" || j "poussée du PID impossible (le suivi la refera)"
wait "$PID_JEU"; CJ=$?
j "jeu fini : code $CJ"
kill "$PID_SUIVI" 2> /dev/null; PID_SUIVI=""
# 7. sorties : vérifiées par leurs compagnons, recopiées, comparées à l'octet, poussées
RUNS=$(find "$D/runs" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' 2> /dev/null | grep -E "$MOTIF_RUN")
[ "$(printf '%s' "$RUNS" | grep -c '^')" = 1 ] || arret "jeu fini (code $CJ) sans run unique de ce jeu (« $(printf '%s' "$RUNS" | tr '\n' ' ')») : traces seules" 4
RUN="$RUNS"
HORS=$(git -C "$D" status --porcelain --untracked-files=all | cut -c4- | grep -v -e "^runs/$RUN/" -e "^$DIAG/$RUN/" | head -n 5)
[ -z "$HORS" ] || j "RESERVE : fichiers écrits par le jeu hors de ses deux dossiers (non poussés) : $(printf '%s' "$HORS" | tr '\n' ' ')"
NF=0; FAUX=""
while IFS= read -r -d '' f; do r=${f#"$D/"}
    case "$f" in *.sha256) [ -f "${f%.sha256}" ] || FAUX="$FAUX $r(sans fichier)"; continue;; esac
    NF=$((NF + 1)); compagnon_seul "$r" || FAUX="$FAUX $r"
done < <(find "$D/runs/$RUN" "$D/$DIAG/$RUN" -type f -print0 2> /dev/null | sort -z)
[ -z "$FAUX" ] && j "sorties : $NF fichiers, chacun égal à son compagnon" || j "RESERVE : sorties sans compagnon ou différentes de lui :$(printf '%s' "$FAUX" | cut -c1-600)"
(   flock -w 600 9 || exit 1
    for p in "runs/$RUN" "$DIAG/$RUN"; do [ -d "$D/$p" ] || continue; mkdir -p "$S/$(dirname "$p")" && cp -a "$D/$p" "$S/$p" || exit 1
        diff -r -q "$D/$p" "$S/$p" > /dev/null || exit 1; done
    [ -d "$S/runs/$RUN" ] && { git -C "$S" add -f -- "runs/$RUN" && commit_pousser "sorties du run $RUN : manifeste" || exit 1; }
    mapfile -d '' -t F < <(cd "$S" && find "$DIAG/$RUN" -type f -print0 2> /dev/null | sort -z)
    for ((k = 0; k < ${#F[@]}; k += 400)); do git -C "$S" add -f -- "${F[@]:k:400}" && commit_pousser "sorties du run $RUN : lot $((k / 400 + 1))" || exit 1; done
) 9> "$VERROU" || arret "recopie ou poussée des sorties du run $RUN impossible (sorties restées sur la machine arrêtée ; nœud de la mère)" 4
DD="$D/$DIAG/$RUN"
if [ "$CJ" = 0 ] && [ -f "$DD/sortie.json" ] && [ ! -e "$DD/arret.json" ] && [ -z "$FAUX" ]; then
    j "FIN : jeu mené au bout, run $RUN, sorties scellées poussées sur $BR (aucune ouverte) ; recopie octet pour octet et lecture par la mère"
    fin_machine 0
elif [ -e "$DD/arret.json" ]; then arret "jeu : arrêt écrit (arret.json poussé ; run invalide ; aucune lecture)" 4
else arret "jeu : code $CJ, sortie.json $([ -f "$DD/sortie.json" ] && echo présent || echo absent), compagnons$([ -z "$FAUX" ] && echo ' conformes' || echo ' FAUX') (jeu.err poussé)" 4; fi
