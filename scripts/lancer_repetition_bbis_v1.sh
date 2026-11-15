#!/usr/bin/env bash
# Chaîne de session de la répétition sur carte de l'étape B bis de T0.7, v1 (mot de Lazar R-2802 : écart déclaré au texte scellé ;
# sous la ligne GO-2026-11-14-09 ; plafond de la répétition strictement sous 3 USD ; une seule machine, A100 SXM4 80 Go comme la
# course). Côté session seulement : aucune commande de ce script ne crée, n'arrête ni ne détruit d'instance ; il contrôle, lit
# (lecture seule) et IMPRIME les commandes, que la mère joue (préfixe GO_ID exigé par la garde de calcul ; destruction par
# l'identifiant avec -y, R10, R-2789). Fichiers de l'outil (`show user`, `show instances`) écrits sous `umask 077` dans un dossier
# jetable, lus par programme (champs utiles seulement), jamais affichés, supprimés aussitôt (contre-lecture de sûreté m3, M3).
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie standard) :
#   credit                           crédit du compte (champ `credit` seul) : au moins 4 USD, sinon refus ;
#   offre-depuis-recherche RECHERCHE.json ID OFFRE.json
#                                    OFFRE.json construit par programme depuis la sortie de `vastai search offers --raw` ;
#                                    recherche (filtre de l'outil, la garde locale décide) :
#                                    ( umask 077; vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 cpu_cores_effective>=16
#                                      cpu_ram>=128 disk_space>=60 reliability>0.98 cuda_max_good>=13.0' -o 'dph_total' --raw
#                                      > RECHERCHE.json ) ;
#   offre OFFRE.json ID PRIX_USD_H   bornes de l'offre (A100 SXM4 80 Go exactement, prix ≤ 1,40 USD/h, étiquette de la répétition,
#                                    version CUDA servie par l'hôte `cuda_max_good` ≥ 13.0, celle de la roue torch de
#                                    requirements-gpu.txt ; clé absente ou illisible : refus) ;
#   commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE ECHEANCE_UTC_S PRIX_USD_H FEU IMAGE
#                                    imprime la commande de création après : l'offre ; le feu écrit portant GO-2026-11-14-09,
#                                    R-2802 et l'image exacte ; GH_TOKEN présent (par le nom) ; l'échéance (coût strictement sous
#                                    3 USD) ; COMMIT présent, portant l'amorce de la course, cette amorce et le script ; l'amorce en
#                                    essai local sur un dossier jetable ;
#   relire CREATION.json             après la création : instance du `new_contract`, étiquette, carte, prix relus ; hors borne : refus ;
#   trouver SORTIE.json              sans `new_contract` lisible : la seule instance de l'étiquette de la répétition, écrite ;
#   depense CUMUL_USD PRIX_CARTE_USD_H   garde de dépense de la course à la coupure de 3 USD (cumul de la répétition seule) ;
#   detruire CREATION.json           garde positive : `new_contract` lu, entier ASCII, jamais une autre session, relu avec
#                                    l'étiquette dans la liste ; imprime `GO_ID=… vastai destroy instance N -y` ;
#   verifier-destruction CREATION.json TEMOIN [LISTE.json]
#                                    absence prouvée dans la liste lue sans erreur, témoin 60480302 ou 60670453 présent.
set -uo pipefail
PY="${PYTHON_BBIS:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
GO_ID=GO-2026-11-14-09
ETIQUETTE=bbis-t07-repetition-v1
DISQUE=60
py_rep() { PYTHONPATH="$RACINE_CODE/src" "$PY" "$ICI/repetition_carte_bbis_v1.py" "$@"; }
lire_prive() {  # $1 = objet de `show` (instances | user) : imprime le chemin d'un fichier privé (umask 077), rien d'autre
    local dl f c
    dl=$(mktemp -d) || return 1
    f="$dl/sortie.json"
    ( umask 077; "${VASTAI_BBIS:-vastai}" show "$1" --raw < /dev/null > "$f" 2> "$dl/erreur.txt" ); c=$?
    if [ "$c" != 0 ]; then rm -f -- "$f" "$dl/erreur.txt"; rmdir -- "$dl"; echo "BBIS REPETITION : lecture de « show $1 » en échec (code $c)" >&2; return 1; fi
    echo "$f"; }
