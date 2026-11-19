#!/bin/sh
# appel-argon-sans-troncature-v1.sh (19 novembre 2026) — enveloppe d'Argon, version neuve (R12 : nom neuf ; appel-argon-v5.sh,
# 37c0205e…, reste en place et inchangée).
#
# Fondement : mot de Lazar « fais sauter la troncature pour argo aussi » (Argon), après « enlève la troncature pour Carbon » ;
# additif v2h de la course d'auto-conception. La commande lancée est la même : commande_argon_v3d.py (épinglée, inchangée,
# 46c91df4…), appel synchrone (countTokens puis generateContent), relais Gemini v2 d'Argon sur le port 8788.
#
# Une seule déclaration sert Argon PROPOSEUR et Argon JUGE (le noyau donne le rôle dans ROLE_POLE) : deux branches.
# - proposeur_ideation : SANS TRONCATURE — --max-sortie-jetons 65536 (maximum de la commande, MAX_SORTIE_JETONS_DEFAUT,
#   l. 348), --sans-config-pensee (aucun thinkingBudget : défaut du fournisseur), --provision-pensee-jetons 65536 (≥ la
#   sortie : la garde « pensée > provision », code 7, ne refuse plus une réponse complète), prix 8,3 / 41,5, 3 caractères par
#   jeton, marge 5 %, délai 1 680 s, arrêt dur timeout -k 20 1720 (1 740 s < 1 800 s de l'orchestrateur). Sous le plafond de
#   session des proposeurs (6,05 USD), la garde de la commande garde la sortie maximale sur la plus grande entrée.
# - juge_ideation : la ligne de l'enveloppe v5 À L'IDENTIQUE (moins la liste d'arguments du noyau, toujours vide) : délai 1 500 s, défauts de
#   la commande (sortie 65 536 réduite par la garde au plafond de juge, 0,60 USD ; provision et thinkingBudget 8 192),
#   timeout -k 20 1700. Sous 0,60 USD, une provision ≥ la sortie ramènerait la sortie à ≈ 6 900 jetons et refuserait toute
#   pensée au-delà (code 7) : plus contraignant que la v5 ; la v5 est gardée (additif v2h).
# - tout autre rôle : refus nommé, code 2 (comme la commande elle-même).
#
# Contrat (celui de l'enveloppe v5) : environnement minimal du noyau ; consigne sur l'entrée standard ; la dernière ligne de la
# sortie standard est toujours un objet JSON {"texte", "cout_usd", "modele_servi", …}. Clé factice seulement ; la vraie clé est
# dans le seul relais. Aucun argument admis.
set -eu
umask 077
if [ "$#" -ne 0 ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "appel-argon-sans-troncature-v1.sh : aucun argument admis (réglage figé)"}'; exit 2
fi
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_argon_v3d.py introuvable"}'; exit 2
fi
GEMINI_API_KEY=factice-relais; export GEMINI_API_KEY
case "${ROLE_POLE:-}" in
proposeur_ideation)
exec /usr/bin/timeout -k 20 1720 /usr/local/bin/python3 -I -B "$COMMANDE" --modele gemini-4-argon --prix-entree 8.3 --prix-sortie 41.5 --provision-pensee-jetons 65536 --sans-config-pensee --max-sortie-jetons 65536 --sortie-min-jetons 4096 --caracteres-par-jeton 3 --marge-entree 0.05 --delai-s 1680 --url-base http://127.0.0.1:8788/v1beta
;;
juge_ideation)
exec /usr/bin/timeout -k 20 1700 /usr/local/bin/python3 -I -B "$COMMANDE" --delai-s 1500 --prix-entree 8.3 --prix-sortie 41.5 --prix-requete-web-usd 0.05 --max-requetes-web-pire-cas 20 --provision-outil-jetons 32768 --url-base http://127.0.0.1:8788/v1beta
;;
*)
echo '{"texte": "", "cout_usd": 1e-06, "erreur": "appel-argon-sans-troncature-v1.sh : ROLE_POLE inconnu (proposeur_ideation ou juge_ideation)"}'; exit 2
;;
esac
