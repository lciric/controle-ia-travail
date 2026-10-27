#!/usr/bin/env bash
# Amorce de l'instance de calcul pour les notations complémentaires de T0.5 (lancement en mode « args », sans accès
# direct à la machine). Dérivée de `amorce_instance_t05.sh` sous un nom nouveau (R12 : l'amorce du pilote, citée par son
# préenregistrement, n'est pas modifiée) : aucune ETUDE, script `complement_t05_instance.sh` (un ou deux runs
# successifs), préenregistrements PREREG_1 et PREREG_2 (facultatif) transmis, plafond de 480 minutes. Une seconde
# exécution refuse de repartir (dossiers présents, R12) : seule la session de pilotage arrête l'instance, par son
# identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement des préenregistrements du complément
#   PREREG_1  préenregistrement du premier run ; PREREG_2 (facultatif) celui du second
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licences Llama 3.1 et Llama 3.2 acceptées sur le compte)
#   DEPOT_URL défaut https://github.com/lciric/controle-ia-travail.git
#   BRANCHE   (facultatif) branche de résultats ; défaut calcul/t05-complement-<MODE>-v1 ; une branche qui existe déjà
#             arrête avant tout calcul : un relancement passe ici une branche nouvelle (…-v2)
# Sortie : journal sur la sortie standard (lu par `vastai logs <identifiant>`, lignes de progression comprises), ligne
# de départ « AMORCE <date> : commit … » et ligne de fin « AMORCE <date> : fin, code N » ; résultats poussés sur la
# branche.
# Pour l'essai local seulement : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG_ABSENT, CONFIG_1, TACHES_1, CONFIG_2,
# TACHES_2, TESTS_ATTENDUS (transmis au script du complément).
#
# Plafond de l'ensemble : 480 minutes, sous la surveillance de la session. Calcul (compte large) : mise en place
# (clonage, environnement, installation de requirements-gpu.txt) 20 min ; tests 26 min (environ 16 min sur la carte pour
# 689 tests, plus 10 min pour les tests ajoutés depuis) ; délai externe global des runs 400 min, plus 5 min du KILL qui
# suit le TERM du dernier run ; poussées et traces 6 min (trois poussées, chacune jusqu'à trois tentatives) ; soit 457
# min, marge 23 min. Au plafond, TERM au script du complément (arrêt consigné, résultats partiels poussés), puis KILL
# cinq minutes plus tard ; l'amorce verse en plus ses propres traces.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
if [ "${PREREG_ABSENT:-0}" != 1 ]; then
    : "${PREREG_1:?PREREG_1 absent}"
fi
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
PLAFOND=480m
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e t05 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/t05"
timeout --signal=TERM --kill-after=5m "$PLAFOND" env COMMIT="$COMMIT" TRAVAIL="$T" PREREG_1="${PREREG_1:-}" \
    PREREG_2="${PREREG_2:-}" bash amorce-depot/scripts/complement_t05_instance.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
if { [ "$code" -eq 124 ] || [ "$code" -eq 137 ]; } && [ -d "$T/controle-ia/.git" ]; then
    # plafond atteint (124 : TERM ; 137 : KILL cinq minutes plus tard) : le script du complément a consigné l'arrêt s'il
    # en a eu le temps ; l'amorce verse en plus ses propres traces, au mieux
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/t05-complement-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T"/run-*.err "$T"/run-*.json; do [ -f "$f" ] && cp "$f" "$d/"; done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        git add -A runs diag "$d" && git commit -qm "T0.5 — complément : plafond de l'amorce atteint : résultats partiels et traces" || true
        git push -q origin "${BRANCHE:-calcul/t05-complement-${MODE:-reel}-v1}" || echo "AMORCE : poussée impossible"
    )
fi
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T"/run-*.err; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$f" | tail -15; }
done
exit $code
