#!/usr/bin/env bash
# P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269) sur l'instance de calcul : mise en place, suite
# COMPLÈTE des tests (suite du dépôt et tests du module de P4 ; l'économie d'environ 30 minutes est refusée, contre-lecture 2,
# VP3-12), puis un run du module `docs/procedures/P4-instrument-v1/instrument_p4_v1.py` (M5, bras I, D, H, B, B′ ; aucune
# génération), poussée des résultats et des traces. Décliné de `scripts/p3_instance.sh` sous un nom neuf (R12). Versé sous
# docs/procedures/P4-instrument-v1/, hors de l'arbre gelé : un script ajouté sous scripts/ changerait l'arbre gelé, que
# le run exige égal à celui de P3 (`7a54d43`, instrument figé ; texte, Plan d'analyse, point 1.1, et Liste d'arrêt).
# Différences avec P3 : étude « p4 » ; aucune consigne ; configuration au chemin écrit par le texte
# (« chemin `prereg/P4-instrument-config-v1.json` », cité une fois, avec l'empreinte canonique, citée une fois) ;
# lignes « Module de P4 » présentes et fichiers du module présents avec leur sceau avant toute installation ; tests :
# `tests/` et les trois fichiers de tests du module, en un seul passage, au nombre cité (« Tests attendus : `N` ») ;
# données poussées : les trois tableaux du run (`validation-p4.npz`, `scores-p4.npz` — les cinq bras —,
# `jetons-principales-p4.npz`) et leurs sceaux, par ajout forcé ; AUCUN TEXTE : aucun fichier de textes n'est écrit ni
# poussé ; aucune activation gardée ; délai externe du run de 90 minutes (texte, Plan d'analyse, point 7). Lignes de
# progression du module (préfixe « PROGRES », couples clé=valeur) recopiées dans le journal que lit la surveillance.
# Rien ne se lance sans GO consigné (garde de calcul, lanceur).
# Chaîne v2 (module v2) : la suite du module exige `P4_TEXTE_PREREG` (chemin du préenregistrement, dont la table
# « Critères de lecture gelés » est comparée à celle du code) : exportée ici, égale à PREREG ; tout Python de ce
# script tourne avec -B et PYTHONDONTWRITEBYTECODE=1 (aucun `__pycache__` sous docs/procedures/P4-instrument-v1/).
#
#   COMMIT=<commit de scellement S> bash p4_instance_v1.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le module vérifie en plus le commit du code, l'arbre gelé, le module,
#                 la configuration, les données de P3, l'entropie et la révision
#   MODE          reel (défaut) ou jouet (répétition sur processeur)
#   PREREG        défaut prereg/P4-instrument-v1.md ; il cite, une seule fois chacun, « Tests attendus : `N` »,
#                 « Configuration de P4 (empreinte canonique) : `…` » et « chemin `prereg/P4-instrument-config-v1.json` »,
#                 que ce script lit avant toute installation
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia-travail.git (dépôt de travail privé ; N-016)
#   GH_TOKEN      jeton GitHub à grain fin ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel)
#   BRANCHE       défaut calcul/p4-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
#   TRAVAIL       défaut $HOME/p4
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement S du préenregistrement de P4)}"
ETUDE=p4
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE="${BRANCHE:-calcul/p4-$MODE-v1}"
PREREG="${PREREG:-prereg/P4-instrument-v1.md}"
TRAVAIL="${TRAVAIL:-$HOME/p4}"
MODULE=docs/procedures/P4-instrument-v1/instrument_p4_v1.py
TESTS_MODULE=(docs/procedures/P4-instrument-v1/test_instrument_p4_v1.py docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py
              docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py)
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac
export PYTHONDONTWRITEBYTECODE=1
# lignes de progression du module recopiées au journal : préfixe fixe, horodatage, puis des couples clé=valeur sans
# espace (nombres, étapes, bras, identifiants de tâches) ; aucune autre ligne de la sortie d'erreur n'y passe (aucun texte)
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
git config user.name "instance de calcul (P4)"
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

