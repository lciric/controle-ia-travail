#!/usr/bin/env bash
# Validation de T0.4 sur l'instance de calcul : mise en place, run A, run B (rejeu entre processus), poussée.
# Procédure : docs/procedures/validation-T0.4-modele-reel-v1.md. Rien ne se lance sans GO consigné.
#
#   COMMIT=<commit de scellement du préenregistrement> bash validation_t04_instance.sh
#
# Variables :
#   COMMIT        (obligatoire) commit à extraire ; le lanceur Python vérifie en plus le commit cité par le préenregistrement
#   MODE          reel (défaut) ou jouet (répétition sur processeur, sans modèle réel ni processeur graphique)
#   DEPOT_URL     défaut https://github.com/lciric/controle-ia.git
#   GH_TOKEN      jeton GitHub à grain fin (dépôt distant GitHub) ; lu par un assistant d'identification, jamais écrit
#   HF_TOKEN      jeton Hugging Face en lecture (mode reel) ; lu par huggingface_hub
#   BRANCHE       défaut calcul/t04-validation
#   TRAVAIL       défaut $HOME/t04
#   VENV_EXISTANT environnement Python déjà prêt à réutiliser (sinon : python3.11 -m venv + requirements-gpu.txt)
set -euo pipefail

: "${COMMIT:?COMMIT obligatoire (commit de scellement du préenregistrement)}"
MODE="${MODE:-reel}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia.git}"
BRANCHE="${BRANCHE:-calcul/t04-validation}"
TRAVAIL="${TRAVAIL:-$HOME/t04}"
PREREG="prereg/T0.4-validation-modele-reel-v1.md"
case "$MODE" in reel|jouet) ;; *) echo "MODE=$MODE : reel ou jouet" >&2; exit 2 ;; esac

mkdir -p "$TRAVAIL"
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
AIDE_GIT='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'

journal "début : MODE=$MODE COMMIT=$COMMIT BRANCHE=$BRANCHE"
if [ "$MODE" = reel ]; then
    : "${HF_TOKEN:?HF_TOKEN obligatoire en mode reel}"
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv | tee -a "$JOURNAL"
fi

DEPOT="$TRAVAIL/controle-ia"
if [ -e "$DEPOT" ]; then
    echo "$DEPOT existe déjà : R12, aucune réécriture ; choisir un autre TRAVAIL" >&2
    exit 2
fi
git -c credential.helper="$AIDE_GIT" clone -q "$DEPOT_URL" "$DEPOT"
cd "$DEPOT"
git config credential.helper "$AIDE_GIT"
git config user.name "instance de calcul (T0.4)"
git config user.email "instance-calcul@invalid"
git checkout -q "$COMMIT"
git checkout -q -b "$BRANCHE"

if [ -n "${VENV_EXISTANT:-}" ]; then
    # shellcheck disable=SC1091
    . "$VENV_EXISTANT/bin/activate"
else
    python3.11 -m venv .venv
    # shellcheck disable=SC1091
    . .venv/bin/activate
    pip install -q -r requirements-gpu.txt
fi
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'disponible', torch.cuda.is_available())" | tee -a "$JOURNAL"
if ! PYTHONPATH=src python -m pytest -q -p no:cacheprovider >"$TRAVAIL/tests.txt" 2>&1; then
    tail -5 "$TRAVAIL/tests.txt" | tee -a "$JOURNAL"
    journal "tests en échec : arrêt"
    exit 1
fi
journal "tests : $(tail -1 "$TRAVAIL/tests.txt")"

if [ "$MODE" = reel ]; then
    # révision citée par le préenregistrement (jamais la branche courante du dépôt du modèle)
    R=$(sed -n 's/.*Révision du modèle : `\([0-9a-f]\{40\}\)`.*/\1/p' "$PREREG" | head -1)
    [ -n "$R" ] || { journal "révision introuvable dans $PREREG : arrêt"; exit 1; }
    journal "révision du modèle (citée) : $R"
    ARGS=(--revision "$R" --prereg "$PREREG" --sortie-tests "$TRAVAIL/tests.txt")
    SUFFIXE=validation-reelle
else
    ARGS=(--repetition-jouet --sortie-tests "$TRAVAIL/tests.txt")
    SUFFIXE=repetition-jouet
fi
# délai externe par run (R10 : le signal vise le processus lancé, par son identifiant) ; TERM est converti en
# arrêt consigné (arret.json), puis KILL cinq minutes plus tard si le processus ne rend pas la main
DELAI=(timeout --signal=TERM --kill-after=5m "${DELAI_RUN:-3h}")

pousser() { git push -q origin "$BRANCHE"; }
consigner_arret() {
    git add -A runs diag
    if git commit -qm "T0.4 — validation : arrêt pendant $1" >/dev/null 2>&1; then
        journal "ARRÊT pendant $1 : résultats partiels committés (dont arret.json s'il existe)"
    else
        journal "ARRÊT pendant $1 : aucun résultat à committer"
    fi
    if pousser; then journal "branche $BRANCHE poussée"; else journal "poussée impossible : résultats restés sur l'instance"; fi
}
A="$(date -u +%Y%m%d-%H%M%S)-$SUFFIXE"
journal "run A : $A"
if ! PYTHONPATH=src "${DELAI[@]}" python -m controle_ia.harnais.validation_reelle "${ARGS[@]}" --run-id "$A" \
        >"$TRAVAIL/run-A.json" 2>>"$TRAVAIL/run-A.err"; then
    consigner_arret "run A"; exit 1
fi
git add "runs/$A" "diag/$A"
git commit -qm "T0.4 — validation ($MODE), run A ($A)"
journal "run A terminé : $A"

sleep 1      # deux identifiants distincts même si le run A a duré moins d'une seconde
B="$(date -u +%Y%m%d-%H%M%S)-$SUFFIXE"
journal "run B (rejeu de $A) : $B"
if ! PYTHONPATH=src "${DELAI[@]}" python -m controle_ia.harnais.validation_reelle "${ARGS[@]}" --rejeu-de "$A" --run-id "$B" \
        >"$TRAVAIL/run-B.json" 2>>"$TRAVAIL/run-B.err"; then
    consigner_arret "run B"; exit 1
fi
git add "runs/$B" "diag/$B"
git commit -qm "T0.4 — validation ($MODE), run B ($B), rejeu entre processus de $A"
journal "run B terminé : $B"
tee -a "$JOURNAL" <"$TRAVAIL/run-B.json"

pousser
journal "fin : A=$A B=$B poussés sur $BRANCHE ; arrêter l'instance par son identifiant (R10)"
