#!/usr/bin/env bash
# Étage III du collisionneur v2.6 sur la QUESTION SCELLÉE du pilier attaque (antériorité et originalité),
# pour l'entretien TAIF. Niveau méthode, aucune recette. Remplace la v2 (R12) : seul le plafond change
# (20 -> 25, GO-2026-11-08-06 mis à jour, R-1787). Copie de lancer-tour-memoire-v3-plafond35-luc.sh : interpréteur = venv
# principal du dépôt (`anthropic`), fichiers d'entrée et dossier de sortie propres à ce tour.
# Un refus de classifieur ARRÊTE le tour (code 2/5), consigné, jamais relancé ni reformulé par le code ;
# reprise humaine seulement, par --accepter-absence (R-468, R-609). Je ne touche pas cette garde.
# Clés : ANTHROPIC_API_KEY <- RR_ANTHROPIC_API_KEY_LUC (R-547) ; GEMINI_API_KEY <- GEMINI_API_KEY
# (jamais GEMINI_API_KEY_2, R-1754). Plafond 25 USD pour tout le dossier (GO-2026-11-08-06). Clés par variable, jamais affichées.
set -uo pipefail; set +x
[ -n "${RR_ANTHROPIC_API_KEY_LUC:-}" ] || { echo "RR_ANTHROPIC_API_KEY_LUC absente de cette session : rien n'est lancé" >&2; exit 2; }
[ -n "${GEMINI_API_KEY:-}" ] || { echo "GEMINI_API_KEY absente de cette session : rien n'est lancé" >&2; exit 2; }
cd "$(dirname "$0")"
[ -f faits-pilier-attaque-v1.md ] || { echo "faits-pilier-attaque-v1.md absent (nœud du faits.md non tranché) : rien n'est lancé" >&2; exit 2; }
[ -f question-pilier-attaque-v1.md ] || { echo "question-pilier-attaque-v1.md absent : rien n'est lancé" >&2; exit 2; }
[ ! -e run-pilier-attaque-e3-v1 ] || { echo "run-pilier-attaque-e3-v1 existe déjà (R12)" >&2; exit 2; }
PYBIN=/home/user/controle-ia-travail/.venv/bin/python
[ -x "$PYBIN" ] || { echo "interpréteur $PYBIN absent" >&2; exit 2; }
exec env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_LUC" GEMINI_API_KEY="$GEMINI_API_KEY" \
  "$PYBIN" -I -B collisionneur_v2.py etage3 \
    --sortie run-pilier-attaque-e3-v1 --faits faits-pilier-attaque-v1.md \
    --question question-pilier-attaque-v1.md --plafond-usd 25
