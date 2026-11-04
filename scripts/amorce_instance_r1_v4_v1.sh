#!/usr/bin/env bash
# Amorce de l'instance de la relance v4 de R1 (addendum `prereg/R1-addendum-relance-v4.md`, à sceller ; dépense sous
# le GO de calcul qu'il cite, GO_ID exigé au lancement par la garde de calcul), en mode « args ». Amorce neuve (R12 ;
# `amorce_instance_r1_relance_v3.sh` n'est pas modifiée) : script `r1_v4_instance_v1.sh`, session SESSION (temoin ou
# reparation). PLAFOND_AMORCE_MIN : garde très large contre une boucle folle (défaut 180 min ; 2 200 min en session 2, passé à la création), jamais un couperet de
# mesure ; hors des entiers de 1 à 9999 : arrêt avant le clonage (R5). Une seconde exécution refuse de repartir
# (dossiers présents, R12) : seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables (--env) : COMMIT, SESSION, TEMOIN_RUN (session reparation), GH_TOKEN, HF_TOKEN, DEPOT_URL, BRANCHE,
# PLAFOND_AMORCE_MIN, DELAI_ETAPE_MIN (transmis au script). Essai local : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT,
# PREREG, PREREG_ABSENT, CONFIG_REPARATION, CONFIG_REJEU, TESTS_ATTENDUS, TESTS_CIBLES, TOKENISEUR_LLAMA31.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${SESSION:?SESSION absente}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
PLAFOND_AMORCE_MIN="${PLAFOND_AMORCE_MIN-180}"
if ! [[ "$PLAFOND_AMORCE_MIN" =~ ^[1-9][0-9]{0,3}$ ]]; then
    echo "AMORCE : PLAFOND_AMORCE_MIN=« $PLAFOND_AMORCE_MIN » : entier de minutes de 1 à 9999 attendu : arrêt avant le clonage"
    exit 1
fi
case "$SESSION" in temoin|reparation) ;; *) echo "AMORCE : SESSION=$SESSION : temoin ou reparation : arrêt avant le clonage"; exit 1 ;; esac
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : relance v4 de R1, session $SESSION, commit $COMMIT, plafond de l'amorce $PLAFOND_AMORCE_MIN min"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e r1v4 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/r1v4"
timeout --signal=TERM --kill-after=5m "${PLAFOND_AMORCE_MIN}m" env COMMIT="$COMMIT" SESSION="$SESSION" TRAVAIL="$T" \
    bash amorce-depot/scripts/r1_v4_instance_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T"/*.err; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$f" | tail -8; }
done
exit $code
