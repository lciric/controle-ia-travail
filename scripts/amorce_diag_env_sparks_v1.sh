#!/usr/bin/env bash
# Tir de DIAGNOSTIC D'ENVIRONNEMENT SPARKS, v1 — hors du code scellé (R-1549 : la session 1 réelle s'est arrêtée en code 2,
# « essais en échec : arrêt avant tout calcul », 16 échecs, 22 sautés, 25 erreurs sur la machine, 361 réussis sur processeur).
# Socle repris à l'octet de l'amorce v12 (`scripts/amorce_instance_sparks_exp7_nul_v12.sh`, l. 74 à 187, 215 à 219, 221 et
# 223 : ligne de démarrage comptée, minuterie de destruction par la clé du conteneur, outils installés sous `timeout`,
# destruction immédiate ou sur refus). Puis : clone du commit de lancement (`COMMIT`, 0d163bdc… par défaut), **même
# séquence que le script d'instance v12, l. 62 à 76** (venv `python3.11` sinon `python3`, `pip install -q -r
# requirements-gpu.txt`, `pip freeze`, `nvidia-smi`, les cinq fichiers d'essais sous `python -I -B -m pytest -q -p
# no:cacheprovider`, avec `--tb=short -rA` pour la sortie complète), relevés d'environnement sans aucune valeur de clé
# (`garde_secrets`, qui refuse la poussée si une valeur de jeton apparaît), poussée vérifiée sur
# `essai/sparks-diag-env-v1-<CONTAINER_ID>`, puis destruction de l'instance par elle-même. Aucun modèle, aucune donnée.
# Variables : COMMIT (lancement), ECHEANCE_UTC_S, GH_TOKEN, DEPOT_URL ; posées par Vast : CONTAINER_ID, CONTAINER_API_KEY.
# Essai local : RACINE_AMORCE, VENV_EXISTANT, DIAG_FICHIERS_ESSAIS (arguments de pytest à la place des cinq fichiers),
# AMORCE_T_GIT_S, AMORCE_T_PIP_S, AMORCE_T_ESSAIS_S (raccourcis seulement), MINUTERIE_*.
set -uo pipefail
R="${RACINE_AMORCE:-/root}"
API=https://console.vast.ai/api/v0
FIN_GO=1795046400            # 2026-11-19T00:00:00Z
GO_ID=GO-2026-11-04-04
export HOME="${HOME:-/root}"
export TZ=UTC
cd "$R" || { echo "AMORCE V10 : racine $R inaccessible : aucune destruction possible : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }
N_DEM=0; [ -s "$R/sparks-v10-demarrages-amorce.txt" ] && read -r N_DEM < "$R/sparks-v10-demarrages-amorce.txt"
case "$N_DEM" in ''|*[!0-9]*) N_DEM=0;; esac
N_DEM=$(( N_DEM + 1 )); echo "$N_DEM" > "$R/sparks-v10-demarrages-amorce.txt"
printf 'AMORCE V10 DEMARRAGE %s : %(%Y-%m-%dT%H:%M:%SZ)T, machine %s, commit %s\n' "$N_DEM" -1 "${CONTAINER_ID:-?}" "${COMMIT:-?}"
IFS= read -r -d '' MINUTERIE_TXT <<'MINUTERIE'
ECH="$1"; R="$2"; API="$3"; J="$R/sparks-v5-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH" >> "$J"
echo "$$" > "$R/sparks-v5-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
supprimer() {  # un DELETE par la clé du conteneur : curl, sinon python3 (urllib) ; corps écrit au disque ; rend le code HTTP
    local c
    if command -v curl >/dev/null 2>&1; then
        c=$(curl -sS -m 60 -o "$R/sparks-v5-delete-corps.txt" -w '%{http_code}' -X DELETE -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" \
            "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
    elif command -v python3 >/dev/null 2>&1; then
        c=$(python3 -I -B -c 'import os, sys, urllib.error, urllib.request
q = urllib.request.Request(sys.argv[1], method="DELETE", headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", "")})
try:
    with urllib.request.urlopen(q, timeout=60) as r:
        code, corps = r.status, r.read()
except urllib.error.HTTPError as e:
    code, corps = e.code, e.read()
except Exception:
    code, corps = 0, b""
open(sys.argv[2], "wb").write(corps)
print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$R/sparks-v5-delete-corps.txt" 2>/dev/null) || c=000
    else c=aucun; fi
    echo "$c"
}
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/sparks-v5-detruire" ]; do sleep "$PAS"; done
raison="échéance"; [ -e "$R/sparks-v5-detruire" ] && raison="ordre de la machine"
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do  # jamais d'arrêt de la machine : il tuerait cette minuterie ; le DELETE recommence jusqu'à la fin de la marge
    n=$((n + 1))
    if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then  # une tentative dure au plus 190 s : jamais au-delà de FIN
        echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue, plus de tentative possible avant la fin de la marge" >> "$J"; exit 4
    fi
    c=$(supprimer)
    if [ "$c" = aucun ]; then echo "$(date -u +%FT%TZ) ALARME : ni curl ni python3 : aucune destruction possible par la machine" >> "$J"; exit 5; fi
    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/sparks-v5-delete-corps.txt" 2>/dev/null && refus=oui
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n, $raison) : HTTP $c, refus dans le corps : $refus" >> "$J"
    case "$c" in 2??) if [ "$refus" = non ]; then echo "$(date -u +%FT%TZ) instance $CONTAINER_ID détruite" >> "$J"; exit 0; fi;; esac
    if command -v vastai >/dev/null 2>&1; then
        timeout -k 5 120 vastai destroy instance "$CONTAINER_ID" -y >/dev/null 2>&1; v=$?
        echo "$(date -u +%FT%TZ) repli : vastai destroy instance $CONTAINER_ID -y : code $v (sortie non gardée)" >> "$J"
        [ "$v" = 0 ] && exit 0
    fi
    [ "$(date +%s)" -lt "$FIN" ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue" >> "$J"; exit 4; }
    sleep "$REESSAI"
done
MINUTERIE
printf '%s' "$MINUTERIE_TXT" > "$R/sparks-v5-minuterie.sh" || { echo "AMORCE V10 : minuterie impossible à écrire : sleep infinity pour ne pas boucler"; sleep infinity; exit 1; }
destruction_immediate() {  # refus avant la minuterie de ce démarrage : la minuterie jouée tout de suite (échéance 0) ; échec : sleep infinity
    echo "AMORCE V5 : $1 : refus avant l'ordre consommé : destruction immédiate de l'instance"
    bash "$R/sparks-v5-minuterie.sh" 0 "$R" "$API" < /dev/null >> "$R/sparks-v5-minuterie.log" 2>&1; local st=$?
    if [ "$st" = 0 ]; then echo "AMORCE V5 : destruction obtenue"; exit 2; fi
    echo "AMORCE V5 : destruction non obtenue (code $st) : sleep infinity pour ne pas boucler ; la session détruit par l'identifiant"
    sleep infinity; exit 2
}
T_APT=300; case "${AMORCE_T_APT_S:-}" in ''|*[!0-9]*) ;; *) [ "$AMORCE_T_APT_S" -ge 1 ] && [ "$AMORCE_T_APT_S" -le 300 ] && T_APT=$AMORCE_T_APT_S;; esac
OUTILS="curl git python3 timeout setsid sha256sum tar gzip awk sed sort cut tail head mktemp find grep date sleep cat tr"
manquants() { local o m=""; for o in $OUTILS; do command -v "$o" >/dev/null 2>&1 || m="$m $o"; done; printf '%s' "$m"; }
paquet() { case "$1" in curl|git|python3|tar|gzip|sed|grep) printf '%s' "$1";; awk) printf gawk;; setsid) printf util-linux;; find) printf findutils;; *) printf coreutils;; esac; }
MANQ=$(manquants)
if [ -n "$MANQ" ]; then
    echo "AMORCE V5 : outils absents :$MANQ : installation bornée (apt-get, $T_APT s par étape)"
    if command -v apt-get >/dev/null 2>&1 && command -v timeout >/dev/null 2>&1; then
        PAQ="ca-certificates"; for o in $MANQ; do PAQ="$PAQ $(paquet "$o")"; done
        DEBIAN_FRONTEND=noninteractive timeout -k 10 "$T_APT" apt-get update -qq >/dev/null 2>&1 \
            && DEBIAN_FRONTEND=noninteractive timeout -k 10 "$T_APT" apt-get install -y -qq --no-install-recommends $PAQ >/dev/null 2>&1
        echo "AMORCE V5 : installation ($PAQ) : code $?"
    else echo "AMORCE V5 : apt-get ou timeout absent : installation impossible"; fi
    MANQ=$(manquants)
    [ -z "$MANQ" ] || destruction_immediate "outils absents après installation :$MANQ"
