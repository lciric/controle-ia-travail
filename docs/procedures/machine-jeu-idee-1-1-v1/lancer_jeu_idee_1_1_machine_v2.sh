#!/usr/bin/env bash
# Chaîne de session de la machine du jeu relancé de l'idée 1.1, v2 (procédure `procedure-machine-jeu-idee-1-1-v5.md` du même
# dossier ; GO-2026-11-16-09, GO-2026-11-16-10 et R-3014 : la dépense part sous sa propre ligne de type « calcul »). Modèle :
# scripts/lancer_bbis_v3.sh. v2 = v1 dont l'amorce nommée est amorce_jeu_idee_1_1_v2.sh (chemin du fichier, nom écrit sur la
# machine, contrôle de la ligne) ; rien d'autre ne change (garde v1 inchangée : elle ne nomme pas l'amorce).
# Côté session seulement : aucune commande de ce script ne crée, n'arrête ni ne détruit de machine et aucune n'appelle le loueur,
# sauf `verifier-destruction` sans LISTE.json (lecture de la liste des instances). Il contrôle et IMPRIME les commandes, que
# l'opérateur joue (préfixe GO_ID exigé par la garde de calcul ; destruction par l'identifiant, R10). Codes : 0 accepté ; 2 refus.
#   offre-depuis-recherche RECHERCHE.json OFFRE.json
#        garde d'offre jouée hors ligne sur CHAQUE offre de la recherche, la moins chère acceptée écrite dans OFFRE.json (mode x).
#        Recherche (lecture seule ; le filtre de l'outil ne décide pas, la garde décide) :
#        ( umask 077; "$V" search offers 'rentable=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=20
#          inet_down>=100 dph_total<=0.06' -o 'dph_total' --storage 20 --raw < /dev/null > RECHERCHE.json )
#   offre OFFRE.json [ID]                      bornes de l'offre relues
#   creation RACINE FEU COMMIT RELANCES        feu « R-<N> GO-… » (forme courte), ligne R-<N> et ligne de GO de type « calcul »
#   commande RACINE OFFRE.json COMMIT EMPREINTE_RELANCE ECHEANCE_UTC_S FEU RELANCES IMAGE DOSSIER [BRANCHE_SORTIE]
#        imprime la ligne de création après : offre ; échéance dans [maintenant + 49 h 30, + 50 h] ; commit ancêtre de la tête
#        distante de main (lecture seule) et portant, à l'octet, le texte, l'addendum d'empreintes, l'addendum de relance
#        (EMPREINTE_RELANCE, compagnon d'une ligne), l'essai du § 6 point 3 ; aucune sortie antérieure de ce jeu dans son arbre ;
#        amorce en essai local (rien écrit) ; garde de création ; branche de sortie absente du dépôt distant. L'amorce passe
#        compressée (gzip -9 -n) puis en base64 ; la réponse du loueur (qui porte une clé propre à la machine, R-3002) va dans
#        DOSSIER/reponse-creation.json (umask 077), dont seuls « success », « new_contract » et les noms des clés s'affichent.
#   prix-relu PRIX                             prix relu après création ≤ 0,06 USD/h, sinon destruction aussitôt
#   depense RACINE GO CUMUL PRIX               cumul + une heure au prix relu ≥ plafond de la ligne de GO → refus, destruction
#   detruire ID DOSSIER GO                     imprime la destruction par l'identifiant, avec -y (R-2789), ID = DOSSIER/id-machine.txt
#   verifier-destruction ID TEMOIN [LISTE.json] absence de ID prouvée dans la liste des instances, témoin présent (jamais un code)
#   controle-ligne COMMANDE_IMPRIMEE.txt       contrôle par programme de la sortie de `commande` (deux lignes ; amorce décodée et
#                                              décompressée égale à l'octet à amorce_jeu_idee_1_1_v2.sh) ; imprime la ligne, base64 masqué
#   inventaire < LISTE.json                    filtre de la liste brute des instances : « <id> <étiquette> » seulement, trié
set -uo pipefail
PY="${PYTHON_JEU11:-python3}"
ICI="$(cd "$(dirname "$0")" && pwd)"
GARDE="$ICI/garde_machine_jeu_idee_1_1_v1.py"; AMORCE="$ICI/amorce_jeu_idee_1_1_v2.sh"
V="${VASTAI_JEU:-/home/user/vastai-env/bin/vastai}"
ETIQUETTE=jeu-idee-1-1-relance-v1; DISQUE=20; ECH_MIN=178200; ECH_MAX=180000
PREREG=prereg/organisme-idee-1-1-poids-du-nul-v2.md; SHA_PREREG=3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff
AE=prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md; SHA_AE=73ea3bf3ed000444cb446b9dd2af0ae83c090dd97adce78109d7a521ae6c6ccc
RELANCE=prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-relance-v1.md
ESSAI_PROJ=docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/essai_projection_cas_v1.py
SHA_ESSAI_PROJ=539f6a6cfce71eaab9010fa9cd16a2607a0bf9faf9499286bcb6fb7f25bda837
g() { "$PY" -I "$GARDE" "$@"; }
refus() { echo "JEU11 REFUS : $*"; exit 2; }
# >>> branche-de-sortie (lecture seule : `git ls-remote` sur « origin » de la racine, qui doit être le dépôt de l'amorce)
branche_de_sortie_neuve() {  # $1 = racine ; $2 = branche
    local url o c
    url=$(sed -n 's/^DEPOT_URL_OFFICIEL=\(.*\)$/\1/p' "$AMORCE" 2> /dev/null)
    [ "$(printf '%s' "$url" | grep -c '^')" = 1 ] || { echo "dépôt de l'amorce illisible ou multiple (DEPOT_URL_OFFICIEL=…)"; return 2; }
    o=$(git -C "$1" remote get-url origin 2> /dev/null) || { echo "dépôt distant « origin » absent de $1"; return 2; }
    url=${url%/}; url=${url%.git}; o=${o%/}; o=${o%.git}
    [ "${o##*/}" = "${url##*/}" ] && [ "$(basename "$(dirname "$o")")" = "$(basename "$(dirname "$url")")" ] \
        || { echo "« origin » de $1 n'est pas le dépôt de l'amorce ($(basename "$(dirname "$url")")/${url##*/})"; return 2; }
    git -C "$1" ls-remote --exit-code origin "refs/heads/$2" > /dev/null 2>&1; c=$?
    case "$c" in
        2) return 0;;
        0) echo "branche de sortie $2 présente sur le dépôt distant (R12) : nom neuf exigé (BRANCHE_SORTIE …-v2)"; return 2;;
        *) echo "dépôt distant injoignable (git ls-remote, code $c) : absence de la branche de sortie $2 non prouvée"; return 2;;
    esac; }
