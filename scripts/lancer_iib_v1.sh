#!/usr/bin/env bash
# Chaîne de session de (ii-b), v1 (conception ii-b, brouillon 2, section 10 ; ordre exploratoire, brouillon 2, §§ 1, 3, 5 et 6) : tirée de
# `scripts/lancer_t06_v13.sh` (nom neuf, R12 ; la v13 reste telle quelle). EXPLORATOIRE, NON OPPOSABLE (R-522). Écrite et éprouvée à blanc
# (essais `tests/test_iib_scripts_v1.py`, registre de GO et registre des décisions FACTICES, faux `vastai`), jamais lancée par son
# développeur. Changements par rapport à la v13 :
#  - la ligne de GO de la course vient de GO_ID (convention de la garde de calcul), doit égaler `go_id` de la configuration, et est LUE dans
#    le registre IIB_REGISTRE_GO (registres/go.md d'un clone de main) : type calcul, Lazar, non échue au jour donné, non révoquée ;
#    plafond de la configuration + dépense antérieure ≤ plafond de la ligne ; la variante de plafond (M7 non tranchée : A 80/75 avec
#    repli H200 NVL, B 60/55 sans repli) est celle que nomme la configuration, et la ligne du registre porte le plafond de cette variante ;
#  - « 7b d'abord » : la ligne du registre des décisions de la création de 7b, citée par la configuration, doit figurer au registre des
#    décisions IIB_REGISTRE_DECISIONS (par défaut `decisions.md` à côté de IIB_REGISTRE_GO, même clone de main), sinon refus, aux
#    contrôles ET à la création ;
#  - étiquette `iib-explo-v1` : seule une instance d'étiquette commençant par `iib` bloque la création (7b, A1-v4 et les instances
#    arrêtées ne sont ni comptées comme bloquantes ni touchées) ;
#  - carte « relance » (H200 NVL) permise seulement en variante A ; fenêtre A100 vide en variante B : nœud (code 3, aucune création) ;
#  - course exploratoire : aucun préenregistrement (PREREG_ABSENT=1), branche poussée `essai/iib-explo-v<n>` seulement ; configuration
#    validée par `iib/session_v1 config` (le mode réel refuse tant qu'un des 30 marqueurs reste) ; tâches et consignes citées présentes et
#    scellées au commit, tâches disjointes ; l'amorce citée est `scripts/amorce_instance_iib_v1.sh` (empreinte relevée) ;
#  - les quatre variables du mandataire (REQUESTS_CA_BUNDLE, SSL_CERT_FILE, HTTPS_PROXY, NO_PROXY) ne sont jamais transmises à l'instance :
#    la commande de création imprimée qui en nommerait une est refusée.
# Usage :
#   bash scripts/lancer_iib_v1.sh --verifier-go-seulement PLAFOND [DEPENSE_ANTERIEURE] [JOUR]       (rien n'est créé ; code 0 ou 2)
#   bash scripts/lancer_iib_v1.sh controles-explo DOSSIER_NEUF COMMIT CONFIG_CHEMIN [JOUR]            (code 0 ; 2 tout échec)
#   bash scripts/lancer_iib_v1.sh creation auto course|relance DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]
#        (imprime la commande de création ; code 0 ; 2 échec ; 3 nœud : aucune offre conforme, instance iib présente, dépense épuisée)
#   bash scripts/lancer_iib_v1.sh apres-creation FICHIER CODE DOSSIER
#   bash scripts/lancer_iib_v1.sh surveillance ID DOSSIER [FACTURE_USD]
# Variables : GO_ID, IIB_REGISTRE_GO, IIB_REGISTRE_DECISIONS, IIB_BRANCHE_CODE (prep/…), IIB_BRANCHE (défaut essai/iib-explo-v1),
# IIB_DEPENSE_ANTERIEURE_USD, IIB_TESTS_ATTENDUS (^[0-9]*$), IIB_DEPOT, IIB_IMAGE, VAST (outil), INTERVALLE ; HF_TOKEN (mode réel),
# CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2 (présence seulement, jamais affichés).
set -uo pipefail
QUOI="${1:?--verifier-go-seulement, controles-explo, creation, apres-creation ou surveillance}"
DEPOT="${IIB_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"
A=scripts/amorce_instance_iib_v1.sh
BRANCHE="${IIB_BRANCHE:-essai/iib-explo-v1}"
GO_ID_ENV="${GO_ID:-}"
REG="${IIB_REGISTRE_GO:-}"
REGDEC="${IIB_REGISTRE_DECISIONS:-}"; [ -n "$REGDEC" ] || { [ -n "$REG" ] && REGDEC="$(dirname "$REG")/decisions.md"; }
MOTIF_GO='^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$'
IMAGE="${IIB_IMAGE:-python:3.11-bookworm}"
VAST="${VAST:-vastai}"
SESSION="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.iib import session_v1; sys.exit(session_v1.main(sys.argv[1:]))"
SESSION3="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.t06 import session_v3; sys.exit(session_v3.main(sys.argv[1:]))"
masquer() { python3 -c '
import os, sys
t = sys.stdin.read()
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) >= 8:
        t = t.replace(v, "***")
