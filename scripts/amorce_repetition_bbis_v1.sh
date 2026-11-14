#!/usr/bin/env bash
# Amorce de la répétition sur carte de l'étape B bis de T0.7, v1 (mot de Lazar R-2802 : écart déclaré au texte scellé ; sous la
# ligne GO-2026-11-14-09, plafond de la répétition 3 USD, une seule machine). **Données synthétiques seulement** : aucune entrée
# de 7b n'est lue ni copiée (aucune branche autre que BRANCHE_CODE n'est récupérée ; runs/, diag/, donnees/, essai/ absents de
# l'arbre extrait, sinon arrêt). Passée par scripts/lancer_repetition_bbis_v1.sh (commande de création imprimée, base64) ; écrit
# sous $R/bbis-t07-repetition-v1 seulement.
# Ordre : 0. arguments, minuterie de destruction armée avant toute passe (DELETE par l'identifiant, jamais jugé par son code :
#   refait tant que l'instance vit) ; 1. machine (A100, clé par son nom) ; 2. dépôt au commit COMMIT, branche de sortie neuve
#   contrôlée (dès lors tout arrêt pousse ses traces), **extraction partielle réelle** : les MOTIFS de scripts/amorce_bbis_v1.sh
#   lus au commit ; script de la répétition pris au commit hors de l'arbre, empreinte égale à SCRIPT_SHA256 ; 3. paquets : pip
#   **verbeux**, borné par `timeout` (DELAI_PIP_S), durée écrite, code dédié 5 au-delà du délai, 6 en échec ; 4. essais de l'arbre
#   de l'instance par la commande de la course, au moins MIN_ESSAIS de la course (lu au commit), sinon 7 ; 5. carte :
#   `scripts/repetition_carte_bbis_v1.py carte` (entrainer, deux familles, algorithmes déterministes, contrôle carte-processeur à
#   10⁻⁴, durées) ; 8 erreur d'apprentissage, 9 contrôle au-delà du seuil ou non-déterminisme ; 6. traces poussées sur la branche
#   neuve calcul/t07bbis-repetition-v1 (commit des seules traces posé sur COMMIT), état « stopped » demandé ; la session détruit
#   par l'identifiant avec -y et vérifie l'absence (lancer_repetition_bbis_v1.sh verifier-destruction).
# Variables (--env) : COMMIT, BRANCHE_CODE, ECHEANCE_UTC_S, GO_ID (GO-2026-11-14-09), SCRIPT_SHA256, GH_TOKEN ; facultative
#   ACTIONS_REPETITION (fraction déclarée de la taille de la course, 640 actions par défaut) ; posées par Vast : CONTAINER_ID,
#   CONTAINER_API_KEY. Aucune clé n'est jamais affichée. Essai local (AMORCE_ESSAI_LOCAL=1) : contrôles des arguments seulement,
#   aucun réseau, aucune écriture.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
R="${RACINE_AMORCE:-/root}"
[ "$ESSAI" = 1 ] || [ -z "${RACINE_AMORCE:-}" ] || { echo "BBIS REPETITION REFUS : RACINE_AMORCE en essai local seulement"; exit 2; }
T="$R/bbis-t07-repetition-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-repetition.txt"; XT=traces/bbis-t07-repetition-v1
API=https://console.vast.ai/api/v0
GO_ATTENDU=GO-2026-11-14-09
BR_SORTIE=calcul/t07bbis-repetition-v1
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
SEUIL=94000000
DELAI_PIP_S=3600
ECHEANCE_MAX_S=10800
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
j() { printf '%s BBIS REPETITION %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
SORTIE_LIBRE=0
fin_instance() {  # état « stopped » demandé ; la session détruit par l'identifiant avec -y et vérifie l'absence
    local c
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    j "fin, code $1 ; état « stopped » demandé : HTTP $c ; la session détruit par l'identifiant (-y) et vérifie l'absence"
    sleep infinity; exit "$1"; }
# >>> traces-de-la-repetition (extrait et joué par tests/test_repetition_bbis_v1.py)
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
arret() { j "ARRET : $1"
    if [ "$SORTIE_LIBRE" = 1 ]; then pousser_traces "arrêt, code ${2:-4}" || j "traces non poussées"; fi
    fin_instance "${2:-4}"; }
# <<< traces-de-la-repetition
# 0. arguments, échéance, minuterie
for v in COMMIT BRANCHE_CODE ECHEANCE_UTC_S GO_ID SCRIPT_SHA256; do
    [ -n "${!v:-}" ] || { echo "BBIS REPETITION REFUS : variable $v absente"; exit 2; }; done
case "$COMMIT" in *[!0-9a-f]*|'') echo "BBIS REPETITION REFUS : COMMIT illisible"; exit 2;; esac
[ "${#COMMIT}" = 40 ] || { echo "BBIS REPETITION REFUS : COMMIT de 40 caractères attendu"; exit 2; }
case "$SCRIPT_SHA256" in *[!0-9a-f]*|'') echo "BBIS REPETITION REFUS : SCRIPT_SHA256 illisible"; exit 2;; esac
[ "${#SCRIPT_SHA256}" = 64 ] || { echo "BBIS REPETITION REFUS : SCRIPT_SHA256 de 64 caractères attendu"; exit 2; }
[ "$GO_ID" = "$GO_ATTENDU" ] || { echo "BBIS REPETITION REFUS : GO_ID $GO_ID ≠ $GO_ATTENDU"; exit 2; }
case "$ECHEANCE_UTC_S" in ''|*[!0-9]*) echo "BBIS REPETITION REFUS : ECHEANCE_UTC_S illisible"; exit 2;; esac
case "${ACTIONS_REPETITION:-640}" in ''|*[!0-9]*) echo "BBIS REPETITION REFUS : ACTIONS_REPETITION illisible"; exit 2;; esac
if [ "$ESSAI" = 1 ]; then echo "BBIS REPETITION ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
mkdir -p "$X" || { echo "BBIS REPETITION REFUS : $X impossible"; exit 2; }
[ "$ECHEANCE_UTC_S" -gt "$(date +%s)" ] && [ "$ECHEANCE_UTC_S" -le $(( $(date +%s) + ECHEANCE_MAX_S )) ] || { echo "BBIS REPETITION REFUS : échéance hors de [maintenant, + 3 h]"; exit 2; }
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "BBIS REPETITION REFUS : identifiant de l'instance illisible"; exit 2;; esac
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
# 1. machine
for o in git curl python3 sha256sum awk sed grep stat timeout; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible (nvidia-smi)" 2
grep -q 'A100' "$X/nvidia-smi.txt" || arret "carte autre qu'une A100 (celle de la course) : $(head -n 1 "$X/nvidia-smi.txt")" 2
j "carte : $(head -n 1 "$X/nvidia-smi.txt") ; disque libre $(df -P -B1 "$R" | awk 'NR == 2 { print $4 }') octets"
# 2. dépôt au commit COMMIT, branche de sortie neuve, extraction partielle de la course, aucune entrée de 7b
[ ! -e "$D" ] || arret "$D existe déjà (R12)" 2
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_CODE" "$DEPOT_URL_OFFICIEL" "$D" || arret "clonage" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (répétition B bis)"; git -C "$D" config user.email "instance-calcul@invalid"
git -C "$D" ls-remote --exit-code origin "refs/heads/$BR_SORTIE" > /dev/null 2>&1; [ $? = 2 ] || arret "branche $BR_SORTIE présente sur le dépôt distant (R12) ou dépôt injoignable" 2
SORTIE_LIBRE=1
# >>> motifs-de-la-course (extrait et joué par tests/test_repetition_bbis_v1.py)
motifs_de_la_course() {  # $1 = texte de scripts/amorce_bbis_v1.sh au commit : imprime ses MOTIFS ; une définition exactement
    [ "$(printf '%s\n' "$1" | grep -c "^MOTIFS='")" = 1 ] || return 1
    printf '%s\n' "$1" | awk "/^MOTIFS='/ { f = 1; sub(/^MOTIFS='/, \"\") } f { if (/'\$/) { sub(/'\$/, \"\"); print; exit } print }"; }
jamais_7b() {  # $1 = racine de l'arbre extrait : aucune entrée de 7b (ni de 7a, T0.7, P3-bis) possible
    local p; for p in runs diag donnees essai; do [ ! -e "$1/$p" ] || return 1; done; return 0; }
# <<< motifs-de-la-course
A_COURSE=$(git -C "$D" show "$COMMIT:scripts/amorce_bbis_v1.sh") || arret "amorce de la course illisible au commit $COMMIT" 2
MOTIFS=$(motifs_de_la_course "$A_COURSE") || arret "MOTIFS de la course illisibles ou multiples" 2
git -C "$D" sparse-checkout init --no-cone && printf '%s\n' "$MOTIFS" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$COMMIT" || arret "commit $COMMIT introuvable sur $BRANCHE_CODE" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
jamais_7b "$D" || arret "runs/, diag/, donnees/ ou essai/ présent dans l'arbre extrait : arrêt (aucune entrée de 7b)" 2
S="$T/repetition_carte_bbis_v1.py"
git -C "$D" show "HEAD:scripts/repetition_carte_bbis_v1.py" > "$S" || arret "script de la répétition absent du commit" 2
[ "$(sha256sum < "$S" | cut -d' ' -f1)" = "$SCRIPT_SHA256" ] || arret "script de la répétition : empreinte ≠ SCRIPT_SHA256" 2
j "dépôt au commit $COMMIT (branche $BRANCHE_CODE) ; extraction partielle par les MOTIFS de la course ; aucune entrée de 7b ; script de la répétition à l'empreinte attendue"
# 3. paquets : pip verbeux, borné, durée écrite, code dédié
# >>> installation (extrait et joué par tests/test_repetition_bbis_v1.py)
installer() {  # $1 = python du venv ; $2 = exigences ; $3 = journal verbeux complet ; rend 0, 5 (au-delà de DELAI_PIP_S), 6 (échec)
    local c t0
    t0=$(date +%s)
    timeout -k 30 "$DELAI_PIP_S" "$1" -m pip install -v -r "$2" > "$3" 2>&1; c=$?
    DUREE_PIP=$(( $(date +%s) - t0 ))
    case "$c" in 0) return 0;; 124|137) return 5;; *) return 6;; esac; }
