#!/usr/bin/env bash
# Répétition jouet finale de bout en bout du script d'instance (dépôt nu local, sans réseau ni carte), après les
# corrections VI. Répertoire courant NEUTRE (finale/neutre, sans donnees/) : le préparateur doit lire ses pièces depuis
# la racine du dépôt de répétition (VI-16). Usage :
#   repetition.sh NOM TESTS_ATTENDUS [options du préparateur] -- [variables d'environnement du lancement]
set -uo pipefail
B=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/finale/rep
SRC=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-addendum
NEUTRE=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/finale/neutre
PY=/home/user/controle-ia-travail/.venv/bin/python
TOK=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/c6/tok
NOM="$1"; shift; ATT="$1"; shift
PREP=(); while [ $# -gt 0 ] && [ "$1" != "--" ]; do PREP+=("$1"); shift; done; [ $# -gt 0 ] && shift
mkdir -p "$B" "$NEUTRE"
D="$B/$NOM"
cd "$NEUTRE" || exit 1
[ ! -e "$NEUTRE/donnees" ] || { echo "répertoire courant non neutre"; exit 1; }
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 "$PY" -B "$SRC/scripts/preparer_repetition_r1_resolution_graine_v1.py" \
    --source "$SRC" --dossier "$D" --tests-attendus "$ATT" "${PREP[@]}" >"$B/$NOM-preparation.txt" 2>&1 \
    || { echo "préparation en échec"; tail -5 "$B/$NOM-preparation.txt"; exit 1; }
grep -E '^(COMMIT|DEPOT_URL|PREREG|EPISODES)' "$B/$NOM-preparation.txt"
eval "$(grep -E '^(COMMIT|DEPOT_URL|PREREG)=' "$B/$NOM-preparation.txt" | sed 's/^/export /')"
mkdir -p "$D/racine"
cp "$SRC/scripts/amorce_instance_r1_resolution_graine_v1.sh" "$D/amorce.sh"
env -i PATH="$(dirname "$PY"):/usr/local/bin:/usr/bin:/bin" HOME="$D/racine" COMMIT="$COMMIT" DEPOT_URL="$DEPOT_URL" \
    PREREG="$PREREG" GH_TOKEN=jeton-factice RACINE_AMORCE="$D/racine" VENV_EXISTANT=/home/user/controle-ia-travail/.venv \
    REPETITION_JOUET=1 TOKENISEUR_LLAMA31="$TOK" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 "$@" \
    bash "$D/amorce.sh" >"$B/$NOM-amorce.txt" 2>&1
code=$?
echo "code de l'amorce : $code"
exit $code
