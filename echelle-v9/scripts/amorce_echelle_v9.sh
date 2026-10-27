#!/usr/bin/env bash
# Amorce de l'instance de la comparaison d'échelle 8B contre 70B, v8 (préenregistrement
# `prereg/test-echelle-conscience-eval-v10.md`, GO cité au lancement). Déclinée de `amorce_echelle_v7.sh` sous un nom
# nouveau (R12) par la lignée « session-depot » le 27 octobre 2026, après la contre-lecture n° 7 (CLT-03) : le délai
# qui borne le calcul est **recalculé après le clonage**, et le contrôle des DELAI_MIN_S refait ; le calcul finit donc
# au plus tard à création + DUREE_MAX_S − 600 s + 2 min (la v7 comptait le délai avant le clonage, qui peut durer
# jusqu'à 630 s). Le contrôle d'avant le clonage reste, pour refuser tôt.
# Depuis la v7 (contre-lecture n° 6) : le clonage est borné à CLONAGE_S = 600 s (CLU-04 ; git n'a pas de délai sur une
# liaison qui stagne) ; au-delà, refus, avec la ligne de fin. CLONAGE_ESSAI_S, réservée à la répétition locale,
# remplace cette borne pour éprouver la garde.
# Depuis la v5 (contre-lecture n° 4, CLW-08) : tout refus précoce écrit aussi la ligne « AMORCE … : fin,
# code 1 », que la surveillance relit, consigne et rend (sortie 7).
# Depuis la v4 (contre-lecture n° 3, CLZ-04, CLZ-05) :
#   - le délai qui borne le calcul sur l'instance est compté depuis la **création** (CREATION_S, passée par le
#     lanceur) : délai = CREATION_S + DUREE_MAX_S − 600 s − maintenant, au plus DUREE_MAX_S − 600 s ;
#   - moins de DELAI_MIN_S restant (le run demande ≈ 1 h) : arrêt, aucun calcul ;
#   - DELAI_ESSAI_S, réservée à la répétition locale, remplace le délai pour éprouver la garde.
# Sans DUREE_MAX_S dans [4 500 ; 21 600] ou sans CREATION_S lisible : arrêt, aucun calcul. Clone superficiel de la
# branche d'outils au commit COMMIT ; une seconde exécution refuse de repartir (dossier présent, R12).
# Variables passées par --env à la création de l'instance :
#   COMMIT       commit de la branche d'outils `outils/echelle-conscience-eval-v9` à exécuter
#   BRANCHE      branche neuve des résultats (une branche qui existe déjà arrête avant tout calcul)
#   DUREE_MAX_S  plafond de durée du lanceur, en secondes (4 500 à 21 600), compté depuis la création
#   CREATION_S   heure de la création (secondes depuis 1970, UTC), prise par le lanceur juste avant `vastai create`
#   GH_TOKEN     jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la
#                copie expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN     jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte : 8B et 70B vérifiés)
#   GO_ID        GO cité dans les messages de commit
#   DEPOT_URL    dépôt de travail (défaut ci-dessous) ; répétition locale : RACINE_AMORCE, BRANCHE_CODE, MODELE_LOCAL,
#                VENV_EXISTANT, DELAI_ESSAI_S, CLONAGE_ESSAI_S
set -uo pipefail
refus() {  # refus précoce : motif, puis la ligne de fin que la surveillance relit (CLW-08)
    echo "AMORCE : $* : arrêt, aucun calcul"
    echo "AMORCE $(date -u +%FT%TZ) : fin, code 1"
    exit 1
}
DELAI_MIN_S=2700
CLONAGE_S=600
[ -n "${COMMIT:-}" ] || refus "COMMIT absent"
[ -n "${BRANCHE:-}" ] || refus "BRANCHE absente"
[ -n "${GH_TOKEN:-}" ] || refus "GH_TOKEN absent"
if ! [[ "${DUREE_MAX_S:-}" =~ ^[0-9]+$ ]] || [ "$DUREE_MAX_S" -lt 4500 ] || [ "$DUREE_MAX_S" -gt 21600 ]; then
    refus "DUREE_MAX_S absente ou hors de [4 500 ; 21 600] s"
