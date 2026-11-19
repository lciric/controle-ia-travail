#!/usr/bin/env bash
# Lanceur de la formation des familles d'adaptateurs jumeaux du barreau 5, côté session (v1, 2026-11-20).
# Texte : prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon3.md (sections figées pour la
# formation) ; devis brouillon 3. Aucune commande de ce script ne crée, n'arrête ni ne détruit d'instance : il contrôle et
# IMPRIME les commandes, que la session de formation joue (préfixe GO_ID exigé par la garde de calcul ; destruction par
# l'identifiant seulement, R10). Toute la logique est dans `controle_ia.barreau5_familles.formation_v1` (sous-commande
# « session »), éprouvée par tests/test_barreau5_familles_formation_v1.py et tests/test_lancer_b5f_formation_v1.py.
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie d'erreur) :
#   plan                          sept instances, étiquette b5f-formation-v1-<n>, familles, coupure du devis ;
#   commande RACINE N OFFRE_ID COMMIT
#                                 GO_ID lu dans l'environnement ; refus sans GO_ID, si le registre propre n'a pas
#                                 CODE-FORMATION-B5F au même commit et GO-FORMATION-B5F au même accord, si l'amorce
#                                 scripts/amorce_b5f_formation_v1.sh manque, ou si la garde de calcul bloquerait la commande ;
#   depense N CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_TOTAL PRIX_TOTAL_H
#                                 point 14 : cumul relevé plus un quart d'heure ≥ coupure de l'instance, ou ≥ plafond de
#                                 200 USD : refus, et rappel de la destruction après versement ;
#   detruire RACINE ID N LISTE.json INVENTAIRE.json COMMIT
#                                 l'instance ID porte l'étiquette b5f-formation-v1-N dans LISTE.json (vastai show instances
#                                 --raw) et chaque sortie de son inventaire scellé est au commit COMMIT (versement prouvé) ;
#                                 sinon refus : rien n'est détruit avant le versement ;
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
    commande)
        [ "$#" = 5 ] || { echo "B5F REFUS : commande RACINE N OFFRE_ID COMMIT" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement (aucun départ sans accord)" >&2; exit 2; }
        echo "B5F COMMANDE (à jouer par la session de formation) :"
        session commande "$2" "$3" "$4" "$5" "$GO_ID";;
    depense)
        [ "$#" = 6 ] || { echo "B5F REFUS : depense N CUMUL_INSTANCE PRIX_INSTANCE_H CUMUL_TOTAL PRIX_TOTAL_H" >&2; exit 2; }
        PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.formation_v1 session depense "$2" "$3" "$4" "$5" "$6" \
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
    *) echo "B5F REFUS : sous-commande inconnue (plan, commande, depense, detruire, verifier-destruction)" >&2; exit 2;;
esac
