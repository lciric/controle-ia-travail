#!/usr/bin/env bash
# Pré-vol de la course d'idéation — pilier attaque, v1
# Zéro dépense : sonde simulée, mesure des consignes, moteur simulé.
#
# La course d'idéation (lanceur v2, noyau v42+) se joue en deux temps :
#   (a) Course : proposeurs (opus, fable, argon) + juges Claude (opus-juge, fable-juge)
#   (b) Bras rapporté différé : juge externe (argon-juge), après attestation de lecture humaine
# Le pré-vol vérifie (a) en moteur simulé. Le bras (b) n'est vérifiable qu'après (a).
#
# Prérequis non inclus dans le pré-vol :
#   - Témoins plantés (CL31-03) : écrits par un tiers, pas par cette session.
#     Format : {"temoins": [{"fiche": {...}, "attendu": "ineligible|eligible",
#               "note_max": {critere: n}}]}
#     Emplacement : organisme-v1/temoins-pilier-attaque-v1.json
#   - La course réelle utilise --moteur claude-sdk (dépense, GO requis).
#
# Usage : bash pre-vol-course-ideation-v1.sh [--reel]
#   Sans argument : sonde simulée + mesure consignes + moteur simulé
#   --reel : sonde réelle (≈ 0,003 USD) ; la course n'est PAS lancée

set -euo pipefail

DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
DEPOT_ORGANISME="${DEPOT_ORGANISME:-/home/user/ideation-organism-lecture}"
SORTIE_PRE_VOL="${DEPOT_TRAVAIL}/docs/notes/ideation-pilier-attaque-v1/organisme-v1/pre-vol"

QUESTION="${DEPOT_TRAVAIL}/docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md"
SYNTHESE="${DEPOT_TRAVAIL}/docs/notes/ideation-pilier-attaque-v1/collisionneur-v1/tour/run-pilier-attaque-e3-v1/synthese-anteriorite-pilier-attaque-v1.md"
QUESTION_SHA256="29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4"
SYNTHESE_SHA256="48adeac041d21c375473f2af1ed85ed88f7e5c97b5f88ba21021cc0c99e49997"

LANCEUR="${DEPOT_ORGANISME}/orchestrator/demonstrations/ideation_v8.py"

echo "=== Pré-vol course d'idéation, pilier attaque, v1 ==="
echo "Date : $(date -u '+%Y-%m-%d %H:%M:%S UTC')"

# --- Étape 1 : vérification des empreintes ---
echo ""
echo "--- Étape 1 : vérification des empreintes ---"

sha_question=$(sha256sum "$QUESTION" | cut -d' ' -f1)
if [ "$sha_question" != "$QUESTION_SHA256" ]; then
    echo "ERREUR : empreinte de la question ne correspond pas"
    echo "  attendue : $QUESTION_SHA256"
    echo "  calculée : $sha_question"
    exit 2
fi
echo "Question : OK ($QUESTION_SHA256)"

sha_synthese=$(sha256sum "$SYNTHESE" | cut -d' ' -f1)
if [ "$sha_synthese" != "$SYNTHESE_SHA256" ]; then
    echo "ERREUR : empreinte de la synthèse ne correspond pas"
    echo "  attendue : $SYNTHESE_SHA256"
    echo "  calculée : $sha_synthese"
    exit 2
fi
echo "Synthèse : OK ($SYNTHESE_SHA256)"

# --- Étape 2 : sonde de la garde de refus ---
echo ""
echo "--- Étape 2 : sonde de la garde de refus (R-514) ---"

SONDE_SORTIE="${SORTIE_PRE_VOL}/sonde-garde-refus-v1.json"
mkdir -p "$(dirname "$SONDE_SORTIE")"

if [ "${1:-}" = "--reel" ]; then
    echo "Mode RÉEL : sonde sur Fable 5.1, Opus 5.5, Argon (≈ 0,003 USD)"
    echo "NON IMPLÉMENTÉ dans ce pré-vol : la sonde réelle est lancée par le lanceur."
    echo "Utiliser : PYTHONPATH=${DEPOT_TRAVAIL}/src python -I -m controle_ia.garde_refus_question_v1 \\"
    echo "  --question $QUESTION --modeles claude-fable-5-1,claude-opus-5-5,gemini-4-argon \\"
    echo "  --sortie $SONDE_SORTIE"
    exit 2
else
    echo "Mode SIMULÉ : tous les modèles acceptent"
    PYTHONPATH="${SRC_CONTROLE_IA:-${DEPOT_TRAVAIL}/src}" python -I -m controle_ia.garde_refus_question_v1 \
        --question "$QUESTION" \
        --modeles claude-fable-5-1,claude-opus-5-5,gemini-4-argon \
        --simuler \
        --sortie "$SONDE_SORTIE"
fi

