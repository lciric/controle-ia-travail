#!/usr/bin/env bash
# v10 (R12) : copie du script d'instance v9 ; garde du code v10 ; essais v1 à v4 et v10 (outils couverts par l'amorce v10).
# v9 (R12) : copie du script d'instance v8 ; garde du code v9 ; essais v1 à v4 et v9.
# v8 (R12, minimale) : copie du script d'instance v7 ; manifeste de chaque phase par `sparks_exp7_nul_v8.manifeste_phase`, qui
# cite l'addendum scellé comme préenregistrement (le texte parent, cité dans la configuration, n'est vérifié que par son
# sceau : répétition v7, refus de `exiger_prereg_scelle`) ; refus du manifeste = arrêt avant tout calcul ; garde du code
# v8 ; essais v1 à v4 et v8.
# v7 (R12, minimale) : copie du script d'instance v6 ; appels de modules par la fonction `module` (interpréteur isolé `-I`,
# chemin absolu de src posé explicitement : `-I` ignore PYTHONPATH et le dossier courant, défaut des v1 à v6) ; manifeste de
# même ; garde du code v7 ; essais v1 à v4 et v7.
# v6 (R12, minimale) : copie du script d'instance v5 ; garde du code v6 ; essais v1 à v4 et v6 (l'essai v6 remplace
# l'essai v5, dont l'essai du tir dépendait du commit extrait et de la date : répétition v5, R-1514).
# SPARKS-EXP7-NUL sur l'instance louée, pour l'addendum n° 1, v5 (version neuve du script d'instance v4, R12 ; v5 : garde du
# code v5, essais v1 à v5, posé par l'amorce v5 ; v4 : la branche
# des sorties est posée par l'amorce v4, liée au commit et, en phase causale, à l'ordre (`BRANCHE`, exigée) ; garde du code
# v4 ; essais v1 à v4. Le reste, de la v3 :
# changements : modules v3, essais v1, v2 et v3, phase causale lancée par l'amorce v3 sur ordre écrit (sorties dans un
# dossier neuf, modèles lus sur le disque de la fabrication), **poussée vérifiée** (`git ls-remote` = tête locale, fichier
# `POUSSEE-VERIFIEE`), condition de la destruction par la minuterie) :
# clone partiel et clairsemé, gardes de code (liste fermée, addendum scellé), essais v1 et v2, accès au modèle de
# départ (code HTTP consigné, repli gelé), essai d'égalité des lots, fabrication v2 (étape 0, B3 et B4 sur
# l'étalonnage, couches du départ exportées) ou contrôle causal v2 (par lots, ou sans lots déclaré), manifeste,
# poussée des sorties légères sur une branche neuve. Les modèles et les couches du départ restent sur le disque.
#   COMMIT=<commit lancé> COMMIT_CODE=<commit du code> TRAVAIL=<dossier> GO_ID=GO-2026-11-04-04 BRANCHE=<branche> bash sparks_exp7_nul_instance_v5.sh
# Variables : MODE (reel | jouet), PHASE (fabrication | causal), BRANCHE, HF_TOKEN, GH_TOKEN, DEPOT_URL, VENV_EXISTANT ;
# phase causal : CLE, REPONSES (dossier des réponses scellées v2), MODELES.
set -euo pipefail
: "${COMMIT:?}" "${COMMIT_CODE:?}" "${TRAVAIL:?}" "${GO_ID:?}"
MODE="${MODE:-reel}"
PHASE="${PHASE:-fabrication}"
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE" >&2; exit 2 ;; esac
case "$PHASE" in fabrication|causal) ;; *) exit 2 ;; esac
: "${BRANCHE:?BRANCHE absente, posée par amorce v5}"
case "$BRANCHE" in calcul/sparks-exp7-nul-*|essai/sparks-exp7-nul-*) ;; *) echo "BRANCHE $BRANCHE hors des préfixes permis" >&2; exit 2 ;; esac
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
PREREG=prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md
SHA_PREREG=4bacf20dbb8a0e3f369119841d6fb0b56069d0d31989431238b115df746dd52d
mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'
journal "début : MODE=$MODE PHASE=$PHASE COMMIT=$COMMIT CODE=$COMMIT_CODE BRANCHE=$BRANCHE GO=$GO_ID"
DEPOT="$TRAVAIL/controle-ia"
[ -e "$DEPOT" ] && { journal "$DEPOT existe déjà (R12)"; exit 2; }
git -c credential.helper="$AIDE_GIT" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (SPARKS-EXP7-NUL)"
git config user.email "instance-calcul@invalid"
git sparse-checkout set --no-cone '/*' '!/*/' '/src/' '/tests/' '/scripts/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md' \
    '/docs/notes/sparks-exp7-nul-v1/' '/runs/' '/diag/'
