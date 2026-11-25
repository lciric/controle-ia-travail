#!/usr/bin/env bash
# [v4 (écart matériel minimal autorisé par Lazar : GO-2026-11-25-01, R-5397) ; nom neuf, R12 : la v3 reste telle quelle.
# Changent seulement : les gardes avant calcul (`controles_v3` : `stockage_max_usd_h` relevé de `0.08` à `0.10` USD/h),
# la course jouée (`controle_ia.dose_reponse.course_v3`), la liste d'essais figée (`scripts/tests-cibles-dose-reponse-v4.txt`,
# empreinte et compte écrits en dur) et la ligne de démarrage « AMORCE DR v4 » ; rien d'autre.]
# [v3 (mot de Lazar GO-2026-11-24-31 : course désignée pour le critère 3, option A) ; nom neuf, R12 : la v2 reste telle quelle.
# Changent seulement : les fichiers cités extraits sur l'instance sont listés par `controle_ia.dose_reponse.extraction_v1`
# (bibliothèque standard), qui ajoute `designation_critere_3.chemin` quand la clé n'est pas `null` (la v2 ne l'extrayait pas :
# arrêt après l'installation sur une course désignée) ; la liste d'essais figée (`scripts/tests-cibles-dose-reponse-v3.txt`) ;
# la ligne de démarrage « AMORCE DR v3 ».]
# [v2, après la contre-lecture 1 du code ; nom neuf, R12 : la v1 reste telle quelle. Changent seulement : la course jouée
# (`controle_ia.dose_reponse.course_v2`), les gardes avant calcul (`controles_v2` : configuration égale à celle que
# reconstruit le code, ligne CODE citant le commit du code), la liste d'essais figée (`scripts/tests-cibles-dose-reponse-v2.txt`,
# empreinte et compte écrits en dur), la ligne de démarrage « AMORCE DR v2 ».]
# Amorce de l'instance de la course de dose–réponse de l'organisme à consigne cachée, v1 (texte scellé
# `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, 2263c5c4… ; GO de calcul reçu du lanceur). Copie adaptée de
# `scripts/amorce_instance_t08_v1.sh` (qui reste telle quelle, R12) ; changent : les noms (`dr`), le clonage (commit de
# lancement LANCEMENT sur la branche BRANCHE_LANCEMENT, dont le code est celui du commit COMMIT_CODE cité par la ligne
# CODE-DOSE-REPONSE-CONSIGNE-CACHEE : `git diff` vide sur le code entre les deux, COMMIT_CODE ancêtre ; extraction limitée au
# code, aux registres lus et aux fichiers que cite la configuration), les gardes avant calcul (`dose_reponse.controles_v1`
# sur le commit de lancement : texte scellé, pièce jointe, textes du premier test, banque, modules repris, lignes du
# registre, bornes de l'offre), la suite d'essais ciblée et figée, un seul modèle (l'agent), la commande jouée
# (`controle_ia.dose_reponse.course_v1`, une fois, poussée à la fin de chaque bloc de tâche par le script de consignation),
# la reprise facultative (REPRISE_BRANCHE et REPRISE_RUN : blocs scellés d'une course antérieure recopiés tels quels) et les
# essais de chaîne facultatifs (ESSAIS : nombre d'épisodes honnêtes, seize au plus). Inchangé : minuterie détachée
# (échéance ; heure d'épuisement du plafond cumulé de 90 USD calculée à la création : consignation, poussée, destruction),
# verrou de consignation, refus annoncés puis destruction, aucun couperet de temps sur la course, destruction après le
# versement prouvé (sinon arrêt, disque gardé), relais des seules lignes PROGRES de comptes.
# Variables (--env) : LANCEMENT, BRANCHE_LANCEMENT, COMMIT_CODE, CONFIG, PREREG, BRANCHE, GO_ID_DR, DEPOT_URL, ECHEANCE_UTC_S,
# FIN_GO_UTC_S, DEPENSE_EPUISEE_UTC_S, HF_TOKEN, GH_TOKEN ; facultatives : REPRISE_BRANCHE, REPRISE_RUN, ESSAIS ; posées par
# Vast : CONTAINER_ID, CONTAINER_API_KEY. Essai local : RACINE_AMORCE, AMORCE_ESSAI_LOCAL=1, MINUTERIE_PAS_S,
# MINUTERIE_REESSAI_S, MINUTERIE_MARGE_S, POUSSEE_ATTENTE_S.
set -uo pipefail
R="${RACINE_AMORCE:-/root}"
API="${API_VAST:-https://console.vast.ai/api/v0}"
GO_ID="${GO_ID_DR:-}"
MORCEAU_MAX="${MORCEAU_MAX_OCTETS:-90000000}"
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
export HOME="${HOME:-/root}" TZ=UTC
cd "$R" || { echo "AMORCE DR : racine $R inaccessible : sleep infinity"; sleep infinity; exit 1; }
N_DEM=0; [ -s "$R/dr-demarrages.txt" ] && read -r N_DEM < "$R/dr-demarrages.txt"
case "$N_DEM" in ''|*[!0-9]*) N_DEM=0;; esac
N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/dr-demarrages.txt"
printf 'AMORCE DR v4 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, lancement %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${LANCEMENT:-?}"
IFS= read -r -d '' MINUTERIE_TXT <<'MINUTERIE'
ECH="$1"; DEP="$2"; R="$3"; API="$4"; J="$R/dr-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac; case "$DEP" in ''|*[!0-9]*) DEP=0;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH, dépense épuisée à $DEP" >> "$J"
echo "$$" > "$R/dr-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
consigner() {
    if [ -f "$R/dr-consigner.sh" ]; then timeout -k 10 2400 bash "$R/dr-consigner.sh" "$1" >> "$J" 2>&1; echo "$(date -u +%FT%TZ) consigné ($1) : code $?" >> "$J"
    else echo "$(date -u +%FT%TZ) rien à consigner ($1) : dépôt non extrait" >> "$J"; fi; }
