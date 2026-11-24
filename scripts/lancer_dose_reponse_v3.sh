#!/usr/bin/env bash
# [v3 ; nom neuf, R12 : la v2 reste telle quelle. Change seulement l'amorce citée, `scripts/amorce_instance_dose_reponse_v3.sh`
# (extraction du texte de désignation pour le critère 3) ; rien d'autre.]
# [v2, après la contre-lecture 1 du code ; nom neuf, R12 : la v1 reste telle quelle. Changent : l'amorce citée
# (`scripts/amorce_instance_dose_reponse_v2.sh`) ; `controles` joue `controles_v2` (configuration égale à celle que reconstruit
# le code, ligne CODE citant le commit du code) ET, avant toute création (CL-04), la forme stricte de la pièce jointe et le
# rapport des longueurs en jetons des huit consignes (tokeniseur seul de l'agent, à la révision figée ; seuls des comptes sont
# imprimés) ; `controles` et `creation` refusent tout jour après le 12 décembre 2026 (dernier jour de création du devis, CL-11).]
# Lanceur de session de la course de dose–réponse de l'organisme à consigne cachée, v1. Copie adaptée de
# `scripts/lancer_t08_v1.sh` (qui reste tel quel, R12) : mêmes sous-commandes, mêmes codes (0 ; 2 échec ; 3 nœud ; 4 refus
# ou création incertaine ; 5 offre refusée à la création). Changent : la branche de lancement (`DR_BRANCHE_LANCEMENT`, dont
# la tête est le commit de lancement : configuration scellée, banque, lignes du registre ; code égal au commit cité par la
# configuration, `commit_code`), l'amorce `scripts/amorce_instance_dose_reponse_v1.sh` citée par son empreinte
# (`DR_AMORCE_SHA256`), les contrôles avant dépense joués dans un arbre de travail du commit de lancement
# (`dose_reponse.controles_v1`), le plafond (90 USD cumulés sur toutes les tentatives) et l'alerte à 72 USD, la branche de
# sortie (`calcul/dose-reponse-v1` par défaut, une neuve par tentative), la reprise facultative (`DR_REPRISE_BRANCHE`,
# `DR_REPRISE_RUN`) et les essais de chaîne facultatifs (`DR_ESSAIS`, seize au plus). La session ne loue rien par ce script :
# elle vérifie puis IMPRIME la commande littérale de création, revérifiée par la garde de calcul.
# Usage :
#   GO_ID=… DR_BRANCHE_LANCEMENT=… DR_AMORCE_SHA256=… bash scripts/lancer_dose_reponse_v3.sh controles DOSSIER_NEUF [JOUR]
#   GO_ID=… bash scripts/lancer_dose_reponse_v3.sh creation auto course DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]
#   bash scripts/lancer_dose_reponse_v3.sh apres-creation FICHIER CODE DOSSIER
#   bash scripts/lancer_dose_reponse_v3.sh surveillance ID DOSSIER [FACTURE_USD]
#   GO_ID=… bash scripts/lancer_dose_reponse_v3.sh --verifier-go-seulement CONFIG.json [DEPENSE_ANTERIEURE] [JOUR]
# Variables : CONTROLE_IA_GITHUB_TOKEN (ou _2) et HF_TOKEN par leur nom seulement ; DR_DEPOT, DR_PREREG, DR_CONFIG,
# DR_BRANCHE, DR_REGISTRE_GO, DR_IMAGE, VAST, INTERVALLE.
set -uo pipefail
QUOI="${1:?controles, creation, apres-creation, surveillance ou --verifier-go-seulement}"
DEPOT="${DR_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"
P="${DR_PREREG:-prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md}"
A=scripts/amorce_instance_dose_reponse_v3.sh
BRANCHE="${DR_BRANCHE:-calcul/dose-reponse-v1}"
CONFIG="${DR_CONFIG:-prereg/T0.6-dose-reponse-configuration-course-v1.json}"
GO_ID_ENV="${GO_ID:-}"
REG="${DR_REGISTRE_GO:-$DEPOT/registres/go.md}"
MOTIF_GO='^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$'
PLAFOND=90; COMPTE_RENDU=72
IMAGE="${DR_IMAGE:-python:3.11-bookworm}"
VAST="${VAST:-vastai}"
SESSION="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v2; sys.exit(session_v2.main(sys.argv[1:]))"
SESSION3="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
SESSION7="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v12; sys.exit(session_v12.main(sys.argv[1:]))"
SESSION8="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.lancement_t08 import session_v1; sys.exit(session_v1.main(sys.argv[1:]))"
masquer() { python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) >= 8:
        t = t.replace(v, "***")