fi
[[ "${CREATION_S:-}" =~ ^[0-9]{10}$ ]] || refus "CREATION_S absente ou illisible"
if [ -n "${DELAI_ESSAI_S:-}" ]; then
    [[ "$DELAI_ESSAI_S" =~ ^[0-9]+$ ]] || refus "DELAI_ESSAI_S illisible"
    echo "AMORCE : délai d'essai $DELAI_ESSAI_S s (répétition locale seulement)"
fi
delai() {  # $1 moment : délai restant avant création + DUREE_MAX_S − 600 s, au plus DUREE_MAX_S − 600 s (CLZ-04, CLT-03)
    DELAI_S=$((CREATION_S + DUREE_MAX_S - 600 - $(date -u +%s)))
    [ "$DELAI_S" -gt $((DUREE_MAX_S - 600)) ] && DELAI_S=$((DUREE_MAX_S - 600))
    if [ -n "${DELAI_ESSAI_S:-}" ]; then
        DELAI_S=$DELAI_ESSAI_S
    elif [ "$DELAI_S" -lt "$DELAI_MIN_S" ]; then
        refus "$DELAI_S s restants avant le plafond $1 (création $CREATION_S + $DUREE_MAX_S s − 600 s), moins de $DELAI_MIN_S s"
    fi
}
delai "avant le clonage"
if [ -n "${CLONAGE_ESSAI_S:-}" ]; then
    [[ "$CLONAGE_ESSAI_S" =~ ^[1-9][0-9]*$ ]] || refus "CLONAGE_ESSAI_S illisible"
    CLONAGE_S=$CLONAGE_ESSAI_S
    echo "AMORCE : borne d'essai du clonage $CLONAGE_S s (répétition locale seulement)"
fi
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE_CODE="${BRANCHE_CODE:-outils/echelle-conscience-eval-v9}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}"
cd "$RACINE_AMORCE" || refus "dossier $RACINE_AMORCE inaccessible"
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT ; branche des résultats $BRANCHE ; création $CREATION_S ; délai $DELAI_S s ; clonage borné à $CLONAGE_S s"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e depot ] || [ -e travail-echelle-v9 ]; then
    refus "dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"
fi
timeout --signal=TERM --kill-after=30s "${CLONAGE_S}s" \
    git -c credential.helper="$AIDE" clone -q --depth 1 --branch "$BRANCHE_CODE" "$DEPOT_URL" depot \
    || refus "clonage impossible ou plus long que $CLONAGE_S s (jeton GitHub ? liaison ? CLU-04)"
git -C depot config credential.helper "$AIDE"
TETE=$(git -C depot rev-parse HEAD)
[ "$TETE" = "$COMMIT" ] || refus "la branche $BRANCHE_CODE pointe sur $TETE, pas sur $COMMIT"
delai "après le clonage"                                   # le calcul part d'ici (CLT-03)
echo "AMORCE $(date -u +%FT%TZ) : délai recalculé après le clonage : $DELAI_S s"
timeout --signal=TERM --kill-after=2m "${DELAI_S}s" env COMMIT="$COMMIT" BRANCHE="$BRANCHE" TRAVAIL="$RACINE_AMORCE/travail-echelle-v9" \
    bash depot/echelle-v9/scripts/echelle_instance_v9.sh
code=$?
[ "$code" = 124 ] && echo "AMORCE $(date -u +%FT%TZ) : délai de $DELAI_S s atteint : calcul interrompu, rien de plus n'est poussé"
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
[ -s "$RACINE_AMORCE/travail-echelle-v9/journal.txt" ] && { echo "----- journal (fin)"; tail -15 "$RACINE_AMORCE/travail-echelle-v9/journal.txt"; }
exit $code