appel() {
    local c
    if command -v curl >/dev/null 2>&1; then
        if [ -n "$2" ]; then c=$(curl -sS -m 60 -o "$R/dr-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" -H 'Content-Type: application/json' -d "$2" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
        else c=$(curl -sS -m 60 -o "$R/dr-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; fi
    else c=aucun; fi
    echo "$c"
}
raison=""
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/dr-detruire" ]; do
    if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/dr-depense-epuisee" ]; then
        echo "$(date -u +%FT%TZ) DÉPENSE ÉPUISÉE (plafond cumulé de la course atteint, 90 USD) : consignation, poussée, puis destruction" >> "$J"
        echo "dépense épuisée $(date -u +%FT%TZ)" > "$R/dr-depense-epuisee"
        consigner "dépense épuisée"
        raison="dépense épuisée"; break
    fi
    sleep "$PAS"
done
[ -n "$raison" ] || { raison="échéance"; [ -e "$R/dr-detruire" ] && raison="ordre de l'amorce"; }
if [ "$raison" = "échéance" ]; then echo "$(date -u +%FT%TZ) ÉCHÉANCE $ECH atteinte : consignation et poussée des résultats partiels avant la destruction" >> "$J"; consigner "échéance"; fi
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do
    n=$((n + 1))
    if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue avant la fin de la marge" >> "$J"; exit 4; fi
    c=$(appel DELETE '')
    if [ "$c" = aucun ]; then echo "$(date -u +%FT%TZ) ALARME : curl absent : aucune destruction possible" >> "$J"; exit 5; fi
    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/dr-api-corps.txt" 2>/dev/null && refus=oui
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n, $raison) : HTTP $c, refus dans le corps : $refus" >> "$J"
    case "$c" in 2??) if [ "$refus" = non ]; then echo "$(date -u +%FT%TZ) instance $CONTAINER_ID détruite" >> "$J"; exit 0; fi;; esac
    [ "$(date +%s)" -lt "$FIN" ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue" >> "$J"; exit 4; }
    sleep "$REESSAI"
done
MINUTERIE
printf '%s' "$MINUTERIE_TXT" > "$R/dr-minuterie.sh" || { echo "AMORCE DR : minuterie impossible à écrire"; [ "$ESSAI" = 1 ] && exit 1; sleep infinity; exit 1; }
[ "${AMORCE_MINUTERIE_SEULE:-0}" = 1 ] && [ "$ESSAI" = 1 ] && { echo "AMORCE DR : minuterie écrite (essai local)"; exit 0; }
PM=""
attendre_minuterie() { local lim=$(( $(date +%s) + ${MINUTERIE_MARGE_S:-1800} + 120 )); while [ -n "$PM" ] && kill -0 "$PM" 2>/dev/null && [ "$(date +%s)" -lt "$lim" ]; do sleep 2; done; }
detruire() {
    echo "$1" > "$R/dr-detruire"; echo "AMORCE $(date -u +%FT%TZ) : destruction demandée ($1)"
    if [ "$ESSAI" = 1 ]; then exit "${2:-2}"; fi
    attendre_minuterie
    local st=124; { [ -n "$PM" ] && ! kill -0 "$PM" 2>/dev/null; } && { wait "$PM" 2>/dev/null; st=$?; }
    [ "$st" = 0 ] && exit "${2:-2}"
    echo "AMORCE $(date -u +%FT%TZ) : destruction non obtenue (minuterie, code $st) : sleep infinity ; la session détruit par l'identifiant"
    sleep infinity; exit "${2:-2}"; }
REFUS_ATTENTE_S=180
[ "$ESSAI" = 1 ] && REFUS_ATTENTE_S="${REFUS_ATTENTE_ESSAI_S:-0}"
attente_refus() { echo "AMORCE $(date -u +%FT%TZ) : refus annoncé : destruction demandée dans ${REFUS_ATTENTE_S} s"; sleep "$REFUS_ATTENTE_S"; }
refus() { echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; detruire "refus : $1" 2; }
refus_precoce() {
    echo "AMORCE $(date -u +%FT%TZ) : refus : $1 : rien ne part"; attente_refus; echo "refus : $1" > "$R/dr-detruire"
    if [ "$ESSAI" = 1 ]; then exit 2; fi
    bash "$R/dr-minuterie.sh" 0 0 "$R" "$API" < /dev/null >> "$R/dr-minuterie.log" 2>&1; sleep infinity; exit 2; }
versement_prouve() { local l r; l=$(git -C "$R/amorce-depot" rev-parse HEAD 2>/dev/null) || return 1
    r=$(timeout -k 5 120 git -C "$R/amorce-depot" ls-remote origin "refs/heads/$1" 2>/dev/null | cut -f1)
    [ -n "$1" ] && [ -n "$l" ] && [ "$l" = "$r" ]; }
sommeil() { echo "AMORCE $(date -u +%FT%TZ) : sommeil ($1) : disque lisible, la session arrête et détruit par l'identifiant"
    if [ "$ESSAI" = 1 ]; then echo "sommeil ($1)" > "$R/dr-sommeil"; exit "${2:-0}"; fi
    sleep infinity; exit "${2:-0}"; }
arreter_instance() {
    echo "AMORCE $(date -u +%FT%TZ) : fin, code $2"
    if [ "$ESSAI" = 1 ]; then echo "stopped ($1)" > "$R/dr-arret-demande"; exit "$2"; fi
    local c corps="$R/dr-arret-corps.txt" ok=non
    c=$(curl -sS -m 60 -o "$corps" -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    case "$c" in 2??) grep -qiE '"success"[[:space:]]*:[[:space:]]*true' "$corps" 2>/dev/null && ok=oui;; esac
    if [ "$ok" = oui ]; then sommeil "arrêt obtenu" "$2"; fi
    echo "AMORCE $(date -u +%FT%TZ) : ARRÊT NON OBTENU (HTTP $c) : la session arrête par l'identifiant (R10)"
    sommeil "arrêt non obtenu" "$2"; }
FIN_GO="${FIN_GO_UTC_S:-}"
case "$FIN_GO" in ''|*[!0-9]*) refus_precoce "FIN_GO_UTC_S absente ou non entière";; esac
if [ "$ESSAI" != 1 ]; then
    OUTILS="curl git python3 timeout setsid flock sha256sum awk sed sort cut tail head mktemp grep date sleep stat"
    MANQ=""; for o in $OUTILS; do command -v "$o" >/dev/null 2>&1 || MANQ="$MANQ $o"; done
    if [ -n "$MANQ" ]; then
        DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get update -qq >/dev/null 2>&1 \
            && DEBIAN_FRONTEND=noninteractive timeout -k 10 300 apt-get install -y -qq --no-install-recommends ca-certificates curl git util-linux coreutils gawk >/dev/null 2>&1
        MANQ=""; for o in $OUTILS; do command -v "$o" >/dev/null 2>&1 || MANQ="$MANQ $o"; done
        [ -z "$MANQ" ] || refus_precoce "outils absents :$MANQ"
    fi
