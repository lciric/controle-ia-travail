#!/usr/bin/env bash
# Amorce de l'instance de l'étape B bis de T0.7, v1 (prereg/T0.7-etape-B-bis-v1.md, plan, points 1 à 8 ; « Calcul et dépense » ;
# « Liste d'arrêt »). Jouée au démarrage de l'instance (A100, étiquette bbis-t07-v1), passée par scripts/lancer_bbis_v1.sh (commande
# de création imprimée, base64). Une instance, une marche ; écrit sous $R/bbis-t07-v1 seulement.
# Ordre : 0. minuterie de destruction par l'identifiant à l'échéance (R10) ; 1. machine (carte, clés par leur nom) ; 2. dépôt au
#   commit COMMIT (extraction partielle : src, tests du paquet, scripts, prereg du texte, registres nommés et fichiers qu'ils citent ;
#   jamais docs/notes/, jamais les fichiers de la pièce « mots et coût », jamais scripts/extraire_mesures_epreuve_t06_v1.py) ;
#   3. sortie de 7b par refspec explicite, FICHIERS NOMMÉS seulement (manifeste, episodes-t06.json, distillation-t06.json,
#   textes, mesures, deux adaptateurs, sous-ensemble d'activations) : jamais lecture-sondes-t06.json, resume.json, ni rien de 7a ;
#   4. paquets ; 5. essais du paquet (tests/test_t07bbis_*.py) ; 6. modèle au cache local (révision du manifeste de 7b) ;
#   7. marche (`controle_ia.t07bbis.marche_v1`, BBIS_INSTANCE=1, hors ligne) ; 8. poussée sur la branche neuve
#   donnees/t07-etape-b-bis-v1 (légers d'abord, fichiers de moins de 95 Mo seulement) ; 9. fin : état « stopped » demandé ; la
#   session détruit par l'identifiant (R10). Arrêt de débit (code 3 de la marche) : relecture et journal poussés, instance
#   arrêtée (« stopped »), gardée au plus 12 heures, nœud de Lazar (la session détruit sans mot dans les 12 heures).
# Aucune aire, aucun état, aucun résumé de score n'est imprimé ni écrit (le journal ne porte que des étapes et des durées).
# Variables (--env) : COMMIT, BRANCHE_CODE (branche qui porte COMMIT), RUN_7B, BRANCHE_7B, RUN_BBIS, ECHEANCE_UTC_S, GO_ID
#   (GO-2026-11-14-09), GH_TOKEN, HF_TOKEN ; facultatives, sur le mot de Lazar seulement : VARIANTE=r1 et DECISION_VARIANTE=R-…
#   (variante (r1) de la garde de débit) ; posées par Vast : CONTAINER_ID, CONTAINER_API_KEY. Aucune clé n'est jamais affichée.
# Essai local (AMORCE_ESSAI_LOCAL=1) : contrôles des arguments seulement, puis sortie (code 0) avant tout réseau ; hors essai,
#   ESSAI_* sont refusées.
set -uo pipefail
ESSAI="${AMORCE_ESSAI_LOCAL:-0}"
R="${RACINE_AMORCE:-/root}"
[ "$ESSAI" = 1 ] || [ -z "${RACINE_AMORCE:-}" ] || { echo "BBIS REFUS : RACINE_AMORCE en essai local seulement"; exit 2; }
T="$R/bbis-t07-v1"; D="$T/depot"; X="$T/traces"; L="$X/journal-bbis.txt"; XT=traces/bbis-t07-v1
API=https://console.vast.ai/api/v0
GO_ATTENDU=GO-2026-11-14-09
BR_SORTIE=donnees/t07-etape-b-bis-v1
DEPOT_URL_OFFICIEL=https://github.com/lciric/controle-ia-travail.git
SEUIL=94000000
mkdir -p "$X" || { echo "BBIS REFUS : $X impossible"; exit 2; }
export TZ=UTC PYTHONDONTWRITEBYTECODE=1
j() { printf '%s BBIS %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "$L"; }
BRANCHE_PRETE=0
fin_instance() {  # état « stopped » demandé ; la minuterie meurt avec le conteneur ; la session détruit par l'identifiant (R10)
    local c
    c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X PUT -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        -H 'Content-Type: application/json' -d '{"state": "stopped"}' "$API/instances/${CONTAINER_ID:-}/" 2>/dev/null) || c=000
    j "fin, code $1 ; état « stopped » demandé : HTTP $c ; la session détruit par l'identifiant (R10)"
    sleep infinity; exit "$1"; }
