#!/usr/bin/env bash
# Version 3 (brouillon 3 ; R12 : la v2 n'est pas modifiée) : GO vérifié par `controle_ia.pilote_exposant_p_v3.go`
# (règle d'extension R-389 de la garde de `main` ; contre-lecture R2 du brouillon 2, I3) ; lance le script d'instance v3.
# Amorce de l'instance de calcul du pilote de l'exposant p (brouillon 2 ; contre-lecture R2, I7, couples S01 et P20).
# Déclinée de `amorce_instance_p3.sh` sous un nom nouveau (R12). Deux étapes :
#
# 1. AMORCE_ETAPE=verifier — sur la machine de la session, AVANT toute création d'instance : vérifie le GO dans le
#    registre (`GO_ID`, type « calcul », accordé par Lazar, date du jour dans sa période, non révoqué, plafond en USD au
#    moins égal au pire cas du devis, périmètre qui nomme l'étude). Rien n'est créé ni lancé ; code 0 si le GO vaut,
#    1 sinon. La session crée ensuite l'instance par une commande qui cite `GO_ID=…` (garde de calcul).
#      AMORCE_ETAPE=verifier GO_ID=GO-2026-11-04-03 REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md \
#          bash scripts/amorce_instance_pilote_exposant_p_v3.sh
# 2. AMORCE_ETAPE=instance (défaut) — commande de démarrage de l'instance : clone, extrait COMMIT, revérifie le même GO
#    sur le registre de la branche `main` du dépôt (REF_GO, défaut origin/main : les registres vivants y sont depuis
#    R-1450) avant toute installation, puis lance `pilote_exposant_p_instance_v3.sh` sous un plafond d'ensemble de
#    630 minutes (au-dessus du délai externe du run, 600 minutes ; devis v2). Plafond atteint : résultats partiels et
#    traces committés et poussés sur la branche. Une seconde exécution refuse de repartir (dossiers présents, R12).
#    Seule la session arrête l'instance, par son identifiant (R10).
# Variables (étape instance, passées par --env) :
#   COMMIT    commit de scellement du préenregistrement du pilote
#   GO_ID     identifiant du GO de calcul (GO-AAAA-MM-JJ-NN)
#   GH_TOKEN  jeton GitHub à grain fin, dépôt de travail privé lciric/controle-ia-travail seulement (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée pour les deux modèles)
#   BRANCHE   (facultatif) branche de résultats ; défaut calcul/pilote-exposant-p-<MODE>-v3
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, REF_GO, MODE=jouet, VENV_EXISTANT, PREREG, PREREG_ABSENT,
# CONFIG, STIMULI, TESTS_ATTENDUS (transmis au script), MONTANT_PIRE_CAS_USD, DATE_GO.
set -uo pipefail
MONTANT_PIRE_CAS_USD="${MONTANT_PIRE_CAS_USD:-17}"     # pire cas du devis v2, arrondi au dollar supérieur
PLAFOND_MIN="${PLAFOND_MIN:-630}"
: "${GO_ID:?GO_ID absent}"

verifier_go() {   # $1 : racine d'un dépôt (pour src/) ; $2 : registre
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$1/src" python3 -B -m controle_ia.pilote_exposant_p_v3.go --registre "$2" \
        --go-id "$GO_ID" --montant "$MONTANT_PIRE_CAS_USD" ${DATE_GO:+--date "$DATE_GO"}
}

if [ "${AMORCE_ETAPE:-instance}" = verifier ]; then
    : "${REGISTRE_GO:?REGISTRE_GO absent (registres/go.md de la branche main)}"
    ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    if verifier_go "$ICI" "$REGISTRE_GO"; then
        echo "AMORCE : $GO_ID vérifié ; la création de l'instance doit citer GO_ID=$GO_ID (garde de calcul) ; rien n'a été créé"
        exit 0
    fi
    echo "AMORCE : $GO_ID ne vaut pas pour ce lancement : aucune instance ne doit être créée"
    exit 1
fi
[ "${AMORCE_ETAPE:-instance}" = instance ] || { echo "AMORCE_ETAPE=${AMORCE_ETAPE} : verifier ou instance"; exit 2; }

: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
REF_GO="${REF_GO:-origin/main}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT, $GO_ID"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e pilote-exposant-p ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
if ! git -C amorce-depot show "$REF_GO:registres/go.md" > go-verifie.md 2>/dev/null; then
    echo "AMORCE : registre des GO introuvable sur $REF_GO : arrêt avant toute installation"; exit 1
fi
if ! verifier_go amorce-depot go-verifie.md; then
    echo "AMORCE : $GO_ID ne vaut pas sur le registre de $REF_GO : arrêt avant toute installation"; exit 1
fi
T="$RACINE_AMORCE/pilote-exposant-p"
BR="${BRANCHE:-calcul/pilote-exposant-p-${MODE:-reel}-v3}"
# plafond de l'ensemble (mise en place, essais, run, poussées) : au-dessus du délai externe du run
timeout --signal=TERM --kill-after=5m "${PLAFOND_MIN}m" env COMMIT="$COMMIT" TRAVAIL="$T" BRANCHE="$BR" \
    bash amorce-depot/scripts/pilote_exposant_p_instance_v3.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
if { [ "$code" -eq 124 ] || [ "$code" -eq 137 ]; } && [ -d "$T/controle-ia/.git" ]; then
    (
        cd "$T/controle-ia" && mkdir -p traces && d=$(mktemp -d "traces/pilote-exposant-p-plafond-$(date -u +%Y%m%d-%H%M%S)-XXXX") &&
        for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err" "$T/run.err" "$T/run.json" "$T/acces-hf.txt"; do
            [ -f "$f" ] && cp "$f" "$d/"
        done
        (cd "$d" && sha256sum -- * > empreintes.sha256) || true
        git add -A runs diag "$d" && git commit -qm "Pilote exposant p : plafond de l'amorce atteint : résultats partiels et traces" || true
        git push -q origin "$BR" || echo "AMORCE : poussée impossible"
    )
fi
for f in "$T/journal.txt" "$T/tests.txt" "$T/tests.err"; do
    [ -s "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
[ -s "$T/run.err" ] && { echo "----- $T/run.err (dernières lignes, hors progression)"; grep -vE '^PROGRES ' "$T/run.err" | tail -15; }
exit $code