fi
E="$R/dr-echeance.txt"; DE="$R/dr-depense-epuisee-utc.txt"
if [ -s "$E" ]; then read -r ECH < "$E"; else
    ECH="${ECHEANCE_UTC_S:-}"; case "$ECH" in ''|*[!0-9]*) refus_precoce "ECHEANCE_UTC_S absente ou non entière";; esac; echo "$ECH" > "$E"; fi
if [ -s "$DE" ]; then read -r DEP < "$DE"; else
    DEP="${DEPENSE_EPUISEE_UTC_S:-}"; case "$DEP" in ''|*[!0-9]*) refus_precoce "DEPENSE_EPUISEE_UTC_S absente ou non entière (heure d'épuisement des 90 USD cumulés, calculée à la création)";; esac
    echo "$DEP" > "$DE"; fi
if [ "$DEP" -gt 0 ] && [ "$ECH" -gt "$DEP" ]; then echo "AMORCE DR : échéance ramenée à l'heure du plafond restant ($DEP)"; ECH=$DEP; echo "$ECH" > "$E"; fi
if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/dr-depense-epuisee" ]; then echo "dépense déjà épuisée au démarrage $(date -u +%FT%TZ)" > "$R/dr-depense-epuisee"; fi
if [ "$ESSAI" != 1 ]; then
    setsid bash "$R/dr-minuterie.sh" "$ECH" "$DEP" "$R" "$API" < /dev/null >> "$R/dr-minuterie.log" 2>&1 &
    PM=$!
    echo "AMORCE DR : minuterie lancée (échéance $ECH ; dépense épuisée à $DEP)"
