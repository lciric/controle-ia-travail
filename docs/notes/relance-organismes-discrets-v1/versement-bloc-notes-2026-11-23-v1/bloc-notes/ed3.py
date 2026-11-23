p = 'scripts/amorce_ligne_1_bras_a_v3.sh'
s = open(p, encoding='utf-8').read()


def r(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:100])
    s = s.replace(a, b)


r('''# Amorce complète de la machine autonome de la ligne 1 de carte du bras A, version 2 (23 novembre 2026 ; la v1,
# `scripts/amorce_ligne_1_bras_a_v1.sh`, reste telle quelle, jamais contre-lue ni jouée).''',
  '''# Amorce complète de la machine autonome de la ligne 1 de carte du bras A, version 3 (23 novembre 2026 ; les v1 et v2
# restent telles quelles, R12). Lancée par l'amorce d'appel v2 (`scripts/amorce_appel_ligne_1_bras_a_v2.sh`).
# Corrections de la contre-lecture de la v2 (`contre-lecture-machine-autonome-ligne-1-v2.md`) :
#  B1 : `curl` absent : les demandes au loueur passent par `python3` (urllib) ; un outil absent n'arrête plus le
#       processus sans demander l'arrêt de l'instance ;
#  M2 : l'arrêt est redemandé en boucle (délai croissant, borné à 10 min), avec relecture de l'état par GET (seuls
#       les champs d'état sont écrits) ;
#  M3 : secours à 25 min après l'heure du plafond ; `timeout` sur chaque git réseau (clone, push, ls-remote) et chaque
#       appel au loueur ;
#  m2 : installation et course sans les trois secrets ; téléchargement du modèle avec HF_TOKEN seul ;
#  m3 : `credential.helper` remis à vide avant l'aide (clone et configurations), GIT_TERMINAL_PROMPT=0 ;
#  m4 : étapes longues lancées par `setsid` ; la coupe tue le groupe de processus (`kill -- -PGID`) ;
#  m5 : à la reprise, les états `fin`, `secours` et `destruction-demandee` d'un départ précédent sont effacés ;
#  m10 : un fichier de plus de 100 Mo n'est pas poussé (il reste sur le disque, le manifeste le dit en manquant).
# Écart déclaré : pas de `set -e` ; chaque commande qui compte est testée à la main (`set -uo pipefail`).
# Ce qui suit décrit la v2.''')
r('''export TZ=UTC PYTHONDONTWRITEBYTECODE=1''', '''export TZ=UTC PYTHONDONTWRITEBYTECODE=1 GIT_TERMINAL_PROMPT=0''')
r('''             AMORCE_GRACE_S AMORCE_SECOURS_S \\''', '''             AMORCE_GRACE_S AMORCE_SECOURS_S AMORCE_TAILLE_MAX_O \\''')
r('''SECOURS_S="${AMORCE_SECOURS_S:-3600}"    # fil principal pas fini 60 min après l'heure du plafond : arrêt demandé''',
  '''SECOURS_S="${AMORCE_SECOURS_S:-1500}"    # fil principal pas fini 25 min après l'heure du plafond : arrêt demandé
TAILLE_MAX_O="${AMORCE_TAILLE_MAX_O:-100000000}"   # au-delà, un fichier n'est pas poussé (GitHub refuse 100 Mo)''')
r('''appel_api() {  # $1 méthode, $2 corps JSON ou vide ; imprime le code HTTP
    local c
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo 000; return 1;; esac
    if [ -n "$2" ]; then
        c=$(printf 'header = "Authorization: Bearer %s"\\n' "${CONTAINER_API_KEY:-}" | "$CURL" -K - -sS -m 60 -o /dev/null \\
            -w '%{http_code}' -X "$1" -H 'Content-Type: application/json' -d "$2" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    else
        c=$(printf 'header = "Authorization: Bearer %s"\\n' "${CONTAINER_API_KEY:-}" | "$CURL" -K - -sS -m 60 -o /dev/null \\
            -w '%{http_code}' -X "$1" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    fi
    printf '%s\\n' "$c"; }''', '''appel_python() {  # $1 méthode, $2 corps ; repli sans curl (B1) : bibliothèque standard, clé lue par son nom
    APPEL_URL="$API/instances/$CONTAINER_ID/" APPEL_METHODE="$1" APPEL_CORPS="$2" timeout 90 "$PYS" -I -c 'import os, urllib.request as u
e = os.environ
d = e["APPEL_CORPS"].encode() or None
q = u.Request(e["APPEL_URL"], d, {"Authorization": "Bearer " + e.get("CONTAINER_API_KEY", ""),
              "Content-Type": "application/json"}, method=e["APPEL_METHODE"])
try:
    print(u.urlopen(q, timeout=60).status)
except Exception as x:
    print(getattr(x, "code", 0) or "000")' 2>/dev/null || echo 000; }
appel_api() {  # $1 méthode, $2 corps JSON ou vide ; imprime le code HTTP
    local c
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo 000; return 1;; esac
    if ! command -v "$CURL" > /dev/null; then appel_python "$1" "$2"; return 0; fi
    if [ -n "$2" ]; then
        c=$(printf 'header = "Authorization: Bearer %s"\\n' "${CONTAINER_API_KEY:-}" | timeout 90 "$CURL" -K - -sS -m 60 -o /dev/null \\
            -w '%{http_code}' -X "$1" -H 'Content-Type: application/json' -d "$2" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    else
        c=$(printf 'header = "Authorization: Bearer %s"\\n' "${CONTAINER_API_KEY:-}" | timeout 90 "$CURL" -K - -sS -m 60 -o /dev/null \\
            -w '%{http_code}' -X "$1" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    fi
    printf '%s\\n' "$c"; }
lire_statut() {  # GET de l'instance ; seuls les champs d'état sont imprimés (la fiche porte les variables -e)
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "illisible"; return 0;; esac
    command -v "$CURL" > /dev/null || { echo "non lu (curl absent)"; return 0; }
    printf 'header = "Authorization: Bearer %s"\\n' "${CONTAINER_API_KEY:-}" | timeout 90 "$CURL" -K - -sS -m 60 \\
        "$API/instances/$CONTAINER_ID/?owner=me" 2>/dev/null | "$PYS" -I -c 'import json, sys
try:
    i = json.load(sys.stdin)["instances"] or {}
    print("voulu", i.get("intended_status"), "; réel", i.get("actual_status"))
except Exception:
    print("illisible")' 2>/dev/null; }''')
