#!/usr/bin/env bash
# Lanceur de la lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur »), v1, écrit le 2026-11-20.
# Texte : prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md (bdff244f…), « Plan d'analyse », points 7
# à 12 et 18. Aucune commande de ce script ne crée, n'arrête ni ne détruit d'instance, et aucune n'atteint le réseau : il
# contrôle, imprime et joue les programmes figés du paquet `controle_ia.barreau5_familles` (relecture_v1, sondes_v1,
# lecture_v1), éprouvés par tests/test_barreau5_familles_{relecture,sondes,lecture}_v1.py et tests/test_lancer_b5f_lecture_v1.py.
# L'amorce de l'instance (clonage au commit, entrées de lecture, paquets, essais, modèle au cache local, minuterie, versement
# prouvé de l'arbre fermé sur donnees/barreau5-familles-jumelles-v1-lecture) est scripts/amorce_b5f_lecture_v1.sh, que la
# sous-commande « commande » emporte en base64 ; ce lanceur ne joue jamais l'amorce.
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
#             épreuve à vérité plantée (point 11) : le même programme, sur un monde fabriqué et son registre fabriqué ;
#   commande PLAN RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json
#             côté session (ajout du 20 novembre) : IMPRIME la commande de création de l'instance de lecture (PLAN
#             decisif, étiquette b5f-lecture-v1, disque de 300 Go) ou de la répétition générale (PLAN repetition, étiquette
#             b5f-repetition-v1), qui porte scripts/amorce_b5f_lecture_v1.sh telle qu'au commit COMMIT ; GO_ID lu dans
#             l'environnement ; OFFRE.json : une entrée de la recherche du loueur, dans les bornes du devis ; COMMIT : commit de
#             la marche, dont le registre admet la marche et dont l'arbre gelé est celui de CODE-LECTURE-B5F ; ENTREES_COMMIT :
#             commit des entrées de lecture sur leur branche (« - » pour la répétition) ; EXISTANTS.json : liste des
#             adaptateurs existants {nom, chemin, sha256} (points d'ancrage du plan décisif, ou les quatre adaptateurs de la
#             répétition), donnée par la mère ; une empreinte absente est refusée ; sinon refus ;
#   detruire RACINE ID PLAN LISTE.json INVENTAIRE.json COMMIT
#             IMPRIME la destruction par l'identifiant (R10), si l'instance porte l'étiquette de la pièce et si chaque fichier
#             de l'inventaire final est au commit prouvé, sur une branche distante ; sinon refus ;
#   verifier-destruction LISTE.json ID TEMOIN
#             ID absent de la liste, TEMOIN présent ; jamais juger une destruction par un code de sortie ;
#   scores RACINE COMMIT RUN_ID
#             contenu de la ligne SCORES-B5F (« commit … ; inventaire sha256 … »), après vérification de l'arbre fermé au
#             commit prouvé (chaque fichier de l'inventaire à sa taille et à son empreinte, commit sur une branche distante).
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
    commande)
        [ "$#" = 11 ] || { echo "B5F REFUS : commande PLAN RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement (aucun départ sans accord)" >&2; exit 2; }
        sortie=$(relecture session commande "$2" "$3" "$4" "$5" "$6" "$7" "$GO_ID" "$8" "$9" "${10}" "${11}") || exit 2
        echo "B5F COMMANDE (à jouer par la session de lecture ; son échéance d'arrêt court depuis maintenant) :"
        printf '%s\n' "$sortie";;
    detruire)
        [ "$#" = 7 ] || { echo "B5F REFUS : detruire RACINE ID PLAN LISTE.json INVENTAIRE.json COMMIT" >&2; exit 2; }
        [ -n "${GO_ID:-}" ] || { echo "B5F REFUS : GO_ID absent de l'environnement" >&2; exit 2; }
        case "$3" in ''|*[!0-9]*) echo "B5F REFUS : identifiant illisible (destruction par l'identifiant seulement, R10)" >&2; exit 2;; esac
        relecture session detruire "$2" "$3" "$4" "$5" "$6" "$7" "$GO_ID"
        echo "B5F PUIS : bash scripts/lancer_b5f_lecture_v1.sh verifier-destruction LISTE_NEUVE.json $3 <TEMOIN>";;
    verifier-destruction)
        [ "$#" = 4 ] || { echo "B5F REFUS : verifier-destruction LISTE.json ID TEMOIN" >&2; exit 2; }
        relecture session verifier-destruction "$2" "$3" "$4";;
    scores)
        [ "$#" = 4 ] || { echo "B5F REFUS : scores RACINE COMMIT RUN_ID" >&2; exit 2; }
        relecture session scores "$2" "$3" "$4";;
    *) echo "B5F REFUS : sous-commande inconnue (config, verifier, marche, preparer, ouvrir, monde, commande, detruire, verifier-destruction, scores)" >&2; exit 2;;
esac
