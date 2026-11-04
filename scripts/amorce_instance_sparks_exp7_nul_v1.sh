#!/usr/bin/env bash
# Amorce de l'instance de SPARKS-EXP7-NUL (texte scellé `prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md`, 4bacf20d…),
# sur le modèle de `amorce_instance_p3.sh`, sous un nom nouveau (R12). Avant toute création de dossier de travail et
# avant tout calcul, elle vérifie au commit cloné que `registres/go.md` porte GO-2026-11-04-04 de type « calcul »,
# plafond 25 USD, accordé par Lazar, dans sa validité et non révoqué ; puis elle borne la durée par le plafond.
# Une seconde exécution refuse de repartir (dossiers présents, R12) ; seule la session arrête l'instance, par son
# identifiant (R10).
# Variables passées par --env à la création de l'instance :
#   COMMIT          commit du dépôt de travail qui porte le code empreinté et le texte scellé
#   GH_TOKEN        jeton GitHub à grain fin, limité au dépôt de travail privé lciric/controle-ia-travail
#   HF_TOKEN        jeton Hugging Face en lecture (accès à google/gemma-3-270m-it voulu : décision D-2)
#   PRIX_HEURE_USD  prix horaire total de l'offre louée (dph_total), pour tenir le plafond
#   PHASE           fabrication (défaut) ou causal (après l'ouverture du coffre ; CLE, REPONSES, MODELES alors)
#   BRANCHE         (facultatif) défaut calcul/sparks-exp7-nul-v1 (fabrication) ou calcul/sparks-exp7-nul-causal-v1
# Pour l'essai local seulement : DEPOT_URL, RACINE_AMORCE, MODE=jouet, GO_DATE (date simulée du contrôle du GO).
set -uo pipefail
: "${COMMIT:?COMMIT absent}" "${GH_TOKEN:?GH_TOKEN absent}" "${PRIX_HEURE_USD:?PRIX_HEURE_USD absent}"
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"
RACINE_AMORCE="${RACINE_AMORCE:-/root}"
GO_ID=GO-2026-11-04-04
PLAFOND_USD=25
export HOME="${HOME:-/root}" DEPOT_URL
cd "$RACINE_AMORCE" || exit 1
echo "AMORCE $(date -u +%FT%TZ) : commit $COMMIT, $GO_ID"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
if [ -e amorce-depot ] || [ -e sparks ]; then
    echo "AMORCE : dossiers d'un essai précédent présents (R12) : relancer sur une instance neuve"; exit 1
fi
if ! git -c credential.helper="$AIDE" clone -q "$DEPOT_URL" amorce-depot; then
    echo "AMORCE : clonage impossible (jeton GitHub ?)"; exit 1
fi
if ! git -C amorce-depot checkout -q "$COMMIT"; then
    echo "AMORCE : commit $COMMIT introuvable"; exit 1
fi
# GO vérifié au commit cloné, avant toute création (module sans dépendance hors bibliothèque standard)
if ! (cd amorce-depot && python3 -I -B -c "import sys; sys.path.insert(0, 'src/controle_ia/sparks_exp7_nul_v1'); import go; sys.exit(go.main(sys.argv[1:]))" registres/go.md ${GO_DATE:+"$GO_DATE"}); then
    echo "AMORCE : $GO_ID non conforme : aucun calcul"; exit 2
fi
# plafond : durée maximale = 90 % du plafond / prix horaire, au plus 24 h (pire cas facturé du devis)
MINUTES=$(python3 -I -c "import sys; p=float(sys.argv[1]); assert p > 0; print(int(min(24*60, 0.9*$PLAFOND_USD/p*60)))" "$PRIX_HEURE_USD") \
    || { echo "AMORCE : PRIX_HEURE_USD illisible : aucun calcul"; exit 2; }
[ "$MINUTES" -ge 60 ] || { echo "AMORCE : plafond trop bas pour ce prix ($MINUTES min) : aucun calcul"; exit 2; }
echo "AMORCE : durée plafonnée à $MINUTES minutes ($PLAFOND_USD USD à $PRIX_HEURE_USD USD/h, marge 10 %)"
T="$RACINE_AMORCE/sparks"
timeout --signal=TERM --kill-after=5m "${MINUTES}m" env COMMIT="$COMMIT" TRAVAIL="$T" GO_ID="$GO_ID" \
    bash amorce-depot/scripts/sparks_exp7_nul_instance_v1.sh
code=$?
echo "AMORCE $(date -u +%FT%TZ) : fin, code $code"
for f in "$T/journal.txt" "$T/tests.txt" "$T/run.err"; do
    [ -s "$f" ] && { echo "----- $f"; grep -vE '^PROGRES ' "$f" | tail -20; }
done
exit $code
