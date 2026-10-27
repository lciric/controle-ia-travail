#!/usr/bin/env bash
# Amorce de l'instance de la comparaison d'échelle 8B contre 70B, v4 (préenregistrement
# `prereg/test-echelle-conscience-eval-v5.md`, GO cité au lancement). Déclinée de `amorce_echelle_v3.sh` sous un nom
# nouveau (R12) par la lignée « session-depot » le 27 octobre 2026, après la contre-lecture n° 3 (CLZ-04, CLZ-05) :
#   - le délai qui borne le calcul sur l'instance est compté depuis la **création** (CREATION_S, passée par le
#     lanceur), et non depuis le départ de l'amorce : délai = CREATION_S + DUREE_MAX_S − 600 s − maintenant, au plus
#     DUREE_MAX_S − 600 s ; le démarrage du conteneur ne l'allonge plus (CLZ-05) ;
#   - moins de DELAI_MIN_S restant (le run demande ≈ 1 h) : arrêt, aucun calcul ;
#   - DELAI_ESSAI_S, réservée à la répétition locale, remplace le délai pour éprouver la garde (CLZ-04).
# Sans DUREE_MAX_S dans [4 500 ; 7 200] ou sans CREATION_S lisible : arrêt, aucun calcul. Clone superficiel de la
# branche d'outils au commit COMMIT ; une seconde exécution refuse de repartir (dossier présent, R12).
# Variables passées par --env à la création de l'instance :
#   COMMIT       commit de la branche d'outils `outils/echelle-conscience-eval-v4` à exécuter
#   BRANCHE      branche neuve des résultats (une branche qui existe déjà arrête avant tout calcul)
#   DUREE_MAX_S  plafond de durée du lanceur, en secondes (4 500 à 7 200), compté depuis la création
#   CREATION_S   heure de la création (secondes depuis 1970, UTC), prise par le lanceur juste avant `vastai create`
#   GH_TOKEN     jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la
#                copie expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN     jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte : 8B et 70B vérifiés)
#   GO_ID        GO cité dans les messages de commit
#   DEPOT_URL    dépôt de travail (défaut ci-dessous) ; répétition locale : RACINE_AMORCE, BRANCHE_CODE, MODELE_LOCAL,
#                VENV_EXISTANT, DELAI_ESSAI_S
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${BRANCHE:?BRANCHE absent}" "${GH_TOKEN:?GH_TOKEN absent}"
DELAI_MIN_S=2700
if ! [[ "${DUREE_MAX_S:-}" =~ ^[0-9]+$ ]] || [ "$DUREE_MAX_S" -lt 4500 ] || [ "$DUREE_MAX_S" -gt 7200 ]; then
    echo "AMORCE : DUREE_MAX_S absente ou hors de [4 500 ; 7 200] s : arrêt, aucun calcul"; exit 1
fi
if ! [[ "${CREATION_S:-}" =~ ^[0-9]{10}$ ]]; then
    echo "AMORCE : CREATION_S absente ou illisible : arrêt, aucun calcul"; exit 1
fi
MAINTENANT=$(date -u +%s)
DELAI_S=$((CREATION_S + DUREE_MAX_S - 600 - MAINTENANT))
[ "$DELAI_S" -gt $((DUREE_MAX_S - 600)) ] && DELAI_S=$((DUREE_MAX_S - 600))
if [ -n "${DELAI_ESSAI_S:-}" ]; then
    [[ "$DELAI_ESSAI_S" =~ ^[0-9]+$ ]] || { echo "AMORCE : DELAI_ESSAI_S illisible : arrêt"; exit 1; }
    DELAI_S=$DELAI_ESSAI_S
    echo "AMORCE : délai d'essai $DELAI_S s (répétition locale seulement)"
elif [ "$DELAI_S" -lt "$DELAI_MIN_S" ]; then
    echo "AMORCE : $DELAI_S s restants avant le plafond (création $CREATION_S + $DUREE_MAX_S s − 600 s), moins de $DELAI_MIN_S s : arrêt, aucun calcul"; exit 1
fi
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE_CODE="${BRANCHE_CODE:-outils/echelle-conscience-eval-v4}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}"
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT ; branche des résultats $BRANCHE ; création $CREATION_S ; délai $DELAI_S s"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e depot ] || [ -e travail-echelle-v4 ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q --depth 1 --branch "$BRANCHE_CODE" "$DEPOT_URL" depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
git -C depot config credential.helper "$AIDE"
if [ "$(git -C depot rev-parse HEAD)" != "$COMMIT" ]; then
    echo "AMORCE : la branche $BRANCHE_CODE pointe sur $(git -C depot rev-parse HEAD), pas sur $COMMIT : arrêt"; exit 1
fi
timeout --signal=TERM --kill-after=2m "${DELAI_S}s" env COMMIT="$COMMIT" BRANCHE="$BRANCHE" TRAVAIL="$RACINE_AMORCE/travail-echelle-v4" \
    bash depot/echelle-v4/scripts/echelle_instance_v4.sh
code=$?
[ "$code" = 124 ] && echo "AMORCE $(date -u +%FT%TZ) : délai de $DELAI_S s atteint : calcul interrompu, rien de plus n'est poussé"
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
[ -s "$RACINE_AMORCE/travail-echelle-v4/journal.txt" ] && { echo "----- journal (fin)"; tail -15 "$RACINE_AMORCE/travail-echelle-v4/journal.txt"; }
exit $code
