#!/usr/bin/env bash
# Surveillance de l'instance de P3-bis (témoin positif planté ; GO-2026-11-02-29), v1, depuis la session de pilotage, sans
# jamais afficher de jeton. Texte : brouillon 9 (eb65773f…), « Liste d'arrêt » et « Ce que le code et la chaîne doivent
# changer », point 6 (i) ; contre-lecture du code (7a074ad1…), point 6. Déclinée de docs/procedures/P3-premier-test-v2/
# surveiller_p3_v1.sh (P3) sous un nom neuf (R12). Ce qui change contre P3 :
#   - AUCUN arrêt à durée : le motif PLAFOND (création + 22 200 s) est retiré ; un run lent mais vivant n'est jamais
#     arrêté ; l'absence de ligne PROGRES nouvelle pendant ALERTE_SANS_PROGRES_S (deux heures, depuis la création ou la
#     dernière ligne PROGRES nouvelle) écrit une ALERTE (sortie standard et alertes.txt), répétée toutes les deux heures,
#     sans arrêt ni sortie ;
#   - chaque motif de fin ARRÊTE L'INSTANCE PAR SON IDENTIFIANT (R10 : « vastai stop instance <id> », jamais par motif),
#     après la garde du module commun (l'identifiant est celui de l'instance créée par le lanceur, seule ligne
#     « instance <id> » des traces, et n'est pas dans ARRETEES_TOLEREES) ; l'arrêt est écrit dans arrets-a-consigner.txt
#     (ligne pour registres/arrets.md, consignée par la session) ; aucune destruction ici (detruire_p3bis_v1.sh, après la
#     récupération vérifiée) ;
#   - motifs (module commun, sous-commande « motif », puis l'état et la dépense) :
#       FIN               ligne « AMORCE … fin, code N » (N ≠ 5, run complet ou arrêt consigné par l'instance) ;
#       GARDER            fin, code 5, ou ligne « SECOND PAQUET EN ÉCHEC » : instance arrêtée, GARDÉE, jamais détruite
#                         jusqu'à la récupération du paquet refait (fichier instance-gardee écrit ; detruire_p3bis_v1.sh
#                         refuse) ;
#       PROCESSUS MORT    fin, avec « run : processus P fini, code C » (C ≠ 0) sans « run complet » : erreur de chaîne si la
#                         récupération ne trouve ni resume.json ni arret.json ; la consignation et la poussée de
#                         l'instance ne sont jamais coupées (le motif est lu à la fin de l'amorce) ;
#       ÉCHEC D'AMORCE    ligne « AMORCE : … » ;
#       REDÉMARRAGE       plus d'une ligne « AMORCE <date> : commit » au relevé cumulatif ;
#       ÉTAT TERMINAL     instance arrêtée ou hors ligne, vue deux fois de suite ;
#       DÉPENSE           dépense cumulée de la course projetée au prochain relevé ≥ 80 USD (dépense antérieure en
#                         argument, toutes tentatives et relances comprises ; prix de l'offre × durée depuis la création ;
#                         téléchargement relevé ; bornes écrites si illisibles : module commun, « depense ») ;
#   - relevé de la dépense à chaque tour (depenses.txt).
# Gardé de P3 : jetons exigés pour le masquage (R5) ; journal gardé comme dernier relevé seulement si l'appel a réussi ;
# relevé cumulatif AMORCE et PROGRES jamais tronqué (progres.txt) ; outil de location exigé sur le PATH.
#
#   surveiller_p3bis_v1.sh <identifiant> <dossier des traces du lancement> <dépense antérieure en USD> <dossier de sortie>
#
# Interroge l'état et le journal toutes les INTERVALLE secondes (120 par défaut, entier de 0 à 600). Sort en écrivant le
# motif sur sa dernière ligne : code 0 si l'instance est arrêtée par son identifiant (état relu écrit) ; code 1 si l'arrêt
# a échoué (la session arrête l'instance par son identifiant, à la main, et consigne). Code 2 : usage, jetons absents,
# traces illisibles, identifiant autre que celui du lancement, dossier de sortie existant (R12), outil introuvable.
set -uo pipefail
ALERTE_SANS_PROGRES_S=7200                       # deux heures sans ligne PROGRES nouvelle : alerte, jamais arrêt
ID=${1:-}; T=${2:-}; ANTERIEURE=${3:-}; D=${4:-}
INTERVALLE=${INTERVALLE:-120}
H=$(dirname "$(realpath "$0")")
VERIF=$H/verifications_p3bis_v1.py
[[ "$ID" =~ ^[0-9]+$ && -n "$T" && "$ANTERIEURE" =~ ^[0-9]+(\.[0-9]+)?$ && -n "$D" ]] \
    || { echo "usage : surveiller_p3bis_v1.sh <identifiant> <dossier des traces du lancement> <dépense antérieure en USD> <dossier neuf>"; exit 2; }
