#!/usr/bin/env bash
# Récupération du tour 2 du collisionneur « évasion et moniteurs » (GO-2026-10-28-03, enveloppe du tour 2 : 22 USD).
# Deux runs neufs (R12), après la fin du tour 3 pour ne pas télescoper les quotas :
#   (1) tour-2bis : même faits, même question ; l'arbitre accepte l'absence de l'espèce A (Opus 5.5, refus sec à la
#       conception) sur ses trois cellules ; Opus 4.8 et Gemini portent conception, équipe rouge et riposte.
#   (2) reprise étroite R-609 : question plus étroite et moins diffuse (validité de construit seule), posée UNE fois à
#       Opus 5.5 seul ; toutes les autres cellules acceptées absentes ; un second refus se consigne, sans autre reprise.
# Clés : RR_ANTHROPIC_API_KEY_3, GEMINI_API_KEY_2 ; par variable, jamais affichées. Un refus arrête le run (consigné).
set -uo pipefail; set +x
cd "$(dirname "$0")"
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente : rien lancé" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente : rien lancé" >&2; exit 2; }
[ ! -e run-tour-2bis-e3-v1 ] || { echo "run-tour-2bis-e3-v1 existe déjà (R12)" >&2; exit 2; }
[ ! -e run-tour-2-r609-e3-v1 ] || { echo "run-tour-2-r609-e3-v1 existe déjà (R12)" >&2; exit 2; }
[ -f question-r609-etroite-v1.md ] || { echo "question-r609-etroite-v1.md absente" >&2; exit 2; }
LOG=recuperation-tour-2-v1.log
h() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }

h "attente de la fin du tour 3 (collisionneur run-tour-3-e3-v1, puis enchaîneur)"
while pgrep -f 'collisionneur_v2.py etage3 --sortie run-tour-3-e3-v1' >/dev/null 2>&1; do sleep 20; done
while pgrep -f 'enchainer-evasion-v1.sh' >/dev/null 2>&1; do sleep 20; done
h "tour 3 fini ; récupération du tour 2"

lancer() {  # $1 sortie ; $2 question ; $3 plafond ; reste : --accepter-absence ID…
  local sortie="$1" question="$2" plafond="$3"; shift 3
  env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 \
    HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" \
    SSL_CERT_FILE="${SSL_CERT_FILE:-}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}" \
    ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" GEMINI_API_KEY="$GEMINI_API_KEY_2" \
    ../venv/bin/python -I -B collisionneur_v2.py etage3 \
      --sortie "$sortie" --faits faits-evasion-moniteurs-v1.md --question "$question" \
      --plafond-usd "$plafond" "$@"
}
verifier() {
  env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 ../venv/bin/python -I -B collisionneur_v2.py verifier "$1"
}

h "(1) tour-2bis : espèce A (Opus 5.5) absente, acceptée par l'arbitre ; B et C portent le tour"
lancer run-tour-2bis-e3-v1 question-evasion-moniteurs-v1.md 22 \
  --accepter-absence E3-T1-conception-A --accepter-absence E3-T2-redteam-A --accepter-absence E3-T3-riposte-A \
  >> tour-2bis-v1.log 2>&1
h "(1) tour-2bis fini, code $?"
verifier run-tour-2bis-e3-v1 >> tour-2bis-v1.log 2>&1; h "(1) verifier : code $?"

h "(2) reprise étroite R-609 : question de validité de construit, Opus 5.5 seul, une seule reprise"
lancer run-tour-2-r609-e3-v1 question-r609-etroite-v1.md 5 \
  --accepter-absence E3-T1-conception-B --accepter-absence E3-T1-conception-C \
  --accepter-absence E3-T2-redteam-A --accepter-absence E3-T2-redteam-B --accepter-absence E3-T2-redteam-C \
  --accepter-absence E3-T3-riposte-A --accepter-absence E3-T3-riposte-B --accepter-absence E3-T3-riposte-C \
  >> tour-2-r609-v1.log 2>&1
h "(2) reprise R-609 finie, code $? (un REFUS ici se consigne et s'arrête : pas d'autre reprise)"
verifier run-tour-2-r609-e3-v1 >> tour-2-r609-v1.log 2>&1; h "(2) verifier : code $?"
h "récupération du tour 2 terminée ; lis run-tour-2bis-e3-v1/etat.md et run-tour-2-r609-e3-v1/etat.md"
