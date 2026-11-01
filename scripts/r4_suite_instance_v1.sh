#!/usr/bin/env bash
# Suite de R4 sur l'instance, après le lanceur de P3 (`p3_instance.sh`, run « …-p3-<MODE> » complet et poussé) : rejeu des
# actions du run (activations au format de R1, contrôle de fidélité fixé d'avance) puis juge de 3 milliards par action
# (format de R2) ; poussée après chaque étape sur la même branche. Configurations citées par le préenregistrement de R4
# (« Chemin de la configuration du rejeu de R4 », « Chemin de la configuration du juge de R4 ») ; chemins et empreintes
# des sorties du run lus dans son résumé scellé (`--run-source`).
#   TRAVAIL=<dossier de p3_instance.sh> bash r4_suite_instance_v1.sh
set -euo pipefail
: "${TRAVAIL:?TRAVAIL obligatoire}"
DEPOT="$TRAVAIL/controle-ia"
cd "$DEPOT"
PREREG="${PREREG:-prereg/R4-dose-cout-gonfle-v1.md}"
PREREG_ABSENT="${PREREG_ABSENT:-0}"
MODE="${MODE:-reel}"
BRANCHE=$(git rev-parse --abbrev-ref HEAD)
JOURNAL="$TRAVAIL/journal.txt"
journal() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$JOURNAL"; }
# shellcheck disable=SC1091
if [ -n "${VENV_EXISTANT:-}" ]; then . "$VENV_EXISTANT/bin/activate"; else . .venv/bin/activate; fi
lire_unique() {
    local n
    n=$(grep -c "$1 : \`" "$PREREG" || true)
    if [ "$n" != 1 ]; then echo ""; return 0; fi
    sed -n "s/.*$1 : \`\\([^\`]*\\)\`.*/\\1/p" "$PREREG"
}
if [ "$PREREG_ABSENT" = 1 ]; then
    [ "$MODE" = jouet ] || { journal "PREREG_ABSENT=1 n'est permis qu'en mode jouet (R1)"; exit 2; }
    : "${CONFIG_REJEU_R4:?}" "${CONFIG_JUGE_R4:?}"
    ARGS=()
else
    CONFIG_REJEU_R4=$(lire_unique "Chemin de la configuration du rejeu de R4")
    CONFIG_JUGE_R4=$(lire_unique "Chemin de la configuration du juge de R4")
    for f in "$CONFIG_REJEU_R4" "$CONFIG_JUGE_R4"; do
        [ -n "$f" ] && [ -f "$f.sha256" ] || { journal "suite de R4 : configuration citée absente ou non scellée : arrêt"; exit 2; }
    done
    PYTHONPATH=src python -m controle_ia.scellement verifier "$CONFIG_REJEU_R4" "$CONFIG_JUGE_R4" >/dev/null
    ARGS=(--prereg "$PREREG")
fi
SOURCE=$(ls -1d diag/*-p3-"$MODE" 2>/dev/null | sort | tail -1 | xargs -r basename)
[ -n "$SOURCE" ] && [ -f "diag/$SOURCE/resume.json" ] && [ ! -f "diag/$SOURCE/arret.json" ] || {
    journal "suite de R4 : aucun run complet du lanceur de P3 trouvé : arrêt"; exit 2; }
journal "suite de R4 : run source $SOURCE"
pousser() {
    local essai
    for essai in 1 2 3; do git push -q origin "$BRANCHE" 2>/dev/null && return 0; sleep $((15 * essai)); done
    return 1
}
for e in rejeu juge; do
    if [ "$e" = rejeu ]; then module=controle_ia.runs_nuit.rejeu_activations_v1; config="$CONFIG_REJEU_R4"
    else module=controle_ia.runs_nuit.juge_actions_v1; config="$CONFIG_JUGE_R4"; fi
    run="$(date -u +%Y%m%d-%H%M%S)-r4-$e-$MODE"
    journal "suite de R4 : étape $e, run $run"
    code=0
    PYTHONPATH=src timeout --signal=TERM --kill-after=2m 45m python -m "$module" --config "$config" --run-id "$run" \
        --run-source "$SOURCE" "${ARGS[@]}" >"$TRAVAIL/r4-$e.json" 2>"$TRAVAIL/r4-$e.err" || code=$?
    grep -E '^PROGRES ' "$TRAVAIL/r4-$e.err" | tee -a "$JOURNAL" >/dev/null || true
    git add -A "runs/$run" "diag/$run" 2>/dev/null || true
    for f in donnees/"$run"/*.npz donnees/"$run"/*.npz.sha256; do
        [ -f "$f" ] && [ "$(stat -c %s "$f")" -le 99000000 ] && git add -f "$f"
    done
    if [ "$code" -ne 0 ] || [ -f "diag/$run/arret.json" ]; then
        grep -v '^PROGRES ' "$TRAVAIL/r4-$e.err" | tail -n 5 | tee -a "$JOURNAL" || true
        git commit -qm "R4 : arrêt de l'étape $e ($run)" >/dev/null 2>&1 || true
        pousser || journal "poussée impossible"
        journal "suite de R4 : étape $e arrêtée (code $code) ; arrêter l'instance par son identifiant (R10)"
        exit 1
    fi
    git commit -qm "R4 ($MODE) : $e, run $run"
    pousser && journal "suite de R4 : $e poussé" || journal "poussée après $e impossible : résultats restés sur l'instance"
done
journal "suite de R4 : fin ; arrêter l'instance par son identifiant (R10)"
