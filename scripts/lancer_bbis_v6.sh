#!/usr/bin/env bash
# v6 (2026-11-18, GO-2026-11-18-04 ; la v5 reste, R12) : la v5, qui passe l'amorce v6, avec cinq écarts, chacun marqué « v6 » :
#   (1) garde neuve « commit de la course » dans `commande` : avant d'imprimer la commande de création, l'arbre que l'amorce
#       extrairait à COMMIT est reconstruit dans un dossier jetable (motifs et copie des fichiers cités LUS DANS L'AMORCE, objets
#       du dépôt de la mère, aucun réseau, rien d'écrit dans RACINE) et la garde d'entrée de la marche y est rejouée par le code
#       même de cet arbre ; la v5 lisait le registre de la tête, non celui de COMMIT (arrêt 2 de R-3160) ;
#   (2) garde neuve « commit joignable » : COMMIT doit être la tête ou un ancêtre de la tête de BRANCHE_CODE sur le dépôt
#       distant (`git ls-remote`, lecture seule) : l'amorce clone cette branche et s'arrêterait sur un commit non poussé ;
#   (3) sous-commande neuve `essais-du-commit RACINE COMMIT DOSSIER` : joue la ligne d'essais de l'amorce sur ce même arbre et
#       compare le compte au plancher MIN_ESSAIS de l'amorce (arrêt 1 : le plancher se mesure sur l'arbre extrait) ;
#   (4) image de la machine exigée égale à IMAGE_COURSE (correction 7 de la contre-lecture du projet de feu : par le nom, non
#       par un condensé) ; (5) prix de l'offre borné par PRIX_MAX_USD_H (GO-2026-11-18-03 (3) : 1,40 USD/h ; s'ajoute au
#       plafond tenu par le feu et au prix relu après création, ne les remplace pas).
# Chaîne de session de l'étape B bis de T0.7, v4 (la v3, qui passe l'amorce v4 : marche v4, contrôle carte-processeur v4 et
# mesure de dispersion du second addendum ; gardes de registre v2 : CODE-BBIS remplacée une fois, une course de plus accordée par
# GO-2026-11-16-11 ; les v1 à v3 restent, R12) (prereg/T0.7-etape-B-bis-v1.md, « Calcul et dépense », « Liste d'arrêt » ; ligne
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
#                                    GO-2026-11-14-09, une relance au plus, plus une course (RELANCES=2) si le feu porte aussi
#                                    GO-2026-11-16-11 et CODE-BBIS est remplacée, échéance, relance après le 21 novembre 12:00 UTC refusée ;
#   commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S FEU RELANCES IMAGE
#                                    imprime la commande de création (amorce scripts/amorce_bbis_v6.sh en base64, variables par leur
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
IMAGE_COURSE=python:3.11-bookworm   # v6 (écart 4) : image des passes précédentes, exigée égale
PRIX_MAX_USD_H=1.40                 # v6 (écart 5) : plafond de GO-2026-11-18-03 (3), prix de carte de l'offre (clé prix_usd_h)
# >>> arbre-du-commit (v6, écarts 1 et 3 ; joué par tests/test_chaine_bbis_v6_v1.py)
arbre_du_commit() {  # $1 = racine (dépôt de la mère) ; $2 = COMMIT ; $3 = amorce ; $4 = dossier neuf : y reconstruit l'arbre que
    # l'amorce extrait à COMMIT (étape 2 : motifs, puis copie des fichiers cités par le registre propre, textes lus dans
    # l'amorce) ; dépôt jetable adossé aux objets de $1 (aucune copie d'objets, aucun clone, aucun filtre, aucun réseau ; rien
    # n'est écrit dans $1). Motif sur la sortie et code 2 sinon. La sortie de 7b (étape 3) n'est pas apportée.
    local rac="$1" c="$2" am="$3" d="$4" objets peu motifs bloc v
    for v in $(compgen -v | grep -E '^GIT_'); do unset "$v"; done      # jamais les variables GIT_* de la session
    [ ! -e "$d" ] || { echo "dossier $d déjà présent (R12)"; return 2; }
    git -C "$rac" cat-file -e "$c^{commit}" 2> /dev/null || { echo "commit $c absent du dépôt $rac"; return 2; }
    objets=$(git -C "$rac" rev-parse --path-format=absolute --git-path objects) && [ -d "$objets" ] || { echo "objets de $rac illisibles"; return 2; }
    motifs=$(sed -n "/^MOTIFS='/,/'\$/p" "$am" | sed "1s/^MOTIFS='//; \$s/'\$//")
    printf '%s\n' "$motifs" | grep -qx '/src/' || { echo "motifs d'extraction illisibles dans l'amorce"; return 2; }
    bloc=$(sed -n '/^# >>> copie-des-fichiers-cites/,/^# <<< copie-des-fichiers-cites/p' "$am")
    [ -n "$bloc" ] || { echo "bloc de copie des fichiers cités illisible dans l'amorce"; return 2; }
    git init -q "$d" && printf '%s\n' "$objets" > "$d/.git/objects/info/alternates" || { echo "dépôt jetable impossible"; return 2; }
    peu=$(git -C "$rac" rev-parse --path-format=absolute --git-path shallow); [ ! -f "$peu" ] || cp "$peu" "$d/.git/shallow"
    git -C "$d" config user.name "essai du commit de la course"; git -C "$d" config user.email "essai@invalid"
    git -C "$d" sparse-checkout init --no-cone > /dev/null 2>&1 && printf '%s\n' "$motifs" | git -C "$d" sparse-checkout set --no-cone --stdin > /dev/null 2>&1 \
        && git -C "$d" checkout -q --detach "$c" 2> /dev/null || { echo "extraction partielle de $c impossible"; return 2; }
    ( D="$d"; COPIES=(); arret() { echo "$1"; exit 2; }; eval "$bloc"
      [ "${#COPIES[@]}" -gt 0 ] || arret "aucun fichier cité par le registre propre à ce commit"
      git -C "$d" add --sparse -f -- "${COPIES[@]}" && git -C "$d" commit -q --allow-empty -m "entrées copiées (essai, jamais poussé)" \
          || arret "commit local des entrées copiées impossible" ) || return 2
    return 0; }