[[ "$INTERVALLE" =~ ^[0-9]+$ ]] && [ "$INTERVALLE" -le 600 ] || { echo "INTERVALLE : entier de 0 à 600 secondes"; exit 2; }
J_HF=${HF_TOKEN:-}; J_GH=${CONTROLE_IA_GITHUB_TOKEN:-}
[ "${#J_HF}" -ge 8 ] && [ "${#J_GH}" -ge 8 ] \
    || { echo "jetons HF_TOKEN et CONTROLE_IA_GITHUB_TOKEN absents ou trop courts : masquage impossible, surveillance refusée"; exit 2; }
unset J_HF J_GH
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
command -v vastai > /dev/null || { echo "outil de location introuvable sur le PATH : surveillance aveugle, arrêt"; exit 2; }
[ -f "$VERIF" ] || { echo "module commun $VERIF absent"; exit 2; }
L="$T/lancement.txt"
[ -f "$L" ] || { echo "traces du lancement illisibles ($L absent)"; exit 2; }
G=$(python3 -I "$VERIF" identifiant "$ID" "$L" 2>&1) || { echo "identifiant : $(printf '%s\n' "$G" | tail -1)"; exit 2; }
une() {   # valeur de la seule ligne « <clé> <valeur> » de lancement.txt (vide si absente ou en double)
    local v
    v=$(sed -n "s/^$1 \([^ ]*\)$/\1/p" "$L")
    [ "$(printf '%s\n' "$v" | grep -c .)" = 1 ] && printf '%s' "$v"
}
CREATION=$(une creation)
CHOISIE=$(sed -n 's/^offre choisie : \([0-9][0-9]*\) (\([0-9.][0-9.]*\) USD\/h).*/\2/p' "$L")
[[ "$CREATION" =~ ^[0-9]+$ ]] && [ "$(printf '%s\n' "$CHOISIE" | grep -c .)" = 1 ] \
    || { echo "traces du lancement illisibles (création ou offre choisie)"; exit 2; }
mkdir -p "$D" && : > "$D/progres.txt" && echo "$CREATION" > "$D/dernier-progres.txt" || exit 2
masquer() {
    python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) > 6:
        t = t.replace(v, "***")
