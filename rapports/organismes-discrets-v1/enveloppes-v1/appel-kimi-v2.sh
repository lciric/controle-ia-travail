#!/bin/sh
# appel-kimi-v2.sh (18 novembre 2026) — copie de appel-kimi-v1.sh (6f006d03…, inchangée, R12), délais seuls changés après la
# contre-lecture du lanceur v9 (constat 2) : Kimi produit 24 à 35 jetons par seconde (13 appels journalisés) et le relais ne
# rend rien avant la fin de la génération ; à 1 500 s la sortie de 98 304 jetons était hors de portée. Délais cohérents :
# commande 3 300 s < enveloppe 3 500 s < orchestrateur 3 600 s (--delai-commande-s, passé par le lanceur v9) ; session de
# l'orchestrateur 3 900 s ; relais Moonshot --delai-amont-s 3 400 (≥ commande).
#
# --- en-tête de la v1, pour mémoire ---
# appel-kimi-v1.sh (18 novembre 2026) — enveloppe de kimi-k3.1-pro (Moonshot) pour la course de l'organisme d'idéation sur
# les organismes discrets (lanceur v9, lignée kimi ; mot de Lazar : « oublie pas kimi dans les courses »). Copie de
# appel-astra-v1.sh (aa2df474…, inchangée, R12) ; la commande lancée est commande_kimi_ideation_v1.py.
#
# Contrat : l'environnement minimal du noyau (PATH, HOME, LANG, PLAFOND_SESSION_USD, ROLE_POLE, MODELE_DEMANDE_POLE) ;
# la consigne sur l'entrée standard (UTF-8) ; la dernière ligne de la sortie standard est toujours un objet JSON
# {"texte", "cout_usd", "modele_servi", …}, coût fini et strictement positif.
#
# Relais compatible OpenAI (relais_kimi_v4.py, --amont https://api.moonshot.ai --variable-cle KIMI_API_KEY
# --modeles-permis kimi-k3.1-pro) lancé séparément, sur la boucle locale, port 8789, avec la vraie clé dans son seul
# environnement ; il lit l'amont en flux. Cette enveloppe et la commande ne détiennent aucune clé. Prix 2 / 10 USD par
# million de jetons d'entrée / sortie : vérifiés le 30 octobre 2026 sur la page des prix de Moonshot (page c62210a0…) et
# observés conformes à la facture (docs/notes/ideation-organisme-v1/course-2/devis-course-2-et-pre-pilote-v4.md l. 36) ;
# cache 0,20 compté au prix plein (borne haute) ; figés après "$@". Sortie maximale 98 304 jetons : Kimi a déjà épuisé
# 32 768 jetons en raisonnement sans rien rendre (registres/depenses.md, 14 novembre) ; le plafond de session borne le reste.
set -eu
umask 077
DEPOT_TRAVAIL="${DEPOT_TRAVAIL:-/home/user/controle-ia-travail}"
COMMANDE="$DEPOT_TRAVAIL/docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_kimi_ideation_v1.py"
if [ ! -f "$COMMANDE" ]; then
    echo '{"texte": "", "cout_usd": 1e-06, "erreur": "commande_kimi_ideation_v1.py introuvable"}'; exit 2
fi
exec /usr/bin/timeout -k 20 3500 /usr/local/bin/python3 -I -B "$COMMANDE" --delai-s 3300 \
     "$@" --url-relais http://127.0.0.1:8789 --modele kimi-k3.1-pro --prix-entree 2 --prix-sortie 10 \
     --max-sortie-jetons 98304 --sortie-min-jetons 4096