sys.stdout.write(t)'; }
vast_masque() {
    local sortie="$1"; shift
    "$@" 2>/dev/null | masquer > "$sortie.tmp"
    local ps=("${PIPESTATUS[@]}")
    if [ "${ps[1]:-1}" != 0 ]; then rm -f "$sortie.tmp"; return 121; fi
    mv -f "$sortie.tmp" "$sortie"; return "${ps[0]}"
}
jeton_gh_nom() { if [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN; elif [ -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN_2; else return 1; fi; }
champ() { sed -n "s/^$1 //p" "$2" | tail -1; }
cle_config() { python3 -I -B -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8"))
for k in sys.argv[2].split("."):
    c = c[k]
print(c if not isinstance(c, bool) else ("oui" if c else "non"))' "$1" "$2"; }
exiger_go_env() { [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN : la ligne de GO de calcul de la course) : rien créé"; exit 2; }; }
exiger_registre() { [ -n "$REG" ] && [ -f "$REG" ] || { echo "IIB_REGISTRE_GO : registres/go.md d'un clone de main exigé : rien créé"; exit 2; }; }
case "$QUOI" in
--verifier-go-seulement)
    PLC="${2:?plafond de la configuration, en USD}"; ANT="${3:-0}"; JOUR="${4:-$(date -u +%F)}"
    exiger_go_env; exiger_registre
    [[ "$PLC" =~ ^[0-9]+([.][0-9]+)?$ ]] && [[ "$ANT" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "plafond ($PLC) ou dépense antérieure ($ANT) : nombre positif en USD attendu : refus"; exit 2; }
    GOL=$(python3 -I -B -c "$SESSION" go "$REG" "$GO_ID_ENV" "$PLC" "$ANT" "$JOUR") || { echo "GO $GO_ID_ENV refusé : $GOL"; exit 2; }
    echo "GO VÉRIFIÉ, RIEN CRÉÉ : $GOL" ;;
controles-explo)
    D=$(realpath -m "${2:?dossier neuf}"); S="${3:?commit (40 caractères)}"; CFG="${4:?chemin de la configuration dans le commit}"; JOUR="${5:-$(date -u +%F)}"
    [ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
    [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit : 40 caractères hexadécimaux"; exit 2; }
    BC="${IIB_BRANCHE_CODE:?IIB_BRANCHE_CODE : branche prep/… du code}"
    case "$BC" in prep/*) ;; *) echo "IIB_BRANCHE_CODE doit commencer par prep/ ($BC)"; exit 2;; esac
    case "$BRANCHE" in essai/iib-explo-v[0-9]*) ;; *) echo "IIB_BRANCHE doit être essai/iib-explo-v<n> ($BRANCHE) : jamais main, 7a, 7b, P3-bis"; exit 2;; esac
    exiger_go_env; exiger_registre
    ANT="${IIB_DEPENSE_ANTERIEURE_USD:-}"; [[ "$ANT" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "IIB_DEPENSE_ANTERIEURE_USD : dépense antérieure de ce run, en USD (0 pour la première instance), exigée"; exit 2; }
    [[ "${IIB_TESTS_ATTENDUS:-}" =~ ^[0-9]*$ ]] || { echo "IIB_TESTS_ATTENDUS illisible (^[0-9]*$ exigé)"; exit 2; }
    git -C "$DEPOT" cat-file -e "$S^{commit}" 2>/dev/null || { echo "commit $S absent du dépôt local (git fetch origin refs/heads/$BC:refs/remotes/origin/$BC d'abord)"; exit 2; }
    git -C "$DEPOT" merge-base --is-ancestor "$S" "refs/remotes/origin/$BC" 2>/dev/null || { echo "commit $S absent de refs/remotes/origin/$BC"; exit 2; }
    mkdir -p "$D"
    git -C "$DEPOT" show "$S:$CFG" > "$D/config.json" 2>/dev/null && git -C "$DEPOT" show "$S:$CFG.sha256" > "$D/config.json.sha256.cite" 2>/dev/null \
        || { echo "configuration $CFG ou son sceau absents du commit $S"; exit 2; }
    [ "$(sha256sum "$D/config.json" | cut -d' ' -f1)" = "$(cut -d' ' -f1 "$D/config.json.sha256.cite")" ] || { echo "sceau de la configuration $CFG non conforme au commit $S"; exit 2; }
    CONF=$(python3 -I -B -c "$SESSION" config "$D/config.json") || { echo "$CONF : pas de création"; exit 2; }
    GOC=$(cle_config "$D/config.json" go_id) && PLC=$(cle_config "$D/config.json" plafond_usd) && MODE_C=$(cle_config "$D/config.json" mode) || { echo "go_id, plafond_usd ou mode illisibles"; exit 2; }
    [ "$GOC" = "$GO_ID_ENV" ] || { echo "go_id de la configuration ($GOC) ≠ GO_ID de l'environnement ($GO_ID_ENV) : pas de création"; exit 2; }
    GOL=$(python3 -I -B -c "$SESSION" go "$REG" "$GOC" "$PLC" "$ANT" "$JOUR") || { echo "ligne de GO $GOC non conforme : $GOL : pas de création"; exit 2; }
    PGL=$(python3 -I -B -c "$SESSION" plafond-ligne "$REG" "$GOC" "$JOUR") || { echo "plafond de la ligne $GOC illisible ($PGL)"; exit 2; }
    VAR=$(python3 -I -B -c "$SESSION" variante "$D/config.json" "$PGL") || { echo "$VAR : pas de création"; exit 2; }
    git -C "$DEPOT" show "$S:registres/go.md" > "$D/go-commit.md" 2>/dev/null && python3 -I -B -c "$SESSION" plafond-ligne "$D/go-commit.md" "$GOC" "$JOUR" >/dev/null \
        || { echo "GO $GOC absent ou non conforme dans registres/go.md du commit $S (l'amorce le relit) : commit postérieur au GO exigé"; exit 2; }
    CAL=$(python3 -I -B -c "$SESSION3" calendrier "$D/config.json" "$REG" "$GOC" "$PGL" "$JOUR") || { echo "calendrier de la configuration : $CAL : pas de création"; exit 2; }
    S7B=$(python3 -I -B -c "$SESSION" creation-7b "$REGDEC" "$D/config.json") || { echo "$S7B : pas de création"; exit 2; }
    for cle in taches_reserve taches_evaluation consigne_maitre consignes_p3; do
        f=$(cle_config "$D/config.json" "$cle.chemin") && h=$(cle_config "$D/config.json" "$cle.sha256") || { echo "$cle illisible"; exit 2; }
        git -C "$DEPOT" cat-file -e "$S:$f" 2>/dev/null && git -C "$DEPOT" cat-file -e "$S:$f.sha256" 2>/dev/null || { echo "fichier cité $f ou son sceau absent du commit $S"; exit 2; }
        [ "$(git -C "$DEPOT" show "$S:$f" | sha256sum | cut -d' ' -f1)" = "$h" ] && [ "$(git -C "$DEPOT" show "$S:$f.sha256" | cut -d' ' -f1)" = "$h" ] || { echo "empreinte de $f ≠ celle de la configuration (R11)"; exit 2; }
    done
    git -C "$DEPOT" show "$S:$(cle_config "$D/config.json" taches_reserve.chemin)" > "$D/reserve.json" && git -C "$DEPOT" show "$S:$(cle_config "$D/config.json" taches_evaluation.chemin)" > "$D/evaluation.json" \
        || { echo "tâches illisibles au commit"; exit 2; }
    DISJ=$(python3 -I -B -c 'import json, sys
def identifiants(f, quoi):          # même lecture que la course (environnements/pilote_a.charger_taches) : resultat.taches si présent, sinon taches
    brut = json.load(open(f, encoding="utf-8"))
    source = brut["resultat"] if isinstance(brut, dict) and "resultat" in brut else brut
    taches = source.get("taches") if isinstance(source, dict) else None
    if not isinstance(taches, list) or not taches:
        print("liste des tâches de " + quoi + " illisible : ni resultat.taches ni taches ne sont une liste non vide"); sys.exit(1)
    return set(t["identifiant"] for t in taches)
ids = [identifiants(f, quoi) for f, quoi in zip(sys.argv[1:3], ("réserve", "évaluation"))]
communes = sorted(ids[0] & ids[1])
print("communes " + " ".join(communes[:5]) if communes else "disjointes"); sys.exit(1 if communes else 0)' "$D/reserve.json" "$D/evaluation.json") \
        || { echo "tâches de réserve et d'évaluation : contrôle « aucune tâche commune » refusé ($DISJ) : aucune création"; exit 2; }
    rm -f "$D/reserve.json" "$D/evaluation.json"
    git -C "$DEPOT" show "$S:$A" > "$D/amorce.sh" 2>/dev/null || { echo "amorce $A absente du commit $S"; exit 2; }
    E=$(sha256sum "$D/amorce.sh" | cut -d' ' -f1)
    if [ "$MODE_C" = reel ]; then [ -n "${HF_TOKEN:-}" ] || { echo "HF_TOKEN absent (mode réel) : pas de création"; exit 2; }; fi
    JGHN=$(jeton_gh_nom) || { echo "jeton absent (ni CONTROLE_IA_GITHUB_TOKEN ni CONTROLE_IA_GITHUB_TOKEN_2) : pas de création"; exit 2; }
    LIBRE=$(df -Pk "$D" | awk 'NR==2 {print $4}'); [ "$LIBRE" -ge 3000000 ] || { echo "place disque : $LIBRE ko libres (3 Go exigés)"; exit 2; }
    printf 'controles-explo iib v1 %s\ncommit %s\nconfig %s\nbranche %s\namorce %s\ngo %s\nplafond %s\nanterieure_controles %s\nmode %s\nvariante %s\ncalendrier %s\n7b %s\ntests_attendus %s\n' \
        "$(date -u +%FT%TZ)" "$S" "$CFG" "$BRANCHE" "$E" "$GOC" "$PLC" "$ANT" "$MODE_C" "$VAR" "$CAL" "$S7B" "${IIB_TESTS_ATTENDUS:-}" >> "$D/lancement.txt"
    echo "CONTRÔLES CONFORMES : S=$S ; amorce $E ; $GOL ; $VAR ; mode $MODE_C ; $CONF ; $S7B" ;;
creation)
    OFFRE_ARG="${2:?auto}"; CARTE="${3:?carte : course ou relance}"; ANT="${4:?dépense antérieure en USD}"; D=$(realpath -m "${5:?dossier des contrôles}"); ECH="${6:-}"
    [ "$OFFRE_ARG" = auto ] || { echo "offre : « auto » seulement (l'offre est choisie dans la liste filtrée, juste avant la création)"; exit 2; }
    case "$CARTE" in course|relance) ;; *) echo "carte : course ou relance"; exit 2;; esac
    [[ "$ANT" =~ ^[0-9]+([.][0-9]+)?$ ]] || { echo "dépense antérieure : nombre positif en USD"; exit 2; }
    [ -f "$D/lancement.txt" ] && grep -q '^controles-explo ' "$D/lancement.txt" && [ -f "$D/config.json" ] || { echo "contrôles absents ($D/lancement.txt, config.json) : pas de création"; exit 2; }
    S=$(champ commit "$D/lancement.txt"); [[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "commit illisible"; exit 2; }
    exiger_go_env; exiger_registre
    GOC=$(cle_config "$D/config.json" go_id) && PLC=$(cle_config "$D/config.json" plafond_usd) && MODE_C=$(cle_config "$D/config.json" mode) || { echo "go_id, plafond_usd ou mode illisibles"; exit 2; }
    [ "$GOC" = "$GO_ID_ENV" ] && [ "$(champ go "$D/lancement.txt")" = "$GOC" ] || { echo "go_id de la configuration ($GOC) ≠ GO_ID de l'environnement (${GO_ID_ENV}) ou des contrôles : pas de création"; exit 2; }
    case "$BRANCHE" in essai/iib-explo-v[0-9]*) ;; *) echo "IIB_BRANCHE doit être essai/iib-explo-v<n> ($BRANCHE)"; exit 2;; esac
    GOL=$(python3 -I -B -c "$SESSION" go "$REG" "$GOC" "$PLC" "$ANT") || { echo "ligne de GO $GOC non conforme au jour de la création : $GOL : pas de création"; exit 2; }
    PGL=$(python3 -I -B -c "$SESSION" plafond-ligne "$REG" "$GOC") || { echo "plafond de la ligne illisible"; exit 2; }
    VAR=$(python3 -I -B -c "$SESSION" variante "$D/config.json" "$PGL") || { echo "$VAR : pas de création"; exit 2; }
    CAR=$(python3 -I -B -c "$SESSION" carte "$D/config.json" "$CARTE") || { echo "$CAR : nœud, pas de création"; exit 3; }
    S7B=$(python3 -I -B -c "$SESSION" creation-7b "$REGDEC" "$D/config.json") || { echo "$S7B : pas de création"; exit 2; }
    CAL=$(python3 -I -B -c "$SESSION3" calendrier "$D/config.json" "$REG" "$GOC" "$PGL") || { echo "calendrier au jour de la création : $CAL : nœud, pas de création"; exit 3; }
    FIN_GO=$(printf '%s\n' "$CAL" | sed -n 's/.*fin_go_utc_s=\([0-9]*\).*/\1/p'); [ -n "$ECH" ] || ECH="$FIN_GO"
    [[ "$ECH" =~ ^[0-9]+$ ]] && [ "$ECH" -le "$FIN_GO" ] && [ "$ECH" -gt "$(date +%s)" ] || { echo "échéance $ECH hors de ]maintenant, fin du GO $FIN_GO]"; exit 2; }
    JGHN=$(jeton_gh_nom) && { [ -n "${HF_TOKEN:-}" ] || [ "$MODE_C" = jouet ]; } || { echo "jeton absent (GitHub, ou HF_TOKEN en mode réel) : pas de création"; exit 2; }
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : pas de création"; exit 2; }
    DISQUE=$(cle_config "$D/config.json" offre.disque_min_go) || { echo "disque illisible"; exit 2; }
    [[ "$DISQUE" =~ ^[0-9]+([.][0-9]+)?$ ]] && [ "${DISQUE%%.*}" -gt 0 ] || { echo "offre.disque_min_go illisible ($DISQUE) : pas de création"; exit 2; }
    ESSAIS=$(grep -c '^essai_creation ' "$D/lancement.txt" || true)
    [ "${ESSAIS:-0}" -lt 3 ] || { echo "trois essais de création déjà faits : arrêt, aucune création ; message à la mère"; exit 3; }
    EXCL=$(sed -n 's/^machine_refusee //p' "$D/lancement.txt" | paste -sd, -)
    FILTRE=$(python3 -I -B -c "$SESSION" filtre "$D/config.json" "$CARTE") || { echo "filtre illisible : $FILTRE"; exit 2; }
    timeout -k 5 120 "$VAST" search offers "$FILTRE" -o dph_total --storage "$DISQUE" --raw > "$D/offres.json" 2>"$D/offres.err" || { echo "recherche filtrée impossible : pas de création"; exit 2; }
    OF=$(python3 -I -B -c "$SESSION" choisir "$D/offres.json" "$D/config.json" "$CARTE" "$EXCL") || { echo "aucune offre conforme dans la liste filtrée : $OF : nœud (fenêtre : rejouer dans 15 minutes, 12 fois au plus), pas de création"; exit 3; }
    OFFRE=$(printf '%s\n' "$OF" | sed -n 's/^id=\([0-9]*\) .*/\1/p'); MACH=$(printf '%s\n' "$OF" | sed -n 's/.* machine=\([^ ]*\) .*/\1/p'); RANG=$(printf '%s\n' "$OF" | sed -n 's/.* rang=\([0-9]*\) .*/\1/p')
    [[ "$OFFRE" =~ ^[0-9]+$ ]] && [ -n "$MACH" ] && [ -n "$RANG" ] || { echo "offre choisie illisible ($OF)"; exit 2; }
    PC=$(printf '%s\n' "$OF" | sed -n 's/.*prix_carte=\([0-9.]*\).*/\1/p'); PS=$(printf '%s\n' "$OF" | sed -n 's/.*prix_stockage=\([0-9.]*\).*/\1/p')
    TEL=$(printf '%s\n' "$OF" | sed -n 's/.*telechargement_forfait=\([0-9.]*\).*/\1/p')
    [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] || { echo "prix illisibles dans la relecture de l'offre"; exit 2; }
    ETIQ=$(cle_config "$D/config.json" offre.etiquette) || { echo "étiquette illisible"; exit 2; }
    vast_masque "$D/instances.json" timeout -k 5 120 "$VAST" show instances --raw || { echo "inventaire des instances impossible ou masquage en échec (code $?) : pas de création"; exit 2; }
    INV=$(python3 -I -B -c "$SESSION" instances "$D/instances.json") || { echo "$INV : nœud, pas de création"; exit 3; }
    NOW=$(date +%s)
    DEP=$(python3 -I -B -c "$SESSION3" depense "$PLC" "$PC" "$PS" "$NOW" "$ANT" "$TEL" "$NOW"); code_dep=$?
    [ "$code_dep" = 0 ] || { echo "dépense cumulée déjà au plafond ou illisible ($DEP) : nœud, pas de création"; exit 3; }
    EPUIS=$(printf '%s\n' "$DEP" | sed -n 's/.*epuisement_utc_s=\([0-9]*\).*/\1/p'); [[ "$EPUIS" =~ ^[0-9]+$ ]] || { echo "heure d'épuisement illisible"; exit 2; }
    git -C "$DEPOT" show "$S:$A" > "$D/amorce-creation.sh" 2>/dev/null || { echo "amorce absente du commit $S"; exit 2; }
    [ "$(sha256sum "$D/amorce-creation.sh" | cut -d' ' -f1)" = "$(champ amorce "$D/lancement.txt")" ] || { echo "amorce changée depuis les contrôles"; exit 2; }
    B64=$(base64 -w0 < "$D/amorce-creation.sh")
    [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$(champ amorce "$D/lancement.txt")" ] || { echo "encodage de l'amorce"; exit 2; }
    TA="$(champ tests_attendus "$D/lancement.txt")"; [[ "$TA" =~ ^[0-9]*$ ]] || { echo "tests attendus illisibles"; exit 2; }
    CMD="GO_ID=$GOC timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT=$S -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e IIB_GO_ID=$GOC -e MODE=$MODE_C -e PREREG_ABSENT=1 -e CONFIG=$(champ config "$D/lancement.txt") -e TESTS_ATTENDUS=$TA -e ECHEANCE_UTC_S=$ECH -e FIN_GO_UTC_S=$FIN_GO -e DEPENSE_EPUISEE_UTC_S=$EPUIS -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$$JGHN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh\" > \"$D/creation-brute.json\" 2>&1; bash $DEPOT/scripts/lancer_iib_v1.sh apres-creation \"$D/creation-brute.json\" \$? \"$D\""
    for v in REQUESTS_CA_BUNDLE SSL_CERT_FILE HTTPS_PROXY NO_PROXY; do
        case "$CMD" in *"$v"*) echo "la commande de création nomme $v (variable du mandataire, jamais transmise à l'instance) : refus"; exit 2;; esac
    done
    printf '{"tool_input":{"command":%s}}' "$(python3 -c 'import json, sys; print(json.dumps(sys.argv[1]))' "$CMD")" | python3 "$DEPOT/.claude/hooks/garde_calcul.py" || { echo "garde de calcul : commande refusée"; exit 2; }
    printf 'creation preparee %s\noffre %s\ncarte %s\nstorage %s\nprix_carte %s\nprix_stockage %s\ntelechargement_forfait %s\nanterieure %s\necheance %s\nepuisement %s\ndepense %s\nplafond_creation %s\nessai_creation %s\nmachine_proposee %s\nrang %s\n' \
        "$(date -u +%FT%TZ)" "$OFFRE" "$CARTE" "$DISQUE" "$PC" "$PS" "$TEL" "$ANT" "$ECH" "$EPUIS" "$DEP" "$PLC" "$((ESSAIS + 1))" "$MACH" "$RANG" >> "$D/lancement.txt"
    echo "OFFRE CONFORME : $OF ; $INV ; $DEP ; $CAR ; $S7B"
    echo "COMMANDE DE CRÉATION (à exécuter une seule fois par l'exécutante, jetons par leur nom seulement) :"
    echo "$CMD" ;;
apres-creation)
    F="${2:?fichier}"; C="${3:?code}"; D="${4:?dossier}"
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    NON=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(False|false)" "$F" 2>/dev/null || true)
    rm -f -- "$F"
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then
        CR=$(date +%s); printf 'instance %s\ncreation %s\n' "$ID" "$CR" >> "$D/lancement.txt"
        echo "CRÉÉE : instance $ID (création $CR) ; surveillance : bash scripts/lancer_iib_v1.sh surveillance $ID $D"; exit 0
    fi
    if [ -z "$ID" ] && [ "${NON:-0}" -ge 1 ] && [ "${OK:-0}" -eq 0 ]; then
        if vast_masque "$D/instances-apres.json" timeout -k 5 120 "$VAST" show instances --raw && python3 -I -B -c "$SESSION" instances "$D/instances-apres.json" >/dev/null; then
            printf 'machine_refusee %s\n' "$(champ machine_proposee "$D/lancement.txt")" >> "$D/lancement.txt"
            echo "OFFRE REFUSÉE À LA CRÉATION (retirée ?) : aucune instance iib ; machine exclue ; rang suivant : bash $DEPOT/scripts/lancer_iib_v1.sh creation auto $(champ carte "$D/lancement.txt") $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")"; exit 5
        fi
    fi
    echo "CRÉATION INCERTAINE (code $C, identifiant « ${ID:-aucun} ») : vérifier l'inventaire (champs filtrés) ; aucune seconde création avant"; exit 4 ;;
surveillance)
    ID="${2:?identifiant}"; D="${3:?dossier}"; FACT="${4:-}"
    [[ "$ID" =~ ^[0-9]+$ ]] || { echo "identifiant : chiffres seuls (R10)"; exit 2; }
    [ -f "$D/lancement.txt" ] || { echo "dossier sans lancement.txt"; exit 2; }
    [ "$(champ instance "$D/lancement.txt")" = "$ID" ] || { echo "identifiant $ID ≠ instance créée d'après $D/lancement.txt (R10)"; exit 2; }
    CR=$(champ creation "$D/lancement.txt"); PC=$(champ prix_carte "$D/lancement.txt"); PS=$(champ prix_stockage "$D/lancement.txt")
    TEL=$(champ telechargement_forfait "$D/lancement.txt"); ANT=$(champ anterieure "$D/lancement.txt"); PLC=$(champ plafond_creation "$D/lancement.txt")
    [[ "$CR" =~ ^[0-9]+$ ]] && [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] && [ -n "$ANT" ] && [ -n "$PLC" ] || { echo "création, prix, plafond ou dépense antérieure illisibles dans lancement.txt"; exit 2; }
    JGH="${CONTROLE_IA_GITHUB_TOKEN:-${CONTROLE_IA_GITHUB_TOKEN_2:-}}"
    [ "${#JGH}" -ge 8 ] || { echo "jeton GitHub absent ou trop court : masquage impossible, surveillance refusée"; exit 2; }
    HF_L="${HF_TOKEN:-}"
    [ "$(champ mode "$D/lancement.txt")" = jouet ] || [ "${#HF_L}" -ge 8 ] || { echo "HF_TOKEN absent ou trop court (mode réel) : surveillance refusée"; exit 2; }
    for K in HF_TOKEN CONTROLE_IA_GITHUB_TOKEN CONTROLE_IA_GITHUB_TOKEN_2 GH_TOKEN VAST_API_KEY; do
        V="${!K:-}"; { [ -z "$V" ] || [ "${#V}" -ge 8 ]; } || { echo "$K présente mais de moins de 8 caractères : surveillance refusée"; exit 2; }
    done
    command -v "$VAST" >/dev/null || { echo "outil de location introuvable : surveillance aveugle, arrêt"; exit 2; }
    : >> "$D/progres.txt"
    INTERVALLE="${INTERVALLE:-60}"; ILLISIBLES=0
    echo "surveillance iib v1 de $ID : création $CR, carte $PC USD/h, stockage $PS USD/h, plafond de la configuration $PLC USD ; alerte après 2 h sans PROGRES ; aucune autre instance lue au-delà des champs filtrés ni touchée" >> "$D/surveillance.txt"
    while true; do
        now=$(date -u +%s)
        timeout -k 5 120 "$VAST" logs "$ID" --tail 20000 2>&1 | masquer > "$D/journal-dernier.tmp"; PSJ=("${PIPESTATUS[@]}")
        if [ "${PSJ[1]:-1}" = 0 ] && [ "${PSJ[0]}" = 0 ]; then
            mv -f "$D/journal-dernier.tmp" "$D/journal-dernier.txt"
            grep -q '^AMORCE ' "$D/journal-dernier.txt" && cp -f "$D/journal-dernier.txt" "$D/journal-instance.txt"
            grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"; done
        else
            rm -f "$D/journal-dernier.tmp"; echo "$(date -u +%FT%TZ) ALERTE journal illisible ou masquage en échec : dernier relevé gardé" >> "$D/surveillance.txt"
        fi
        if DEC=$(python3 -I -B -c "$SESSION3" surveillance "$PLC" "$D/progres.txt" "$now" "$PC" "$PS" "$CR" "$ANT" "$TEL" ${FACT:+"$FACT"} 2>&1); then ILLISIBLES=0
        else
            ILLISIBLES=$((ILLISIBLES + 1))
            if [ "$ILLISIBLES" -ge 3 ]; then DEC="ARRET garde : garde de dépense illisible trois fois de suite ($DEC)"; else DEC="ALERTE garde de dépense illisible ($ILLISIBLES/3) : $DEC"; fi
        fi
        echo "$(date -u +%FT%TZ) $DEC" >> "$D/surveillance.txt"
        case "$DEC" in
            ARRET*) echo "$DEC"; echo "ARRÊT PAR L'IDENTIFIANT (R10) : timeout -k 5 120 $VAST stop instance $ID"; exit 3 ;;
            FIN*) echo "$DEC"; echo "FIN : instance à arrêter par son identifiant (disque gardé jusqu'au rapatriement vérifié) : timeout -k 5 120 $VAST stop instance $ID"; exit 0 ;;
            REFUS*) echo "$DEC"; exit 4 ;;
            ALERTE*) echo "$(date -u +%FT%TZ) $DEC" ;;
        esac
        sleep "$INTERVALLE"
    done ;;
*) echo "usage : --verifier-go-seulement | controles-explo | creation | apres-creation | surveillance" >&2; exit 2 ;;
esac
