#!/usr/bin/env bash
# Chaîne de session de l'étape B bis de T0.7, v2 (la v1, qui passe l'amorce v2 : marche v2, contrôle carte-processeur
# aux deux horizons, R-2917 ; la v1 reste, R12) (prereg/T0.7-etape-B-bis-v1.md, « Calcul et dépense », « Liste d'arrêt » ; ligne
# de GO GO-2026-11-14-09 : 40 USD, A100 seulement, une relance au plus, échéance 2026-11-22). Côté session seulement : aucune
# commande de ce script ne crée, n'arrête ni ne détruit d'instance ; il contrôle et IMPRIME les commandes, que la mère joue
# (préfixe GO_ID exigé par la garde de calcul ; destruction par l'identifiant, R10).
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie standard) :
#   offre-depuis-recherche RECHERCHE.json ID OFFRE.json
#                                    OFFRE.json construit par programme depuis la sortie de la recherche (même fonction que la
#                                    répétition, `registre_bbis_v1.lire_offre_de_recherche`, garde `cuda_max_good` comprise),
#                                    puis les bornes de `offre` ; jamais retapé, jamais réécrit (R12) ;
#   offre OFFRE.json                 bornes du devis (A100 SXM4 80 Go, ≥ 16 cœurs, ≥ 128 000 Mo, ≥ 150 Go, stockage ≤ 0,08 USD/h,
#                                    étiquette bbis-t07-v1 ; aucune H200 ; version CUDA servie par l'hôte, clé `cuda_max_good`
#                                    recopiée telle quelle de `vastai search offers --raw`, ≥ 13.0, celle de la roue torch de
#                                    requirements-gpu.txt ; clé absente ou illisible : refus) ; recherche (filtre de l'outil, la
#                                    garde locale décide) : ( umask 077; vastai search offers 'gpu_name=A100_SXM4 num_gpus=1
#                                    cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0' -o 'dph_total'
#                                    --raw > RECHERCHE.json ) ;
#   creation RACINE FEU RELANCES     SCELLEMENT-BBIS, CODE-BBIS, GO-BBIS au registre propre, feu écrit de la mère portant
#                                    GO-2026-11-14-09, une relance au plus, échéance, relance après le 21 novembre 12:00 UTC refusée ;
#   commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S FEU RELANCES IMAGE
#                                    imprime la commande de création (amorce scripts/amorce_bbis_v2.sh en base64, variables par leur
#                                    nom, jamais une valeur de clé) après : l'offre décrite dans OFFRE.json, d'identifiant OFFRE_ID
#                                    (clé `id`), dans les bornes (correction m5) ; la branche de sortie de l'amorce (BR_SORTIE)
#                                    absente du dépôt distant (`git ls-remote` sur `origin` de RACINE, lecture seule) ; l'amorce en essai local sur un dossier jetable
#                                    (correction m5 ; elle n'écrit rien) ; la garde de création ; le commit de la fiche de
#                                    CODE-BBIS ancêtre de COMMIT dans RACINE (correction B1) ; variables facultatives
#                                    VARIANTE=r1 et DECISION_VARIANTE=R-… (variante (r1), sur le mot de Lazar seulement) ;
#   depense CUMUL_USD PRIX_CARTE_USD_H   garde de dépense : cumul relevé + un quart d'heure de carte ≥ 39,5 USD → refus et commande
#                                    de destruction imprimée ;
#   detruire ID                      imprime la commande de destruction par l'identifiant (R10 ; jamais par motif), **avec -y**
#                                    (R-2789 : sans -y, `vastai` 1.11.0 demande [y/N], abandonne et rend 0), puis la vérification ;
#                                    refus : identifiant non numérique ou d'une autre session ;
#   verifier-destruction ID TEMOIN [LISTE.json]
#                                    la destruction n'est jamais jugée par un code de sortie : absence de ID prouvée dans la
#                                    liste des instances (`vastai show instances --raw`, lue sans erreur, ou LISTE.json), une
#                                    instance témoin TEMOIN y étant présente ; sinon « absence non prouvée », code 2 (arrêt et
#                                    compte rendu ; destruction et vérification à refaire). Lecture seule : rien n'est détruit.
set -uo pipefail
PY="${PYTHON_BBIS:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
GO_ID=GO-2026-11-14-09
ETIQUETTE=bbis-t07-v1
DISQUE=150
# >>> branche-de-sortie (même texte dans les deux lanceurs de B bis ; joué par les essais)
branche_de_sortie_neuve() {  # $1 = racine (dépôt de la mère, distant `origin`) ; $2 = amorce : 0 si la branche de sortie de
    # l'amorce est absente du dépôt distant (prouvé par `git ls-remote`, lecture seule) ; sinon motif sur la sortie, code 2
    local br url o c
    br=$(sed -n 's/^BR_SORTIE=\([A-Za-z0-9._/-][A-Za-z0-9._/-]*\)$/\1/p' "$2" 2> /dev/null)
    [ "$(printf '%s' "$br" | grep -c '^')" = 1 ] || { echo "branche de sortie de l'amorce illisible ou multiple (BR_SORTIE=…)"; return 2; }
    url=$(sed -n 's/^DEPOT_URL_OFFICIEL=\(.*\)$/\1/p' "$2" 2> /dev/null)
    [ "$(printf '%s' "$url" | grep -c '^')" = 1 ] || { echo "dépôt de l'amorce illisible ou multiple (DEPOT_URL_OFFICIEL=…)"; return 2; }
    o=$(git -C "$1" remote get-url origin 2> /dev/null) || { echo "dépôt distant « origin » absent de $1"; return 2; }
    url=${url%/}; url=${url%.git}; o=${o%/}; o=${o%.git}
    [ "${o##*/}" = "${url##*/}" ] && [ "$(basename "$(dirname "$o")")" = "$(basename "$(dirname "$url")")" ] \
        || { echo "« origin » de $1 n'est pas le dépôt de l'amorce ($(basename "$(dirname "$url")")/${url##*/})"; return 2; }
    git -C "$1" ls-remote --exit-code origin "refs/heads/$br" > /dev/null 2>&1; c=$?
    case "$c" in
        2) return 0;;
        0) echo "branche de sortie $br présente sur le dépôt distant (R12) : la passe s'arrêterait sans trace ; nouveau nom exigé"; return 2;;
        *) echo "dépôt distant injoignable (git ls-remote, code $c) : absence de la branche de sortie $br non prouvée"; return 2;;
    esac; }
