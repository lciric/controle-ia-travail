#!/usr/bin/env bash
# Amorce de l'instance de l'extraction des traits de l'étape 1 (GO-2026-10-24-05, R-355), lancement en mode « args ».
# Déclinée de `scripts/amorce_instance_p3.sh` (main) sous un nom nouveau (R12) par la lignée « session-depot » le
# 24 octobre 2026 : clone superficiel de la branche d'outils au commit COMMIT, plafond de 100 minutes sur l'ensemble
# (installation, téléchargement, deux extractions, poussée), sous la surveillance de la session, qui arrête l'instance
# par son identifiant (R10). Une seconde exécution refuse de repartir (dossier présent, R12).
# Variables passées par --env à la création de l'instance :
#   COMMIT    commit de la branche d'outils `outils/traits-etape1-v1` à exécuter
#   BRANCHE   branche neuve des résultats (une branche qui existe déjà arrête avant tout calcul)
#   GH_TOKEN  jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail (jamais la copie
#             expurgée publique lciric/controle-ia ; N-016)
#   HF_TOKEN  jeton Hugging Face en lecture (licence Llama 3.1 acceptée sur le compte)
#   DEPOT_URL dépôt de travail (défaut ci-dessous) ; répétition locale : RACINE_AMORCE, BRANCHE_CODE, MODELE_LOCAL, VENV_EXISTANT
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${BRANCHE:?BRANCHE absent}" "${GH_TOKEN:?GH_TOKEN absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
BRANCHE_CODE="${BRANCHE_CODE:-outils/traits-etape1-v1}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
export HOME="${HOME:-/root}"
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT ; branche des résultats $BRANCHE"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e depot ] || [ -e traits ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q --depth 1 --branch "$BRANCHE_CODE" "$DEPOT_URL" depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
git -C depot config credential.helper "$AIDE"
if [ "$(git -C depot rev-parse HEAD)" != "$COMMIT" ]; then
    echo "AMORCE : la branche $BRANCHE_CODE pointe sur $(git -C depot rev-parse HEAD), pas sur $COMMIT : arrêt"; exit 1
fi
timeout --signal=TERM --kill-after=2m 100m env COMMIT="$COMMIT" BRANCHE="$BRANCHE" TRAVAIL="$RACINE_AMORCE/traits" \
    bash depot/essaim-m3-refonte-v1/scripts/traits_etape1_instance_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
[ -s "$RACINE_AMORCE/traits/journal.txt" ] && { echo "----- journal (fin)"; tail -15 "$RACINE_AMORCE/traits/journal.txt"; }
exit $code
