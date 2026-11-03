#!/usr/bin/env bash
# Pilote préenregistré de l'exposant p (Ferreira da Silva et Heimersheim, arXiv 2606.24964) sur l'instance de calcul :
# plan (évaluation, registre) sur Llama-3.1-8B-Instruct, témoin positif sur Llama-3.1-8B. Mise en place, accès aux deux
# modèles vérifié, essais, un run du lanceur `controle_ia.pilote_exposant_p.run`, poussée des résultats (runs/, diag/)
# et des traces sur une branche `calcul/…` neuve, fin propre. Décliné de `scripts/p3_instance.sh` sous un nom nouveau
# (R12 : le script de P3 n'est pas modifié). Différences : étude « pilote-exposant-p » ; citations lues dans le
# préenregistrement (essais attendus, configuration, stimuli) ; accès Hugging Face vérifié sur les deux modèles avant
# tout téléchargement lourd, jeton lu par nom (jamais affiché) ; dépendances de l'instance installées sous la contrainte
# du `pip freeze` de l'environnement GPU ; essais limités aux quatre fichiers du pilote et des modules qu'il appelle ;
# code 3 du lanceur = « instrument non validé » (run complet, rien n'est lu) ; délai externe de 270 minutes.
# Ce script ne se lance pas sans GO consigné (garde de calcul, registres/go.md) ; il n'a jamais été lancé.
#
#   COMMIT=<commit de scellement du préenregistrement du pilote> bash pilote_exposant_p_instance_v1.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le lanceur vérifie en plus configuration, stimuli, références,
#                 copie amont et préenregistrement scellé
#   MODE          reel (défaut) ou jouet (répétition sur processeur, petit modèle aléatoire, aucun téléchargement de modèle)
#   PREREG        défaut prereg/pilote-exposant-p-v1.md ; il cite, une seule fois chacun, « Tests attendus : `N` »,
#                 « Chemin de la configuration du pilote : `…` », « Chemin des stimuli du pilote : `…` »
#   PREREG_ABSENT 1 seulement en mode jouet : répétition sans préenregistrement ; CONFIG et STIMULI donnent les chemins
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN      jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel) ; licence Llama 3.1 acceptée pour les deux dépôts
#   BRANCHE       défaut calcul/pilote-exposant-p-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TESTS_ATTENDUS nombre d'essais attendus (sans préenregistrement seulement)
#   TRAVAIL       défaut $HOME/pilote-exposant-p
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement du préenregistrement du pilote)}"
ETUDE=pilote-exposant-p
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/pilote-exposant-p-$MODE-v1}"
PREREG="${PREREG:-prereg/pilote-exposant-p-v1.md}"
TRAVAIL="${TRAVAIL:-$HOME/pilote-exposant-p}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
FICHIERS_ESSAIS=(tests/test_pilote_exposant_p_v1.py tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py)
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
if [ "$PREREG_ABSENT" = 1 ] && [ "$MODE" != jouet ]; then
    echo "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)" >&2; exit 2