commit_de_la_course() {  # $1 = arbre reconstruit ; $2 = amorce ; $3 = run de 7b : rejoue la garde d'entrée de la marche que
    # l'amorce lance (module lu dans l'amorce), par le code de l'arbre lui-même ; BBIS_INSTANCE n'est posée que pour cet
    # appel, qui ne lit que le registre propre, les sceaux, la fiche et les fichiers qu'elle cite : rien n'est appris ni noté.
    local m
    m=$(sed -n 's/^.*-m \(controle_ia\.t07bbis\.marche_v[0-9][0-9]*\) \\$/\1/p' "$2")
    [ "$(printf '%s' "$m" | grep -c '^')" = 1 ] || { echo "module de la marche illisible ou multiple dans l'amorce"; return 2; }
    BBIS_INSTANCE=1 PYTHONPATH="$1/src" PYTHONDONTWRITEBYTECODE=1 "$PY" -c 'import importlib, sys
try:
    r = importlib.import_module(sys.argv[1]).gardes_d_entree(sys.argv[2], sys.argv[3])
except Exception as e:   # garde de la marche, sceau refusé ou code illisible : refus, jamais un passage silencieux
    print(f"garde d'"'"'entrée de la marche au commit de la course : {type(e).__name__} : {e}"); sys.exit(2)
print(f"{len(r['"'"'fiche'"'"']['"'"'fichiers'"'"'])} fichiers de la fiche, tête {r['"'"'tete'"'"']}")' "$m" "$1" "$3" 2>&1 || return 2; }
commit_joignable() {  # $1 = racine ; $2 = COMMIT ; $3 = BRANCHE_CODE : COMMIT est la tête ou un ancêtre de la tête de la branche
    # sur le dépôt distant (lecture seule) ; branche absente, distant injoignable, tête distante inconnue du clone : refus
    local h
    h=$(git -C "$1" ls-remote origin "refs/heads/$3" 2> /dev/null | cut -f1)
    case "$h" in ''|*[!0-9a-f]*) echo "branche $3 absente du dépôt distant, ou dépôt injoignable : l'amorce ne pourrait pas la cloner"; return 2;; esac
    git -C "$1" cat-file -e "$h^{commit}" 2> /dev/null || { echo "tête distante $h de $3 absente du clone local (git fetch) : commit joignable non prouvé"; return 2; }
    git -C "$1" merge-base --is-ancestor "$2" "$h" 2> /dev/null || { echo "commit $2 absent de la branche $3 du dépôt distant (non poussé, ou autre branche) : l'amorce s'arrêterait après le clonage"; return 2; }
    return 0; }
# <<< arbre-du-commit
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
py_registre() { PYTHONPATH="$RACINE_CODE/src" "$PY" -m controle_ia.t07bbis.registre_bbis_v2 "$@"; }
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
        [ "$IMAGE" = "$IMAGE_COURSE" ] || { echo "BBIS REFUS : image $IMAGE ≠ $IMAGE_COURSE (image de la course)"; exit 2; }   # v6 (écart 4)
        py_registre offre "$FOFFRE" "$OFFRE" > /dev/null || { py_registre offre "$FOFFRE" "$OFFRE"; exit 2; }
        # v6 (écart 5) : prix de carte de l'offre, nombre dans ]0 ; PRIX_MAX_USD_H] ; clé absente ou illisible : refus
        "$PY" -I -c 'import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8")).get("prix_usd_h")
sys.exit(0 if not isinstance(p, bool) and isinstance(p, (int, float)) and 0 < p <= float(sys.argv[2]) else 1)' "$FOFFRE" "$PRIX_MAX_USD_H" 2> /dev/null \
            || { echo "BBIS REFUS : prix de l'offre (clé prix_usd_h) absent, illisible ou au-dessus de $PRIX_MAX_USD_H USD/h (GO-2026-11-18-03)"; exit 2; }
        RAC_ESSAI=$(mktemp -d) || { echo "BBIS REFUS : dossier jetable de l'essai local impossible"; exit 2; }
        AMORCE_ESSAI_LOCAL=1 RACINE_AMORCE="$RAC_ESSAI" COMMIT="$COMMIT" BRANCHE_CODE="$BRC" RUN_7B="$RUN7B" BRANCHE_7B="$BR7B" \
            RUN_BBIS="$RUNB" ECHEANCE_UTC_S="$ECH" GO_ID="$GO_ID" VARIANTE="${VARIANTE:-}" DECISION_VARIANTE="${DECISION_VARIANTE:-}" \
            bash "$ICI/amorce_bbis_v6.sh" > /dev/null; c=$?
        rmdir "$RAC_ESSAI" || { echo "BBIS REFUS : l'amorce en essai local a écrit dans $RAC_ESSAI"; exit 2; }
        [ "$c" = 0 ] || { echo "BBIS REFUS : arguments refusés par l'amorce"; exit 2; }
        py_registre creation "$RAC" "$FEU" "$(date +%s)" "$REL" > /dev/null || { py_registre creation "$RAC" "$FEU" "$(date +%s)" "$REL"; exit 2; }
        py_registre ancetre "$RAC" "$COMMIT" > /dev/null || { py_registre ancetre "$RAC" "$COMMIT"; exit 2; }
        # v6 (écarts 1 et 2) : ce que la marche exigera, vérifié sur l'arbre extrait À COMMIT, et COMMIT joignable par l'amorce
        M=$(commit_joignable "$RAC" "$COMMIT" "$BRC") || { echo "BBIS REFUS : $M"; exit 2; }
        RAC_ARBRE=$(mktemp -d) || { echo "BBIS REFUS : dossier jetable de l'arbre du commit impossible"; exit 2; }
        M=$(arbre_du_commit "$RAC" "$COMMIT" "$ICI/amorce_bbis_v6.sh" "$RAC_ARBRE/arbre") && M=$(commit_de_la_course "$RAC_ARBRE/arbre" "$ICI/amorce_bbis_v6.sh" "$RUN7B"); c=$?
        rm -rf "$RAC_ARBRE"
        [ "$c" = 0 ] || { echo "BBIS REFUS : commit de la course $COMMIT : $M"; exit 2; }
        M=$(branche_de_sortie_neuve "$RAC" "$ICI/amorce_bbis_v6.sh") || { echo "BBIS REFUS : $M"; exit 2; }
        B64=$(base64 -w 0 < "$ICI/amorce_bbis_v6.sh") || { echo "BBIS REFUS : amorce illisible"; exit 2; }
        EXTRA=""; [ -n "${VARIANTE:-}" ] && EXTRA=" -e VARIANTE=$VARIANTE -e DECISION_VARIANTE=$DECISION_VARIANTE"
        echo "BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce $(sha256sum < "$ICI/amorce_bbis_v6.sh" | cut -c1-16)) :"
        echo "GO_ID=$GO_ID vastai create instance $OFFRE --raw --image $IMAGE --disk $DISQUE --cancel-unavail --label $ETIQUETTE --env \"-e COMMIT=$COMMIT -e BRANCHE_CODE=$BRC -e RUN_7B=$RUN7B -e BRANCHE_7B=$BR7B -e RUN_BBIS=$RUNB -e ECHEANCE_UTC_S=$ECH -e GO_ID=$GO_ID$EXTRA -e HF_TOKEN=\$HF_TOKEN -e GH_TOKEN=\$GH_TOKEN\" --entrypoint bash --args -c \"echo $B64 | base64 -d > /root/amorce_bbis_v6.sh && bash /root/amorce_bbis_v6.sh\""
        exit 0;;
    essais-du-commit)   # v6 (écart 3) : plancher d'essais de l'amorce mesuré sur l'arbre qu'elle extrait à COMMIT ; DOSSIER neuf, gardé
        [ "$#" = 4 ] || { echo "BBIS REFUS : essais-du-commit RACINE COMMIT DOSSIER"; exit 2; }
        AM="$ICI/amorce_bbis_v6.sh"; DOS="$4"
        [ ! -e "$DOS" ] && mkdir -p "$DOS" && DOS=$(cd "$DOS" && pwd) || { echo "BBIS REFUS : dossier $4 déjà présent ou impossible (R12)"; exit 2; }
        M=$(arbre_du_commit "$2" "$3" "$AM" "$DOS/depot") || { echo "BBIS REFUS : $M"; exit 2; }
        MIN=$(sed -n 's/^MIN_ESSAIS=\([0-9][0-9]*\)$/\1/p' "$AM"); LIGNE=$(grep -c '^PYTHONPATH=src "\$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_\*\.py --basetemp=' "$AM")
        [ "$(printf '%s' "$MIN" | grep -c '^')" = 1 ] && [ "$LIGNE" = 1 ] || { echo "BBIS REFUS : plancher ou ligne d'essais illisible dans l'amorce"; exit 2; }
        eval "$(sed -n '/^# >>> compte-des-essais/,/^# <<< compte-des-essais/p' "$AM")"
        find "$DOS/depot" -path "$DOS/depot/.git" -prune -o -type f -print | sed "s#^$DOS/depot/##" | LC_ALL=C sort > "$DOS/fichiers-de-l-arbre.txt"
        # même ligne que l'amorce (étape 5), depuis l'arbre, par l'interpréteur de la session (PYTHON_BBIS)
        ( cd "$DOS/depot" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py --basetemp="$DOS/essais-tmp" > "$DOS/essais.txt" 2> "$DOS/essais.err" ); c=$?
        RES=$(tail -n 1 "$DOS/essais.txt"); NP=$(compte_passes "$RES")
        echo "BBIS ESSAIS DU COMMIT $3 : code $c, ligne de compte : $RES ; plancher de l'amorce $MIN ; $(grep -c '' "$DOS/fichiers-de-l-arbre.txt") fichiers sur l'arbre ($DOS)"
        [ "$c" = 0 ] || { echo "BBIS REFUS : essais en échec sur l'arbre extrait (essais.txt) : l'amorce s'arrêterait à son étape 5"; exit 2; }
        [ "$NP" -ge "$MIN" ] || { echo "BBIS REFUS : $NP passés < $MIN : l'amorce s'arrêterait à son étape 5"; exit 2; }
        [ -z "$(git -C "$DOS/depot" status --porcelain --untracked-files=all -- src tests)" ] || { echo "BBIS REFUS : les essais ont écrit sous src ou tests"; exit 2; }
        echo "BBIS ESSAIS DU COMMIT : $NP passés ≥ $MIN : le plancher de l'amorce serait franchi"; exit 0;;
    depense)
        [ "$#" = 3 ] || { echo "BBIS REFUS : depense CUMUL_USD PRIX_CARTE_USD_H"; exit 2; }
        py_registre depense "$2" "$3"; c=$?
        [ "$c" = 0 ] || echo "BBIS : arrêt et destruction par l'identifiant (R10) : bash scripts/lancer_bbis_v6.sh detruire <ID>, puis bash scripts/lancer_bbis_v6.sh verifier-destruction <ID> <TEMOIN>"
        exit "$c";;
    detruire)
        [ "$#" = 2 ] || { echo "BBIS REFUS : detruire ID"; exit 2; }
        case "$2" in ''|*[!0-9]*) echo "BBIS REFUS : identifiant illisible (destruction par l'identifiant seulement, R10)"; exit 2;; esac
        py_registre identifiant "$2" > /dev/null || { py_registre identifiant "$2"; exit 2; }
        echo "GO_ID=$GO_ID vastai destroy instance $2 -y"
        echo "BBIS PUIS (jamais juger la destruction par le code de sortie) : bash scripts/lancer_bbis_v6.sh verifier-destruction $2 <TEMOIN>"
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
    *) echo "BBIS REFUS : sous-commande inconnue (offre-depuis-recherche, offre, creation, commande, essais-du-commit, depense, detruire, verifier-destruction)"; exit 2;;
esac
