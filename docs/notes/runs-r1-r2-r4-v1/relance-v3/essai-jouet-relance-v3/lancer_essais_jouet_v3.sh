#!/usr/bin/env bash
# Essais jouets de l'amorce et du script d'instance v3 (bornes de durée réglables), au commit d'essai tiré du commit
# cité par preparer_essai_v3.py ; hors réseau (dépôts nus locaux), processeur, jetons factices « jouet ».
set -u
W=/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad
E=$W/essai-relance-v3
COMMIT_ESSAI=$(git -C "$E/depot-source" rev-parse HEAD)
COMMIT_TEMOIN=$(git -C "$E/depot-temoin" rev-parse HEAD)
AMORCE="$E/depot-source/scripts/amorce_instance_r1_relance_v3.sh"
commun=(GH_TOKEN=jouet HF_TOKEN=jouet VENV_EXISTANT=/home/user/controle-ia-travail/.venv HF_HUB_OFFLINE=1
        TRANSFORMERS_OFFLINE=1 GIT_TERMINAL_PROMPT=0 MODE=jouet PREREG_ABSENT=1)
jouer() {   # nom, puis variables propres
    local nom=$1 t0 code; shift
    mkdir -p "$E/inst-$nom"
    t0=$(date +%s)
    env "${commun[@]}" RACINE_AMORCE="$E/inst-$nom" "$@" nice -n 5 bash "$AMORCE" > "$E/amorce-$nom.log" 2>&1
    code=$?
    echo "$nom : code $code ($(( $(date +%s) - t0 )) s)" | tee -a "$E/codes.txt"
}
S=(COMMIT="$COMMIT_ESSAI" DEPOT_URL="file://$E/depot.git")
jouer sain "${S[@]}" CONFIG_REJEU=essai/rejeu-v3.json TESTS_CIBLES=tests/test_bornes_relance_v3.py \
    TESTS_ATTENDUS=23 PLAFOND_AMORCE_MIN=720 DELAI_REJEU_MIN=600 BRANCHE=calcul/essai-relance-v3-sain
jouer table-falsifiee "${S[@]}" CONFIG_REJEU=essai/rejeu-v3-table-falsifiee.json \
    TESTS_CIBLES=tests/test_bornes_relance_v3.py TESTS_ATTENDUS=23 PLAFOND_AMORCE_MIN=720 DELAI_REJEU_MIN=600 \
    BRANCHE=calcul/essai-relance-v3-falsifiee
jouer plafond-1min "${S[@]}" CONFIG_REJEU=essai/rejeu-v3.json TESTS_CIBLES=tests/test_runs_nuit_v2.py \
    TESTS_ATTENDUS=11 PLAFOND_AMORCE_MIN=1 DELAI_REJEU_MIN=600 BRANCHE=calcul/essai-relance-v3-plafond
jouer delai-1min COMMIT="$COMMIT_TEMOIN" DEPOT_URL="file://$E/depot-temoin.git" CONFIG_REJEU=essai/rejeu-v3.json \
    TESTS_CIBLES=tests/test_bornes_relance_v3.py TESTS_ATTENDUS=23 PLAFOND_AMORCE_MIN=720 DELAI_REJEU_MIN=1 \
    BRANCHE=calcul/essai-relance-v3-delai
jouer plafond-invalide "${S[@]}" CONFIG_REJEU=essai/rejeu-v3.json TESTS_CIBLES=tests/test_bornes_relance_v3.py \
    PLAFOND_AMORCE_MIN=0 BRANCHE=calcul/essai-relance-v3-plafond-invalide
jouer delai-invalide "${S[@]}" CONFIG_REJEU=essai/rejeu-v3.json TESTS_CIBLES=tests/test_bornes_relance_v3.py \
    DELAI_REJEU_MIN=abc BRANCHE=calcul/essai-relance-v3-delai-invalide
# branches poussées sur les dépôts nus (aucun résultat n'est lu ici : noms et présence de fichiers seulement)
for d in depot depot-temoin; do
    echo "== $d.git"
    git -C "$E/$d.git" for-each-ref --format='%(refname:short)' refs/heads/ | while read -r b; do
        echo "-- $b : $(git -C "$E/$d.git" ls-tree -r --name-only "$b" -- donnees diag runs traces | grep -E 'r1-rejeu|traces/' \
            | sed -E 's#/[0-9]{8}-[0-9]{6}-#/<run>-#; s#traces/r1-relance-v3-[0-9-]+-[A-Za-z0-9]{4}/#traces/<t>/#' | sort | tr '\n' ' ')"
    done
done