# <<< branche-de-sortie
py_registre() { PYTHONPATH="$RACINE_CODE/src" "$PY" -m controle_ia.t07bbis.registre_bbis_v1 "$@"; }
case "${1:-}" in
    offre-depuis-recherche)
        [ "$#" = 4 ] || { echo "BBIS REFUS : offre-depuis-recherche RECHERCHE.json ID OFFRE.json"; exit 2; }
        py_registre offre-depuis-recherche "$2" "$3" "$4"; exit $?;;
    offre)
        [ "$#" = 2 ] || { echo "BBIS REFUS : offre OFFRE.json"; exit 2; }
        py_registre offre "$2"; exit $?;;
    creation)
        [ "$#" = 4 ] || { echo "BBIS REFUS : creation RACINE FEU RELANCES"; exit 2; }
        py_registre creation "$2" "$3" "$(date +%s)" "$4"; exit $?;;
    commande)
        [ "$#" = 13 ] || { echo "BBIS REFUS : commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S FEU RELANCES IMAGE"; exit 2; }
        RAC="$2"; FOFFRE="$3"; OFFRE="$4"; COMMIT="$5"; BRC="$6"; RUN7B="$7"; BR7B="$8"; RUNB="$9"; ECH="${10}"; FEU="${11}"; REL="${12}"; IMAGE="${13}"
        case "$OFFRE" in ''|*[!0-9]*) echo "BBIS REFUS : identifiant d'offre illisible"; exit 2;; esac
        case "$ECH" in ''|*[!0-9]*) echo "BBIS REFUS : échéance illisible"; exit 2;; esac
        case "$IMAGE" in *[!A-Za-z0-9._:/-]*|'') echo "BBIS REFUS : image illisible"; exit 2;; esac
        py_registre offre "$FOFFRE" "$OFFRE" > /dev/null || { py_registre offre "$FOFFRE" "$OFFRE"; exit 2; }
        RAC_ESSAI=$(mktemp -d) || { echo "BBIS REFUS : dossier jetable de l'essai local impossible"; exit 2; }
        AMORCE_ESSAI_LOCAL=1 RACINE_AMORCE="$RAC_ESSAI" COMMIT="$COMMIT" BRANCHE_CODE="$BRC" RUN_7B="$RUN7B" BRANCHE_7B="$BR7B" \
            RUN_BBIS="$RUNB" ECHEANCE_UTC_S="$ECH" GO_ID="$GO_ID" VARIANTE="${VARIANTE:-}" DECISION_VARIANTE="${DECISION_VARIANTE:-}" \
            bash "$ICI/amorce_bbis_v2.sh" > /dev/null; c=$?
        rmdir "$RAC_ESSAI" || { echo "BBIS REFUS : l'amorce en essai local a écrit dans $RAC_ESSAI"; exit 2; }
        [ "$c" = 0 ] || { echo "BBIS REFUS : arguments refusés par l'amorce"; exit 2; }
        py_registre creation "$RAC" "$FEU" "$(date +%s)" "$REL" > /dev/null || { py_registre creation "$RAC" "$FEU" "$(date +%s)" "$REL"; exit 2; }
        py_registre ancetre "$RAC" "$COMMIT" > /dev/null || { py_registre ancetre "$RAC" "$COMMIT"; exit 2; }
        M=$(branche_de_sortie_neuve "$RAC" "$ICI/amorce_bbis_v2.sh") || { echo "BBIS REFUS : $M"; exit 2; }
        B64=$(base64 -w 0 < "$ICI/amorce_bbis_v2.sh") || { echo "BBIS REFUS : amorce illisible"; exit 2; }
        EXTRA=""; [ -n "${VARIANTE:-}" ] && EXTRA=" -e VARIANTE=$VARIANTE -e DECISION_VARIANTE=$DECISION_VARIANTE"
        echo "BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce $(sha256sum < "$ICI/amorce_bbis_v2.sh" | cut -c1-16)) :"
        echo "GO_ID=$GO_ID vastai create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQUETTE --env \"-e COMMIT=$COMMIT -e BRANCHE_CODE=$BRC -e RUN_7B=$RUN7B -e BRANCHE_7B=$BR7B -e RUN_BBIS=$RUNB -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GO_ID$EXTRA -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$GH_TOKEN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce_bbis_v2.sh && bash /root/amorce_bbis_v2.sh\""
        exit 0;;
    depense)
        [ "$#" = 3 ] || { echo "BBIS REFUS : depense CUMUL_USD PRIX_CARTE_USD_H"; exit 2; }
        py_registre depense "$2" "$3"; c=$?
        [ "$c" = 0 ] || echo "BBIS : arrêt et destruction par l'identifiant (R10) : bash scripts/lancer_bbis_v2.sh detruire <ID>, puis bash scripts/lancer_bbis_v2.sh verifier-destruction <ID> <TEMOIN>"
        exit "$c";;
    detruire)
        [ "$#" = 2 ] || { echo "BBIS REFUS : detruire ID"; exit 2; }
        case "$2" in ''|*[!0-9]*) echo "BBIS REFUS : identifiant illisible (destruction par l'identifiant seulement, R10)"; exit 2;; esac
        py_registre identifiant "$2" > /dev/null || { py_registre identifiant "$2"; exit 2; }
        echo "GO_ID=$GO_ID vastai destroy instance $2 -y"
        echo "BBIS PUIS (jamais juger la destruction par le code de sortie) : bash scripts/lancer_bbis_v2.sh verifier-destruction $2 <TEMOIN>"
        exit 0;;
    verifier-destruction)
        [ "$#" = 3 ] || [ "$#" = 4 ] || { echo "BBIS REFUS : verifier-destruction ID TEMOIN [LISTE.json]"; exit 2; }
        case "$2$3" in ''|*[!0-9]*) echo "BBIS ABSENCE NON PROUVEE : identifiants illisibles : arrêt"; exit 2;; esac
        if [ "$#" = 4 ]; then LISTE="$4"
        else
            DL=$(mktemp -d) || { echo "BBIS ABSENCE NON PROUVEE : dossier de la liste impossible : arrêt"; exit 2; }
            LISTE="$DL/instances.json"
            "${VASTAI_BBIS:-vastai}" show instances --raw < /dev/null > "$LISTE" 2> "$DL/instances.err"; c=$?
            [ "$c" = 0 ] || { echo "BBIS ABSENCE NON PROUVEE : lecture de la liste des instances en échec (code $c, $DL/instances.err) : arrêt"; exit 2; }
            echo "BBIS liste des instances gardée : $LISTE"
        fi
        py_registre absence "$2" "$3" "$LISTE"; exit $?;;
    *) echo "BBIS REFUS : sous-commande inconnue (offre-depuis-recherche, offre, creation, commande, depense, detruire, verifier-destruction)"; exit 2;;
esac