sys.stdout.write(t)'; }
vast_masque() { local sortie="$1"; shift
    "$@" 2>/dev/null | masquer > "$sortie.tmp"; local ps=("${PIPESTATUS[@]}")
    if [ "${ps[1]:-1}" != 0 ]; then rm -f "$sortie.tmp"; return 121; fi
    mv -f "$sortie.tmp" "$sortie"; return "${ps[0]}"; }
jeton_gh_nom() { if [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN; elif [ -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN_2; else return 1; fi; }
commit_s() { git -C "$DEPOT" log origin/main --diff-filter=A -1 --format=%H -- "$P.sha256"; }
champ() { sed -n "s/^$1 //p" "$2" | tail -1; }
cle_config() { python3 -I -B -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8"))
for k in sys.argv[2].split("."):
    c = c[k]
print(c)' "$1" "$2"; }
case "$QUOI" in
controles)
    D=$(realpath -m "${2:?dossier neuf}"); JOUR="${3:-$(date -u +%F)}"
    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible (GO_ID=GO-AAAA-MM-JJ-NN) : pas de création"; exit 2; }
    BL="${DR_BRANCHE_LANCEMENT:?DR_BRANCHE_LANCEMENT : branche dont la tête est le commit de lancement}"; AS="${DR_AMORCE_SHA256:?DR_AMORCE_SHA256 : empreinte de l amorce, celle de la ligne CODE}"
    [[ "$AS" =~ ^[0-9a-f]{64}$ ]] || { echo "DR_AMORCE_SHA256 : 64 caractères hexadécimaux"; exit 2; }
    mkdir -p "$D"
    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/main:refs/remotes/origin/main" || { echo "fetch de main impossible"; exit 2; }
    S=$(commit_s); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit de scellement de $P introuvable sur origin/main"; exit 2; }
    git -C "$DEPOT" show "$S:$P" > "$D/prereg-S.md" || { echo "texte absent de S"; exit 2; }
    [ "$(sha256sum < "$D/prereg-S.md" | cut -d' ' -f1)" = "$(git -C "$DEPOT" show "$S:$P.sha256" | cut -d' ' -f1)" ] || { echo "sceau de $P non conforme à S"; exit 2; }
    timeout 300 git -C "$DEPOT" fetch -q origin "refs/heads/$BL:refs/remotes/origin/$BL" || { echo "branche de lancement $BL introuvable"; exit 2; }
    L=$(git -C "$DEPOT" rev-parse "refs/remotes/origin/$BL^{commit}") || { echo "branche de lancement illisible"; exit 2; }
    [ "$(git -C "$DEPOT" rev-parse "$L:$P")" = "$(git -C "$DEPOT" rev-parse "$S:$P")" ] || { echo "texte du commit de lancement ≠ texte scellé de S"; exit 2; }
    git -C "$DEPOT" show "$L:$CONFIG" > "$D/config.json" 2>/dev/null || { echo "configuration $CONFIG absente du commit de lancement"; exit 2; }
    [ "$(sha256sum < "$D/config.json" | cut -d' ' -f1)" = "$(git -C "$DEPOT" show "$L:$CONFIG.sha256" 2>/dev/null | cut -d' ' -f1)" ] || { echo "configuration non scellée au commit de lancement"; exit 2; }
    COMMIT=$(cle_config "$D/config.json" commit_code) && [[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "commit_code illisible dans la configuration"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$COMMIT" "$L" || { echo "commit du code $COMMIT non ancêtre du commit de lancement $L"; exit 2; }
    git -C "$DEPOT" diff --quiet "$COMMIT" "$L" -- src scripts tests .claude pyproject.toml 'requirements-*.txt' || { echo "code du commit de lancement ≠ code du commit cité $COMMIT"; exit 2; }
    git -C "$DEPOT" show "$L:$A" > "$D/amorce.sh" || { echo "amorce absente du commit de lancement"; exit 2; }
    E=$(sha256sum "$D/amorce.sh" | cut -d' ' -f1)
    [ "$E" = "$AS" ] && [ "$E" = "$(git -C "$DEPOT" show "$L:$A.sha256" 2>/dev/null | cut -d' ' -f1)" ] || { echo "empreinte de l'amorce ($E) ≠ DR_AMORCE_SHA256 ou son compagnon"; exit 2; }
    GOL=$(python3 -I -B -c "$SESSION8" go "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") || { echo "GO : $GOL : pas de création"; exit 2; }
    CAL=$(python3 -I -B -c "$SESSION8" calendrier "$REG" "$D/config.json" "$GO_ID_ENV" "$JOUR") || { echo "calendrier : $CAL : pas de création"; exit 2; }
    VUE=$(python3 -I -B -c "$SESSION8" vue "$D/config.json" "$D/vue-offre.json") || { echo "bornes de l'offre : $VUE : pas de création"; exit 2; }
    [ "$(cle_config "$D/config.json" lancement.plafond_usd)" = "$PLAFOND" ] || { echo "plafond de la configuration ≠ $PLAFOND USD"; exit 2; }
    # contrôles avant dépense du texte scellé, joués dans un arbre de travail du commit de lancement
    W=$(mktemp -d "$D/arbre-XXXX"); rmdir "$W"
    git -C "$DEPOT" worktree add -q --detach "$W" "$L" || { echo "arbre de travail du commit de lancement impossible"; exit 2; }
    CT=$(cd "$W" && PYTHONPATH=src python3 -B - "$CONFIG" "$JOUR" <<'PY' 2>&1
import json, sys
from pathlib import Path
from controle_ia.gardes import GardeArret
from controle_ia.scellement import verifier
from controle_ia.dose_reponse import controles_v2 as ct
try:
    verifier(sys.argv[1])
    c = json.load(open(sys.argv[1], encoding="utf-8"))
    if c.get("mode") != "reel":
        raise GardeArret("configuration en mode autre que réel")
    ct.exiger_calendrier(sys.argv[2])
    r = ct.controles_avant_depense(Path("."), c)
    b = r["banque"]
    t = ct.controler_textes_avant_creation(Path("."), c, ct.charger_tokeniseur_agent(c))
    print(f"contrôles conformes : texte {r['prereg_sha256'][:12]}, banque {b['taches']} tâches (rangs {b['rang_min']} à {b['rang_max']}), lignes {r['registre']['lignes']} ; pièce jointe de forme conforme, rapport des longueurs {t['rapport']} ≤ 1,15")
except (GardeArret, OSError, ValueError, KeyError) as e:
    print(f"ARRÊT : {e}")
    sys.exit(1)
PY
); RC=$?
    git -C "$DEPOT" worktree remove --force "$W" >/dev/null 2>&1 || true
    [ "$RC" = 0 ] || { echo "contrôles avant dépense : $(printf '%s' "$CT" | tail -n 1) : pas de création"; exit 2; }
    [ -n "${HF_TOKEN:-}" ] && JGHN=$(jeton_gh_nom) || { echo "jeton absent (HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN) : pas de création"; exit 2; }
    printf 'controles dose-reponse v3 %s\ncommit_texte %s\nlancement %s\nbranche_lancement %s\ncommit %s\nprereg %s\nconfig %s\nbranche %s\namorce %s\ngo %s\nplafond %s\ncompte_rendu %s\nmode reel\ncalendrier %s\nreprise_branche %s\nreprise_run %s\nessais %s\n' "$(date -u +%FT%TZ)" "$S" "$L" "$BL" "$COMMIT" "$P" "$CONFIG" "$BRANCHE" "$E" "$GO_ID_ENV" "$PLAFOND" "$COMPTE_RENDU" "$CAL" "${DR_REPRISE_BRANCHE:-}" "${DR_REPRISE_RUN:-}" "${DR_ESSAIS:-0}" >> "$D/lancement.txt"
    echo "CONTRÔLES CONFORMES : texte S=$S ; lancement $L ; code $COMMIT ; amorce $E ; $GOL ; $CAL ; $CT" ;;
creation)
    OFFRE_ARG="${2:?auto}"; CARTE="${3:?course}"; ANT="${4:?dépense antérieure en USD}"; D=$(realpath -m "${5:?dossier des contrôles}"); ECH="${6:-}"
    [ "$OFFRE_ARG" = auto ] || { echo "offre : « auto » seulement"; exit 2; }
    [ "$CARTE" = course ] || { echo "carte : course seulement (aucune carte plus chère, point 11)"; exit 2; }
    [[ "$ANT" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "dépense antérieure : nombre positif en USD"; exit 2; }
    [ -f "$D/lancement.txt" ] && [ -f "$D/config.json" ] || { echo "contrôles absents : pas de création"; exit 2; }
    S=$(champ commit_texte "$D/lancement.txt"); L=$(champ lancement "$D/lancement.txt"); COMMIT=$(champ commit "$D/lancement.txt")
    [[ "$S" =~ ^[0-9a-f]{40}$ ]] && [[ "$L" =~ ^[0-9a-f]{40}$ ]] && [[ "$COMMIT" =~ ^[0-9a-f]{40}$ ]] || { echo "commits illisibles dans lancement.txt"; exit 2; }
    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] && [ "$GO_ID_ENV" = "$(champ go "$D/lancement.txt")" ] || { echo "GO_ID ≠ GO des contrôles : pas de création"; exit 2; }
    [ "$(champ plafond "$D/lancement.txt")" = "$PLAFOND" ] || { echo "plafond des contrôles ≠ $PLAFOND USD"; exit 2; }
    CAL=$(python3 -I -B -c "$SESSION8" calendrier "$REG" "$D/config.json" "$GO_ID_ENV") || { echo "calendrier au jour de la création : $CAL : nœud"; exit 3; }
    [ "$(date -u +%F)" \< "2026-12-13" ] || { echo "jour de création après le 12 décembre 2026 (dernier jour de création du devis) : nœud, pas de création"; exit 3; }
    FIN_GO=$(printf '%s\n' "$CAL" | sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p'); [[ "$FIN_GO" =~ ^[0-9]+$ ]] || { echo "fin du GO illisible"; exit 2; }
    python3 -I -B -c "$SESSION8" go "$REG" "$D/config.json" "$GO_ID_ENV" >/dev/null || { echo "GO non conforme au jour de la création"; exit 2; }
    JGHN=$(jeton_gh_nom) && [ -n "${HF_TOKEN:-}" ] || { echo "jeton absent : pas de création"; exit 2; }
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : pas de création"; exit 2; }
    DISQUE=$(cle_config "$D/vue-offre.json" offre.disque_min_go) || { echo "disque illisible"; exit 2; }
    [ "${DISQUE%%.*}" -ge 300 ] || { echo "disque $DISQUE < 300 Go : pas de création"; exit 2; }
    ESSAIS=$(grep -c '^essai_creation ' "$D/lancement.txt" || true)
    [ "${ESSAIS:-0}" -lt 3 ] || { echo "trois essais de création déjà faits : arrêt, message à la mère"; exit 3; }
    EXCL=$(sed -n 's/^machine_refusee //p' "$D/lancement.txt" | paste -sd, -)
    FILTRE=$(python3 -I -B -c "$SESSION7" filtre "$D/vue-offre.json" course) || { echo "filtre illisible : $FILTRE"; exit 2; }
    timeout -k 5 120 "$VAST" search offers "$FILTRE" -o dph_total --storage "$DISQUE" --raw > "$D/offres.json" 2>"$D/offres.err" || { echo "recherche filtrée impossible : pas de création"; exit 2; }
    OF=$(python3 -I -B -c "$SESSION7" choisir "$D/offres.json" "$D/vue-offre.json" course "$EXCL") || { echo "aucune offre conforme : $OF : nœud, pas de création"; exit 3; }
    OFFRE=$(printf '%s\n' "$OF" | sed -n 's/^id=\([0-9]*\) .*/\1/p'); MACH=$(printf '%s\n' "$OF" | sed -n 's/.* machine=\([^ ]*\) .*/\1/p'); RANG=$(printf '%s\n' "$OF" | sed -n 's/.* rang=\([0-9]*\) .*/\1/p')
    [[ "$OFFRE" =~ ^[0-9]+$ ]] && [ -n "$MACH" ] || { echo "offre choisie illisible ($OF)"; exit 2; }
    PC=$(printf '%s\n' "$OF" | sed -n 's/.*prix_carte=\([0-9.]*\).*/\1/p'); PS=$(printf '%s\n' "$OF" | sed -n 's/.*prix_stockage=\([0-9.]*\).*/\1/p'); TEL=$(printf '%s\n' "$OF" | sed -n 's/.*telechargement_forfait=\([0-9.]*\).*/\1/p')
    [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] || { echo "prix illisibles"; exit 2; }
    ETIQ=$(cle_config "$D/vue-offre.json" offre.etiquette) || { echo "étiquette illisible"; exit 2; }
    vast_masque "$D/instances.json" timeout -k 5 120 "$VAST" show instances --raw || { echo "inventaire des instances impossible : pas de création"; exit 2; }
    INV=$(python3 -I -B -c "$SESSION" instances "$D/instances.json" "$ETIQ") || { echo "$INV : nœud, pas de création"; exit 3; }
    NOW=$(date +%s)
    DEP=$(python3 -I -B -c "$SESSION3" depense "$PLAFOND" "$PC" "$PS" "$NOW" "$ANT" "$TEL" "$NOW"); [ $? = 0 ] || { echo "dépense cumulée déjà au plafond ou illisible ($DEP) : nœud, pas de création"; exit 3; }
    EPUIS=$(printf '%s\n' "$DEP" | sed -n 's/.*epuisement_utc_s=\([0-9]*\).*/\1/p'); [[ "$EPUIS" =~ ^[0-9]+$ ]] || { echo "heure d'épuisement illisible"; exit 2; }
    [ -n "$ECH" ] || ECH="$EPUIS"
    [[ "$ECH" =~ ^[0-9]+$ ]] || { echo "échéance $ECH illisible"; exit 2; }
    [ "$ECH" -gt "$FIN_GO" ] && ECH="$FIN_GO"
    [ "$ECH" -le "$EPUIS" ] && [ "$ECH" -gt "$(date +%s)" ] || { echo "échéance $ECH hors de ]maintenant, $EPUIS]"; exit 2; }
    B64=$(base64 -w0 < "$D/amorce.sh")
    [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$(champ amorce "$D/lancement.txt")" ] || { echo "encodage de l'amorce"; exit 2; }
    RB=$(champ reprise_branche "$D/lancement.txt"); RR=$(champ reprise_run "$D/lancement.txt"); NE=$(champ essais "$D/lancement.txt")
    [[ "${NE:-0}" =~ ^[0-9]+$ ]] && [ "${NE:-0}" -le 16 ] || { echo "essais de chaîne : 0 à 16"; exit 2; }
    REPRISE=""; [ -n "$RB" ] && REPRISE=" -e REPRISE_BRANCHE=$RB -e REPRISE_RUN=$RR"
    CMD="GO_ID=$GO_ID_ENV timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e LANCEMENT=$L -e BRANCHE_LANCEMENT=$(champ branche_lancement "$D/lancement.txt") -e COMMIT_CODE=$COMMIT -e PREREG=$P -e CONFIG=$(champ config "$D/lancement.txt") -e BRANCHE=$(champ branche "$D/lancement.txt") -e GO_ID_DR=$GO_ID_ENV -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e ECHEANCE_UTC_S=$ECH -e FIN_GO_UTC_S=$FIN_GO -e DEPENSE_EPUISEE_UTC_S=$EPUIS -e ESSAIS=${NE:-0}$REPRISE -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$$JGHN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh\" > \"$D/creation-brute.json\" 2>&1; bash $DEPOT/scripts/lancer_dose_reponse_v3.sh apres-creation \"$D/creation-brute.json\" \$? \"$D\""
    printf '{"tool_input":{"command":%s}}' "$(python3 -c 'import json, sys; print(json.dumps(sys.argv[1]))' "$CMD")" | python3 "$DEPOT/.claude/hooks/garde_calcul.py" || { echo "garde de calcul : commande refusée"; exit 2; }
    printf 'creation preparee %s\noffre %s\ncarte %s\nstorage %s\nprix_carte %s\nprix_stockage %s\ntelechargement_forfait %s\nanterieure %s\necheance %s\nepuisement %s\ndepense %s\nplafond_creation %s\nessai_creation %s\nmachine_proposee %s\nrang %s\n' "$(date -u +%FT%TZ)" "$OFFRE" "$CARTE" "$DISQUE" "$PC" "$PS" "$TEL" "$ANT" "$ECH" "$EPUIS" "$DEP" "$PLAFOND" "$((ESSAIS + 1))" "$MACH" "$RANG" >> "$D/lancement.txt"
    echo "OFFRE CONFORME : $OF ; $INV ; $DEP"
    echo "COMMANDE DE CRÉATION (à exécuter par la session, jetons par leur nom seulement) :"
    echo "$CMD" ;;
apres-creation)
    F="${2:?fichier}"; C="${3:?code}"; D="${4:?dossier}"
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    NON=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(False|false)" "$F" 2>/dev/null || true)
    rm -f -- "$F"
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then
        CR=$(date +%s); printf 'instance %s\ncreation %s\n' "$ID" "$CR" >> "$D/lancement.txt"
        echo "CRÉÉE : instance $ID (création $CR) ; surveillance : bash scripts/lancer_dose_reponse_v3.sh surveillance $ID $D"; exit 0
    fi
    if [ -z "$ID" ] && [ "${NON:-0}" -ge 1 ] && [ "${OK:-0}" -eq 0 ]; then
        ETIQ=$(cle_config "$D/vue-offre.json" offre.etiquette) || { echo "étiquette illisible"; exit 4; }
        if vast_masque "$D/instances-apres.json" timeout -k 5 120 "$VAST" show instances --raw && python3 -I -B -c "$SESSION" instances "$D/instances-apres.json" "$ETIQ" >/dev/null; then
            printf 'machine_refusee %s\n' "$(champ machine_proposee "$D/lancement.txt")" >> "$D/lancement.txt"
            echo "OFFRE REFUSÉE À LA CRÉATION : aucune instance du programme ; rang suivant : bash $DEPOT/scripts/lancer_dose_reponse_v3.sh creation auto course $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")"; exit 5
        fi
    fi
    echo "CRÉATION INCERTAINE (code $C, identifiant « ${ID:-aucun} ») : vérifier « vastai show instances » ; aucune seconde création avant"; exit 4 ;;
surveillance)
    ID="${2:?identifiant}"; D="${3:?dossier}"; FACT="${4:-}"
    [[ "$ID" =~ ^[0-9]+$ ]] || { echo "identifiant : chiffres seuls (R10)"; exit 2; }
    [ "$(champ instance "$D/lancement.txt")" = "$ID" ] || { echo "identifiant $ID ≠ instance créée (R10)"; exit 2; }
    CR=$(champ creation "$D/lancement.txt"); PC=$(champ prix_carte "$D/lancement.txt"); PS=$(champ prix_stockage "$D/lancement.txt")
    TEL=$(champ telechargement_forfait "$D/lancement.txt"); ANT=$(champ anterieure "$D/lancement.txt")
    [ "$(champ plafond_creation "$D/lancement.txt")" = "$PLAFOND" ] || { echo "plafond de la création ≠ $PLAFOND USD"; exit 2; }
    [[ "$CR" =~ ^[0-9]+$ ]] && [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] && [ -n "$ANT" ] || { echo "création ou prix illisibles"; exit 2; }
    JGH="${CONTROLE_IA_GITHUB_TOKEN:-${CONTROLE_IA_GITHUB_TOKEN_2:-}}"; [ "${#JGH}" -ge 8 ] || { echo "jeton GitHub absent : masquage impossible, surveillance refusée"; exit 2; }
    HF_L="${HF_TOKEN:-}"; [ "${#HF_L}" -ge 8 ] || { echo "HF_TOKEN absent : masquage impossible, surveillance refusée"; exit 2; }
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : surveillance aveugle"; exit 2; }
    : >> "$D/progres.txt"; INTERVALLE="${INTERVALLE:-120}"; ILLISIBLES=0
    alerte() { local m; m="$(date -u +%FT%TZ) $1"; echo "$m" >> "$D/surveillance.txt"; echo "$m"; }
    echo "surveillance dose-réponse v3 de $ID : carte $PC USD/h, stockage $PS USD/h, antérieur $ANT USD ; arrêt sur processus mort ou dépense cumulée ≥ $PLAFOND USD ; alerte unique à $COMPTE_RENDU USD ; alerte après 2 h sans PROGRES" >> "$D/surveillance.txt"
    while true; do
        now=$(date -u +%s)
        timeout -k 5 120 "$VAST" logs "$ID" --tail 20000 2>&1 | masquer > "$D/journal-dernier.tmp"; PSJ=("${PIPESTATUS[@]}")
        if [ "${PSJ[1]:-1}" != 0 ]; then rm -f "$D/journal-dernier.tmp"; alerte "ALERTE masquage en échec : relevé écarté"
        elif [ "${PSJ[0]}" = 0 ]; then mv -f "$D/journal-dernier.tmp" "$D/journal-dernier.txt"
            grep -q '^AMORCE ' "$D/journal-dernier.txt" && cp -f "$D/journal-dernier.txt" "$D/journal-instance.txt"
            grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"; done
        else rm -f "$D/journal-dernier.tmp"; fi
        vast_masque "$D/inventaire-tour.json" timeout -k 5 120 "$VAST" show instances --raw; st=$?
        if [ "$st" = 0 ] && ! python3 -I -B -c "$SESSION7" presente "$D/inventaire-tour.json" "$ID" >/dev/null 2>&1; then
            sleep "${ABSENCE_ATTENTE_S:-15}"
            vast_masque "$D/inventaire-tour.json" timeout -k 5 120 "$VAST" show instances --raw && ! python3 -I -B -c "$SESSION7" presente "$D/inventaire-tour.json" "$ID" >/dev/null 2>&1 \
                && { alerte "ARRET mort : instance $ID absente à deux relevés ; confirmer par show instance $ID ; cause dans $D/journal-instance.txt et sur la branche"; exit 3; }
        fi
        if DEC=$(python3 -I -B -c "$SESSION8" surveillance "$PLAFOND" "$COMPTE_RENDU" "$D/progres.txt" "$now" "$PC" "$PS" "$CR" "$ANT" "$TEL" ${FACT:+"$FACT"} 2>&1); then ILLISIBLES=0
        else ILLISIBLES=$((ILLISIBLES + 1))
            if [ "$ILLISIBLES" -ge 3 ]; then DEC="ARRET garde : garde de dépense illisible trois fois de suite ($DEC)"; else DEC="ALERTE garde de dépense illisible ($ILLISIBLES/3) : $DEC"; fi
        fi
        echo "$(date -u +%FT%TZ) $DEC" >> "$D/surveillance.txt"
        case "$DEC" in
            ARRET*) echo "$DEC"; echo "ARRÊT PAR L'IDENTIFIANT (R10) : timeout -k 5 120 $VAST stop instance $ID"; exit 3 ;;
            FIN*) echo "$DEC"; echo "FIN : l'amorce détruit la machine après le versement prouvé ; vérifier la poussée, puis l'inventaire ; machine encore là : timeout -k 5 120 $VAST destroy instance $ID (R10)"; exit 0 ;;
            REFUS*) echo "$DEC"; exit 4 ;;
            "ALERTE compte rendu"*) [ -e "$D/compte-rendu-alerte.txt" ] || echo "$(date -u +%FT%TZ) $DEC" | tee "$D/compte-rendu-alerte.txt" ;;
            ALERTE*) echo "$(date -u +%FT%TZ) $DEC" ;;
        esac
        sleep "$INTERVALLE"
    done ;;
--verifier-go-seulement)
    CFG="${2:?configuration}"; ANT_EPR="${3:-0}"; JOUR="${4:-$(date -u +%F)}"
    [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible : rien vérifié, rien créé"; exit 2; }
    [[ "$ANT_EPR" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "dépense antérieure illisible : refus"; exit 2; }
    GOL=$(python3 -I -B -c "$SESSION8" go "$REG" "$CFG" "$GO_ID_ENV" "$JOUR") || { echo "GO $GO_ID_ENV refusé : $GOL"; exit 2; }
    python3 -I -c 'import sys; from decimal import Decimal as D; sys.exit(0 if D(sys.argv[1]) < D(sys.argv[2]) else 1)' "$ANT_EPR" "$PLAFOND" || { echo "dépense antérieure $ANT_EPR ≥ plafond $PLAFOND USD : refus"; exit 2; }
    echo "GO VÉRIFIÉ, RIEN CRÉÉ : $GOL ; dépense antérieure $ANT_EPR < plafond $PLAFOND USD" ;;
*) echo "usage : controles | creation | apres-creation | surveillance | --verifier-go-seulement" >&2; exit 2 ;;
esac
