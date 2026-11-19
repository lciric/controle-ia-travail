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
#
# VERSION 2 (nom neuf, R12 ; `scripts/lancer_iib_v1.sh`, cité par l'ordre scellé de la première course, reste tel quel). Trois défauts de
# forme relevés le 19 novembre 2026 pendant la première course, corrigés ici ; essais : `tests/test_iib_lanceur_forme_v2.py` (faux outil
# de location, aucun réseau, aucune instance) :
#  (1) chemin de l'outil de location (R-3683) : la variable VAST, si elle est donnée, est un CHEMIN explicite de l'outil ; il est vérifié
#      (fichier présent, exécutable, rend sa version), rendu absolu, écrit dans le journal de la session et porté dans toutes les commandes
#      imprimées ; introuvable ou muet : refus clair (code 2). Sans VAST : comme la v1, recherche de `vastai` dans le PATH, refus s'il est
#      introuvable ; la version est demandée et consignée, sans refus si elle n'est pas rendue (comportement de la v1 gardé).
#  (2) réponse brute du loueur (R-3687, R-3661) : `apres-creation` ne supprime plus rien. La réponse est conservée dans tous les cas,
#      « création incertaine » comprise : copie datée dans `DOSSIER/traces-location/`, avec son empreinte compagnon ; les secrets y sont
#      masqués par programme (valeurs des clés de l'environnement, motifs de jeton, champs nommés clé, jeton, mot de passe), le nombre de
#      masques est dit ; le fichier d'origine est remplacé par sa forme masquée (rien d'autre n'en est retiré) ; si le masquage échoue,
#      il est laissé tel quel et le programme le dit. Les inventaires, la liste des offres et les sorties de la destruction sont versés au
#      même dossier ; une sortie dont le masquage échoue est gardée sous un nom daté au lieu d'être supprimée.
#  (3) destruction (R-3722) : sous-commande neuve `destruction`, par le seul identifiant créé (R10), avec l'option de confirmation non
#      interactive de l'outil (`-y`), entrée standard fermée ; puis l'inventaire est relu et l'identifiant doit en être absent ; tout
#      échec est dit, avec un code propre, sans repli.
# Usage :
#   bash scripts/lancer_iib_v2.sh outil                                                              (vérifie l'outil de location ; 0 ou 2)
#   bash scripts/lancer_iib_v2.sh --verifier-go-seulement PLAFOND [DEPENSE_ANTERIEURE] [JOUR]       (rien n'est créé ; code 0 ou 2)
#   bash scripts/lancer_iib_v2.sh controles-explo DOSSIER_NEUF COMMIT CONFIG_CHEMIN [JOUR]            (code 0 ; 2 tout échec)
#   bash scripts/lancer_iib_v2.sh creation auto course|relance DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]
#        (imprime la commande de création ; code 0 ; 2 échec ; 3 nœud : aucune offre conforme, instance iib présente, dépense épuisée)
#   bash scripts/lancer_iib_v2.sh apres-creation FICHIER CODE DOSSIER
#        (0 créée ; 5 offre refusée, rang suivant ; 4 création incertaine ; la réponse brute est conservée dans les trois cas)
#   bash scripts/lancer_iib_v2.sh surveillance ID DOSSIER [FACTURE_USD]
#   bash scripts/lancer_iib_v2.sh destruction ID DOSSIER
#        (0 détruite et absente de l'inventaire, ou déjà absente ; 2 refus, aucun appel de destruction ; 6 instance encore à l'inventaire ;
#         4 incertain : inventaire illisible, ou commande en échec alors que l'instance est absente)
# Variables : GO_ID, IIB_REGISTRE_GO, IIB_REGISTRE_DECISIONS, IIB_BRANCHE_CODE (prep/…), IIB_BRANCHE (défaut essai/iib-explo-v1),
# IIB_DEPENSE_ANTERIEURE_USD, IIB_TESTS_ATTENDUS (^[0-9]*$), IIB_DEPOT, IIB_IMAGE, VAST (chemin explicite de l'outil de location),
# INTERVALLE, IIB_DESTRUCTION_RELECTURES (défaut 6) et IIB_DESTRUCTION_ATTENTE_S (défaut 10) ; HF_TOKEN (mode réel),
# CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2 (présence seulement, jamais affichés).
set -uo pipefail
QUOI="${1:?outil, --verifier-go-seulement, controles-explo, creation, apres-creation, surveillance ou destruction}"
MOI=scripts/lancer_iib_v2.sh
DEPOT="${IIB_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"
A=scripts/amorce_instance_iib_v1.sh
BRANCHE="${IIB_BRANCHE:-essai/iib-explo-v1}"
GO_ID_ENV="${GO_ID:-}"
REG="${IIB_REGISTRE_GO:-}"
REGDEC="${IIB_REGISTRE_DECISIONS:-}"; [ -n "$REGDEC" ] || { [ -n "$REG" ] && REGDEC="$(dirname "$REG")/decisions.md"; }
MOTIF_GO='^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$'
IMAGE="${IIB_IMAGE:-python:3.11-bookworm}"
VAST_DONNE="${VAST:-}"; VAST=""; VAST_VERSION=""; VAST_ORIGINE=""
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
horodate() { date -u +%Y%m%dT%H%M%SZ; }
# Outil de location (défaut 1, R-3683). Avec VAST : chemin explicite, vérifié, jamais cherché ailleurs. Sans VAST : `vastai` du PATH.
# Rend 0 et fixe VAST (chemin absolu), VAST_VERSION, VAST_ORIGINE ; sinon écrit la raison et rend 1. Aucun autre appel que `--version`.
resoudre_outil() {
    local v
    if [ -n "$VAST_DONNE" ]; then
        VAST_ORIGINE="variable VAST"
        case "$VAST_DONNE" in */*) ;; *) echo "outil de location introuvable : VAST=« $VAST_DONNE » n'est pas un chemin (un chemin explicite est exigé, par exemple /home/user/outil-vastai-v1/bin/vastai ; sans VAST, l'outil est cherché dans le PATH)"; return 1;; esac
        [ -f "$VAST_DONNE" ] || { echo "outil de location introuvable : VAST=« $VAST_DONNE » n'existe pas ou n'est pas un fichier"; return 1; }
        [ -x "$VAST_DONNE" ] || { echo "outil de location inutilisable : VAST=« $VAST_DONNE » n'est pas exécutable"; return 1; }
        VAST=$(realpath -- "$VAST_DONNE") || { echo "outil de location : chemin « $VAST_DONNE » illisible"; return 1; }
        v=$(timeout -k 5 60 "$VAST" --version </dev/null 2>&1 | head -1 | masquer); local ps=("${PIPESTATUS[@]}")
        [ "${ps[0]}" = 0 ] && [ -n "$v" ] || { echo "outil de location inutilisable : « $VAST --version » ne rend pas sa version (code ${ps[0]})"; return 1; }
        VAST_VERSION="$v"
    else
        VAST_ORIGINE="PATH"
        VAST=$(command -v vastai) || { VAST=""; echo "outil de location introuvable dans le PATH (donner son chemin par VAST=/chemin/vers/vastai)"; return 1; }
        v=$(timeout -k 5 60 "$VAST" --version </dev/null 2>/dev/null | head -1 | masquer) || v=""
        VAST_VERSION="${v:-non rendue}"
    fi
    case "$VAST" in *[!A-Za-z0-9_./+-]*) echo "outil de location : le chemin « $VAST » porte un caractère hors de [A-Za-z0-9_./+-] ; il ne peut pas être écrit dans une commande imprimée : refus"; return 1;; esac
    return 0
}
ligne_outil() { echo "outil de location employé : $VAST (version : $VAST_VERSION ; trouvé par : $VAST_ORIGINE)"; }
# Masquage d'une réponse du loueur avant conservation (défaut 2, R-3687) : valeurs des clés de l'environnement, puis motifs.
# Lit l'entrée standard, écrit la forme masquée sur la sortie standard et le nombre de masques dans le fichier donné.
masquer_reponse() { python3 -c '
import os, re, sys
t = sys.stdin.buffer.read().decode("utf-8", "replace")
n = 0
for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "CONTROLE_IA_GITHUB_TOKEN_2", "GH_TOKEN", "VAST_API_KEY", "CONTAINER_API_KEY"):
    v = os.environ.get(k)
    if v and len(v) >= 8:
        n += t.count(v); t = t.replace(v, "***")
NOM = r"[A-Za-z0-9_]*(?:TOKEN|KEY|SECRET|PASSWORD|PASSWD|CREDENTIAL|token|key|secret|password|passwd|credential)[A-Za-z0-9_]*"
motifs = [
    (r"\b(?:hf_[A-Za-z0-9]{8,}|gh[pousr]_[A-Za-z0-9]{8,}|github_pat_[A-Za-z0-9_]{8,})", "***"),
    (r"(?i)(\bBearer\s+)[A-Za-z0-9._~+/=-]{8,}", r"\1***"),
    (r"([\"\x27]" + NOM + r"[\"\x27]\s*:\s*[\"\x27])[^\"\x27]+([\"\x27])", r"\1***\2"),
    (r"(\b" + NOM + r"=)(?!\*\*\*)[^\s\"\x27,;&}\\]+", r"\1***"),
]
for motif, par in motifs:
    t, k = re.subn(motif, par, t); n += k
open(sys.argv[1], "w", encoding="utf-8").write(str(n) + "\n")
sys.stdout.write(t)' "$1"; }
# Conservation (R-3661) : copie datée d'un fichier déjà masqué dans DOSSIER/traces-location/, empreinte compagnon ; jamais d'écrasement.
# Écrit le chemin de la copie ; rend 1 si la copie ou l'empreinte manque.
conserver() {  # fichier source, dossier de la session, nom de base, extension
    local src="$1" dt="$2/traces-location" base="$3" ext="$4" cible k=0
    mkdir -p "$dt" || return 1
    cible="$dt/$base-$(horodate).$ext"
    while [ -e "$cible" ]; do k=$((k + 1)); cible="$dt/$base-$(horodate)-$k.$ext"; done
    cp -- "$src" "$cible" || return 1
    ( cd "$dt" && sha256sum -- "$(basename "$cible")" > "$(basename "$cible").sha256" ) || return 1
    [ "$(sha256sum < "$src" | cut -d' ' -f1)" = "$(cut -d' ' -f1 "$cible.sha256")" ] || return 1
    printf '%s\n' "$cible"
}
vast_masque() {
    local sortie="$1"; shift
    "$@" 2>/dev/null </dev/null | masquer > "$sortie.tmp"
    local ps=("${PIPESTATUS[@]}")
    if [ "${ps[1]:-1}" != 0 ]; then mv -f -- "$sortie.tmp" "$sortie.masquage-en-echec-$(horodate)" 2>/dev/null; return 121; fi   # gardée, jamais supprimée
    mv -f "$sortie.tmp" "$sortie"
    [ -d "$(dirname "$sortie")" ] && conserver "$sortie" "$(dirname "$sortie")" "$(basename "${sortie%.json}")" json >/dev/null || echo "ALERTE : sortie $(basename "$sortie") non versée aux traces de la location" >&2
    return "${ps[0]}"
}
# Identifiants des instances d'un inventaire (liste, ou {"instances": liste ou null}) : « present », « absent », code 1 si illisible.
presence_instance() { python3 -I -B -c 'import json, sys
try:
    brut = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception as e:
    print("inventaire illisible : " + type(e).__name__); sys.exit(1)
liste = brut.get("instances") if isinstance(brut, dict) and "instances" in brut else brut
if liste is None:
    liste = []
if not isinstance(liste, list) or not all(isinstance(i, dict) and "id" in i for i in liste):
    print("inventaire illisible : ni une liste d instances à identifiant, ni {instances: …}"); sys.exit(1)
print("present" if any(str(i["id"]) == sys.argv[2] for i in liste) else "absent")' "$1" "$2"; }
jeton_gh_nom() { if [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN; elif [ -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN_2; else return 1; fi; }
champ() { sed -n "s/^$1 //p" "$2" | tail -1; }
cle_config() { python3 -I -B -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8"))
for k in sys.argv[2].split("."):
    c = c[k]
print(c if not isinstance(c, bool) else ("oui" if c else "non"))' "$1" "$2"; }
exiger_go_env() { [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN : la ligne de GO de calcul de la course) : rien créé"; exit 2; }; }
exiger_registre() { [ -n "$REG" ] && [ -f "$REG" ] || { echo "IIB_REGISTRE_GO : registres/go.md d'un clone de main exigé : rien créé"; exit 2; }; }
case "$QUOI" in
outil)
    MSG=$(resoudre_outil) || { echo "$MSG : refus"; exit 2; }; resoudre_outil >/dev/null
    echo "OUTIL DE LOCATION VÉRIFIÉ, RIEN CRÉÉ : $(ligne_outil)" ;;
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
    MSG=$(resoudre_outil) || { echo "$MSG : pas de création"; exit 2; }; resoudre_outil >/dev/null
    ligne_outil; printf 'outil_location %s\noutil_location_version %s\n' "$VAST" "$VAST_VERSION" >> "$D/lancement.txt"
    DISQUE=$(cle_config "$D/config.json" offre.disque_min_go) || { echo "disque illisible"; exit 2; }
    [[ "$DISQUE" =~ ^[0-9]+([.][0-9]+)?$ ]] && [ "${DISQUE%%.*}" -gt 0 ] || { echo "offre.disque_min_go illisible ($DISQUE) : pas de création"; exit 2; }
    ESSAIS=$(grep -c '^essai_creation ' "$D/lancement.txt" || true)
    [ "${ESSAIS:-0}" -lt 3 ] || { echo "trois essais de création déjà faits : arrêt, aucune création ; message à la mère"; exit 3; }
    EXCL=$(sed -n 's/^machine_refusee //p' "$D/lancement.txt" | paste -sd, -)
    FILTRE=$(python3 -I -B -c "$SESSION" filtre "$D/config.json" "$CARTE") || { echo "filtre illisible : $FILTRE"; exit 2; }
    timeout -k 5 120 "$VAST" search offers "$FILTRE" -o dph_total --storage "$DISQUE" --raw > "$D/offres.json" 2>"$D/offres.err" </dev/null || { echo "recherche filtrée impossible : pas de création"; exit 2; }
    conserver "$D/offres.json" "$D" offres json >/dev/null || echo "ALERTE : liste des offres non versée aux traces de la location"
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
    CMD="GO_ID=$GOC timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT=$S -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e IIB_GO_ID=$GOC -e MODE=$MODE_C -e PREREG_ABSENT=1 -e CONFIG=$(champ config "$D/lancement.txt") -e TESTS_ATTENDUS=$TA -e ECHEANCE_UTC_S=$ECH -e FIN_GO_UTC_S=$FIN_GO -e DEPENSE_EPUISEE_UTC_S=$EPUIS -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$$JGHN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh\" > \"$D/creation-brute.json\" 2>&1 </dev/null; VAST=$VAST bash $DEPOT/$MOI apres-creation \"$D/creation-brute.json\" \$? \"$D\""
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
    [ -d "$D" ] || { echo "CRÉATION INCERTAINE (code $C) : dossier de la session $D absent ; réponse brute laissée telle quelle à $F ; vérifier l'inventaire (champs filtrés) ; aucune seconde création avant"; exit 4; }
    # Conservation de la réponse brute AVANT toute lecture et tout verdict (R-3687, R-3661) : rien n'est supprimé.
    if [ -f "$F" ]; then
        MASQUEE="$D/creation-brute-masquee.tmp"; NBM="$D/creation-brute-nombre-de-masques.txt"; : > "$NBM"
        if masquer_reponse "$NBM" < "$F" > "$MASQUEE" && [ -s "$NBM" ]; then
            NM=$(cat "$NBM")
            if COPIE=$(conserver "$MASQUEE" "$D" creation-brute json); then
                mv -f -- "$MASQUEE" "$F"      # l'original est remplacé par sa forme masquée : seuls les secrets en sont retirés
                echo "RÉPONSE BRUTE DU LOUEUR CONSERVÉE : $COPIE (empreinte $(cut -d' ' -f1 "$COPIE.sha256")) ; secrets masqués par programme avant conservation : $NM remplacement(s) ; l'original $F porte la même forme masquée"
                printf 'reponse_creation %s %s masques=%s\n' "$COPIE" "$(cut -d' ' -f1 "$COPIE.sha256")" "$NM" >> "$D/lancement.txt"
            else
                echo "ALERTE : copie datée de la réponse brute impossible dans $D/traces-location ; forme masquée gardée à $MASQUEE ; original $F laissé tel quel, NON MASQUÉ : ne pas le verser avant la garde des secrets"
            fi
        else
            echo "ALERTE : masquage de la réponse brute en échec : aucune copie faite ; original $F laissé tel quel, NON MASQUÉ : ne pas le verser avant la garde des secrets"
        fi
        EXTRAIT=$(python3 -I -B -c 'import json, re, sys
t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
vus = []
for cle in ("success", "new_contract", "error", "msg"):
    m = re.search(r"[\"\x27]?" + cle + r"[\"\x27]?\s*:\s*([^,}\n]*)", t)
    vus.append(cle + "=" + (m.group(1).strip()[:300] if m else "absent"))
print(" ; ".join(vus) + " ; taille " + str(len(t)) + " caractères")' "$F" 2>/dev/null | masquer) || EXTRAIT=""
        echo "champs lus par programme dans la réponse (tronqués à 300 caractères, masqués) : ${EXTRAIT:-extraction impossible}"
    else
        echo "ALERTE : réponse brute du loueur absente ($F n'est pas un fichier) : rien à conserver, rien à lire"
    fi
    ID=$(grep -oE "new_contract['\"]?[[:space:]]*:[[:space:]]*[0-9]+" "$F" 2>/dev/null | grep -oE '[0-9]+$' | head -1 || true)
    OK=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(True|true)" "$F" 2>/dev/null || true)
    NON=$(grep -cE "success['\"]?[[:space:]]*:[[:space:]]*(False|false)" "$F" 2>/dev/null || true)
    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then
        CR=$(date +%s); printf 'instance %s\ncreation %s\n' "$ID" "$CR" >> "$D/lancement.txt"
        echo "CRÉÉE : instance $ID (création $CR) ; surveillance : bash $MOI surveillance $ID $D"; exit 0
    fi
    if [ -z "$ID" ] && [ "${NON:-0}" -ge 1 ] && [ "${OK:-0}" -eq 0 ]; then
        MSG=$(resoudre_outil) || { echo "CRÉATION INCERTAINE (code $C, refus lu dans la réponse) : $MSG : inventaire non relu ; vérifier l'inventaire (champs filtrés) ; aucune seconde création avant"; exit 4; }; resoudre_outil >/dev/null
        ligne_outil
        if vast_masque "$D/instances-apres.json" timeout -k 5 120 "$VAST" show instances --raw && python3 -I -B -c "$SESSION" instances "$D/instances-apres.json" >/dev/null; then
            printf 'machine_refusee %s\n' "$(champ machine_proposee "$D/lancement.txt")" >> "$D/lancement.txt"
            echo "OFFRE REFUSÉE À LA CRÉATION (retirée ?) : aucune instance iib ; machine exclue ; rang suivant : VAST=$VAST bash $DEPOT/$MOI creation auto $(champ carte "$D/lancement.txt") $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")"; exit 5
        fi
    fi
    echo "CRÉATION INCERTAINE (code $C, identifiant « ${ID:-aucun} ») : la réponse brute est conservée (lignes ci-dessus) ; vérifier l'inventaire (champs filtrés) ; aucune seconde création avant"; exit 4 ;;
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
    MSG=$(resoudre_outil) || { echo "$MSG : surveillance aveugle, arrêt"; exit 2; }; resoudre_outil >/dev/null
    : >> "$D/progres.txt"
    echo "$(date -u +%FT%TZ) $(ligne_outil)" >> "$D/surveillance.txt"
    INTERVALLE="${INTERVALLE:-60}"; ILLISIBLES=0
    echo "surveillance iib v1 de $ID : création $CR, carte $PC USD/h, stockage $PS USD/h, plafond de la configuration $PLC USD ; alerte après 2 h sans PROGRES ; aucune autre instance lue au-delà des champs filtrés ni touchée" >> "$D/surveillance.txt"
    while true; do
        now=$(date -u +%s)
        timeout -k 5 120 "$VAST" logs "$ID" --tail 20000 2>&1 </dev/null | masquer > "$D/journal-dernier.tmp"; PSJ=("${PIPESTATUS[@]}")
        if [ "${PSJ[1]:-1}" = 0 ] && [ "${PSJ[0]}" = 0 ]; then
            mv -f "$D/journal-dernier.tmp" "$D/journal-dernier.txt"
            grep -q '^AMORCE ' "$D/journal-dernier.txt" && cp -f "$D/journal-dernier.txt" "$D/journal-instance.txt"
            grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"; done
        else
            if [ "${PSJ[1]:-1}" = 0 ] && [ -s "$D/journal-dernier.tmp" ]; then mv -f -- "$D/journal-dernier.tmp" "$D/journal-illisible-dernier.txt"      # masqué : gardé, jamais supprimé
            else mv -f -- "$D/journal-dernier.tmp" "$D/journal-masquage-en-echec-$(horodate).tmp" 2>/dev/null; fi
            echo "$(date -u +%FT%TZ) ALERTE journal illisible ou masquage en échec : dernier relevé gardé" >> "$D/surveillance.txt"
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
destruction)
    # Défaut 3 (R-3722) : destruction du seul identifiant créé (R10), option de confirmation non interactive, puis preuve par l'inventaire.
    ID="${2:?identifiant}"; D="${3:?dossier}"
    [[ "$ID" =~ ^[0-9]+$ ]] || { echo "identifiant : chiffres seuls (R10) : aucune destruction"; exit 2; }
    [ -f "$D/lancement.txt" ] || { echo "dossier sans lancement.txt : aucune destruction"; exit 2; }
    [ "$(champ instance "$D/lancement.txt")" = "$ID" ] || { echo "identifiant $ID ≠ instance créée d'après $D/lancement.txt (R10) : aucune destruction"; exit 2; }
    RELECTURES="${IIB_DESTRUCTION_RELECTURES:-6}"; ATTENTE="${IIB_DESTRUCTION_ATTENTE_S:-10}"
    [[ "$RELECTURES" =~ ^[1-9][0-9]*$ ]] && [[ "$ATTENTE" =~ ^[0-9]+$ ]] || { echo "IIB_DESTRUCTION_RELECTURES (entier ≥ 1) ou IIB_DESTRUCTION_ATTENTE_S (entier ≥ 0) illisible : aucune destruction"; exit 2; }
    MSG=$(resoudre_outil) || { echo "$MSG : aucune destruction"; exit 2; }; resoudre_outil >/dev/null
    ligne_outil
    JD="$D/destruction.txt"; echo "$(date -u +%FT%TZ) destruction demandée de l'instance $ID ; $(ligne_outil)" >> "$JD"
    vast_masque "$D/instances-avant-destruction.json" timeout -k 5 120 "$VAST" show instances --raw; c_inv=$?
    [ "$c_inv" = 0 ] && AVANT=$(presence_instance "$D/instances-avant-destruction.json" "$ID") \
        || { echo "$(date -u +%FT%TZ) inventaire d'avant illisible (code $c_inv ; ${AVANT:-})" >> "$JD"; echo "DESTRUCTION NON TENTÉE : inventaire d'avant illisible (code $c_inv ; ${AVANT:-masquage ou appel en échec}) : aucune destruction ; à relire"; exit 4; }
    if [ "$AVANT" = absent ]; then
        echo "$(date -u +%FT%TZ) instance $ID déjà absente de l'inventaire : aucune commande de destruction envoyée" >> "$JD"
        printf 'destruction_verifiee %s deja_absente\n' "$(date +%s)" >> "$D/lancement.txt"
        echo "INSTANCE $ID DÉJÀ ABSENTE DE L'INVENTAIRE : aucune commande de destruction envoyée"; exit 0
    fi
    echo "commande de destruction (par l'identifiant, R10 ; confirmation non interactive) : timeout -k 5 120 $VAST destroy instance $ID -y"
    timeout -k 5 120 "$VAST" destroy instance "$ID" -y </dev/null 2>&1 | masquer > "$D/destruction-sortie.tmp"; PSD=("${PIPESTATUS[@]}")
    CD="${PSD[0]}"
    if [ "${PSD[1]:-1}" = 0 ]; then
        SORTIE=$(conserver "$D/destruction-sortie.tmp" "$D" destruction-sortie txt) && mv -f -- "$D/destruction-sortie.tmp" "$D/destruction-sortie.txt" || SORTIE="$D/destruction-sortie.tmp (non versée aux traces)"
    else SORTIE="$D/destruction-sortie.tmp (masquage en échec : à ne pas verser avant la garde des secrets)"; fi
    echo "$(date -u +%FT%TZ) destroy instance $ID -y : code $CD ; sortie $SORTIE" >> "$JD"
    echo "commande de destruction : code $CD ; sortie conservée : $SORTIE"
    APRES=""; n=0
    while [ "$n" -lt "$RELECTURES" ]; do
        n=$((n + 1))
        vast_masque "$D/instances-apres-destruction.json" timeout -k 5 120 "$VAST" show instances --raw; c_inv=$?
        if [ "$c_inv" = 0 ] && APRES=$(presence_instance "$D/instances-apres-destruction.json" "$ID"); then :; else APRES="illisible (code $c_inv ; ${APRES:-})"; fi
        echo "$(date -u +%FT%TZ) relecture $n/$RELECTURES de l'inventaire : instance $ID $APRES" >> "$JD"
        [ "$APRES" = absent ] && break
        [ "$n" -lt "$RELECTURES" ] && sleep "$ATTENTE"
    done
    case "$APRES" in
        absent)
            if [ "$CD" = 0 ]; then
                printf 'destruction_verifiee %s\n' "$(date +%s)" >> "$D/lancement.txt"
                echo "DÉTRUITE : instance $ID absente de l'inventaire (relecture $n/$RELECTURES) ; commande de destruction rendue avec le code 0"; exit 0
            fi
            echo "DESTRUCTION INCERTAINE : la commande de destruction a échoué (code $CD) alors que l'instance $ID est absente de l'inventaire (relecture $n/$RELECTURES) : à relire, sortie $SORTIE"; exit 4 ;;
        present)
            if [ "$CD" = 0 ]; then echo "DESTRUCTION NON OBTENUE : la commande a rendu le code 0 mais l'instance $ID est encore à l'inventaire après $n relecture(s) : elle coûte encore ; message à la mère ; sortie $SORTIE"
            else echo "DESTRUCTION EN ÉCHEC : la commande a rendu le code $CD et l'instance $ID est encore à l'inventaire après $n relecture(s) : elle coûte encore ; message à la mère ; sortie $SORTIE"; fi
            exit 6 ;;
        *) echo "DESTRUCTION INCERTAINE : commande de destruction rendue avec le code $CD, inventaire $APRES après $n relecture(s) : l'absence de l'instance $ID n'est pas établie ; à relire ; sortie $SORTIE"; exit 4 ;;
    esac ;;
*) echo "usage : outil | --verifier-go-seulement | controles-explo | creation | apres-creation | surveillance | destruction" >&2; exit 2 ;;
esac
