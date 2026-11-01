#!/usr/bin/env bash
# Amorce de l'instance des runs de nuit R1 et R2 (GO-2026-11-01-13), lancement en mode « args ». Copie déclinée de
# `amorce_instance_p3.sh` sous un nom nouveau (R12 ; l'amorce de P3 n'est pas modifiée) : script `r1_r2_instance_v1.sh`,
# plafond de 150 minutes (mise en place ≈ 20 min, tests ≈ 15 min, rejeu ≈ 15 min, juges ≈ 20 min, poussées), sous la
# surveillance de la session. Une seconde exécution refuse de repartir (dossiers présents, R12) : seule la session de
# pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement du préenregistrement de R1-R2
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licences Llama 3.1 et 3.2 acceptées sur le compte)
#   DEPOT_URL https://github.com/lciric/controle-ia-travail.git (passé explicitement, CLAUDE.md)
#   BRANCHE   (facultatif) défaut calcul/r1-r2-<MODE>-v1 ; une branche qui existe déjà arrête avant tout calcul
# Pour l'essai local seulement : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT, CONFIG_REJEU,
# CONFIG_JUGE3B, CONFIG_JUGE8B, ETAPES, TESTS_ATTENDUS (transmis au script).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : R1-R2, commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e r1r2 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/r1r2"
timeout --signal=TERM --kill-after=5m 150m env COMMIT="$COMMIT" TRAVAIL="$T" bash amorce-depot/scripts/r1_r2_instance_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T"/r1-rejeu.err "$T"/r2-juge3b.err "$T"/r2-juge8b.err; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$f" | tail -8; }
done
exit $code