fi
outil() { command -v "$1" >/dev/null 2>&1 && echo oui || echo NON; }
echo "AMORCE V5 : outils : curl oui, git oui, unshare $(outil unshare), chroot $(outil chroot), prlimit $(outil prlimit), vastai $(outil vastai)"
E="$R/sparks-v5-echeance.txt"
[ -s "$R/sparks-v5-creation.txt" ] || date +%s > "$R/sparks-v5-creation.txt"
if [ -s "$E" ]; then read -r ECH < "$E"; else
    ECH="${ECHEANCE_UTC_S:-}"
    case "$ECH" in ''|*[!0-9]*) destruction_immediate "ECHEANCE_UTC_S absente ou non entière : rien ne part";; esac
    [ "$ECH" -le "$FIN_GO" ] || { echo "AMORCE V5 : échéance ramenée à la fin du GO ($FIN_GO)"; ECH=$FIN_GO; }
    echo "$ECH" > "$E"
fi
case "$ECH" in ''|*[!0-9]*) destruction_immediate "échéance du disque illisible";; esac
if [ -s "$R/sparks-v5-minuterie.pid" ] && kill -0 "$(cat "$R/sparks-v5-minuterie.pid")" 2>/dev/null; then
    echo "AMORCE V5 : TÉMOIN : minuterie antérieure $(cat "$R/sparks-v5-minuterie.pid") encore vivante (hors conteneur ?)"
