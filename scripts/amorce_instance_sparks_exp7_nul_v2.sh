#!/usr/bin/env bash
# Amorce de l'instance de SPARKS-EXP7-NUL pour l'addendum n° 1 (version neuve de `amorce_instance_sparks_exp7_nul_v1.sh`,
# R12). Avant toute création de dossier de travail et avant tout calcul, au commit cloné :
#   1. GO-2026-11-04-04 : ligne de base (calcul, 25 USD, Lazar) ET ligne d'extension à 40 USD (règle R-389), dans sa
#      validité, non révoqué (`sparks_exp7_nul_v2/go.py`) ;
#   2. code : la différence 55399606..COMMIT_CODE est la liste fermée ; le commit lancé descend de COMMIT_CODE sans
#      toucher au code ; l'addendum scellé cite COMMIT_CODE (`sparks_exp7_nul_v2/garde_code.py`) ;
#   3. durée bornée par 90 % de (40 USD − DEJA_USD − stockage projeté jusqu'à la fin du 18 novembre) au prix horaire de
#      la carte (`sparks_exp7_nul_v2/depense.py duree`), au plus 24 h ; moins de 60 minutes : aucun calcul.
# Clone partiel et clairsemé (seuls les dossiers utiles sont extraits). Seule la session arrête ou détruit l'instance,
# par son identifiant (R10).
# Variables passées par --env :
#   COMMIT, COMMIT_CODE, GH_TOKEN, HF_TOKEN, PRIX_HEURE_USD, PRIX_STOCKAGE_HEURE_USD, DEJA_USD (défaut 0), PHASE, BRANCHE
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, GO_DATE, VENV_EXISTANT.
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${COMMIT_CODE:?COMMIT_CODE absent}" "${GH_TOKEN:?GH_TOKEN absent}"
: "${PRIX_HEURE_USD:?PRIX_HEURE_USD absent}" "${PRIX_STOCKAGE_HEURE_USD:?PRIX_STOCKAGE_HEURE_USD absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
DEJA_USD="${DEJA_USD:-0}"
GO_ID=GO-2026-11-04-04
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT, code $COMMIT_CODE, $GO_ID"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e sparks ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
git -C amorce-depot sparse-checkout set --no-cone '/*' '!/*/' '/src/' '/scripts/' '/registres/go.md' '/prereg/SPARKS-EXP7-NUL-*' \
    || { echo "AMORCE : extraction clairsemée impossible"; exit 1; }
if ! git -c credential.helper="$AIDE" -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
P=src/controle_ia/sparks_exp7_nul_v2
if ! (cd amorce-depot && python3 -I -B -c "import sys; sys.path.insert(0, '$P'); import go; sys.exit(go.main(sys.argv[1:]))" registres/go.md ${GO_DATE:+"$GO_DATE"}); then
    echo "AMORCE : $GO_ID non conforme (base et extension à 40 USD) : aucun calcul"; exit 2
fi
if ! (cd amorce-depot && git config credential.helper "$AIDE" && python3 -I -B -c "import sys; sys.path.insert(0, '$P'); import garde_code; sys.exit(garde_code.main(sys.argv[1:]))" lancement . "$COMMIT_CODE" "$COMMIT"); then
    echo "AMORCE : code ou addendum non conformes : aucun calcul"; exit 2
fi
MINUTES=$(cd amorce-depot && python3 -I -B -c "import sys; sys.path.insert(0, '$P'); import depense; sys.exit(depense.main(sys.argv[1:]))" duree "$PRIX_HEURE_USD" "$PRIX_STOCKAGE_HEURE_USD" "$DEJA_USD") \
    || { echo "AMORCE : prix illisibles : aucun calcul"; exit 2; }
[ "$MINUTES" -ge 60 ] || { echo "AMORCE : plafond trop bas pour ce prix ($MINUTES min) : aucun calcul"; exit 2; }
echo "AMORCE : durée plafonnée à $MINUTES minutes (40 USD − $DEJA_USD − stockage projeté, à $PRIX_HEURE_USD USD/h, marge 10 %)"
T="$RACINE_AMORCE/sparks"
timeout --signal=TERM --kill-after=5m "${MINUTES}m" env COMMIT="$COMMIT" COMMIT_CODE="$COMMIT_CODE" TRAVAIL="$T" GO_ID="$GO_ID" \
    bash amorce-depot/scripts/sparks_exp7_nul_instance_v2.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt" "$T/run.err"; do
    [ -s "$f" ] && { echo "----- $f"; grep -vE '^PROGRES ' "$f" | tail -20; }
done
exit $code
