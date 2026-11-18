#!/bin/sh
# appel-carbon-v2.sh (18 novembre 2026) — enveloppe de gemini-4-carbon pour la troisième course Carbon (lanceur v10). Copie de
# appel-carbon-v1.sh (f0f15108…, inchangée, R12) avec deux changements, établis par deux épreuves réelles du 18 novembre
# (06:45Z) : (1) budget de pensée borné à 2 048 jetons (--provision-pensee-jetons 2048 ; la v1 laissait le défaut, 8 192) :
# avec 8 192, Carbon restait muet plus de 240 à 300 s, au-delà de la coupure à 300 s des connexions muettes de ce conteneur ;
# avec 1 024, il répond en 4,5 s sans flux et en 46 s en flux ; (2) relais Gemini v3 (lecture de l'amont en flux,
# relais_gemini_v3.py, 2cf6bc6d…) sur le port 8791, pour que seul le premier octet compte face à cette coupure.
# Écart déclaré : Argon pense avec 8 192 jetons ; les courses Carbon et Argon ne sont pas strictement jumelles.
#
# --- en-tête de la v1, pour mémoire ---
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
     --provision-outil-jetons 32768 --url-base http://127.0.0.1:8791/v1beta --provision-pensee-jetons 2048
