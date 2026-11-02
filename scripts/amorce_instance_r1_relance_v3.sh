#!/usr/bin/env bash
# Amorce de l'instance de la relance de R1 sur la table de tokenisation version 3 (addendum
# `prereg/R1-addendum-relance-v3.md`, à sceller ; dépense sous le GO de calcul que cite l'addendum, la garde de calcul
# exige GO_ID au lancement), en mode « args ». Version 3, sous un nom nouveau (R12 ; `amorce_instance_r1_relance_v2.sh`
# n'est pas modifiée) : script `r1_relance_instance_v3.sh`, R1 seule, sous la surveillance de la session. Plafond de
# l'amorce : PLAFOND_AMORCE_MIN minutes (défaut 110, inchangé : mise en place ≈ 20 min, préchargement du modèle ≈ 5 min,
# tests ≈ 20 min dont le rejeu à graine et la relance v3, rejeu ≈ 15 min, poussées) ; l'addendum v3 le règle à la
# création de l'instance (garde très large contre une boucle folle, non un budget). Valeur hors des entiers de 1 à 9999 :
# arrêt avant le clonage (aucun repli silencieux, R5). Une seconde exécution refuse de repartir (dossiers présents,
# R12) : seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement de l'addendum de relance v3
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
#   DEPOT_URL https://github.com/lciric/controle-ia-travail.git (passé explicitement, CLAUDE.md)
#   BRANCHE   (facultatif) défaut calcul/r1-relance-<MODE>-v3 ; une branche qui existe déjà arrête avant tout calcul
#   PLAFOND_AMORCE_MIN (facultatif) plafond de l'amorce en minutes, entier de 1 à 9999 (défaut 110)
#   DELAI_REJEU_MIN    (facultatif) délai externe de l'étape du rejeu en minutes, transmis au script (défaut 60)
# Pour l'essai local seulement : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT, CONFIG_REJEU,
# TESTS_ATTENDUS, TESTS_CIBLES, TOKENISEUR_LLAMA31 (transmis au script).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
# défaut seulement si la variable est absente : une valeur vide est refusée (aucun repli silencieux)
PLAFOND_AMORCE_MIN="${PLAFOND_AMORCE_MIN-110}"
if ! [[ "$PLAFOND_AMORCE_MIN" =~ ^[1-9][0-9]{0,3}$ ]]; then
    echo "AMORCE : PLAFOND_AMORCE_MIN=« $PLAFOND_AMORCE_MIN » : entier de minutes de 1 à 9999 attendu : arrêt avant le clonage"
    exit 1
fi
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : relance de R1 (table v3), commit $COMMIT, plafond de l'amorce $PLAFOND_AMORCE_MIN min"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e r1rel3 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/r1rel3"
timeout --signal=TERM --kill-after=5m "${PLAFOND_AMORCE_MIN}m" env COMMIT="$COMMIT" TRAVAIL="$T" \
    bash amorce-depot/scripts/r1_relance_instance_v3.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T"/r1-rejeu.err; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$f" | tail -8; }
done
exit $code
