#!/usr/bin/env bash
# Lanceur de la commande de création de l'instance de relecture décisive du barreau 5, version 3, écrit le 2026-11-22.
# Pièce qui commande : erratum de chaîne de la relecture décisive du barreau 5, v2 (01298f0f…), § 4.3 ; accord
# GO-2026-11-22-147. La commande est celle de la version 2, l'amorce embarquée corrigée (une ligne ajoutée après la l. 362 :
# l'aide d'identification inscrite dans le clone des entrées ; 54a676f3… → 0adb6efb…).
# Ce script ne crée, n'arrête ni ne détruit d'instance, et n'atteint pas le réseau : il IMPRIME l'empreinte de l'amorce
# embarquée, puis la commande de création, après les gardes du module `controle_ia.barreau5_familles.commande_lecture_v3`
# (épreuves : tests/test_commande_lecture_v3.py). Condition d'arrêt (C12) : aucune commande ne sort si son segment base64
# décodé n'a pas l'empreinte de l'amorce corrigée.
#
# Une seule sous-commande (codes : 0 accepté ; 2 refus, motif sur la sortie d'erreur) :
#   commande decisif RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json
#             mêmes arguments que la version 2 ; GO_ID (GO-LECTURE-B5F) lu dans l'environnement ; RACINE : l'arbre de
#             travail de la session au commit v3, c'est-à-dire l'arbre de ce script même (sinon refus) ; COMMIT : le commit
#             de la marche, dont l'arbre gelé est celui de CODE-LECTURE-B5F, dont la ligne GO-LECTURE-B5F cite le commit v2
#             et dont le registre propre porte, sous la table, la ligne d'épinglage du commit v3.
# Toutes les autres sous-commandes se jouent par scripts/lancer_b5f_lecture_v1.sh, depuis un arbre au code de lecture figé ;
# l'ouverture à noms suffixés, par scripts/lancer_b5f_ouverture_suffixes_v1.sh.
set -uo pipefail
PY="${PYTHON_B5F:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
CORRIGEE=0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001
V1="scripts/lancer_b5f_lecture_v1.sh, depuis un arbre au code de lecture figé (ouverture à noms suffixés : scripts/lancer_b5f_ouverture_suffixes_v1.sh)"
case "${1:-}" in
    commande)
        [ "$#" = 11 ] || { echo "B5F REFUS : commande decisif RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json" >&2; exit 2; }
        [ "$2" = decisif ] || { echo "B5F REFUS : la version 3 ne sert que la relecture décisive (PLAN decisif) ; la répétition générale se commande par $V1" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement (aucun départ sans accord)" >&2; exit 2; }
        sortie=$(PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.commande_lecture_v3 commande \
            "$2" "$3" "$4" "$5" "$6" "$7" "$GO_ID" "$8" "$9" "${10}" "${11}") || exit 2
        n=$(printf '%s\n' "$sortie" | grep -o 'base64 -d' | wc -l)
        seg=$(printf '%s\n' "$sortie" | sed -n 's/^.*echo \([A-Za-z0-9+\/=]*\) | base64 -d > \/root\/amorce_b5f_lecture_v1\.sh.*$/\1/p')
        [ "$n" = 1 ] && [ -n "$seg" ] && [ "$(printf '%s\n' "$sortie" | wc -l)" = 1 ] \
            || { echo "B5F REFUS : un et un seul segment d'amorce embarquée attendu (C12) : aucune commande" >&2; exit 2; }
        sha=$(printf '%s' "$seg" | base64 -d 2> /dev/null | sha256sum | cut -c1-64)
        [ "$sha" = "$CORRIGEE" ] || { echo "B5F REFUS : amorce embarquée d'empreinte $sha ≠ amorce corrigée $CORRIGEE (C12) : aucune commande" >&2; exit 2; }
        echo "B5F AMORCE EMBARQUÉE : sha256 $sha"
        echo "B5F COMMANDE (à jouer par la session de lecture ; son échéance d'arrêt court depuis maintenant) :"
        printf '%s\n' "$sortie";;
    config|verifier|marche|preparer|ouvrir|monde|detruire|verifier-destruction|scores|variante)
        echo "B5F REFUS : « $1 » ne se joue pas par la version 3 : $V1" >&2; exit 2;;
    *) echo "B5F REFUS : sous-commande inconnue (la version 3 ne porte que « commande decisif … ») ; les autres : $V1" >&2; exit 2;;
esac
