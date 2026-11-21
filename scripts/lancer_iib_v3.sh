#!/usr/bin/env bash
# Lanceur de session de l'organisme retenu du saboteur à budget, version 3 : `scripts/lancer_iib_v2.sh` (intact, R12) avec ces
# seuls changements : l'amorce citée est `scripts/amorce_instance_iib_v5.sh` ; la configuration est vérifiée par `iib/session_v5`
# (`configuration_v5`), les autres contrôles de session restant ceux de `session_v1` ; les tâches sont lues sous `pieces.` ;
# branche par défaut `essai/iib-explo-v5`. Écrit, jamais lancé par son développeur ; les essais de forme de la version 2 ne
# sont pas rejoués sur lui (ils dépendent de la configuration de la version 1) : à contre-lire et à éprouver avant l'ordre.
# --- en-tête d'origine de la version 2 :
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
#      « création incertaine » comprise : copie datée dans `DOSSIER/traces-location/`, avec son empreinte compagnon, jamais écrasée.
#      Les secrets y sont masqués par programme (`src/controle_ia/iib/location_v1.py` : par analyse de la structure si la réponse est du
#      JSON, par motifs sinon ; clés nommées, paires `["NOM", "valeur"]`, formes échappées, jetons à préfixe) et le nombre de masques est
#      dit. Si le masquage échoue, la sortie brute est gardée ENTIÈRE dans un fichier « NON-MASQUE », aux droits restreints, et le
#      programme le dit. Le masquage n'est pas une garde des secrets : celle du dépôt reste exigée avant tout versement.
#      Inventaires : seuls les champs filtrés des instances du saboteur (identifiant, étiquette, état, prix, machine) vont aux traces ;
#      l'inventaire entier du compte n'est jamais conservé (le fichier de travail n'en garde qu'identifiant, étiquette, état).
#  (3) destruction (R-3722) : sous-commande neuve `destruction`, par le seul identifiant créé (R10), avec l'option de confirmation non
#      interactive de l'outil (`-y`), entrée standard fermée. Gardes avant tout appel de destruction : RAPATRIEMENT_VERIFIE=oui ;
#      identifiant hors de la liste IIB_INSTANCES_INTOUCHABLES ; inventaire lisible qui montre l'instance, avec l'étiquette posée à la
#      création, à l'arrêt. Preuve : deux relectures concordantes de l'inventaire. Un inventaire vide, illisible ou en erreur n'est
#      jamais une preuve. Tout échec est dit, avec un code propre, sans repli.
#  Corrections de la contre-lecture du 19 novembre (un bloquant, trois majeurs, huit mineurs) : l'identifiant créé se lit à la clé de
#  premier niveau `new_contract` de la réponse analysée comme JSON, jamais par un motif ; toute autre valeur candidate est un refus.
#  Erratum 1 (vérification des corrections, quatre mineurs neufs) : états d'arrêt en liste FERMÉE dans le code (aucune variable ne
#  l'élargit : une instance qui tourne n'est jamais détruite ici ; un état d'arrêt d'un autre nom est un refus, le code changera en
#  version nouvelle) ; étiquette de l'inventaire ÉGALE à celle consignée à la création ; liste des intouchables exigée non vide, sauf
#  attestation IIB_AUCUNE_INTOUCHABLE=oui ; un refus de `creation` ne consomme plus un essai ; empreinte du module de lecture vérifiée
#  avant tout emploi ; copie datée des journaux à la fin de la surveillance ; attestation du rapatriement écrite dans `lancement.txt`.
# Usage :
#   bash scripts/lancer_iib_v2.sh outil                                                              (vérifie l'outil de location ; 0 ou 2)
#   bash scripts/lancer_iib_v2.sh --verifier-go-seulement PLAFOND [DEPENSE_ANTERIEURE] [JOUR]       (rien n'est créé ; code 0 ou 2)
#   bash scripts/lancer_iib_v2.sh controles-explo DOSSIER_NEUF COMMIT CONFIG_CHEMIN [JOUR]            (code 0 ; 2 tout échec)
#   bash scripts/lancer_iib_v2.sh creation auto course|relance DEPENSE_ANTERIEURE_USD DOSSIER [ECHEANCE_UTC_S]
#        (imprime la commande de création ; code 0 ; 2 échec ; 3 nœud : aucune offre conforme, instance iib présente, dépense épuisée)
#   bash scripts/lancer_iib_v2.sh apres-creation FICHIER CODE DOSSIER
#        (0 créée ; 5 offre refusée, rang suivant ; 4 création incertaine ; la réponse brute est conservée dans les trois cas)
#   bash scripts/lancer_iib_v2.sh surveillance ID DOSSIER [FACTURE_USD]
#   RAPATRIEMENT_VERIFIE=oui bash scripts/lancer_iib_v2.sh destruction ID DOSSIER
#        (0 détruite : commande au code 0, puis absente de deux relectures concordantes de l'inventaire ; 2 refus avant tout appel de
#         destruction ; 6 instance encore à l'inventaire ; 7 instance absente de l'inventaire d'avant : absence NON confirmée, aucune
#         commande envoyée ; 4 incertain : inventaire illisible, vide de façon incohérente ou en erreur, ou commande en échec)
# Variables : GO_ID, IIB_REGISTRE_GO, IIB_REGISTRE_DECISIONS, IIB_BRANCHE_CODE (prep/…), IIB_BRANCHE (défaut essai/iib-explo-v1),
# IIB_DEPENSE_ANTERIEURE_USD, IIB_TESTS_ATTENDUS (^[0-9]*$), IIB_DEPOT, IIB_IMAGE, VAST (chemin explicite de l'outil de location),
# INTERVALLE ; pour la destruction : RAPATRIEMENT_VERIFIE (« oui » exigé : rapatriement vérifié et mot de la mère),
# IIB_INSTANCES_INTOUCHABLES (identifiants séparés par des virgules ; liste vide ou absente : refus, sauf attestation explicite
# IIB_AUCUNE_INTOUCHABLE=oui, dite au journal), IIB_DESTRUCTION_RELECTURES (défaut 6, au moins 2), IIB_DESTRUCTION_ATTENTE_S (défaut 10) ;
# IIB_LOCATION_SHA256 (empreinte attendue du module de lecture `src/controle_ia/iib/location_v1.py` ; à défaut, celle que la configuration
# de la course écrit dans sa liste des empreintes du code ; ni l'une ni l'autre, ou empreinte différente : refus) ; HF_TOKEN (mode réel),
# CONTROLE_IA_GITHUB_TOKEN ou CONTROLE_IA_GITHUB_TOKEN_2 (présence seulement, jamais affichés).
set -uo pipefail
QUOI="${1:?outil, --verifier-go-seulement, controles-explo, creation, apres-creation, surveillance ou destruction}"
MOI=scripts/lancer_iib_v3.sh
DEPOT="${IIB_DEPOT:-$(cd "$(dirname "$0")/.." && pwd)}"
A=scripts/amorce_instance_iib_v5.sh
BRANCHE="${IIB_BRANCHE:-essai/iib-explo-v5}"
GO_ID_ENV="${GO_ID:-}"
REG="${IIB_REGISTRE_GO:-}"
REGDEC="${IIB_REGISTRE_DECISIONS:-}"; [ -n "$REGDEC" ] || { [ -n "$REG" ] && REGDEC="$(dirname "$REG")/decisions.md"; }
MOTIF_GO='^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$'
IMAGE="${IIB_IMAGE:-python:3.11-bookworm}"
VAST_DONNE="${VAST:-}"; VAST=""; VAST_VERSION=""; VAST_ORIGINE=""
SESSION="import sys; sys.path.insert(0, '$DEPOT/src'); from controle_ia.iib import session_v5; sys.exit(session_v5.main(sys.argv[1:]))"
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
LOCATION="$(cd "$(dirname "$0")/.." && pwd)/src/controle_ia/iib/location_v1.py"      # à côté du lanceur, dans le même arbre (et non dans IIB_DEPOT)
MODULE_VERIFIE=non
location() { [ "$MODULE_VERIFIE" = oui ] || return 97; python3 -I -B "$LOCATION" "$@"; }
# Le module de lecture est du code de confiance, au même titre que le lanceur : son empreinte est vérifiée avant tout emploi. Empreinte
# attendue : IIB_LOCATION_SHA256, ou celle de la liste des empreintes du code de la configuration de la course (DOSSIER/config.json) ;
# les deux présentes doivent être égales. Rend 0 et fixe MODULE_VERIFIE=oui ; sinon écrit la raison et rend 1. Argument : dossier.
verifier_module() {
    local env="${IIB_LOCATION_SHA256:-}" cfg="" attendue vue
    [ -z "$env" ] || [[ "$env" =~ ^[0-9a-f]{64}$ ]] || { echo "IIB_LOCATION_SHA256 illisible (64 caractères hexadécimaux)"; return 1; }
    [ ! -f "$1/config.json" ] || cfg=$(cle_config "$1/config.json" marqueurs.EMPREINTES_CODE_IIB 2>/dev/null | grep -oE 'src/controle_ia/iib/location_v1\.py [0-9a-f]{64}' | head -1 | cut -d' ' -f2) || cfg=""
    [ -n "$env" ] || [ -n "$cfg" ] || { echo "empreinte attendue du module de lecture absente (ni IIB_LOCATION_SHA256, ni la liste des empreintes du code de la configuration)"; return 1; }
    [ -z "$env" ] || [ -z "$cfg" ] || [ "$env" = "$cfg" ] || { echo "empreinte attendue du module de lecture : IIB_LOCATION_SHA256 et la configuration se contredisent"; return 1; }
    attendue="${env:-$cfg}"
    [ -f "$LOCATION" ] || { echo "module de lecture absent ($LOCATION)"; return 1; }
    vue=$(sha256sum < "$LOCATION" | cut -d' ' -f1)
    [ "$vue" = "$attendue" ] || { echo "module de lecture $LOCATION : empreinte $vue ≠ empreinte attendue $attendue"; return 1; }
    MODULE_VERIFIE=oui
}
ETATS_ARRET="exited stopped"   # liste FERMÉE des états d'arrêt : aucune variable ne l'élargit ; un état neuf passe par une version nouvelle du code
# Fichier neuf à nom unique et daté, droits restreints (jamais d'écrasement, R12) : dossier, base, extension ; écrit le chemin.
fichier_neuf() { ( umask 077; mktemp "$1/$2-$(horodate)-XXXXXX.$3" ); }
# Mise à l'écart d'une sortie brute que le masquage n'a pas pu traiter : gardée ENTIÈRE, nom marqué, droits restreints ; écrit le chemin.
garder_non_masque() {
    local cible="$1.NON-MASQUE"
    mv -n -- "$1" "$cible" 2>/dev/null && [ ! -e "$1" ] || cible="$1"
    chmod 600 -- "$cible" 2>/dev/null
    printf '%s\n' "$cible"
}
# Conservation (R-3661) : copie datée d'un fichier déjà masqué dans DOSSIER/traces-location/, empreinte compagnon ; jamais d'écrasement
# (création exclusive, puis empreinte de la copie comparée à celle de la source). Écrit le chemin de la copie ; rend 1 si la copie ou l'empreinte manque.
conserver() {  # fichier source, dossier de la session, nom de base, extension
    local src="$1" dt="$2/traces-location" base="$3" ext="$4" cible k=0
    mkdir -p "$dt" || return 1
    cible="$dt/$base-$(horodate).$ext"
    while [ -e "$cible" ] || [ -e "$cible.sha256" ]; do k=$((k + 1)); cible="$dt/$base-$(horodate)-$k.$ext"; done
    ( set -o noclobber; cat -- "$src" > "$cible" ) 2>/dev/null || return 1      # création exclusive : une trace n'est jamais écrasée
    [ "$(sha256sum < "$src" | cut -d' ' -f1)" = "$(sha256sum < "$cible" | cut -d' ' -f1)" ] || return 1     # une autre écriture a pris le nom : refus
    ( cd "$dt" && [ ! -e "$(basename "$cible").sha256" ] && sha256sum -- "$(basename "$cible")" > "$(basename "$cible").sha256" ) || return 1
    printf '%s\n' "$cible"
}
# Masquage sur place d'une sortie brute déjà écrite sur disque (jamais dans un tube : rien n'est perdu si le masquage échoue).
# Rend 0 et fixe NB_MASQUES et MODE_MASQUE ; sinon rend 1, le fichier n'est pas touché.
masquer_fichier() {
    local r
    r=$(location masquer-en-place "$1" 2>/dev/null) || return 1
    NB_MASQUES="${r%% *}"; MODE_MASQUE="${r##* }"
    [[ "$NB_MASQUES" =~ ^[0-9]+$ ]] || return 1
}
# Inventaire du compte, lu par programme. Arguments : dossier de la session, nom de base, identifiant visé (ou vide), fichier réduit
# d'avant (ou vide). La sortie brute va d'abord sur disque (droits restreints) ; en succès elle est remplacée par une forme réduite
# (identifiant, étiquette, état de chaque instance) et seuls les champs filtrés des instances du saboteur vont aux traces ; la sortie
# d'erreur est gardée, masquée. Fixe INV_FICHIER (forme réduite), INV_LIGNE (n= etat= etiquette= statut= autres_manquants=), INV_ERR.
# Rend 0 ; 122 si l'appel a échoué ; 121 si l'inventaire est illisible (sortie brute alors gardée entière, marquée, non versée).
inventaire_lu() {
    local d="$1" base="$2" id="$3" avant="$4" c trace
    INV_LIGNE=""; INV_ERR=""
    INV_FICHIER=$(fichier_neuf "$d" "$base" json) || { INV_LIGNE="fichier de travail impossible dans $d"; return 121; }
    INV_ERR="${INV_FICHIER%.json}.err"
    timeout -k 5 120 "$VAST" show instances --raw > "$INV_FICHIER" 2> "$INV_ERR" </dev/null; c=$?
    chmod 600 -- "$INV_ERR" 2>/dev/null
    if [ -s "$INV_ERR" ]; then masquer_fichier "$INV_ERR" || INV_ERR=$(garder_non_masque "$INV_ERR"); fi
    if [ "$c" != 0 ]; then
        masquer_fichier "$INV_FICHIER" || INV_FICHIER=$(garder_non_masque "$INV_FICHIER")
        INV_LIGNE="appel de l'inventaire en échec (code $c) ; sortie gardée, NON VERSÉE : $INV_FICHIER ; sortie d'erreur : $INV_ERR"; return 122
    fi
    mkdir -p "$d/traces-location" && trace="$d/traces-location/$(basename "${INV_FICHIER%.json}")-champs-filtres.json" \
        && INV_LIGNE=$(location inventaire "$INV_FICHIER" "$trace" "$PREFIXE_ETIQUETTE" ${id:+"$id"} ${avant:+"$avant"} 2>/dev/null) \
        && ( cd "$d/traces-location" && sha256sum -- "$(basename "$trace")" > "$(basename "$trace").sha256" ) && return 0
    INV_FICHIER=$(garder_non_masque "$INV_FICHIER")
    INV_LIGNE="inventaire illisible (${INV_LIGNE:-lecture par programme impossible}) ; sortie brute gardée entière, NON MASQUÉE, NON VERSÉE : $INV_FICHIER ; sortie d'erreur : $INV_ERR"; return 121
}
mot_inv() { printf '%s\n' "$INV_LIGNE" | sed -n "s/.*\b$1=\([^ ]*\).*/\1/p"; }
jeton_gh_nom() { if [ -n "${CONTROLE_IA_GITHUB_TOKEN:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN; elif [ -n "${CONTROLE_IA_GITHUB_TOKEN_2:-}" ]; then echo CONTROLE_IA_GITHUB_TOKEN_2; else return 1; fi; }
champ() { sed -n "s/^$1 //p" "$2" | tail -1; }
cle_config() { python3 -I -B -c 'import json, sys; c = json.load(open(sys.argv[1], encoding="utf-8"))
for k in sys.argv[2].split("."):
    c = c[k]
print(c if not isinstance(c, bool) else ("oui" if c else "non"))' "$1" "$2"; }
exiger_go_env() { [[ "$GO_ID_ENV" =~ $MOTIF_GO ]] || { echo "GO_ID absent ou illisible dans l'environnement (GO_ID=GO-AAAA-MM-JJ-NN : la ligne de GO de calcul de la course) : rien créé"; exit 2; }; }
exiger_registre() { [ -n "$REG" ] && [ -f "$REG" ] || { echo "IIB_REGISTRE_GO : registres/go.md d'un clone de main exigé : rien créé"; exit 2; }; }
PREFIXE_ETIQUETTE=iib          # la règle de la création : seule une instance dont l'étiquette commence par « iib » est du saboteur à budget
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
    for cle in conception taches_reserve taches_evaluation consigne_maitre_N consigne_maitre_P consigne_flagrant entrees; do
        f=$(cle_config "$D/config.json" "pieces.$cle.chemin") && h=$(cle_config "$D/config.json" "pieces.$cle.sha256") || { echo "$cle illisible"; exit 2; }
        git -C "$DEPOT" cat-file -e "$S:$f" 2>/dev/null && git -C "$DEPOT" cat-file -e "$S:$f.sha256" 2>/dev/null || { echo "fichier cité $f ou son sceau absent du commit $S"; exit 2; }
        [ "$(git -C "$DEPOT" show "$S:$f" | sha256sum | cut -d' ' -f1)" = "$h" ] && [ "$(git -C "$DEPOT" show "$S:$f.sha256" | cut -d' ' -f1)" = "$h" ] || { echo "empreinte de $f ≠ celle de la configuration (R11)"; exit 2; }
    done
    git -C "$DEPOT" show "$S:$(cle_config "$D/config.json" pieces.taches_reserve.chemin)" > "$D/reserve.json" && git -C "$DEPOT" show "$S:$(cle_config "$D/config.json" pieces.taches_evaluation.chemin)" > "$D/evaluation.json" \
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
    MSG=$(verifier_module "$D") || { echo "$MSG : pas de création"; exit 2; }; verifier_module "$D" >/dev/null
    ligne_outil; printf 'outil_location %s\noutil_location_version %s\n' "$VAST" "$VAST_VERSION" >> "$D/lancement.txt"
    DISQUE=$(cle_config "$D/config.json" offre.disque_min_go) || { echo "disque illisible"; exit 2; }
    [[ "$DISQUE" =~ ^[0-9]+([.][0-9]+)?$ ]] && [ "${DISQUE%%.*}" -gt 0 ] || { echo "offre.disque_min_go illisible ($DISQUE) : pas de création"; exit 2; }
    ESSAIS=$(grep -c '^essai_creation ' "$D/lancement.txt" || true)
    [ "${ESSAIS:-0}" -lt 3 ] || { echo "trois essais de création déjà faits : arrêt, aucune création ; message à la mère"; exit 3; }
    EXCL=$(sed -n 's/^machine_refusee //p' "$D/lancement.txt" | paste -sd, -)
    FILTRE=$(python3 -I -B -c "$SESSION" filtre "$D/config.json" "$CARTE") || { echo "filtre illisible : $FILTRE"; exit 2; }
    timeout -k 5 120 "$VAST" search offers "$FILTRE" -o dph_total --storage "$DISQUE" --raw > "$D/offres.json" 2>"$D/offres.err" </dev/null || { echo "recherche filtrée impossible : pas de création"; exit 2; }
    conserver "$D/offres.json" "$D" offres json >/dev/null || echo "ALERTE : liste des offres non versée aux traces de la location"
    [ ! -s "$D/offres.err" ] || { cp -- "$D/offres.err" "$(fichier_neuf "$D" offres-erreur err)" 2>/dev/null; true; }      # nom neuf et unique : rien n'est écrasé
    OF=$(python3 -I -B -c "$SESSION" choisir "$D/offres.json" "$D/config.json" "$CARTE" "$EXCL") || { echo "aucune offre conforme dans la liste filtrée : $OF : nœud (fenêtre : rejouer dans 15 minutes, 12 fois au plus), pas de création"; exit 3; }
    OFFRE=$(printf '%s\n' "$OF" | sed -n 's/^id=\([0-9]*\) .*/\1/p'); MACH=$(printf '%s\n' "$OF" | sed -n 's/.* machine=\([^ ]*\) .*/\1/p'); RANG=$(printf '%s\n' "$OF" | sed -n 's/.* rang=\([0-9]*\) .*/\1/p')
    [[ "$OFFRE" =~ ^[0-9]+$ ]] && [ -n "$MACH" ] && [ -n "$RANG" ] || { echo "offre choisie illisible ($OF)"; exit 2; }
    PC=$(printf '%s\n' "$OF" | sed -n 's/.*prix_carte=\([0-9.]*\).*/\1/p'); PS=$(printf '%s\n' "$OF" | sed -n 's/.*prix_stockage=\([0-9.]*\).*/\1/p')
    TEL=$(printf '%s\n' "$OF" | sed -n 's/.*telechargement_forfait=\([0-9.]*\).*/\1/p')
    [ -n "$PC" ] && [ -n "$PS" ] && [ -n "$TEL" ] || { echo "prix illisibles dans la relecture de l'offre"; exit 2; }
    ETIQ=$(cle_config "$D/config.json" offre.etiquette) || { echo "étiquette illisible"; exit 2; }
    inventaire_lu "$D" instances "" "" || { echo "inventaire des instances impossible ou illisible (code $? ; $INV_LIGNE) : pas de création"; exit 2; }
    INV=$(python3 -I -B -c "$SESSION" instances "$INV_FICHIER") || { echo "$INV : nœud, pas de création"; exit 3; }
    NOW=$(date +%s)
    DEP=$(python3 -I -B -c "$SESSION3" depense "$PLC" "$PC" "$PS" "$NOW" "$ANT" "$TEL" "$NOW"); code_dep=$?
    [ "$code_dep" = 0 ] || { echo "dépense cumulée déjà au plafond ou illisible ($DEP) : nœud, pas de création"; exit 3; }
    EPUIS=$(printf '%s\n' "$DEP" | sed -n 's/.*epuisement_utc_s=\([0-9]*\).*/\1/p'); [[ "$EPUIS" =~ ^[0-9]+$ ]] || { echo "heure d'épuisement illisible"; exit 2; }
    git -C "$DEPOT" show "$S:$A" > "$D/amorce-creation.sh" 2>/dev/null || { echo "amorce absente du commit $S"; exit 2; }
    [ "$(sha256sum "$D/amorce-creation.sh" | cut -d' ' -f1)" = "$(champ amorce "$D/lancement.txt")" ] || { echo "amorce changée depuis les contrôles"; exit 2; }
    B64=$(base64 -w0 < "$D/amorce-creation.sh")
    [ "$(printf %s "$B64" | base64 -d | sha256sum | cut -d' ' -f1)" = "$(champ amorce "$D/lancement.txt")" ] || { echo "encodage de l'amorce"; exit 2; }
    TA="$(champ tests_attendus "$D/lancement.txt")"; [[ "$TA" =~ ^[0-9]*$ ]] || { echo "tests attendus illisibles"; exit 2; }
    CMD="GO_ID=$GOC timeout -k 10 300 $VAST create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQ --env \"-e COMMIT=$S -e BRANCHE=$BRANCHE -e DEPOT_URL=https://github.com/lciric/controle-ia-travail.git -e IIB_GO_ID=$GOC -e MODE=$MODE_C -e PREREG_ABSENT=1 -e CONFIG=$(champ config "$D/lancement.txt") -e TESTS_ATTENDUS=$TA -e ECHEANCE_UTC_S=$ECH -e FIN_GO_UTC_S=$FIN_GO -e DEPENSE_EPUISEE_UTC_S=$EPUIS -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$$JGHN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce.sh && bash /root/amorce.sh\" > \"$D/creation-brute-essai$((ESSAIS + 1)).json\" 2>&1 </dev/null; VAST=$VAST bash $DEPOT/$MOI apres-creation \"$D/creation-brute-essai$((ESSAIS + 1)).json\" \$? \"$D\""
    [ ! -e "$D/creation-brute-essai$((ESSAIS + 1)).json" ] || { echo "$D/creation-brute-essai$((ESSAIS + 1)).json existe déjà (R12) : pas de création"; exit 2; }
    case "$ETIQ" in "$PREFIXE_ETIQUETTE"*) ;; *) echo "étiquette de la configuration ($ETIQ) hors du préfixe « $PREFIXE_ETIQUETTE » du saboteur à budget : pas de création"; exit 2;; esac
    [[ "$ETIQ" =~ ^[A-Za-z0-9_.-]{1,60}$ ]] || { echo "étiquette de la configuration illisible (1 à 60 caractères de [A-Za-z0-9_.-]) : pas de création"; exit 2; }
    for v in REQUESTS_CA_BUNDLE SSL_CERT_FILE HTTPS_PROXY NO_PROXY; do
        case "$CMD" in *"$v"*) echo "la commande de création nomme $v (variable du mandataire, jamais transmise à l'instance) : refus"; exit 2;; esac
    done
    printf '{"tool_input":{"command":%s}}' "$(python3 -c 'import json, sys; print(json.dumps(sys.argv[1]))' "$CMD")" | python3 "$DEPOT/.claude/hooks/garde_calcul.py" || { echo "garde de calcul : commande refusée"; exit 2; }
    # Tous les refus sont AU-DESSUS de cette ligne : un refus ne consomme pas un des trois essais de création.
    printf 'creation preparee %s\noffre %s\ncarte %s\nstorage %s\nprix_carte %s\nprix_stockage %s\ntelechargement_forfait %s\nanterieure %s\necheance %s\nepuisement %s\ndepense %s\nplafond_creation %s\nessai_creation %s\nmachine_proposee %s\nrang %s\n' \
        "$(date -u +%FT%TZ)" "$OFFRE" "$CARTE" "$DISQUE" "$PC" "$PS" "$TEL" "$ANT" "$ECH" "$EPUIS" "$DEP" "$PLC" "$((ESSAIS + 1))" "$MACH" "$RANG" >> "$D/lancement.txt"
    printf 'etiquette %s\n' "$ETIQ" >> "$D/lancement.txt"
    echo "OFFRE CONFORME : $OF ; $INV ; $DEP ; $CAR ; $S7B"
    echo "COMMANDE DE CRÉATION (à exécuter une seule fois par l'exécutante, jetons par leur nom seulement) :"
    echo "$CMD" ;;
