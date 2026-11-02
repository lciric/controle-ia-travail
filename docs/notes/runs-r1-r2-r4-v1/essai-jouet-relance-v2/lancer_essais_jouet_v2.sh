#!/usr/bin/env bash
# Essais jouets de l'amorce v2 au commit d'essai (tiré du commit du code 5e678b5b) ; hors réseau, processeur.
set -u
W=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad
E=$W/essai-relance-v2
COMMIT_ESSAI=$(git -C "$E/depot-source" rev-parse HEAD)
AMORCE="$E/depot-source/scripts/amorce_instance_r1_relance_v2.sh"
commun=(COMMIT="$COMMIT_ESSAI" GH_TOKEN=jouet HF_TOKEN=jouet DEPOT_URL="file://$E/depot.git"
        VENV_EXISTANT=/home/user/controle-ia-travail/.venv HF_HUB_OFFLINE=1)
jouer() {   # nom, puis variables propres
    local nom=$1; shift
    mkdir -p "$E/inst-$nom"
    env "${commun[@]}" RACINE_AMORCE="$E/inst-$nom" "$@" nice -n 10 bash "$AMORCE" > "$E/amorce-$nom.log" 2>&1
    echo "$nom : code $?" | tee -a "$E/codes.txt"
}
jouer sain MODE=jouet PREREG_ABSENT=1 CONFIG_REJEU=essai/rejeu.json TESTS_ATTENDUS=11 TESTS_CIBLES=tests/test_runs_nuit_v2.py BRANCHE=calcul/essai-relance-sain
jouer falsifiee MODE=jouet PREREG_ABSENT=1 CONFIG_REJEU=essai/rejeu-table-falsifiee.json TESTS_ATTENDUS=11 TESTS_CIBLES=tests/test_runs_nuit_v2.py BRANCHE=calcul/essai-relance-falsifiee
jouer etapes-refusees MODE=jouet PREREG_ABSENT=1 CONFIG_REJEU=essai/rejeu.json ETAPES="rejeu juge3b" BRANCHE=calcul/essai-relance-etapes
jouer reel-addendum-present-non-scelle MODE=reel BRANCHE=calcul/essai-relance-prereg
