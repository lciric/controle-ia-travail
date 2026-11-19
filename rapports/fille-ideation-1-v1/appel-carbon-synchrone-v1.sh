#!/bin/sh
# appel-carbon-synchrone-v1.sh (19 novembre 2026) — enveloppe de Carbon par la commande SYNCHRONE d'Argon, version 1 (R12 :
# nom neuf ; aucun fichier épinglé n'est modifié).
#
# Fondement : mot de Lazar « go (a) » (Carbon par la commande synchrone d'Argon, éprouvé d'abord par un appel réel sur le
# plus grand lot, puis course) et « augmente le plafond » (plafond de session des proposeurs 6,00 USD) ; additif v2g de la
# course d'auto-conception. Cause : en mode lot, le budget de pensée de Carbon n'est pas tenu (journal provisoire v62,
# PO-178 : budget 28 672, sortie 32 768 → pensée 32 765, réponse 3 jetons).
#
# Ce que fait cette enveloppe : lance commande_argon_v3d.py (épinglée, inchangée, 46c91df4…) — celle d'Argon, appel
# synchrone generateContent précédé de countTokens — avec TOUT le réglage de Carbon figé ici (aucun argument admis : le
# noyau ne peut rien changer) :
#   --modele gemini-4-carbon --prix-entree 8.3 --prix-sortie 41.5 (prix de Carbon, USD par million)
#   SANS TRONCATURE (mot de Lazar « enlève la troncature pour Carbon ») :
#   --max-sortie-jetons 65536 (le maximum de la commande, MAX_SORTIE_JETONS_DEFAUT, commande_argon_v3d.py l. 348)
#   --sans-config-pensee (aucun thinkingBudget posé : défaut du fournisseur ; en lot, le budget n'était pas tenu)
#   --provision-pensee-jetons 65536 (provision de la garde ≥ la sortie : la garde « pensée > provision », code 7, ne refuse
#     plus une réponse complète quand la pensée compte dans maxOutputTokens ; elle est comptée EN PLUS de la sortie au pire cas)
#   --sortie-min-jetons 4096 (la commande réduirait la sortie pour tenir PLAFOND_SESSION_USD ; le lanceur v7 exige qu'elle ne
#     la réduise pas sur la plus grande entrée de la course, au plafond de 6 USD)
#   --caracteres-par-jeton 3 --marge-entree 0.05 (estimation de l'entrée ; le compte exact countTokens l'emporte s'il est plus grand)
#   --delai-s 1680 (délai global de la commande : code 6 et pire cas compté au-delà)
#   --url-base http://127.0.0.1:8792/v1beta (relais Gemini v2 DÉDIÉ à Carbon, port 8792, lancé avec --modele gemini-4-carbon)
# Arrêt dur : timeout 1720 s puis SIGKILL 20 s plus tard (1 740 s), sous le délai fixe de 1 800 s que l'orchestrateur
# donne à toute commande externe.
#
# Contrat (celui de l'enveloppe d'Argon v5) : environnement minimal du noyau (PATH, HOME, LANG, PLAFOND_SESSION_USD,
# ROLE_POLE, MODELE_DEMANDE_POLE) ; consigne sur l'entrée standard ; la dernière ligne de la sortie standard est toujours
# un objet JSON {"texte", "cout_usd", "modele_servi", …}, coût fini et strictement positif. Cette enveloppe ne détient que
# la clé factice ; la vraie clé n'est connue que du relais.
set -eu
umask 077
if [ "$#" -ne 0 ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "appel-carbon-synchrone-v1.sh : aucun argument admis (réglage figé)"}'; exit 2
fi
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_argon_v3d.py introuvable"}'; exit 2
fi
GEMINI_API_KEY=factice-relais; export GEMINI_API_KEY
exec /usr/bin/timeout -k 20 1720 /usr/local/bin/python3 -I -B "$COMMANDE" --modele gemini-4-carbon --prix-entree 8.3 --prix-sortie 41.5 --provision-pensee-jetons 65536 --sans-config-pensee --max-sortie-jetons 65536 --sortie-min-jetons 4096 --caracteres-par-jeton 3 --marge-entree 0.05 --delai-s 1680 --url-base http://127.0.0.1:8792/v1beta