# Lecture précoce du préenregistrement, avant toute installation : chaque citation lue y figure une seule fois
[ -f "$PREREG" ] && [ -f "$PREREG.sha256" ] || { journal "préenregistrement $PREREG ou son sceau absent au commit $COMMIT : arrêt avant l'installation"; exit 2; }
n=$(grep -c "Tests attendus : \`" "$PREREG" || true)
ATTENDUS=$( [ "$n" = 1 ] && sed -n "s/.*Tests attendus : \`\([0-9][0-9]*\)\`.*/\1/p" "$PREREG" || true)
[[ "$ATTENDUS" =~ ^[0-9]+$ ]] || { journal "nombre de tests attendus introuvable ou cité plusieurs fois dans $PREREG : arrêt avant l'installation"; exit 2; }
CONFIG=prereg/P4-instrument-config-v1.json      # chemin écrit par le texte ; l'empreinte canonique est relue par le module
n=$(grep -c "Configuration de P4 (empreinte canonique) : \`[0-9a-f]\{64\}\`" "$PREREG" || true)
nc=$(grep -o "chemin \`$CONFIG\`" "$PREREG" | wc -l)
[ "$n" = 1 ] && [ "$nc" = 1 ] || { journal "empreinte de la configuration de P4 ou chemin \`$CONFIG\` absents ou cités plusieurs fois : arrêt avant l'installation"; exit 2; }
NM=$(grep -cE '^[[:space:]]*-[[:space:]]+Module de P4 : `docs/procedures/P4-instrument-v1/[a-z0-9_]+\.py` : `[0-9a-f]{64}`[[:space:]]*$' "$PREREG" || true)
[ "$NM" = 6 ] || { journal "lignes « Module de P4 » : $NM au lieu de 6 : arrêt avant l'installation"; exit 2; }
for f in "$CONFIG" "$MODULE" "${TESTS_MODULE[@]}"; do
    [ -f "$f" ] && [ -f "$f.sha256" ] || { journal "fichier $f ou son sceau absent de l'arbre du commit $COMMIT : arrêt avant l'installation"; exit 2; }
done
if ! PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -u -m controle_ia.scellement verifier "$PREREG" "$CONFIG" "$MODULE" "${TESTS_MODULE[@]}" \
        >"$TRAVAIL/sceaux.txt" 2>&1; then
    cause=$(grep -v '^OK ' "$TRAVAIL/sceaux.txt" | tail -n 1 || true)
    journal "sceau non conforme parmi le préenregistrement, la configuration et le module ($cause) : arrêt avant l'installation"
    exit 2
