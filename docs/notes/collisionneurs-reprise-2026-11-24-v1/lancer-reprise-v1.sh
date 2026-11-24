#!/usr/bin/env bash
# Lanceur de la reprise des collisionneurs (GO-2026-11-24-08). Usage : lancer-reprise-v1.sh {principal|temoin|cible} ETIQUETTE
# Clés lues par leur nom seulement ; aucune valeur affichée.
set -u
cd "$(dirname "$0")/../../.."
export PYTHONPATH=src
R=docs/notes/collisionneurs-reprise-2026-11-24-v1
P=docs/notes/protocole-x-boucle-organisme-controle-v1
C=docs/notes/cartographie-mathematiques-ouvertes-v1/cible-publication-collisionneur-v1
S=docs/notes/collisionneur-v9/collisionneur_v9_v8d.py
mkdir -p "$R/journaux"
quoi=$1; etiquette=$2
log="$R/journaux/$quoi-$etiquette.log"
commun=(etage3 --opus --carbon --neon --cle-anthropic RR_ANTHROPIC_API_KEY_LUC --plafond-usd 18 --ligne-usd 18 --reprise)
echo "début $(date -u +%FT%TZ) $quoi $etiquette" > "$log"
case $quoi in
  principal) python3 -u $S "${commun[@]}" --sortie $R/boucle-organisme-controle/principal \
               --faits $P/faits-neutres-boucle-organisme-controle-v2.md \
               --question $P/question-neutre-collisionneur-boucle-organisme-controle-v2.md >> "$log" 2>&1 ;;
  temoin)    python3 -u $S "${commun[@]}" --sortie $R/boucle-organisme-controle/temoin \
               --faits $P/faits-neutres-boucle-organisme-controle-v2.md \
               --question $P/question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md >> "$log" 2>&1 ;;
  cible)     GEMINI_API_KEY="$GEMINI_API_KEY_2" python3 -u $S "${commun[@]}" --sortie $R/cible-publication/collisionneur \
               --faits $C/faits-neutres-cible-publication-evasion-v1.md \
               --question $C/question-neutre-cible-publication-evasion-v1.md >> "$log" 2>&1 ;;
  *) echo "inconnu" >> "$log"; exit 2 ;;
esac
code=$?
echo "fin $(date -u +%FT%TZ) code $code" >> "$log"
exit $code
