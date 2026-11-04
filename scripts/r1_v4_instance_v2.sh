#!/usr/bin/env bash
# Relance v4 de R1 sur l'instance de calcul, selon l'addendum `prereg/R1-addendum-relance-v4.md` (à sceller ; dépense
# sous le GO de calcul qu'il cite). Script neuf (R12), version 2 de `r1_v4_instance_v1.sh` (non modifié) : module de la
# réparation `resolution_graine_lot_v3` (témoin non exact → lot puis repli, arbitrage M7 ; mesure de l'indépendance des
# lignes, I5), étape « chaine » neuve entre la table v4 et le rejeu (`chaine_table_v4_v1`, I1 : arrêt avant le rejeu
# si la table ne suit pas exactement le résultat scellé de la réparation), essais neufs dans CIBLES ; même structure
# (gardes avant l'installation, branche de résultats neuve poussée d'abord, tests au nombre exact, étapes sous délai
# externe, poussées, traces, fin propre, arrêt de l'instance par la session et par son identifiant, R10).
# Deux sessions, une instance chacune, choisies par SESSION :
#   SESSION=temoin      étape « temoin » de `resolution_graine_lot_v3` (lots 2 et 13 de P3, lecture gelée « exact » /
#                       « non exact »), sortie scellée et poussée ; rien d'autre.
#   SESSION=reparation  étape « reparation » (voie lue dans le résultat scellé du témoin, versé à l'octet au commit
#                       lancé : TEMOIN_RUN), puis « table-v4 » (processeur : table v4 écrite et scellée au chemin cité
#                       par la configuration du rejeu, jamais écrasée, committée et poussée), puis « chaine » (garde
#                       de chaîne, processeur), puis le rejeu v4
#                       (`rejeu_activations_v4`, configuration v6 : table « construite-en-session », revérifiée par
#                       l'oracle de P3 au chargement).
# Le délai externe de chaque étape (DELAI_ETAPE_MIN) et le plafond de l'amorce sont des gardes contre une boucle folle,
# jamais des couperets de mesure (C2 du complément ; mots de Lazar du 2 novembre).
#
#   COMMIT=<commit> SESSION=temoin|reparation [TEMOIN_RUN=<run>] bash r1_v4_instance_v2.sh
#
# Variables :
#   COMMIT          (obligatoire) commit à extraire (commit de scellement de l'addendum v4, ou commit qui y ajoute le
#                   seul versement du run du témoin pour la session 2)
#   SESSION         (obligatoire) temoin ou reparation
#   TEMOIN_RUN      (session 2) identifiant du run du témoin, versé au commit : diag/<run>/resolution-graine-lot-v3-temoin.json
#                   et son sceau, runs/<run>/manifeste.json
#   MODE            reel (défaut) ou jouet (répétition sur processeur)
#   PREREG          défaut prereg/R1-addendum-relance-v4.md ; il cite une seule fois chacun : « Tests attendus : `N` »,
#                   « Chemin de la configuration de la réparation : `…` », « Chemin de la configuration du rejeu : `…` »,
#                   « Chemin de la table de tokenisation v3 : `…` », « Chemin du préenregistrement parent : `…` »
#   DELAI_ETAPE_MIN délai externe de chaque étape en minutes, entier de 1 à 9999 (défaut 4320) ; autre valeur : arrêt
#   DEPOT_URL       défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN, HF_TOKEN  jetons, lus par nom, jamais écrits
#   BRANCHE         défaut calcul/r1-v4-<SESSION>-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TRAVAIL         défaut $HOME/r1v4-<SESSION>
#   VENV_EXISTANT, TESTS_CIBLES, TOKENISEUR_LLAMA31, PREREG_ABSENT, CONFIG_REPARATION, CONFIG_REJEU, TESTS_ATTENDUS :
#                   répétition jouet seulement (comme la v3)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire}"
: "${SESSION:?SESSION obligatoire (temoin ou reparation)}"
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/r1-v4-$SESSION-$MODE-v1}"
PREREG="${PREREG:-prereg/R1-addendum-relance-v4.md}"
TRAVAIL="${TRAVAIL:-$HOME/r1v4-$SESSION}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
DELAI_ETAPE_MIN="${DELAI_ETAPE_MIN-4320}"
MODULE_LOT=controle_ia.runs_nuit.resolution_graine_lot_v3
MODULE_CHAINE=controle_ia.runs_nuit.chaine_table_v4_v1
MODULE_REJEU=controle_ia.runs_nuit.rejeu_activations_v4
case "$SESSION" in temoin|reparation) ;; *) echo "SESSION=$SESSION : temoin ou reparation : arrêt" >&2; exit 2 ;; esac
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if ! [[ "$DELAI_ETAPE_MIN" =~ ^[1-9][0-9]{0,3}$ ]]; then
    echo "DELAI_ETAPE_MIN=« $DELAI_ETAPE_MIN » : entier de minutes de 1 à 9999 attendu : arrêt avant tout clonage" >&2; exit 2
