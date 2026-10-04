#!/usr/bin/env bash
# Amorce de l'instance de calcul pour la validation de T0.4 (lancement en mode « args », sans accès direct à la machine).
# La commande de lancement l'embarque encodée en base64 ; le conteneur l'exécute au démarrage, puis s'arrête.
# Variables passées par --env à la création de l'instance (ou au niveau du compte de location) :
#   COMMIT    commit de scellement du préenregistrement
#   GH_TOKEN  jeton GitHub à grain fin, limité à lciric/controle-ia (contenu en lecture et écriture)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
# Sortie : journal sur la sortie standard (lu par `vastai logs <identifiant>`), résultats poussés sur calcul/t04-validation.
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, VENV_EXISTANT (transmis au script de validation).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${HF_TOKEN:?HF_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
T="$RACINE_AMORCE/t04"
timeout 7h env COMMIT="$COMMIT" TRAVAIL="$T" bash amorce-depot/scripts/validation_t04_instance.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt"; do
    [ -f "$f" ] && { echo "----- $f"; tail -20 "$f"; }
done
for f in "$T/run-A.err" "$T/run-B.err"; do
    [ -s "$f" ] && { echo "----- $f (dernières lignes)"; tail -15 "$f"; }
done
exit $code
