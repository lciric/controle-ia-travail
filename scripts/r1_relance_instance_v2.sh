#!/usr/bin/env bash
# Relance de R1 seule (rejeu des 2 400 actions de P3, activations aux couches 7, 15, 23) sur l'instance de calcul, selon
# l'addendum `prereg/R1-addendum-relance-v1.md` (GO-2026-11-01-13). Version 2 du script d'instance, sous un nom nouveau
# (R12 ; `r1_r2_instance_v1.sh`, cité par le scellement de R1-R2, n'est pas modifié). Changements : R1 seule
# (`ETAPES=rejeu`, tout autre valeur arrête avant l'installation : R2 ne se relance pas, ses scores existent) ; module
# `controle_ia.runs_nuit.rejeu_activations_v2` (règles A et B de l'addendum) ; préenregistrement par défaut = l'addendum,
# qui cite la configuration v3, elle-même la table de tokenisation scellée ; branche de résultats par défaut
# `calcul/r1-relance-<MODE>-v1` ; plus de garde N-029 (aucun juge) ; sceau de la table et du préenregistrement parent
# vérifiés avant l'installation.
#
#   COMMIT=<commit de scellement de l'addendum> bash r1_relance_instance_v2.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire
#   MODE          reel (défaut) ou jouet (répétition sur processeur)
#   PREREG        défaut prereg/R1-addendum-relance-v1.md ; il cite, une seule fois chacun, « Tests attendus : `N` »,
#                 « Chemin de la configuration du rejeu : `…` », « Chemin de la table de tokenisation : `…` » et
#                 « Chemin du préenregistrement parent : `…` », lus avant toute installation
#   PREREG_ABSENT 1 seulement en mode jouet ; CONFIG_REJEU donne alors le chemin
#   ETAPES        « rejeu » (défaut et seule valeur admise)
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN      jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel ; licence Llama 3.1 acceptée)
#   BRANCHE       défaut calcul/r1-relance-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TESTS_ATTENDUS nombre de tests attendus (sans préenregistrement seulement)
#   TRAVAIL       défaut $HOME/r1rel
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
#   TESTS_CIBLES  mode jouet seulement : fichiers de tests remplaçant la suite ciblée (répétition rapide)
# Suite ciblée : celle de R1-R2 (17 fichiers) plus `tests/test_runs_nuit_v2.py` ; le nombre exact est cité par
# l'addendum (« Tests attendus »).
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire}"
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/r1-relance-$MODE-v1}"
PREREG="${PREREG:-prereg/R1-addendum-relance-v1.md}"
TRAVAIL="${TRAVAIL:-$HOME/r1rel}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
ETAPES="${ETAPES:-rejeu}"
if [ "$ETAPES" != rejeu ]; then
    echo "ETAPES=$ETAPES : la relance de R1 n'admet que « rejeu » (R2 ne se relance pas, addendum) : arrêt" >&2; exit 2
fi
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : relance de R1 MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE ETAPES=$ETAPES"
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
git config user.name "instance de calcul (relance de R1)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$TRAVAIL/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) journal "branche $BRANCHE déjà présente sur le dépôt distant : relancement sous une branche nouvelle (BRANCHE=…) ; arrêt avant l'installation"
       exit 2 ;;
    2) ;;
    *) journal "vérification de la branche $BRANCHE impossible (git ls-remote, code $code_branche) : arrêt avant l'installation"
       exit 2 ;;
esac
git checkout -q -b "$BRANCHE"

lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$PREREG" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"
}
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG_REJEU:=}"
else
    [ -f "$PREREG" ] && [ -f "$PREREG.sha256" ] || { journal "préenregistrement $PREREG ou son sceau absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois dans $PREREG : arrêt"; exit 2; }
    CONFIG_REJEU=$(lire_unique "Chemin de la configuration du rejeu")
    TABLE=$(lire_unique "Chemin de la table de tokenisation")
    PARENT=$(lire_unique "Chemin du préenregistrement parent")
    for f in "$PREREG" "$CONFIG_REJEU" "$TABLE" "$PARENT"; do
        [ -n "$f" ] || { journal "chemin cité introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
        [ -f "$f" ] && [ -f "$f.sha256" ] || { journal "fichier cité $f ou son sceau absent : arrêt avant l'installation"; exit 2; }
    done
    if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "$PREREG" "$CONFIG_REJEU" \
            "$TABLE" "$PARENT" >"$TRAVAIL/sceaux.txt" 2>&1; then
        journal "sceau non conforme parmi les fichiers cités ($(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1)) : arrêt avant l'installation"
        exit 2
    fi
    journal "addendum lu : $ATTENDUS tests attendus ; rejeu $CONFIG_REJEU ; table $TABLE ; parent $PARENT : présents et scellés"
fi

if ! git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee-initiale.err"; then
    journal "poussée initiale de la branche $BRANCHE refusée ($(tail -n 1 "$TRAVAIL/poussee-initiale.err")) : droit d'écriture du jeton ? arrêt"
    exit 2
fi
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"

pousser() {
    local essai
    for essai in 1 2 3; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then return 0; fi
        journal "poussée de la branche $BRANCHE : tentative $essai refusée ($(tail -n 1 "$TRAVAIL/poussee.err"))"
        if [ "$essai" -lt 3 ]; then sleep $((15 * essai * essai)); fi
    done
    return 1
}
traces() {
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/r1-relance-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL"/tests.txt "$TRAVAIL"/tests.err "$TRAVAIL"/*.json "$TRAVAIL"/*.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "Relance de R1 : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
# sorties légères poussées par ajout forcé (donnees/ est ignoré par git) ; le fichier complet des activations n'est poussé
# que s'il tient sous la limite (sinon ses deux moitiés, « -moyenne » et « -maximum », le sont)
ajouter_donnees() {
    local f
    for f in donnees/*/activations-p3-rejeu-v1.npz donnees/*/activations-p3-rejeu-v1.npz.sha256 \
             donnees/*/activations-p3-rejeu-v1-maximum.npz* \
             donnees/*/activations-p3-rejeu-v1-complement-hors-cout.npz*; do
        [ -f "$f" ] || continue
        if [ "$(stat -c %s "$f")" -gt 99000000 ]; then journal "$f : $(stat -c %s "$f") octets, au-dessus de la limite de poussée : laissé sur l'instance"; continue; fi
        git add -f "$f"
    done
    return 0
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag
    ajouter_donnees
    if git commit -qm "Relance de R1 : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json s'il existe)"
    else
        journal "ARRÊT pendant $1 : aucun résultat à committer"
    fi
    traces "arrêt pendant $1"
    if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi
}
ETAPE="mise en place"
PID_RUN=""
sur_term() {
    trap '' TERM
    journal "TERM reçu pendant $ETAPE (plafond de l'amorce)"
    if [ -n "$PID_RUN" ]; then kill -TERM "$PID_RUN" 2>/dev/null || true; wait "$PID_RUN" 2>/dev/null || true; fi
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
python -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>/dev/null || journal "pip freeze impossible (descriptif)"
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch : arrêt avant les tests"; consigner_arret "contrôle de la carte"; exit 1
fi
ETAPE="tests"
CIBLES=(tests/test_runs_nuit_v1.py tests/test_premier_test_ia_run.py tests/test_premier_test_ia_notation.py
        tests/test_premier_test_ia_figees.py tests/test_premier_test_ia_conditions.py tests/test_harnais_formats.py
        tests/test_pilote_a.py tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py
        tests/test_harnais.py tests/test_bases.py tests/test_validation_reelle.py tests/test_harnais_lots.py
        tests/test_environnement_a.py tests/test_premier_test_ia_gardes_v1.py tests/test_premier_test_ia_entrainement.py tests/test_runs_nuit_v2.py)
if [ -n "${TESTS_CIBLES:-}" ]; then
    [ "$MODE" = jouet ] || { journal "TESTS_CIBLES n'est permis qu'en mode jouet : arrêt"; consigner_arret "tests"; exit 2; }
    read -r -a CIBLES <<<"$TESTS_CIBLES"
fi
if ! PYTHONPATH=src:tests python -m pytest -q -p no:cacheprovider --color=no "${CIBLES[@]}" >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"; consigner_arret "tests"; exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt")
journal "tests : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed », sans test sauté ni en échec : arrêt"; consigner_arret "tests"; exit 1
fi

# une étape : module, configuration, identifiant de run, délai externe en minutes ; complète si son résultat existe sans
# arrêt consigné ; sinon arrêt de toute la suite (les étapes déjà poussées restent)
etape() {
    local nom="$1" module="$2" config="$3" delai="$4" run code=0
    run="$(date -u +%Y%m%d-%H%M%S)-$nom-$MODE"
    ETAPE="$nom ($run)"
    journal "étape $nom : run $run, configuration $config"
    local args=()
    [ "$PREREG_ABSENT" = 1 ] || args=(--prereg "$PREREG")
    : >"$TRAVAIL/$nom.err"
    PYTHONPATH=src timeout --signal=TERM --kill-after=2m "${delai}m" python -m "$module" --config "$config" \
        --run-id "$run" "${args[@]}" >"$TRAVAIL/$nom.json" 2>>"$TRAVAIL/$nom.err" &
    PID_RUN=$!
    ( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/$nom.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
        | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
    local relais=$!
    wait "$PID_RUN" || code=$?
    PID_RUN=""
    wait "$relais" 2>/dev/null || true
    if [ "$code" -ne 0 ] || [ -f "diag/$run/arret.json" ]; then
        grep -v '^PROGRES ' "$TRAVAIL/$nom.err" | tail -n 5 | tee -a "$JOURNAL" || true
        git add -A runs diag; ajouter_donnees
        git commit -qm "Relance de R1 : arrêt de l'étape $nom ($run)" >/dev/null 2>&1 || true
        pousser || journal "poussée après l'arrêt de $nom impossible"
        journal "étape $nom arrêtée (code $code) ; étapes suivantes poursuivies"
        ARRETS="$ARRETS $nom"
        return 0
    fi
    git add "runs/$run" "diag/$run"
    ajouter_donnees
    git commit -qm "Relance de R1 ($MODE) : $nom, run $run"
    journal "étape $nom terminée : $run"
    pousser || journal "poussée après $nom impossible : résultats restés sur l'instance"
}
ARRETS=""
for e in $ETAPES; do
    case "$e" in
        rejeu)  [ -n "$CONFIG_REJEU" ] && etape r1-rejeu controle_ia.runs_nuit.rejeu_activations_v2 "$CONFIG_REJEU" 60 ;;
        *) journal "étape inconnue $e : arrêt"; consigner_arret "étapes"; exit 2 ;;
    esac
done
ETAPE="fin"
journal "fin : étapes « $ETAPES » passées (arrêtées :${ARRETS:- aucune}) ; arrêter l'instance par son identifiant (R10)"
CONSIGNE=1
traces "fin"
if pousser; then journal "branche $BRANCHE poussée (résultats et traces)"; else journal "poussée finale impossible"; exit 1; fi
[ -z "$ARRETS" ] || exit 1