fi
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
if [ "$SESSION" = reparation ] && ! [[ "${TEMOIN_RUN:-}" =~ ^[0-9]{8}-[0-9]{6}-[a-z0-9-]+$ ]]; then
    echo "session reparation sans TEMOIN_RUN valide : arrêt avant tout clonage" >&2; exit 2
fi
if [ "$MODE" = jouet ] && [ -z "${TOKENISEUR_LLAMA31:-}" ] && [ -z "${TESTS_CIBLES:-}" ]; then
    echo "mode jouet sans TOKENISEUR_LLAMA31 ni TESTS_CIBLES : des tests seraient sautés : arrêt" >&2; exit 2
fi
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'
journal "début : relance v4 de R1, session $SESSION, MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE DELAI_ETAPE_MIN=$DELAI_ETAPE_MIN TEMOIN_RUN=${TEMOIN_RUN:-}"
[ "$MODE" = reel ] && : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel}"
DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then echo "$DEPOT existe déjà : R12 ; choisir un autre TRAVAIL" >&2; exit 2; fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (relance v4 de R1)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>"$TRAVAIL/ls-remote.err" || code_branche=$?
case "$code_branche" in
    0) journal "branche $BRANCHE déjà présente : arrêt avant l'installation"; exit 2 ;;
    2) ;;
    *) journal "vérification de la branche $BRANCHE impossible (code $code_branche) : arrêt avant l'installation"; exit 2 ;;
esac
git checkout -q -b "$BRANCHE"

lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$PREREG" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"
}
TABLE_V4=""
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG_REPARATION:?}" "${CONFIG_REJEU:=}"
else
    [ -f "$PREREG" ] && [ -f "$PREREG.sha256" ] || { journal "préenregistrement $PREREG ou son sceau absent : arrêt avant l'installation"; exit 2; }
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois : arrêt"; exit 2; }
    CONFIG_REPARATION=$(lire_unique "Chemin de la configuration de la réparation")
    CONFIG_REJEU=$(lire_unique "Chemin de la configuration du rejeu")
    TABLE_V3=$(lire_unique "Chemin de la table de tokenisation v3")
    PARENT=$(lire_unique "Chemin du préenregistrement parent")
    for f in "$PREREG" "$CONFIG_REPARATION" "$CONFIG_REJEU" "$TABLE_V3" "$PARENT"; do
        [ -n "$f" ] || { journal "chemin cité introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
        [ -f "$f" ] && [ -f "$f.sha256" ] || { journal "fichier cité $f ou son sceau absent : arrêt avant l'installation"; exit 2; }
    done
    if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "$PREREG" "$CONFIG_REPARATION" \
            "$CONFIG_REJEU" "$TABLE_V3" "$PARENT" >"$TRAVAIL/sceaux.txt" 2>&1; then
        journal "sceau non conforme parmi les fichiers cités ($(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1)) : arrêt avant l'installation"
        exit 2
    fi
fi
# la configuration de la réparation cite la table v3 (chemin et empreinte) ; celle du rejeu cite une table v4 absente du
# commit (construite dans la session, R12), d'empreinte « construite-en-session »
if ! TABLE_V4=$(python3 - "$CONFIG_REPARATION" "${CONFIG_REJEU:-}" "$SESSION" 2>"$TRAVAIL/configs.err" <<'PY'
import hashlib, json, os, sys
r = json.load(open(sys.argv[1], encoding="utf-8"))
t3 = r.get("chemin_table_v3")
if not t3 or not os.path.isfile(t3):
    sys.exit(f"table v3 citée {t3!r} absente")
if r.get("table_v3_sha256") not in (None, hashlib.sha256(open(t3, "rb").read()).hexdigest()):
    sys.exit("configuration de la réparation : table_v3_sha256 ≠ empreinte de la table v3")
if json.load(open(t3, encoding="utf-8")).get("version") != 3:
    sys.exit("table v3 citée : version ≠ 3")
if sys.argv[3] == "reparation":
    if not sys.argv[2]:
        sys.exit("session reparation sans configuration du rejeu")
    c = json.load(open(sys.argv[2], encoding="utf-8"))
    t4 = c.get("chemin_table_tokenisation")
    if c.get("table_tokenisation_sha256") != "construite-en-session":
        sys.exit("configuration du rejeu : table_tokenisation_sha256 ≠ « construite-en-session »")
    if not t4 or os.path.exists(t4) or os.path.exists(t4 + ".sha256"):
        sys.exit(f"table v4 {t4!r} déjà présente au commit (R12) ou non citée")
    print(t4)
PY
); then
    journal "configurations non conformes ($(tail -n 1 "$TRAVAIL/configs.err")) : arrêt avant l'installation"; exit 2
fi
if [ "$SESSION" = reparation ]; then
    TEMOIN="diag/$TEMOIN_RUN/resolution-graine-lot-v3-temoin.json"
    [ -f "$TEMOIN" ] && [ -f "$TEMOIN.sha256" ] && [ -f "runs/$TEMOIN_RUN/manifeste.json" ] \
        || { journal "résultat du témoin $TEMOIN (ou son sceau, ou son manifeste) absent au commit : arrêt avant l'installation"; exit 2; }
    [ ! -f "diag/$TEMOIN_RUN/arret.json" ] || { journal "témoin arrêté (arret.json) : arrêt avant l'installation"; exit 2; }
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "$TEMOIN" >>"$TRAVAIL/sceaux.txt" 2>&1 \
        || { journal "sceau du témoin non conforme : arrêt avant l'installation"; exit 2; }
    journal "témoin lu au commit : $TEMOIN (lecture : $(python3 -c "import json,sys; print(json.load(open(sys.argv[1]))['resultat']['lecture'])" "$TEMOIN"))"
fi
journal "addendum lu : $ATTENDUS tests attendus ; réparation $CONFIG_REPARATION ; rejeu ${CONFIG_REJEU:-} ; table v4 à écrire ${TABLE_V4:-(session 1 : aucune)}"
if ! git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee-initiale.err"; then
    journal "poussée initiale de $BRANCHE refusée ($(tail -n 1 "$TRAVAIL/poussee-initiale.err")) : arrêt"; exit 2
fi
journal "branche $BRANCHE poussée avant l'installation (droit d'écriture éprouvé)"

pousser() {
    local essai
    for essai in 1 2 3; do
        if git push -q origin "$BRANCHE" 2>"$TRAVAIL/poussee.err"; then return 0; fi
        journal "poussée de $BRANCHE : tentative $essai refusée ($(tail -n 1 "$TRAVAIL/poussee.err"))"
        if [ "$essai" -lt 3 ]; then sleep $((15 * essai * essai)); fi
    done
    return 1
}
traces() {
    local d
    mkdir -p traces
    d=$(mktemp -d "traces/r1-v4-$SESSION-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL"/tests.txt "$TRAVAIL"/tests.err "$TRAVAIL"/*.json "$TRAVAIL"/*.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "Relance v4 de R1 ($SESSION, script v2) : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
ajouter_donnees() {
    local f
    for f in donnees/*/activations-p3-rejeu-v1*.npz donnees/*/activations-p3-rejeu-v1*.npz.sha256; do
        [ -f "$f" ] || continue
        if [ "$(stat -c %s "$f")" -gt 99000000 ]; then journal "$f : au-dessus de la limite de poussée : laissé sur l'instance"; continue; fi
        git add -f "$f"
    done
    return 0
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag prereg 2>/dev/null || true
    ajouter_donnees
    if git commit -qm "Relance v4 de R1 ($SESSION) : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json et épisodes consignés s'il en existe)"
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
    journal "TERM reçu pendant $ETAPE (plafond de l'amorce ou garde de dépense)"
    if [ -n "$PID_RUN" ]; then kill -TERM "$PID_RUN" 2>/dev/null || true; wait "$PID_RUN" 2>/dev/null || true; fi
    consigner_arret "$ETAPE (TERM)" || true
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
if [ "$MODE" = reel ]; then
    ETAPE="préchargement du modèle"
    if ! PYTHONPATH=src python - "$CONFIG_REPARATION" >"$TRAVAIL/modele.txt" 2>"$TRAVAIL/modele.err" <<'PY'
import json, sys
from controle_ia.harnais.modeles import precharger_modele
a = json.load(open(sys.argv[1], encoding="utf-8"))["agent"]
print(precharger_modele(a["modele"], a["revision"]))
PY
    then
        journal "préchargement du modèle impossible ($(tail -n 1 "$TRAVAIL/modele.err")) : arrêt"; consigner_arret "$ETAPE"; exit 1
    fi
    TOKENISEUR_LLAMA31=$(tail -n 1 "$TRAVAIL/modele.txt")
    export TOKENISEUR_LLAMA31
    journal "modèle et tokeniseur en cache : $(basename "$TOKENISEUR_LLAMA31")"
fi
ETAPE="tests"
CIBLES=(tests/test_runs_nuit_v1.py tests/test_premier_test_ia_run.py tests/test_premier_test_ia_notation.py
        tests/test_premier_test_ia_figees.py tests/test_premier_test_ia_conditions.py tests/test_harnais_formats.py
        tests/test_pilote_a.py tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py
        tests/test_harnais.py tests/test_bases.py tests/test_validation_reelle.py tests/test_harnais_lots.py
        tests/test_environnement_a.py tests/test_premier_test_ia_gardes_v1.py tests/test_premier_test_ia_entrainement.py tests/test_runs_nuit_v2.py
        tests/test_resolution_graine_v1.py tests/test_rejeu_activations_v3.py
        tests/test_resolution_graine_lot_v1.py tests/test_resolution_graine_lot_v2.py tests/test_rejeu_activations_v4.py
        tests/test_resolution_graine_lot_v3.py tests/test_chaine_table_v4_v1.py tests/test_garde_depense_v4_v1.py)
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

# une étape : nom, module puis ses arguments ; arrêt de toute la suite au premier arrêt (une étape suivante dépend
# toujours de la précédente : témoin → réparation → table → rejeu)
etape() {
    local nom="$1" run="$2"; shift 2
    local code=0
    ETAPE="$nom ($run)"
    journal "étape $nom : run $run, délai externe $DELAI_ETAPE_MIN min (garde contre une boucle folle)"
    : >"$TRAVAIL/$nom.err"
    PYTHONPATH=src timeout --signal=TERM --kill-after=2m "${DELAI_ETAPE_MIN}m" python -m "$@" \
        >"$TRAVAIL/$nom.json" 2>>"$TRAVAIL/$nom.err" &
    PID_RUN=$!
    ( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/$nom.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
        | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
    local relais=$!
    wait "$PID_RUN" || code=$?
    PID_RUN=""
    wait "$relais" 2>/dev/null || true
    if [ "$code" -ne 0 ] || { [ -n "$run" ] && [ -f "diag/$run/arret.json" ]; }; then
        grep -v '^PROGRES ' "$TRAVAIL/$nom.err" | tail -n 5 | tee -a "$JOURNAL" || true
        journal "étape $nom arrêtée (code $code) : étapes suivantes non lancées"
        consigner_arret "$nom"
        exit 1
    fi
    git add -A runs diag prereg 2>/dev/null || true
    ajouter_donnees
    git commit -qm "Relance v4 de R1 ($MODE, $SESSION) : $nom${run:+, run $run}" >/dev/null 2>&1 || true
    journal "étape $nom terminée${run:+ : $run}"
    pousser || journal "poussée après $nom impossible : résultats restés sur l'instance"
}
pre=()
[ "$PREREG_ABSENT" = 1 ] || pre=(--prereg "$PREREG")
horodatage() { date -u +%Y%m%d-%H%M%S; }
if [ "$SESSION" = temoin ]; then
    RUN_T="$(horodatage)-r1-v4-temoin-$MODE"
    etape temoin "$RUN_T" "$MODULE_LOT" --etape temoin --config "$CONFIG_REPARATION" --run-id "$RUN_T" "${pre[@]}"
else
    RUN_R="$(horodatage)-r1-v4-reparation-$MODE"
    etape reparation "$RUN_R" "$MODULE_LOT" --etape reparation --config "$CONFIG_REPARATION" --run-id "$RUN_R" \
        --temoin "$TEMOIN" "${pre[@]}"
    tok=()
    [ "$MODE" = reel ] && tok=(--tokeniseur "$TOKENISEUR_LLAMA31")
    etape table-v4 "" "$MODULE_LOT" --etape table-v4 --config "$CONFIG_REPARATION" \
        --reparation "diag/$RUN_R/resolution-graine-lot-v3-reparation.json" --sortie "$TABLE_V4" "${tok[@]}"
    [ -f "$TABLE_V4" ] && [ -f "$TABLE_V4.sha256" ] || { journal "table v4 absente après son étape : arrêt"; consigner_arret "table-v4"; exit 1; }
    journal "table v4 : $TABLE_V4 ($(cut -d' ' -f1 "$TABLE_V4.sha256"))"
    # garde de chaîne (I1) : table = sortie exacte du résultat scellé de la réparation (retrouvées et non retrouvées) ;
    # sinon arrêt avant le rejeu, rien n'est lu
    etape chaine "" "$MODULE_CHAINE" --config "$CONFIG_REPARATION" \
        --reparation "diag/$RUN_R/resolution-graine-lot-v3-reparation.json" --table "$TABLE_V4"
    journal "chaîne de la table v4 : conforme"
    RUN_J="$(horodatage)-r1-v4-rejeu-$MODE"
    etape r1-rejeu "$RUN_J" "$MODULE_REJEU" --config "$CONFIG_REJEU" --run-id "$RUN_J" "${pre[@]}"
fi
ETAPE="fin"
journal "fin : session $SESSION passée ; arrêter l'instance par son identifiant (R10)"
CONSIGNE=1
traces "fin"
if pousser; then journal "branche $BRANCHE poussée (résultats et traces)"; else journal "poussée finale impossible"; exit 1; fi