fi
case "$BRANCHE" in calcul/*) ;; *) echo "BRANCHE=$BRANCHE : une branche calcul/… neuve est exigée" >&2; exit 2 ;; esac
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : ETUDE=$ETUDE MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE"
if [ "$MODE" = reel ]; then
    # le jeton est lu par son nom seulement ; sa valeur n'est jamais affichée ni écrite
    if [ -z "${HF_TOKEN:-}" ]; then journal "HF_TOKEN absent en mode reel : arrêt"; exit 2; fi
fi

DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (pilote exposant p)"
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

# Lecture précoce du préenregistrement, avant toute installation : chaque citation lue doit y figurer une seule fois
lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$PREREG" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"
}
if [ "$PREREG_ABSENT" = 1 ]; then
    ATTENDUS="${TESTS_ATTENDUS:-}"
    : "${CONFIG:?CONFIG obligatoire sans préenregistrement}" "${STIMULI:?STIMULI obligatoire sans préenregistrement}"
else
    [ -f "$PREREG" ] || { journal "préenregistrement $PREREG absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
    ATTENDUS=$(lire_unique "Tests attendus")
    [[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre d'essais attendus introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
    CONFIG=$(lire_unique "Chemin de la configuration du pilote")
    STIMULI=$(lire_unique "Chemin des stimuli du pilote")
    CITES=("$PREREG" "$CONFIG" "$STIMULI")
    for f in "${CITES[@]}"; do
        [ -n "$f" ] || { journal "chemin cité introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
        if [ ! -f "$f" ] || [ ! -f "$f.sha256" ]; then
            journal "fichier cité $f ou son sceau absent de l'arbre du commit $COMMIT : arrêt avant l'installation"
            exit 2
        fi
    done
    if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "${CITES[@]}" \
            >"$TRAVAIL/sceaux.txt" 2>&1; then
        cause=$(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1 || true)
        journal "sceau non conforme parmi les fichiers cités ($cause) : arrêt avant l'installation"
        exit 2
    fi
    journal "préenregistrement lu : $ATTENDUS essais attendus ; configuration $CONFIG ; stimuli $STIMULI : présents et scellés"
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
    d=$(mktemp -d "traces/pilote-exposant-p-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL"/run.json "$TRAVAIL"/run.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt "$TRAVAIL"/acces-hf.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "Pilote exposant p : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag 2>/dev/null || true
    if git commit -qm "Pilote exposant p : arrêt pendant $1" >/dev/null 2>&1; then
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
    journal "TERM reçu pendant $ETAPE (plafond externe)"
    if [ -n "$PID_RUN" ]; then
        kill -TERM "$PID_RUN" 2>/dev/null || true
        wait "$PID_RUN" 2>/dev/null || true
    fi
    consigner_arret "$ETAPE (plafond externe)" || true
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
    df -h "$HOME" | tee -a "$JOURNAL"
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
# dépendances du pilote sous contrainte : aucun paquet déjà installé ne doit changer de version
python -m pip freeze --all >"$TRAVAIL/contraintes.txt"
if ! pip install -q -c "$TRAVAIL/contraintes.txt" -r src/controle_ia/pilote_exposant_p/requirements-instance-v1.txt \
        >"$TRAVAIL/pip-pilote.txt" 2>&1; then
    journal "dépendances du pilote non installables sans changer une version figée : arrêt avant les essais"
    tail -n 5 "$TRAVAIL/pip-pilote.txt" | tee -a "$JOURNAL"
    consigner_arret "installation"
    exit 1
fi
if ! python -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>"$TRAVAIL/pip-freeze.err"; then
    journal "pip freeze impossible (descriptif, sans effet sur le run) : $(tail -n 1 "$TRAVAIL/pip-freeze.err" | tr '\n' ' ')"
fi

python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ]; then
    if ! python -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
        journal "carte indisponible pour torch (pilote CUDA trop ancien ?) : arrêt avant les essais"
        consigner_arret "contrôle de la carte"
        exit 1
    fi
    ETAPE="accès Hugging Face"
    # accès aux deux dépôts vérifié avant tout téléchargement lourd ; seuls les noms et les révisions sont écrits
    if ! python - "$CONFIG" >"$TRAVAIL/acces-hf.txt" 2>&1 <<'PY'
import json, sys
from huggingface_hub import HfApi
cfg_noms = list(json.load(open(sys.argv[1], encoding="utf-8"))["modeles"].values())
api = HfApi()
ok = True
for nom in cfg_noms:
    try:
        info = api.model_info(nom)
        api.hf_hub_download(nom, "config.json")
        print(json.dumps({"modele": nom, "revision": info.sha, "acces": True}))
    except Exception as e:  # nom de l'exception seulement : le message peut citer l'en-tête d'autorisation
        print(json.dumps({"modele": nom, "acces": False, "erreur": type(e).__name__}))
        ok = False
sys.exit(0 if ok else 1)
PY
    then
        cat "$TRAVAIL/acces-hf.txt" | tee -a "$JOURNAL"
        journal "accès refusé à au moins un des deux modèles (licence ou jeton) : arrêt avant les essais"
        consigner_arret "accès Hugging Face"
        exit 1
    fi
    tee -a "$JOURNAL" <"$TRAVAIL/acces-hf.txt"
fi
ETAPE="essais"
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider --color=no "${FICHIERS_ESSAIS[@]}" >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" | tee -a "$JOURNAL"
    journal "essais en échec : arrêt"
    consigner_arret "essais"
    exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt")
journal "essais : $DERNIERE"
if [ -n "$ATTENDUS" ] && ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "essais : « $DERNIERE » ≠ « $ATTENDUS passed », sans essai sauté ni en échec : arrêt"
    consigner_arret "essais"
    exit 1
fi

ETAPE="lancement"
ARGS=()
if [ "$PREREG_ABSENT" = 1 ]; then
    journal "répétition sans préenregistrement (jouet, non décisive)"
    ARGS=(--jouet)
else
    ARGS=(--prereg "$PREREG")
    if [ "$MODE" = jouet ]; then ARGS+=(--jouet); fi
fi
journal "configuration : $CONFIG ; stimuli : $STIMULI"
# délai externe du run, figé (R1) : TERM à 270 minutes, converti en arrêt consigné, puis KILL cinq minutes plus tard ;
# le plafond interne du lanceur (plafonds.duree_max_s, 14 400 s) est plus court. Le signal vise le processus lancé
# par timeout, par son identifiant (R10).
DELAI=(timeout --signal=TERM --kill-after=5m 270m)
RUN="$(date -u +%Y%m%d-%H%M%S)-pilote-exposant-p-$MODE"
ETAPE="run $RUN"
journal "run : $RUN"
code=0
: >"$TRAVAIL/run.err"
PYTHONPATH=src "${DELAI[@]}" python -m controle_ia.pilote_exposant_p.run --config "$CONFIG" --stimuli "$STIMULI" \
    --run-id "$RUN" "${ARGS[@]}" >"$TRAVAIL/run.json" 2>>"$TRAVAIL/run.err" &
PID_RUN=$!
( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
    | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
PID_RELAIS=$!
wait "$PID_RUN" || code=$?
PID_RUN=""
wait "$PID_RELAIS" 2>/dev/null || true
# un run est complet si son résumé existe sans arrêt consigné ; code 3 = « instrument non validé » (run complet)
if [ "$code" -ne 0 ]; then
    if [ -f "diag/$RUN/resume.json" ] && [ ! -f "diag/$RUN/arret.json" ]; then
        journal "run : code $code, résumé écrit sans arrêt consigné : run complet (3 = instrument non validé)"
    else
        grep -v '^PROGRES ' "$TRAVAIL/run.err" | tail -n 5 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; exit 1
    fi
fi
git add "runs/$RUN" "diag/$RUN"
git commit -qm "Pilote exposant p ($MODE), run $RUN"
journal "run terminé : $RUN"
ETAPE="poussée"
pousser || journal "poussée du run impossible : résultats restés sur l'instance"
ETAPE="fin"
journal "fin : $RUN ; arrêter l'instance par son identifiant (R10)"
CONSIGNE=1
traces "fin"
if pousser; then
    journal "branche $BRANCHE poussée (résultats et traces)"
else
    journal "run complet, mais poussée finale impossible après trois tentatives : résultats et traces restés sur l'instance"
    exit 1
fi