fi
if [ -d "$R/amorce-depot" ]; then
    if [ -e "$R/dr-fin-normale" ] || [ -e "$R/dr-depense-epuisee" ]; then
        [ -f "$R/dr-consigner.sh" ] && timeout -k 10 1200 bash "$R/dr-consigner.sh" "second démarrage"
        if [ -e "$R/dr-depense-epuisee" ] || [ "$(date +%s)" -ge "$DEP" ]; then detruire "second démarrage après la dépense épuisée : commits en attente poussés, destruction" 0; fi
        [ "$(date +%s)" -lt "$ECH" ] || detruire "second démarrage après l'échéance : commits en attente poussés, destruction" 0
        versement_prouve "${BRANCHE:-}" && detruire "second démarrage après une fin normale : versement prouvé, destruction" 0
        sommeil "second démarrage après une fin normale, versement non prouvé" 0
    fi
    [ -f "$R/dr-consigner.sh" ] && timeout -k 10 1200 bash "$R/dr-consigner.sh" "redémarrage d'une course interrompue"
    refus "redémarrage : dépôt déjà extrait (course interrompue) : résultats partiels consignés, rien ne repart ici (reprise : instance neuve, REPRISE_BRANCHE)"
fi
[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun calcul"
[ "$(date +%s)" -lt "$DEP" ] || detruire "démarrage après l'heure de dépense épuisée : aucun calcul"
for v in LANCEMENT BRANCHE_LANCEMENT COMMIT_CODE CONFIG GH_TOKEN BRANCHE; do [ -n "${!v:-}" ] || refus "$v absent"; done
[ -n "${HF_TOKEN:-}" ] || refus "HF_TOKEN absent"
for v in LANCEMENT COMMIT_CODE; do case "${!v}" in *[!0-9a-f]*) refus "$v illisible";; esac; [ "${#v}" -gt 0 ] && [ "$(printf %s "${!v}" | wc -c)" = 40 ] || refus "$v de 40 caractères attendu"; done
case "$GO_ID" in GO-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) refus "GO_ID_DR=$GO_ID illisible";; esac
case "$BRANCHE" in calcul/*) ;; *) refus "branche de sortie $BRANCHE : calcul/… attendue";; esac
ESSAIS="${ESSAIS:-0}"; case "$ESSAIS" in ''|*[!0-9]*) refus "ESSAIS=$ESSAIS : entier attendu";; esac; [ "$ESSAIS" -le 16 ] || refus "ESSAIS=$ESSAIS > 16 (texte scellé, point 4)"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"; export DEPOT_URL
PREREG="${PREREG:-prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md}"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
CHEMINS_CLONAGE='/.gitignore
/.claude/
/src/
/tests/
/scripts/
/pyproject.toml
/requirements-*.txt
/registres/go.md
/registres/scellements-v1.md
/docs/sources/invites-2606.08892-v1/
/prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md*
/diag/20261006-134235-t05-corpus/tirage.json*
/donnees/20261007-082440-t05-extraction/taches-evaluation.json*
/donnees/20261007-082440-t05-extraction/taches-entrainement.json*
/prereg/T0.6-organismes-config-7b-v1.json*
/brouillons/g0-criteres-2-3-v1/pieces/puissance_dose_reponse_consigne_cachee_v5.py*'
T_CLONE0=$(date +%s)
timeout -k 10 900 git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --no-tags --branch "$BRANCHE_LANCEMENT" "$DEPOT_URL" "$R/amorce-depot" || refus "clonage impossible (branche de lancement $BRANCHE_LANCEMENT ?)"
git -C "$R/amorce-depot" config credential.helper "$AIDE"
git -C "$R/amorce-depot" config user.name "instance de calcul (dose-réponse)"
git -C "$R/amorce-depot" config user.email "instance-calcul@invalid"
SP_MSG=$(git -C "$R/amorce-depot" sparse-checkout init --no-cone 2>&1) || refus "extraction partielle impossible : $(printf '%s' "$SP_MSG" | head -c 300 | tr '\n' ' ')"
SP_MSG=$( { printf '%s\n' "$CHEMINS_CLONAGE"; printf '/%s*\n' "$CONFIG"; } | git -C "$R/amorce-depot" sparse-checkout set --no-cone --stdin 2>&1) || refus "extraction partielle impossible : $(printf '%s' "$SP_MSG" | head -c 300 | tr '\n' ' ')"
timeout -k 10 900 git -C "$R/amorce-depot" checkout -q "$LANCEMENT" || refus "commit de lancement $LANCEMENT introuvable sur $BRANCHE_LANCEMENT"
cd "$R/amorce-depot" || refus "dépôt extrait inaccessible"
[ -f "$CONFIG" ] && [ -f "$CONFIG.sha256" ] || refus "configuration $CONFIG ou son sceau absent du commit de lancement"
# fichiers cités par la configuration (pièce jointe, textes du premier test, banque) : chemins ajoutés à l'extraction
CITES=$(python3 -I -B -c "import sys; sys.path.insert(0, 'src'); from controle_ia.dose_reponse import extraction_v1 as e; sys.exit(e.main(sys.argv[1:]))" "$CONFIG" 2>&1) || refus "chemins cités par la configuration illisibles : $(printf '%s' "$CITES" | tail -n 1)"
SP_MSG=$(printf '%s\n' "$CITES" | git sparse-checkout add --stdin 2>&1) || refus "extraction des fichiers cités impossible : $(printf '%s' "$SP_MSG" | head -c 300 | tr '\n' ' ')"
git merge-base --is-ancestor "$COMMIT_CODE" "$LANCEMENT" 2>/dev/null || refus "commit du code $COMMIT_CODE non ancêtre du commit de lancement"
git diff --quiet "$COMMIT_CODE" "$LANCEMENT" -- src scripts tests .claude pyproject.toml 'requirements-*.txt' || refus "code du commit de lancement ≠ code du commit cité $COMMIT_CODE (ligne CODE-DOSE-REPONSE-CONSIGNE-CACHEE)"
echo "AMORCE $(date -u +%FT%TZ) : CLONAGE secondes=$(( $(date +%s) - T_CLONE0 )) lancement=$LANCEMENT code=$COMMIT_CODE"
RUN="$(date -u +%Y%m%d-%H%M%S)-dose-reponse"
T="$R/dr"; mkdir -p "$T"
JOURNAL="$T/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-zA-Z0-9_-]+=[^ ]+)+$'
MOTIF_INTERDIT='cout|cost|effet|moyen|median|sonde|score|aire=|bas=|haut=|ligne_|table_|plancher'
cat > "$R/dr-consigner.sh" <<CONSIGNER
#!/usr/bin/env bash
# écrit par l'amorce de la dose-réponse : consigne et pousse ; git seul, sous verrou ; \$1 = motif
R='$R'; BRANCHE='$BRANCHE'; T='$T'; JOURNAL='$JOURNAL'; MORCEAU_MAX='$MORCEAU_MAX'; RUN='$RUN'; POUSSEE_ATTENTE_S='${POUSSEE_ATTENTE_S:-15}'
CONSIGNER
cat >> "$R/dr-consigner.sh" <<'CONSIGNER'
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
pousser() { local essai; for essai in 1 2 3; do timeout -k 10 600 git push -q origin "$BRANCHE" 2>"$T/poussee.err" && return 0; journal "poussée : tentative $essai refusée"; [ "$essai" -lt 3 ] && sleep $((POUSSEE_ATTENTE_S * essai * essai)); done; return 1; }
refuser_gros() { local f t; while IFS= read -r f; do [ -f "$f" ] || continue; t=$(stat -c %s -- "$f" 2>/dev/null || echo 0)
        if [ "$t" -gt "$MORCEAU_MAX" ]; then git rm -q --sparse --cached -- "$f" >/dev/null 2>&1; journal "ERREUR DE CHAÎNE : $f fait $t octets > $MORCEAU_MAX : retiré du commit, resté sur l'instance"; echo "$f $t" >> "$R/dr-fichiers-trop-gros.txt"; fi
    done < <(git diff --cached --name-only --diff-filter=AM); return 0; }
ajouter() { git add --sparse "$@" 2>"$T/add.err" && return 0
    journal "ERREUR DE CHAÎNE : git add en échec ($*) : $(tr '\n' ' ' < "$T/add.err" | cut -c1-200)"; echo "$(date -u +%FT%TZ) git add en échec : $*" >> "$R/dr-erreurs-chaine.txt"; return 1; }
commit_verifie() { refuser_gros
    local rc essai; git diff --cached --quiet 2>/dev/null; rc=$?
    [ "$rc" = 0 ] && return 10
    if [ "$rc" != 1 ]; then journal "ERREUR DE CHAÎNE : lecture de l'index impossible (code $rc)"; return 1; fi
    for essai in 1 2; do git commit -qm "$1" >/dev/null 2>"$T/commit.err" && return 0
        journal "ERREUR DE CHAÎNE : commit en échec (tentative $essai) : $(tr '\n' ' ' < "$T/commit.err" | cut -c1-200)"; [ "$essai" = 1 ] && sleep 2; done
    echo "$(date -u +%FT%TZ) commit en échec : $1" >> "$R/dr-erreurs-chaine.txt"; return 1; }
etape_commit() { local rc; commit_verifie "$1"; rc=$?
    case "$rc" in 0) [ -z "$2" ] || journal "$2"; return 0;; 10) [ -z "$3" ] || journal "$3"; return 0;; *) return 1;; esac; }
trace_consignation() { local d; mkdir -p traces || return 1
    d=$(mktemp -d "traces/consignation-$(date -u +%Y%m%d-%H%M%S)-XXXX") || return 1
    { echo "motif : $1"; echo "heure : $(date -u +%FT%TZ)"; echo "--- 400 dernières lignes du journal ---"; tail -n 400 "$JOURNAL" 2>/dev/null | cut -c1-400; } > "$d/journal-consignation.txt"
    [ -f "$R/dr-minuterie.log" ] && tail -n 200 "$R/dr-minuterie.log" | cut -c1-400 > "$d/dr-minuterie-fin.txt"
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    ajouter "$d" || return 1
    etape_commit "Dose-réponse : journal de l'instance ($1)" "$1 : journal de l'instance committé" ""; }
consigner_partiel() { local echec=0
    for x in runs diag; do [ -d "$x" ] && { ajouter -A "$x" || echec=1; }; done
    [ -d "donnees/$RUN" ] && { ajouter -f "donnees/$RUN" || echec=1; }
    etape_commit "Dose-réponse : résultats et blocs de la course ($1)" "$1 : résultats et blocs committés" "$1 : rien de neuf à committer" || echec=1
    if [ "${TRACE_CONSIGNATION:-0}" = 1 ]; then trace_consignation "$1" || echec=1; fi
    if pousser; then journal "branche $BRANCHE poussée ($1)"; [ "$echec" = 0 ] && return 0; return 2; fi
    journal "poussée impossible ($1) : résultats restés sur l'instance"; return 1; }
if [ "${1:-}" = "--source" ]; then return 0 2>/dev/null || exit 0; fi
exec 9>>"$R/dr-consigner.lock"; flock -w 1500 9 || { echo "verrou de consignation non obtenu ($1)"; exit 1; }
cd "$R/amorce-depot" || { echo "dépôt extrait inaccessible"; exit 1; }
TRACE=1; [ "${DR_SANS_TRACE:-0}" = 1 ] && TRACE=0
TRACE_CONSIGNATION=$TRACE consigner_partiel "$1"
exit $?
CONSIGNER
. "$R/dr-consigner.sh" --source
journal "début dose-réponse v4 : LANCEMENT=$LANCEMENT ($BRANCHE_LANCEMENT) CODE=$COMMIT_CODE BRANCHE=$BRANCHE PREREG=$PREREG CONFIG=$CONFIG GO=$GO_ID FIN_GO=$FIN_GO ECHEANCE=$ECH DEPENSE_EPUISEE=$DEP RUN=$RUN REPRISE=${REPRISE_BRANCHE:-aucune}:${REPRISE_RUN:-} ESSAIS=$ESSAIS"
SESSION_GO="import sys; sys.path.insert(0, 'src'); from controle_ia.lancement_t08 import session_v1; sys.exit(session_v1.main(sys.argv[1:]))"
GOL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_GO" go registres/go.md "$CONFIG" "$GO_ID" 2>&1) || refus "$GO_ID non conforme dans registres/go.md du commit de lancement ($GOL)"
journal "GO : $GOL"
CAL=$(timeout -k 5 120 python3 -I -B -c "$SESSION_GO" calendrier registres/go.md "$CONFIG" "$GO_ID" 2>&1) || refus "calendrier non conforme ($CAL)"
FIN_CONFIG=$(printf '%s\n' "$CAL" | sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p' | tail -1)
[ "$FIN_CONFIG" = "$FIN_GO" ] || refus "fin du GO reçue ($FIN_GO) ≠ fin de validité de $GO_ID au registre du commit ($FIN_CONFIG)"
code_branche=0
timeout -k 5 300 git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$T/ls-remote.err" || code_branche=$?
case "$code_branche" in 0) refus "branche $BRANCHE déjà présente sur le dépôt distant";; 2) ;; *) refus "vérification de la branche $BRANCHE impossible (code $code_branche)";; esac
REPRISE_ARGS=()
if [ -n "${REPRISE_BRANCHE:-}" ]; then
    case "${REPRISE_RUN:-}" in [0-9]*-dose-reponse) ;; *) refus "REPRISE_RUN=${REPRISE_RUN:-} illisible";; esac
    timeout -k 10 900 git fetch -q --no-tags origin "refs/heads/$REPRISE_BRANCHE:refs/remotes/origin/$REPRISE_BRANCHE" || refus "branche de reprise $REPRISE_BRANCHE introuvable"
    printf '/donnees/%s/\n' "$REPRISE_RUN" | git sparse-checkout add --stdin >/dev/null 2>&1 || refus "extraction de la reprise impossible"
    git checkout -q "refs/remotes/origin/$REPRISE_BRANCHE" -- "donnees/$REPRISE_RUN" || refus "blocs de la reprise absents de $REPRISE_BRANCHE"
    git reset -q -- "donnees/$REPRISE_RUN"
    REPRISE_ARGS=(--reprise "donnees/$REPRISE_RUN")
    journal "reprise : blocs de $REPRISE_RUN ($REPRISE_BRANCHE) extraits ; ils seront vérifiés par la course et recopiés tels quels"
fi
git checkout -q -b "$BRANCHE"
timeout -k 5 300 git push -q origin "$BRANCHE" 2>"$T/poussee-initiale.err" || refus "poussée initiale de la branche $BRANCHE refusée (droit d'écriture du jeton ?)"
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"
inventaire() {  # avant toute destruction (mot de Lazar du 19 novembre) : noms, tailles, empreintes des sorties ; activations des trois couches comptées
    { echo "inventaire $(date -u +%FT%TZ), run $RUN"; [ -d "donnees/$RUN" ] && find "donnees/$RUN" -type f -printf '%s %p\n' | sort -k2
      [ -d "donnees/$RUN" ] && (find "donnees/$RUN" -type f -name '*.sha256' -exec cat {} + 2>/dev/null | sort)
      echo "activations sur le disque de l'instance : $(find "$R/activations-$RUN" -type f 2>/dev/null | wc -l) fichiers, $(du -sb "$R/activations-$RUN" 2>/dev/null | cut -f1) octets"; } > "$T/inventaire.txt" 2>&1; }
traces() { local d; mkdir -p traces; d=$(mktemp -d "traces/dr-$(date -u +%Y%m%d-%H%M%S)-XXXX"); inventaire
    for f in "$JOURNAL" "$T/tests.txt" "$T/tests.err" "$T/run.json" "$T/run.err" "$T/nvidia-smi.txt" "$T/pip-freeze.txt" "$T/gardes.txt" "$T/inventaire.txt" "$R/dr-minuterie.log" "$R/dr-fichiers-trop-gros.txt" "$T/progres-retenues.txt"; do [ -f "$f" ] && cp "$f" "$d/"; done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    ajouter "$d" || return 1; etape_commit "Dose-réponse : traces de l'instance ($1)" "" ""; }
prendre_verrou() { exec 9>>"$R/dr-consigner.lock"; if flock -w "${VERROU_ATTENTE_S:-1500}" 9; then return 0; fi
    journal "ERREUR DE CHAÎNE : verrou de consignation non obtenu ($1)"; exec 9>&-; return 1; }
liberer_verrou() { exec 9>&-; }
consigner_arret() { prendre_verrou "arrêt pendant $1"; consigner_partiel "arrêt pendant $1"; traces "arrêt pendant $1"; pousser || true; liberer_verrou; }
fin_anormale() { echo "fin anormale $(date -u +%FT%TZ), run $RUN : $1" > "$R/dr-fin-anormale"; journal "FIN ANORMALE : $1"; liberer_verrou; arreter_instance "fin anormale" 1; }
nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$T/nvidia-smi.txt"
timeout -k 10 1800 python3.11 -m venv "$R/venv-dr" && . "$R/venv-dr/bin/activate" && timeout -k 10 3600 pip install -q -r requirements-gpu.txt || { journal "installation impossible"; consigner_arret "installation"; arreter_instance "installation impossible" 1; }
python -m pip freeze --all >"$T/pip-freeze.txt" 2>/dev/null || true
if ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)" 2>"$T/torch-cuda.err"; then
    journal "carte invisible pour torch : $(tail -c 300 "$T/torch-cuda.err" 2>/dev/null | tr '\n' ' ')"; consigner_arret "contrôle de la carte"; refus "carte invisible pour torch : aucun calcul"
fi
# gardes avant tout calcul, sur le commit de lancement : contrôles avant dépense du texte scellé (empreintes, banque, modules,
# lignes du registre, bornes de l'offre) ; code cité égal au commit du code de la configuration
GARDES=$(PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src timeout -k 10 900 python - "$CONFIG" "$COMMIT_CODE" <<'FIN_GARDES' 2>&1
import json, sys
from pathlib import Path
from controle_ia.gardes import GardeArret
from controle_ia.scellement import verifier
from controle_ia.dose_reponse import controles_v3 as ct
config_chemin, commit = sys.argv[1:3]
try:
    verifier(config_chemin)
    c = json.load(open(config_chemin, encoding="utf-8"))
    if c.get("mode") != "reel":
        raise GardeArret("configuration de la course en mode autre que réel")
    if c.get("commit_code") != commit:
        raise GardeArret(f"commit du code de la configuration {c.get('commit_code')} ≠ COMMIT_CODE {commit}")
    r = ct.controles_avant_depense(Path("."), c)
    print(f"gardes conformes : texte {r['prereg_sha256'][:12]}, banque {r['banque']['taches']} tâches (rangs {r['banque']['rang_min']} à {r['banque']['rang_max']}), {r['modules']['modules']} modules, lignes {r['registre']['lignes']}")
except (GardeArret, OSError, ValueError, KeyError) as e:
    print(f"ARRÊT : {e}")
    sys.exit(1)
FIN_GARDES
) || { MG=$(printf '%s' "$GARDES" | tail -n 1); journal "gardes avant tout calcul : $MG"; printf '%s\n' "$GARDES" > "$T/gardes.txt"; consigner_arret "gardes"; refus "gardes avant tout calcul : $(printf '%s' "$MG" | cut -c1-300)"; }
printf '%s\n' "$GARDES" > "$T/gardes.txt"; journal "$GARDES"
LISTE_TESTS="scripts/tests-cibles-dose-reponse-v4.txt"; LISTE_SHA256="2766a9b022d4e9db45dd0c85d224473409b4cacb20aad9a1c3fd81166c449d55"; ATTENDUS="60"; FICHIERS_TESTS=""
liste_refus() { journal "suite ciblée : $1 : arrêt avant tout essai"; consigner_arret "liste des essais"; arreter_instance "liste des essais" 1; }
[ -f "$LISTE_TESTS" ] || liste_refus "liste $LISTE_TESTS absente"
[ "$(sha256sum "$LISTE_TESTS" | cut -d' ' -f1)" = "$LISTE_SHA256" ] || liste_refus "empreinte de $LISTE_TESTS ≠ celle de l'amorce"
while IFS= read -r f; do [ -n "$f" ] || continue
    printf '%s\n' "$f" | grep -Eq '^tests/test_[A-Za-z0-9_]+\.py$' || liste_refus "chemin illisible : $f"
    [ -f "$f" ] || liste_refus "essai absent : $f"; FICHIERS_TESTS="$FICHIERS_TESTS $f"; done < "$LISTE_TESTS"
[ -n "$FICHIERS_TESTS" ] || liste_refus "liste vide"
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no $FICHIERS_TESTS >"$T/tests.txt" 2>"$T/tests.err"; then
    tail -n 5 "$T/tests.txt" "$T/tests.err" | tee -a "$JOURNAL"; journal "tests en échec : arrêt"; consigner_arret "tests"; arreter_instance "tests en échec" 1
fi
DERNIERE=$(tail -1 "$T/tests.txt"); journal "tests : $DERNIERE"
printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$" || { journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed » : arrêt"; consigner_arret "tests"; arreter_instance "nombre de tests" 1; }
PYTHONPATH=src timeout -k 10 3600 python -c 'import json, sys
from controle_ia.harnais.modeles import precharger_modele
c = json.load(open(sys.argv[1], encoding="utf-8"))
print(c["agent"]["modele"], precharger_modele(c["agent"]["modele"], c["agent"]["revision"]), flush=True)' "$CONFIG" > "$T/modeles.txt" 2>&1 \
    || { journal "modèle : descente impossible : $(tail -n 1 "$T/modeles.txt" | cut -c1-300)"; consigner_arret "descente du modèle"; arreter_instance "descente du modèle" 1; }
journal "modèle au cache local"
journal "run : $RUN (sans couperet de temps ; course de dose-réponse, une fois)"
: >"$T/run.err"; : >"$T/progres-retenues.txt"
HF_HUB_OFFLINE=1 PYTHONPATH=src python -m controle_ia.dose_reponse.course_v3 --config "$CONFIG" --run-id "$RUN" --prereg "$PREREG" \
    --dossier-activations "$R/activations-$RUN" --commande-poussee "DR_SANS_TRACE=1 bash $R/dr-consigner.sh" --essais "$ESSAIS" "${REPRISE_ARGS[@]}" >"$T/run.json" 2>>"$T/run.err" &
PID_RUN=$!
( tail -n +1 -F --pid="$PID_RUN" "$T/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" | while IFS= read -r ligne; do
    if printf '%s\n' "$ligne" | grep -qiE "$MOTIF_INTERDIT"; then printf '%s\n' "$(date -u +%FT%TZ) PROGRES non relayée : motif interdit" | tee -a "$JOURNAL" >> "$T/progres-retenues.txt"
    else printf '%s\n' "$ligne" | tee -a "$JOURNAL"; fi; done ) &
PID_RELAIS=$!
code=0; wait "$PID_RUN" || code=$?
wait "$PID_RELAIS" 2>/dev/null || true
if [ "$code" -ne 0 ]; then
    if grep -q '^ARRÊT : ' "$T/run.err"; then
        grep '^ARRÊT : ' "$T/run.err" | grep -viE "$MOTIF_INTERDIT" | tail -n 3 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; arreter_instance "arrêt consigné pendant le run" 1
    else
        echo "AMORCE $(date -u +%FT%TZ) : RUN MORT sans résumé ni arrêt consigné (code $code) : arrêt de l'instance par son identifiant (R10)" | tee -a "$JOURNAL"
        consigner_arret "run mort (code $code)"; arreter_instance "run mort" 1
    fi
fi
ECHEC=0
prendre_verrou "fin de run" || ECHEC=1
consigner_partiel "fin de run" || ECHEC=1
traces "fin" || ECHEC=1
[ ! -s "$R/dr-fichiers-trop-gros.txt" ] || { journal "ERREUR DE CHAÎNE : fichier(s) trop gros restés sur l'instance"; ECHEC=1; }
if [ "$ECHEC" != 0 ]; then pousser || true; fin_anormale "un ajout, un commit ou le verrou a échoué en fin de run"; fi
RESTE=$(git status --porcelain -- runs diag traces 2>&1; git status --porcelain --ignored -- "donnees/$RUN" 2>&1)   # « !! » : fichier de la course resté hors du dépôt
[ -z "$RESTE" ] || { pousser || true; fin_anormale "fichiers non consignés : $(printf '%s' "$RESTE" | head -n 3 | tr '\n' ';')"; }
echo "fin normale $(date -u +%FT%TZ), run $RUN" > "$R/dr-fin-normale"
if pousser; then journal "branche $BRANCHE poussée (blocs, résultats, traces)"; liberer_verrou
    if versement_prouve "$BRANCHE"; then journal "versement prouvé : $(git rev-parse HEAD) = origin/$BRANCHE ; activations des trois couches restées sur le disque de l'instance (recalculables par la même passe)"; detruire "fin normale : versement prouvé, destruction" 0; fi
    journal "poussée faite, versement non prouvé : arrêt, disque gardé"; arreter_instance "versement non prouvé" 1
fi
journal "poussée finale impossible : résultats restés sur l'instance"
liberer_verrou
arreter_instance "poussée impossible" 1