fi
journal "préenregistrement lu : $ATTENDUS tests attendus ; configuration $CONFIG ; module $MODULE : présents et scellés"

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
    d=$(mktemp -d "traces/p4-$(date -u +%Y%m%d-%H%M%S)-XXXX")
    for f in "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" "$TRAVAIL"/run.json "$TRAVAIL"/run.err \
             "$TRAVAIL"/nvidia-smi.txt "$TRAVAIL"/pip-freeze.txt; do
        [ -f "$f" ] && cp "$f" "$d/"
    done
    (cd "$d" && sha256sum -- * > empreintes.sha256) || true
    git add "$d" && git commit -qm "P4 : traces de l'instance ($1)" >/dev/null 2>&1 || true
}
# données du run, par ajout forcé (donnees/ est ignoré par git) : les trois tableaux de P4 et leurs sceaux, du seul run de
# P4 de cette instance ; aucun fichier de textes (le run n'en écrit pas)
ajouter_donnees() {
    local f
    for f in donnees/*-p4-"$MODE"/validation-p4.npz donnees/*-p4-"$MODE"/validation-p4.npz.sha256 \
             donnees/*-p4-"$MODE"/scores-p4.npz donnees/*-p4-"$MODE"/scores-p4.npz.sha256 \
             donnees/*-p4-"$MODE"/jetons-principales-p4.npz donnees/*-p4-"$MODE"/jetons-principales-p4.npz.sha256; do
        if [ -f "$f" ]; then git add -f "$f"; fi
    done
    return 0
}
CONSIGNE=""
consigner_arret() {
    CONSIGNE=1
    git add -A runs diag
    ajouter_donnees
    if git commit -qm "P4 : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont le résumé avec son motif s'il existe)"
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
if ! python -B -m pip freeze --all >"$TRAVAIL/pip-freeze.txt" 2>"$TRAVAIL/pip-freeze.err"; then
    journal "pip freeze impossible (descriptif, sans effet sur le run) : $(tail -n 1 "$TRAVAIL/pip-freeze.err" | tr '\n' ' ')"
fi

python -B -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if [ "$MODE" = reel ] && ! python -B -c "import sys, torch; sys.exit(0 if torch.cuda.is_available() else 1)"; then
    journal "carte indisponible pour torch (pilote CUDA trop ancien ?) : arrêt avant les tests"
    consigner_arret "contrôle de la carte"
    exit 1
fi
# suite COMPLÈTE : tests du dépôt et tests du module de P4, en un seul passage, au nombre cité (VP3-12)
ETAPE="tests"
if ! P4_TEXTE_PREREG="$PREREG" PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider --color=no tests "${TESTS_MODULE[@]}" >"$TRAVAIL/tests.txt" 2>"$TRAVAIL/tests.err"; then
    tail -n 5 "$TRAVAIL/tests.txt" "$TRAVAIL/tests.err" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi
DERNIERE=$(tail -1 "$TRAVAIL/tests.txt")
journal "tests : $DERNIERE"
if ! printf '%s\n' "$DERNIERE" | grep -Eq "^$ATTENDUS passed(, [0-9]+ warnings?)? in [0-9.]+s( \([0-9]+:[0-9]{2}:[0-9]{2}\))?$"; then
    journal "tests : « $DERNIERE » ≠ « $ATTENDUS passed », sans test sauté ni en échec : arrêt"
    consigner_arret "tests"
    exit 1
fi

ETAPE="lancement"
journal "configuration : $CONFIG ; module : $MODULE"
# délai externe du run, figé (R1) : TERM à 90 minutes, converti par le module en arrêt consigné (résumé avec son motif),
# puis KILL cinq minutes plus tard ; l'échéance interne (duree_max_s, 3 600 s) est plus courte. Le signal vise le
# processus lancé par timeout, par son identifiant (R10).
DELAI=(timeout --signal=TERM --kill-after=5m 90m)
RUN="$(date -u +%Y%m%d-%H%M%S)-p4-$MODE"
ETAPE="run $RUN"
journal "run : $RUN"
code=0
: >"$TRAVAIL/run.err"
PYTHONPATH=src "${DELAI[@]}" python -B "$MODULE" --config "$CONFIG" --prereg "$PREREG" --run-id "$RUN" >"$TRAVAIL/run.json" \
    2>>"$TRAVAIL/run.err" &
PID_RUN=$!
# relais des lignes de progression : tail s'arrête de lui-même quand le run se termine (--pid), sans arrêt par motif
( tail -n +1 -F --pid="$PID_RUN" "$TRAVAIL/run.err" 2>/dev/null | grep --line-buffered -E "$MOTIF_PROGRES" \
    | while IFS= read -r ligne; do printf '%s\n' "$ligne" | tee -a "$JOURNAL"; done ) &
PID_RELAIS=$!
wait "$PID_RUN" || code=$?
PID_RUN=""
wait "$PID_RELAIS" 2>/dev/null || true
# un run est complet si son résumé existe sans motif d'arrêt (le module écrit le résumé avant tout arrêt, avec son motif)
complet() { [ -f "diag/$RUN/resume.json" ] && python3 -B -c 'import json, sys; sys.exit(0 if json.load(open(sys.argv[1]))["resultat"].get("arret") is None else 1)' "diag/$RUN/resume.json" 2>/dev/null; }
if [ "$code" -ne 0 ]; then
    if complet; then
        journal "run : code $code, mais résumé écrit sans motif d'arrêt : run complet"
    else
        # diagnostic : dernières lignes de la sortie d'erreur, hors de toute ligne de progression (motifs de garde, aucun texte)
        grep -v '^PROGRES ' "$TRAVAIL/run.err" | tail -n 5 | cut -c1-300 | tee -a "$JOURNAL" || true
        consigner_arret "run (code $code)"; exit 1
    fi
fi
git add "runs/$RUN" "diag/$RUN"
ajouter_donnees
git commit -qm "P4 ($MODE), run $RUN"
# le résumé reste dans run.json, versé aux traces ; il n'est pas recopié au journal que lit la surveillance
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
