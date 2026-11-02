#!/usr/bin/env bash
# Amorce de l'instance du rejeu à graine (relance de R1, addendum `prereg/R1-addendum-relance-v2.md` à sceller),
# lancement en mode « args ». Version 1, nom nouveau (R12) : script `r1_resolution_graine_instance_v1.sh`, plafond
# PLAFOND_MIN (défaut 120 minutes) supérieur à la somme des délais (VG-01) : mise en place, tokeniseur, tests et poids
# ≤ 30 min ; chaque étape ≤ duree_max_s + 10 min (délai externe du script, lu dans la configuration scellée ; le module
# tient ses budgets par épisode et par étape et écrit toujours son résultat avant) ; poussées 5 min. Le script vérifie
# 30 + 2 × (duree_max_s/60 + 10) + 5 ≤ PLAFOND_MIN avant l'installation (duree_max_s = 1 800 : 115 ≤ 120). Sous la
# surveillance de la session. Une seconde exécution refuse de repartir (dossiers présents, R12) : seule la session de
# pilotage arrête l'instance, par son identifiant (R10). Dépense : sous le GO que Lazar donnera pour ce passage (la
# garde de calcul de la session exige GO_ID au lancement).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement de l'addendum v2
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
#   DEPOT_URL https://github.com/lciric/controle-ia-travail.git (passé explicitement, CLAUDE.md)
#   BRANCHE   (facultatif) défaut calcul/r1-resolution-graine-v1 ; une branche qui existe déjà arrête avant tout calcul
# Pour l'essai local et la répétition jouet seulement : RACINE_AMORCE, PLAFOND_MIN, VENV_EXISTANT, PREREG,
# ARRET_AVANT_CALCUL, REPETITION_JOUET, REPETITION_ECHEC_COMMIT, TOKENISEUR_LLAMA31, TORCH_ATTENDU, CUDA_ATTENDU,
# CARTE_ATTENDUE (transmis au script par l'environnement).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}"
if [ "${ARRET_AVANT_CALCUL:-0}" != 1 ] && [ "${REPETITION_JOUET:-0}" != 1 ]; then : "${HF_TOKEN:?HF_TOKEN absent}"; fi
PLAFOND_MIN="${PLAFOND_MIN:-120}"
[[ "$PLAFOND_MIN" =~ ^[0-9]+$ ]] || { echo "AMORCE : PLAFOND_MIN non entier"; exit 1; }
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : rejeu à graine, commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e r1graine ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/r1graine"
timeout --signal=TERM --kill-after=3m "${PLAFOND_MIN}m" env COMMIT="$COMMIT" TRAVAIL="$T" PLAFOND_AMORCE_MIN="$PLAFOND_MIN" \
    bash amorce-depot/scripts/r1_resolution_graine_instance_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T"/validation.err "$T"/resolution.err; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$f" | tail -8; }
done
exit $code
