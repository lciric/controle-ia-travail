#!/bin/bash
# KIT JANG-FENG, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Jang-Feng (question à une section servie et ses règles d'intégrité, deux pièces servies, trois variantes comme Ibrahim, juge du n° 419, marge d'appels 2 × plan + 5) ; n'accepte que les configurations de ce kit.
# KIT JANG-FENG Q1, LANCEUR SHELL v2 (sous-agent de session-depot, 3 novembre 2026) = lancer-course-jangfeng-v1.sh (gardé, R12) qui n'accepte QUE les trois configurations Jang-Feng v2 (source Gu-Krenn v2, CLI-02 ; max_appels des relais = 2 × plan + 5, CLI-01) ; rien d'autre ne change. Les lignes d'en-tête suivantes sont héritées de la v1 et des kits Kirchner et Heimersheim.
# v2 = lancer-course-jangfeng-v1.sh (gardé, R12) qui n'accepte que les configurations v2 (aiguilleur v2, source Gu-Krenn v2 : contre-lecture CLK-01, CLK-02).
# Lanceur de la course d'idéation Jang-Feng (question 1), v3 = v2 (lancer-course-jangfeng-v1.sh, gardé, R12) qui appelle le
# lanceur Python v2 (garde lexicale CLH-03) et n'accepte que les configurations v2 (pièces v2 de la contre-lecture). La v2 était la v1 dont seul
# change le délai de la course : 43 200 s (12 h) au lieu de 21 600 s. Raison : durée attendue ≈ 5 h (SUPPOSÉ, 322 appels un à
# la fois, durées du second tour réel : médiane 58 s pour Kimi), marge trop mince, et un arrêt par délai ne rend aucune fiche
# (fiches.json n'est écrit qu'en fin de génération). Dérivé de nuit/lancer-mini-course-v2.sh (inchangé).
# Rédigé le 3 novembre 2026 par un sous-agent de session-depot ; jamais lancé de façon payante par son rédacteur (répétitions
# derrière de faux amonts seulement). Course NON décisive (démonstration, matière à réflexion pour Lazar).
# Usage :
#   GO_ID=GO-2026-11-03-NN PY_RELAIS_CLAUDE=/chemin/python-avec-anthropic nohup bash lancer-course-jangfeng-v1.sh lancer \
#     GO-2026-11-03-NN configuration-course-jang-feng-v1-cinq-especes.json /home/user/runs-jangfeng/run-AAAAMMJJ-HHMM \
#     FICHE_DE_LANCEMENT_SCELLEE RAPPORT_DE_CONTRE_LECTURE_SCELLE > RUN.demarrage.log 2>&1 &
#   (mode `repeter` : mêmes arguments, derrière une autorité de certification FACTICE marquée ; REGISTRE_GO et
#   CONFIGURATION_REPETITION — chemin absolu d'une configuration d'artefact — permis en répétition seulement)
# Arguments : mode ; identifiant de GO attendu (comparé à GO_ID de l'environnement) ; nom d'une des trois configurations de ce
# dossier ; dossier du run (NEUF, hors du clone) ; fiche de lancement scellée ; rapport de contre-lecture scellé.
# Variables : GO_ID ; PY_RELAIS_CLAUDE (Python qui porte le SDK anthropic) ; CLE_ANTHROPIC_NOM (NOM de la variable de la clé
# Anthropic, défaut RR_ANTHROPIC_API_KEY_LUC) ; OPENAI_API_KEY ; KIMI_API_KEY si la configuration porte Kimi ; GEMINI_API_KEY_2
# si elle porte Argon ; HTTPS_PROXY, SSL_CERT_FILE. Les clés ne sont jamais affichées ni écrites ni passées en argument d'un
# programme : chaque relais tourne sous env -i avec la SEULE clé qu'il tient (limite dite : la valeur transite par la ligne
# de commande d'env -i jusqu'à son exec, et /proc/<pid>/environ des relais l'expose au même utilisateur) ; l'orchestrateur, les
# commandes, l'agrégateur et les outils ne voient aucune clé ; seule la recherche des clés les hérite (environnement).
# Déroulé : gardes (GO, configuration, dossier neuf hors clone, empreintes de la copie de l'orchestrateur, des commandes A1-bis,
# du relais Kimi, fiche et contre-lecture scellées, vérification Python sans appel ni écriture, pièces gelées comprises) ;
# relais 8806 (Claude : Fable 5.1 et Opus 5.5, --effort high --reflexion adaptative), 8807 (Astra), 8804 (Kimi) et 8805
# (Argon) selon la configuration, PID vérifiés (R10) ; manifeste de départ écrit et scellé AVANT le premier appel ; un appel de
# contrôle par modèle (« Réponds seulement par le mot OK », plafond de session 0,05 USD : code 0, coût > 0, modèle servi =
# modèle demandé ; un contrôle en échec → aucune course) ; course en arrière-plan sous `wait` (signal → SIGTERM à la course,
# KILL 120 s plus tard par timeout) ; relais arrêtés par PID ; sortie scellée (empreintes du run) AVANT toute lecture ; trace
# agrégée, épreuve anti-fuite, recherche des clés.
# Codes : 0 fini ; 2 refus de lancer, ou arrêt de la course (motif au journal) ; 3 relais ou contrôle en échec ; 6 clé trouvée
# dans une sortie ; 7 trace refusée ; 124 délai (12 h) ; 130 signal reçu (manifestes, sceau, trace et recherche des clés faits quand même).
set -uo pipefail; set +x
cd "$(dirname "$0")" || exit 2
H="$PWD"; O="$(cd .. && pwd)"; N="$O/nuit"; REPO="$(cd ../../../.. && pwd)"
A1=$REPO/docs/notes/ideation-organisme-v1/commandes-a1-bis-v1; K=$REPO/docs/notes/ideation-organisme-v1/relais-kimi-v1
MODE="${1:?mode : lancer ou repeter}"; GO_ATTENDU="${2:?identifiant de GO attendu}"; CONF_NOM="${3:?configuration}"
RUN="${4:?dossier du run (neuf, hors clone)}"; P="${5:?fiche de lancement scellée}"; C="${6:?rapport de contre-lecture scellé}"
GO_ID="${GO_ID:?GO_ID absent}"; CLE_ANTHROPIC_NOM="${CLE_ANTHROPIC_NOM:-RR_ANTHROPIC_API_KEY_LUC}"
PY_RELAIS_CLAUDE="${PY_RELAIS_CLAUDE:?PY_RELAIS_CLAUDE absent (Python qui porte le SDK anthropic)}"
REG_GO="$REPO/registres/go.md"
case "$MODE" in
  lancer) [ -z "${REGISTRE_GO:-}${CONFIGURATION_REPETITION:-}" ] || { echo "REGISTRE_GO et CONFIGURATION_REPETITION ne sont permis qu'en répétition" >&2; exit 2; } ;;
  repeter) [ -n "${SSL_CERT_FILE:-}" ] && [ -f "$(dirname "$SSL_CERT_FILE")/AUTORITE-FACTICE-DE-REPETITION" ] \
             || { echo "repeter : SSL_CERT_FILE doit être l'autorité FACTICE marquée de la répétition" >&2; exit 2; }
           REG_GO="${REGISTRE_GO:-$REG_GO}" ;;
  *) echo "mode : lancer ou repeter" >&2; exit 2 ;;
