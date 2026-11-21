#!/usr/bin/env bash
# Lanceur de la commande de création de l'instance de relecture du barreau 5, version 2, écrit le 2026-11-21.
# Pièce qui commande : additif 1, version 2, au devis du barreau 5 (c3120d3a…), § 3 : plafond du stockage de l'instance de
# relecture porté à 0,12 USD de l'heure à 300 Go ; la répétition générale et les instances de formation gardent 0,08.
# Ce script ne crée, n'arrête ni ne détruit d'instance, et n'atteint pas le réseau : il IMPRIME la commande de création,
# après les gardes du module `controle_ia.barreau5_familles.commande_lecture_v2` (épreuves : tests/test_commande_lecture_v2.py).
#
# Une seule sous-commande, pour la seule relecture décisive (codes : 0 accepté ; 2 refus, motif sur la sortie d'erreur) :
#   commande decisif RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json
#             mêmes arguments que la sous-commande « commande » de scripts/lancer_b5f_lecture_v1.sh ; GO_ID (l'accord de
#             lecture, GO-LECTURE-B5F) lu dans l'environnement ; RACINE : l'arbre de travail de la session au commit de
#             commande, c'est-à-dire l'arbre de ce script même (sinon refus) ; COMMIT : le commit de la marche, dont l'arbre
#             gelé est celui de CODE-LECTURE-B5F, et dont le registre propre porte, dans la colonne de référence de
#             GO-LECTURE-B5F : « <session de lecture> ; additif 1 v2 au devis sha256 <64 signes> ; commande de lecture v2,
#             commit <40 signes>, vérifiée sha256 <64 signes> ».
#
# D'où se joue chaque sous-commande (additif, § 3.2) : SEULE celle-ci se joue depuis l'arbre de travail au commit de
# commande. Toutes les autres (config, verifier, marche, preparer, ouvrir, monde, scores, detruire, verifier-destruction, et
# « commande repetition ») se jouent par scripts/lancer_b5f_lecture_v1.sh depuis un arbre dont la partie gelée est celle du
# commit de CODE-LECTURE-B5F (par exemple un arbre de travail extrait au commit de la marche), JAMAIS depuis le commit de
# commande : la garde de l'arbre de la session de la version 1 y refuserait. Ordre, inchangé : « config », « verifier »
# (arbre figé), puis « commande » (arbre de commande), puis création par la session.
set -uo pipefail
PY="${PYTHON_B5F:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
V1="scripts/lancer_b5f_lecture_v1.sh, depuis un arbre au code de lecture figé (jamais depuis le commit de commande)"
case "${1:-}" in
    commande)
        [ "$#" = 11 ] || { echo "B5F REFUS : commande decisif RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json" >&2; exit 2; }
        [ "$2" = decisif ] || { echo "B5F REFUS : la version 2 ne sert que la relecture décisive (PLAN decisif) ; la répétition générale se commande par $V1" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement (aucun départ sans accord)" >&2; exit 2; }
        sortie=$(PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.commande_lecture_v2 commande \
            "$2" "$3" "$4" "$5" "$6" "$7" "$GO_ID" "$8" "$9" "${10}" "${11}") || exit 2
        echo "B5F COMMANDE (à jouer par la session de lecture ; son échéance d'arrêt court depuis maintenant) :"
        printf '%s\n' "$sortie";;
    config|verifier|marche|preparer|ouvrir|monde|detruire|verifier-destruction|scores)
        echo "B5F REFUS : « $1 » ne se joue pas par la version 2 : $V1" >&2; exit 2;;
    *) echo "B5F REFUS : sous-commande inconnue (la version 2 ne porte que « commande decisif … ») ; les autres : $V1" >&2; exit 2;;
esac