apres-creation)
    F="${2:-}"; C="${3:-}"; D="${4:-}"
    [ -n "$F" ] && [ -n "$C" ] && [ -n "$D" ] || { echo "usage : apres-creation FICHIER CODE DOSSIER"; exit 2; }
    [ -d "$D" ] && [ -f "$D/lancement.txt" ] || { echo "CRÉATION INCERTAINE (code $C) : dossier de la session $D ou son lancement.txt absent ; réponse brute laissée telle quelle à $F ; vérifier l'inventaire (champs filtrés) ; aucune seconde création avant"; exit 4; }
    MSG=$(verifier_module "$D") && verifier_module "$D" >/dev/null || echo "ALERTE : $MSG : aucune lecture par programme (ni masquage, ni verdict)"
    # Conservation de la réponse brute AVANT toute lecture et tout verdict (R-3687, R-3661) : rien n'est supprimé.
    LUE=""
    if [ -f "$F" ]; then
        chmod 600 -- "$F" 2>/dev/null
        if masquer_fichier "$F"; then
            LUE="$F"
            if COPIE=$(conserver "$F" "$D" creation-brute json); then
                echo "RÉPONSE BRUTE DU LOUEUR CONSERVÉE : $COPIE (empreinte $(cut -d' ' -f1 "$COPIE.sha256")) ; secrets masqués par programme avant conservation ($MODE_MASQUE) : $NB_MASQUES remplacement(s) ; l'original $F porte la même forme masquée ; le masquage n'est pas une garde des secrets : garde des secrets exigée avant tout versement"
                printf 'reponse_creation %s %s masques=%s\n' "$COPIE" "$(cut -d' ' -f1 "$COPIE.sha256")" "$NB_MASQUES" >> "$D/lancement.txt"
            else
                echo "ALERTE : copie datée de la réponse brute impossible dans $D/traces-location ; la réponse, masquée ($NB_MASQUES remplacement(s)), reste à $F"
            fi
        else
            LUE=$(garder_non_masque "$F")
            echo "ALERTE : masquage de la réponse brute en échec : aucune copie aux traces ; la sortie brute est gardée ENTIÈRE, NON MASQUÉE, droits restreints : $LUE ; ne pas la verser"
        fi
    else
        echo "ALERTE : réponse brute du loueur absente ($F n'est pas un fichier) : rien à conserver, rien à lire"
    fi
    # Verdict : par programme, clé de premier niveau de la réponse analysée comme JSON ; jamais un motif cherché dans le texte.
    VERDICT=""; ID=""; RAISON="réponse absente"; CHAMPS=""
    if [ -n "$LUE" ]; then
        if LECTURE=$(location creation "$LUE" 2>/dev/null); then
            VERDICT=$(printf '%s\n' "$LECTURE" | sed -n '1s/^verdict=\([a-z]*\) id=.*/\1/p'); ID=$(printf '%s\n' "$LECTURE" | sed -n '1s/^verdict=cree id=\([1-9][0-9]*\)$/\1/p')
            RAISON=$(printf '%s\n' "$LECTURE" | sed -n 2p); CHAMPS=$(printf '%s\n' "$LECTURE" | sed -n 3p)
            [ "$LUE" != "$F" ] || echo "champs de premier niveau lus par programme (tronqués à 300 caractères, masqués) : $CHAMPS"     # jamais imprimés si le masquage a échoué
        else RAISON="lecture par programme de la réponse impossible"; fi
    fi
    if [ "$VERDICT" = cree ] && [ -n "$ID" ] && [ "$C" = 0 ]; then
        CR=$(date +%s); printf 'instance %s\ncreation %s\n' "$ID" "$CR" >> "$D/lancement.txt"
        echo "CRÉÉE : instance $ID (création $CR ; $RAISON) ; surveillance : bash $MOI surveillance $ID $D"; exit 0
    fi
    if [ "$VERDICT" = refusee ]; then
        MSG=$(resoudre_outil) || { echo "CRÉATION INCERTAINE (code $C, refus lu dans la réponse) : $MSG : inventaire non relu ; vérifier l'inventaire (champs filtrés) ; aucune seconde création avant"; exit 4; }; resoudre_outil >/dev/null
        ligne_outil
        if inventaire_lu "$D" instances-apres "" "" && python3 -I -B -c "$SESSION" instances "$INV_FICHIER" >/dev/null; then
            printf 'machine_refusee %s\n' "$(champ machine_proposee "$D/lancement.txt")" >> "$D/lancement.txt"
            echo "OFFRE REFUSÉE À LA CRÉATION (retirée ?) : aucune instance iib ; machine exclue ; rang suivant : VAST=$VAST bash $DEPOT/$MOI creation auto $(champ carte "$D/lancement.txt") $(champ anterieure "$D/lancement.txt") $D $(champ echeance "$D/lancement.txt")"; exit 5
        fi
        RAISON="refus lu dans la réponse, mais l'inventaire d'après est illisible ou montre une instance du saboteur (${INV_LIGNE:-})"
    fi
    echo "CRÉATION INCERTAINE (code $C, identifiant « ${ID:-aucun} » ; $RAISON) : aucun identifiant consigné ; la réponse brute est conservée (lignes ci-dessus) ; vérifier l'inventaire (champs filtrés) ; aucune seconde création avant"; exit 4 ;;
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
        ( umask 077; timeout -k 5 120 "$VAST" logs "$ID" --tail 20000 > "$D/journal-brut.tmp" 2>&1 </dev/null ); CJ=$?      # sur disque d'abord : rien n'est perdu si le masquage échoue
        if masquer < "$D/journal-brut.tmp" > "$D/journal-dernier.tmp" 2>/dev/null; then
            : > "$D/journal-brut.tmp"                                                  # le relevé brut n'est vidé qu'une fois sa forme masquée écrite
            if [ "$CJ" = 0 ]; then
                mv -f "$D/journal-dernier.tmp" "$D/journal-dernier.txt"
                grep -q '^AMORCE ' "$D/journal-dernier.txt" && cp -f "$D/journal-dernier.txt" "$D/journal-instance.txt"
                grep -E '^(AMORCE|PROGRES) ' "$D/journal-dernier.txt" | while IFS= read -r ligne; do grep -qxF -- "$ligne" "$D/progres.txt" || printf '%s\n' "$ligne" >> "$D/progres.txt"; done
            else
                [ ! -s "$D/journal-dernier.tmp" ] || cp -- "$D/journal-dernier.tmp" "$(fichier_neuf "$D" journal-illisible txt)" 2>/dev/null      # masqué ; nom neuf et unique
                echo "$(date -u +%FT%TZ) ALERTE journal illisible (code $CJ) : dernier relevé gardé" >> "$D/surveillance.txt"
            fi
        else
            NM=$(fichier_neuf "$D" journal-brut txt) && cp -- "$D/journal-brut.tmp" "$NM" && NM=$(garder_non_masque "$NM")
            echo "$(date -u +%FT%TZ) ALERTE masquage du journal en échec : relevé brut gardé entier, NON MASQUÉ, droits restreints (${NM:-copie impossible : $D/journal-brut.tmp}) ; dernier relevé gardé" >> "$D/surveillance.txt"
        fi
        if DEC=$(python3 -I -B -c "$SESSION3" surveillance "$PLC" "$D/progres.txt" "$now" "$PC" "$PS" "$CR" "$ANT" "$TEL" ${FACT:+"$FACT"} 2>&1); then ILLISIBLES=0
        else
            ILLISIBLES=$((ILLISIBLES + 1))
            if [ "$ILLISIBLES" -ge 3 ]; then DEC="ARRET garde : garde de dépense illisible trois fois de suite ($DEC)"; else DEC="ALERTE garde de dépense illisible ($ILLISIBLES/3) : $DEC"; fi
        fi
        echo "$(date -u +%FT%TZ) $DEC" >> "$D/surveillance.txt"
        case "$DEC" in ARRET*|FIN*|REFUS*)      # fin de la surveillance : une copie datée des journaux, avec empreinte (R-3661) ; rien d'autre ne change
            for jf in surveillance.txt progres.txt journal-dernier.txt journal-instance.txt; do
                [ ! -s "$D/$jf" ] || conserver "$D/$jf" "$D" "fin-de-surveillance-${jf%.txt}" txt >/dev/null || echo "ALERTE : copie datée de $jf impossible"
            done; echo "journaux de la surveillance copiés, datés, dans $D/traces-location (fin-de-surveillance-*)" ;;
        esac
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
    # Capacité irréversible : toutes les gardes ci-dessous refusent AVANT tout appel de destruction.
    ID="${2:-}"; D="${3:-}"
    [ -n "$ID" ] && [ -n "$D" ] || { echo "usage : destruction ID DOSSIER (identifiant ou dossier vide) : aucune destruction"; exit 2; }
    [[ "$ID" =~ ^[1-9][0-9]*$ ]] || { echo "identifiant : chiffres seuls, sans zéro de tête (R10) : aucune destruction"; exit 2; }
    [ -f "$D/lancement.txt" ] || { echo "dossier sans lancement.txt : aucune destruction"; exit 2; }
    [ "$(champ instance "$D/lancement.txt")" = "$ID" ] || { echo "identifiant $ID ≠ instance créée d'après $D/lancement.txt (R10) : aucune destruction"; exit 2; }
    [ "${RAPATRIEMENT_VERIFIE:-}" = oui ] || { echo "RAPATRIEMENT_VERIFIE=oui exigé (rapatriement vérifié, ou mot de la mère sur les écarts : ordre, étapes 5 et 6) : aucune destruction"; exit 2; }
    [ -z "${IIB_DESTRUCTION_ETATS_ARRET:-}" ] || { echo "IIB_DESTRUCTION_ETATS_ARRET n'existe plus : la liste des états d'arrêt ($ETATS_ARRET) est fermée, écrite dans le code ; retirer la variable : aucune destruction"; exit 2; }
    INTOUCHABLES="${IIB_INSTANCES_INTOUCHABLES:-}"; AUCUNE="${IIB_AUCUNE_INTOUCHABLE:-}"
    [[ "$INTOUCHABLES" =~ ^([1-9][0-9]*(,[1-9][0-9]*)*)?$ ]] || { echo "IIB_INSTANCES_INTOUCHABLES illisible (identifiants séparés par des virgules) : aucune destruction"; exit 2; }
    # version 3 (vérification de la contre-lecture, n1) : l'attestation « aucune intouchable » n'existe plus ; liste non vide exigée
    [ -z "$AUCUNE" ] || { echo "IIB_AUCUNE_INTOUCHABLE n'existe plus dans cette version : la liste IIB_INSTANCES_INTOUCHABLES, non vide, est exigée (les machines des autres chantiers relevées à l'inventaire) : aucune destruction"; exit 2; }
    [ -n "$INTOUCHABLES" ] || { echo "liste des instances intouchables vide ou absente (IIB_INSTANCES_INTOUCHABLES : identifiants des machines des autres chantiers) : refus, sans attestation possible : aucune destruction"; exit 2; }
    DIT_INTOUCHABLES="$INTOUCHABLES"
    case ",$INTOUCHABLES," in *",$ID,"*) echo "identifiant $ID dans la liste des instances intouchables (IIB_INSTANCES_INTOUCHABLES) : aucune destruction"; exit 2;; esac
    ETIQ=$(champ etiquette "$D/lancement.txt"); [ -n "$ETIQ" ] || ETIQ=$(cle_config "$D/config.json" offre.etiquette 2>/dev/null) || ETIQ=""
    [[ "$ETIQ" =~ ^[A-Za-z0-9_.-]{1,60}$ ]] && case "$ETIQ" in "$PREFIXE_ETIQUETTE"*) true;; *) false;; esac \
        || { echo "étiquette posée à la création illisible ou hors du préfixe « $PREFIXE_ETIQUETTE » (ligne « etiquette » de lancement.txt, ou offre.etiquette de config.json) : aucune destruction"; exit 2; }
    RELECTURES="${IIB_DESTRUCTION_RELECTURES:-6}"; ATTENTE="${IIB_DESTRUCTION_ATTENTE_S:-10}"
    [[ "$RELECTURES" =~ ^[1-9][0-9]*$ ]] && [ "$RELECTURES" -ge 2 ] && [[ "$ATTENTE" =~ ^[0-9]+$ ]] || { echo "IIB_DESTRUCTION_RELECTURES (entier ≥ 2 : deux relectures concordantes exigées) ou IIB_DESTRUCTION_ATTENTE_S (entier ≥ 0) illisible : aucune destruction"; exit 2; }
    MSG=$(verifier_module "$D") || { echo "DESTRUCTION NON TENTÉE : $MSG : aucune lecture par programme de l'inventaire, donc aucune commande de destruction envoyée ; à relire"; exit 4; }; verifier_module "$D" >/dev/null
    MSG=$(resoudre_outil) || { echo "$MSG : aucune destruction"; exit 2; }; resoudre_outil >/dev/null
    ligne_outil
    JD="$D/destruction.txt"
    echo "$(date -u +%FT%TZ) destruction demandée de l'instance $ID ; $(ligne_outil) ; rapatriement attesté par RAPATRIEMENT_VERIFIE=oui ; étiquette exigée : exactement « $ETIQ » ; états d'arrêt admis (liste fermée) : $ETATS_ARRET ; instances intouchables : $DIT_INTOUCHABLES ; module de lecture vérifié" >> "$JD"
    echo "instances intouchables : $DIT_INTOUCHABLES"
    inventaire_lu "$D" instances-avant-destruction "$ID" ""; c_inv=$?
    echo "$(date -u +%FT%TZ) inventaire d'avant (code $c_inv) : $INV_LIGNE" >> "$JD"
    [ "$c_inv" = 0 ] || { echo "DESTRUCTION NON TENTÉE : inventaire d'avant illisible ou en erreur ($INV_LIGNE) : aucune commande de destruction envoyée ; un inventaire illisible n'est pas une preuve ; à relire"; exit 4; }
    AVANT_FICHIER="$INV_FICHIER"; ETAT=$(mot_inv etat); ETIQ_VUE=$(mot_inv etiquette); STATUT=$(mot_inv statut)
    if [ "$ETAT" != present ]; then
        echo "ABSENCE NON CONFIRMÉE : l'instance $ID n'est pas à l'inventaire d'avant ($(mot_inv n) instance(s) au compte) ; aucune commande de destruction envoyée ; ce n'est pas une preuve de destruction (inventaire vide par erreur, autre compte, filtre) : rien n'est consigné comme vérifié ; à relire, message à la mère"; exit 7
    fi
    case "$ETIQ_VUE" in "$ETIQ") ;; *) echo "$(date -u +%FT%TZ) refus : étiquette « $ETIQ_VUE »" >> "$JD"
        echo "REFUS : à l'inventaire, l'instance $ID porte l'étiquette « $ETIQ_VUE », qui n'est pas exactement « $ETIQ », celle consignée à la création : ce n'est pas l'instance du saboteur à budget : aucune destruction"; exit 2;; esac
    case " $ETATS_ARRET " in *" $STATUT "*) ;; *) echo "$(date -u +%FT%TZ) refus : état « $STATUT »" >> "$JD"
        echo "REFUS : l'instance $ID est à l'état « $STATUT », hors de la liste fermée des états d'arrêt ($ETATS_ARRET) : une instance qui tourne n'est jamais détruite par cette sous-commande (l'arrêter d'abord par son identifiant, rapatrier, puis détruire) ; si c'est le nom que l'outil donne à l'arrêt, le code changera en version nouvelle : aucune destruction"; exit 2;; esac
    printf 'rapatriement_atteste %s RAPATRIEMENT_VERIFIE=oui instance=%s par=%s@%s\n' "$(date -u +%FT%TZ)" "$ID" "$(id -un 2>/dev/null | tr -c 'A-Za-z0-9_.\n-' '?' || echo inconnu)" "$(hostname 2>/dev/null | tr -c 'A-Za-z0-9_.\n-' '?' || echo inconnu)" >> "$D/lancement.txt"
    echo "commande de destruction (par l'identifiant, R10 ; confirmation non interactive) : timeout -k 5 120 $VAST destroy instance $ID -y"
    SORTIE=$(fichier_neuf "$D" destruction-sortie txt) || { echo "fichier de sortie impossible dans $D : aucune destruction"; exit 2; }
    timeout -k 5 120 "$VAST" destroy instance "$ID" -y > "$SORTIE" 2>&1 </dev/null; CD=$?                 # sur disque d'abord, puis masquée
    if masquer_fichier "$SORTIE"; then
        COPIE=$(conserver "$SORTIE" "$D" destruction-sortie txt) && SORTIE="$COPIE" || SORTIE="$SORTIE (masquée ; non versée aux traces)"
    else SORTIE="$(garder_non_masque "$SORTIE") (masquage en échec : gardée entière, NON MASQUÉE, droits restreints ; ne pas la verser)"; fi
    echo "$(date -u +%FT%TZ) destroy instance $ID -y : code $CD ; sortie $SORTIE" >> "$JD"
    echo "commande de destruction : code $CD ; sortie conservée : $SORTIE"
    # Preuve : deux relectures CONCORDANTES d'un inventaire dont l'appel a réussi, analysable, où les autres instances d'avant sont encore là.
    n=0; ABSENCES=0; DERNIER=""
    while [ "$n" -lt "$RELECTURES" ]; do
        n=$((n + 1))
        inventaire_lu "$D" instances-apres-destruction "$ID" "$AVANT_FICHIER"; c_inv=$?
        if [ "$c_inv" != 0 ]; then DERNIER=illisible; ABSENCES=0
        elif [ "$(mot_inv etat)" = present ]; then DERNIER=present; ABSENCES=0
        elif [ "$(mot_inv etat)" = absent ] && [ "$(mot_inv autres_manquants)" = 0 ]; then DERNIER=absent; ABSENCES=$((ABSENCES + 1))
        else DERNIER=incoherent; ABSENCES=0; fi
        echo "$(date -u +%FT%TZ) relecture $n/$RELECTURES de l'inventaire (code $c_inv) : instance $ID $DERNIER ; $INV_LIGNE" >> "$JD"
        [ "$ABSENCES" -ge 2 ] && break
        [ "$n" -lt "$RELECTURES" ] && sleep "$ATTENTE"
    done
    if [ "$ABSENCES" -ge 2 ]; then
        if [ "$CD" = 0 ]; then
            printf 'destruction_verifiee %s\n' "$(date +%s)" >> "$D/lancement.txt"
            echo "DÉTRUITE : instance $ID absente de deux relectures concordantes de l'inventaire (relecture $n/$RELECTURES) ; commande de destruction rendue avec le code 0"; exit 0
        fi
        echo "DESTRUCTION INCERTAINE : la commande de destruction a échoué (code $CD) alors que l'instance $ID est absente de deux relectures de l'inventaire : rien n'est consigné comme vérifié ; à relire, sortie $SORTIE"; exit 4
    fi
    case "$DERNIER" in
        present)
            if [ "$CD" = 0 ]; then echo "DESTRUCTION NON OBTENUE : la commande a rendu le code 0 mais l'instance $ID est encore à l'inventaire après $n relecture(s) : elle coûte encore ; message à la mère ; sortie $SORTIE"
            else echo "DESTRUCTION EN ÉCHEC : la commande a rendu le code $CD et l'instance $ID est encore à l'inventaire après $n relecture(s) : elle coûte encore ; message à la mère ; sortie $SORTIE"; fi
            exit 6 ;;
        incoherent) echo "DESTRUCTION INCERTAINE : commande rendue avec le code $CD ; l'inventaire d'après ne montre plus l'instance $ID, mais d'autres instances vues avant y manquent aussi ($INV_LIGNE) : un inventaire vide ou amputé n'est pas une preuve ; l'absence de l'instance $ID n'est pas établie ; à relire ; sortie $SORTIE"; exit 4 ;;
        *) echo "DESTRUCTION INCERTAINE : commande de destruction rendue avec le code $CD ; inventaire d'après $DERNIER après $n relecture(s), sans deux relectures concordantes ($INV_LIGNE) : l'absence de l'instance $ID n'est pas établie ; à relire ; sortie $SORTIE"; exit 4 ;;
    esac ;;
*) echo "usage : outil | --verifier-go-seulement | controles-explo | creation | apres-creation | surveillance | destruction" >&2; exit 2 ;;
esac
