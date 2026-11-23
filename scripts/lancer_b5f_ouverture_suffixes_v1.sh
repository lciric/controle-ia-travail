#!/usr/bin/env bash
# Lanceur de l'ouverture de la lecture du barreau 5 sur une table à noms suffixés, v1, écrit le 2026-11-22.
# Pièce qui commande : erratum de chaîne de la relecture décisive du barreau 5, v2 (01298f0f…), § 5 ; variante accordée
# d'avance par GO-2026-11-22-147. Ce script ne crée, n'arrête ni ne détruit rien, et n'atteint pas le réseau : il joue le
# module `controle_ia.barreau5_familles.ouverture_suffixes_v1` (épreuves : tests/test_ouverture_suffixes_v1.py), depuis
# l'arbre de travail au commit v3, qui appelle le programme de lecture figé (lecture_v1.py, à son empreinte).
#
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie d'erreur) ; registre lu au commit COMMIT_REGISTRE ;
# l'épinglage du commit v3 est vérifié au registre du commit prouvé que cite SCORES-B5F :
#   variante RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json
#             à jouer d'abord, dans tous les cas : cohérence et engagement de la table, épinglage, règle ; imprime la
#             variante (a : table nue, lire par scripts/lancer_b5f_lecture_v1.sh depuis l'arbre au code figé ; b : table
#             à noms formés, lire par ce lanceur) et les traces E_a et E_b ; n'écrit rien ;
#   preparer RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json SORTIE
#             en (b) : coûts et résumé de la formation, bâtis sur la table traduite (mêmes arguments que la version 1) ;
#   ouvrir RACINE COMMIT_REGISTRE ARBRE TABLE.json COUTS.json FORMATION.json SORTIE
#             en (b) : ouverture et lecture ; résultat scellé sous SORTIE, avec traduction-table-b5f.json (mêmes arguments
#             que la version 1).
# RACINE : l'arbre de travail au commit v3, celui de ce script (sinon refus). Ordre recommandé à l'ouvreur : OUVERTURE-B5F
# inscrite, puis variante, preparer et ouvrir, au même commit du registre.
set -uo pipefail
PY="${PYTHON_B5F:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
ouverture() { PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.ouverture_suffixes_v1 "$@" || exit 2; }
case "${1:-}" in
    variante)
        [ "$#" = 5 ] || { echo "B5F REFUS : variante RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json" >&2; exit 2; }
        ouverture "$@";;
    preparer)
        [ "$#" = 6 ] || { echo "B5F REFUS : preparer RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json SORTIE" >&2; exit 2; }
        ouverture "$@";;
    ouvrir)
        [ "$#" = 8 ] || { echo "B5F REFUS : ouvrir RACINE COMMIT_REGISTRE ARBRE TABLE.json COUTS.json FORMATION.json SORTIE" >&2; exit 2; }
        ouverture "$@";;
    *) echo "B5F REFUS : sous-commande inconnue (variante, preparer, ouvrir) ; toutes les autres : scripts/lancer_b5f_lecture_v1.sh ou scripts/lancer_b5f_lecture_v3.sh" >&2; exit 2;;
esac