esac
[[ "$GO_ATTENDU" =~ ^GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]] || { echo "identifiant de GO attendu mal formé : $GO_ATTENDU" >&2; exit 2; }
[ "$GO_ID" = "$GO_ATTENDU" ] || { echo "la course ne court que sous $GO_ATTENDU (GO_ID reçu : $GO_ID)" >&2; exit 2; }
grep -q "^| $GO_ID |" "$REG_GO" || { echo "$GO_ID absent de $REG_GO" >&2; exit 2; }
case "$CONF_NOM" in
  configuration-course-jang-feng-v1-sans-kimi.json|configuration-course-jang-feng-v1-avec-kimi.json|configuration-course-jang-feng-v1-cinq-especes.json) ;;
  *) echo "configuration inconnue : $CONF_NOM (une des trois de $H)" >&2; exit 2 ;;
esac
CONF="$H/$CONF_NOM"
if [ "$MODE" = "repeter" ] && [ -n "${CONFIGURATION_REPETITION:-}" ]; then  # répétition seulement : configuration mutée (artefact)
  case "$CONFIGURATION_REPETITION" in /*) ;; *) echo "CONFIGURATION_REPETITION : chemin absolu exigé" >&2; exit 2 ;; esac
  [ -f "$CONFIGURATION_REPETITION" ] || { echo "CONFIGURATION_REPETITION absente" >&2; exit 2; }
  CONF="$CONFIGURATION_REPETITION"
fi
[ ! -e "$RUN" ] || { echo "$RUN existe déjà (R12)" >&2; exit 2; }
PARENT="$(cd "$(dirname "$RUN")" 2>/dev/null && pwd -P)" || { echo "dossier parent du run absent : $(dirname "$RUN")" >&2; exit 2; }
for interdit in "$(cd "$REPO" && pwd -P)" /home/user/controle-ia-travail; do
  case "$PARENT/" in "$interdit"/*) echo "le dossier du run doit être hors du clone ($interdit)" >&2; exit 2 ;; esac
done
mkdir "$RUN" || exit 2
RA="$PARENT/$(basename "$RUN")"
exec >>"$RA/journal-lancement-course-jangfeng-v1.log" 2>&1
echo "$(date -u +%FT%TZ) début ; mode $MODE ; GO $GO_ID ; configuration $CONF_NOM ; run $RA ; PID du lanceur $$"
[ "$MODE" = "repeter" ] && echo "RÉPÉTITION : autorité factice $SSL_CERT_FILE ; registre des GO $REG_GO ; fiche $P"

PY=/usr/bin/python3; E=(env -i PATH=/usr/bin:/bin LANG=C.UTF-8)
"${E[@]}" "$PY" -I -c "import numpy" 2>/dev/null || { echo "Python des appels absent ou sans numpy : $PY" >&2; exit 2; }
"${E[@]}" "$PY_RELAIS_CLAUDE" -I -c "import anthropic" 2>/dev/null || { echo "PY_RELAIS_CLAUDE sans le SDK anthropic : $PY_RELAIS_CLAUDE" >&2; exit 2; }
FOURS="$("${E[@]}" "$PY" -I -c "import json,sys; print(' '.join(sorted(json.load(open(sys.argv[1]))['relais'])))" "$CONF")" \
  || { echo "configuration illisible : $CONF" >&2; exit 2; }
a() { case " $FOURS " in *" $1 "*) return 0 ;; esac; return 1; }
relais_param() { "${E[@]}" "$PY" -I -c "import json,sys; r=json.load(open(sys.argv[1]))['relais'][sys.argv[2]]; print(r[sys.argv[3]])" "$CONF" "$1" "$2"; }
S17="$("${E[@]}" "$PY" -I -c "import json,sys; print('%g' % json.load(open(sys.argv[1]))['budget']['plafond_usd'])" "$CONF")"
echo "fournisseurs : $FOURS ; S17 (plafond technique) $S17 USD"
[ -n "${!CLE_ANTHROPIC_NOM:-}" ] || { echo "$CLE_ANTHROPIC_NOM absente" >&2; exit 2; }
[ -n "${OPENAI_API_KEY:-}" ] || { echo "OPENAI_API_KEY absente" >&2; exit 2; }
CLES=("$CLE_ANTHROPIC_NOM" OPENAI_API_KEY)
if a kimi; then [ -n "${KIMI_API_KEY:-}" ] || { echo "KIMI_API_KEY absente" >&2; exit 2; }; CLES+=(KIMI_API_KEY); fi
if a argon; then [ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }; CLES+=(GEMINI_API_KEY_2); fi
(cd "$O" && sha256sum -c --quiet jangfeng/EMPREINTES-orchestrateur-course-jang-feng-v1.txt) \
  || { echo "copie de l'orchestrateur v56 modifiée" >&2; exit 2; }
(cd "$A1" && sha256sum -c --quiet EMPREINTES-commandes-a1-bis-v1.txt) || { echo "commandes A1-bis non conformes" >&2; exit 2; }
if a kimi; then (cd "$K" && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }; fi
if a argon; then (cd "$H/argon" && sha256sum -c --quiet collisionneur_v7.py.sha256) || { echo "collisionneur v7 non conforme" >&2; exit 2; }; fi
for f in "$P" "$C"; do (cd "$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") \
  || { echo "$f absent, non scellé ou modifié (R1, R2) : aucun lancement" >&2; exit 2; }; done
"${E[@]}" HOME="$RA" GO_ID="$GO_ID" "$PY" -I -B lancer_course_jangfeng_v1.py verifier --configuration "$CONF" --registre-go "$REG_GO" \
  --go-attendu "$GO_ATTENDU" --preenregistrement "$P" --contre-lecture "$C" > "$RA/verification-avant-lancement.json" \
  || { echo "vérification refusée (motif ci-dessus)" >&2; exit 2; }

REG="$RA/registre-depense-cumulee-v1.jsonl"
declare -A PORT=([claude]=8806 [astra]=8807 [kimi]=8804 [argon]=8805) PIDR=()
PID_C=""; SIGNAL=""
arreter_pid() { local p="$1" i=0; [ -n "$p" ] || return 0; kill "$p" 2>/dev/null; while kill -0 "$p" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done; kill -0 "$p" 2>/dev/null && kill -9 "$p" 2>/dev/null; true; }
etat_relais() { "${E[@]}" "$PY" -I -c "import urllib.request,sys; o=urllib.request.build_opener(urllib.request.ProxyHandler({})); sys.stdout.write(o.open('http://127.0.0.1:$1/relais/etat', timeout=5).read().decode())" 2>/dev/null; }
arreter_relais() {
  local f
  for f in "${!PIDR[@]}"; do etat_relais "${PORT[$f]}" > "$RA/etat-final-relais-$f.json"; arreter_pid "${PIDR[$f]}"; echo "$(date -u +%FT%TZ) relais $f arrêté (PID ${PIDR[$f]})"; unset "PIDR[$f]"; done
}
sur_signal() { SIGNAL="$1"; echo "$(date -u +%FT%TZ) signal $1 reçu"
  if [ -n "$PID_C" ] && kill -0 "$PID_C" 2>/dev/null; then kill -TERM "$PID_C" 2>/dev/null; echo "SIGTERM envoyé à la course (PID $PID_C)"; fi; }
sortie_imprevue() { [ -n "$PID_C" ] && kill -0 "$PID_C" 2>/dev/null && kill -TERM "$PID_C" 2>/dev/null; arreter_relais; }
trap sortie_imprevue EXIT; trap 'sur_signal TERM' TERM; trap 'sur_signal INT' INT; trap 'sur_signal HUP' HUP
for f in $FOURS; do
  "${E[@]}" "$PY" -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',${PORT[$f]})) else 1)" \
    || { echo "port ${PORT[$f]} déjà pris : aucun lancement (jamais toucher au relais d'une autre course)" >&2; exit 2; }
done
MANDATAIRE=(HTTPS_PROXY="${HTTPS_PROXY:-}")  # urllib : une variable de mandataire VIDE en annule une autre ; seules les posées passent
for v in https_proxy NO_PROXY no_proxy; do [ -n "${!v:-}" ] && MANDATAIRE+=("$v=${!v}"); done
CA="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}"
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 ANTHROPIC_API_KEY="${!CLE_ANTHROPIC_NOM}" "${MANDATAIRE[@]}" SSL_CERT_FILE="$CA" \
  "$PY_RELAIS_CLAUDE" -I -B "$A1/commande_claude_a1bis_v1.py" servir --port 8806 --plafond-usd "$(relais_param claude plafond_usd)" \
  --max-appels "$(relais_param claude max_appels)" --journal "$RA/relais-claude-journal.jsonl" \
  --modeles-permis claude-fable-5-1,claude-opus-5-5 --effort high --reflexion adaptative > "$RA/relais-claude.log" 2>&1 &
PIDR[claude]=$!
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 OPENAI_API_KEY="$OPENAI_API_KEY" "${MANDATAIRE[@]}" SSL_CERT_FILE="$CA" \
  "$PY" -I -B "$A1/commande_astra_a1bis_v1.py" servir --port 8807 --plafond-usd "$(relais_param astra plafond_usd)" \
  --max-appels "$(relais_param astra max_appels)" --journal "$RA/relais-astra-journal.jsonl" --modeles-permis gpt-6-astra \
  > "$RA/relais-astra.log" 2>&1 &
PIDR[astra]=$!
if a kimi; then
  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE="$CA" \
    "$PY" -I -B "$K/relais_kimi_v3.py" --port 8804 --modeles-permis kimi-k3.1-pro --plafond-usd "$(relais_param kimi plafond_usd)" \
    --reserve-par-appel 0.05 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels "$(relais_param kimi max_appels)" \
    --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1700 --delai-silence-s 600 --journal "$RA/relais-kimi-journal.jsonl" \
    > "$RA/relais-kimi.log" 2>&1 &
  PIDR[kimi]=$!
fi
if a argon; then
  env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" "${MANDATAIRE[@]}" SSL_CERT_FILE="$CA" \
    "$PY" -I -B "$N/commande_argon_v56_nuit_v2.py" servir --port 8805 --plafond-usd "$(relais_param argon plafond_usd)" \
    --max-appels "$(relais_param argon max_appels)" --journal "$RA/relais-argon-journal.jsonl" \
    --collisionneur "$H/argon/collisionneur_v7.py" > "$RA/relais-argon.log" 2>&1 &
  PIDR[argon]=$!
fi
sleep 1
declare -A SIGNE=([claude]="commande_claude_a1bis_v1.py servir" [astra]="commande_astra_a1bis_v1.py servir" [kimi]="relais_kimi_v3.py" [argon]="commande_argon_v56_nuit_v2.py servir")
for f in "${!PIDR[@]}"; do
  tr '\0' ' ' < "/proc/${PIDR[$f]}/cmdline" 2>/dev/null | grep -q "${SIGNE[$f]}" || { echo "PID ${PIDR[$f]} n'est pas le relais $f (R10)" >&2; exit 3; }
  i=0; until etat_relais "${PORT[$f]}" > /dev/null; do i=$((i+1)); [ $i -lt 30 ] || { echo "relais $f (port ${PORT[$f]}) non prêt" >&2; exit 3; }; sleep 1; done
  echo "relais $f PID ${PIDR[$f]} (port ${PORT[$f]}, plafond $(relais_param "$f" plafond_usd) USD, $(relais_param "$f" max_appels) appels au plus)"
done
MODELES="claude-fable-5-1 claude-opus-5-5 gpt-6-astra"; a kimi && MODELES+=" kimi-k3.1-pro"; a argon && MODELES+=" gemini-4-argon"
"${E[@]}" "$PY" -I -B - "$RA/manifeste-depart-lanceur-jangfeng-v1.json" "$O" <<EOF || { echo "manifeste de départ non écrit : aucun appel" >&2; exit 2; }
import hashlib, json, sys
sys.path.insert(0, sys.argv[2])
from pole.outils import ecrire_json_scelle
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
ecrire_json_scelle(sys.argv[1], {"version": "lanceur-shell-course-jangfeng-v1", "mode": "$MODE", "go": "$GO_ID",
    "configuration": "$CONF_NOM", "configuration_sha256": sha("$CONF"), "fiche_de_lancement": "$P", "fiche_sha256": sha("$P"),
    "contre_lecture": "$C", "contre_lecture_sha256": sha("$C"), "run": "$RA", "fournisseurs": "$FOURS".split(),
    "relais": {f: {"pid": int(p)} for f, p in zip("${!PIDR[*]}".split(), "${PIDR[*]}".split())},
    "modeles_controles": "$MODELES".split(), "plafond_technique_usd": float("$S17"), "temoins_plantes": "aucun",
    "regle": "écrit et scellé avant le premier appel (contrôles compris)"})
EOF
echo "$(date -u +%FT%TZ) manifeste de départ scellé : $RA/manifeste-depart-lanceur-jangfeng-v1.json"

controle() {  # $1 modèle ; $2 sortie ; puis la commande et ses options
  local mod="$1" out="$2"; shift 2
  printf 'Réponds seulement par le mot OK.' | env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$RA" PLAFOND_SESSION_USD=0.05 \
    ROLE_POLE=juge_ideation MODELE_DEMANDE_POLE="$mod" ETAPE_POLE=controle PLAFOND_ETAPE_USD=0.30 \
    "$PY" -I -B "$@" --registre "$REG" --plafond-cumule-usd "$S17" > "$out" 2>&1 || return 1
  tail -n 1 "$out" | "${E[@]}" "$PY" -I -c "import json,sys; o=json.loads(sys.stdin.read()); sys.exit(0 if o.get('modele_servi')=='$mod' and o.get('cout_usd',0)>0 and str(o.get('texte') or '').strip() else 1)"
}
code=0
for mod in $MODELES; do
  [ $code -eq 0 ] && [ -z "$SIGNAL" ] || break
  case "$mod" in
    claude-*) controle "$mod" "$RA/controle-$mod.json" "$H/commande_claude_jangfeng_v1.py" --url-relais http://127.0.0.1:8806 \
                --max-sortie-proposeur 64000 --max-sortie-court 16000 --sortie-min-jetons 256 --delai-s 600 --effort high --reflexion adaptative ;;
    gpt-6-astra) controle "$mod" "$RA/controle-$mod.json" "$A1/commande_astra_a1bis_v1.py" appeler --modele gpt-6-astra \
                --url-relais http://127.0.0.1:8807 --max-sortie-proposeur 32000 --max-sortie-court 16000 --sortie-min-jetons 256 --delai-s 600 ;;
    kimi-k3.1-pro) controle "$mod" "$RA/controle-$mod.json" "$N/commande_kimi_v2.py" --url-relais http://127.0.0.1:8804 \
                --max-sortie-court 4096 --sortie-min-jetons 1024 ;;
    gemini-4-argon) controle "$mod" "$RA/controle-$mod.json" "$N/commande_argon_v56_nuit_v2.py" appeler --url-relais http://127.0.0.1:8805 \
                --max-sortie-court 1000 --sortie-min-jetons 256 ;;
  esac || { echo "contrôle de $mod en échec : aucune course" >&2; code=3; }
done
if [ $code -eq 0 ] && [ -z "$SIGNAL" ]; then
  echo "$(date -u +%FT%TZ) contrôles conformes ($MODELES) ; registre : $("${E[@]}" "$PY" -I -B "$N/registre_depense_cumulee_v1.py" restant "$REG" "$S17") USD restants"
  "${E[@]}" HOME="$RA" GO_ID="$GO_ID" timeout -k 120 43200 "$PY" -I -B lancer_course_jangfeng_v1.py lancer \
    --configuration "$CONF" --sortie "$RA/course" --registre-depense "$REG" --registre-go "$REG_GO" --go-attendu "$GO_ATTENDU" \
    --confirmer-moteur-reel --preenregistrement "$P" --contre-lecture "$C" &
  PID_C=$!
  echo "$(date -u +%FT%TZ) course lancée en arrière-plan, PID $PID_C (timeout, puis le Python)"
  while :; do wait "$PID_C"; rc=$?; kill -0 "$PID_C" 2>/dev/null && continue; code=$rc; break; done
  PID_C=""
  echo "$(date -u +%FT%TZ) course finie, code $code ; registre : $("${E[@]}" "$PY" -I -B "$N/registre_depense_cumulee_v1.py" etat "$REG" | tr -d '\n' | cut -c1-400)"
elif [ -n "$SIGNAL" ]; then echo "signal reçu avant la course : aucune course"; fi
arreter_relais; trap - EXIT
(cd "$RA" && find . -type f ! -name 'journal-lancement-course-jangfeng-v1.log' ! -name 'empreintes-run-jangfeng-v1.txt*' -print0 \
  | sort -z | xargs -0 -r sha256sum > empreintes-run-jangfeng-v1.txt && sha256sum empreintes-run-jangfeng-v1.txt > empreintes-run-jangfeng-v1.txt.sha256) \
  && echo "$(date -u +%FT%TZ) sortie scellée avant toute lecture : $(wc -l < "$RA/empreintes-run-jangfeng-v1.txt") fichiers (empreintes-run-jangfeng-v1.txt)" \
  || { echo "sceau de la sortie en échec" >&2; [ $code -eq 0 ] && code=7; }
if [ -d "$RA/course" ]; then
  "${E[@]}" "$PY" -I -B "$H/trace_agregee_course_jangfeng_v1.py" --run "$RA" --configuration "$CONF" || { echo "trace agrégée refusée ou illisible" >&2; [ $code -eq 0 ] && code=7; }
  echo "épreuve anti-fuite sur le run : $("${E[@]}" "$PY" -I -B "$H/trace_agregee_course_jangfeng_v1.py" --run "$RA" --configuration "$CONF" --artefacts-sur-run 2>&1)"
fi
"$PY" -I -B "$N/chercher_cles_v1.py" "$RA" "${CLES[@]}" || code=6
[ -n "$SIGNAL" ] && [ $code -ne 6 ] && code=130
echo "$(date -u +%FT%TZ) fin, code $code"; exit $code
