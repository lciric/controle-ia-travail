#!/usr/bin/env bash
# Amorce de l'instance de calcul de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269), lancement
# en mode « args ». Déclinée de `scripts/amorce_instance_p3.sh` sous un nom neuf (R12) et versée sous
# docs/procedures/P4-instrument-v1/, hors de l'arbre gelé (un script ajouté sous scripts/ changerait l'arbre gelé, que le
# run exige égal à celui de P3, `7a54d43`). Script `docs/procedures/P4-instrument-v1/p4_instance_v1.sh` ; plafond de
# 150 minutes (mise en place, suite complète des tests, run, poussées ; texte, Plan d'analyse, point 7), au-dessus du
# délai externe du run (90 minutes) et sous la surveillance de la session (création + 9 600 s). Une seconde exécution
# refuse de repartir (dossiers présents, R12) : seule la session de pilotage arrête l'instance, par son identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de scellement S du préenregistrement de P4
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
#   BRANCHE   (facultatif) branche de résultats ; défaut calcul/p4-<MODE>-v1 ; une branche qui existe déjà arrête avant
#             tout calcul
# Sortie : journal sur la sortie standard (lu par `vastai logs <identifiant>`, lignes de progression comprises),
# résultats poussés sur la branche. Aucun texte d'action : le run n'en écrit pas, et le plafond ne pousse que les
# résultats, les trois tableaux de P4 et les traces.
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, VENV_EXISTANT, PREREG (transmis au script).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e p4 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/p4"
# plafond de l'ensemble (mise en place, tests, run, poussées) : 150 minutes, au-dessus du délai externe du run (90
# minutes) et sous la surveillance de la session (création + 9 600 s)
timeout --signal=TERM --kill-after=5m 150m env COMMIT="$COMMIT" TRAVAIL="$T" \
    bash amorce-depot/docs/procedures/P4-instrument-v1/p4_instance_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
if { [ "$code" -eq 124 ] || [ "$code" -eq 137 ]; } && [ -d "$T/controle-ia/.git" ]; then
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/p4-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T/run.err" "$T/run.json"; do [ -f "$f" ] && cp "$f" "$d/"; done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        for f in donnees/*-p4-"${MODE:-reel}"/validation-p4.npz donnees/*-p4-"${MODE:-reel}"/validation-p4.npz.sha256 \
                 donnees/*-p4-"${MODE:-reel}"/scores-p4.npz donnees/*-p4-"${MODE:-reel}"/scores-p4.npz.sha256 \
                 donnees/*-p4-"${MODE:-reel}"/jetons-principales-p4.npz donnees/*-p4-"${MODE:-reel}"/jetons-principales-p4.npz.sha256; do
            [ -f "$f" ] && git add -f "$f"
        done
        git add -A runs diag "$d" && git commit -qm "P4 : plafond de l'amorce atteint : résultats partiels et traces" || true
        git push -q origin "${BRANCHE:-calcul/p4-${MODE:-reel}-v1}" || echo "AMORCE : poussée impossible"
    )
fi
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
[ -s "$T/run.err" ] && { echo "----- $T/run.err (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$T/run.err" | tail -15 | cut -c1-300; }
exit $code
