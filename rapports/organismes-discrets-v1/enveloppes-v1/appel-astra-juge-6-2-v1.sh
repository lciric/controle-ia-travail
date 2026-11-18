#!/bin/sh
# appel-astra-juge-6-2-v1.sh (18 novembre 2026) — enveloppe de gpt-6.2-astra (OpenAI) pour le SEUL bras du juge externe
# différé de la lignée Astra de l'organisme d'idéation sur les organismes discrets (lanceur du bras v2), sur mot de Lazar
# « go 6.2 » : le juge est joué avec gpt-6.2-astra à la place de gpt-6-astra, remplacement déclaré au manifeste du bras.
# Copie de appel-astra-v1.sh ; seuls changent le modèle et les prix. La commande lancée reste commande_astra_v1.py.
#
# Contrat : l'environnement minimal du noyau (PATH, HOME, LANG, PLAFOND_SESSION_USD, ROLE_POLE, MODELE_DEMANDE_POLE) ;
# la consigne sur l'entrée standard (UTF-8) ; la dernière ligne de la sortie standard est toujours un objet JSON
# {"texte", "cout_usd", "modele_servi", …}, coût fini et strictement positif.
#
# Relais compatible OpenAI (relais_kimi_v4.py, --amont https://api.openai.com --variable-cle OPENAI_API_KEY
# --modeles-permis gpt-6.2-astra) lancé séparément, sur la boucle locale, port 8790, avec la vraie clé dans son seul
# environnement ; cette enveloppe et la commande ne détiennent aucune clé. Prix 8 / 40 USD par million de jetons d'entrée /
# sortie : lus sur la page officielle des tarifs d'OpenAI le 18 novembre 2026 (tableau « Standard » ;
# docs/sources/tarifs-openai-v2/developers-openai-com-api-docs-pricing-2026-11-18.html, 35a04829… ; entrée en cache 0,40
# comptée au prix plein, borne haute), comptés au coût ; figés après "$@".
set -eu
umask 077
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_astra_v1.py introuvable"}'; exit 2
fi
exec /usr/bin/timeout -k 20 1700 /usr/local/bin/python3 -I -B "$COMMANDE" --delai-s 1500 \
     "$@" --url-relais http://127.0.0.1:8790 --modele gpt-6.2-astra --prix-entree 8 --prix-sortie 40 \
     --max-sortie-jetons 32768 --sortie-min-jetons 4096