# <<< branche-de-sortie
# >>> commit-du-jeu (lecture seule de git dans la racine)
commit_du_jeu() {  # $1 = racine ; $2 = commit ; $3 = empreinte attendue de l'addendum de relance
    local rac="$1" c="$2" tete n
    printf '%s' "$c" | grep -qxE '[0-9a-f]{40}' || { echo "commit : 40 caractères hexadécimaux attendus"; return 2; }
    printf '%s' "$3" | grep -qxE '[0-9a-f]{64}' || { echo "EMPREINTE_RELANCE illisible"; return 2; }
    git -C "$rac" cat-file -e "$c^{commit}" 2> /dev/null || { echo "commit $c absent de $rac"; return 2; }
    tete=$(git -C "$rac" ls-remote origin refs/heads/main 2> /dev/null | cut -f1)
    printf '%s' "$tete" | grep -qxE '[0-9a-f]{40}' || { echo "tête distante de main illisible (git ls-remote)"; return 2; }
    git -C "$rac" cat-file -e "$tete^{commit}" 2> /dev/null || { echo "tête distante de main ${tete:0:12} absente de $rac : la rapatrier d'abord (git fetch origin refs/heads/main:refs/remotes/origin/main)"; return 2; }
    git -C "$rac" merge-base --is-ancestor "$c" "$tete" || { echo "commit ${c:0:12} : pas un ancêtre de la tête distante de main ${tete:0:12}"; return 2; }
    sha_au() { git -C "$rac" show "$c:$1" 2> /dev/null | sha256sum | cut -d' ' -f1; }
    git -C "$rac" cat-file -e "$c:$RELANCE" 2> /dev/null || { echo "addendum de relance $RELANCE absent du commit"; return 2; }
    [ "$(sha_au "$PREREG")" = "$SHA_PREREG" ] || { echo "texte $PREREG au commit ≠ ${SHA_PREREG:0:12}…"; return 2; }
    [ "$(sha_au "$AE")" = "$SHA_AE" ] || { echo "addendum d'empreintes au commit ≠ ${SHA_AE:0:12}…"; return 2; }
    [ "$(git -C "$rac" show "$c:$AE.sha256" 2> /dev/null)" = "$SHA_AE  $(basename "$AE")" ] || { echo "compagnon de l'addendum d'empreintes faux au commit"; return 2; }
    [ "$(sha_au "$RELANCE")" = "$3" ] || { echo "addendum de relance au commit $(sha_au "$RELANCE" | cut -c1-12)… ≠ EMPREINTE_RELANCE ${3:0:12}…"; return 2; }
    [ "$(git -C "$rac" show "$c:$RELANCE.sha256" 2> /dev/null)" = "$3  $(basename "$RELANCE")" ] || { echo "compagnon de l'addendum de relance faux ou absent au commit (une ligne « <empreinte>  <nom> »)"; return 2; }
    [ "$(sha_au "$ESSAI_PROJ")" = "$SHA_ESSAI_PROJ" ] || { echo "essai du § 6 point 3 au commit ≠ ${SHA_ESSAI_PROJ:0:12}…"; return 2; }
    n=$(git -C "$rac" ls-tree --name-only "$c" -- runs/ diag/organisme-idees-juge-v1/ 2> /dev/null | grep -cE 'idee-1-1-poids-du-nul-v[1-5]$')
    [ "$n" = 0 ] || { echo "$n sortie(s) ou manifeste(s) de ce jeu dans l'arbre du commit : le lanceur du jeu refuserait (noms seulement lus)"; return 2; }
    return 0; }
