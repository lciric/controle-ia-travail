#!/usr/bin/env bash
# Amorce de l'instance de la comparaison d'échelle 8B contre 70B, v3 (préenregistrement
# `prereg/test-echelle-conscience-eval-v4.md`, GO cité au lancement). Déclinée de `amorce_echelle_v2.sh` sous un nom
# nouveau (R12) par la lignée « session-depot » le 27 octobre 2026, après la contre-lecture n° 2 (CLY-03) : le
# plafond de durée calculé par le lanceur (DUREE_MAX_S, compté depuis la création) borne aussi le calcul sur
# l'instance elle-même, indépendamment de la surveillance locale : délai = DUREE_MAX_S − 600 s (démarrage du
# conteneur et poussée), au plus 6 600 s. Sans DUREE_MAX_S lisible : arrêt, aucun calcul. Clone superficiel de la
# branche d'outils au commit COMMIT ; une seconde exécution refuse de repartir (dossier présent, R12).
# Variables passées par --env à la création de l'instance :
#   COMMIT       commit de la branche d'outils `outils/echelle-conscience-eval-v3` à exécuter
#   BRANCHE      branche neuve des résultats (une branche qui existe déjà arrête avant tout calcul)
#   DUREE_MAX_S  plafond de durée du lanceur, en secondes (4 500 à 7 200)
#   GH_TOKEN     jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la
#                copie expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN     jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte : 8B et 70B vérifiés)
#   GO_ID        GO cité dans les messages de commit
#   DEPOT_URL    dépôt de travail (défaut ci-dessous) ; répétition locale : RACINE_AMORCE, BRANCHE_CODE, MODELE_LOCAL,
#                VENV_EXISTANT
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${BRANCHE:?BRANCHE absent}" "${GH_TOKEN:?GH_TOKEN absent}"
if ! [[ "${DUREE_MAX_S:-}" =~ ^[0-9]+$ ]] || [ "$DUREE_MAX_S" -lt 4500 ] || [ "$DUREE_MAX_S" -gt 7200 ]; then
    echo "AMORCE : DUREE_MAX_S absente ou hors de [4 500 ; 7 200] s : arrêt, aucun calcul"; exit 1
fi
DELAI_S=$((DUREE_MAX_S - 600))
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE_CODE="${BRANCHE_CODE:-outils/echelle-conscience-eval-v3}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}"
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT ; branche des résultats $BRANCHE ; délai $DELAI_S s"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e depot ] || [ -e travail-echelle-v3 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q --depth 1 --branch "$BRANCHE_CODE" "$DEPOT_URL" depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
git -C depot config credential.helper "$AIDE"
if [ "$(git -C depot rev-parse HEAD)" != "$COMMIT" ]; then
    echo "AMORCE : la branche $BRANCHE_CODE pointe sur $(git -C depot rev-parse HEAD), pas sur $COMMIT : arrêt"; exit 1
fi
timeout --signal=TERM --kill-after=2m "${DELAI_S}s" env COMMIT="$COMMIT" BRANCHE="$BRANCHE" TRAVAIL="$RACINE_AMORCE/travail-echelle-v3" \
    bash depot/echelle-v3/scripts/echelle_instance_v3.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
[ -s "$RACINE_AMORCE/travail-echelle-v3/journal.txt" ] && { echo "----- journal (fin)"; tail -15 "$RACINE_AMORCE/travail-echelle-v3/journal.txt"; }
exit $code
