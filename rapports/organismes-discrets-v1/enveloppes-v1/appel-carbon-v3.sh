#!/bin/sh
# appel-carbon-v3.sh (18 novembre 2026) — enveloppe de gemini-4-carbon **par lot** pour la troisième course Carbon (lanceur v12).
# Décision de la session mère (R-3241) : la lignée Carbon passe par le mode par lot à 8 192 jetons de pensée, en courses
# jumelles d'Argon (en appel synchrone à ce budget, Carbon reste muet au-delà de la coupure à 300 s des connexions muettes de
# ces conteneurs ; par lot, il a rendu en 430 s : addendum des témoins et de Carbon v4, § 5, 3c6f9448…).
#
# Contrat : celui de appel-carbon-v1.sh (environnement minimal du noyau ; consigne sur l'entrée standard ; dernière ligne JSON).
# Commande : commande_gemini_lot_v1.py (9484dce0…, scellée) ; relais Gemini v4 (relais_gemini_v4.py, 543e728d…) lancé à part,
# port 8792, modèle permis gemini-4-carbon, clé GEMINI_API_KEY dans son seul environnement ; cette enveloppe et la commande
# ne détiennent aucune clé. Budget de pensée 8 192 (comme Argon). Prix 8,3 / 41,5 USD par million de jetons d'entrée /
# sortie, bornes hautes reprises des enveloppes Carbon et Argon (page publique lue le 18 novembre : 2 / 10 jusqu'au 30 novembre ;
# lecture d'agent non empreintée), au prix plein (facteur de lot 1 : la remise de moitié n'est pas comptée, borne haute).
# Délais cohérents : commande 3 300 s (plus intervalle 30 s et deux délais de requête de 120 s : 3 570 s au plus) <
# enveloppe 3 590 s < orchestrateur 3 600 s (--delai-commande-s passé par le lanceur v12). Tout est figé
# après "$@".
set -eu
umask 077
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_gemini_lot_v1.py introuvable"}'; exit 2
fi
exec /usr/bin/timeout -k 5 3590 /usr/local/bin/python3 -I -B "$COMMANDE" \
     "$@" --modele gemini-4-carbon --url-base http://127.0.0.1:8792/v1beta --prix-entree 8.3 --prix-sortie 41.5 \
     --facteur-lot 1 --provision-pensee-jetons 8192 --max-sortie-jetons 32768 --sortie-min-jetons 4096 \
     --intervalle-s 30 --delai-s 3300 --delai-requete-s 120
