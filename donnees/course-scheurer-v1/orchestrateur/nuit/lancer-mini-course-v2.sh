#!/bin/bash
# Lanceur de la mini-course d'idéation, Kimi et Argon seuls (GO-2026-11-01-12, plafond 10 USD au barème supposé, devis scénario B), v2.
# Rédigé le 1er novembre 2026 par un sous-agent de session-depot ; jamais lancé de façon payante par son rédacteur (répétitions devant des
# amonts factices seulement). Version 2 = lancer-mini-course-v1.sh (inchangé, R12) avec les corrections de la contre-lecture
# (docs/notes/mini-course-kimi-argon-v1/contre-lecture-mini-course-kimi-argon-v1.md) :
#  CLM-01 : la course tourne en arrière-plan sous `wait` ; un signal (TERM, INT, HUP) arrête la course par son PID (timeout relaie le
#           signal au Python, qui lève ArretParSignal ; KILL 120 s plus tard s'il ne sort pas), puis les relais par leur PID ; l'agrégateur,
#           l'épreuve sur le run et la recherche des clés tournent quand même ; code 130 ensuite ;
#  CLM-04 : rapport de contre-lecture au nom réel (contre-lecture-mini-course-kimi-argon-v1.md) ; préenregistrement v2 ;
#  CLM-05 : plafonds des relais 3 USD (Kimi) et 7 USD (Argon), somme 10 ;
#  CLM-06 : clés cherchées par chercher_cles_v1.py (valeurs lues dans son environnement, jamais en argument) ; outils sous env -i ;
#  CLM-07 : épreuve anti-fuite sur le run réel (--artefacts-sur-run), sortie au journal ;
#  répétition v2 : mandataire en minuscules (https_proxy, no_proxy) transmis seulement s'il est posé (un `https_proxy=` vide
#           annulait HTTPS_PROXY pour urllib, donc pour appeler_gemini) ; commande d'Argon v2 et configuration v2 ;
#  mode `repeter` : même chaîne, spécification de répétition donnée en argument, exigé derrière une autorité de certification FACTICE
#           marquée (SSL_CERT_FILE à côté du fichier AUTORITE-FACTICE-DE-REPETITION) : aucune connexion TLS réelle ne peut aboutir.
# Usage :
#   GO_ID=GO-2026-11-01-12 nohup bash lancer-mini-course-v2.sh lancer /home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/run-AAAAMMJJ-HHMM >RUN.demarrage.log 2>&1 &
#   GO_ID=GO-2026-11-01-12 bash lancer-mini-course-v2.sh repeter RUN PREREG_REPETITION CONTRE_LECTURE_REPETITION
# Clés : GEMINI_API_KEY_2 donnée au seul relais Argon (servir, sous le nom GEMINI_API_KEY lu par appeler_gemini), KIMI_API_KEY au seul relais
# Kimi (relais_kimi_v3.py) ; les deux sous env -i, PID vérifiés (R10). L'orchestrateur, les commandes, l'agrégateur et les outils ne voient
# aucune clé ; seule la recherche des clés les hérite (environnement, pas ligne de commande). Limite dite : les clés transitent par la
# ligne de commande d'env -i des deux relais jusqu'à son exec, et /proc/<pid>/environ des relais les expose au même utilisateur. Sans set -e.
# Garantie : 10 USD au plus AU BARÈME SUPPOSÉ d'Argon (10 et 50 USD par million), si chaque appel coûte moins que son pire cas (entrée
# d'Argon <= caractères / 3 jetons, réflexion bornée par maxOutputTokens : SUPPOSÉ) ; un dépassement de réserve arrête la course ; facture
# réelle à relire au tableau de bord de chaque fournisseur.
# Codes : 0 fini ; 2 refus de lancer, ou arrêt de la course (motif au journal) ; 3 relais ou contrôle en échec ; 6 clé trouvée dans une
# sortie ; 7 trace refusée ; 124 délai ; 130 signal reçu (manifestes, trace et recherche des clés faits quand même).
set -uo pipefail; set +x
cd "$(dirname "$0")" || exit 2
N="$PWD"; REPO=/home/user/controle-ia-travail; DP=$REPO/docs/notes/mini-course-kimi-argon-v1
GO_ID="${GO_ID:?GO_ID absent}"; MODE="${1:?mode : lancer ou repeter}"; RUN="${2:?dossier du run (neuf, sous donnees/)}"
case "$MODE" in
  lancer) P=$DP/preregistrement-mini-course-kimi-argon-v2.md; C=$DP/contre-lecture-mini-course-kimi-argon-v1.md ;;
  repeter) P="${3:?préenregistrement de répétition}"; C="${4:?contre-lecture de répétition}"
           [ -n "${SSL_CERT_FILE:-}" ] && [ -f "$(dirname "$SSL_CERT_FILE")/AUTORITE-FACTICE-DE-REPETITION" ] \
             || { echo "repeter : SSL_CERT_FILE doit être l'autorité FACTICE marquée de la répétition" >&2; exit 2; } ;;
  *) echo "mode : lancer ou repeter" >&2; exit 2 ;;
