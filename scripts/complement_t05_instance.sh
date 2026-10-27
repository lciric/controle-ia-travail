#!/usr/bin/env bash
# Notations complémentaires de T0.5 sur l'instance de calcul : mise en place, tests, un ou deux runs successifs du lanceur
# `noter_complement_t05` (juges 8B puis 3B, couples (épisode, passe) que le run source n'a pas notés), poussée des
# résultats et des traces (rien ne reste sur l'instance : leçon de N-012). Dérivé de `notations_t05_instance.sh` sous un
# nom nouveau (R12 : le script des notations refaites n'est pas modifié). Différences : deux runs successifs au plus
# (PREREG_1, puis PREREG_2 facultatif), chacun sous son identifiant, avec ses chemins cités lus avant toute
# installation ; un échec du premier est consigné (résultats partiels committés et poussés) et n'empêche pas le second ;
# un délai externe global (400 minutes au plus) borne les deux runs ensemble. Rien ne se lance sans GO consigné.
#
#   COMMIT=<commit de scellement des préenregistrements> PREREG_1=… [PREREG_2=…] bash complement_t05_instance.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le lanceur Python vérifie en plus le commit, la configuration, le run
#                 source, les empreintes de son manifeste, de ses épisodes, de son arrêt et des notations qu'il porte
#                 déjà, les tâches et l'entropie
#   MODE          reel (défaut) ou jouet (répétition sur processeur)
#   PREREG_1      (obligatoire sauf PREREG_ABSENT=1) préenregistrement du premier run ; PREREG_2 (facultatif) celui du
#                 second. Chacun cite, une seule fois chacun, « Tests attendus : `N` » (le même nombre dans les deux),
#                 « Chemin de la configuration du complément : `…` », « Chemin des tâches du run source : `…` »,
#                 « Chemin du manifeste du run source : `…` », « Chemin des épisodes du run source : `…` », que ce
#                 script lit avant toute installation (fichiers et sceaux présents au commit, sceaux conformes)
#   PREREG_ABSENT 1 seulement en mode jouet : répétition sans préenregistrement ; CONFIG_1 et TACHES_1 (et CONFIG_2,
#                 TACHES_2 pour un second run) donnent les chemins
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN      jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel)
#   BRANCHE       défaut calcul/t05-complement-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TESTS_ATTENDUS nombre de tests attendus (sans préenregistrement seulement)
#   DELAI_GLOBAL_MIN délai externe global des runs, en minutes (défaut 400, au plus 400) : chaque run reçoit le temps
#                 qui reste jusqu'à cette échéance, comptée depuis le début du premier run (TERM, converti en arrêt
#                 consigné, puis KILL cinq minutes plus tard) ; un second run qui trouverait moins de 60 s n'est pas
#                 lancé (consigné). Les échéances internes de chaque run (par juge et globale, 23 100 s au plus) se
#                 fixent au préenregistrement de sorte que leur somme tienne sous ce délai.
#   TRAVAIL       défaut $HOME/t05
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement des préenregistrements du complément)}"
ETUDE=complement
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/t05-complement-$MODE-v1}"
TRAVAIL="${TRAVAIL:-$HOME/t05}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
PREREG_1="${PREREG_1:-}"
PREREG_2="${PREREG_2:-}"
DELAI_GLOBAL_MIN="${DELAI_GLOBAL_MIN:-400}"
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
if ! [[ "$DELAI_GLOBAL_MIN" =~ ^[0-9]+$ ]] || [ "$DELAI_GLOBAL_MIN" -lt 1 ] || [ "$DELAI_GLOBAL_MIN" -gt 400 ]; then
    echo "DELAI_GLOBAL_MIN=$DELAI_GLOBAL_MIN : un entier de minutes dans [1 ; 400]" >&2; exit 2
fi
if [ "$PREREG_ABSENT" != 1 ] && [ -z "$PREREG_1" ]; then
    echo "PREREG_1 obligatoire (préenregistrement du premier run)" >&2; exit 2
