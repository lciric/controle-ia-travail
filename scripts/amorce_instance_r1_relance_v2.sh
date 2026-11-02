#!/usr/bin/env bash
# Amorce de l'instance de la relance de R1 (addendum `prereg/R1-addendum-relance-v1.md`, GO-2026-11-01-13), lancement
# en mode « args ». Version 2, sous un nom nouveau (R12 ; `amorce_instance_r1_r2_v1.sh` n'est pas modifiée) : script
# `r1_relance_instance_v2.sh`, R1 seule, plafond de 100 minutes (mise en place ≈ 20 min, tests ≈ 15 min, rejeu ≈ 15 min,
# poussées), sous la surveillance de la session. Une seconde exécution refuse de repartir (dossiers présents, R12) :
# seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement de l'addendum de relance
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
#   DEPOT_URL https://github.com/lciric/controle-ia-travail.git (passé explicitement, CLAUDE.md)
#   BRANCHE   (facultatif) défaut calcul/r1-relance-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
# Pour l'essai local seulement : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT, CONFIG_REJEU,
# TESTS_ATTENDUS, TESTS_CIBLES (transmis au script).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : relance de R1, commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e r1rel ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/r1rel"
timeout --signal=TERM --kill-after=5m 100m env COMMIT="$COMMIT" TRAVAIL="$T" bash amorce-depot/scripts/r1_relance_instance_v2.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T"/r1-rejeu.err; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$f" | tail -8; }
done
exit $code