traces() { mkdir -p "$D/$XT" && cp -f "$X"/* "$D/$XT/"; }
arret() { j "ARRET : $1"; if [ "$BRANCHE_PRETE" = 1 ]; then traces && pousser "B bis : traces de l'arrêt" "$XT" || true; fi
    fin_instance "${2:-4}"; }
# 0. arguments, échéance, minuterie
for v in COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS ECHEANCE_UTC_S GO_ID; do
    [ -n "${!v:-}" ] || { echo "BBIS REFUS : variable $v absente"; exit 2; }; done
case "$COMMIT" in *[!0-9a-f]*|'') echo "BBIS REFUS : COMMIT illisible"; exit 2;; esac
[ "${#COMMIT}" = 40 ] || { echo "BBIS REFUS : COMMIT de 40 caractères attendu"; exit 2; }
[ "$GO_ID" = "$GO_ATTENDU" ] || { echo "BBIS REFUS : GO_ID $GO_ID ≠ $GO_ATTENDU (ligne de GO de B bis)"; exit 2; }
case "$RUN_BBIS" in [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-bbis-*) ;; *) echo "BBIS REFUS : RUN_BBIS illisible"; exit 2;; esac
case "$ECHEANCE_UTC_S" in ''|*[!0-9]*) echo "BBIS REFUS : ECHEANCE_UTC_S illisible"; exit 2;; esac
# variante (r1) de la garde de débit : seulement sur le mot de Lazar, ligne de décision citée (DECISION_VARIANTE=R-…)
VARIANTE_ARGS=()
case "${VARIANTE:-}" in
    '') [ -z "${DECISION_VARIANTE:-}" ] || { echo "BBIS REFUS : DECISION_VARIANTE sans VARIANTE"; exit 2; };;
    r1) case "${DECISION_VARIANTE:-}" in R-[0-9]*) VARIANTE_ARGS=(--variante r1 --decision "$DECISION_VARIANTE");;
            *) echo "BBIS REFUS : variante (r1) sans ligne de décision R-… (DECISION_VARIANTE)"; exit 2;; esac;;
    *) echo "BBIS REFUS : VARIANTE ${VARIANTE} inconnue ((r1) seulement)"; exit 2;;
esac
if [ "$ESSAI" = 1 ]; then echo "BBIS ESSAI LOCAL : arguments conformes ; aucun réseau, aucune minuterie"; exit 0; fi
[ "$ECHEANCE_UTC_S" -gt "$(date +%s)" ] && [ "$ECHEANCE_UTC_S" -le $(( $(date +%s) + 86400 )) ] || { echo "BBIS REFUS : échéance hors de [maintenant, + 24 h]"; exit 2; }
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "BBIS REFUS : identifiant de l'instance illisible"; exit 2;; esac
minuterie() { local n c; while [ "$(date +%s)" -lt "$ECHEANCE_UTC_S" ]; do sleep 30; done
    j "MINUTERIE : échéance atteinte : destruction de l'instance $CONTAINER_ID par son identifiant (DELETE)"
    for n in 1 2 3 4 5; do c=$(curl -sS -m 60 -o /dev/null -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
        "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; j "MINUTERIE : DELETE, essai $n : HTTP $c"
        case "$c" in 2??) return 0;; esac; sleep 60; done; }
minuterie < /dev/null & j "minuterie lancée (PID $!, échéance $(date -u -d "@$ECHEANCE_UTC_S" +%FT%TZ))"
# 1. machine
for o in git curl python3 sha256sum awk sed grep stat find sort; do command -v "$o" > /dev/null || arret "outil absent : $o" 2; done
[ -n "${GH_TOKEN:-}" ] || arret "GH_TOKEN absent (par le nom)" 2
[ -n "${HF_TOKEN:-}" ] || arret "HF_TOKEN absent (par le nom)" 2
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader > "$X/nvidia-smi.txt" 2>&1 || arret "carte invisible (nvidia-smi)" 2
grep -q 'A100' "$X/nvidia-smi.txt" || arret "carte autre qu'une A100 : $(head -n 1 "$X/nvidia-smi.txt")" 2
j "carte : $(head -n 1 "$X/nvidia-smi.txt") ; disque libre $(df -P -B1 "$R" | awk 'NR == 2 { print $4 }') octets"
# 2. dépôt au commit COMMIT, extraction partielle
[ ! -e "$D" ] || arret "$D existe déjà (R12)" 2
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch "$BRANCHE_CODE" "$DEPOT_URL_OFFICIEL" "$D" || arret "clonage" 2
git -C "$D" config credential.helper "$AIDE"; git -C "$D" config user.name "instance de calcul (B bis)"; git -C "$D" config user.email "instance-calcul@invalid"
MOTIFS='/*
!/*/
/src/
/tests/conftest.py
/tests/test_t07bbis_*
/tests/aide_t07bbis_*
/scripts/amorce_bbis_v1.sh*
/scripts/enumerer_issues_bbis_v1.py*
/scripts/epreuve_niveau_deux_plis_bbis_v1.py*
/prereg/T0.7-etape-B-bis-v1.md*
/prereg/P3-consignes-v1.md*
/docs/sources/invites-2606.08892-v1/
/registres/t07-etape-b-bis-v1.md*
/registres/t07-etape-b-bis/
/registres/scellements-v1.md
/registres/scellements-v1.md.sha256
/registres/go-extraits/
!/diag/*/lecture-sondes-t06.json*
!/scripts/extraire_mesures_epreuve_t06_v1.py
!/scripts/mots_et_cout_t06_*'
git -C "$D" sparse-checkout init --no-cone && printf '%s\n' "$MOTIFS" | git -C "$D" sparse-checkout set --no-cone --stdin || arret "extraction partielle" 2
git -C "$D" checkout -q "$COMMIT" || arret "commit $COMMIT introuvable sur $BRANCHE_CODE" 2
[ "$(git -C "$D" rev-parse HEAD)" = "$COMMIT" ] || arret "tête ≠ COMMIT" 2
for p in $(awk -F'|' 'NF >= 6 { gsub(/ /, "", $4); if ($4 ~ /^[A-Za-z0-9._\/-]+$/ && $4 !~ /\.\./) print $4 }' "$D/registres/t07-etape-b-bis-v1.md" | sort -u); do
    case "$p" in *lecture-sondes-t06*|donnees/bras-attaque*|donnees/mode-tenu-a-l-ecart*|docs/notes/*) arret "chemin interdit cité : $p" 2;; esac
    for q in "$p" "$p.sha256"; do git -C "$D" cat-file -e "HEAD:$q" 2>/dev/null || continue
        mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "HEAD:$q" > "$D/$q" || arret "copie de $q" 2; done; done
j "dépôt au commit $COMMIT (branche $BRANCHE_CODE), registre propre et fichiers cités présents"
# 3. sortie de 7b : fichiers nommés seulement
git -C "$D" fetch -q origin "refs/heads/$BRANCHE_7B:refs/remotes/origin/$BRANCHE_7B" || arret "branche de 7b $BRANCHE_7B introuvable" 2
B7="refs/remotes/origin/$BRANCHE_7B"
apporter() { local q; for q in "$2" "$2.sha256"; do git -C "$D" cat-file -e "$1:$q" 2>/dev/null || continue
    mkdir -p "$D/$(dirname "$q")" && git -C "$D" show "$1:$q" > "$D/$q" || arret "copie de $q" 2; done; }
for f in "runs/$RUN_7B/manifeste.json" "diag/$RUN_7B/episodes-t06.json" "diag/$RUN_7B/distillation-t06.json"; do
    git -C "$D" cat-file -e "$B7:$f" 2>/dev/null || arret "$f absent de la branche de 7b" 2; apporter "$B7" "$f"; done
N7=0
for f in $(git -C "$D" ls-tree --name-only "$B7" -- "donnees/$RUN_7B/" | grep -E "^donnees/$RUN_7B/(adaptateur-(saboteur|temoin)\.pt|mesures-t06\.npz|textes-actions-t06\.jsonl|activations-sous-ensemble-t06-manifeste\.json|activations-sous-ensemble-t06-[0-9]{3}\.npz)$"); do
    apporter "$B7" "$f"; N7=$((N7 + 1)); done
[ "$N7" -ge 6 ] || arret "sortie de 7b incomplète ($N7 fichiers de données)" 2
for f in "diag/$RUN_7B/lecture-sondes-t06.json" "diag/$RUN_7B/resume.json"; do [ ! -e "$D/$f" ] || arret "$f présent (liste « Jamais ») : arrêt" 2; done
for p in $(python3 -I -c 'import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))["config"]
def f(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if isinstance(v, str) and (k == "chemin" or k.startswith("chemin_")):
                yield v
            yield from f(v)
    elif isinstance(x, list):
        for v in x:
            yield from f(v)
print("\n".join(sorted(set(f(c)))))' "$D/runs/$RUN_7B/manifeste.json"); do
    case "$p" in *lecture-sondes-t06*|docs/notes/*) arret "chemin interdit cité par la configuration de 7b : $p" 2;; esac
    apporter "HEAD" "$p"; done
j "sortie de 7b extraite : manifeste, épisodes, distillation, $N7 fichiers de données ; fichiers cités par sa configuration recopiés"
# 4. paquets
python3 -m venv "$T/venv" && timeout -k 10 3600 "$T/venv/bin/pip" install -q -r "$D/requirements-gpu.txt" > "$X/pip.txt" 2>&1 || arret "installation des paquets" 2
PY="$T/venv/bin/python"
"$PY" -c 'import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)' || arret "torch ne voit pas la carte" 2
"$PY" -m pip freeze --all > "$X/pip-freeze.txt" 2>/dev/null
cd "$D" || arret "dépôt" 2
# 5. essais du paquet (aucun couperet de temps)
PYTHONPATH=src "$PY" -m pytest -q -p no:cacheprovider --color=no tests/test_t07bbis_*.py --basetemp="$T/essais-tmp" > "$X/essais.txt" 2> "$X/essais.err"; c=$?
j "essais du paquet : code $c, $(tail -n 1 "$X/essais.txt" | sed -E 's/ in [0-9.]+s.*$//')"
[ "$c" = 0 ] || arret "essais du paquet en échec (essais.txt)" 2
[ -z "$(git status --porcelain --untracked-files=all -- src tests)" ] || arret "les essais ont écrit sous src ou tests" 2
# 6. modèle au cache local
PYTHONPATH=src timeout -k 10 3600 "$PY" -c 'import json, sys
from controle_ia.harnais.modeles import precharger_modele
a = json.load(open(sys.argv[1], encoding="utf-8"))["config"]["agent"]
print(precharger_modele(a["modele"], a["revision"]))' "runs/$RUN_7B/manifeste.json" > "$X/modele.txt" 2>&1 || arret "descente du modèle" 2
j "modèle au cache local"
# 7. branche de sortie neuve et poussées (chemins présents seulement, ajout explicite)
git ls-remote --exit-code origin "refs/heads/$BR_SORTIE" > /dev/null 2>&1; [ $? = 2 ] || arret "branche $BR_SORTIE présente sur le dépôt distant (R12) ou dépôt injoignable" 2
git checkout -q -b "$BR_SORTIE" || arret "branche locale" 2
envoyer() { local n; for n in 1 2 3; do git push -q origin "HEAD:refs/heads/$BR_SORTIE" && { j "poussé : $(git rev-parse HEAD) « $1 »"; return 0; }; sleep $((20 * n)); done
    BRANCHE_PRETE=0; arret "poussée « $1 » impossible" 4; }
pousser() {  # $1 = message ; puis chemins ; un fichier de plus de SEUIL octets arrête (la marche écrit des morceaux de moins de 90 Mo)
    local m="$1" x a=(); shift; for x in "$@"; do [ -e "$x" ] && a+=("$x"); done
    [ "${#a[@]}" -gt 0 ] || { j "rien à pousser (« $m »)"; return 0; }
    git add --sparse -f -- "${a[@]}" || { BRANCHE_PRETE=0; arret "ajout « $m »" 4; }
    while IFS= read -r -d '' x; do [ "$(stat -c %s "$x")" -le "$SEUIL" ] || { BRANCHE_PRETE=0; arret "fichier de plus de $SEUIL octets : $x (nœud)" 4; }
    done < <(git diff --cached --name-only -z --diff-filter=AM)
    if git diff --cached --quiet; then j "rien de neuf (« $m »)"; else git commit -q -m "$m" || { BRANCHE_PRETE=0; arret "commit « $m »" 4; }; envoyer "$m"; fi; }
BRANCHE_PRETE=1
# 8. marche (relecture forcée, apprentissage, notation, fichiers fermés), hors ligne ; une marche lente mais vivante n'est jamais
#    arrêtée hors la garde de débit
j "marche : début (run $RUN_BBIS)"
env BBIS_INSTANCE=1 HF_HUB_OFFLINE=1 CUBLAS_WORKSPACE_CONFIG=:4096:8 PYTHONPATH=src "$PY" -m controle_ia.t07bbis.marche_v1 \
    --racine . --run-7b "$RUN_7B" --run-bbis "$RUN_BBIS" --travail "$T/travail" ${VARIANTE_ARGS[@]+"${VARIANTE_ARGS[@]}"} \
    > "$X/marche.txt" 2> "$X/marche.err"; c=$?
j "marche : code $c"
CH=("runs/$RUN_BBIS" "diag/$RUN_BBIS" "$XT")
case "$c" in
    0) traces; pousser "B bis : relecture et sondes (aucune aire), run $RUN_BBIS" "runs/$RUN_BBIS" "diag/$RUN_BBIS" "$XT"
       for f in $(find "donnees/$RUN_BBIS" -type f | sort); do pousser "B bis : $f" "$f"; done
       traces; pousser "B bis : traces de fin" "$XT"
       j "FIN : marche menée au bout, run $RUN_BBIS, tête $(git rev-parse HEAD) ; SCORES-BBIS à inscrire par la mère (diag/$RUN_BBIS/sondes-bbis.json)"
       fin_instance 0;;
    3) traces; pousser "B bis : ARRÊT DE DÉBIT (relecture et journal ; aucun score)" "${CH[@]}"
       arret "garde de débit : marche projetée au-delà de 11 h : instance arrêtée, gardée au plus 12 h, nœud de Lazar ((r1) ou (r2))" 3;;
    *) traces; pousser "B bis : marche en arrêt, code $c" "${CH[@]}"; arret "marche : code $c (marche.err)" 4;;
esac