git checkout -q "$COMMIT"
code_branche=0
git ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1 || code_branche=$?
[ "$code_branche" = 2 ] || { journal "branche $BRANCHE déjà présente ou dépôt illisible (code $code_branche) : arrêt"; exit 2; }
git checkout -q -b "$BRANCHE"
echo "$SHA_PREREG  $PREREG" | sha256sum -c --quiet || { journal "texte scellé altéré au commit : arrêt"; exit 2; }
python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v10'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" \
    lancement . "$COMMIT_CODE" "$COMMIT" >> "$JOURNAL" 2>&1 || { journal "garde du code : refus : arrêt"; exit 2; }
git push -q origin "$BRANCHE" || { journal "poussée initiale refusée : arrêt avant l'installation"; exit 2; }

if [ -n "${VENV_EXISTANT:-}" ]; then . "$VENV_EXISTANT/bin/activate"; else
    python3.11 -m venv "$TRAVAIL/venv" 2>/dev/null || python3 -m venv "$TRAVAIL/venv"
    . "$TRAVAIL/venv/bin/activate"
    pip install -q -r requirements-gpu.txt > "$TRAVAIL/pip.txt" 2>&1 || { journal "installation refusée"; exit 2; }
fi
pip freeze > "$TRAVAIL/pip-freeze.txt"
nvidia-smi > "$TRAVAIL/nvidia-smi.txt" 2>&1 || journal "pas de carte graphique visible"
export PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 TOKENIZERS_PARALLELISM=false
SRC="$PWD/src"   # le script est alors dans le clone, $DEPOT : chemin absolu
module() {  # module NOM ARGS… : interpréteur isolé (-I : ni PYTHON*, ni site de l'utilisateur, ni dossier courant) ; src posé par chemin absolu
    python -u -I -B -c 'import runpy, sys; sys.path.insert(0, sys.argv[1]); n = sys.argv[2]; sys.argv = [n] + sys.argv[3:]; runpy.run_module(n, run_name="__main__", alter_sys=True)' "$SRC" "$@"
}
python -I -B -m pytest -q -p no:cacheprovider tests/test_sparks_exp7_nul_v1.py tests/test_sparks_exp7_nul_v2.py tests/test_sparks_exp7_nul_v3.py tests/test_sparks_exp7_nul_v4.py tests/test_sparks_exp7_nul_v10.py > "$TRAVAIL/tests.txt" 2>&1 \
    || { journal "essais en échec : arrêt avant tout calcul"; tail -5 "$TRAVAIL/tests.txt"; exit 2; }
journal "essais : $(tail -1 "$TRAVAIL/tests.txt")"
LOTS=oui
module controle_ia.sparks_exp7_nul_v3.instance egalite-lots >> "$JOURNAL" 2>&1 || LOTS=non
journal "essai d'égalité des lots : $LOTS"

code_http() {
    curl -s -o /dev/null -w '%{http_code}' --max-time 60 ${HF_TOKEN:+-H "Authorization: Bearer $HF_TOKEN"} \
        "https://huggingface.co/$1/resolve/main/config.json" || echo 000
}
if [ "$MODE" = jouet ]; then DEPART=jouet; HTTP=sans-objet; else
    DEPART=""
    for candidat in google/gemma-3-270m-it Qwen/Qwen2.5-0.5B-Instruct HuggingFaceTB/SmolLM2-360M-Instruct; do
        HTTP=$(code_http "$candidat")
        journal "accès $candidat : HTTP $HTTP"
        echo "$candidat $HTTP" >> "$TRAVAIL/acces-modeles.txt"
        if [ "$HTTP" = 200 ]; then DEPART=$candidat; break; fi
    done
    [ -n "$DEPART" ] || { journal "aucun modèle accessible : arrêt"; exit 2; }
    [ "$DEPART" = google/gemma-3-270m-it ] || journal "REPLI : modèle de secours $DEPART employé et déclaré (Gemma inaccessible)"
