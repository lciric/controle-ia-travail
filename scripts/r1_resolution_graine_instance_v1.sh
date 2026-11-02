#!/usr/bin/env bash
# Rejeu à graine des épisodes de P3 sur l'instance de calcul (relance de R1 : « résoudre les 7 épisodes avant la
# relance ») : étape « validation » (les épisodes résolus de la table de tokenisation v2, à l'aveugle), puis, seulement
# si la validation atteint son seuil, étape « resolution » (les 7 épisodes de C-6). Module
# `controle_ia.runs_nuit.resolution_graine_v1`. Version 1, nom nouveau (R12), sur le modèle de
# `r1_relance_instance_v2.sh` (inchangé). Préenregistrement par défaut : `prereg/R1-addendum-relance-v2.md` (scellé avant
# tout lancement ; il cite le commit du code, l'entropie, l'empreinte canonique de la configuration, « Tests attendus »
# et « Chemin de la configuration de la résolution à graine »). Dépense : sous le GO que Lazar donnera pour ce passage
# (aucun GO n'est supposé ici ; la garde de calcul de la session exige GO_ID au lancement de l'instance).
#
#   COMMIT=<commit de scellement de l'addendum v2> bash r1_resolution_graine_instance_v1.sh
#
# Variables :
#   COMMIT         (obligatoire) commit à extraire
#   PREREG         défaut prereg/R1-addendum-relance-v2.md ; cite une seule fois chacun « Tests attendus : `N` » et
#                  « Chemin de la configuration de la résolution à graine : `…` », lus avant toute installation
#   DEPOT_URL      défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN       jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit ni affiché
#   HF_TOKEN       jeton Hugging Face en lecture (licence Llama 3.1 acceptée) ; lu par huggingface_hub, jamais écrit
#   BRANCHE        défaut calcul/r1-resolution-graine-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TRAVAIL        défaut $HOME/r1graine
#   VENV_EXISTANT  environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
#   TORCH_ATTENDU  défaut 2.14.1 (version de P3 ; la méthode suppose son tirage multinomial) : autre version → arrêt
#   CARTE_ATTENDUE défaut A100-SXM4-80GB (carte de P3, `diag/20261019-230011-p3-reel/episodes-p3.json`) ; autre carte :
#                  réserve consignée au journal, sans arrêt (la validation à l'aveugle juge)
#   ARRET_AVANT_CALCUL 1 : essai local des gardes ; arrêt propre après les tests, avant le téléchargement du modèle
# Plafond : 60 minutes pour l'ensemble (amorce) ; délais externes : validation 35 min, résolution 15 min. Sorties scellées
# par le module avant toute lecture (`diag/<run>/*.json` et `.npz`, compagnons `.sha256`) ; rien n'est lu ni affiché
# ici hors des lignes de progression et de la dernière ligne des erreurs. Arrêt de l'instance : par la session de
# pilotage, par son identifiant (R10).
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/r1-resolution-graine-v1}"
PREREG="${PREREG:-prereg/R1-addendum-relance-v2.md}"
TRAVAIL="${TRAVAIL:-$HOME/r1graine}"
TORCH_ATTENDU="${TORCH_ATTENDU:-2.14.1}"
CARTE_ATTENDUE="${CARTE_ATTENDUE:-A100-SXM4-80GB}"
ARRET_AVANT_CALCUL="${ARRET_AVANT_CALCUL:-0}"
MODULE=controle_ia.runs_nuit.resolution_graine_v1
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : rejeu à graine COMMIT=$COMMIT BRANCHE=$BRANCHE"
if [ "$ARRET_AVANT_CALCUL" != 1 ]; then
    : "${HF_TOKEN:?HF_TOKEN obligatoire}"