fi
setsid bash "$R/sparks-v5-minuterie.sh" "$ECH" "$R" "$API" < /dev/null >> "$R/sparks-v5-minuterie.log" 2>&1 &
PM=$!
echo "AMORCE V5 : minuterie lancée (échéance $ECH, $(date -u -d "@$ECH" +%FT%TZ 2>/dev/null || echo "?"))"
attendre_minuterie() {   # le conteneur reste en vie tant que la minuterie de CE démarrage détruit ($PM ; borné)
    local lim=$(( $(date +%s) + ${MINUTERIE_MARGE_S:-1800} + 120 ))
    while kill -0 "$PM" 2>/dev/null && [ "$(date +%s)" -lt "$lim" ]; do sleep 2; done
}
resultat_destruction() {  # minuterie finie en code 0 : sortie ; sinon (ou encore vivante) : sleep infinity, dit au journal
    local st=124
    kill -0 "$PM" 2>/dev/null || { wait "$PM" 2>/dev/null; st=$?; }
    [ "$st" = 0 ] && exit "$1"
    echo "AMORCE V5 : destruction non obtenue (minuterie, code $st) : sleep infinity pour ne pas boucler ; la session détruit par l'identifiant"
    sleep infinity; exit "$1"; }
detruire() { echo "$1" > "$R/sparks-v5-detruire"; echo "AMORCE V5 : destruction demandée ($1)"; attendre_minuterie; resultat_destruction "${2:-0}"; }
refus() {  # refus avant l'ordre consommé : destruction de l'instance, jamais une sortie (une sortie fait relancer le conteneur)
    echo "AMORCE V5 : $1 : refus avant l'ordre consommé : destruction de l'instance"
    local a="${AMORCE_ATTENTE_REFUS_S:-0}"; case "$a" in ''|*[!0-9]*) a=0;; esac; [ "$a" -le 600 ] || a=600
    if [ "$a" -gt 0 ]; then echo "AMORCE V5 : attente de $a s avant la destruction (lecture du journal par la session)"; sleep "$a"; fi
    detruire "refus : $1" 2; }
