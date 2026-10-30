#!/bin/bash
# lancer-course-v2.sh — course 1, tentative 2, sur l'orchestrateur v50 (sans étage de tests de mort, sans moisson).
# session-depot, 30 octobre 2026. Écrit d'après les commandes réelles de la tentative 1 (29 octobre, 10:19 à 10:36 UTC) :
# relais Claude (pole/relais_reel.py) avec RR_ANTHROPIC_API_KEY_3, relais Gemini local (relais_gemini_v1.py) avec GEMINI_API_KEY_2,
# clés passées par variable sous env -i, jamais en argument ni en fichier. Ajout v47 (R-764, barrière 3) : --modeles-permis.
# L'appel de contrôle de chaque modèle est fait par l'orchestrateur lui-même avant la course (CL31-01) ; un refus = arrêt (R-764).
# Relais arrêtés par leur PID à la fin, quoi qu'il arrive (R10). Rien n'est écrasé (R12).
# Usage (root) : GO_ID=GO-2026-10-30-03 bash /root/ideation-v1/lancer-course-v2.sh
set -uo pipefail; set +x
DOS=/root/ideation-v1
. $DOS/args-course-v2.sh            # définit O, P, ARGS
SORTIE=$DOS/sortie-course-v2
DEPOT=/home/user/controle-ia-travail
RELAIS_G=$DEPOT/docs/notes/ideation-organisme-v1/lancement-v2/relais_gemini_v1.py
[ -n "${GO_ID:-}" ] || { echo "GO_ID absent" >&2; exit 2; }
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ "$(id -u)" = 0 ] || { echo "root exigé (setpriv)" >&2; exit 2; }
for f in $SORTIE $DOS/course-v2.log $DOS/relais-journal-v2.jsonl $DOS/relais-v2.log $DOS/relais-gemini-journal-v2.jsonl $DOS/relais-gemini-v2.log; do
  [ ! -e "$f" ] || { echo "$f existe déjà (R12)" >&2; exit 2; }; done
(cd $O && sha256sum -c --quiet EMPREINTES-orchestrateur-pole-v7-v50.txt) || { echo "arbre v50 non conforme" >&2; exit 2; }
(cd "$(dirname $RELAIS_G)" && sha256sum -c --quiet relais_gemini_v1.py.sha256) || { echo "relais Gemini non conforme" >&2; exit 2; }
[ "$(sha256sum /opt/argon/appel-argon-v3.sh | cut -c1-16)" = 24d5d16c7cb4ee85 ] || { echo "enveloppe Argon non conforme" >&2; exit 2; }
[ "$(sha256sum /opt/argon/commande_argon_v2.py | cut -c1-16)" = 6905ac71f126bfd4 ] || { echo "commande Argon non conforme" >&2; exit 2; }
for port in 8787 8788; do
  python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$port)) else 1)" || { echo "port $port déjà pris" >&2; exit 2; }; done

PID_C=""; PID_G=""
arreter() { [ -n "$PID_C" ] && kill "$PID_C" 2>/dev/null; [ -n "$PID_G" ] && kill "$PID_G" 2>/dev/null; true; }
trap arreter EXIT

# (1) relais Claude : plafond 40 (budget total Claude de la course, sans Opus proposeur), réserve 4 par appel, modèles permis exactement ceux des
#     proposeurs et des juges (le lanceur exige l'égalité exacte)
cd $O && setsid nohup env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" python3 -I pole/relais_reel.py --port 8787 --variable-cle ANTHROPIC_API_KEY \
  --plafond-usd 40 --reserve-par-appel 4 --modeles-permis claude-opus-5-5,claude-fable-5-1 \
  --journal $DOS/relais-journal-v2.jsonl > $DOS/relais-v2.log 2>&1 &
PID_C=$!; echo "$PID_C" > $DOS/relais-v2.pid
# (2) relais Gemini : 64 appels au plus (comme la tentative 1)
cd $DOS && setsid nohup env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" HTTPS_PROXY="${HTTPS_PROXY:-}" \
  SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 -I -B $RELAIS_G --port 8788 --max-appels 64 \
  --journal $DOS/relais-gemini-journal-v2.jsonl > $DOS/relais-gemini-v2.log 2>&1 &
PID_G=$!; echo "$PID_G" > $DOS/relais-gemini-v2.pid
for port in 8787 8788; do i=0
  until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$port/relais/etat', timeout=2)" 2>/dev/null; do
    i=$((i+1)); [ $i -lt 30 ] || { echo "relais $port non prêt" >&2; exit 3; }; sleep 1; done; done
python3 -I -c "import json,urllib.request; d=json.load(urllib.request.urlopen('http://127.0.0.1:8787/relais/etat')); print('relais claude : modeles_permis', d.get('modeles_permis'))"

# (3) course : mesure des consignes d'abord (sans appel), puis la course réelle ; l'orchestrateur fait l'appel de contrôle de
#     chaque modèle avant la première session
cd $O && env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 python3 -I -B demonstrations/ideation_v1.py "${ARGS[@]}" --mesurer-consignes \
  > $DOS/mesure-consignes-v50-lancement-v2.txt 2>&1 || { echo "mesure des consignes en échec" >&2; exit 4; }
grep -q '"passerait": true' $DOS/mesure-consignes-v50-lancement-v2.txt || { echo "consignes : ne passerait pas" >&2; exit 4; }
echo "début de la course : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
code=0
cd $O && env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 GO_ID="$GO_ID" python3 -I -B demonstrations/ideation_v1.py $SORTIE "${ARGS[@]}" \
  --moteur claude-sdk --url-relais http://127.0.0.1:8787 --confirmer-moteur-reel --horodatage "$(date -u)" > $DOS/course-v2.log 2>&1 || code=$?
echo "fin de la course : $(date -u +%Y-%m-%dT%H:%M:%SZ), code $code"

# (4) état final des relais (dépense comptée), arrêt par PID (R10), scellement des fichiers hors sortie
python3 -I -c "import json,urllib.request; print('claude', json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:8787/relais/etat')))[:600])" 2>/dev/null \
  > $DOS/relais-etat-final-v2.txt || true
python3 -I -c "import json,urllib.request; print('gemini', json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:8788/relais/etat')))[:600])" 2>/dev/null \
  >> $DOS/relais-etat-final-v2.txt || true
arreter; trap - EXIT; echo "relais arrêtés : $PID_C (claude), $PID_G (gemini)"
cd $DOS && for f in course-v2.log relais-journal-v2.jsonl relais-v2.log relais-gemini-journal-v2.jsonl relais-gemini-v2.log relais-etat-final-v2.txt mesure-consignes-v50-lancement-v2.txt; do
  [ -e "$f" ] && sha256sum "$f" > "$f.sha256"; done
exit $code