fi
DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (rejeu à graine)"
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
[ -f "$PREREG" ] && [ -f "$PREREG.sha256" ] || { journal "préenregistrement $PREREG ou son sceau absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
ATTENDUS=$(lire_unique "Tests attendus")
[[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois dans $PREREG : arrêt"; exit 2; }
CONFIG=$(lire_unique "Chemin de la configuration de la résolution à graine")
[ -n "$CONFIG" ] || { journal "chemin de la configuration introuvable ou cité plusieurs fois dans $PREREG : arrêt"; exit 2; }
[ -f "$CONFIG" ] && [ -f "$CONFIG.sha256" ] || { journal "configuration $CONFIG ou son sceau absent : arrêt avant l'installation"; exit 2; }
if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "$PREREG" "$CONFIG" \
        >"$TRAVAIL/sceaux.txt" 2>&1; then
    journal "sceau non conforme ($(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1)) : arrêt avant l'installation"
    exit 2
fi
journal "addendum lu : $ATTENDUS tests attendus ; configuration $CONFIG : présents et scellés"

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
    d=$(mktemp -d "traces/r1-graine-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL"/tests.txt "$TRAVAIL"/tests.err "$TRAVAIL"/*.json "$TRAVAIL"/*.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "Rejeu à graine : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag 2>/dev/null || true
    if git commit -qm "Rejeu à graine : arrêt pendant $1" >/dev/null 2>&1; then
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

if command -v nvidia-smi >/dev/null 2>&1; then
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL" "$TRAVAIL/nvidia-smi.txt"
    if ! grep -q "$CARTE_ATTENDUE" "$TRAVAIL/nvidia-smi.txt"; then
        journal "RÉSERVE : carte autre que $CARTE_ATTENDUE (celle de P3) ; arrondis des logits possiblement plus éloignés ; la validation juge"
    fi
elif [ "$ARRET_AVANT_CALCUL" != 1 ]; then
    journal "nvidia-smi absent : arrêt avant l'installation"; consigner_arret "contrôle de la carte"; exit 1
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
VERSION_TORCH=$(python -c "import torch; print(torch.__version__.split('+')[0])")
if [ "$VERSION_TORCH" != "$TORCH_ATTENDU" ]; then
    journal "torch $VERSION_TORCH ≠ $TORCH_ATTENDU (version de P3) : arrêt avant le téléchargement"; consigner_arret "contrôle de torch"; exit 1
fi
if [ "$ARRET_AVANT_CALCUL" != 1 ] && ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch : arrêt avant le téléchargement"; consigner_arret "contrôle de la carte"; exit 1
fi

# modèle et tokeniseur à la révision de P3 (lus dans la configuration scellée) ; les tests lisent ce tokeniseur
ETAPE="téléchargement du modèle"
if [ "$ARRET_AVANT_CALCUL" = 1 ]; then
    : "${TOKENISEUR_LLAMA31:?essai local : TOKENISEUR_LLAMA31 (dossier du tokeniseur à la révision de P3) obligatoire}"
else
    if ! PYTHONPATH=src python - "$CONFIG" >"$TRAVAIL/modele.txt" 2>"$TRAVAIL/modele.err" <<'PY'
import json, sys
from controle_ia.harnais.modeles import precharger_modele
a = json.load(open(sys.argv[1], encoding="utf-8"))["agent"]
print(precharger_modele(a["modele"], a["revision"]))
PY
    then
        journal "téléchargement du modèle impossible ($(tail -n 1 "$TRAVAIL/modele.err")) : arrêt"; consigner_arret "$ETAPE"; exit 1
    fi
    TOKENISEUR_LLAMA31=$(tail -n 1 "$TRAVAIL/modele.txt")
    export TOKENISEUR_LLAMA31
    journal "modèle et tokeniseur en cache : $(basename "$TOKENISEUR_LLAMA31")"
fi

ETAPE="tests"
CIBLES=(tests/test_resolution_graine_v1.py tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py
        tests/test_harnais_formats.py)
if ! PYTHONPATH=src:tests python -m pytest -q -p no:cacheprovider --color=no "${CIBLES[@]}" >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"; consigner_arret "tests"; exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt")
journal "tests : $DERNIERE"
if ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed », sans test sauté ni en échec : arrêt"; consigner_arret "tests"; exit 1
fi
if [ "$ARRET_AVANT_CALCUL" = 1 ]; then
    journal "ARRET_AVANT_CALCUL=1 : essai des gardes terminé avant le calcul"
    CONSIGNE=1
    exit 0
fi

# une étape : nom, délai externe en minutes, arguments du module ; rend 0 si le résultat existe sans arrêt consigné
RUN=""
etape() {
    local nom="$1" delai="$2" code=0
    shift 2
    RUN="$(date -u +%Y%m%d-%H%M%S)-r1-graine-$nom"
    ETAPE="$nom ($RUN)"
    journal "étape $nom : run $RUN"
    : >"$TRAVAIL/$nom.err"
    PYTHONPATH=src timeout --signal=TERM --kill-after=2m "${delai}m" python -m "$MODULE" --etape "$nom" --config "$CONFIG" \
        --run-id "$RUN" --prereg "$PREREG" "$@" >"$TRAVAIL/$nom.json" 2>>"$TRAVAIL/$nom.err" &
    PID_RUN=$!
    ( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/$nom.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
        | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
    local relais=$!
    wait "$PID_RUN" || code=$?
    PID_RUN=""
    wait "$relais" 2>/dev/null || true
    git add -A "runs/$RUN" "diag/$RUN" 2>/dev/null || true
    if [ "$code" -ne 0 ] || [ -f "diag/$RUN/arret.json" ]; then
        grep -v '^PROGRES ' "$TRAVAIL/$nom.err" | tail -n 1 | tee -a "$JOURNAL" || true
        git commit -qm "Rejeu à graine : arrêt de l'étape $nom ($RUN)" >/dev/null 2>&1 || true
        pousser || journal "poussée après l'arrêt de $nom impossible"
        journal "étape $nom arrêtée (code $code)"
        return 1
    fi
    git commit -qm "Rejeu à graine : $nom, run $RUN"
    journal "étape $nom terminée : $RUN"
    pousser || journal "poussée après $nom impossible : résultats restés sur l'instance"
    return 0
}
if ! etape validation 35; then
    journal "validation non atteinte ou arrêtée : résolution non lancée"
    CONSIGNE=1
    traces "validation arrêtée"
    pousser || journal "poussée finale impossible"
    exit 1
fi
RUN_VALIDATION="$RUN"
if ! etape resolution 15 --validation "diag/$RUN_VALIDATION/resolution-graine-validation.json"; then
    CONSIGNE=1
    traces "résolution arrêtée"
    pousser || journal "poussée finale impossible"
    exit 1
fi
ETAPE="fin"
journal "fin : validation $RUN_VALIDATION et résolution $RUN passées ; arrêter l'instance par son identifiant (R10)"
CONSIGNE=1
traces "fin"
if pousser; then journal "branche $BRANCHE poussée (résultats et traces)"; else journal "poussée finale impossible"; exit 1; fi