esac
[ "$GO_ID" = "GO-2026-11-01-12" ] || { echo "la mini-course ne court que sous GO-2026-11-01-12" >&2; exit 2; }
grep -q "^| $GO_ID |" "$REPO/registres/go.md" || { echo "$GO_ID absent de registres/go.md" >&2; exit 2; }
case "$RUN" in "$REPO"/donnees/*) ;; *) echo "le dossier du run doit être sous $REPO/donnees/ (exclu de la copie publique)" >&2; exit 2 ;; esac
[ ! -e "$RUN" ] || { echo "$RUN existe déjà (R12)" >&2; exit 2; }
mkdir -p "$RUN" || exit 2
RA="$(cd "$RUN" && pwd)"
exec >>"$RA/journal-lancement-mini-course-v2.log" 2>&1
echo "$(date -u +%FT%TZ) début ; mode $MODE ; GO $GO_ID ; run $RA ; PID du lanceur $$"
[ "$MODE" = "repeter" ] && echo "RÉPÉTITION : autorité factice $SSL_CERT_FILE ; spécification $P"

PY=/usr/bin/python3; E=(env -i PATH=/usr/bin:/bin LANG=C.UTF-8)
[ -x "$PY" ] && "${E[@]}" "$PY" -I -c "import numpy" 2>/dev/null || { echo "Python des appels absent ou sans numpy : $PY" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ -n "${KIMI_API_KEY:-}" ] || { echo "KIMI_API_KEY absente" >&2; exit 2; }
K=$REPO/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd "$K" && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
(cd "$REPO/donnees/espece-seule-v1" && sha256sum -c --quiet collisionneur_v7.py.sha256) || { echo "collisionneur v7 non conforme" >&2; exit 2; }
(cd "$N/.." && sha256sum -c --quiet nuit/EMPREINTES-orchestrateur-v56-copie-v1.txt) \
  || { echo "copie de l'orchestrateur v56 modifiée (archive 29b1b38c…)" >&2; exit 2; }
for f in "$P" "$C"; do (cd "$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") \
  || { echo "$f absent, non scellé ou modifié (R1, R2) : aucun lancement" >&2; exit 2; }; done
CONF=$N/configuration-mini-course-kimi-argon-v2.json
"${E[@]}" HOME="$RA" GO_ID="$GO_ID" "$PY" -I -B lancer_mini_course_v2.py verifier --configuration "$CONF" \
  --registre-go "$REPO/registres/go.md" > "$RA/verification-avant-lancement.json" || { echo "vérification refusée" >&2; exit 2; }

REG="$RA/registre-depense-cumulee-v1.jsonl"
PORT_K=8804; PORT_A=8805; PID_K=""; PID_A=""; PID_C=""; SIGNAL=""
arreter_pid() { local p="$1" i=0; [ -n "$p" ] || return 0; kill "$p" 2>/dev/null; while kill -0 "$p" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done; kill -0 "$p" 2>/dev/null && kill -9 "$p" 2>/dev/null; true; }
etat_relais() { "${E[@]}" "$PY" -I -c "import urllib.request,sys; o=urllib.request.build_opener(urllib.request.ProxyHandler({})); sys.stdout.write(o.open('http://127.0.0.1:$1/relais/etat', timeout=5).read().decode())" 2>/dev/null; }
arreter_relais() { [ -n "$PID_K" ] && etat_relais $PORT_K > "$RA/etat-final-relais-kimi.json"; [ -n "$PID_A" ] && etat_relais $PORT_A > "$RA/etat-final-relais-argon.json"; arreter_pid "$PID_K"; arreter_pid "$PID_A"; [ -n "$PID_K$PID_A" ] && echo "$(date -u +%FT%TZ) relais arrêtés (PID ${PID_K:-—} et ${PID_A:-—})"; PID_K=""; PID_A=""; }
sur_signal() {  # CLM-01 : arrêt de la course par son PID ; la suite du script (relais, trace, clés) s'exécute ensuite
  SIGNAL="$1"; echo "$(date -u +%FT%TZ) signal $1 reçu"
  if [ -n "$PID_C" ] && kill -0 "$PID_C" 2>/dev/null; then kill -TERM "$PID_C" 2>/dev/null; echo "SIGTERM envoyé à la course (PID $PID_C)"; fi
}
sortie_imprevue() { [ -n "$PID_C" ] && kill -0 "$PID_C" 2>/dev/null && kill -TERM "$PID_C" 2>/dev/null; arreter_relais; }
trap sortie_imprevue EXIT; trap 'sur_signal TERM' TERM; trap 'sur_signal INT' INT; trap 'sur_signal HUP' HUP
for p in $PORT_K $PORT_A; do
  "${E[@]}" "$PY" -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$p)) else 1)" || { echo "port $p déjà pris" >&2; exit 2; }
done
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" \
  "$PY" -I -B "$K/relais_kimi_v3.py" --port $PORT_K --modeles-permis kimi-k3.1-pro --plafond-usd 3 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 40 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1700 \
  --delai-silence-s 600 --journal "$RA/relais-kimi-journal.jsonl" > "$RA/relais-kimi.log" 2>&1 &
PID_K=$!
MANDATAIRE_A=(HTTPS_PROXY="${HTTPS_PROXY:-}")  # urllib : une variable de mandataire VIDE en annule une autre ; seules les posées passent
for v in https_proxy NO_PROXY no_proxy; do [ -n "${!v:-}" ] && MANDATAIRE_A+=("$v=${!v}"); done
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" "${MANDATAIRE_A[@]}" \
  SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" \
  "$PY" -I -B "$N/commande_argon_v56_nuit_v2.py" servir --port $PORT_A --plafond-usd 7 --max-appels 60 \
  --journal "$RA/relais-argon-journal.jsonl" > "$RA/relais-argon.log" 2>&1 &
PID_A=$!
sleep 1
tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais Kimi (R10)" >&2; exit 3; }
tr '\0' ' ' < /proc/$PID_A/cmdline | grep -q "commande_argon_v56_nuit_v2.py servir" || { echo "PID $PID_A n'est pas le relais Argon (R10)" >&2; exit 3; }
echo "relais Kimi PID $PID_K (port $PORT_K, plafond 3 USD) ; relais Argon PID $PID_A (port $PORT_A, plafond 7 USD)"
for p in $PORT_K $PORT_A; do
  i=0; until etat_relais $p > /dev/null; do i=$((i+1)); [ $i -lt 30 ] || { echo "relais du port $p non prêt" >&2; exit 3; }; sleep 1; done
done

controle() {  # $1 commande  $2 modèle  $3 sortie  $4… options
  local cmd="$1" mod="$2" out="$3"; shift 3
  printf 'Réponds seulement par le mot OK.' | env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$RA" PLAFOND_SESSION_USD=0.05 \
    ROLE_POLE=juge_ideation MODELE_DEMANDE_POLE="$mod" ETAPE_POLE=controle PLAFOND_ETAPE_USD=0.10 \
    "$PY" -I -B "$cmd" "$@" --registre "$REG" --plafond-cumule-usd 10 > "$out" 2>&1 || return 1
  tail -n 1 "$out" | "${E[@]}" "$PY" -I -c "import json,sys; o=json.loads(sys.stdin.read()); sys.exit(0 if o.get('modele_servi')=='$mod' and o.get('cout_usd',0)>0 else 1)"
}
code=0
controle "$N/commande_kimi_v2.py" kimi-k3.1-pro "$RA/controle-kimi.json" --url-relais http://127.0.0.1:$PORT_K \
  --max-sortie-court 4096 --sortie-min-jetons 1024 || { echo "contrôle de Kimi en échec : aucune course" >&2; code=3; }
[ $code -eq 0 ] && { controle "$N/commande_argon_v56_nuit_v2.py" gemini-4-argon "$RA/controle-argon.json" appeler \
  --url-relais http://127.0.0.1:$PORT_A --max-sortie-court 1000 --sortie-min-jetons 256 || { echo "contrôle d'Argon en échec : aucune course" >&2; code=3; }; }
if [ $code -eq 0 ] && [ -z "$SIGNAL" ]; then
  echo "$(date -u +%FT%TZ) contrôles conformes ; registre : $("${E[@]}" "$PY" -I -B registre_depense_cumulee_v1.py restant "$REG" 10) USD restants"
  "${E[@]}" HOME="$RA" GO_ID="$GO_ID" timeout -k 120 12600 "$PY" -I -B lancer_mini_course_v2.py lancer \
    --configuration "$CONF" --sortie "$RA/course" --registre-depense "$REG" --registre-go "$REPO/registres/go.md" \
    --confirmer-moteur-reel --preenregistrement "$P" --contre-lecture "$C" &
  PID_C=$!
  echo "$(date -u +%FT%TZ) course lancée en arrière-plan, PID $PID_C (timeout, puis le Python)"
  while :; do wait "$PID_C"; rc=$?; kill -0 "$PID_C" 2>/dev/null && continue; code=$rc; break; done
  PID_C=""
  echo "$(date -u +%FT%TZ) course finie, code $code ; registre : $("${E[@]}" "$PY" -I -B registre_depense_cumulee_v1.py etat "$REG" | tr -d '\n' | cut -c1-400)"
elif [ -n "$SIGNAL" ]; then echo "signal reçu avant la course : aucune course"; fi
arreter_relais; trap - EXIT
if [ -d "$RA/course" ] || [ -f "$RA/manifeste-lancement-nuit-v2.json" ]; then
  "${E[@]}" "$PY" -I -B trace_agregee_mini_course_v2.py --run "$RA" --configuration "$CONF" || { echo "trace agrégée refusée ou illisible" >&2; [ $code -eq 0 ] && code=7; }
  echo "épreuve anti-fuite sur le run (CLM-07) : $("${E[@]}" "$PY" -I -B trace_agregee_mini_course_v2.py --run "$RA" --configuration "$CONF" --artefacts-sur-run 2>&1)"
fi
"$PY" -I -B chercher_cles_v1.py "$RA" GEMINI_API_KEY_2 KIMI_API_KEY || code=6
[ -n "$SIGNAL" ] && [ $code -ne 6 ] && code=130
echo "$(date -u +%FT%TZ) fin, code $code"; exit $code
