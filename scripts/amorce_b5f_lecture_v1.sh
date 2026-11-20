#!/usr/bin/env bash
# Amorce de l'instance de lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») et de la répétition générale
# (v1, écrite le 2026-11-20 sur le modèle de scripts/amorce_b5f_formation_v1.sh, lue sans être modifiée). Texte :
# prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md, « Plan d'analyse », points 7 (deuxième tiret),
# 8 à 10 et 18 ; « Données gardées » ; « Liste d'arrêt », points 5 à 11 et 14 ; devis, § 3 à 5. Passée en base64 par la
# commande de création qu'imprime scripts/lancer_b5f_lecture_v1.sh (sous-commande « commande »), jouée par la session.
# Une instance, une marche (`controle_ia.barreau5_familles.relecture_v1`, mode réel), sous $R/b5f-lecture-v1.
# Ordre :
#   0. arguments (essai local : arrêt ici, code 0, rien d'écrit) ; minuterie lancée, par l'identifiant de l'instance (R10),
#      à ECHEANCE_ARRET_UTC_S + 15 minutes. À son échéance, elle DÉTRUIT l'instance seulement si le versement final est
#      prouvé (témoin), sinon elle l'ARRÊTE (état « stopped », disque gardé) et écrit un signal pour la mère (R-3661) ;
#   1. machine (outils, clés reçues comme valeurs, citées par leur nom ; carte A100 ; CUDA du pilote au moins 13.0) ;
#   2. dépôt au commit COMMIT, extraction partielle nommée (code, essais de la lecture, scripts de la lecture, texte scellé,
#      configuration scellée, registre propre, tâches d'évaluation seules, invites ; adaptateurs existants cités) ; jamais
#      docs/notes, diag, runs, brouillons ni une marche de formation ; branche de sortie absente du dépôt distant ;
#   3. plan décisif : entrées de lecture tirées de leur branche à ENTREES_COMMIT, seul leur dossier extrait, dans un clone à
#      part ; tous leurs fichiers ajoutés par ce seul commit (point 7 : « en un seul commit ») ; aucune référence à la branche
#      de la formation ; la marche refait la liste blanche, les empreintes, les noms opaques contigus et « seuls tenseurs » ;
#   4. paquets ; 5. essais de la lecture (au moins MIN_ESSAIS passés) ; 6. modèle au cache local ; 7. configuration réelle ;
#   8. marche sous `timeout` jusqu'à ECHEANCE_ARRET_UTC_S (TERM au seul processus lancé, jamais par motif) ;
#   9. versement, dans cet ordre (devis, § 4 : les scores avant les activations) : fichiers fermés, poids, inventaires,
#      manifeste, résultats, traces ; puis, si la règle de garde est « une_sur_dix », les activations gardées, par lots de
#      LOT_OCTETS au plus ; preuve (inventaire poussé et relu) ; contenu de SCORES-B5F écrit au journal pour la mère ;
#  10. fin : état « stopped » demandé ; la session vérifie le versement, puis détruit par l'identifiant.
# Le témoin du versement final (qui permet la destruction) n'est écrit que si la marche est menée au bout, les sorties
# prouvées et les activations gardées versées : avec la règle « trois_couches » ou « couche_15 », les activations vont sur
# un volume accordé (nœud 4) que l'amorce ne connaît pas : aucune destruction, signal pour la mère.
# Rien n'est supprimé. Aucun journal ne porte un score ni une grandeur d'adaptateur : la marche n'imprime que des étapes, des
# comptes et l'empreinte de l'inventaire. GH_TOKEN, HF_TOKEN et CONTAINER_API_KEY ne sont cités que par leur nom.
# Variables (--env) : PLAN_B5F (decisif ou repetition), COMMIT, BRANCHE_CODE, PREREG, RUN_LECTURE, PRIX_USD_H,
#   ECHEANCE_ARRET_UTC_S, GO_ID, DEPOT_URL, ENTREES_COMMIT (« - » pour la répétition), DIVERGENCE_B5F (0 ou 1), GARDE_B5F,
#   EXISTANTS_B5F (liste JSON des adaptateurs existants, en base64), EXISTANTS_CHEMINS (leurs chemins, séparés par des
#   virgules, ou « - »), GH_TOKEN, HF_TOKEN ; posées par le loueur : CONTAINER_ID, CONTAINER_API_KEY.
# Essai local (AMORCE_ESSAI_LOCAL=1) : contrôle des arguments seulement, sortie (code 0) avant tout réseau et toute écriture.
# Essai à blanc (AMORCE_ESSAI_BLANC=1, tests/test_amorce_b5f_lecture_entiere_v1.py) : l'amorce entière, sous RACINE_AMORCE,
#   avec les faux outils que l'essai met dans le PATH ; toutes les gardes restent ; seuls le quart d'heure du versement
#   (B5F_VERSEMENT_S) et, à l'échéance, une seule demande de la minuterie (B5F_MINUTERIE_UNE_FOIS) y sont permis.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
BLANC="${AMORCE_ESSAI_BLANC:-0}"
R="${RACINE_AMORCE:-/root}"
[ "$ESSAI" = 1 ] || [ "$BLANC" = 1 ] || [ -z "${RACINE_AMORCE:-}" ] || { echo "B5F REFUS : RACINE_AMORCE en essai local seulement (ou essai à blanc)"; exit 2; }
T="$R/b5f-lecture-v1"; D="$T/depot"; E="$T/entrees"; X="$T/traces"; L="$X/journal-b5f-lecture.txt"
API=https://console.vast.ai/api/v0
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
BRANCHE_ENTREES=donnees/barreau5-familles-jumelles-v1-entrees-de-lecture
DOSSIER_ENTREES=entrees-de-lecture-b5f
TEXTE_B5F=prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md
SEUIL=94000000
LOT_OCTETS=900000000
VERSEMENT_S=900
[ "$BLANC" != 1 ] || VERSEMENT_S="${B5F_VERSEMENT_S:-900}"
case "$VERSEMENT_S" in ''|*[!0-9]*) echo "B5F REFUS : quart d'heure du versement illisible"; exit 2;; esac
TEMOIN="$T/versement-final-prouve"
SORTIES_PROUVEES="$T/versement-des-sorties-prouve"
ACTIVATIONS_VERSEES="$T/activations-gardees-versees"
MARCHE_FINIE="$T/marche-menee-au-bout"
SIGNAL="$X/signal-pour-la-mere.txt"
# essais de la lecture sur l'arbre extrait (lanceur et amorce exclus : ils lisent la garde de calcul ou jouent l'amorce) ;
# un essai de tests/test_amorce_b5f_lecture_v1.py exige l'égalité avec le nombre d'essais de ces trois fichiers
MIN_ESSAIS=146
PY=python3                  # remplacé par l'interpréteur de l'environnement des paquets dès qu'il existe (étape 4)
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
j() { mkdir -p "$X" 2> /dev/null; printf '%s B5F %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
# >>> arguments (extrait et joué par tests/test_amorce_b5f_lecture_v1.py)
verifier_arguments() {  # 0 si conformes ; sinon motif sur la sortie, code 2
    local v s c
    for v in PLAN_B5F COMMIT BRANCHE_CODE PREREG RUN_LECTURE PRIX_USD_H ECHEANCE_ARRET_UTC_S GO_ID DEPOT_URL ENTREES_COMMIT \
             DIVERGENCE_B5F GARDE_B5F EXISTANTS_B5F EXISTANTS_CHEMINS; do
        [ -n "${!v:-}" ] || { echo "B5F REFUS : variable $v absente"; return 2; }; done
    case "$PLAN_B5F" in decisif) s=b5f-lecture;; repetition) s=b5f-repetition;; *) echo "B5F REFUS : PLAN_B5F : decisif ou repetition"; return 2;; esac
    case "$COMMIT" in *[!0-9a-f]*) echo "B5F REFUS : COMMIT illisible"; return 2;; esac
    [ "${#COMMIT}" = 40 ] || { echo "B5F REFUS : COMMIT de 40 caractères attendu"; return 2; }
    case "$BRANCHE_CODE" in *[!A-Za-z0-9._/-]*) echo "B5F REFUS : BRANCHE_CODE illisible"; return 2;; esac
    [ "$PREREG" = "$TEXTE_B5F" ] || { echo "B5F REFUS : PREREG ≠ $TEXTE_B5F"; return 2; }
    case "$RUN_LECTURE" in [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-"$s") ;;
        *) echo "B5F REFUS : RUN_LECTURE illisible ou d'un autre plan"; return 2;; esac
    printf '%s' "$PRIX_USD_H" | LC_ALL=C grep -qxE '[0-9]+(\.[0-9]+)?' || { echo "B5F REFUS : PRIX_USD_H illisible"; return 2; }
    awk -v p="$PRIX_USD_H" 'BEGIN { exit !(p > 0 && p <= 1.30) }' || { echo "B5F REFUS : PRIX_USD_H hors de ]0 ; 1,30]"; return 2; }
    case "$ECHEANCE_ARRET_UTC_S" in *[!0-9]*) echo "B5F REFUS : ECHEANCE_ARRET_UTC_S illisible"; return 2;; esac
    printf '%s' "$GO_ID" | LC_ALL=C grep -qxE 'GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}' || { echo "B5F REFUS : GO_ID illisible"; return 2; }
    [ "$DEPOT_URL" = "$DEPOT_URL_OFFICIEL" ] || { echo "B5F REFUS : DEPOT_URL ≠ $DEPOT_URL_OFFICIEL (jamais la copie publique)"; return 2; }
    if [ "$PLAN_B5F" = decisif ]; then
        printf '%s' "$ENTREES_COMMIT" | LC_ALL=C grep -qxE '[0-9a-f]{40}' || { echo "B5F REFUS : ENTREES_COMMIT de 40 caractères attendu (plan décisif)"; return 2; }
    else
        [ "$ENTREES_COMMIT" = "-" ] || { echo "B5F REFUS : ENTREES_COMMIT « - » attendu pour la répétition"; return 2; }
    fi
    case "$DIVERGENCE_B5F" in 0|1) ;; *) echo "B5F REFUS : DIVERGENCE_B5F : 0 ou 1"; return 2;; esac
    case "$GARDE_B5F" in trois_couches|couche_15|une_sur_dix) ;; *) echo "B5F REFUS : GARDE_B5F inconnue"; return 2;; esac
    printf '%s' "$EXISTANTS_B5F" | LC_ALL=C grep -qxE '[A-Za-z0-9+/]+={0,2}' || { echo "B5F REFUS : EXISTANTS_B5F illisible (base64)"; return 2; }
    if [ "$EXISTANTS_CHEMINS" != "-" ]; then
        for c in ${EXISTANTS_CHEMINS//,/ }; do
            printf '%s' "$c" | LC_ALL=C grep -qxE '[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*\.(pt|safetensors)' || { echo "B5F REFUS : chemin d'adaptateur existant illisible"; return 2; }
            case "/$c/" in */../*|/docs/*|/diag/*|/runs/*|*b5f-formation*) echo "B5F REFUS : chemin d'adaptateur existant refusé"; return 2;; esac
        done
    fi
    [ "$PLAN_B5F" = decisif ] || [ "$EXISTANTS_CHEMINS" != "-" ] || { echo "B5F REFUS : répétition sans adaptateurs existants"; return 2; }
    return 0; }
# <<< arguments
# >>> branche (extrait et joué par tests/test_amorce_b5f_lecture_v1.py : même nom que `relecture_v1.PIECES_LECTURE`)
branche_sortie() {  # $1 = plan
    case "$1" in
        decisif) echo "donnees/barreau5-familles-jumelles-v1-lecture";;
        repetition) echo "donnees/barreau5-familles-jumelles-v1-repetition";;
        *) return 1;;
    esac; }
# <<< branche
# >>> duree-de-la-marche (extrait et joué par tests/test_amorce_b5f_lecture_v1.py)
duree_marche() {  # $1 = échéance d'arrêt (s UTC), $2 = maintenant (s UTC) : secondes laissées à la marche ; code 1 sous 60 s
    local d=$(( $1 - $2 ))
    [ "$d" -ge 60 ] || return 1
    echo "$d"; }
# <<< duree-de-la-marche
# >>> fin-instance (extrait et joué par tests/test_amorce_b5f_lecture_v1.py)
fin_instance() {  # état « stopped » demandé par l'identifiant de l'instance ; la session détruit après le versement (R10)
    local c
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
    j "fin, code $1 ; état « stopped » demandé : HTTP $c ; la session vérifie le versement puis détruit par l'identifiant"
    [ "${B5F_SANS_ATTENTE:-0}" = 1 ] || sleep infinity
    exit "$1"; }
# <<< fin-instance
# >>> minuterie (extrait et joué par tests/test_amorce_b5f_lecture_v1.py ; une destruction n'est jamais jugée par un code)
minuterie() {  # $1 = échéance (s UTC). À l'échéance : versement final prouvé (témoin) → DELETE par l'identifiant ; sinon
    # « stopped » par l'identifiant, sans destruction, et signal écrit pour la mère ; la demande est refaite tant que ce
    # processus vit (il meurt avec l'instance arrêtée ou détruite)
    local n=0 c
    j "minuterie : échéance $1 ($(date -u -d "@$1" +%FT%TZ))"
    while [ "$(date +%s)" -lt "$1" ]; do sleep "${B5F_PAS_MINUTERIE:-30}"; done
    if [ -s "$TEMOIN" ]; then
        j "MINUTERIE : échéance atteinte ; versement final prouvé (commit $(cat "$TEMOIN")) : destruction de l'instance ${CONTAINER_ID:-} par son identifiant (DELETE)"
        while :; do n=$((n + 1))
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
            j "MINUTERIE : DELETE, essai $n : HTTP $c (seule l'absence de l'identifiant dans la liste prouve la destruction)"
            [ "${BLANC:-0}" = 1 ] && [ "${B5F_MINUTERIE_UNE_FOIS:-0}" = 1 ] && return 0     # essai à blanc seulement
            sleep "${B5F_PAS_MINUTERIE:-60}"; done
    fi
    printf '%s\n' "$(date -u +%FT%TZ) SIGNAL POUR LA MÈRE : instance ${CONTAINER_ID:-}, marche ${RUN_LECTURE:-} : versement final non prouvé à l'échéance (sorties ou activations gardées) ; instance arrêtée (état « stopped »), NON détruite, disque gardé ; reprendre le versement, puis détruire par l'identifiant après la preuve (nœud, R-3661)" >> "$SIGNAL"
    j "SIGNAL POUR LA MÈRE : versement final non prouvé à l'échéance : aucune destruction (nœud) ; état « stopped » demandé"
    while :; do n=$((n + 1))
        c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
        j "MINUTERIE : « stopped », essai $n : HTTP $c (aucune destruction sans preuve du versement)"
        [ "${BLANC:-0}" = 1 ] && [ "${B5F_MINUTERIE_UNE_FOIS:-0}" = 1 ] && return 0         # essai à blanc seulement
        sleep "${B5F_PAS_MINUTERIE:-60}"; done; }
# <<< minuterie
# >>> entrees (extrait et joué par tests/test_amorce_b5f_lecture_v1.py)
verifier_entrees() {  # $1 = clone des entrées extrait à ENTREES_COMMIT. Code 0 si : tête = ENTREES_COMMIT ; DOSSIER_ENTREES
    # non vide ; chacun de ses fichiers ajouté par ce seul commit (aucun n'existait avant, aucun modifié ni retiré) ; aucun
    # autre fichier extrait ; aucune référence à la branche de la formation. Sinon motif au journal, code 1
    local tous ajoutes autres
    [ "$(git -C "$1" rev-parse HEAD 2> /dev/null)" = "$ENTREES_COMMIT" ] || { j "entrées : tête ≠ ENTREES_COMMIT"; return 1; }
    tous=$(git -C "$1" ls-tree -r --name-only "$ENTREES_COMMIT" -- "$DOSSIER_ENTREES" | LC_ALL=C sort)
    [ -n "$tous" ] || { j "entrées : $DOSSIER_ENTREES vide ou absent du commit"; return 1; }
    ajoutes=$(git -C "$1" diff-tree --root --no-commit-id -r --name-status "$ENTREES_COMMIT" -- "$DOSSIER_ENTREES" \
              | awk -F '\t' '$1 == "A" { print $2 }' | LC_ALL=C sort)
    autres=$(git -C "$1" diff-tree --root --no-commit-id -r --name-status "$ENTREES_COMMIT" -- "$DOSSIER_ENTREES" \
             | awk -F '\t' '$1 != "A"')
    [ "$tous" = "$ajoutes" ] && [ -z "$autres" ] || { j "entrées : $DOSSIER_ENTREES non versé en un seul commit (point 7) : refus"; return 1; }
    [ -z "$(git -C "$1" for-each-ref --format='%(refname)' | grep 'barreau5-familles-jumelles-v1-formation')" ] \
        || { j "entrées : référence à la branche de la formation (liste d'arrêt, point 8) : refus"; return 1; }
    [ -z "$(cd "$1" && find . -path ./.git -prune -o -type f -print | grep -v "^\./$DOSSIER_ENTREES/")" ] \
        || { j "entrées : fichier hors de $DOSSIER_ENTREES extrait : refus"; return 1; }
    return 0; }
# <<< entrees
# >>> versement (extrait et joué par tests/test_amorce_b5f_lecture_v1.py)
# Les sorties sont poussées sur la branche de sortie par des commits faits à part (index séparé, parent = dernier commit
# poussé, au départ COMMIT) : la tête et l'arbre de travail de la marche ne bougent jamais. Rien n'est supprimé.
permis() {  # 0 si le chemin (relatif à $D) peut sortir de l'instance de lecture, hors activations (liste blanche)
    local f="$1" r="$RUN_LECTURE" e
    for e in "^donnees/$r/lecture/(inventaire\\.json|bilan-relecture\\.json|textes-honnetes\\.jsonl|produits\\.json|intensites\\.json|scores/[a-zA-Z0-9-]+-pli[01]\\.json|jetons/[a-zA-Z0-9-]+-pli[01]/[A-Za-z0-9_-]+\\.json)(\\.sha256)?\$" \
             "^donnees/$r/poids/[a-zA-Z0-9-]+-pli[01]\\.json(\\.sha256)?\$" \
             "^donnees/$r/(garde-activations|inventaire-activations)\\.json(\\.sha256)?\$" \
             "^runs/$r/manifeste\\.json(\\.sha256)?\$" \
             "^diag/$r/(mise-en-place|chemin|resume|arret)\\.json(\\.sha256)?\$" \
             "^traces-b5f-lecture/journal/[A-Za-z0-9._-]+\$" "^traces-b5f-lecture/inventaire-final\\.json(\\.sha256)?\$"; do
        [[ "$f" =~ $e ]] && return 0; done
    return 1; }
permis_activation() {  # 0 si le chemin est une activation gardée de la marche (demi-précision, couches du texte)
    [[ "$1" =~ ^donnees/$RUN_LECTURE/activations/[A-Za-z0-9_-]+/c(7|15|23)/[A-Za-z0-9._-]+__p[0-9]{1,3}\.npy$ ]]; }
tous_les_fichiers() { (cd "$D" && find "$@" -type f 2> /dev/null | LC_ALL=C sort); }
sorties_fermees() {  # ce qui sort avant les activations : arbre fermé, poids, inventaires, manifeste, résultats, traces
    tous_les_fichiers "donnees/$RUN_LECTURE/lecture" "donnees/$RUN_LECTURE/poids" "runs/$RUN_LECTURE" "diag/$RUN_LECTURE" \
        traces-b5f-lecture/journal
    (cd "$D" && for f in "donnees/$RUN_LECTURE"/garde-activations.json* "donnees/$RUN_LECTURE"/inventaire-activations.json*; do
        [ -f "$f" ] && printf '%s\n' "$f"; done); }
verser() {  # $1 = message ; puis chemins relatifs à $D. Pousse ceux qui existent, sont permis (PERMIS, par défaut
    # `permis`) et ne dépassent pas SEUIL ; les autres restent sur le disque, notés au journal (nœud). Code 0 si tout ce qui
    # existe est poussé (ou rien de neuf), 1 sinon
    local m="$1" ix="$T/index-sortie" parent arbre c n f a=() ecart=0
    shift
    for f in "$@"; do
        [ -e "$D/$f" ] || continue
        if ! "${PERMIS:-permis}" "$f"; then
            j "hors de la liste blanche, non poussé, gardé sur le disque : $f ($(stat -c %s "$D/$f") octets) (nœud)"
            ecart=1; continue; fi
        if [ "$(stat -c %s "$D/$f")" -gt "$SEUIL" ]; then
            j "fichier de plus de $SEUIL octets, non poussé, gardé sur le disque : $f (nœud)"; ecart=1; continue; fi
        a+=("$f"); done
    [ "${#a[@]}" -gt 0 ] || return "$ecart"
    parent=$(cat "$T/parent-sortie") || return 1
    rm -f "$ix"
    GIT_INDEX_FILE="$ix" git -C "$D" read-tree "$parent" || return 1
    GIT_INDEX_FILE="$ix" git -C "$D" add --sparse -f -- "${a[@]}" || return 1
    arbre=$(GIT_INDEX_FILE="$ix" git -C "$D" write-tree) || return 1
    [ "$arbre" != "$(git -C "$D" rev-parse "$parent^{tree}")" ] || return "$ecart"
    c=$(git -C "$D" commit-tree "$arbre" -p "$parent" -m "$m") || return 1
    for n in 1 2 3; do
        git -C "$D" push -q origin "$c:refs/heads/$BR" && { echo "$c" > "$T/parent-sortie"; j "poussé : $c « $m »"; return "$ecart"; }
        sleep $((10 * n)); done
    return 1; }
verser_par_lots() {  # $1 = message ; puis chemins d'activations : lots de LOT_OCTETS au plus, un commit poussé par lot
    # (une poussée du dépôt distant est bornée) ; chaque chemin doit être une activation gardée. Code 0 si tout est poussé
    local m="$1" lot=() taille=0 o f n=0 ecart=0
    shift
    for f in "$@"; do
        [ -f "$D/$f" ] || { j "activation gardée absente : $f (nœud)"; ecart=1; continue; }
        o=$(stat -c %s "$D/$f")
        if [ "${#lot[@]}" -gt 0 ] && [ $((taille + o)) -gt "$LOT_OCTETS" ]; then
            n=$((n + 1)); PERMIS=permis_activation verser "$m (lot $n)" "${lot[@]}" || ecart=1
            lot=(); taille=0; fi
        lot+=("$f"); taille=$((taille + o)); done
    if [ "${#lot[@]}" -gt 0 ]; then n=$((n + 1)); PERMIS=permis_activation verser "$m (lot $n)" "${lot[@]}" || ecart=1; fi
    return "$ecart"; }
# <<< versement
# >>> preuve (extrait et joué par tests/test_amorce_b5f_lecture_v1.py)
prouver_versement() {  # inventaire (noms, tailles, empreintes) des sorties fermées et des activations gardées listées
    # ($T/activations-gardees.txt, s'il existe) ; poussé ; relu : la tête de la branche distante est le dernier commit
    # poussé, et chaque fichier inventorié y est, à sa taille et à son empreinte. Écrit SORTIES_PROUVEES (commit) si tout
    # tient ; code 1 sinon
    local inv="traces-b5f-lecture/inventaire-final.json" tsv="$T/inventaire-final.tsv" f o s tete premier=1
    [ -d "$D/.git" ] && [ -f "$T/parent-sortie" ] || return 1
    mkdir -p "$D/traces-b5f-lecture" || return 1
    : > "$tsv" || return 1
    for f in $(sorties_fermees; [ -f "$T/activations-gardees.txt" ] && cat "$T/activations-gardees.txt"); do
        case "$f" in *[!A-Za-z0-9._/-]*) j "preuve : nom illisible, inventaire refusé : $f"; return 1;; esac
        [ -f "$D/$f" ] || { j "preuve : $f absent"; return 1; }
        printf '%s\t%s\t%s\n' "$f" "$(stat -c %s "$D/$f")" "$(sha256sum < "$D/$f" | cut -c1-64)" >> "$tsv" || return 1
    done
    [ -s "$tsv" ] || { j "preuve : rien à inventorier"; return 1; }
    { printf '{"run_id": "%s", "fichiers": [' "$RUN_LECTURE"
      while IFS="$(printf '\t')" read -r f o s; do
          [ "$premier" = 1 ] || printf ', '
          premier=0
          printf '{"chemin": "%s", "octets": %s, "sha256": "%s"}' "$f" "$o" "$s"
      done < "$tsv"
      printf ']}\n'; } > "$D/$inv" || return 1
    printf '%s  %s\n' "$(sha256sum < "$D/$inv" | cut -c1-64)" "inventaire-final.json" > "$D/$inv.sha256" || return 1
    verser "barreau 5, lecture : inventaire final ($(wc -l < "$tsv") fichiers)" "$inv" "$inv.sha256" || return 1
    tete=$(git -C "$D" ls-remote origin "refs/heads/$BR" | cut -f1)
    [ -n "$tete" ] && [ "$tete" = "$(cat "$T/parent-sortie")" ] || { j "preuve : tête distante ≠ dernier commit poussé"; return 1; }
    while IFS="$(printf '\t')" read -r f o s; do
        [ "$(git -C "$D" cat-file -s "$tete:$f" 2> /dev/null)" = "$o" ] \
            && [ "$(git -C "$D" cat-file blob "$tete:$f" 2> /dev/null | sha256sum | cut -c1-64)" = "$s" ] \
            || { j "preuve : $f absent du commit $tete ou différent (taille, empreinte)"; return 1; }
    done < "$tsv"
    echo "$tete" > "$SORTIES_PROUVEES"
    j "versement des sorties prouvé : $(wc -l < "$tsv") fichiers inventoriés, poussés et relus au commit $tete de $BR"
    return 0; }
temoin_final() {  # le témoin qui permet la destruction : marche menée au bout, sorties prouvées, activations gardées versées
    if [ -f "$MARCHE_FINIE" ] && [ -s "$SORTIES_PROUVEES" ] && [ -f "$ACTIVATIONS_VERSEES" ]; then
        cp -f "$SORTIES_PROUVEES" "$TEMOIN" && j "versement final prouvé au commit $(cat "$TEMOIN") : la minuterie détruira l'instance à l'échéance"
        return 0; fi
    j "versement final non prouvé (marche $([ -f "$MARCHE_FINIE" ] && echo menée || echo inachevée), sorties $([ -s "$SORTIES_PROUVEES" ] && echo prouvées || echo 'non prouvées'), activations $([ -f "$ACTIVATIONS_VERSEES" ] && echo versées || echo 'non versées')) : aucune destruction (nœud)"
    return 1; }
# <<< preuve
# 0. arguments, minuterie
verifier_arguments || exit 2
BR=$(branche_sortie "$PLAN_B5F")
if [ "$ESSAI" = 1 ]; then echo "B5F ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "B5F REFUS : identifiant de l'instance illisible"; exit 2;; esac
[ -n "${CONTAINER_API_KEY:-}" ] || { echo "B5F REFUS : CONTAINER_API_KEY absente (par le nom) : la minuterie n'arrêterait rien"; exit 2; }
DUREE=$(duree_marche "$ECHEANCE_ARRET_UTC_S" "$(date +%s)") || { echo "B5F REFUS : échéance d'arrêt passée ou trop proche"; exit 2; }
[ ! -e "$T" ] || { echo "B5F REFUS : $T existe déjà (R12)"; exit 2; }
mkdir -p "$X" || exit 2
ECHEANCE_MINUTERIE=$(( ECHEANCE_ARRET_UTC_S + VERSEMENT_S ))
minuterie "$ECHEANCE_MINUTERIE" < /dev/null &
j "minuterie lancée (PID $!, échéance $(date -u -d "@$ECHEANCE_MINUTERIE" +%FT%TZ) : destruction si le versement final est prouvé, sinon arrêt sans destruction)"
j "amorce de lecture v1 : empreinte $(sha256sum < "$0" 2> /dev/null | cut -c1-64) ; plan $PLAN_B5F, run $RUN_LECTURE, accord $GO_ID"
cp_traces() { mkdir -p "$D/traces-b5f-lecture/journal" && cp -f "$X"/* "$D/traces-b5f-lecture/journal/" 2> /dev/null; }
terminer() {  # $1 = code, $2 = motif : versement (fichiers fermés d'abord, activations gardées ensuite), preuve, fin
    local code="$1"
    j "$2"
    if [ -d "$D/.git" ] && [ -f "$T/parent-sortie" ]; then
        cp_traces
        verser "barreau 5, lecture : fichiers fermés, poids, inventaires, manifeste, résultats, traces (code $code)" \
            $(sorties_fermees) || j "versement des sorties incomplet ou en échec : voir les lignes précédentes (nœud)"
        if [ -f "$MARCHE_FINIE" ] && [ "$GARDE_B5F" = une_sur_dix ]; then
            if (cd "$D" && PYTHONPATH=src "$PY" -m controle_ia.barreau5_familles.relecture_v1 session gardees "donnees/$RUN_LECTURE") > "$T/activations-gardees.txt" \
                && verser_par_lots "barreau 5, lecture : activations gardées (une action sur dix)" $(cat "$T/activations-gardees.txt"); then
                printf 'versees\n' > "$ACTIVATIONS_VERSEES"
            else
                j "activations gardées non versées en entier (nœud)"
            fi
        elif [ -f "$MARCHE_FINIE" ]; then
            printf '%s\n' "$(date -u +%FT%TZ) SIGNAL POUR LA MÈRE : marche $RUN_LECTURE : activations gardées par la règle $GARDE_B5F, à verser sur le volume accordé (nœud 4) ; inventaire donnees/$RUN_LECTURE/inventaire-activations.json ; aucune destruction avant ce versement" >> "$SIGNAL"
            j "activations à verser sur le volume accordé (règle $GARDE_B5F) : signal pour la mère, aucune destruction"
        fi
        prouver_versement || { j "versement des sorties NON PROUVÉ : la minuterie arrêtera l'instance sans la détruire (nœud)"; [ "$code" != 0 ] || code=5; }
        temoin_final || true
        if [ "$code" = 0 ] && [ -s "$SORTIES_PROUVEES" ] && [ -f "$D/donnees/$RUN_LECTURE/lecture/inventaire.json" ]; then
            j "SCORES-B5F, contenu à inscrire par la mère après « lancer_b5f_lecture_v1.sh scores » : commit $(cat "$SORTIES_PROUVEES") ; inventaire sha256 $(sha256sum < "$D/donnees/$RUN_LECTURE/lecture/inventaire.json" | cut -c1-64)"
        fi
        cp_traces                    # journal de fin, après la preuve : un commit de plus, qui ne la change pas
        verser "barreau 5, lecture : journal de fin" $(tous_les_fichiers traces-b5f-lecture/journal) || j "journal de fin non poussé"
    else
        j "aucun dépôt cloné : rien à verser ; versement final non prouvé (nœud)"
        [ "$code" != 0 ] || code=5
    fi
    fin_instance "$code"; }
arret() { terminer "${2:-4}" "ARRET : $1"; }
# 1. machine
for o in git curl python3 sha256sum awk sed grep stat find sort timeout base64; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
[ -n "${HF_TOKEN:-}" ] || arret "HF_TOKEN absent (par le nom)" 2
case "${GH_TOKEN:-}${HF_TOKEN:-}" in *'$'*) arret "GH_TOKEN ou HF_TOKEN : un nom de variable reçu à la place d'une valeur (par le nom)" 2;; esac
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible" 2
grep -q 'A100' "$X/nvidia-smi.txt" || arret "carte autre qu'une A100 : $(head -n 1 "$X/nvidia-smi.txt")" 2
nvidia-smi > "$X/nvidia-smi-entete.txt" 2>&1 || arret "carte invisible (en-tête)" 2
V=$(sed -n 's/^.*CUDA Version: *\([0-9][0-9]*\)\.[0-9][0-9]*.*$/\1/p' "$X/nvidia-smi-entete.txt")
[ "$(printf '%s' "$V" | grep -c '^')" = 1 ] && [ "$V" -ge 13 ] 2> /dev/null || arret "CUDA servie par le pilote illisible ou < 13.0" 2
# 2. dépôt au commit COMMIT, extraction partielle nommée
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_CODE" "$DEPOT_URL" "$D" || arret "clonage" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (barreau 5, lecture)"; git -C "$D" config user.email "instance-calcul@invalid"
# >>> motifs (lus par tests/test_amorce_b5f_lecture_v1.py)
MOTIFS='/requirements-gpu.txt
/requirements-cpu.txt
/requirements-donnees.txt
/pyproject.toml
/.gitignore
/.gitattributes
/src/
/tests/conftest.py
/tests/test_barreau5_familles_lecture_v1.py
/tests/test_barreau5_familles_sondes_v1.py
/tests/test_barreau5_familles_relecture_v1.py
/scripts/amorce_b5f_lecture_v1.sh*
/scripts/lancer_b5f_lecture_v1.sh*
/prereg/T0.6-organismes-config-7b-v1.json*
/prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md*
/registres/barreau5-familles-jumelles-v1.md*
/donnees/20261007-082440-t05-extraction/taches-evaluation.json*
/docs/sources/invites-2606.08892-v1/'
# <<< motifs
{ printf '%s\n' "$MOTIFS"; [ "$EXISTANTS_CHEMINS" = "-" ] || for c in ${EXISTANTS_CHEMINS//,/ }; do printf '/%s\n' "$c"; done; } \
    | { git -C "$D" sparse-checkout init --no-cone && git -C "$D" sparse-checkout set --no-cone --stdin; } || arret "extraction partielle" 2
git -C "$D" checkout -q "$COMMIT" || arret "commit $COMMIT introuvable sur $BRANCHE_CODE" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
[ -f "$D/$PREREG" ] && [ -f "$D/registres/barreau5-familles-jumelles-v1.md" ] || arret "texte ou registre propre absent du commit" 2
for d in docs/notes diag runs brouillons; do [ ! -e "$D/$d" ] || arret "$d extrait : arrêt (jamais sur une instance de lecture)" 2; done
[ -z "$(find "$D" -path "$D/.git" -prune -o -type d -name '*-b5f-formation-*' -print)" ] || arret "marche de la formation extraite : arrêt (liste d'arrêt, point 8)" 2
[ "$EXISTANTS_CHEMINS" = "-" ] || for c in ${EXISTANTS_CHEMINS//,/ }; do [ -f "$D/$c" ] || arret "adaptateur existant absent du commit : $c" 2; done
git -C "$D" ls-remote --exit-code origin "refs/heads/$BR" > /dev/null 2>&1; [ $? = 2 ] || arret "branche de sortie $BR présente sur le dépôt distant (R12) ou dépôt injoignable" 2
echo "$COMMIT" > "$T/parent-sortie"
printf '%s' "$EXISTANTS_B5F" | base64 -d > "$T/existants.json" || arret "EXISTANTS_B5F illisible" 2
j "dépôt au commit $COMMIT (branche $BRANCHE_CODE) ; branche de sortie $BR libre"
# 3. entrées de lecture (plan décisif) : leur seul dossier, à leur commit, dans un clone à part
ENTREES=""
if [ "$PLAN_B5F" = decisif ]; then
    git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_ENTREES" "$DEPOT_URL" "$E" || arret "clonage des entrées de lecture" 2
    printf '/%s/\n' "$DOSSIER_ENTREES" | { git -C "$E" sparse-checkout init --no-cone && git -C "$E" sparse-checkout set --no-cone --stdin; } || arret "extraction des entrées" 2
    git -C "$E" checkout -q "$ENTREES_COMMIT" || arret "commit des entrées $ENTREES_COMMIT introuvable" 2
    verifier_entrees "$E" || arret "entrées de lecture refusées (voir le journal)" 2
    ENTREES="../entrees/$DOSSIER_ENTREES"
    j "entrées de lecture au commit $ENTREES_COMMIT ($(find "$E/$DOSSIER_ENTREES" -type f | wc -l) fichiers, compagnons compris)"
fi
# 4. paquets
python3 -m venv "$T/venv" && timeout -k 10 3600 "$T/venv/bin/pip" install -q -r "$D/requirements-gpu.txt" > "$X/pip.txt" 2>&1 || arret "installation des paquets" 2
PY="$T/venv/bin/python"
cd "$D" || arret "dépôt" 2
# 5. essais de la lecture
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no tests/test_barreau5_familles_lecture_v1.py \
    tests/test_barreau5_familles_sondes_v1.py tests/test_barreau5_familles_relecture_v1.py --basetemp="$T/essais-tmp" > "$X/essais.txt" 2> "$X/essais.err"; c=$?
RES=$(tail -n 1 "$X/essais.txt"); NP=$(printf '%s\n' "$RES" | grep -oE '[0-9]+ passed' | grep -oE '[0-9]+' | head -n 1)
j "essais de la lecture : code $c, ligne de compte : $RES"
[ "$c" = 0 ] && [ "${NP:-0}" -ge "$MIN_ESSAIS" ] || arret "essais de la lecture en échec ou moins de $MIN_ESSAIS passés" 2
[ -z "$(git status --porcelain --untracked-files=all -- src tests prereg registres)" ] || arret "les essais ont écrit dans le dépôt" 2
# 6. modèle au cache local (révision de la configuration scellée)
PYTHONPATH=src timeout -k 10 3600 "$PY" -m controle_ia.barreau5_familles.relecture_v1 session precharger . > "$X/modele.txt" 2>&1 || arret "descente du modèle" 2
j "modèle au cache local"
# 7. configuration réelle de la marche (recette lue dans la configuration scellée), hors du dépôt
PYTHONPATH=src "$PY" -m controle_ia.barreau5_familles.relecture_v1 session config . "$GO_ID" "$PLAN_B5F" "$ENTREES" \
    "$DIVERGENCE_B5F" "$GARDE_B5F" "$T/existants.json" > "$T/config-lecture.json" 2> "$X/config.err" || arret "configuration refusée (config.err)" 2
cp -f "$T/config-lecture.json" "$X/config-lecture.json"
# 8. marche, sous timeout jusqu'à l'échéance d'arrêt ; attente par `wait` (aucun versement pendant la marche : les fichiers
# fermés n'existent qu'à la fin ; la marche est bornée par `timeout`, la minuterie veille à part)
DUREE=$(duree_marche "$ECHEANCE_ARRET_UTC_S" "$(date +%s)") || arret "échéance d'arrêt atteinte avant la marche" 3
[ -z "$(git status --porcelain --untracked-files=all)" ] || arret "arbre non propre avant la marche" 2
j "marche : début (run $RUN_LECTURE, $DUREE s au plus)"
env HF_HUB_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONPATH=src timeout --signal=TERM --kill-after=120 "$DUREE" \
    "$PY" -m controle_ia.barreau5_familles.relecture_v1 --config "$T/config-lecture.json" --run-id "$RUN_LECTURE" \
    --prereg "$PREREG" > "$X/marche.txt" 2> "$X/marche.err" &
PID=$!
j "marche lancée (PID $PID ; arrêt par ce seul processus, R10)"
wait "$PID"; c=$?
j "marche : code $c"
# 9. versement, preuve ; 10. fin (rien n'est supprimé)
case "$c" in
    0) printf 'menee\n' > "$MARCHE_FINIE"; terminer 0 "FIN : marche menée au bout";;
    124) terminer 3 "ARRET : échéance d'arrêt atteinte (cumul plus un quart d'heure à la coupure) : marche arrêtée par TERM";;
    *) terminer 4 "ARRET : marche : arrêt écrit, code $c (marche.err ; diag/$RUN_LECTURE/arret.json)";;
esac