r('''arreter() {  # $1 motif : arrêt simple (disque gardé), jamais une destruction
    local c
    c=$(appel_api PUT '{"state": "stopped"}')
    j "ARRÊT (state=stopped) demandé, disque gardé ($1) : HTTP $c ; la session lit l'état, rapatrie ou repousse, puis détruit par l'identifiant"
    fin 3; }''', '''arreter() {  # $1 motif : arrêt simple (disque gardé), jamais une destruction ; redemandé tant que le processus vit (M2)
    local c n=0
    etat arret-demande
    case "${CONTAINER_ID:-}" in ''|*[!0-9]*) j "ARRÊT IMPOSSIBLE ($1) : identifiant de l'instance illisible ; la session détruit par l'identifiant"; fin 4;; esac
    while :; do n=$((n + 1))
        c=$(appel_api PUT '{"state": "stopped"}')
        j "ARRÊT (state=stopped) demandé, essai $n, disque gardé ($1) : HTTP $c ; état relu : $(lire_statut) ; la session lit l'état, rapatrie ou repousse, puis détruit par l'identifiant"
        if [ "$JOUET" = 1 ]; then case "$c" in 2??) fin 3;; esac; [ "$n" -ge 3 ] && fin 4; fi
        sleep $(( (n < 10 ? n : 10) * ${AMORCE_PAS_ARRET_S:-60} )); done; }''')
r('''        [ -z "${!v:-}" ] || { echo "LIGNE-1 REFUS : $v n'est admise qu'en mode jouet"; exit 2; }; done''',
  '''        [ -z "${!v:-}" ] || { echo "LIGNE-1 REFUS : $v n'est admise qu'en mode jouet"; exit 2; }; done
    [ -z "${AMORCE_PAS_ARRET_S:-}" ] || { echo "LIGNE-1 REFUS : AMORCE_PAS_ARRET_S n'est admise qu'en mode jouet"; exit 2; }''')
r('''REPRISE=0; a_etat amorce-commencee && REPRISE=1''',
  '''REPRISE=0; a_etat amorce-commencee && REPRISE=1
[ "$REPRISE" = 1 ] && rm -f "$M/fin" "$M/secours" "$M/destruction-demandee" "$M/arret-demande"   # m5''')
r('''for o in git "$CURL" "$PYS" sha256sum awk sed grep date; do command -v "$o" > /dev/null || { j "outil absent : $o"; fin 2; }; done''',
  '''command -v "$CURL" > /dev/null || j "curl absent : les demandes au loueur passent par python3 (bibliothèque standard)"
for o in git "$PYS" sha256sum awk sed grep date timeout setsid; do
    command -v "$o" > /dev/null || { j "outil absent : $o"; arreter "outil absent : $o"; }; done''')