# <<< commit-du-jeu
case "${1:-}" in
    offre-depuis-recherche) [ "$#" = 3 ] || refus "offre-depuis-recherche RECHERCHE.json OFFRE.json"; g offre-depuis-recherche "$2" "$3"; exit $?;;
    offre) [ "$#" = 2 ] || [ "$#" = 3 ] || refus "offre OFFRE.json [ID]"; g "$@"; exit $?;;
    creation) [ "$#" = 5 ] || refus "creation RACINE FEU COMMIT RELANCES"; g creation "$2" "$3" "$4" "$(date +%s)" "$5"; exit $?;;
    commande)
        [ "$#" = 10 ] || [ "$#" = 11 ] || refus "commande RACINE OFFRE.json COMMIT EMPREINTE_RELANCE ECHEANCE_UTC_S FEU RELANCES IMAGE DOSSIER [BRANCHE_SORTIE]"
        RAC="$2"; FOFFRE="$3"; COMMIT="$4"; ER="$5"; ECH="$6"; FEU="$7"; REL="$8"; IMAGE="$9"; DOS="${10}"; BR="${11:-calcul/idee-1-1-jeu-relance-v1}"
        printf '%s' "$ECH" | grep -qxE '[0-9]+' || refus "échéance illisible"
        N=$(date +%s); [ "$ECH" -ge $((N + ECH_MIN)) ] && [ "$ECH" -le $((N + ECH_MAX)) ] || refus "échéance hors de [maintenant + 49 h 30, + 50 h]"
        printf '%s' "$IMAGE" | grep -qxE '[A-Za-z0-9._:/@-]+' || refus "image illisible"
        printf '%s' "$DOS" | grep -qxE '/[A-Za-z0-9._/-]+' && [ -d "$DOS" ] || refus "dossier d'envoi $DOS : chemin absolu existant exigé"
        [ ! -e "$DOS/reponse-creation.json" ] || refus "$DOS/reponse-creation.json existe déjà (R12 : une création par dossier d'envoi)"
        printf '%s' "$BR" | grep -qxE 'calcul/idee-1-1-jeu-relance-v[1-9][0-9]*' || refus "branche de sortie illisible"
        OFFRE=$("$PY" -I -c 'import json, sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["id"])' "$FOFFRE" 2> /dev/null) || refus "OFFRE.json illisible"
        g offre "$FOFFRE" "$OFFRE" > /dev/null || { g offre "$FOFFRE" "$OFFRE"; exit 2; }
        M=$(commit_du_jeu "$RAC" "$COMMIT" "$ER") || refus "$M"
        GO=$(printf '%s' "$FEU" | sed -n 's/^R-[1-9][0-9]* \(GO-[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}-[0-9]\{2\}\)$/\1/p')
        [ -n "$GO" ] || refus "feu : forme courte « R-<N> GO-AAAA-MM-JJ-NN » exigée"
        RAC_ESSAI=$(mktemp -d) || refus "dossier jetable de l'essai local impossible"
        AMORCE_ESSAI_LOCAL=1 COMMIT="$COMMIT" EMPREINTE_RELANCE="$ER" ECHEANCE_UTC_S="$ECH" GO_ID="$GO" BRANCHE_SORTIE="$BR" \
            HOME="$RAC_ESSAI" bash "$AMORCE" > /dev/null < /dev/null; c=$?
        rmdir "$RAC_ESSAI" || refus "l'amorce en essai local a écrit dans $RAC_ESSAI"
        [ "$c" = 0 ] || refus "arguments refusés par l'amorce en essai local"
        g creation "$RAC" "$FEU" "$COMMIT" "$(date +%s)" "$REL" > /dev/null || { g creation "$RAC" "$FEU" "$COMMIT" "$(date +%s)" "$REL"; exit 2; }
        M=$(branche_de_sortie_neuve "$RAC" "$BR") || refus "$M"
        B64=$(gzip -9 -n -c < "$AMORCE" | base64 -w 0) || refus "amorce illisible"
        F="python3 -I -c 'import json, sys; d = json.load(open(sys.argv[1], encoding=\"utf-8\")); print(\"JEU11 CREATION success\", d.get(\"success\"), \"new_contract\", d.get(\"new_contract\"), \"cles\", sorted(d))' $DOS/reponse-creation.json"
        echo "JEU11 COMMANDE (à jouer telle quelle, une fois, après le feu écrit ; empreinte de l'amorce $(sha256sum < "$AMORCE" | cut -c1-16) ; base64 de l'amorce compressée : ${#B64} caractères) :"
        echo "( umask 077; GO_ID=$GO $V create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQUETTE --env \"-e COMMIT=$COMMIT -e EMPREINTE_RELANCE=$ER -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GO -e BRANCHE_SORTIE=$BR -e GH_TOKEN=\$GH_TOKEN\" --entrypoint bash --args -c \"echo $B64 | base64 -d | gunzip > /root/amorce_jeu_idee_1_1_v2.sh && bash /root/amorce_jeu_idee_1_1_v2.sh\" < /dev/null > $DOS/reponse-creation.json ); $F"
        exit 0;;
    prix-relu) [ "$#" = 2 ] || refus "prix-relu PRIX"; g prix-relu "$2"; c=$?
        [ "$c" = 0 ] || echo "JEU11 : destruction aussitôt : bash $0 detruire <ID> <DOSSIER> <GO>, puis verifier-destruction"; exit "$c";;
    depense) [ "$#" = 5 ] || refus "depense RACINE GO CUMUL PRIX"; g depense "$2" "$3" "$4" "$5"; c=$?
        [ "$c" = 0 ] || echo "JEU11 : arrêt et destruction par l'identifiant (R10) : bash $0 detruire <ID> <DOSSIER> <GO>, puis verifier-destruction <ID> <TEMOIN>"; exit "$c";;
    detruire)
        [ "$#" = 4 ] || refus "detruire ID DOSSIER GO"
        printf '%s' "$4" | grep -qxE 'GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}' || refus "GO illisible"
        g identifiant "$2" "$3" > /dev/null || { g identifiant "$2" "$3"; exit 2; }
        echo "GO_ID=$4 $V destroy instance $2 -y"
        echo "JEU11 PUIS (jamais juger la destruction par le code de sortie ; attendre 30 s) : bash $0 verifier-destruction $2 <TEMOIN>"
        exit 0;;
    verifier-destruction)
        [ "$#" = 3 ] || [ "$#" = 4 ] || refus "verifier-destruction ID TEMOIN [LISTE.json]"
        if [ "$#" = 4 ]; then LISTE="$4"
        else
            DL=$(umask 077; mktemp -d) || { echo "JEU11 ABSENCE NON PROUVEE : dossier de la liste impossible : arrêt"; exit 2; }
            LISTE="$DL/instances.json"
            ( umask 077; "$V" show instances --raw < /dev/null > "$LISTE" 2> "$DL/instances.err" ); c=$?
            [ "$c" = 0 ] || { echo "JEU11 ABSENCE NON PROUVEE : lecture de la liste en échec (code $c, $DL/instances.err) : arrêt"; exit 2; }
            echo "JEU11 liste brute des instances gardée (à effacer par ce chemin exact après la preuve, C8) : $DL"
        fi
        g absence "$2" "$3" "$LISTE"; exit $?;;
    controle-ligne)
        [ "$#" = 2 ] || refus "controle-ligne COMMANDE_IMPRIMEE.txt"
        "$PY" -I -c 'import base64, gzip, hashlib, re, sys
