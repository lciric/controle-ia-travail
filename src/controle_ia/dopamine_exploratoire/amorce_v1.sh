#!/usr/bin/env bash
# Amorce d'une machine A100 du loueur, bras « papier dopamine », mode EXPLORATOIRE (GO-2026-11-21-44), v1.
# Passée en base64 par `controle_ia.dopamine_exploratoire.lanceur_v1` (commande imprimée, jouée par la session de course).
# Ordre :
#   0. arguments (essai local : arrêt ici, code 0, rien d'écrit) ; minuterie lancée par l'identifiant de l'instance (R10), à
#      DESTRUCTION_UTC_S (6 h 30 après la commande, devis de l'étape 1, § 5) : elle DÉTRUIT l'instance seulement si le
#      versement final est prouvé (témoin), sinon elle l'ARRÊTE (disque gardé) et écrit un signal pour la mère (R-3661) ;
#   1. machine (outils, clés reçues comme valeurs, carte A100, CUDA du pilote ≥ 13) ;
#   2. dépôt au commit COMMIT, extraction partielle (code et essais du paquet, jamais docs/notes, diag, runs, brouillons) ;
#      la course RUN_ID ne doit pas exister sur la branche de sortie (R12) ;
#   3. paquets (environnement principal ; environnement vLLM à part pour l'étape 1) ; 4. essais du paquet ;
#   5. modèle et jeu au disque local ; 6. marche (génération, puis noyau et blocs) sous `timeout` jusqu'à un quart d'heure
#      avant la destruction ; plus aucun bloc lancé après FIN_LANCEMENTS_UTC_S (5 h 30) ; versement périodique ;
#   7. versement de ce qui est permis, inventaire de tout ce qui existe (noms, tailles, empreintes), poussé puis relu :
#      preuve ; 8. fin : état « stopped » demandé ; la session vérifie le versement puis détruit par l'identifiant.
# Rien n'est supprimé. Les trajectoires d'états (donnees/RUN/etats/couche-*/lot-*.npy, plusieurs Go) ne sortent pas :
# elles restent sur le disque, inscrites à l'inventaire, et se recalculent des générations versées et du modèle.
# Aucune valeur de clé n'est lue ni affichée : GH_TOKEN, HF_TOKEN, CONTAINER_API_KEY ne sont cités que par leur nom.
# Variables (--env) : ETAPE (1), COMMIT, RUN_ID, PRIX_USD_H, FIN_LANCEMENTS_UTC_S, DESTRUCTION_UTC_S, GO_ID, DEPOT_URL,
#   CONTEXTES et LISTE_HONNETES (fichiers scellés du dépôt pour le bloc de relecture forcée, « - » sinon), GH_TOKEN,
#   HF_TOKEN ; posées par le loueur : CONTAINER_ID, CONTAINER_API_KEY.
# Essai local (AMORCE_ESSAI_LOCAL=1) : contrôle des arguments seulement. Les fonctions balisées « # >>> nom » sont extraites
# et jouées par tests/test_dopamine_exploratoire_amorce_v1.py.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
R=/root
T="$R/dopamine-exploratoire-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal.txt"
API=https://console.vast.ai/api/v0
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
BR=donnees/dopamine-exploratoire-v1
SEUIL=94000000
VERSEMENT_S=900
PERIODE_VERSEMENT_S=600
PAS_ATTENTE_S=5
VERSION_VLLM=0.11.0
MODELE=meta-llama/Llama-3.1-8B-Instruct
MIN_ESSAIS=124
TEMOIN="$T/versement-final-prouve"
SIGNAL="$X/signal-pour-la-mere.txt"
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
j() { mkdir -p "$X" 2> /dev/null; printf '%s DOPAMINE %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
# >>> arguments
verifier_arguments() {  # 0 si conformes ; sinon motif sur la sortie, code 2
    local v
    for v in ETAPE COMMIT RUN_ID PRIX_USD_H FIN_LANCEMENTS_UTC_S DESTRUCTION_UTC_S GO_ID DEPOT_URL CONTEXTES LISTE_HONNETES; do
        [ -n "${!v:-}" ] || { echo "DOPAMINE REFUS : variable $v absente"; return 2; }; done
    case "$ETAPE" in 1) ;; *) echo "DOPAMINE REFUS : ETAPE : 1"; return 2;; esac
    case "$COMMIT" in *[!0-9a-f]*) echo "DOPAMINE REFUS : COMMIT illisible"; return 2;; esac
    [ "${#COMMIT}" = 40 ] || { echo "DOPAMINE REFUS : COMMIT de 40 caractères attendu"; return 2; }
    printf '%s' "$RUN_ID" | LC_ALL=C grep -qxE "[0-9]{8}-[0-9]{6}-[a-z0-9-]*exploratoire[a-z0-9-]*-etape-$ETAPE" \
        || { echo "DOPAMINE REFUS : RUN_ID illisible, sans « exploratoire » ou d'une autre étape"; return 2; }
    printf '%s' "$PRIX_USD_H" | LC_ALL=C grep -qxE '[0-9]+(\.[0-9]+)?' || { echo "DOPAMINE REFUS : PRIX_USD_H illisible"; return 2; }
    awk -v p="$PRIX_USD_H" 'BEGIN { exit !(p > 0 && p <= 1.38) }' || { echo "DOPAMINE REFUS : PRIX_USD_H hors de ]0 ; 1,38]"; return 2; }
    case "$FIN_LANCEMENTS_UTC_S" in *[!0-9]*) echo "DOPAMINE REFUS : FIN_LANCEMENTS_UTC_S illisible"; return 2;; esac
    case "$DESTRUCTION_UTC_S" in *[!0-9]*) echo "DOPAMINE REFUS : DESTRUCTION_UTC_S illisible"; return 2;; esac
    [ "$FIN_LANCEMENTS_UTC_S" -lt "$DESTRUCTION_UTC_S" ] || { echo "DOPAMINE REFUS : fin des lancements après la destruction"; return 2; }
    printf '%s' "$GO_ID" | LC_ALL=C grep -qxE 'GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}' || { echo "DOPAMINE REFUS : GO_ID illisible"; return 2; }
    [ "$DEPOT_URL" = "$DEPOT_URL_OFFICIEL" ] || { echo "DOPAMINE REFUS : DEPOT_URL ≠ $DEPOT_URL_OFFICIEL (jamais la copie publique)"; return 2; }
    for v in CONTEXTES LISTE_HONNETES; do
        [ "${!v}" = - ] && continue
        case "${!v}" in *[!A-Za-z0-9._/-]*|*..*|/*) echo "DOPAMINE REFUS : $v illisible"; return 2;; esac; done
    { [ "$CONTEXTES" = - ] && [ "$LISTE_HONNETES" = - ]; } || { [ "$CONTEXTES" != - ] && [ "$LISTE_HONNETES" != - ]; } \
        || { echo "DOPAMINE REFUS : CONTEXTES et LISTE_HONNETES : les deux ou aucun"; return 2; }
    return 0; }
# <<< arguments
# >>> duree
duree_marche() {  # $1 = échéance (s UTC), $2 = maintenant : secondes laissées ; code 1 sous 60 s
    local d=$(( $1 - $2 ))
    [ "$d" -ge 60 ] || return 1
    echo "$d"; }
# <<< duree
# >>> minuterie
minuterie() {  # $1 = échéance (s UTC). Versement prouvé (témoin) → DELETE par l'identifiant ; sinon « stopped » et signal
    local n=0 c
    j "minuterie : échéance $1"
    while [ "$(date +%s)" -lt "$1" ]; do sleep "${DOPAMINE_PAS_MINUTERIE:-30}"; done
    if [ -s "$TEMOIN" ]; then
        j "MINUTERIE : versement final prouvé (commit $(cat "$TEMOIN")) : destruction de l'instance ${CONTAINER_ID:-} par son identifiant"
        while :; do n=$((n + 1))
            c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
                "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
            j "MINUTERIE : DELETE, essai $n : HTTP $c (seule l'absence dans la liste prouve la destruction)"
            [ "$n" -lt "${DOPAMINE_ESSAIS_MINUTERIE:-1000000}" ] || return 0
            sleep "${DOPAMINE_PAS_MINUTERIE:-60}"; done
    fi
    printf '%s\n' "$(date -u +%FT%TZ) SIGNAL POUR LA MÈRE : instance ${CONTAINER_ID:-}, course ${RUN_ID:-} : versement final non prouvé à l'échéance ; instance arrêtée, NON détruite, disque gardé (R-3661)" >> "$SIGNAL"
    while :; do n=$((n + 1))
        c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
        j "MINUTERIE : « stopped », essai $n : HTTP $c (aucune destruction sans preuve du versement)"
        [ "$n" -lt "${DOPAMINE_ESSAIS_MINUTERIE:-1000000}" ] || return 0
        sleep "${DOPAMINE_PAS_MINUTERIE:-60}"; done; }
# <<< minuterie
# >>> versement
permis() {  # 0 si le chemin (relatif à $D) peut sortir de l'instance
    local f="$1" r="$RUN_ID" e
    for e in "^donnees/$r/(generations|notation|episodes)/lot-[0-9]{5}\\.jsonl(\\.sha256)?\$" \
             "^donnees/$r/etats/couche-[0-9]{2}/lot-[0-9]{5}\\.index\\.json(\\.sha256)?\$" \
             "^donnees/$r/etats/confiance-jeton/lot-[0-9]{5}\\.json(\\.sha256)?\$" \
             "^donnees/$r/relecture-forcee/couche-[0-9]{2}\\.(npy|index\\.json)(\\.sha256)?\$" \
             "^donnees/$r/sondes/poids/[A-Za-z0-9.-]+\\.npz(\\.sha256)?\$" \
             "^donnees/$r/invite-question-0\\.txt(\\.sha256)?\$" \
             "^donnees/$r/etats-s0/couche-[0-9]{2}\\.(npy|ids\\.json)(\\.sha256)?\$" \
             "^donnees/$r/sondes/[A-Za-z0-9.-]+\\.json(\\.sha256)?\$" \
             "^runs/$r/manifeste\\.json(\\.sha256)?\$" "^diag/$r/[A-Za-z0-9.-]+\\.json(\\.sha256)?\$" \
             "^traces-dopamine/journal/[A-Za-z0-9._-]+\$" "^traces-dopamine/inventaire-final\\.json(\\.sha256)?\$"; do
        [[ "$f" =~ $e ]] && return 0; done
    return 1; }
tous_les_fichiers() { (cd "$D" && find "$@" -type f ! -name '*.partiel' ! -name '*.partiel.abandon-*' 2> /dev/null | LC_ALL=C sort); }
fichiers_scelles() {  # fichiers sous les dossiers donnés dont le compagnon .sha256 est conforme, et ce compagnon
    local f s
    (cd "$D" && for f in $(find "$@" -type f ! -name '*.sha256' 2> /dev/null | LC_ALL=C sort); do
        [ -f "$f.sha256" ] || continue
        s=$(sha256sum < "$f" | cut -c1-64)
        [ "$(cut -c1-64 < "$f.sha256")" = "$s" ] && printf '%s\n%s\n' "$f" "$f.sha256"
    done); }
parent_courant() {  # tête distante de la branche de sortie (rapatriée), ou COMMIT si la branche n'existe pas encore
    local t
    t=$(git -C "$D" ls-remote origin "refs/heads/$BR" | cut -f1) || return 1
    if [ -n "$t" ]; then git -C "$D" fetch -q --filter=blob:none origin "refs/heads/$BR" > /dev/null 2>&1 || return 1; echo "$t"
    else echo "$COMMIT"; fi; }
verser() {  # $1 = message ; puis chemins relatifs à $D. Pousse ceux qui existent, sont permis et ne dépassent pas SEUIL,
    # par un commit fait à part (index neuf, parent = tête distante) : la tête de travail ne bouge jamais. Rien n'est
    # supprimé. Code 0 si tout ce qui est permis est poussé (ou rien de neuf), 1 sinon.
    local m="$1" ix parent arbre c n f a=() ecart=0
    shift
    for f in "$@"; do
        [ -e "$D/$f" ] || continue
        permis "$f" || continue
        if [ "$(stat -c %s "$D/$f")" -gt "$SEUIL" ]; then
            j "plus de $SEUIL octets, non poussé, gardé sur le disque : $f (nœud)"; ecart=1; continue; fi
        a+=("$f"); done
    [ "${#a[@]}" -gt 0 ] || return "$ecart"
    for n in 1 2 3 4 5; do
        parent=$(parent_courant) || { sleep $((5 * n)); continue; }
        ix="$T/index-sortie-$(date +%s%N)-$n"
        GIT_INDEX_FILE="$ix" git -C "$D" read-tree "$parent" || return 1
        GIT_INDEX_FILE="$ix" git -C "$D" add --sparse -f -- "${a[@]}" || return 1
        arbre=$(GIT_INDEX_FILE="$ix" git -C "$D" write-tree) || return 1
        if [ "$arbre" = "$(git -C "$D" rev-parse "$parent^{tree}")" ]; then echo "$parent" > "$T/parent-sortie"; return "$ecart"; fi
        c=$(git -C "$D" commit-tree "$arbre" -p "$parent" -m "$m") || return 1
        if git -C "$D" push -q origin "$c:refs/heads/$BR" 2> /dev/null; then
            echo "$c" > "$T/parent-sortie"; j "poussé : $c « $m »"; return "$ecart"; fi
        j "poussée refusée (essai $n ; une autre course a pu pousser) : reprise sur la tête distante"
        sleep $((5 * n)); done
    return 1; }
# <<< versement
# >>> preuve
prouver_versement() {  # inventaire de tout ce qui existe (noms, tailles, empreintes, versé ou non) ; poussé ; relu : chaque
    # fichier permis est à la tête distante, à sa taille et à son empreinte. Écrit le témoin seulement si tout tient.
    local inv="traces-dopamine/inventaire-final.json" tsv="$T/inventaire-final.tsv" f o s p tete premier=1
    [ -d "$D/.git" ] || return 1
    mkdir -p "$D/traces-dopamine" || return 1
    : > "$tsv" || return 1
    for f in $(tous_les_fichiers "donnees/$RUN_ID" "runs/$RUN_ID" "diag/$RUN_ID" traces-dopamine/journal); do
        case "$f" in *[!A-Za-z0-9._/-]*) j "preuve : nom illisible : $f"; return 1;; esac
        p=false; permis "$f" && [ "$(stat -c %s "$D/$f")" -le "$SEUIL" ] && p=true
        printf '%s\t%s\t%s\t%s\n' "$f" "$(stat -c %s "$D/$f")" "$(sha256sum < "$D/$f" | cut -c1-64)" "$p" >> "$tsv" || return 1
    done
    [ -s "$tsv" ] || { j "preuve : rien à inventorier"; return 1; }
    { printf '{"run_id": "%s", "fichiers": [' "$RUN_ID"
      while IFS="$(printf '\t')" read -r f o s p; do
          [ "$premier" = 1 ] || printf ', '
          premier=0
          printf '{"chemin": "%s", "octets": %s, "sha256": "%s", "verse": %s}' "$f" "$o" "$s" "$p"
      done < "$tsv"
      printf ']}\n'; } > "$D/$inv" || return 1
    printf '%s  %s\n' "$(sha256sum < "$D/$inv" | cut -c1-64)" "inventaire-final.json" > "$D/$inv.sha256" || return 1
    verser "dopamine exploratoire, course $RUN_ID : inventaire final" $(awk -F'\t' '$4 == "true" {print $1}' "$tsv") \
        "$inv" "$inv.sha256" || return 1
    tete=$(git -C "$D" ls-remote origin "refs/heads/$BR" | cut -f1)
    [ -n "$tete" ] || { j "preuve : branche distante absente"; return 1; }
    git -C "$D" fetch -q origin "refs/heads/$BR" > /dev/null 2>&1 || { j "preuve : rapatriement impossible"; return 1; }
    while IFS="$(printf '\t')" read -r f o s p; do
        [ "$p" = true ] || continue
        [ "$(git -C "$D" cat-file -s "$tete:$f" 2> /dev/null)" = "$o" ] \
            && [ "$(git -C "$D" cat-file blob "$tete:$f" 2> /dev/null | sha256sum | cut -c1-64)" = "$s" ] \
            || { j "preuve : $f absent de $tete ou différent"; return 1; }
    done < "$tsv"
    echo "$tete" > "$TEMOIN"
    j "versement final prouvé au commit $tete de $BR ($(awk -F'\t' '$4 == "true"' "$tsv" | wc -l) fichiers versés, $(awk -F'\t' '$4 != "true"' "$tsv" | wc -l) inscrits seulement)"
    return 0; }
# <<< preuve
# >>> attente
attendre_la_marche() {  # $1 = PID : rend la main au plus PAS_ATTENTE_S secondes après sa fin ; versement périodique
    local n=0
    while [ -d "/proc/$1" ]; do
        sleep "$PAS_ATTENTE_S"; n=$((n + PAS_ATTENTE_S))
        [ "$n" -ge "$PERIODE_VERSEMENT_S" ] || continue
        n=0
        verser "dopamine exploratoire, course $RUN_ID : sorties scellées" \
            $(fichiers_scelles "donnees/$RUN_ID" "runs/$RUN_ID" "diag/$RUN_ID") || j "versement périodique incomplet"
    done; }
# <<< attente
fin_instance() {  # état « stopped » demandé par l'identifiant ; la session vérifie le versement puis détruit (R10)
    local c
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2> /dev/null) || c=000
    j "fin, code $1 ; « stopped » demandé : HTTP $c"
    sleep infinity
    exit "$1"; }
# 0. arguments, minuterie
verifier_arguments || exit 2
if [ "$ESSAI" = 1 ]; then echo "DOPAMINE ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie, aucun dossier"; exit 0; fi
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "DOPAMINE REFUS : identifiant de l'instance illisible"; exit 2;; esac
[ -n "${CONTAINER_API_KEY:-}" ] || { echo "DOPAMINE REFUS : CONTAINER_API_KEY absente : la minuterie n'arrêterait rien"; exit 2; }
FIN_MARCHE=$(( DESTRUCTION_UTC_S - VERSEMENT_S ))
duree_marche "$FIN_MARCHE" "$(date +%s)" > /dev/null || { echo "DOPAMINE REFUS : destruction passée ou trop proche"; exit 2; }
[ ! -e "$T" ] || { echo "DOPAMINE REFUS : $T existe déjà (R12)"; exit 2; }
mkdir -p "$X" || exit 2
minuterie "$DESTRUCTION_UTC_S" < /dev/null &
j "minuterie lancée (PID $!) ; amorce $(sha256sum < "$0" 2> /dev/null | cut -c1-64) ; étape $ETAPE, course $RUN_ID, accord $GO_ID ; fin des lancements $FIN_LANCEMENTS_UTC_S, destruction $DESTRUCTION_UTC_S"
cp_traces() { mkdir -p "$D/traces-dopamine/journal" && cp -f "$X"/* "$D/traces-dopamine/journal/" 2> /dev/null; }
terminer() {  # $1 = code, $2 = motif
    local code="$1"
    j "$2"
    if [ -d "$D/.git" ]; then
        cp_traces
        verser "dopamine exploratoire, course $RUN_ID : sorties et traces (code $code)" \
            $(tous_les_fichiers "donnees/$RUN_ID" "runs/$RUN_ID" "diag/$RUN_ID" traces-dopamine/journal) \
            || j "versement final incomplet (nœud)"
        prouver_versement || { j "versement final NON PROUVÉ : la minuterie arrêtera l'instance sans la détruire (nœud)"; [ "$code" != 0 ] || code=5; }
    else
        j "aucun dépôt cloné : rien à verser (nœud)"; [ "$code" != 0 ] || code=5
    fi
    fin_instance "$code"; }
arret() { terminer "${2:-4}" "ARRET : $1"; }
# 1. machine
for o in git curl python3 sha256sum awk sed grep stat find sort timeout; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ -n "${GH_TOKEN:-}" ] && [ -n "${HF_TOKEN:-}" ] || arret "GH_TOKEN ou HF_TOKEN absent (par le nom)" 2
case "${GH_TOKEN}${HF_TOKEN}" in *'$'*) arret "un nom de variable reçu à la place d'une valeur de clé" 2;; esac
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible" 2
grep -q 'A100' "$X/nvidia-smi.txt" || arret "carte autre qu'une A100" 2
V=$(nvidia-smi | sed -n 's/^.*CUDA Version: *\([0-9][0-9]*\)\.[0-9][0-9]*.*$/\1/p')
[ "${V:-0}" -ge 13 ] 2> /dev/null || arret "CUDA servie par le pilote < 13.0" 2
# 2. dépôt
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$D" || arret "clonage" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (dopamine exploratoire)"; git -C "$D" config user.email "instance-calcul@invalid"
MOTIFS='/requirements-gpu.txt
/requirements-cpu.txt
/requirements-donnees.txt
/pyproject.toml
/.gitignore
/.gitattributes
/src/
/tests/conftest.py
/tests/test_dopamine_exploratoire_*
/.claude/hooks/garde_calcul.py'
P_EP=""; [ "$CONTEXTES" != - ] && P_EP=$(printf '/%s\n/%s.sha256\n/%s\n/%s.sha256' "$CONTEXTES" "$CONTEXTES" "$LISTE_HONNETES" "$LISTE_HONNETES")
git -C "$D" sparse-checkout init --no-cone && printf '%s\n%s\n' "$MOTIFS" "$P_EP" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$COMMIT" || arret "commit $COMMIT introuvable" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
for d in docs/notes diag runs brouillons; do [ ! -e "$D/$d" ] || arret "$d extrait : arrêt" 2; done
if [ "$CONTEXTES" != - ]; then
    for f in "$CONTEXTES" "$LISTE_HONNETES"; do
        [ -f "$D/$f" ] && [ "$(sha256sum < "$D/$f" | cut -c1-64)" = "$(cut -c1-64 < "$D/$f.sha256")" ] || arret "$f absent ou différent de son empreinte" 2; done
fi
P=$(parent_courant) || arret "branche de sortie illisible" 2
[ -z "$(git -C "$D" ls-tree -d "$P" "donnees/$RUN_ID" 2> /dev/null)" ] || arret "course $RUN_ID déjà présente sur $BR (R12)" 2
j "dépôt au commit $COMMIT ; branche de sortie $BR (parent $P)"
# 3. paquets
python3 -m venv "$T/venv" && timeout 3600 "$T/venv/bin/pip" install -q -r "$D/requirements-gpu.txt" > "$X/pip.txt" 2>&1 || arret "installation des paquets" 2
PY="$T/venv/bin/python"
"$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte" 2
if true; then
    python3 -m venv "$T/venv-vllm" && timeout 3600 "$T/venv-vllm/bin/pip" install -q "vllm==$VERSION_VLLM" scipy > "$X/pip-vllm.txt" 2>&1 || arret "installation de vLLM $VERSION_VLLM" 2
fi
cd "$D" || arret "dépôt" 2
# 4. essais du paquet
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no tests/test_dopamine_exploratoire_*.py --basetemp="$T/essais-tmp" > "$X/essais.txt" 2>&1; c=$?
NP=$(tail -n 1 "$X/essais.txt" | grep -oE '[0-9]+ passed' | grep -oE '[0-9]+' | head -n 1)
j "essais du paquet : code $c, $(tail -n 1 "$X/essais.txt")"
[ "$c" = 0 ] && [ "${NP:-0}" -ge "$MIN_ESSAIS" ] || arret "essais en échec ou moins de $MIN_ESSAIS passés" 2
[ -z "$(git status --porcelain --untracked-files=all)" ] || arret "les essais ont écrit dans le dépôt" 2
# 5. modèle et jeu (clé Hugging Face lue par la bibliothèque, par son nom)
timeout 3600 "$PY" - "$T/modele" "$T/math500" "$MODELE" > "$X/descente.txt" 2>&1 <<'EOF' || arret "descente du modèle ou du jeu" 2
import sys
from huggingface_hub import HfApi, hf_hub_download, snapshot_download
modele, jeu, nom = sys.argv[1], sys.argv[2], sys.argv[3]
info = HfApi().model_info(nom)
snapshot_download(nom, revision=info.sha, local_dir=modele, allow_patterns=["*.json", "*.safetensors", "tokenizer*"])
hf_hub_download("HuggingFaceH4/MATH-500", "test.jsonl", repo_type="dataset", local_dir=jeu)
print("revision du modele", info.sha)
EOF
j "modèle et jeu au disque : $(tail -n 1 "$X/descente.txt")"
# 6. marche
lancer() {  # $1 = python ; puis arguments de course_v1 : marche sous timeout jusqu'à FIN_MARCHE, arrêt de ce seul processus
    local py="$1" d c; shift
    d=$(duree_marche "$FIN_MARCHE" "$(date +%s)") || return 124
    env HF_HUB_OFFLINE=1 PYTHONPATH=src timeout --signal=TERM --kill-after=120 "$d" \
        "$py" -m controle_ia.dopamine_exploratoire.course_v1 "$@" --racine "$D" --run-id "$RUN_ID" --modele-local "$T/modele" \
        >> "$X/marche.txt" 2>> "$X/marche.err" &
    local pid=$!
    j "marche lancée (PID $pid ; $*)"
    attendre_la_marche "$pid"
    wait "$pid"; c=$?
    j "marche : code $c ($1)"
    return "$c"; }
[ -z "$(git status --porcelain --untracked-files=all)" ] || arret "arbre non propre avant la marche" 2
A_REL=(); [ "$CONTEXTES" != - ] && A_REL=(--contextes "$CONTEXTES" --contextes-sha256 "$(cut -c1-64 < "$D/$CONTEXTES.sha256")" --liste-honnetes "$LISTE_HONNETES")
lancer "$T/venv-vllm/bin/python" generer --jeu "$T/math500/test.jsonl" --generateur vllm --fin-lancements-utc-s "$FIN_LANCEMENTS_UTC_S" "${A_REL[@]}"; c=$?
[ "$c" = 0 ] && { lancer "$PY" suite --jeu "$T/math500/test.jsonl" --generateur vllm --fin-lancements-utc-s "$FIN_LANCEMENTS_UTC_S" "${A_REL[@]}"; c=$?; }
case "$c" in
    0) terminer 0 "FIN : marche menée au bout";;
    124) terminer 3 "ARRET : un quart d'heure avant la destruction : marche arrêtée par TERM";;
    3) terminer 4 "ARRET : garde de la course (tranche, génération, vérité plantée ou horloge) : voir marche.err";;
    *) terminer 4 "ARRET : marche en échec, code $c (marche.err)";;
esac
