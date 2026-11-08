#!/usr/bin/env bash
# sonde-garde-reelle-v1.sh — sonde réelle de la garde refus-question (R-1788)
# Coût estimé : ≈ 0,003 USD (trois appels courts).
# Envoie la question scellée à chaque modèle (Opus 5.5, Fable 5.1, Argon) ;
# un modèle qui refuse est retiré de tous les rôles de la course.
#
# Prérequis :
#   - Relais Claude lancé sur 127.0.0.1:PORT avec --modeles-permis claude-opus-5-5,claude-fable-5-1
#   - Relais Gemini lancé sur 127.0.0.1:8788 (pour Argon via appel-argon-v4d.sh)
#   - Question scellée : 29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4
#
# Usage : bash sonde-garde-reelle-v1.sh PORT_RELAIS_CLAUDE SORTIE.json
#
# NE PAS LANCER sans le mot de Lazar et le GO de la mère.
set -euo pipefail

DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"

QUESTION="${DEPOT_TRAVAIL}/docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md"
QUESTION_SHA256="29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4"

if [ $# -lt 2 ]; then
    echo "Usage : $0 PORT_RELAIS_CLAUDE SORTIE.json" >&2
    exit 2
fi

PORT_RELAIS="$1"
SORTIE="$2"

sha_question=$(sha256sum "$QUESTION" | cut -d' ' -f1)
if [ "$sha_question" != "$QUESTION_SHA256" ]; then
    echo "ERREUR : empreinte de la question incorrecte ($sha_question)" >&2
    exit 2
fi

exec python3 -I "${DEPOT_TRAVAIL}/docs/notes/ideation-pilier-attaque-v1/organisme-v1/pre-vol/sonde-garde-reelle-v1.py" \
    --question "$QUESTION" \
    --port-relais "$PORT_RELAIS" \
    --sortie "$SORTIE"
