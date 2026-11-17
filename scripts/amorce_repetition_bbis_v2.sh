#!/usr/bin/env bash
# Amorce de la répétition sur carte de l'étape B bis de T0.7, v2 (quatrième passe : la v1, qui joue
# scripts/repetition_carte_bbis_v2.py et lit scripts/amorce_bbis_v2.sh ; contrôle carte-processeur aux deux horizons,
# R-2917 ; blocs marqués identiques à ceux de la v1 hors les noms ; la v1 reste, R12) (mot de Lazar R-2802 : écart déclaré au texte scellé ; sous la
# ligne GO-2026-11-14-09, plafond de la répétition strictement sous 3 USD, une seule machine). **Données synthétiques seulement** :
# aucune entrée de 7b n'est lue ni copiée (aucune branche autre que BRANCHE_CODE n'est récupérée ; runs/, diag/, donnees/, essai/
# absents de l'arbre extrait, sinon arrêt). Passée par scripts/lancer_repetition_bbis_v2.sh (commande de création imprimée,
# base64) ; écrit sous $R/bbis-t07-repetition-v1 seulement. Chaque étape est une fonction marquée, jouée par les essais
# (tests/test_repetition_bbis_v1.py) avec de faux outils.
# Ordre : 0. arguments ; un refus **avant** la minuterie demande la destruction de l'instance par elle-même (DELETE, jamais jugé,
#   puis « stopped ») ; minuterie de destruction armée avant toute passe (même texte que celle de la course) ; piège de sortie
#   (`set -u`, erreur imprévue : traces poussées si possible, instance laissée en marche, minuterie armée) ; 1. machine (A100 SXM4
#   80 Go, clé par son nom) ; 2. dépôt au commit COMMIT, branche de sortie neuve contrôlée (dès lors tout arrêt pousse ses
#   traces), extraction partielle réelle par les MOTIFS de la course lus au commit, aucune entrée de 7b, script de la répétition
#   pris au commit hors de l'arbre, empreinte SCRIPT_SHA256 ; version CUDA servie par le pilote (en-tête de nvidia-smi, lu à
#   l'étape 1) au moins 13.0, sinon arrêt avant toute installation (code 2, traces poussées) ; 3. paquets : pip verbeux borné
#   par `timeout`, durée écrite ;
#   4. essais de l'arbre de l'instance par la commande de la course, MIN_ESSAIS de la course ; 5. carte ; 6. traces poussées sur
#   calcul/t07bbis-repetition-v3 (commit des seules traces posé sur COMMIT). **Budget** : chaque étape longue est bornée pour que le
#   travail cesse RESERVE_FIN_S (15 min) avant l'échéance et que les traces partent avant la destruction (code 10).
#   **Fin voulue** (fin_instance) : ni « stopped » ni sortie : l'instance reste en marche, minuterie armée, jusqu'à la destruction
#   par la mère (-y, absence vérifiée) ou l'échéance ; le coût reste borné par l'échéance (plafond calculé jusqu'à elle).
# Codes de fin réellement émis : 0 réussie ; 2 garde ; 4 autre ; 5 installation au-delà de 60 min ; 6 installation en échec ;
#   7 essais en échec ou moins de MIN_ESSAIS ; 8 erreur d'apprentissage ; 9 contrôle carte-processeur ou non-déterminisme ;
#   10 échéance proche (travail interrompu, traces poussées). Le code 3 n'est jamais émis.
# Variables (--env) : COMMIT, BRANCHE_CODE, ECHEANCE_UTC_S, GO_ID (GO-2026-11-14-09), SCRIPT_SHA256, GH_TOKEN ; facultative
#   ACTIONS_REPETITION ; posées par Vast : CONTAINER_ID, CONTAINER_API_KEY. Aucune clé n'est jamais affichée. Essai local
#   (AMORCE_ESSAI_LOCAL=1) : contrôles des arguments seulement, aucun réseau, aucune écriture.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
R="${RACINE_AMORCE:-/root}"
[ "$ESSAI" = 1 ] || [ -z "${RACINE_AMORCE:-}" ] || { echo "BBIS REPETITION REFUS : RACINE_AMORCE en essai local seulement"; exit 2; }
T="$R/bbis-t07-repetition-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-repetition.txt"; XT=traces/bbis-t07-repetition-v2
API=https://console.vast.ai/api/v0
GO_ATTENDU=GO-2026-11-14-09
# R12 : nouvelle passe, nouveau nom (calcul/t07bbis-repetition-v1 : passe du 15 novembre, 56f5b8b8 ;
# calcul/t07bbis-repetition-v2 : troisième passe, 3528a2e8, arrêt en code 9)
BR_SORTIE=calcul/t07bbis-repetition-v3
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
SEUIL=94000000
DELAI_PIP_S=3600
ECHEANCE_MAX_S=10800
RESERVE_FIN_S=900
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
j() { printf '%s BBIS REPETITION %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
SORTIE_LIBRE=0
FIN_VOULUE=0
# >>> refus-avant-minuterie (extrait et joué par tests/test_repetition_bbis_v1.py ; contre-lecture de sûreté M2 bis (i))
entier_ascii() { printf '%s' "$1" | LC_ALL=C grep -qxE '[1-9][0-9]*'; }
refus() {  # refus avant la minuterie : en marche réelle, l'instance demande sa propre destruction (jamais jugée), puis « stopped »
    local n c
    echo "BBIS REPETITION REFUS : $1"
    if [ "$ESSAI" != 1 ]; then
        if entier_ascii "${CONTAINER_ID:-}"; then
            for n in 1 2 3; do
                c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                    "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
                echo "BBIS REPETITION REFUS : destruction demandée par l'instance, essai $n : HTTP $c (jamais jugé)"; sleep 20; done
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
            echo "BBIS REPETITION REFUS : état « stopped » demandé : HTTP $c ; la mère vérifie l'absence (verifier-destruction)"
        else
            echo "BBIS REPETITION REFUS : identifiant de l'instance illisible : aucune destruction par l'instance ; la mère détruit (geste 9)"
        fi
    fi
    exit 2; }
# <<< refus-avant-minuterie
# >>> fins (extrait et joué par tests/test_repetition_bbis_v1.py ; contre-lecture de sûreté M2 bis (ii), (iii))
traces() { mkdir -p "$D/$XT" && cp -f "$X"/* "$D/$XT/"; }
pousser_traces() {  # commit des seules traces posé sur COMMIT par un index à part, poussé une fois sur la branche neuve
    local ix="$T/index-traces-repetition" arbre c f n
    SORTIE_LIBRE=0
    [ ! -e "$ix" ] && traces || return 1
    for f in "$D/$XT"/*; do [ "$(stat -c %s "$f")" -le "$SEUIL" ] || return 1; done
    GIT_INDEX_FILE="$ix" git -C "$D" read-tree "$COMMIT" && GIT_INDEX_FILE="$ix" git -C "$D" add --sparse -f -- "$XT" || return 1
    arbre=$(GIT_INDEX_FILE="$ix" git -C "$D" write-tree) || return 1
    c=$(git -C "$D" commit-tree "$arbre" -p "$COMMIT" -m "B bis : traces de la répétition sur carte ($1)") || return 1
    for n in 1 2 3; do git -C "$D" push -q origin "$c:refs/heads/$BR_SORTIE" \
        && { j "traces poussées : $c (parent $COMMIT, branche $BR_SORTIE)"; return 0; }; sleep $((20 * n)); done
    return 1; }
fin_instance() {  # fin voulue : ni « stopped » ni sortie ; l'instance reste en marche, minuterie armée (coût borné par l'échéance)
    FIN_VOULUE=1
    j "fin, code $1 ; instance laissée en marche, minuterie armée jusqu'à l'échéance ; la mère lit vastai logs, puis détruit (-y) et vérifie l'absence (gestes 8 et 9, dans les 15 minutes)"
    sleep infinity; exit "$1"; }
arret() { j "ARRET : $1"
    if [ "$SORTIE_LIBRE" = 1 ]; then pousser_traces "arrêt, code ${2:-4}" || j "traces non poussées"; fi
    fin_instance "${2:-4}"; }
fin_inattendue() {  # piège de sortie (`set -u`, erreur imprévue) : traces poussées si possible ; instance laissée en marche
    local c="$1"
    set +u
    [ "$FIN_VOULUE" = 1 ] && return 0
    FIN_VOULUE=1
    j "SORTIE INATTENDUE (code $c) : traces poussées si possible ; instance laissée en marche, minuterie armée jusqu'à l'échéance"
    if [ "$SORTIE_LIBRE" = 1 ]; then pousser_traces "sortie inattendue, code $c" || j "traces non poussées"; fi
    sleep infinity; }
# <<< fins
# >>> budget (extrait et joué par tests/test_repetition_bbis_v1.py ; contre-lecture M-4)
budget_ou_arret() {  # BUDGET = secondes de travail avant la réserve de fin ; moins d'une minute : arrêt 10, traces poussées
    BUDGET=$(( ECHEANCE_UTC_S - RESERVE_FIN_S - $(date +%s) ))
    [ "$BUDGET" -gt 60 ] || arret "échéance proche : plus de temps pour $1 (réserve de fin de $RESERVE_FIN_S s avant l'échéance)" 10; }
# <<< budget
# 0. arguments, échéance, minuterie
for v in COMMIT BRANCHE_CODE ECHEANCE_UTC_S GO_ID SCRIPT_SHA256; do [ -n "${!v:-}" ] || refus "variable $v absente"; done
case "$COMMIT" in *[!0-9a-f]*|'') refus "COMMIT illisible";; esac
[ "${#COMMIT}" = 40 ] || refus "COMMIT de 40 caractères attendu"
case "$SCRIPT_SHA256" in *[!0-9a-f]*|'') refus "SCRIPT_SHA256 illisible";; esac
[ "${#SCRIPT_SHA256}" = 64 ] || refus "SCRIPT_SHA256 de 64 caractères attendu"
[ "$GO_ID" = "$GO_ATTENDU" ] || refus "GO_ID $GO_ID ≠ $GO_ATTENDU"
entier_ascii "$ECHEANCE_UTC_S" || refus "ECHEANCE_UTC_S illisible"
entier_ascii "${ACTIONS_REPETITION:-640}" || refus "ACTIONS_REPETITION illisible"
if [ "$ESSAI" = 1 ]; then echo "BBIS REPETITION ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
entier_ascii "${CONTAINER_ID:-}" || refus "identifiant de l'instance illisible"
[ "$ECHEANCE_UTC_S" -gt "$(date +%s)" ] && [ "$ECHEANCE_UTC_S" -le $(( $(date +%s) + ECHEANCE_MAX_S )) ] || refus "échéance hors de [maintenant, + 3 h]"
mkdir -p "$X" || refus "$X impossible"
# >>> minuterie (même texte que celle de la course ; destruction jamais jugée par un code de retour, R-2789)
minuterie() { local n=0 c; while [ "$(date +%s)" -lt "$ECHEANCE_UTC_S" ]; do sleep 30; done
    j "MINUTERIE : échéance atteinte : destruction de l'instance $CONTAINER_ID par son identifiant (DELETE)"
    while :; do n=$((n + 1))
        c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
        j "MINUTERIE : DELETE, essai $n : HTTP $c (code jamais jugé ; seule l'absence de l'identifiant dans la liste des instances, lue par la session, prouve la destruction ; nouvel essai dans 60 s si l'instance vit encore)"
        if [ "$n" = 5 ]; then
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
            j "MINUTERIE : instance toujours vivante après 5 demandes de destruction : état « stopped » demandé : HTTP $c ; la session vérifie l'absence (verifier-destruction)"
        fi
        sleep 60; done; }
# <<< minuterie
minuterie < /dev/null & j "minuterie lancée (PID $!, échéance $(date -u -d "@$ECHEANCE_UTC_S" +%FT%TZ)), avant toute passe"
trap 'fin_inattendue $?' EXIT
# >>> cuda-du-pilote (même texte dans les deux amorces de B bis ; extrait et joué par tests/test_repetition_bbis_v1.py)
# Roue torch 2.14.1 de requirements-gpu.txt construite pour CUDA 13.0 : le pilote doit servir CUDA 13.0 au moins, lu dans l'en-tête
# de `nvidia-smi` (« CUDA Version: M.m », une fois exactement), AVANT l'installation des paquets (répétition du 15 novembre :
# pilote 570.211.01, CUDA 12.8, arrêt « torch ne voit pas la carte » après 118 s d'installation). Absente, multiple ou illisible :
# arrêt, jamais un défaut deviné ; même code que « torch ne voit pas la carte » (2).
cuda_du_pilote() {  # $1 = fichier de la sortie de `nvidia-smi` sans argument : imprime « M.m » ; 1 si absente, multiple ou illisible
    local v
    v=$(sed -n 's/^.*CUDA Version: *\([0-9][0-9]*\.[0-9][0-9]*\)[^0-9.].*$/\1/p; s/^.*CUDA Version: *\([0-9][0-9]*\.[0-9][0-9]*\)$/\1/p' "$1" 2>/dev/null)
    [ "$(printf '%s' "$v" | grep -c '^')" = 1 ] || return 1
    printf '%s\n' "$v" | LC_ALL=C grep -qxE '[0-9]{1,3}\.[0-9]{1,3}' || return 1
    printf '%s\n' "$v"; }
exiger_cuda_du_pilote() {  # $1 = fichier de la sortie de `nvidia-smi` ; arrêt (code 2) sous 13.0, absente ou illisible
    local v
    v=$(cuda_du_pilote "$1") || { j "lignes « CUDA » lues dans l'en-tête : $(grep -a 'CUDA' "$1" 2>/dev/null | head -n 3 | cut -c1-200 | tr '\n' ' ')"
        arret "version CUDA servie par le pilote illisible (« CUDA Version: » absent, multiple ou illisible dans la sortie de nvidia-smi) : torch ne verrait pas la carte (roue CUDA 13.0) ; arrêt avant l'installation des paquets" 2; }
    if [ "$((10#${v%%.*}))" -lt 13 ]; then
        arret "pilote trop ancien : CUDA $v servie par le pilote < 13.0 exigée par la roue torch de requirements-gpu.txt : torch ne verrait pas la carte ; arrêt avant l'installation des paquets" 2
    fi
    j "CUDA servie par le pilote : $v (au moins 13.0)"; }
# <<< cuda-du-pilote
# >>> machine (extrait et joué par tests/test_repetition_bbis_v1.py)
verifier_machine() {
    local o
    for o in git curl python3 sha256sum awk sed grep stat timeout; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
    [ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
    nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible (nvidia-smi)" 2
    grep -q 'A100-SXM4-80GB' "$X/nvidia-smi.txt" || arret "carte autre qu'une A100 SXM4 80 Go (celle de la course) : $(head -n 1 "$X/nvidia-smi.txt")" 2
    nvidia-smi > "$X/nvidia-smi-entete.txt" 2>&1 || arret "carte invisible (nvidia-smi, en-tête)" 2
    j "carte : $(head -n 1 "$X/nvidia-smi.txt") ; disque libre $(df -P -B1 "$R" | awk 'NR == 2 { print $4 }') octets"; }
verifier_torch() {  # $1 = python du venv
    "$1" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte" 2; }
# <<< machine
# >>> motifs-de-la-course (extrait et joué par tests/test_repetition_bbis_v1.py)
motifs_de_la_course() {  # $1 = texte de scripts/amorce_bbis_v2.sh au commit : imprime ses MOTIFS ; une définition exactement
    [ "$(printf '%s\n' "$1" | grep -c "^MOTIFS='")" = 1 ] || return 1
    printf '%s\n' "$1" | awk "/^MOTIFS='/ { f = 1; sub(/^MOTIFS='/, \"\") } f { if (/'\$/) { sub(/'\$/, \"\"); print; exit } print }"; }
jamais_7b() {  # $1 = racine de l'arbre extrait : aucune entrée de 7b (ni de 7a, T0.7, P3-bis) possible
    local p; for p in runs diag donnees essai; do [ ! -e "$1/$p" ] || return 1; done; return 0; }
# <<< motifs-de-la-course
# >>> depot (extrait et joué par tests/test_repetition_bbis_v1.py)
preparer_depot() {  # $1 = adresse du dépôt ; pose A_COURSE et S
    local aide
    [ ! -e "$D" ] || arret "$D existe déjà (R12)" 2
    aide='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
    git -c credential.helper="$aide" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_CODE" "$1" "$D" || arret "clonage" 2
    git -C "$D" config credential.helper "$aide"; git -C "$D" config user.name "instance de calcul (répétition B bis)"; git -C "$D" config user.email "instance-calcul@invalid"
    git -C "$D" ls-remote --exit-code origin "refs/heads/$BR_SORTIE" > /dev/null 2>&1; [ $? = 2 ] || arret "branche $BR_SORTIE présente sur le dépôt distant (R12) ou dépôt injoignable" 2
    SORTIE_LIBRE=1
    A_COURSE=$(git -C "$D" show "$COMMIT:scripts/amorce_bbis_v2.sh") || arret "amorce de la course illisible au commit $COMMIT" 2
    MOTIFS=$(motifs_de_la_course "$A_COURSE") || arret "MOTIFS de la course illisibles ou multiples" 2
    git -C "$D" sparse-checkout init --no-cone && printf '%s\n' "$MOTIFS" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
    git -C "$D" checkout -q "$COMMIT" || arret "commit $COMMIT introuvable sur $BRANCHE_CODE" 2
    [ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
    jamais_7b "$D" || arret "runs/, diag/, donnees/ ou essai/ présent dans l'arbre extrait : arrêt (aucune entrée de 7b)" 2
    S="$T/repetition_carte_bbis_v2.py"
    git -C "$D" show "HEAD:scripts/repetition_carte_bbis_v2.py" > "$S" || arret "script de la répétition absent du commit" 2
    [ "$(sha256sum < "$S" | cut -d' ' -f1)" = "$SCRIPT_SHA256" ] || arret "script de la répétition : empreinte ≠ SCRIPT_SHA256" 2
    j "dépôt au commit $COMMIT (branche $BRANCHE_CODE) ; extraction partielle par les MOTIFS de la course ; aucune entrée de 7b ; script de la répétition à l'empreinte attendue"; }
# <<< depot
# >>> installation (extrait et joué par tests/test_repetition_bbis_v1.py)
installer() {  # $1 = python du venv ; $2 = exigences ; $3 = journal verbeux complet ; délai DELAI (défaut DELAI_PIP_S) ; 0, 5, 6
    local c t0
    t0=$(date +%s)
    timeout -k 30 "${DELAI:-$DELAI_PIP_S}" "$1" -m pip install -v -r "$2" > "$3" 2>&1; c=$?
    DUREE_PIP=$(( $(date +%s) - t0 ))
    case "$c" in 0) return 0;; 124|137) return 5;; *) return 6;; esac; }
installer_paquets() {  # $1 = python du venv : pip borné par min(DELAI_PIP_S, budget) ; 5 au-delà de 60 min, 10 si le budget coupe
    local c
    budget_ou_arret "l'installation"
    DELAI=$(( BUDGET < DELAI_PIP_S ? BUDGET : DELAI_PIP_S ))
    installer "$1" "$D/requirements-gpu.txt" "$T/pip-verbeux-complet.txt"; c=$?
    { head -c 2000000 "$T/pip-verbeux-complet.txt"; echo; echo "[…]"; tail -c 20000000 "$T/pip-verbeux-complet.txt"; } > "$X/pip-verbeux.txt" 2>/dev/null
    j "installation des paquets : code $c, $DUREE_PIP s (délai $DELAI s ; journal verbeux : pip-verbeux.txt, début et fin)"
    case "$c" in 0) ;;
        5) if [ "$DELAI" -lt "$DELAI_PIP_S" ]; then arret "échéance proche : installation interrompue après $DELAI s" 10
           else arret "installation au-delà de $DELAI_PIP_S s (pip-verbeux.txt)" 5; fi;;
        *) arret "installation en échec (pip-verbeux.txt)" 6;; esac; }
# <<< installation
# >>> lecture-de-la-course (extrait et joué par tests/test_repetition_bbis_v1.py)
lire_course() {  # $1 = texte de scripts/amorce_bbis_v2.sh : définit compte_passes (texte même de la course) et MIN_COURSE
    eval "$(printf '%s\n' "$1" | sed -n '/^# >>> compte-des-essais/,/^# <<< compte-des-essais/p')"
    declare -F compte_passes > /dev/null || return 1
    MIN_COURSE=$(printf '%s\n' "$1" | sed -n 's/^MIN_ESSAIS=\([0-9][0-9]*\)$/\1/p')
    [ "$(printf '%s\n' "$MIN_COURSE" | grep -c '[0-9]')" = 1 ] || return 1; }
resume_carte() {  # $1 = python ; $2 = sortie de la partie carte : une ligne pour le journal (aucune aire)
    "$1" -I -c 'import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
g = d.get("garde_de_debit") or {}
c = {f: x.get("ecart_relatif_max", x.get("refus")) for f, x in (d.get("controle_carte_processeur") or {}).items()}
print("état", d.get("etat"), "; jetons", d.get("jetons"), "; déterministe", d.get("deterministe"), "; médiane",
      g.get("mediane_s"), "s ; projeté", g.get("projete_h"), "h (limite", g.get("limite_h"), ") ; écarts carte-processeur", c)' "$2"; }
# <<< lecture-de-la-course
# >>> essais-et-carte (extrait et joué par tests/test_repetition_bbis_v1.py)
essais_de_la_course() {  # $1 = python du venv ; dans l'arbre extrait ; A_COURSE posé
    local c np res
    lire_course "$A_COURSE" || arret "compte des essais ou MIN_ESSAIS de la course illisible ou multiple" 2
    budget_ou_arret "les essais"
    timeout -k 30 "$BUDGET" env PYTHONPATH=src "$1" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py \
        --basetemp="$T/essais-tmp" > "$X/essais.txt" 2> "$X/essais.err"; c=$?
    res=$(tail -n 1 "$X/essais.txt")
    j "essais de l'arbre de l'instance : code $c, ligne de compte : $res ; minimum de la course : $MIN_COURSE"
    case "$c" in 0) ;; 124|137) arret "échéance proche : essais interrompus (essais.txt)" 10;; *) arret "essais en échec (essais.txt)" 7;; esac
    np=$(compte_passes "$res")
    [ "$np" -ge "$MIN_COURSE" ] || arret "essais : $np passés < MIN_ESSAIS $MIN_COURSE de la course (essais.txt, sautés nommés par -rs)" 7
    [ -z "$(git -C "$D" status --porcelain --untracked-files=all -- src tests)" ] || arret "les essais ont écrit sous src ou tests" 2; }
partie_carte() {  # $1 = python du venv ; S posé
    local c
    budget_ou_arret "la partie carte"
    timeout -k 30 "$BUDGET" env CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONPATH=src "$1" "$S" carte --sortie "$X/repetition-carte.json" \
        --actions "${ACTIONS_REPETITION:-640}" > "$X/carte.txt" 2> "$X/carte.err"; c=$?
    j "carte : code $c ; $(tail -n 1 "$X/carte.txt")"
    if [ -e "$X/repetition-carte.json" ]; then resume_carte "$1" "$X/repetition-carte.json" > "$X/carte-resume.txt" 2>&1; j "carte : $(cat "$X/carte-resume.txt")"; fi
    case "$c" in 0) ;; 8) arret "carte : erreur d'apprentissage (repetition-carte.json, carte.err)" 8;;
        9) arret "carte : contrôle carte-processeur au-delà de 10⁻⁴ ou apprentissage non déterministe (repetition-carte.json)" 9;;
        2) arret "carte : garde (repetition-carte.json)" 2;;
        124|137) arret "échéance proche : partie carte interrompue (état partiel dans repetition-carte.json)" 10;;
        *) arret "carte : code $c (carte.err)" 4;; esac; }
# <<< essais-et-carte
# 1. machine ; 2. dépôt, puis CUDA du pilote ; 3. paquets ; 4. essais ; 5. carte ; 6. traces et fin
verifier_machine
preparer_depot "$DEPOT_URL_OFFICIEL"
exiger_cuda_du_pilote "$X/nvidia-smi-entete.txt"   # après le dépôt (traces poussées sur COMMIT), avant toute installation
python3 -m venv "$T/venv" || arret "environnement virtuel" 6
installer_paquets "$T/venv/bin/python"
PY="$T/venv/bin/python"
verifier_torch "$PY"
"$PY" -m pip freeze --all > "$X/pip-freeze.txt" 2>/dev/null
cd "$D" || arret "dépôt" 2
essais_de_la_course "$PY"
partie_carte "$PY"
j "FIN : répétition menée au bout"
pousser_traces "répétition menée au bout" || { j "traces non poussées"; fin_instance 4; }
fin_instance 0
