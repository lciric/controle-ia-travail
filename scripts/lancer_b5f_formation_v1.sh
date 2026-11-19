#!/usr/bin/env bash
# Lanceur de la formation des familles d'adaptateurs jumeaux du barreau 5, côté session (v1, écrit et corrigé le 2026-11-19).
# Texte : le préenregistrement que cite la ligne SCELLEMENT-B5F du registre propre (sections figées pour la formation) ;
# devis du brouillon 3. Aucune commande de ce script ne crée, n'arrête ni ne détruit d'instance : il contrôle et IMPRIME
# les commandes, que la session de formation joue (préfixe GO_ID exigé par la garde de calcul ; destruction par
# l'identifiant seulement, R10). Toute la logique est dans `controle_ia.barreau5_familles.formation_v1` (sous-commande
# « session »), éprouvée par tests/test_barreau5_familles_formation_v1.py et tests/test_lancer_b5f_formation_v1.py.
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie d'erreur) :
#   plan                          sept instances, étiquette b5f-formation-v1-<n>, familles, coupure du devis ;
#   commande RACINE N OFFRE.json COMMIT BRANCHE_CODE PREREG RUN_ID
#                                 GO_ID lu dans l'environnement ; OFFRE.json : une entrée de la recherche du loueur (champs
#                                 bruts), dans les bornes du devis (A100 SXM4 80 Go, ≤ 1,30 USD/h, ≥ 16 cœurs, ≥ 128 Go,
#                                 ≥ 150 Go de disque, stockage ≤ 0,08 USD/h, CUDA ≥ 13.0) ; COMMIT : commit de la course,
#                                 dont le registre propre porte SCELLEMENT-B5F (PREREG à son empreinte ; membres des familles
#                                 d'apprentissage ; sens de « pièce »), CODE-FORMATION-B5F (code identique, ancêtre ; arbre de
#                                 travail de la session identique aussi) et GO-FORMATION-B5F au même accord, et qui porte
#                                 l'amorce ; configuration de l'instance acceptée ; échéance d'arrêt calculée au prix de
#                                 l'offre ; garde de calcul rejouée ; sinon refus. Les clés passent par leur nom
#                                 ($HF_TOKEN, $GH_TOKEN) : le shell qui joue la ligne en donne la valeur au loueur ;
#   relance  RACINE N OFFRE.json COMMIT BRANCHE_CODE PREREG RUN_ID
#                                 relance unique d'une instance tombée (calendrier du texte) : mêmes contrôles, accord
#                                 GO-RELANCE-FORMATION-B5F qui cite l'instance N (GO_ID égal ; la ligne cite deux instances
#                                 au plus, et 56 USD de coupures au plus, sinon refus), RUN_ID et familles suffixés
#                                 « -x1 » (graines neuves), branche de sortie …-instance-N-x1 ; la première copie est versée
#                                 et jamais lue ;
#   config RACINE N PRIX_USD_H COMMIT RELANCE
#                                 imprime la configuration réelle de l'instance N (recette scellée, plan, coupure, prix,
#                                 membres et pièce lus dans SCELLEMENT-B5F au commit COMMIT ; RELANCE : 0 ou 1) ;
#   depense N MEMBRES CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_COMMUN PRIX_COMMUN_H RELANCE
#                                 point 14, deux compteurs (erratum 1 au brouillon 5, couples E-4a et E-8a) : cumul de
#                                 l'instance plus un quart d'heure ≥ sa coupure (MEMBRES : membres des familles
#                                 d'apprentissage, 2 ou 3 ; une relance a la coupure de l'instance qu'elle remplace), ou,
#                                 pour une pièce du devis (RELANCE=0), cumul commun de toutes les pièces du devis, sans la
#                                 dépense d'aucune relance, plus un quart d'heure ≥ plafond de 200 USD : refus, et rappel du
#                                 versement puis de la destruction. Une relance (RELANCE=1) n'a pas de troisième compteur, et
#                                 le plafond atteint ne l'arrête pas : seule sa coupure compte (CUMUL_COMMUN non lu) ;
#   detruire RACINE ID N LISTE.json INVENTAIRE.json COMMIT
#                                 l'instance ID porte l'étiquette b5f-formation-v1-N dans LISTE.json (vastai show instances
#                                 --raw) ; chaque sortie de son inventaire scellé est au commit COMMIT, à sa taille et à son
#                                 empreinte, le manifeste de la marche aussi dès que l'inventaire liste une sortie de la
#                                 marche (après un arrêt avant la marche, l'inventaire final ne porte que des traces), et
#                                 COMMIT est sur une branche distante (versement prouvé) ; sinon refus : rien n'est détruit
#                                 avant le versement. COMMIT est le commit prouvé, que nomme la ligne « versement final
#                                 prouvé … au commit » du journal de l'instance (l'avant-dernier de la branche de sortie quand
#                                 le journal de fin a été poussé), et non la tête de la branche ; INVENTAIRE.json :
#                                 traces-b5f/inventaire-final.json et son compagnon, tirés de ce commit après git fetch
#                                 (l'inventaire de la marche, donnees/RUN/inventaire.json, est accepté aussi) ;
#   verifier-destruction LISTE.json ID TEMOIN
#                                 ID absent de la liste, TEMOIN présent ; jamais juger une destruction par un code de sortie.
set -uo pipefail
PY="${PYTHON_B5F:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
session() { PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.formation_v1 session "$@" || exit 2; }
case "${1:-}" in
    plan)
        [ "$#" = 1 ] || { echo "B5F REFUS : plan" >&2; exit 2; }
        session plan;;
    commande|relance)
        [ "$#" = 8 ] || { echo "B5F REFUS : $1 RACINE N OFFRE.json COMMIT BRANCHE_CODE PREREG RUN_ID" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement (aucun départ sans accord)" >&2; exit 2; }
        echo "B5F COMMANDE (à jouer par la session de formation) :"
        session "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$GO_ID";;
    config)
        [ "$#" = 6 ] || { echo "B5F REFUS : config RACINE N PRIX_USD_H COMMIT RELANCE" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement" >&2; exit 2; }
        session config "$2" "$3" "$4" "$5" "$6" "$GO_ID";;
    depense)
        [ "$#" = 8 ] || { echo "B5F REFUS : depense N MEMBRES CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_COMMUN PRIX_COMMUN_H RELANCE" >&2; exit 2; }
        PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.formation_v1 session depense "$2" "$3" "$4" "$5" "$6" "$7" "$8" \
            || { echo "B5F : arrêt ; verser les sorties, puis : bash scripts/lancer_b5f_formation_v1.sh detruire RACINE <ID> $2 LISTE.json INVENTAIRE.json COMMIT" >&2; exit 2; };;
    detruire)
        [ "$#" = 7 ] || { echo "B5F REFUS : detruire RACINE ID N LISTE.json INVENTAIRE.json COMMIT" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement" >&2; exit 2; }
        case "$3" in ''|*[!0-9]*) echo "B5F REFUS : identifiant illisible (destruction par l'identifiant seulement, R10)" >&2; exit 2;; esac
        session detruire "$2" "$3" "$4" "$5" "$6" "$7" "$GO_ID"
        echo "B5F PUIS : bash scripts/lancer_b5f_formation_v1.sh verifier-destruction LISTE_NEUVE.json $3 <TEMOIN>";;
    verifier-destruction)
        [ "$#" = 4 ] || { echo "B5F REFUS : verifier-destruction LISTE.json ID TEMOIN" >&2; exit 2; }
        session verifier-destruction "$2" "$3" "$4";;
    *) echo "B5F REFUS : sous-commande inconnue (plan, commande, relance, config, depense, detruire, verifier-destruction)" >&2; exit 2;;
esac