t = open(sys.argv[1], encoding="utf-8").read()
l = t.split("\n")
m = re.search(r"echo ([A-Za-z0-9+/=]+) \| base64 -d \| gunzip > /root/amorce_jeu_idee_1_1_v2\.sh && bash /root/amorce_jeu_idee_1_1_v2\.sh", l[1] if len(l) > 1 else "")
if len(l) != 3 or l[2] != "" or not l[0].startswith("JEU11 COMMANDE") or not m:
    print("JEU11 REFUS : sortie de commande mal formée (deux lignes, en-tête JEU11 COMMANDE, amorce en base64 attendus)"); sys.exit(2)
try:
    a = gzip.decompress(base64.b64decode(m.group(1), validate=True))
except Exception as e:
    print("JEU11 REFUS : base64 ou compression illisible (%s)" % type(e).__name__); sys.exit(2)
h, f = hashlib.sha256(a).hexdigest(), hashlib.sha256(open(sys.argv[2], "rb").read()).hexdigest()
if h != f or h[:16] not in l[0]:
    print("JEU11 REFUS : amorce décodée %s ≠ fichier %s (ou absente de l en-tête)" % (h[:16], f[:16])); sys.exit(2)
print("JEU11 LIGNE CONFORME : amorce décodée égale à l octet (%s), ligne de %d caractères" % (h[:16], len(l[1])))
print(l[1].replace(m.group(1), "<B64>"))' "$2" "$AMORCE"
        exit $?;;
    inventaire)
        [ "$#" = 1 ] || refus "inventaire < LISTE.json"
        "$PY" -I -c 'import json, sys
d = json.load(sys.stdin); l = d.get("instances") if isinstance(d, dict) else d
assert isinstance(l, list) and all(isinstance(i, dict) and "id" in i for i in l), "liste illisible"
[print(i["id"], i.get("label")) for i in sorted(l, key=lambda i: int(i["id"]))]' 2> /dev/null || { echo "JEU11 REFUS : liste des instances illisible"; exit 2; }
        exit 0;;
    *) refus "sous-commande inconnue (offre-depuis-recherche, offre, creation, commande, prix-relu, depense, detruire, verifier-destruction, controle-ligne, inventaire)";;
esac
