#!/usr/bin/env bash
# Amorce de l'instance du run de nuit R4 (seconde dose de l'organisme « coût gonflé », GO-2026-11-01-13), lancement en
# mode « args ». Copie déclinée de `amorce_instance_p3.sh` sous un nom nouveau (R12) : (1) le script de P3 décliné en
# `p3_instance_r4_v1.sh` (seule différence : suite de tests ciblée), avec le préenregistrement de R4 (PREREG) et une branche de résultats propre (BRANCHE) : même
# lanceur, mêmes gardes, mêmes sorties que P3 ; (2) puis, sur le même clone et le même environnement,
# `r4_suite_instance_v1.sh` : rejeu des actions de R4 (activations au format de R1) et juge de 3 milliards (format de R2).
# Plafond de l'ensemble : 330 minutes ; partie P3 : 310 minutes, soit le délai externe du run (300) plus 10 minutes
# seulement pour l'installation et les tests (déclaré, CLR-17 : un run qui irait au bout de son délai serait coupé par
# l'amorce ; R4 attendu ≈ 2 h 30 au total), sous la surveillance de la session. Une
# seconde exécution refuse de repartir (R12) ; seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance : COMMIT (commit de scellement du préenregistrement de R4),
# GH_TOKEN, HF_TOKEN, DEPOT_URL ; BRANCHE (facultatif, défaut calcul/r4-dose-reel-v1).
# Pour l'essai local seulement : RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT, CONFIG, TACHES,
# TESTS_ATTENDUS, CONFIG_REJEU_R4, CONFIG_JUGE_R4.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
export PREREG="${PREREG:-prereg/R4-dose-cout-gonfle-v1.md}"
export BRANCHE="${BRANCHE:-calcul/r4-dose-${MODE:-reel}-v1}"
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : R4, commit $COMMIT, préenregistrement $PREREG, branche $BRANCHE"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e r4 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/r4"
debut=$(date +%s)
timeout --signal=TERM --kill-after=5m 310m env COMMIT="$COMMIT" TRAVAIL="$T" bash amorce-depot/scripts/p3_instance_r4_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : lanceur de P3 (R4) fini, code $code"
# bloc rétabli de amorce_instance_p3.sh (CLR-17) : au plafond (124, 137), résultats partiels et traces committés et poussés
if { [ "$code" -eq 124 ] || [ "$code" -eq 137 ]; } && [ -d "$T/controle-ia/.git" ]; then
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/r4-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T/run.err" "$T/run.json"; do [ -f "$f" ] && cp "$f" "$d/"; done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        for f in donnees/*/sondes-figees-legeres.npz donnees/*/sondes-figees-legeres.npz.sha256 donnees/*/scores-p3.npz \
                 donnees/*/scores-p3.npz.sha256 donnees/*/jetons-principales-p3.npz donnees/*/jetons-principales-p3.npz.sha256 \
                 donnees/*/textes-actions-p3.jsonl donnees/*/textes-actions-p3.jsonl.sha256 \
                 donnees/*/sondes-figees.npz.sha256; do [ -f "$f" ] && git add -f "$f"; done
        git add -A runs diag "$d" && git commit -qm "R4 : plafond de l'amorce atteint : résultats partiels et traces" || true
        git push -q origin "$BRANCHE" || echo "AMORCE : poussée impossible"
    )
fi
if [ "$code" -eq 0 ]; then
    reste=$(( 330 - ($(date +%s) - debut) / 60 ))
    if [ "$reste" -lt 10 ]; then
        echo "AMORCE : moins de 10 minutes sous le plafond : suite (rejeu, juge) non lancée"; code=3
    else
        timeout --signal=TERM --kill-after=2m "${reste}m" env TRAVAIL="$T" bash amorce-depot/scripts/r4_suite_instance_v1.sh
        code=$?
        echo "AMORCE $(date -u +%FT%TZ) : suite de R4 (rejeu, juge) finie, code $code"
    fi
fi
for f in "$T/journal.txt" "$T/tests.txt"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
[ -s "$T/run.err" ] && { echo "----- $T/run.err (hors progression)"; grep -vE '^PROGRES ' "$T/run.err" | tail -8; }
exit $code