[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun calcul"
[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l'échéance : aucun diagnostic"
AIDE='!f() { echo username=x-access-token; echo "password=${GH_TOKEN:-}"; }; f'
borne_t() { case "${1:-}" in ''|*[!0-9]*) echo "$2";; *) if [ "$1" -ge 1 ] && [ "$1" -le "$2" ]; then echo "$1"; else echo "$2"; fi;; esac; }
echo "AMORCE V5 : tir de diagnostic d'environnement v1 (hors code scellé) ; aucun modèle, aucune donnée"
T_GIT=$(borne_t "${AMORCE_T_GIT_S:-}" 600); T_PIP=$(borne_t "${AMORCE_T_PIP_S:-}" 1200); T_ESSAIS=$(borne_t "${AMORCE_T_ESSAIS_S:-}" 1500)
COMMIT="${COMMIT:-0d163bdcea563a9e001f336c33f36ee6d41c800a}"
case "$COMMIT" in *[!0-9a-f]*|'') refus "COMMIT illisible";; esac
[ "${#COMMIT}" = 40 ] || refus "COMMIT de 40 caractères attendu"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) refus "CONTAINER_ID illisible";; esac
DEPOT_URL="${DEPOT_URL:-https://github.com/lciric/controle-ia-travail.git}"; export DEPOT_URL
BRANCHE="essai/sparks-diag-env-v1-$CONTAINER_ID"
D="$R/diag-env"; mkdir -p "$D" || refus "dossier des relevés impossible"
garde_secrets() {  # aucune valeur de jeton dans les fichiers à pousser ; refus sinon (la lecture par la session est aveugle)
    local f v val
    for f in "$@"; do
        [ -f "$f" ] || continue
        for v in GH_TOKEN CONTAINER_API_KEY HF_TOKEN VAST_API_KEY CONTROLE_IA_GITHUB_TOKEN; do
            val="${!v:-}"; [ "${#val}" -ge 8 ] || continue
            if grep -qF -- "$val" "$f"; then echo "AMORCE V5 : GARDE DES SECRETS : valeur de $v trouvée dans $(basename "$f") : aucune poussée"; return 1; fi
        done
    done
    return 0
}
relever() {  # relevés d'environnement, noms de variables seuls (aucune valeur), système, interpréteurs
    { echo "# variables d'environnement : noms seuls, triés (aucune valeur)"; env | cut -d= -f1 | sort; } > "$D/env-sans-secrets.txt"
    { echo "# uname"; uname -a; echo "# os-release"; cat /etc/os-release 2>/dev/null; echo "# nproc"; nproc; echo "# free -g"; free -g 2>/dev/null
      echo "# df -h /"; df -h / 2>/dev/null; echo "# locale"; locale 2>/dev/null; } > "$D/systeme.txt" 2>&1
    { echo "# python3.11 : $(command -v python3.11 || echo absent)"; echo "# python3 : $(command -v python3 || echo absent)"
      python3 -VV 2>&1; [ -n "$(command -v python3.11)" ] && python3.11 -VV 2>&1; echo "# python du venv : $(command -v python)"; python -VV 2>&1
      echo "# pip : $(pip --version 2>&1)"; } > "$D/python-version.txt" 2>&1
    nvidia-smi > "$D/nvidia-smi.txt" 2>&1 || echo "AMORCE V5 : pas de carte graphique visible"
}
pousser() {  # commit et poussée vérifiée des relevés ; aucune sortie brute de git affichée
    garde_secrets "$D"/* || return 1
    mkdir -p "$R/amorce-depot/diag-env" && cp "$D"/* "$R/amorce-depot/diag-env/" || return 1
    git -C "$R/amorce-depot" config user.name "instance de diagnostic (SPARKS)" && git -C "$R/amorce-depot" config user.email "instance-diag@invalid"
    git -C "$R/amorce-depot" add diag-env && git -C "$R/amorce-depot" commit -qm "SPARKS diag env v1 : relevés de l'instance $CONTAINER_ID" || return 1
    local essai distant
    for essai in 1 2 3; do timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" push -q origin "$BRANCHE" >/dev/null 2>&1 && break; sleep $((15 * essai)); done
    distant=$(timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" ls-remote origin "refs/heads/$BRANCHE" 2>/dev/null | cut -f1)
    if [ -n "$distant" ] && [ "$distant" = "$(git -C "$R/amorce-depot" rev-parse HEAD)" ]; then echo "AMORCE V5 : poussée vérifiée sur $BRANCHE ($distant)"; return 0; fi
    echo "AMORCE V5 : POUSSÉE NON VÉRIFIÉE sur $BRANCHE"; return 1
}
fin_diag() {  # fin du diagnostic : relevés, poussée (vérifiée ou non), puis destruction de l'instance par elle-même
    relever
    if pousser; then detruire "fin du diagnostic ($1), poussée vérifiée" "${2:-0}"; fi
    detruire "fin du diagnostic ($1), poussée NON vérifiée : relevés perdus" "${2:-0}"
}
timeout -k 10 "$T_GIT" git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout "$DEPOT_URL" "$R/amorce-depot" \
    || refus "clonage impossible (ou délai de $T_GIT s)"
git -C "$R/amorce-depot" config credential.helper "$AIDE"
timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" sparse-checkout set --no-cone '/*' '!/*/' '/src/' '/tests/' '/scripts/' '/prereg/SPARKS-EXP7-NUL-*' '/registres/go.md' '/docs/notes/sparks-exp7-nul-v1/' \
    && timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" checkout -q "$COMMIT" \
    || refus "commit $COMMIT introuvable (ou délai de $T_GIT s)"
code_branche=0
timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" ls-remote --exit-code origin "refs/heads/$BRANCHE" >/dev/null 2>&1 || code_branche=$?
[ "$code_branche" = 2 ] || refus "branche $BRANCHE déjà présente ou dépôt illisible (code $code_branche)"
git -C "$R/amorce-depot" checkout -q -b "$BRANCHE"
cd "$R/amorce-depot" || refus "clone inaccessible"
echo "AMORCE V5 : séquence du script d'instance v12 (l. 62 à 76) : venv, installation, essais"
if [ -n "${VENV_EXISTANT:-}" ]; then . "$VENV_EXISTANT/bin/activate"; echo "venv existant ($VENV_EXISTANT) : installation sautée" > "$D/pip.txt"; else
    python3.11 -m venv "$R/venv" 2>/dev/null || python3 -m venv "$R/venv"
    . "$R/venv/bin/activate"
    timeout -k 30 "$T_PIP" pip install -q -r requirements-gpu.txt > "$D/pip.txt" 2>&1 || { echo "AMORCE V5 : installation refusée (code $?)"; echo "INSTALLATION REFUSÉE" >> "$D/pip.txt"; fin_diag "installation refusée" 2; }
fi
pip freeze > "$D/pip-freeze.txt" 2>&1
export PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 TOKENIZERS_PARALLELISM=false
{ echo "# torch"; python -I -c 'import torch, sys; print(torch.__version__, "cuda", torch.cuda.is_available(), torch.version.cuda, sys.version)'; } > "$D/torch.txt" 2>&1 || true
ESSAIS="${DIAG_FICHIERS_ESSAIS:-tests/test_sparks_exp7_nul_v1.py tests/test_sparks_exp7_nul_v2.py tests/test_sparks_exp7_nul_v3.py tests/test_sparks_exp7_nul_v4.py tests/test_sparks_exp7_nul_v12.py}"
echo "AMORCE V5 : essais ($ESSAIS)"
# shellcheck disable=SC2086
timeout -k 30 "$T_ESSAIS" python -I -B -m pytest -q -p no:cacheprovider --tb=short -rA $ESSAIS > "$D/tests.txt" 2>&1; code=$?
echo "$code" > "$D/tests-code.txt"
echo "AMORCE V5 $(date -u +%FT%TZ) : essais : code $code : $(tail -1 "$D/tests.txt")"
fin_diag "essais : code $code" "$code"