fi

RUN_ID="$(date -u +%Y%m%d-%H%M%S)-sparks-exp7-nul-v5-$PHASE"
module controle_ia.sparks_exp7_nul_v8.manifeste_phase "$RUN_ID" "$DEPART" "$HTTP" "$PHASE" "$COMMIT_CODE" "$LOTS" "$MODE" >> "$JOURNAL" 2>&1 \
    || { journal "manifeste refusé (addendum scellé exigé) : arrêt avant tout calcul"; tail -3 "$JOURNAL"; exit 2; }
journal "manifeste runs/$RUN_ID/manifeste.json"
SORTIE="$TRAVAIL/sortie"
set +e
if [ "$PHASE" = fabrication ]; then
    if [ "$MODE" = jouet ]; then module controle_ia.sparks_exp7_nul_v3.instance jouet --sortie "$SORTIE" 2> "$TRAVAIL/run.err"
    else module controle_ia.sparks_exp7_nul_v3.instance fabriquer --sortie "$SORTIE" --depart "$DEPART" 2> "$TRAVAIL/run.err"; fi
else
    : "${CLE:?}" "${REPONSES:?}" "${MODELES:?}"
    SANS=""; [ "$LOTS" = oui ] || { SANS=--sans-lots; journal "contrôle causal SANS LOTS (déclaré ; règle de dépense)"; }
    module controle_ia.sparks_exp7_nul_v3.instance causal --sortie "$SORTIE" --depart "$DEPART" --cle "$CLE" \
        --reponses "$REPONSES"/*/*/reponse-v2.json --modeles "$MODELES" $SANS 2> "$TRAVAIL/run.err"
fi
code=$?
set -e
journal "fin du calcul, code $code"
D="diag/$RUN_ID"
mkdir -p "$D"
for f in "$SORTIE"/fabrication-v1.json "$SORTIE"/fabrication-complement-v2.json "$SORTIE"/causal-v2.json; do [ -f "$f" ] && cp "$f" "$D/"; done
[ -f "$SORTIE/couches-depart-v1.safetensors" ] && (cd "$SORTIE" && sha256sum couches-depart-v1.safetensors) > "$D/empreinte-couches-depart.txt"
if [ -d "$SORTIE/modeles" ]; then
    (cd "$SORTIE/modeles" && find . -name comportement.json -o -name resume.json -o -name log.jsonl -o -name split.json \
        | tar -czf "$OLDPWD/$D/modeles-legers.tar.gz" -T -)
    (cd "$SORTIE/modeles" && find . -name couches.safetensors -exec sha256sum {} +) > "$D/empreintes-couches.txt"
fi
cp "$JOURNAL" "$TRAVAIL/tests.txt" "$TRAVAIL/pip-freeze.txt" "$D/" 2>/dev/null || true
[ -f "$TRAVAIL/acces-modeles.txt" ] && cp "$TRAVAIL/acces-modeles.txt" "$D/"
grep -vE '^PROGRES ' "$TRAVAIL/run.err" | tail -200 > "$D/run-err-fin.txt" || true
module controle_ia.scellement sceller "$D"/* > /dev/null
git add -A runs "$D" && git commit -qm "SPARKS-EXP7-NUL v10 : $PHASE ($MODE), code $code" || true
for essai in 1 2 3; do git push -q origin "$BRANCHE" && break; sleep $((15 * essai)); done
DISTANT=$(git ls-remote origin "refs/heads/$BRANCHE" 2>/dev/null | cut -f1)
if [ -n "$DISTANT" ] && [ "$DISTANT" = "$(git rev-parse HEAD)" ]; then
    echo "$DISTANT" > "$TRAVAIL/POUSSEE-VERIFIEE"; journal "poussée vérifiée sur $BRANCHE ($DISTANT)"
else journal "POUSSÉE NON VÉRIFIÉE sur $BRANCHE : aucune destruction ne suivra"; fi
journal "modèles gardés dans $SORTIE/modeles ou sur le disque de la fabrication (destruction par la minuterie ou par identifiant, R10)"
exit $code