fi
# lignes de progression du lanceur recopiées au journal : préfixe fixe, horodatage, puis des couples clé=valeur sans
# espace (nombres, rangs, noms de juges, statuts) ; aucune autre ligne de la sortie d'erreur n'y passe (aucun texte)
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : ETUDE=$ETUDE MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE"
if [ "$MODE" = reel ]; then
    : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel}"
fi

DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (T0.5)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$TRAVAIL/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) journal "branche $BRANCHE déjà présente sur le dépôt distant : relancement sous une branche nouvelle (BRANCHE=…) ; arrêt avant l'installation"
       exit 2 ;;
    2) ;;
    *) cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/ls-remote.err" || tail -n 2 "$TRAVAIL/ls-remote.err") | tr '\n' ' ' || true)
       journal "vérification de la branche $BRANCHE impossible (git ls-remote, code $code_branche : $cause) : arrêt avant l'installation"
       exit 2 ;;
esac
git checkout -q -b "$BRANCHE"

# Lecture précoce des préenregistrements, avant toute installation : chaque citation lue doit figurer une seule fois
# dans le préenregistrement de son run
lire_unique() {
    local n
    n=$(grep -c "$2 : \`" "$1" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$2 : \`\\([^\`]*\\)\`.*/\\1/p" "$1"
}
PREREGS=()
CONFIGS=()
TACHES_RUNS=()
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG_1:?CONFIG_1 obligatoire sans préenregistrement}" "${TACHES_1:?TACHES_1 obligatoire sans préenregistrement}"
    CONFIGS=("$CONFIG_1"); TACHES_RUNS=("$TACHES_1"); PREREGS=("")
    if [ -n "${CONFIG_2:-}" ]; then
        : "${TACHES_2:?TACHES_2 obligatoire avec CONFIG_2}"
        CONFIGS+=("$CONFIG_2"); TACHES_RUNS+=("$TACHES_2"); PREREGS+=("")
    fi
else
    ATTENDUS=""
    for P in "$PREREG_1" ${PREREG_2:+"$PREREG_2"}; do
        [ -f "$P" ] || { journal "préenregistrement $P absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
        A=$(lire_unique "$P" "Tests attendus")
        [[ "$A" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois dans $P : arrêt avant l'installation"; exit 2; }
        if [ -n "$ATTENDUS" ] && [ "$A" != "$ATTENDUS" ]; then
            journal "tests attendus différents d'un préenregistrement à l'autre ($ATTENDUS, $A) : arrêt avant l'installation"
            exit 2
        fi
        ATTENDUS="$A"
        C=$(lire_unique "$P" "Chemin de la configuration du complément")
        T=$(lire_unique "$P" "Chemin des tâches du run source")
        M=$(lire_unique "$P" "Chemin du manifeste du run source")
        E=$(lire_unique "$P" "Chemin des épisodes du run source")
        CITES=("$C" "$T" "$M" "$E")
        for f in "${CITES[@]}"; do
            [ -n "$f" ] || { journal "chemin cité introuvable ou cité plusieurs fois dans $P : arrêt avant l'installation"; exit 2; }
            if [ ! -f "$f" ] || [ ! -f "$f.sha256" ]; then
                journal "fichier cité $f ou son sceau absent de l'arbre du commit $COMMIT : arrêt avant l'installation"
                exit 2
            fi
        done
        if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "${CITES[@]}" \
                >"$TRAVAIL/sceaux.txt" 2>&1; then
            cause=$(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1 || true)
            journal "sceau non conforme parmi les fichiers cités par $P ($cause) : arrêt avant l'installation"
            exit 2
        fi
        PREREGS+=("$P"); CONFIGS+=("$C"); TACHES_RUNS+=("$T")
        journal "préenregistrement $P lu : $ATTENDUS tests attendus ; configuration $C ; tâches $T ; run source : manifeste et épisodes présents et scellés"
    done
fi

poussee_initiale=0
for essai in 1 2 3; do
    if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee-initiale.err"; then poussee_initiale=1; break; fi
    journal "poussée initiale de la branche $BRANCHE : tentative $essai refusée"
    if [ "$essai" -lt 3 ]; then sleep 5; fi
done
if [ "$poussee_initiale" != 1 ]; then
    cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/poussee-initiale.err" || tail -n 2 "$TRAVAIL/poussee-initiale.err") | tr '\n' ' ' || true)
    journal "poussée initiale de la branche $BRANCHE refusée ($cause) : droit d'écriture du jeton ? arrêt avant l'installation"
    exit 2
fi
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"

pousser() {
    local essai cause
    for essai in 1 2 3; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then return 0; fi
        cause=$( (grep -E '^(fatal|error|remote):' "$TRAVAIL/poussee.err" || tail -n 2 "$TRAVAIL/poussee.err") | tr '\n' ' ' || true)
        journal "poussée de la branche $BRANCHE : tentative $essai refusée ($cause)"
        if [ "$essai" -lt 3 ]; then sleep $((15 * essai * essai)); fi
    done
    return 1
}
traces() {
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/t05-complement-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL"/run-*.json "$TRAVAIL"/run-*.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "T0.5 — complément : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
CONSIGNE=""
# résultats partiels d'une étape committés (dont arret.json s'il existe) ; le script continue
committer_partiel() {
    git add -A runs diag
    if git commit -qm "T0.5 — complément : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json s'il existe)"
    else
        journal "ARRÊT pendant $1 : aucun résultat à committer"
    fi
}
consigner_arret() {
    CONSIGNE=1
    committer_partiel "$1"
    traces "arrêt pendant $1"
    if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi
}

ETAPE="mise en place"
PID_RUN=""
sur_term() {
    trap '' TERM
    journal "TERM reçu pendant $ETAPE (plafond de l'amorce)"
    if [ -n "$PID_RUN" ]; then
        kill -TERM "$PID_RUN" 2>/dev/null || true
        wait "$PID_RUN" 2>/dev/null || true
    fi
    consigner_arret "$ETAPE (plafond de l'amorce)" || true
    exit 124
}
trap sur_term TERM
sur_sortie() {
    local code=$?
    if [ "$code" -ne 0 ] && [ -z "$CONSIGNE" ]; then
        trap '' TERM
        journal "sortie imprévue (code $code) pendant $ETAPE" || true
        consigner_arret "$ETAPE (sortie imprévue, code $code)" || true
    fi
    exit "$code"
}
trap sur_sortie EXIT

if [ "$MODE" = reel ]; then
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$TRAVAIL/nvidia-smi.txt"
fi

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    python3.11 -m venv .venv
    # shellcheck disable=SC1091
    . .venv/bin/activate
    pip install -q -r requirements-gpu.txt
fi
if ! python -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>"$TRAVAIL/pip-freeze.err"; then
    journal "pip freeze impossible (descriptif, sans effet sur les runs) : $(tail -n 1 "$TRAVAIL/pip-freeze.err" | tr '\n' ' ')"
fi

python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch (pilote CUDA trop ancien ?) : arrêt avant les tests"
    consigner_arret "contrôle de la carte"
    exit 1
fi
ETAPE="tests"
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt")
journal "tests : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed », sans test sauté ni en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi

# délai externe global, figé (R1) : échéance commune aux runs, comptée depuis le début du premier ; chaque run reçoit le
# temps qui reste (TERM, converti en arrêt consigné par le lanceur, puis KILL cinq minutes plus tard). Le signal vise le
# processus lancé par timeout, par son identifiant (R10).
FIN_GLOBALE=$(( $(date +%s) + DELAI_GLOBAL_MIN * 60 ))
ECHECS=0
NB_RUNS=${#CONFIGS[@]}
for i in $(seq 1 "$NB_RUNS"); do
    CONFIG="${CONFIGS[$((i - 1))]}"
    TACHES="${TACHES_RUNS[$((i - 1))]}"
    PREREG="${PREREGS[$((i - 1))]}"
    ETAPE="lancement du run $i"
    RESTANT=$(( FIN_GLOBALE - $(date +%s) ))
    if [ "$RESTANT" -lt 60 ]; then
        journal "run $i/$NB_RUNS non lancé : délai externe global épuisé (${RESTANT} s restantes)"
        ECHECS=$((ECHECS + 1))
        continue
    fi
    ARGS=()
    if [ -z "$PREREG" ]; then
        journal "run $i/$NB_RUNS : répétition sans préenregistrement (jouet, non décisive)"
    else
        ARGS=(--prereg "$PREREG")
    fi
    journal "run $i/$NB_RUNS : configuration $CONFIG ; tâches $TACHES ; délai externe ${RESTANT} s"
    LANCEUR=(controle_ia.environnements.noter_complement_t05 --config "$CONFIG" --taches "$TACHES")
    DELAI=(timeout --signal=TERM --kill-after=5m "${RESTANT}s")
    RUN="$(date -u +%Y%m%d-%H%M%S)-t05-complement-$i-$MODE"
    ETAPE="run $RUN"
    journal "run $i/$NB_RUNS : $RUN"
    ERR="$TRAVAIL/run-$i.err"
    code=0
    : >"$ERR"
    PYTHONPATH=src "${DELAI[@]}" python -m "${LANCEUR[@]}" --run-id "$RUN" "${ARGS[@]}" >"$TRAVAIL/run-$i.json" \
        2>>"$ERR" &
    PID_RUN=$!
    # relais des lignes de progression : tail s'arrête de lui-même quand le run se termine (--pid), sans arrêt par motif
    ( tail -n +1 -F --pid="$PID_RUN" "$ERR" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
        | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
    PID_RELAIS=$!
    wait "$PID_RUN" || code=$?
    PID_RUN=""
    wait "$PID_RELAIS" 2>/dev/null || true
    # un run est complet si son résumé existe sans arrêt consigné (un juge échu est consigné dans le résumé)
    if [ "$code" -ne 0 ] && { [ ! -f "diag/$RUN/resume.json" ] || [ -f "diag/$RUN/arret.json" ]; }; then
        # diagnostic : dernières lignes de la sortie d'erreur, hors de toute ligne de progression
        grep -v '^PROGRES ' "$ERR" | tail -n 5 | tee -a "$JOURNAL" || true
        committer_partiel "run $RUN (code $code)"
        ECHECS=$((ECHECS + 1))
        ETAPE="poussée du run $i"
        pousser || journal "poussée du run $RUN impossible : résultats restés sur l'instance"
        [ "$i" -lt "$NB_RUNS" ] && journal "run $i/$NB_RUNS en échec, consigné : le run suivant est lancé"
        continue
    fi
    if [ "$code" -ne 0 ]; then
        journal "run $RUN : code $code, mais résumé écrit sans arrêt consigné : run complet"
    fi
    git add "runs/$RUN" "diag/$RUN"
    git commit -qm "T0.5 — complément ($MODE), run $i, $RUN"
    # le résumé reste dans run-<i>.json, versé aux traces ; il n'est pas recopié au journal que lit la surveillance
    journal "run terminé : $RUN"
    ETAPE="poussée du run $i"
    pousser || journal "poussée du run $RUN impossible : résultats restés sur l'instance"
done
ETAPE="fin"
journal "fin : $NB_RUNS runs prévus, $ECHECS en échec ou non lancés ; arrêter l'instance par son identifiant (R10)"
CONSIGNE=1
traces "fin"
if pousser; then
    journal "branche $BRANCHE poussée (résultats et traces)"
else
    journal "poussée finale impossible après trois tentatives : résultats et traces restés sur l'instance"
    exit 1
fi
if [ "$ECHECS" -ne 0 ]; then exit 1; fi
