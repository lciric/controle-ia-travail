#!/usr/bin/env bash
# Lanceur de la lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur »), v1, écrit le 2026-11-20.
# Texte : prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md (bdff244f…), « Plan d'analyse », points 7
# à 12 et 18. Aucune commande de ce script ne crée, n'arrête ni ne détruit d'instance, et aucune n'atteint le réseau : il
# contrôle, imprime et joue les programmes figés du paquet `controle_ia.barreau5_familles` (relecture_v1, sondes_v1,
# lecture_v1), éprouvés par tests/test_barreau5_familles_{relecture,sondes,lecture}_v1.py et tests/test_lancer_b5f_lecture_v1.py.
# L'amorce de l'instance de lecture (clonage au commit, paquets, modèle au cache local, minuterie, versement prouvé de
# l'arbre fermé sur la branche donnees/barreau5-familles-jumelles-v1-lecture) n'est pas écrite ici (rapport du développeur).
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie d'erreur) :
#   config RACINE PLAN ENTREES DIVERGENCE GARDE
#             côté session : configuration réelle de la marche (recette lue dans la configuration scellée de la course de
#             confirmation, empreinte vérifiée) ; GO_ID lu dans l'environnement (GO-LECTURE-B5F pour le plan « decisif »,
#             l'accord de calcul de la formation pour la « repetition ») ; PLAN : decisif ou repetition ; ENTREES : dossier
#             des entrées de lecture, relatif à RACINE (vide pour la répétition) ; DIVERGENCE : 1, ou 0 si la coupe 1 du
#             calendrier s'applique ; GARDE : trois_couches, couche_15 ou une_sur_dix (« Données gardées », replis) ;
#   verifier RACINE COMMIT CONFIG.json
#             côté session, juste avant la création de l'instance : registre propre au commit de la marche
#             (ENGAGEMENT-B5F antérieure à maintenant, postérieure à SORTIES-FORMATION-B5F et à toute relance ;
#             CODE-LECTURE-B5F, empreinte du programme de lecture égale ; EPREUVE-B5F passée pour ce programme ;
#             GO-LECTURE-B5F égale à l'accord de la configuration ; ni SCORES-B5F ni OUVERTURE-B5F), code du commit égal à
#             celui de CODE-LECTURE-B5F, arbre de travail de la session identique ; sinon refus ;
#   marche CONFIG.json RUN_ID PREREG
#             sur l'instance, depuis la racine du dépôt extrait au commit : la marche de relecture et de notation (mode
#             réel), modèle lu au cache local seulement ; elle écrit donnees/RUN_ID/ (arbre fermé lecture/, poids/,
#             activations/, inventaires) ; l'empreinte imprimée de lecture/inventaire.json est le contenu de SCORES-B5F ;
#   preparer RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json SORTIE
#             ouvreur : coûts et résumé de la formation (forme canonique), depuis la branche de la formation extraite dans
#             BRANCHE_FORMATION, par la règle de la copie lue (ligne de relance du registre au commit donné) ;
#   ouvrir RACINE COMMIT_REGISTRE ARBRE TABLE.json COUTS.json FORMATION.json SORTIE
#             ouvreur : ouverture et lecture au processeur (point 12), registre lu au commit donné, code de RACINE au commit
#             de CODE-LECTURE-B5F ; résultat scellé sous SORTIE (dossier neuf) ; LECTURE-B5F à inscrire ensuite ;
#   monde REGISTRE.md ARBRE TABLE.json COUTS.json FORMATION.json SORTIE
#             épreuve à vérité plantée (point 11) : le même programme, sur un monde fabriqué et son registre fabriqué.
set -uo pipefail
PY="${PYTHON_B5F:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
relecture() { PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.relecture_v1 "$@" || exit 2; }
lecture() { PYTHONPATH="$RACINE_CODE/src" "$PY" -B -m controle_ia.barreau5_familles.lecture_v1 "$@" || exit 2; }
case "${1:-}" in
    config)
        [ "$#" = 6 ] || { echo "B5F REFUS : config RACINE PLAN ENTREES DIVERGENCE GARDE" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement (aucune marche sans accord)" >&2; exit 2; }
        case "$3" in decisif|repetition) ;; *) echo "B5F REFUS : PLAN : decisif ou repetition" >&2; exit 2;; esac
        relecture session config "$2" "$GO_ID" "$3" "$4" "$5" "$6";;
    verifier)
        [ "$#" = 4 ] || { echo "B5F REFUS : verifier RACINE COMMIT CONFIG.json" >&2; exit 2; }
        relecture session verifier "$2" "$3" "$4"
        echo "B5F : registre, code et arbre conformes : l'instance de lecture peut être créée (étiquette b5f-lecture-v1)";;
    marche)
        [ "$#" = 4 ] || { echo "B5F REFUS : marche CONFIG.json RUN_ID PREREG" >&2; exit 2; }
        case "$3" in [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-b5f-lecture|[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-b5f-repetition) ;;
            *) echo "B5F REFUS : RUN_ID AAAAMMJJ-HHMMSS-b5f-lecture ou -b5f-repetition attendu" >&2; exit 2;; esac
        env HF_HUB_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$RACINE_CODE/src" \
            "$PY" -B -m controle_ia.barreau5_familles.relecture_v1 --config "$2" --run-id "$3" --prereg "$4" || exit 2;;
    preparer)
        [ "$#" = 6 ] || { echo "B5F REFUS : preparer RACINE COMMIT_REGISTRE BRANCHE_FORMATION TABLE.json SORTIE" >&2; exit 2; }
        lecture preparer --racine "$2" --commit-registre "$3" --formation-branche "$4" --table "$5" --sortie "$6";;
    ouvrir)
        [ "$#" = 8 ] || { echo "B5F REFUS : ouvrir RACINE COMMIT_REGISTRE ARBRE TABLE.json COUTS.json FORMATION.json SORTIE" >&2; exit 2; }
        lecture ouvrir --racine "$2" --commit-registre "$3" --arbre "$4" --table "$5" --couts "$6" --formation "$7" --sortie "$8";;
    monde)
        [ "$#" = 7 ] || { echo "B5F REFUS : monde REGISTRE.md ARBRE TABLE.json COUTS.json FORMATION.json SORTIE" >&2; exit 2; }
        lecture monde --registre "$2" --arbre "$3" --table "$4" --couts "$5" --formation "$6" --sortie "$7";;
    *) echo "B5F REFUS : sous-commande inconnue (config, verifier, marche, preparer, ouvrir, monde)" >&2; exit 2;;
esac
