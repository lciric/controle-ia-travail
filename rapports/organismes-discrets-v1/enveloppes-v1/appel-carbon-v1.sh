#!/bin/sh
# appel-carbon-v1.sh (18 novembre 2026) — enveloppe de gemini-4-carbon pour la course de l'organisme d'idéation sur les organismes
# discrets (lanceur v8). Copie de rapports/fille-ideation-1-v1/appel-argon-v5.sh (empreinte 37c0205e26f83cbd…, inchangée, R12)
# avec deux changements : la commande lancée est commande_argon_v3e.py (lit MODELE_DEMANDE_POLE), et le modèle est figé
# après "$@" (--modele gemini-4-carbon) : ni le noyau ni un argument ne peuvent le changer.
#
# Contrat : l'environnement minimal du noyau (PATH, HOME, LANG, PLAFOND_SESSION_USD, ROLE_POLE, MODELE_DEMANDE_POLE) ;
# la consigne sur l'entrée standard (UTF-8) ; la dernière ligne de la sortie standard est toujours un objet JSON
# {"texte", "cout_usd", "modele_servi", …}, coût fini et strictement positif.
#
# Relais Gemini v2 (relais_gemini_v2.py) lancé séparément, sur la boucle locale, port 8788, avec la vraie GEMINI_API_KEY
# dans son seul environnement et gemini-4-carbon dans sa liste de modèles permis ; cette enveloppe ne détient que la clé factice.
# Prix : 8,3 / 41,5 USD par million de jetons d'entrée / sortie, repris de l'enveloppe v5 (bornes hautes : la page publique
# des tarifs lue le 18 novembre 2026 affiche 2 / 10 jusqu'au 30 novembre 2026 pour les deux modèles) ; comptés au coût.
set -eu
umask 077
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3e.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_argon_v3e.py introuvable"}'; exit 2
fi
GEMINI_API_KEY=factice-relais; export GEMINI_API_KEY
exec /usr/bin/timeout -k 20 1700 /usr/local/bin/python3 -I -B "$COMMANDE" --delai-s 1500 \
     "$@" --modele gemini-4-carbon --prix-entree 8.3 --prix-sortie 41.5 --prix-requete-web-usd 0.05 --max-requetes-web-pire-cas 20 \
     --provision-outil-jetons 32768 --url-base http://127.0.0.1:8788/v1beta
