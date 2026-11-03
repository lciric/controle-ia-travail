#!/bin/bash
# Suite du tour v9 (GO-2026-11-02-31, option (b) de Lazar, « kimi rechargé ») : joue seulement E3-T3-reponse-D (Kimi, essai 2) et
# E3-T3-reponse-E (Astra, essai 1) du run run-brainstorm-e3-v1, sur la copie du dossier scellé (ac25c055). Lanceur de suite v1
# (3 novembre 2026, session fille ; ordre `docs/procedures/ordre-fille-collisionneur-v9-suite-v1.md`, 9be11cba…) : copie de
# lancer-tour-brainstorm-v9-v1.sh (2fd85687…, branche 9edaeb26), seuls changements : le run doit exister ; Python du collisionneur
# lu dans PY_COLLISIONNEUR (exigé, avec anthropic) ; tous les compagnons de la copie vérifiés ; barrage (a) (barrage_suite_v1.py)
# avant le contrôle ; contrôle v11 sur D et E vers controle-brainstorm-v1-suite.json ; journaux du relais Kimi au suffixe -suite-v1
# (--plafond-usd 3, --max-appels 4) ; barrage (b) : GEMINI_API_KEY et ANTHROPIC_API_KEY factices dans ENVI (seules KIMI_API_KEY et
# OPENAI_API_KEY sont exigées) ; présence des clés vérifiée après les gardes de structure ; avant la suite, empreintes de journal.jsonl
# et etat.md dans avant-suite-v1.txt (scellé), puis retrait de leurs deux seuls compagnons. Clés par nom sous env -i ; jamais en argument.
set -uo pipefail; set +x
cd "$(dirname "$0")"
GO_ID="${GO_ID:?GO_ID absent : un GO de registres/go.md avec le mot direct de Lazar est requis}"
PORT=8802
RUN=run-brainstorm-e3-v1
PLAFOND="${PLAFOND_USD:?PLAFOND_USD absent : le plafond de la ligne de GO est requis}"
PY="${PY_COLLISIONNEUR:?PY_COLLISIONNEUR absent : le Python du collisionneur (avec anthropic) est requis}"
FACTICE=INTERDIT-SUITE-V1
[ -d "$RUN" ] && [ -f "$RUN/journal.jsonl" ] || { echo "$RUN absent : la suite reprend un run existant" >&2; exit 2; }
for f in controle-brainstorm-v1-suite.json avant-suite-v1.txt relais-kimi-brainstorm-journal-suite-v1.jsonl relais-kimi-brainstorm-suite-v1.log; do
  [ ! -e "$f" ] || { echo "$f existe déjà (R12)" >&2; exit 2; }; done
mauvais=0; while IFS= read -r c; do (cd "$(dirname "$c")" && sha256sum -c --quiet "$(basename "$c")" >/dev/null 2>&1) || { echo "compagnon non conforme : $c" >&2; mauvais=1; }
  done < <(find . -name '*.sha256' -type f | sort)
[ $mauvais -eq 0 ] || { echo "empreintes de la copie non conformes" >&2; exit 2; }
for f in question.md faits.md balayage-faits.txt collisionneur_v9.py appel_controle_v11.py barrage_suite_v1.py "$RUN/journal.jsonl" "$RUN/etat.md"; do
  [ -f "$f.sha256" ] || { echo "$f sans compagnon" >&2; exit 2; }; done
grep -q "^$GO_ID " /home/user/controle-ia-travail/registres/go.md || grep -q "| $GO_ID |" /home/user/controle-ia-travail/registres/go.md || { echo "$GO_ID absent de registres/go.md" >&2; exit 2; }
K=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd $K && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
[ -x "$PY" ] && "$PY" -I -c "import anthropic" 2>/dev/null || { echo "python du collisionneur absent ou sans anthropic" >&2; exit 2; }
# barrage (a) : 13 cellules valides, seules non valides E3-T3-reponse-D et E3-T3-reponse-E ; sans appel ni écriture
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B barrage_suite_v1.py collisionneur_v9.py "$RUN" || { echo "barrage (a) : refus" >&2; exit 2; }
for v in KIMI_API_KEY OPENAI_API_KEY; do [ -n "${!v:-}" ] || { echo "$v absente" >&2; exit 2; }; done
python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$PORT)) else 1)" || { echo "port $PORT déjà pris" >&2; exit 2; }
# relais Kimi v3 : commande simple en arrière-plan, $! = PID de python (env l'exécute)
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$KIMI_API_KEY" HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  python3 -I -B $K/relais_kimi_v3.py --port $PORT --modeles-permis kimi-k3.1-pro --plafond-usd 3 --reserve-par-appel 0.05 \
  --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 4 --max-jetons-sortie-pire-cas 65536 --delai-amont-s 1800 \
  --delai-silence-s 600 --journal "$PWD/relais-kimi-brainstorm-journal-suite-v1.jsonl" > "$PWD/relais-kimi-brainstorm-suite-v1.log" 2>&1 &