case "${1:-}" in
    credit)
        [ "$#" = 1 ] || { echo "BBIS REPETITION REFUS : credit"; exit 2; }
        F=$(lire_prive user) || { echo "BBIS REPETITION REFUS : crédit illisible (lecture en échec) : aucune location"; exit 2; }
        py_rep credit "$F" --supprimer; exit $?;;
    offre-depuis-recherche)
        [ "$#" = 4 ] || { echo "BBIS REPETITION REFUS : offre-depuis-recherche RECHERCHE.json ID OFFRE.json"; exit 2; }
        py_rep offre-depuis-recherche "$2" "$3" "$4"; exit $?;;
    offre)
        [ "$#" = 4 ] || { echo "BBIS REPETITION REFUS : offre OFFRE.json ID PRIX_USD_H"; exit 2; }
        py_rep offre "$2" "$3" "$4"; exit $?;;
    commande)
        [ "$#" = 10 ] || { echo "BBIS REPETITION REFUS : commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE ECHEANCE_UTC_S PRIX_USD_H FEU IMAGE"; exit 2; }
        RAC="$2"; FOFFRE="$3"; OFFRE="$4"; COMMIT="$5"; BRC="$6"; ECH="$7"; PRIX="$8"; FEU="$9"; IMAGE="${10}"
        printf '%s' "$OFFRE" | LC_ALL=C grep -qxE '[1-9][0-9]*' || { echo "BBIS REPETITION REFUS : identifiant d'offre illisible (entier ASCII)"; exit 2; }
        case "$ECH" in ''|*[!0-9]*) echo "BBIS REPETITION REFUS : échéance illisible"; exit 2;; esac
        case "$IMAGE" in *[!A-Za-z0-9._:/-]*|'') echo "BBIS REPETITION REFUS : image illisible"; exit 2;; esac
        case "$BRC" in *[!A-Za-z0-9._/-]*|'') echo "BBIS REPETITION REFUS : branche illisible"; exit 2;; esac
        case "$FEU" in *"$IMAGE"*) ;; *) echo "BBIS REPETITION REFUS : le feu écrit ne nomme pas l'image $IMAGE"; exit 2;; esac
        [ -n "${GH_TOKEN:-}" ] || { echo "BBIS REPETITION REFUS : GH_TOKEN absent du shell de la mère (par le nom) : la machine serait louée pour rien"; exit 2; }
        py_rep offre "$FOFFRE" "$OFFRE" "$PRIX" > /dev/null || { py_rep offre "$FOFFRE" "$OFFRE" "$PRIX"; exit 2; }
        py_rep garde-commande "$ECH" "$PRIX" "$FEU" "$(date +%s)" > /dev/null || { py_rep garde-commande "$ECH" "$PRIX" "$FEU" "$(date +%s)"; exit 2; }
        git -C "$RAC" cat-file -e "$COMMIT^{commit}" 2> /dev/null || { echo "BBIS REPETITION REFUS : commit $COMMIT absent de $RAC"; exit 2; }
        git -C "$RAC" cat-file -e "$COMMIT:scripts/amorce_bbis_v1.sh" 2> /dev/null || { echo "BBIS REPETITION REFUS : amorce de la course absente du commit"; exit 2; }
        git -C "$RAC" show "$COMMIT:scripts/amorce_repetition_bbis_v1.sh" 2> /dev/null | cmp -s - "$ICI/amorce_repetition_bbis_v1.sh" \
            || { echo "BBIS REPETITION REFUS : amorce de répétition du commit ≠ celle de ce dossier"; exit 2; }
        SH=$(git -C "$RAC" show "$COMMIT:scripts/repetition_carte_bbis_v1.py" 2> /dev/null | sha256sum | cut -d' ' -f1)
        [ "$SH" != "$(printf '' | sha256sum | cut -d' ' -f1)" ] || { echo "BBIS REPETITION REFUS : script de la répétition absent du commit"; exit 2; }
        RAC_ESSAI=$(mktemp -d) || { echo "BBIS REPETITION REFUS : dossier jetable de l'essai local impossible"; exit 2; }
        AMORCE_ESSAI_LOCAL=1 RACINE_AMORCE="$RAC_ESSAI" COMMIT="$COMMIT" BRANCHE_CODE="$BRC" ECHEANCE_UTC_S="$ECH" GO_ID="$GO_ID" \
            SCRIPT_SHA256="$SH" bash "$ICI/amorce_repetition_bbis_v1.sh" > /dev/null; c=$?
        rmdir "$RAC_ESSAI" || { echo "BBIS REPETITION REFUS : l'amorce en essai local a écrit dans $RAC_ESSAI"; exit 2; }
        [ "$c" = 0 ] || { echo "BBIS REPETITION REFUS : arguments refusés par l'amorce de répétition"; exit 2; }
        B64=$(base64 -w 0 < "$ICI/amorce_repetition_bbis_v1.sh") || { echo "BBIS REPETITION REFUS : amorce illisible"; exit 2; }
        py_rep garde-commande "$ECH" "$PRIX" "$FEU" "$(date +%s)"
        echo "BBIS REPETITION COMMANDE (à jouer par la mère, sortie écrite sous umask 077 dans CREATION.json ; amorce $(sha256sum < "$ICI/amorce_repetition_bbis_v1.sh" | cut -c1-16), script $(printf '%s' "$SH" | cut -c1-16)) :"
        echo "GO_ID=$GO_ID vastai create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQUETTE --env \"-e COMMIT=$COMMIT -e BRANCHE_CODE=$BRC -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GO_ID -e SCRIPT_SHA256=$SH -e GH_TOKEN=\$GH_TOKEN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce_repetition_bbis_v1.sh && bash /root/amorce_repetition_bbis_v1.sh\""
        exit 0;;
    relire|detruire)
        [ "$#" = 2 ] || { echo "BBIS REPETITION REFUS : $1 CREATION.json"; exit 2; }
        N=$(py_rep creation "$2") || { echo "$N"; exit 2; }
        N=${N##* }
        F=$(lire_prive instances) || { echo "BBIS REPETITION REFUS : liste des instances illisible (lecture en échec) : rien n'est imprimé"; exit 2; }
        if [ "$1" = relire ]; then py_rep relire "$2" "$F" --supprimer; exit $?; fi
        py_rep etiquette "$2" "$F" --supprimer || exit 2
        echo "GO_ID=$GO_ID vastai destroy instance $N -y"
        echo "BBIS REPETITION PUIS (jamais juger la destruction par le code de sortie) : bash scripts/lancer_repetition_bbis_v1.sh verifier-destruction $2 60480302"
        exit 0;;
    trouver)
        [ "$#" = 2 ] || { echo "BBIS REPETITION REFUS : trouver SORTIE.json"; exit 2; }
        F=$(lire_prive instances) || { echo "BBIS REPETITION REFUS : liste des instances illisible (lecture en échec)"; exit 2; }
        py_rep trouver "$F" "$2" --supprimer; exit $?;;
    depense)
        [ "$#" = 3 ] || { echo "BBIS REPETITION REFUS : depense CUMUL_USD PRIX_CARTE_USD_H"; exit 2; }
        py_rep depense "$2" "$3"; c=$?
        [ "$c" = 0 ] || echo "BBIS REPETITION : arrêt et destruction par l'identifiant : bash scripts/lancer_repetition_bbis_v1.sh detruire CREATION.json, puis bash scripts/lancer_repetition_bbis_v1.sh verifier-destruction CREATION.json 60480302"
        exit "$c";;
    verifier-destruction)
        [ "$#" = 3 ] || [ "$#" = 4 ] || { echo "BBIS REPETITION REFUS : verifier-destruction CREATION.json TEMOIN [LISTE.json]"; exit 2; }
        if [ "$#" = 4 ]; then py_rep absence "$2" "$3" "$4"; exit $?; fi
        F=$(lire_prive instances) || { echo "BBIS REPETITION ABSENCE NON PROUVEE : lecture de la liste des instances en échec : arrêt"; exit 2; }
        py_rep absence "$2" "$3" "$F" --supprimer; exit $?;;
    *) echo "BBIS REPETITION REFUS : sous-commande inconnue (credit, offre-depuis-recherche, offre, commande, relire, trouver, depense, detruire, verifier-destruction)"; exit 2;;
esac
