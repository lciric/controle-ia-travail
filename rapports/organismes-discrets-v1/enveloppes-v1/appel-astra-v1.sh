#!/bin/sh
# appel-astra-v1.sh (18 novembre 2026) — enveloppe de gpt-6-astra (OpenAI) pour la course de l'organisme d'idéation sur les
# organismes discrets (lanceur v8). Même contrat que appel-argon-v6.sh ; la commande lancée est commande_astra_v1.py.
#
# Contrat : l'environnement minimal du noyau (PATH, HOME, LANG, PLAFOND_SESSION_USD, ROLE_POLE, MODELE_DEMANDE_POLE) ;
# la consigne sur l'entrée standard (UTF-8) ; la dernière ligne de la sortie standard est toujours un objet JSON
# {"texte", "cout_usd", "modele_servi", …}, coût fini et strictement positif.
#
# Relais compatible OpenAI (relais_kimi_v4.py, --amont https://api.openai.com --variable-cle OPENAI_API_KEY
# --modeles-permis gpt-6-astra) lancé séparément, sur la boucle locale, port 8790, avec la vraie clé dans son seul
# environnement ; cette enveloppe et la commande ne détiennent aucune clé. Prix 10 / 50 USD par million de jetons d'entrée /
# sortie : SUPPOSÉS (barème volontairement haut du collisionneur v8), comptés au coût ; figés après "$@".
set -eu
umask 077
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_astra_v1.py introuvable"}'; exit 2
fi
exec /usr/bin/timeout -k 20 1700 /usr/local/bin/python3 -I -B "$COMMANDE" --delai-s 1500 \
     "$@" --url-relais http://127.0.0.1:8790 --modele gpt-6-astra --prix-entree 10 --prix-sortie 50 \
     --max-sortie-jetons 32768 --sortie-min-jetons 4096