r('''    pid=$(lire_etat etape-pid)
    case "$pid" in ''|*[!0-9]*) ;; *) kill -TERM "$pid" 2>/dev/null && j "MINUTERIE : TERM envoyé au PID $pid"
        sleep "$PAS"; kill -0 "$pid" 2>/dev/null && kill -KILL "$pid" 2>/dev/null && j "MINUTERIE : KILL envoyé au PID $pid";; esac; }''',
  '''    pid=$(lire_etat etape-pid)          # lancée par setsid : PID = numéro du groupe ; tout le groupe est coupé (m4)
    case "$pid" in ''|*[!0-9]*) ;; *) { kill -TERM -- "-$pid" 2>/dev/null || kill -TERM "$pid" 2>/dev/null; } \\
            && j "MINUTERIE : TERM envoyé au groupe $pid"
        sleep "$PAS"; kill -0 "$pid" 2>/dev/null && { kill -KILL -- "-$pid" 2>/dev/null || kill -KILL "$pid"; } 2>/dev/null \\
            && j "MINUTERIE : KILL envoyé au groupe $pid";; esac; }''')
r('''if a_etat plafond-atteint && ! a_etat fin && ! a_etat secours && ! a_etat destruction-demandee &&''',
  '''if a_etat plafond-atteint && ! a_etat fin && ! a_etat secours && ! a_etat destruction-demandee && ! a_etat arret-demande &&''')
r('''    "$@" > "$f" 2>&1 < /dev/null & pid=$!''', '''    setsid "$@" > "$f" 2>&1 < /dev/null & pid=$!''')
r('''    cp "$L" "$VD/journal-amorce.txt"; masquer_fichier "$VD/journal-amorce.txt"''',
  '''    : > "$T/gros.txt"
    while IFS= read -r -d '' f; do       # m10 : plus de TAILLE_MAX_O octets : gardé sur le disque, non poussé, dit
        rel=${f#"$VD/"}; mkdir -p "$T/hors-versement/$(dirname "$rel")" && mv "$f" "$T/hors-versement/$rel" \\
            && printf '%s\\n' "$rel" >> "$T/gros.txt" && j "fichier de plus de $TAILLE_MAX_O octets gardé sur le disque, non poussé : $rel"
    done < <(find "$VD" -type f -size +"${TAILLE_MAX_O}"c -print0)
    cp "$L" "$VD/journal-amorce.txt"; masquer_fichier "$VD/journal-amorce.txt"''')
r('''    git init -q -b "$BR_SORTIE" "$G" && git -C "$G" config user.name "machine de la ligne 1 (bras A)" \\
        && git -C "$G" config user.email machine-ligne-1@invalid && git -C "$G" config credential.helper "$AIDE" \\''',
  '''    git init -q -b "$BR_SORTIE" "$G" && git -C "$G" config user.name "machine de la ligne 1 (bras A)" \\
        && git -C "$G" config user.email machine-ligne-1@invalid && git -C "$G" config credential.helper '' \\
        && git -C "$G" config --add credential.helper "$AIDE" \\''')
r('''        git -C "$G" push -q origin''', '''        timeout 900 git -C "$G" push -q origin''')
r('''lu=$(git -C "$G" ls-remote origin''', '''lu=$(timeout 300 git -C "$G" ls-remote origin''', 2)
r('''    [ "$(git -C "$E" config credential.helper)" = "$AIDE" ] || git -C "$E" config credential.helper "$AIDE"''',
  '''    [ "$(git -C "$E" config credential.helper)" = "$AIDE" ] \\
        || { git -C "$E" config --unset-all credential.helper; git -C "$E" config credential.helper '' \\
             && git -C "$E" config --add credential.helper "$AIDE"; }''')
r('''    if ! git -c credential.helper="$AIDE" clone -q --depth 1''', '''    if ! timeout 900 git -c credential.helper= -c credential.helper="$AIDE" clone -q --depth 1''')
r('''    git -C "$E" config credential.helper "$AIDE"        # avant toute extraction et toute poussée (R-5101)''',
  '''    git -C "$E" config credential.helper '' && git -C "$E" config --add credential.helper "$AIDE"   # avant l'extraction (R-5101)''')
r('''    etape_longue "$T/installation.txt" bash -c "python3 -m venv '$T/venv' && '$T/venv/bin/pip' install -q -r '$E/requirements-gpu.txt'" \\''',
  '''    etape_longue "$T/installation.txt" env -u GH_TOKEN -u HF_TOKEN -u CONTAINER_API_KEY \\
        bash -c "python3 -m venv '$T/venv' && exec '$T/venv/bin/pip' install -q -r '$E/requirements-gpu.txt'" \\''')
r('''bash -c "cd '$E' && PYTHONPATH=src '$PYV' -c 'import json, sys''', '''bash -c "cd '$E' && PYTHONPATH=src exec '$PYV' -c 'import json, sys''')
r('j "amorce v2 : départ', 'j "amorce v3 : départ')
open(p, 'w', encoding='utf-8').write(s)