echo "Sonde écrite : $SONDE_SORTIE"

# --- Étape 3 : construction de la liste blanche ---
echo ""
echo "--- Étape 3 : construction de la liste blanche ---"

LISTE_BLANCHE="${SORTIE_PRE_VOL}/liste-blanche-v1.json"

# La liste inclut question + synthèse ; les témoins seront ajoutés quand ils existeront.
python3 -I -c "
import json, hashlib, sys

fichiers = ['$QUESTION', '$SYNTHESE']
lb = {}
for f in fichiers:
    with open(f, 'rb') as fh:
        lb[f] = hashlib.sha256(fh.read()).hexdigest()
with open('$LISTE_BLANCHE', 'w') as fh:
    json.dump(lb, fh, indent=2, ensure_ascii=False)
    fh.write('\n')
print(f'Liste blanche : {len(lb)} fichiers', file=sys.stderr)
"

echo "Liste blanche écrite : $LISTE_BLANCHE"

# --- Étape 4 : --mesurer-consignes (sans appel, sans fichier) ---
# Note : le lanceur v2 n'a pas de --verifier-seulement ; --mesurer-consignes
# mesure les tailles des consignes et les gardes sans aucun appel ni écriture.
echo ""
echo "--- Étape 4 : mesure des consignes (--mesurer-consignes) ---"

cd "$DEPOT_ORGANISME/orchestrator"

python -I -B "$LANCEUR" \
    --mesurer-consignes \
    --question "$QUESTION" \
    --piece "$SYNTHESE" \
    --piece-juge "$SYNTHESE" \
    --liste-blanche "$LISTE_BLANCHE" \
    --proposeur opus=claude-opus-5-5 \
    --proposeur fable=claude-fable-5-1 \
    --proposeur-externe argon=gemini-4-argon \
    --juge opus-juge=claude-opus-5-5 \
    --juge fable-juge=claude-fable-5-1 \
    --seconde-passe \
    --nombre 8 \
    --budget proposeur=2.5 \
    --budget juge=1.0 \
    --budget-total-usd 15.0 \
    --budget-externe-usd 5.0 \
    2>&1 | tee "${SORTIE_PRE_VOL}/mesurer-consignes-stdout.txt"

echo "Mesure des consignes terminée."

# --- Étape 5 : --moteur simule (course sans le bras) ---
# Note : la course de base (lanceur v2) exige --temoins (CL31-03 : fichier
# écrit par un tiers). Pour le pré-vol, un fichier de témoins de
# substitution est attendu dans TEMOINS_PRE_VOL (voir composition).
# Sans témoins, cette étape est sautée.
echo ""
echo "--- Étape 5 : passe simulée (--moteur simule, course sans le bras) ---"

SORTIE_SIMULE="${SORTIE_PRE_VOL}/sortie-moteur-simule"
TEMOINS_PRE_VOL="${SORTIE_PRE_VOL}/temoins-pre-vol-v1.json"

if [ ! -f "$TEMOINS_PRE_VOL" ]; then
    echo "SAUTÉ : témoins absents ($TEMOINS_PRE_VOL)."
    echo "  Les témoins doivent être écrits par un tiers (CL31-03)."
    echo "  Pour le pré-vol, créer un fichier de témoins de substitution"
    echo "  et le placer dans la liste blanche."
else
    echo "Témoins de pré-vol trouvés : $TEMOINS_PRE_VOL"
    python -I -B "$LANCEUR" \
        "${SORTIE_SIMULE}" \
        --question "$QUESTION" \
        --piece "$SYNTHESE" \
        --piece-juge "$SYNTHESE" \
        --liste-blanche "$LISTE_BLANCHE" \
        --temoins "$TEMOINS_PRE_VOL" \
        --proposeur opus=claude-opus-5-5 \
        --proposeur fable=claude-fable-5-1 \
        --proposeur-externe argon=gemini-4-argon \
        --juge opus-juge=claude-opus-5-5 \
        --juge fable-juge=claude-fable-5-1 \
        --seconde-passe \
        --nombre 8 \
        --budget proposeur=2.5 \
        --budget juge=1.0 \
        --budget-total-usd 15.0 \
        --budget-externe-usd 5.0 \
        --moteur simule \
        2>&1 | tee "${SORTIE_PRE_VOL}/moteur-simule-stdout.txt"
    echo "Passe simulée terminée."
fi

echo ""
echo "=== Pré-vol terminé ==="
echo "Sorties : $SORTIE_PRE_VOL"
echo ""
echo "Étape suivante (non automatisée) :"
echo "  (b) Bras rapporté différé : après la course réelle et l'attestation"
echo "      de lecture humaine, lancer avec --bras-rapporte-differe"
echo "      --juge-externe argon-juge=gemini-4-argon"
echo "      --attestation-lecture-humaine ATTESTATION.json"