# <<< installation
python3 -m venv "$T/venv" || arret "environnement virtuel" 6
installer "$T/venv/bin/python" "$D/requirements-gpu.txt" "$T/pip-verbeux-complet.txt"; c=$?
{ head -c 2000000 "$T/pip-verbeux-complet.txt"; echo; echo "[…]"; tail -c 20000000 "$T/pip-verbeux-complet.txt"; } > "$X/pip-verbeux.txt" 2>/dev/null
j "installation des paquets : code $c, $DUREE_PIP s (délai $DELAI_PIP_S s ; journal verbeux : pip-verbeux.txt, début et fin)"
case "$c" in 0) ;; 5) arret "installation au-delà de $DELAI_PIP_S s (pip-verbeux.txt)" 5;; *) arret "installation en échec (pip-verbeux.txt)" 6;; esac
PY="$T/venv/bin/python"
"$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte" 2
"$PY" -m pip freeze --all > "$X/pip-freeze.txt" 2>/dev/null
cd "$D" || arret "dépôt" 2
# 4. essais de l'arbre de l'instance : commande et minimum de la course (lus au commit)
# >>> lecture-de-la-course (extrait et joué par tests/test_repetition_bbis_v1.py)
lire_course() {  # $1 = texte de scripts/amorce_bbis_v1.sh : définit compte_passes (texte même de la course) et MIN_COURSE
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
lire_course "$A_COURSE" || arret "compte des essais ou MIN_ESSAIS de la course illisible ou multiple" 2
PYTHONPATH=src "$PY" -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py --basetemp="$T/essais-tmp" > "$X/essais.txt" 2> "$X/essais.err"; c=$?
RES=$(tail -n 1 "$X/essais.txt")
j "essais de l'arbre de l'instance : code $c, ligne de compte : $RES ; minimum de la course : $MIN_COURSE"
[ "$c" = 0 ] || arret "essais en échec (essais.txt)" 7
NP=$(compte_passes "$RES")
[ "$NP" -ge "$MIN_COURSE" ] || arret "essais : $NP passés < MIN_ESSAIS $MIN_COURSE de la course (essais.txt, sautés nommés par -rs)" 7
[ -z "$(git status --porcelain --untracked-files=all -- src tests)" ] || arret "les essais ont écrit sous src ou tests" 2
# 5. carte : entrainer (deux familles, algorithmes déterministes), contrôle carte-processeur, durées
env CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONPATH=src "$PY" "$S" carte --sortie "$X/repetition-carte.json" \
    --actions "${ACTIONS_REPETITION:-640}" > "$X/carte.txt" 2> "$X/carte.err"; c=$?
j "carte : code $c ; $(tail -n 1 "$X/carte.txt")"
resume_carte "$PY" "$X/repetition-carte.json" > "$X/carte-resume.txt" 2>&1
j "carte : $(cat "$X/carte-resume.txt")"
case "$c" in 0) ;; 8) arret "carte : erreur d'apprentissage (repetition-carte.json, carte.err)" 8;;
    9) arret "carte : contrôle carte-processeur au-delà de 10⁻⁴ ou apprentissage non déterministe (repetition-carte.json)" 9;;
    2) arret "carte : garde (repetition-carte.json)" 2;; *) arret "carte : code $c (carte.err)" 4;; esac
# 6. traces et fin
j "FIN : répétition menée au bout"
pousser_traces "répétition menée au bout" || { j "traces non poussées"; fin_instance 4; }
fin_instance 0
