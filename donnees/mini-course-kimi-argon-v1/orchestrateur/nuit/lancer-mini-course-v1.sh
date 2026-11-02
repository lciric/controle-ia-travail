#!/bin/bash
# Lanceur de la mini-course d'idéation, Kimi et Argon seuls (GO-2026-11-01-12, plafond cumulé 10 USD, devis scénario B), v1.
# Rédigé le 1er novembre 2026 par un sous-agent de session-depot ; jamais lancé par son rédacteur (répétition simulée seulement,
# sans réseau). Gabarit : donnees/epreuve-fraiche-pont-v1/lancer-epreuve-pont-v2.sh et donnees/espece-seule-v1/lancer-espece-seule-v3.sh.
# Usage (en arrière-plan ; journal dans le dossier du run, voir LISEZMOI-mini-course-kimi-argon-v1.md) :
#   GO_ID=GO-2026-11-01-12 nohup bash lancer-mini-course-v1.sh lancer /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/run-AAAAMMJJ-HHMM >RUN.demarrage.log 2>&1 &
# Clés : GEMINI_API_KEY_2 donnée au seul relais Argon local (commande_argon_v56_nuit_v1.py servir), sous le nom GEMINI_API_KEY que lit
# appeler_gemini ; KIMI_API_KEY donnée au seul relais Kimi local (relais_kimi_v3.py, empreinte vérifiée). Les deux relais tournent sous
# env -i, PID vérifiés (R10), arrêtés par trap. L'orchestrateur et les commandes ne voient aucune clé (le noyau v56 refuse de partir
# sinon). Aucune clé en argument, aucune en fichier. Limite dite (comme les lanceurs précédents) : les clés transitent par la ligne de
# commande d'env -i jusqu'à son exec (quelques microsecondes dans /proc), et /proc/<pid>/environ des relais les expose au même
# utilisateur ; conteneur à un seul utilisateur. Sans set -e.
# Garde cumulée au pire cas avant chaque appel : registre-depense-cumulee-v1.jsonl du run (réglé + engagé + pire cas <= 10 USD), tenu
# par les deux commandes et les deux contrôles ; seconds barrages : plafond de chaque relais (10 USD), plafond dur de chaque étape
# (noyau v56, porte « environnement »), plafond de session de chaque appel.
# Codes : 0 fini ; 2 refus de lancer ; 3 relais ou contrôle en échec ; 6 clé trouvée dans une sortie ; 7 trace refusée ;
# autre : code du lanceur Python (2 : refus, arrêt ou nœud) ou de timeout (124).
set -uo pipefail; set +x
cd "$(dirname "$0")" || exit 2
N="$PWD"; REPO=/home/user/controle-ia-travail
GO_ID="${GO_ID:?GO_ID absent}"; MODE="${1:?mode : lancer}"; RUN="${2:?dossier du run (neuf, sous donnees/)}"
[ "$MODE" = "lancer" ] || { echo "mode : lancer" >&2; exit 2; }
[ "$GO_ID" = "GO-2026-11-01-12" ] || { echo "la mini-course ne court que sous GO-2026-11-01-12" >&2; exit 2; }
grep -q "^| $GO_ID |" "$REPO/registres/go.md" || { echo "$GO_ID absent de registres/go.md" >&2; exit 2; }
case "$RUN" in "$REPO"/donnees/*) ;; *) echo "le dossier du run doit être sous $REPO/donnees/ (exclu de la copie publique)" >&2; exit 2 ;; esac
[ ! -e "$RUN" ] || { echo "$RUN existe déjà (R12)" >&2; exit 2; }
mkdir -p "$RUN" || exit 2
RA="$(cd "$RUN" && pwd)"
exec >>"$RA/journal-lancement-mini-course-v1.log" 2>&1
echo "$(date -u +%FT%TZ) début ; GO $GO_ID ; run $RA ; PID du lanceur $$"

PY=/usr/bin/python3
[ -x "$PY" ] && "$PY" -I -c "import numpy" 2>/dev/null || { echo "Python des appels absent ou sans numpy : $PY" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ -n "${KIMI_API_KEY:-}" ] || { echo "KIMI_API_KEY absente" >&2; exit 2; }
K=$REPO/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd "$K" && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
(cd "$REPO/donnees/espece-seule-v1" && sha256sum -c --quiet collisionneur_v7.py.sha256) || { echo "collisionneur v7 non conforme" >&2; exit 2; }
(cd "$N/.." && sha256sum -c --quiet nuit/EMPREINTES-orchestrateur-v56-copie-v1.txt) \
  || { echo "copie de l'orchestrateur v56 modifiée (archive 29b1b38c…)" >&2; exit 2; }
DP=$REPO/docs/notes/mini-course-kimi-argon-v1
(cd "$DP" && sha256sum -c --quiet preregistrement-mini-course-kimi-argon-v1.md.sha256 \
   contre-lecture-preregistrement-mini-course-kimi-argon-v1.md.sha256) \
  || { echo "préenregistrement ou contre-lecture absents, non scellés ou modifiés (R1, R2) : aucun lancement" >&2; exit 2; }
CONF=$N/configuration-mini-course-kimi-argon-v1.json
# Vérification complète sans écriture ni appel (configuration, gardes R5 à É0, ligne de GO à 10 USD exactement).
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$RA" GO_ID="$GO_ID" "$PY" -I -B lancer_mini_course_v1.py verifier \
  --configuration "$CONF" --registre-go "$REPO/registres/go.md" > "$RA/verification-avant-lancement.json" \
  || { echo "vérification refusée (voir ci-dessus)" >&2; exit 2; }

REG="$RA/registre-depense-cumulee-v1.jsonl"
PORT_K=8804; PORT_A=8805; PID_K=""; PID_A=""
arreter_pid() { local p="$1" i=0; [ -n "$p" ] || return 0; kill "$p" 2>/dev/null; while kill -0 "$p" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done; kill -0 "$p" 2>/dev/null && kill -9 "$p" 2>/dev/null; true; }
etat_relais() { "$PY" -I -c "import urllib.request,sys; o=urllib.request.build_opener(urllib.request.ProxyHandler({})); sys.stdout.write(o.open('http://127.0.0.1:$1/relais/etat', timeout=5).read().decode())" 2>/dev/null; }
arreter() { [ -n "$PID_K" ] && etat_relais $PORT_K > "$RA/etat-final-relais-kimi.json"; [ -n "$PID_A" ] && etat_relais $PORT_A > "$RA/etat-final-relais-argon.json"; arreter_pid "$PID_K"; arreter_pid "$PID_A"; PID_K=""; PID_A=""; }
trap arreter EXIT; trap 'arreter; exit 130' INT TERM HUP
for p in $PORT_K $PORT_A; do
  "$PY" -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$p)) else 1)" || { echo "port $p déjà pris" >&2; exit 2; }
done
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" \
  "$PY" -I -B "$K/relais_kimi_v3.py" --port $PORT_K --modeles-permis kimi-k3.1-pro --plafond-usd 10 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 40 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1700 \
  --delai-silence-s 600 --journal "$RA/relais-kimi-journal.jsonl" > "$RA/relais-kimi.log" 2>&1 &
PID_K=$!
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" \
  NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" \
  "$PY" -I -B "$N/commande_argon_v56_nuit_v1.py" servir --port $PORT_A --plafond-usd 10 --max-appels 60 \
  --journal "$RA/relais-argon-journal.jsonl" > "$RA/relais-argon.log" 2>&1 &
PID_A=$!
sleep 1
tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais Kimi (R10)" >&2; exit 3; }
tr '\0' ' ' < /proc/$PID_A/cmdline | grep -q "commande_argon_v56_nuit_v1.py servir" || { echo "PID $PID_A n'est pas le relais Argon (R10)" >&2; exit 3; }
echo "relais Kimi PID $PID_K (port $PORT_K) ; relais Argon PID $PID_A (port $PORT_A)"
for p in $PORT_K $PORT_A; do
  i=0; until etat_relais $p > /dev/null; do i=$((i+1)); [ $i -lt 30 ] || { echo "relais du port $p non prêt" >&2; exit 3; }; sleep 1; done
done

# Contrôles (2 appels du devis) : chaîne complète commande -> relais -> interface, modèle servi exact, coût au registre cumulé.
controle() {  # $1 commande  $2 modèle  $3 sortie  $4… options
  local cmd="$1" mod="$2" out="$3"; shift 3
  printf 'Réponds seulement par le mot OK.' | env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$RA" PLAFOND_SESSION_USD=0.05 \
    ROLE_POLE=juge_ideation MODELE_DEMANDE_POLE="$mod" ETAPE_POLE=controle PLAFOND_ETAPE_USD=0.10 \
    "$PY" -I -B "$cmd" "$@" --registre "$REG" --plafond-cumule-usd 10 > "$out" 2>&1 || return 1
  tail -n 1 "$out" | "$PY" -I -c "import json,sys; o=json.loads(sys.stdin.read()); sys.exit(0 if o.get('modele_servi')=='$mod' and o.get('cout_usd',0)>0 else 1)"
}
controle "$N/commande_kimi_v2.py" kimi-k3.1-pro "$RA/controle-kimi.json" --url-relais http://127.0.0.1:$PORT_K \
  --max-sortie-court 4096 --sortie-min-jetons 1024 || { echo "contrôle de Kimi en échec : aucune course" >&2; exit 3; }
controle "$N/commande_argon_v56_nuit_v1.py" gemini-4-argon "$RA/controle-argon.json" appeler --url-relais http://127.0.0.1:$PORT_A \
  --max-sortie-court 1000 --sortie-min-jetons 256 || { echo "contrôle d'Argon en échec : aucune course" >&2; exit 3; }
echo "$(date -u +%FT%TZ) contrôles conformes ; registre : $("$PY" -I -B registre_depense_cumulee_v1.py restant "$REG" 10) USD restants"

code=0
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$RA" GO_ID="$GO_ID" timeout 12600 "$PY" -I -B lancer_mini_course_v1.py lancer \
  --configuration "$CONF" --sortie "$RA/course" --registre-depense "$REG" --registre-go "$REPO/registres/go.md" \
  --confirmer-moteur-reel || code=$?
echo "$(date -u +%FT%TZ) course finie, code $code ; registre : $("$PY" -I -B registre_depense_cumulee_v1.py etat "$REG" | tr -d '\n' | cut -c1-400)"
arreter; trap - EXIT
"$PY" -I -B trace_agregee_mini_course_v1.py --run "$RA" --configuration "$CONF" || { echo "trace agrégée refusée ou illisible" >&2; [ $code -eq 0 ] && code=7; }
for v in GEMINI_API_KEY_2 KIMI_API_KEY; do grep -rqF -- "${!v}" "$RA" 2>/dev/null && { echo "ALERTE : $v trouvée dans une sortie" >&2; code=6; }; done
echo "$(date -u +%FT%TZ) fin, code $code"; exit $code
