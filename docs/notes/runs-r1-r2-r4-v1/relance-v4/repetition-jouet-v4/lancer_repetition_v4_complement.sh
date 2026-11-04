#!/usr/bin/env bash
# Complément de lancer_repetition_v4.sh : les deux derniers artefacts (sceau du témoin faux ; session 2 sans TEMOIN_RUN)
# étaient tombés sur « No space left on device » au clonage (disque plein, banc de mutations en parallèle) ; rejoués
# seuls, mêmes commits, dossiers d'amorce neufs.
set -u
E=$(cd "$1" && pwd)
SRC=$E/depot-source
AMORCE="$SRC/scripts/amorce_instance_r1_v4_v2.sh"
C2=$(git -C "$SRC" rev-parse main)
C4=$(git -C "$SRC" rev-parse essai-sceau)
RUN_T=$(git -C "$SRC" ls-tree --name-only main diag/ | sed 's#^diag/##' | grep -E -- '-r1-v4-temoin-jouet$' | head -n 1)
commun=(GH_TOKEN=jouet HF_TOKEN=jouet VENV_EXISTANT=/home/user/controle-ia-travail/.venv HF_HUB_OFFLINE=1
        TRANSFORMERS_OFFLINE=1 GIT_TERMINAL_PROMPT=0 MODE=jouet PREREG_ABSENT=1
        CONFIG_REPARATION=essai/reparation-v4-jouet.json CONFIG_REJEU=essai/rejeu-v6-jouet.json
        TESTS_CIBLES=tests/test_garde_depense_v4_v1.py TESTS_ATTENDUS=7 DEPOT_URL="file://$E/depot.git")
jouer() {
    local nom=$1 racine=$2 t0 code; shift 2
    mkdir -p "$racine"
    t0=$(date +%s)
    env "${commun[@]}" RACINE_AMORCE="$racine" "$@" timeout 1100 nice -n 10 bash "$AMORCE" > "$E/amorce-$nom.log" 2>&1
    code=$?
    echo "$nom : code $code ($(( $(date +%s) - t0 )) s)" | tee -a "$E/codes.txt"
}
echo "== complément (disque plein au premier passage) : $(date -u +%FT%TZ)" | tee -a "$E/codes.txt"
jouer sceau-temoin-faux-2 "$E/inst-a5b" COMMIT="$C4" SESSION=reparation TEMOIN_RUN="$RUN_T" PLAFOND_AMORCE_MIN=2200 \
    DELAI_ETAPE_MIN=2100 BRANCHE=calcul/a5b
jouer sans-temoin-run-2 "$E/inst-a6b" COMMIT="$C2" SESSION=reparation PLAFOND_AMORCE_MIN=2200 DELAI_ETAPE_MIN=2100 \
    BRANCHE=calcul/a6b