sys.stdout.write(t)'
}
arreter() {   # $1 motif, $2 détail ; arrêt par l'identifiant (R10), jamais par motif ; aucune destruction
    local m=$1 detail=$2 r e c=0 k
    python3 -I "$VERIF" identifiant "$ID" "$L" > /dev/null 2>&1 || { echo "$m : $detail ; ARRÊT REFUSÉ PAR LA GARDE (identifiant)"; exit 1; }
    [ "$m" = GARDER ] && printf '%s\n' "$detail" > "$D/instance-gardee"
    r=$(vastai stop instance "$ID" 2>&1 | masquer) || c=$?
    printf '%s arrêt de %s demandé par son identifiant (motif %s) : code %s ; %s\n' "$(date -u +%FT%TZ)" "$ID" "$m" "$c" "$(printf '%s' "$r" | tr '\n' ' ' | cut -c1-200)" >> "$D/arret.txt"
    e=""
    for k in 1 2 3; do
        e=$(vastai show instance "$ID" --raw 2>&1 | python3 -I "$VERIF" etat | masquer)
        case "$e" in *"cur_state=stopped"*|*"actual_status=exited"*|*"actual_status=stopped"*) break ;; esac
        sleep "$INTERVALLE"
    done
    printf '| %s | P3-bis, %s | instance %s arrêtée par son identifiant (R10), motif %s : %s ; état relu : %s |\n' \
        "$(date -u +%FT%TZ)" "GO-2026-11-02-29" "$ID" "$m" "$detail" "$e" >> "$D/arrets-a-consigner.txt"
    if [ "$c" != 0 ]; then
        echo "$m : $detail ; ARRÊT DE L'INSTANCE $ID EN ÉCHEC (code $c) : l'arrêter à la main par son identifiant (R10), consigner"; exit 1
    fi
    case "$m" in
        GARDER) echo "$m : $detail ; instance $ID arrêtée par son identifiant (R10), GARDÉE, jamais détruite ; état relu : $e" ;;
        *)      echo "$m : $detail ; instance $ID arrêtée par son identifiant (R10) ; état relu : $e" ;;
    esac
    exit 0
}
terminal=0; derniere_alerte=0; TAB=$'\t'
echo "surveillance de $ID : création $CREATION, prix de l'offre $CHOISIE USD/h, dépense antérieure $ANTERIEURE USD, intervalle $INTERVALLE s ; aucun plafond de durée ; alerte après $ALERTE_SANS_PROGRES_S s sans PROGRES" > "$D/surveillance.txt"
while true; do
    maintenant=$(date -u +%s)
    vastai show instance "$ID" --raw 2>&1 | masquer > "$D/etat-tour.json"
    e=$(python3 -I "$VERIF" etat < "$D/etat-tour.json")
    echo "$(date -u +%FT%TZ) $e" >> "$D/etats.txt"
    if vastai logs "$ID" --tail 20000 > "$D/journal-tour.txt" 2>&1; then
        masquer < "$D/journal-tour.txt" > "$D/journal-dernier.txt"
        nouveau=0
        while IFS= read -r ligne; do
            grep -qxF -- "$ligne" "$D/progres.txt" && continue
            printf '%s\n' "$ligne" >> "$D/progres.txt"
            case "$ligne" in PROGRES*) nouveau=1 ;; esac
        done < <(grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt")
        [ "$nouveau" = 1 ] && echo "$maintenant" > "$D/dernier-progres.txt"
    else
        echo "$(date -u +%FT%TZ) journal illisible (appel en échec) : dernier relevé gardé" >> "$D/etats.txt"
    fi
    rm -f "$D/journal-tour.txt"
    [ -f "$D/journal-dernier.txt" ] && J="$D/journal-dernier.txt" || J=-
    m=$(python3 -I "$VERIF" motif "$J" "$D/progres.txt") || { echo "motif illisible (module commun) : surveillance arrêtée sans arrêt de l'instance"; exit 1; }
    [ "${m%%"$TAB"*}" = AUCUN ] || arreter "${m%%"$TAB"*}" "${m#*"$TAB"}"
    case "$e" in
        *"actual_status=exited"*|*"actual_status=offline"*|*"cur_state=stopped"*) terminal=$((terminal + 1)) ;;
        *) terminal=0 ;;
    esac
    [ "$terminal" -ge 2 ] && arreter "ÉTAT TERMINAL" "$e"
    c=0
    dep=$(python3 -I "$VERIF" depense "$CREATION" "$maintenant" "$CHOISIE" "$ANTERIEURE" "$INTERVALLE" < "$D/etat-tour.json") || c=$?
    echo "$(date -u +%FT%TZ) $dep" >> "$D/depenses.txt"
    case "$c" in
        0) ;;
        3) arreter "DÉPENSE" "$dep" ;;
        *) echo "dépense illisible (module commun, code $c) : surveillance arrêtée sans arrêt de l'instance ; $dep"; exit 1 ;;
    esac
    dernier=$(cat "$D/dernier-progres.txt")
    if [ $((maintenant - dernier)) -ge "$ALERTE_SANS_PROGRES_S" ] && [ $((maintenant - derniere_alerte)) -ge "$ALERTE_SANS_PROGRES_S" ]; then
        a="ALERTE : $(date -u +%FT%TZ) aucune ligne PROGRES nouvelle depuis $((maintenant - dernier)) s (deux heures au moins) ; aucun arrêt (run lent mais vivant jamais arrêté) ; à lire par la session"
        echo "$a" | tee -a "$D/alertes.txt"
        derniere_alerte=$maintenant
    fi
    sleep "$INTERVALLE"
done
