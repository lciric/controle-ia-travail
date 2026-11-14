#!/usr/bin/env bash
# Chaîne de session de la répétition sur carte de l'étape B bis de T0.7, v1 (mot de Lazar R-2802 : écart déclaré au texte scellé ;
# sous la ligne GO-2026-11-14-09 ; plafond de la répétition 3 USD ; une seule machine, A100 SXM4 80 Go comme la course). Côté
# session seulement : aucune commande de ce script ne crée, n'arrête ni ne détruit d'instance ; il contrôle et IMPRIME les
# commandes, que la mère joue (préfixe GO_ID exigé par la garde de calcul ; destruction par l'identifiant avec -y, R10, R-2789).
# Sous-commandes (codes : 0 accepté ; 2 refus, motif sur la sortie standard) :
#   offre OFFRE.json ID PRIX_USD_H   offre de la classe de la course (A100 SXM4 80 Go, ≥ 16 cœurs, ≥ 128 000 Mo, ≥ 60 Go, stockage
#                                    ≤ 0,08 USD/h, prix du jour ≤ 1,40 USD/h, étiquette bbis-t07-repetition-v1, clé `id` = ID) ;
#   commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE ECHEANCE_UTC_S PRIX_USD_H FEU IMAGE
#                                    imprime la commande de création après : l'offre ; le feu écrit de la mère portant
#                                    GO-2026-11-14-09 et R-2802 ; l'échéance (minuterie) dans ]maintenant, + 3 h] et telle que la carte
#                                    jusqu'à l'échéance, plus un quart d'heure, plus 0,40 USD (stockage, téléchargements), reste sous
#                                    3 USD ; COMMIT présent dans RACINE, portant l'amorce de la course, cette amorce de répétition
#                                    (égale à celle d'ici) et le script de la répétition (empreinte passée à l'instance) ; l'amorce
#                                    de répétition en essai local sur un dossier jetable (elle n'écrit rien) ;
#   depense CUMUL_USD PRIX_CARTE_USD_H   garde de dépense de la course à la coupure de 3 USD (cumul + un quart d'heure) ;
#   detruire ID                      imprime `GO_ID=… vastai destroy instance ID -y`, puis la vérification ; refus : identifiant non
#                                    numérique ou d'une autre session (58936096, 58936099, 58936100, 60480302, 60599797, 60670453) ;
#   verifier-destruction ID TEMOIN [LISTE.json]
#                                    absence de ID prouvée dans la liste des instances (`vastai show instances --raw`, lue sans
#                                    erreur, ou LISTE.json), témoin présent (60480302 ou 60670453) ; jamais par un code de sortie.
set -uo pipefail
PY="${PYTHON_BBIS:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
RACINE_CODE="$(cd "$ICI/.." && pwd)"
GO_ID=GO-2026-11-14-09
ETIQUETTE=bbis-t07-repetition-v1
DISQUE=60
py_rep() { PYTHONPATH="$RACINE_CODE/src" "$PY" "$ICI/repetition_carte_bbis_v1.py" "$@"; }
case "${1:-}" in
    offre)
        [ "$#" = 4 ] || { echo "BBIS REPETITION REFUS : offre OFFRE.json ID PRIX_USD_H"; exit 2; }
        py_rep offre "$2" "$3" "$4"; exit $?;;
    commande)
        [ "$#" = 10 ] || { echo "BBIS REPETITION REFUS : commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE ECHEANCE_UTC_S PRIX_USD_H FEU IMAGE"; exit 2; }
        RAC="$2"; FOFFRE="$3"; OFFRE="$4"; COMMIT="$5"; BRC="$6"; ECH="$7"; PRIX="$8"; FEU="$9"; IMAGE="${10}"
        case "$OFFRE" in ''|*[!0-9]*) echo "BBIS REPETITION REFUS : identifiant d'offre illisible"; exit 2;; esac
        case "$ECH" in ''|*[!0-9]*) echo "BBIS REPETITION REFUS : échéance illisible"; exit 2;; esac
        case "$IMAGE" in *[!A-Za-z0-9._:/-]*|'') echo "BBIS REPETITION REFUS : image illisible"; exit 2;; esac
        case "$BRC" in *[!A-Za-z0-9._/-]*|'') echo "BBIS REPETITION REFUS : branche illisible"; exit 2;; esac
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
        echo "BBIS REPETITION COMMANDE (à jouer par la mère, après le feu écrit ; amorce $(sha256sum < "$ICI/amorce_repetition_bbis_v1.sh" | cut -c1-16), script $(printf '%s' "$SH" | cut -c1-16)) :"
        echo "GO_ID=$GO_ID vastai create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQUETTE --env \"-e COMMIT=$COMMIT -e BRANCHE_CODE=$BRC -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GO_ID -e SCRIPT_SHA256=$SH -e GH_TOKEN=\$GH_TOKEN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce_repetition_bbis_v1.sh && bash /root/amorce_repetition_bbis_v1.sh\""
        exit 0;;
    depense)
        [ "$#" = 3 ] || { echo "BBIS REPETITION REFUS : depense CUMUL_USD PRIX_CARTE_USD_H"; exit 2; }
        py_rep depense "$2" "$3"; c=$?
        [ "$c" = 0 ] || echo "BBIS REPETITION : arrêt et destruction par l'identifiant : bash scripts/lancer_repetition_bbis_v1.sh detruire <ID>, puis bash scripts/lancer_repetition_bbis_v1.sh verifier-destruction <ID> <TEMOIN>"
        exit "$c";;
    detruire)
        [ "$#" = 2 ] || { echo "BBIS REPETITION REFUS : detruire ID"; exit 2; }
        py_rep identifiant "$2" > /dev/null || { py_rep identifiant "$2"; exit 2; }
        echo "GO_ID=$GO_ID vastai destroy instance $2 -y"
        echo "BBIS REPETITION PUIS (jamais juger la destruction par le code de sortie) : bash scripts/lancer_repetition_bbis_v1.sh verifier-destruction $2 60480302"
        exit 0;;
    verifier-destruction)
        [ "$#" = 3 ] || [ "$#" = 4 ] || { echo "BBIS REPETITION REFUS : verifier-destruction ID TEMOIN [LISTE.json]"; exit 2; }
        case "$2$3" in ''|*[!0-9]*) echo "BBIS REPETITION ABSENCE NON PROUVEE : identifiants illisibles : arrêt"; exit 2;; esac
        if [ "$#" = 4 ]; then LISTE="$4"
        else
            DL=$(mktemp -d) || { echo "BBIS REPETITION ABSENCE NON PROUVEE : dossier de la liste impossible : arrêt"; exit 2; }
            LISTE="$DL/instances.json"
            "${VASTAI_BBIS:-vastai}" show instances --raw < /dev/null > "$LISTE" 2> "$DL/instances.err"; c=$?
            [ "$c" = 0 ] || { echo "BBIS REPETITION ABSENCE NON PROUVEE : lecture de la liste des instances en échec (code $c, $DL/instances.err) : arrêt"; exit 2; }
            echo "BBIS REPETITION liste des instances gardée : $LISTE"
        fi
        py_rep absence "$2" "$3" "$LISTE"; exit $?;;
    *) echo "BBIS REPETITION REFUS : sous-commande inconnue (offre, commande, depense, detruire, verifier-destruction)"; exit 2;;
esac
