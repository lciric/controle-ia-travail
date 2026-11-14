#!/usr/bin/env bash
# Chaîne de session de l'étape B bis de T0.7, v1 (prereg/T0.7-etape-B-bis-v1.md, « Calcul et dépense », « Liste d'arrêt » ; ligne
# de GO GO-2026-11-14-09 : 40 USD, A100 seulement, une relance au plus, échéance 2026-11-22). Côté session seulement : aucune
# commande de ce script ne crée, n'arrête ni ne détruit d'instance ; il contrôle et IMPRIME les commandes, que la mère joue
# (préfixe GO_ID exigé par la garde de calcul ; destruction par l'identifiant, R10).
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie standard) :
#   offre OFFRE.json                 bornes du devis (A100 SXM4 80 Go, ≥ 16 cœurs, ≥ 128 000 Mo, ≥ 150 Go, stockage ≤ 0,08 USD/h,
#                                    étiquette bbis-t07-v1 ; aucune H200) ;
#   creation RACINE FEU RELANCES     SCELLEMENT-BBIS, CODE-BBIS, GO-BBIS au registre propre, feu écrit de la mère portant
#                                    GO-2026-11-14-09, une relance au plus, échéance, relance après le 21 novembre 12:00 UTC refusée ;
#   commande RACINE OFFRE_ID COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S FEU RELANCES IMAGE
#                                    imprime la commande de création (amorce scripts/amorce_bbis_v1.sh en base64, variables par leur
#                                    nom, jamais une valeur de clé) après les deux contrôles ci-dessus ; variables facultatives
#                                    VARIANTE=r1 et DECISION_VARIANTE=R-… (variante (r1), sur le mot de Lazar seulement) ;
#   depense CUMUL_USD PRIX_CARTE_USD_H   garde de dépense : cumul relevé + un quart d'heure de carte ≥ 39,5 USD → refus et commande
#                                    de destruction imprimée ;
#   detruire ID                      imprime la commande de destruction par l'identifiant (R10 ; jamais par motif).
set -uo pipefail
PY="${PYTHON_BBIS:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
GO_ID=GO-2026-11-14-09
ETIQUETTE=bbis-t07-v1
DISQUE=150
py_registre() { PYTHONPATH="$RACINE_CODE/src" "$PY" -m controle_ia.t07bbis.registre_bbis_v1 "$@"; }
case "${1:-}" in
    offre)
        [ "$#" = 2 ] || { echo "BBIS REFUS : offre OFFRE.json"; exit 2; }
        py_registre offre "$2"; exit $?;;
    creation)
        [ "$#" = 4 ] || { echo "BBIS REFUS : creation RACINE FEU RELANCES"; exit 2; }
        py_registre creation "$2" "$3" "$(date +%s)" "$4"; exit $?;;
    commande)
        [ "$#" = 12 ] || { echo "BBIS REFUS : commande RACINE OFFRE_ID COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S FEU RELANCES IMAGE"; exit 2; }
        RAC="$2"; OFFRE="$3"; COMMIT="$4"; BRC="$5"; RUN7B="$6"; BR7B="$7"; RUNB="$8"; ECH="$9"; FEU="${10}"; REL="${11}"; IMAGE="${12}"
        case "$OFFRE" in ''|*[!0-9]*) echo "BBIS REFUS : identifiant d'offre illisible"; exit 2;; esac
        case "$ECH" in ''|*[!0-9]*) echo "BBIS REFUS : échéance illisible"; exit 2;; esac
        case "$IMAGE" in *[!A-Za-z0-9._:/-]*|'') echo "BBIS REFUS : image illisible"; exit 2;; esac
        AMORCE_ESSAI_LOCAL=1 COMMIT="$COMMIT" BRANCHE_CODE="$BRC" RUN_7B="$RUN7B" BRANCHE_7B="$BR7B" RUN_BBIS="$RUNB" \
            ECHEANCE_UTC_S="$ECH" GO_ID="$GO_ID" VARIANTE="${VARIANTE:-}" DECISION_VARIANTE="${DECISION_VARIANTE:-}" \
            bash "$ICI/amorce_bbis_v1.sh" > /dev/null || { echo "BBIS REFUS : arguments refusés par l'amorce"; exit 2; }
        py_registre creation "$RAC" "$FEU" "$(date +%s)" "$REL" > /dev/null || { py_registre creation "$RAC" "$FEU" "$(date +%s)" "$REL"; exit 2; }
        B64=$(base64 -w 0 < "$ICI/amorce_bbis_v1.sh") || { echo "BBIS REFUS : amorce illisible"; exit 2; }
        EXTRA=""; [ -n "${VARIANTE:-}" ] && EXTRA=" -e VARIANTE=$VARIANTE -e DECISION_VARIANTE=$DECISION_VARIANTE"
        echo "BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce $(sha256sum < "$ICI/amorce_bbis_v1.sh" | cut -c1-16)) :"
        echo "GO_ID=$GO_ID vastai create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQUETTE --env \"-e COMMIT=$COMMIT -e BRANCHE_CODE=$BRC -e RUN_7B=$RUN7B -e BRANCHE_7B=$BR7B -e RUN_BBIS=$RUNB -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GO_ID$EXTRA -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$GH_TOKEN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce_bbis_v1.sh && bash /root/amorce_bbis_v1.sh\""
        exit 0;;
    depense)
        [ "$#" = 3 ] || { echo "BBIS REFUS : depense CUMUL_USD PRIX_CARTE_USD_H"; exit 2; }
        py_registre depense "$2" "$3"; c=$?
        [ "$c" = 0 ] || echo "BBIS : arrêt et destruction par l'identifiant (R10) : bash scripts/lancer_bbis_v1.sh detruire <ID>"
        exit "$c";;
    detruire)
        [ "$#" = 2 ] || { echo "BBIS REFUS : detruire ID"; exit 2; }
        case "$2" in ''|*[!0-9]*) echo "BBIS REFUS : identifiant illisible (destruction par l'identifiant seulement, R10)"; exit 2;; esac
        echo "GO_ID=$GO_ID vastai destroy instance $2"; exit 0;;
    *) echo "BBIS REFUS : sous-commande inconnue (offre, creation, commande, depense, detruire)"; exit 2;;
esac
