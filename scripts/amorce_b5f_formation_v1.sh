#!/usr/bin/env bash
# Amorce d'une instance de formation des familles d'adaptateurs jumeaux du barreau 5 (v1, 2026-11-20).
# Texte : le préenregistrement du barreau 5 (chemin passé dans PREREG), sections figées pour la formation ; devis du brouillon 3,
# § 3 et 4. Passée en base64 par scripts/lancer_b5f_formation_v1.sh (commande de création imprimée, jouée par la session de
# formation). Une instance, une marche (`controle_ia.barreau5_familles.formation_v1`, mode réel), sous $R/b5f-formation-v1.
# Ordre : 0. arguments (essai local : arrêt ici, code 0, rien d'écrit) ; minuterie de destruction par l'identifiant de
#   l'instance à ECHEANCE_ARRET_UTC_S + 15 minutes (R10 ; le quart d'heure du point 14 est le temps du versement) ;
#   1. machine (outils, clés par leur nom, carte A100, CUDA servie par le pilote au moins 13.0) ; 2. dépôt au commit COMMIT,
#   extraction partielle (code, essais du paquet, scripts de la chaîne, textes scellés et tâches cités ; jamais docs/notes/,
#   jamais diag/) ; branche de sortie absente du dépôt distant ; 3. paquets ; 4. essais du paquet (au moins MIN_ESSAIS
#   passés) ; 5. modèle au cache local ; 6. marche sous `timeout` jusqu'à ECHEANCE_ARRET_UTC_S (TERM au seul processus lancé,
#   jamais par motif), versement périodique des sorties scellées pendant la marche ; 7. versement de tout ce qui existe
#   (sorties, manifeste, résultats, journal) ; 8. fin : état « stopped » demandé ; la session vérifie le versement, puis
#   détruit par l'identifiant (lancer_b5f_formation_v1.sh detruire) ; la minuterie détruit sinon à l'échéance.
# La marche ne lit aucune activation et n'écrit aucun score (liste d'arrêt, point 5, gardé par son code) ; cette amorce ne
# lance rien d'autre qu'elle, les essais du paquet et la descente du modèle. Aucune valeur de clé n'est lue ni affichée :
# GH_TOKEN, HF_TOKEN et CONTAINER_API_KEY ne sont cités que par leur nom.
# Variables (--env) : INSTANCE_B5F, COMMIT, BRANCHE_CODE, PREREG, RUN_B5F, PRIX_USD_H, ECHEANCE_ARRET_UTC_S, GO_ID, DEPOT_URL,
#   GH_TOKEN, HF_TOKEN ; posées par le loueur : CONTAINER_ID, CONTAINER_API_KEY.
# Essai local (AMORCE_ESSAI_LOCAL=1) : contrôle des arguments seulement, sortie (code 0) avant tout réseau et toute écriture ;
#   hors essai, RACINE_AMORCE est refusée.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
R="${RACINE_AMORCE:-/root}"
[ "$ESSAI" = 1 ] || [ -z "${RACINE_AMORCE:-}" ] || { echo "B5F REFUS : RACINE_AMORCE en essai local seulement"; exit 2; }
T="$R/b5f-formation-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-b5f.txt"
API=https://console.vast.ai/api/v0
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
SEUIL=94000000
VERSEMENT_S=900
PERIODE_VERSEMENT_S=600
# essais de tests/test_barreau5_familles_*.py sur l'arbre extrait (essais du lanceur exclus : ils lisent la garde de calcul,
# hors de l'extraction) ; compte mesuré sur l'arbre de travail du développeur, à remesurer au commit de la course
MIN_ESSAIS=115
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
j() { mkdir -p "$X" 2> /dev/null; printf '%s B5F %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
# >>> arguments (extrait et joué par tests/test_amorce_b5f_formation_v1.py)
verifier_arguments() {  # 0 si conformes ; sinon motif sur la sortie, code 2
    local v
    for v in INSTANCE_B5F COMMIT BRANCHE_CODE PREREG RUN_B5F PRIX_USD_H ECHEANCE_ARRET_UTC_S GO_ID DEPOT_URL; do
        [ -n "${!v:-}" ] || { echo "B5F REFUS : variable $v absente"; return 2; }; done
    case "$INSTANCE_B5F" in [1-7]) ;; *) echo "B5F REFUS : INSTANCE_B5F hors de 1 à 7"; return 2;; esac
    case "$COMMIT" in *[!0-9a-f]*) echo "B5F REFUS : COMMIT illisible"; return 2;; esac
    [ "${#COMMIT}" = 40 ] || { echo "B5F REFUS : COMMIT de 40 caractères attendu"; return 2; }
    case "$BRANCHE_CODE" in *[!A-Za-z0-9._/-]*) echo "B5F REFUS : BRANCHE_CODE illisible"; return 2;; esac
    case "$PREREG" in prereg/*.md) ;; *) echo "B5F REFUS : PREREG illisible"; return 2;; esac
    case "$PREREG" in *[!A-Za-z0-9._/-]*|*..*) echo "B5F REFUS : PREREG illisible"; return 2;; esac
    case "$RUN_B5F" in [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-b5f-formation-"$INSTANCE_B5F") ;;
        *) echo "B5F REFUS : RUN_B5F illisible ou d'une autre instance"; return 2;; esac
    printf '%s' "$PRIX_USD_H" | LC_ALL=C grep -qxE '[0-9]+(\.[0-9]+)?' || { echo "B5F REFUS : PRIX_USD_H illisible"; return 2; }
    awk -v p="$PRIX_USD_H" 'BEGIN { exit !(p > 0 && p <= 1.30) }' || { echo "B5F REFUS : PRIX_USD_H hors de ]0 ; 1,30]"; return 2; }
    case "$ECHEANCE_ARRET_UTC_S" in *[!0-9]*) echo "B5F REFUS : ECHEANCE_ARRET_UTC_S illisible"; return 2;; esac
    printf '%s' "$GO_ID" | LC_ALL=C grep -qxE 'GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}' || { echo "B5F REFUS : GO_ID illisible"; return 2; }
    [ "$DEPOT_URL" = "$DEPOT_URL_OFFICIEL" ] || { echo "B5F REFUS : DEPOT_URL ≠ $DEPOT_URL_OFFICIEL (jamais la copie publique)"; return 2; }
    return 0; }
# <<< arguments
# >>> duree-de-la-marche (extrait et joué par tests/test_amorce_b5f_formation_v1.py)
duree_marche() {  # $1 = échéance d'arrêt (s UTC), $2 = maintenant (s UTC) : secondes laissées à la marche ; code 1 sous 60 s
    local d=$(( $1 - $2 ))
    [ "$d" -ge 60 ] || return 1
    echo "$d"; }
# <<< duree-de-la-marche
# >>> fin-instance (extrait et joué par tests/test_amorce_b5f_formation_v1.py)
fin_instance() {  # état « stopped » demandé par l'identifiant de l'instance ; la session détruit après le versement (R10)
    local c
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
    j "fin, code $1 ; état « stopped » demandé : HTTP $c ; la session vérifie le versement puis détruit par l'identifiant"
    [ "${B5F_SANS_ATTENTE:-0}" = 1 ] || sleep infinity
    exit "$1"; }
# <<< fin-instance
# >>> minuterie (extrait et joué par tests/test_amorce_b5f_formation_v1.py ; une destruction n'est jamais jugée par un code)
minuterie() {  # $1 = instant de destruction (s UTC) : DELETE par l'identifiant de l'instance, refait tant que ce processus vit
    local n=0 c
    while [ "$(date +%s)" -lt "$1" ]; do sleep "${B5F_PAS_MINUTERIE:-30}"; done
    j "MINUTERIE : échéance atteinte : destruction de l'instance ${CONTAINER_ID:-} par son identifiant (DELETE)"
    while :; do n=$((n + 1))
        c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
        j "MINUTERIE : DELETE, essai $n : HTTP $c (seule l'absence de l'identifiant dans la liste prouve la destruction)"
        sleep "${B5F_PAS_MINUTERIE:-60}"; done; }
# <<< minuterie
# >>> versement (extrait et joué par tests/test_amorce_b5f_formation_v1.py)
# Les sorties sont poussées sur la branche de sortie par des commits faits à part (index séparé, parent = dernier commit
# poussé, au départ COMMIT) : la tête et l'arbre de travail de la marche ne bougent jamais. Rien n'est supprimé.
fichiers_scelles() {  # chemins relatifs à $D sous les dossiers donnés : fichiers dont le compagnon .sha256 est conforme, et ce compagnon
    local f s
    (cd "$D" && for f in $(find "$@" -type f ! -name '*.sha256' 2> /dev/null | LC_ALL=C sort); do
        [ -f "$f.sha256" ] || continue
        s=$(sha256sum < "$f" | cut -c1-64)
        [ "$(cut -c1-64 < "$f.sha256")" = "$s" ] && printf '%s\n%s\n' "$f" "$f.sha256"
    done); }
tous_les_fichiers() { (cd "$D" && find "$@" -type f 2> /dev/null | LC_ALL=C sort); }
verser() {  # $1 = message ; puis chemins relatifs à $D ; 0 si poussé (ou rien de neuf), 1 sinon
    local m="$1" ix="$T/index-sortie" parent arbre c n f a=()
    shift
    for f in "$@"; do [ -e "$D/$f" ] && a+=("$f"); done
    [ "${#a[@]}" -gt 0 ] || return 0
    for f in "${a[@]}"; do [ "$(stat -c %s "$D/$f")" -le "$SEUIL" ] || { j "fichier de plus de $SEUIL octets, non poussé, gardé sur le disque : $f (nœud)"; return 1; }; done
    parent=$(cat "$T/parent-sortie") || return 1
    rm -f "$ix"
    GIT_INDEX_FILE="$ix" git -C "$D" read-tree "$parent" || return 1
    GIT_INDEX_FILE="$ix" git -C "$D" add --sparse -f -- "${a[@]}" || return 1
    arbre=$(GIT_INDEX_FILE="$ix" git -C "$D" write-tree) || return 1
    [ "$arbre" != "$(git -C "$D" rev-parse "$parent^{tree}")" ] || return 0
    c=$(git -C "$D" commit-tree "$arbre" -p "$parent" -m "$m") || return 1
    for n in 1 2 3; do
        git -C "$D" push -q origin "$c:refs/heads/$BR" && { echo "$c" > "$T/parent-sortie"; j "poussé : $c « $m »"; return 0; }
        sleep $((10 * n)); done
    return 1; }
# <<< versement
# 0. arguments, minuterie
verifier_arguments || exit 2
BR="donnees/barreau5-familles-jumelles-v1-formation-instance-$INSTANCE_B5F"
if [ "$ESSAI" = 1 ]; then echo "B5F ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "B5F REFUS : identifiant de l'instance illisible"; exit 2;; esac
[ -n "${CONTAINER_API_KEY:-}" ] || { echo "B5F REFUS : CONTAINER_API_KEY absente (par le nom) : la minuterie ne détruirait rien"; exit 2; }
DUREE=$(duree_marche "$ECHEANCE_ARRET_UTC_S" "$(date +%s)") || { echo "B5F REFUS : échéance d'arrêt passée ou trop proche"; exit 2; }
[ ! -e "$T" ] || { echo "B5F REFUS : $T existe déjà (R12)"; exit 2; }
mkdir -p "$X" || exit 2
minuterie $(( ECHEANCE_ARRET_UTC_S + VERSEMENT_S )) < /dev/null & j "minuterie lancée (PID $!, destruction à $(date -u -d "@$(( ECHEANCE_ARRET_UTC_S + VERSEMENT_S ))" +%FT%TZ))"
j "amorce v1 : empreinte $(sha256sum < "$0" 2> /dev/null | cut -c1-64) ; instance $INSTANCE_B5F, run $RUN_B5F, accord $GO_ID"
arret() { j "ARRET : $1"
    [ -f "$T/parent-sortie" ] && verser "barreau 5, formation, instance $INSTANCE_B5F : traces de l'arrêt" traces-b5f || true
    fin_instance "${2:-4}"; }
# 1. machine
for o in git curl python3 sha256sum awk sed grep stat find sort timeout; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
[ -n "${HF_TOKEN:-}" ] || arret "HF_TOKEN absent (par le nom)" 2
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible" 2
grep -q 'A100' "$X/nvidia-smi.txt" || arret "carte autre qu'une A100 : $(head -n 1 "$X/nvidia-smi.txt")" 2
nvidia-smi > "$X/nvidia-smi-entete.txt" 2>&1 || arret "carte invisible (en-tête)" 2
V=$(sed -n 's/^.*CUDA Version: *\([0-9][0-9]*\)\.[0-9][0-9]*.*$/\1/p' "$X/nvidia-smi-entete.txt")
[ "$(printf '%s' "$V" | grep -c '^')" = 1 ] && [ "$V" -ge 13 ] 2> /dev/null || arret "CUDA servie par le pilote illisible ou < 13.0" 2
# 2. dépôt au commit COMMIT, extraction partielle
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_CODE" "$DEPOT_URL" "$D" || arret "clonage" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (barreau 5)"; git -C "$D" config user.email "instance-calcul@invalid"
# >>> motifs (lus par tests/test_amorce_b5f_formation_v1.py)
MOTIFS='/*
!/*/
/src/
/tests/conftest.py
/tests/test_barreau5_familles_*
/scripts/amorce_b5f_formation_v1.sh*
/scripts/lancer_b5f_formation_v1.sh*
/prereg/T0.6-organismes-config-7b-v1.json*
/prereg/P3-consignes-v1.md*
/prereg/barreau5-sabotage-ou-empreinte-*
/prereg/gabarit-preregistrement-v1.md*
/registres/barreau5-familles-jumelles-v1.md*
/donnees/20261007-082440-t05-extraction/taches-entrainement.json*
/donnees/20261007-082440-t05-extraction/taches-evaluation.json*
/docs/sources/invites-2606.08892-v1/'
# <<< motifs
git -C "$D" sparse-checkout init --no-cone && printf '%s\n' "$MOTIFS" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$COMMIT" || arret "commit $COMMIT introuvable sur $BRANCHE_CODE" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
[ -f "$D/$PREREG" ] && [ -f "$D/registres/barreau5-familles-jumelles-v1.md" ] || arret "texte ou registre propre absent du commit" 2
[ ! -e "$D/docs/notes" ] && [ ! -e "$D/diag" ] || arret "docs/notes ou diag extraits : arrêt" 2
git -C "$D" ls-remote --exit-code origin "refs/heads/$BR" > /dev/null 2>&1; [ $? = 2 ] || arret "branche de sortie $BR présente sur le dépôt distant (R12) ou dépôt injoignable" 2
echo "$COMMIT" > "$T/parent-sortie"
cp_traces() { mkdir -p "$D/traces-b5f/journal" && cp -f "$X"/* "$D/traces-b5f/journal/" 2> /dev/null; }
arret() { j "ARRET : $1"; cp_traces; verser "barreau 5, formation, instance $INSTANCE_B5F : traces de l'arrêt" $(tous_les_fichiers traces-b5f/journal) || true
    fin_instance "${2:-4}"; }
j "dépôt au commit $COMMIT (branche $BRANCHE_CODE) ; branche de sortie $BR libre"
# 3. paquets
python3 -m venv "$T/venv" && timeout -k 10 3600 "$T/venv/bin/pip" install -q -r "$D/requirements-gpu.txt" > "$X/pip.txt" 2>&1 || arret "installation des paquets" 2
PY="$T/venv/bin/python"
"$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte" 2
cd "$D" || arret "dépôt" 2
# 4. essais du paquet
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no tests/test_barreau5_familles_*.py --basetemp="$T/essais-tmp" > "$X/essais.txt" 2> "$X/essais.err"; c=$?
RES=$(tail -n 1 "$X/essais.txt"); NP=$(printf '%s\n' "$RES" | grep -oE '[0-9]+ passed' | grep -oE '[0-9]+' | head -n 1)
j "essais du paquet : code $c, ligne de compte : $RES"
[ "$c" = 0 ] && [ "${NP:-0}" -ge "$MIN_ESSAIS" ] || arret "essais du paquet en échec ou moins de $MIN_ESSAIS passés" 2
[ -z "$(git status --porcelain --untracked-files=all -- src tests prereg registres)" ] || arret "les essais ont écrit dans le dépôt" 2
# 5. modèle au cache local (révision de la configuration scellée)
PYTHONPATH=src timeout -k 10 3600 "$PY" -c 'import json, sys
from controle_ia.harnais.modeles import precharger_modele
a = json.load(open(sys.argv[1], encoding="utf-8"))["agent"]
print(precharger_modele(a["modele"], a["revision"]))' prereg/T0.6-organismes-config-7b-v1.json > "$X/modele.txt" 2>&1 || arret "descente du modèle" 2
j "modèle au cache local"
# 6. marche, sous timeout jusqu'à l'échéance d'arrêt ; versement des sorties scellées toutes les PERIODE_VERSEMENT_S secondes
DUREE=$(duree_marche "$ECHEANCE_ARRET_UTC_S" "$(date +%s)") || arret "échéance d'arrêt atteinte avant la marche" 3
[ -z "$(git status --porcelain --untracked-files=all)" ] || arret "arbre non propre avant la marche" 2
j "marche : début (run $RUN_B5F, $DUREE s au plus)"
env HF_HUB_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONPATH=src timeout --signal=TERM --kill-after=120 "$DUREE" \
    "$PY" -m controle_ia.barreau5_familles.formation_v1 --instance "$INSTANCE_B5F" --prix-usd-h "$PRIX_USD_H" \
    --go-id "$GO_ID" --run-id "$RUN_B5F" --prereg "$PREREG" > "$X/marche.txt" 2> "$X/marche.err" &
PID=$!
j "marche lancée (PID $PID ; arrêt par ce seul processus, R10)"
while kill -0 "$PID" 2> /dev/null; do
    sleep "$PERIODE_VERSEMENT_S"
    verser "barreau 5, formation, instance $INSTANCE_B5F : sorties scellées" $(fichiers_scelles "donnees/$RUN_B5F" "runs/$RUN_B5F" "diag/$RUN_B5F") \
        || j "versement périodique en échec : refait au prochain pas et à la fin"
done
wait "$PID"; c=$?
j "marche : code $c"
# 7. versement de tout ce qui existe (règle « récupérer ce qui est récupérable ») ; rien n'est supprimé
cp_traces
verser "barreau 5, formation, instance $INSTANCE_B5F : sorties (code $c)" $(tous_les_fichiers "donnees/$RUN_B5F" "runs/$RUN_B5F" "diag/$RUN_B5F") \
    || arret "versement final en échec : instance arrêtée, disque gardé jusqu'à la minuterie ; versement à reprendre (nœud)" 4
cp_traces
verser "barreau 5, formation, instance $INSTANCE_B5F : journal de fin" $(tous_les_fichiers traces-b5f/journal) || j "journal de fin non poussé"
# 8. fin
case "$c" in
    0) j "FIN : marche menée au bout ; tête de sortie $(cat "$T/parent-sortie") ; SORTIES-FORMATION-B5F à inscrire par la session"; fin_instance 0;;
    124) arret "échéance d'arrêt atteinte (cumul plus un quart d'heure à la coupure) : marche arrêtée par TERM, sorties versées" 3;;
    *) arret "marche : arrêt écrit, code $c (marche.err ; diag/$RUN_B5F/arret.json)" 4;;
esac