PID_K=$!; echo $PID_K > relais-kimi-brainstorm-suite-v1.pid
arreter() { local i=0; kill "$PID_K" 2>/dev/null; while kill -0 "$PID_K" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done
  kill -0 "$PID_K" 2>/dev/null && kill -9 "$PID_K" 2>/dev/null; true; }
trap arreter EXIT; trap 'arreter; exit 130' INT TERM HUP
sleep 1; tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais (R10)" >&2; exit 3; }
i=0; until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$PORT/relais/etat', timeout=2)" 2>/dev/null; do
  i=$((i+1)); [ $i -lt 30 ] || { echo "relais Kimi non prêt" >&2; exit 3; }; sleep 1; done
# barrage (b) : Gemini (C) et Anthropic (A, B) reçoivent une valeur factice ; un appel imprévu échoue sans dépense ni quota
ENVI=(env -i PATH=/usr/bin:/bin HOME="$PWD" LANG=C.UTF-8 GO_ID=$GO_ID KIMI_RELAIS_URL=http://127.0.0.1:$PORT
  HTTPS_PROXY="${HTTPS_PROXY:-}" https_proxy="${https_proxy:-}" NO_PROXY="${NO_PROXY:-}" no_proxy="${no_proxy:-}"
  SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" REQUESTS_CA_BUNDLE="${REQUESTS_CA_BUNDLE:-}"
  ANTHROPIC_API_KEY="$FACTICE" GEMINI_API_KEY="$FACTICE" OPENAI_API_KEY="$OPENAI_API_KEY")
# contrôle préalable (R-919) : variables présentes par nom, relais joignable ; aucun appel payant.
"${ENVI[@]}" python3 -I -c "
import os, sys, urllib.request
manque = [n for n in ('ANTHROPIC_API_KEY', 'GEMINI_API_KEY', 'KIMI_RELAIS_URL', 'OPENAI_API_KEY', 'GO_ID') if not os.environ.get(n)]
if manque:
    sys.exit('variables lues par le collisionneur absentes : ' + ', '.join(manque))
url = os.environ['KIMI_RELAIS_URL'].rstrip('/') + '/relais/etat'
urllib.request.build_opener(urllib.request.ProxyHandler({})).open(url, timeout=5).read()
print('contrôle préalable : variables présentes (par nom), relais joignable à KIMI_RELAIS_URL', flush=True)
" || { echo "contrôle préalable en échec" >&2; exit 2; }
"${ENVI[@]}" timeout 600 "$PY" -I -B appel_controle_v11.py collisionneur_v9.py controle-brainstorm-v1-suite.json $GO_ID DE || { echo "appel de contrôle en échec" >&2; exit 2; }
grep -q '"ECHEC"' controle-brainstorm-v1-suite.json && { echo "une espèce en échec au contrôle" >&2; exit 2; }
# avant la suite : empreintes du journal et de l'état scellés, puis retrait de leurs deux seuls compagnons
(cd "$RUN" && sha256sum -c --quiet journal.jsonl.sha256 etat.md.sha256) || { echo "journal ou état modifié avant la suite" >&2; exit 2; }
sha256sum "$RUN/journal.jsonl" "$RUN/etat.md" > avant-suite-v1.txt && sha256sum avant-suite-v1.txt > avant-suite-v1.txt.sha256
rm -- "$RUN/journal.jsonl.sha256" "$RUN/etat.md.sha256"
code=0
"${ENVI[@]}" timeout 6900 "$PY" -I -B collisionneur_v9.py etage3 --sortie $RUN --faits faits.md \
    --question question.md --plafond-usd $PLAFOND || code=$?
python3 -I -c "import json,urllib.request; print(json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:$PORT/relais/etat')))[:900])" \
  > relais-kimi-brainstorm-etat-final-suite-v1.txt 2>/dev/null || true
arreter; trap - EXIT; echo "relais Kimi arrêté : PID $PID_K ; code de la suite $code"
for f in controle-brainstorm-v1-suite.json relais-kimi-brainstorm-journal-suite-v1.jsonl relais-kimi-brainstorm-suite-v1.log relais-kimi-brainstorm-etat-final-suite-v1.txt relais-kimi-brainstorm-suite-v1.pid; do
  [ -e "$f" ] && sha256sum "$f" > "$f.sha256"; done
for v in RR_ANTHROPIC_API_KEY_LUC GEMINI_API_KEY_2 KIMI_API_KEY OPENAI_API_KEY; do
  [ -n "${!v:-}" ] || continue
  grep -rqF -- "${!v}" $RUN relais-kimi-brainstorm-suite-v1.log relais-kimi-brainstorm-journal-suite-v1.jsonl controle-brainstorm-v1-suite.json 2>/dev/null && echo "ALERTE : $v trouvée dans une sortie" >&2; done
exit $code
