#!/bin/bash
# Répétition complète de la mini-course, SANS RÉSEAU ni dépense (sous-agent de session-depot, 1er novembre 2026), v1.
# Même chaîne que lancer-mini-course-v1.sh — vraies commandes, vrai relais Kimi (empreinte vérifiée, clé FACTICE, amont sur la
# boucle locale), vrai serveur du relais Argon (appelant remplacé), vrai registre cumulé, vrai lanceur en moteur réel, vraie
# ligne de GO lue dans registres/go.md (aucune dépense : les amonts sont factices) — sauf : préenregistrement et contre-lecture
# sont des COPIES DE RÉPÉTITION scellées dans le dossier de répétition (jamais les vraies pièces), et la fiche factice est plantée.
# Usage : bash repetition_complete_v1.sh DOSSIER_NEUF        (hors de donnees/ de préférence : bloc-notes de la session)
set -uo pipefail; set +x
cd "$(dirname "$0")/.." || exit 2
N="$PWD"; REPO=/home/user/controle-ia-travail; PY=/usr/bin/python3
RUN="${1:?dossier de répétition neuf}"; [ ! -e "$RUN" ] || { echo "$RUN existe déjà" >&2; exit 2; }
mkdir -p "$RUN" && RA="$(cd "$RUN" && pwd)"
FICHE_FACTICE=MC1-FICHE-FACTICE-67b8c480
CLE_K=cle-factice-kimi-repetition-0123456789; CLE_A=cle-factice-argon-repetition-0123456789
CONF=$N/configuration-mini-course-kimi-argon-v1.json
K=$REPO/docs/notes/ideation-organisme-v1/relais-kimi-v1
(cd "$K" && sha256sum -c --quiet relais_kimi_v3.py.sha256) || { echo "relais Kimi v3 non conforme" >&2; exit 2; }
(cd "$N/.." && sha256sum -c --quiet nuit/EMPREINTES-orchestrateur-v56-copie-v1.txt) || { echo "copie v56 modifiée" >&2; exit 2; }

# Spécification de répétition : copie du brouillon, table des pièces gelées remplie, contre-lecture factice scellée.
S="$RA/specification-repetition"; mkdir -p "$S"
"$PY" -I -B - "$S" <<'EOF' || exit 2
import os, sys, hashlib
sys.path.insert(0, os.path.join(os.getcwd(), "repetition"))
import table_pieces_gelees_v1 as t
d = sys.argv[1]
src = "/home/user/controle-ia-travail/docs/notes/mini-course-kimi-argon-v1/preregistrement-mini-course-kimi-argon-v1.md"
cl = os.path.join(d, "contre-lecture-repetition.md")
octets = "Contre-lecture FACTICE de répétition (aucune valeur réelle).\n".encode("utf-8")
open(cl, "wb").write(octets)
sha_cl = hashlib.sha256(octets).hexdigest()
open(cl + ".sha256", "w").write(f"{sha_cl}  {os.path.basename(cl)}\n")
texte = open(src, encoding="utf-8").read()
if "TABLE_DES_PIECES" in texte:
    texte = texte.replace("TABLE_DES_PIECES", "\n".join(t.lignes()))
texte = texte.replace("À FOURNIR AU SCELLEMENT", sha_cl)
p = os.path.join(d, "preregistrement-repetition.md")
b = texte.encode("utf-8")
open(p, "wb").write(b)
open(p + ".sha256", "w").write(f"{hashlib.sha256(b).hexdigest()}  {os.path.basename(p)}\n")
print("spécification de répétition scellée dans", d)
EOF

REG="$RA/registre-depense-cumulee-v1.jsonl"; PORT_K=8804; PORT_A=8805; PID_F=""; PID_K=""; PID_A=""
arreter_pid() { local p="$1" i=0; [ -n "$p" ] || return 0; kill "$p" 2>/dev/null; while kill -0 "$p" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done; kill -0 "$p" 2>/dev/null && kill -9 "$p" 2>/dev/null; true; }
etat_relais() { "$PY" -I -c "import urllib.request,sys; o=urllib.request.build_opener(urllib.request.ProxyHandler({})); sys.stdout.write(o.open('http://127.0.0.1:$1/relais/etat', timeout=5).read().decode())" 2>/dev/null; }
arreter() { [ -n "$PID_K" ] && etat_relais $PORT_K > "$RA/etat-final-relais-kimi.json"; [ -n "$PID_A" ] && etat_relais $PORT_A > "$RA/etat-final-relais-argon.json"; arreter_pid "$PID_K"; arreter_pid "$PID_A"; arreter_pid "$PID_F"; PID_K=""; PID_A=""; PID_F=""; }
trap arreter EXIT; trap 'arreter; exit 130' INT TERM HUP
for p in $PORT_K $PORT_A; do "$PY" -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$p)) else 1)" || { echo "port $p pris" >&2; exit 2; }; done
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 "$PY" -I -B "$N/repetition/faux_amonts_repetition_v1.py" kimi --port-fichier "$RA/port-faux-kimi" \
  --fiche-factice "$FICHE_FACTICE" > "$RA/faux-amont-kimi.log" 2>&1 &
PID_F=$!
i=0; until [ -s "$RA/port-faux-kimi" ]; do i=$((i+1)); [ $i -lt 30 ] || { echo "faux amont Kimi non prêt" >&2; exit 3; }; sleep 0.5; done
PF=$(cat "$RA/port-faux-kimi")
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 KIMI_API_KEY="$CLE_K" \
  "$PY" -I -B "$K/relais_kimi_v3.py" --port $PORT_K --amont "http://127.0.0.1:$PF" --modeles-permis kimi-k3.1-pro --plafond-usd 10 \
  --reserve-par-appel 0.05 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 40 --max-jetons-sortie-pire-cas 65536 \
  --delai-amont-s 1700 --delai-silence-s 600 --journal "$RA/relais-kimi-journal.jsonl" > "$RA/relais-kimi.log" 2>&1 &
PID_K=$!
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$CLE_A" \
  "$PY" -I -B "$N/repetition/faux_amonts_repetition_v1.py" argon --port $PORT_A --journal "$RA/relais-argon-journal.jsonl" \
  --fiche-factice "$FICHE_FACTICE" > "$RA/relais-argon.log" 2>&1 &
PID_A=$!
sleep 1
tr '\0' ' ' < /proc/$PID_K/cmdline | grep -q relais_kimi_v3.py || { echo "PID $PID_K n'est pas le relais Kimi (R10)" >&2; exit 3; }
tr '\0' ' ' < /proc/$PID_A/cmdline | grep -q "faux_amonts_repetition_v1.py argon" || { echo "PID $PID_A n'est pas le relais Argon (R10)" >&2; exit 3; }
for p in $PORT_K $PORT_A; do i=0; until etat_relais $p > /dev/null; do i=$((i+1)); [ $i -lt 30 ] || { echo "relais $p non prêt" >&2; exit 3; }; sleep 1; done; done
echo "relais Kimi PID $PID_K, relais Argon PID $PID_A, faux amont Kimi PID $PID_F (port $PF)"

controle() {
  local cmd="$1" mod="$2" out="$3"; shift 3
  printf 'Réponds seulement par le mot OK.' | env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$RA" PLAFOND_SESSION_USD=0.05 \
    ROLE_POLE=juge_ideation MODELE_DEMANDE_POLE="$mod" ETAPE_POLE=controle PLAFOND_ETAPE_USD=0.10 \
    "$PY" -I -B "$cmd" "$@" --registre "$REG" --plafond-cumule-usd 10 > "$out" 2>&1 || return 1
  tail -n 1 "$out" | "$PY" -I -c "import json,sys; o=json.loads(sys.stdin.read()); sys.exit(0 if o.get('modele_servi')=='$mod' and o.get('cout_usd',0)>0 else 1)"
}
controle "$N/commande_kimi_v2.py" kimi-k3.1-pro "$RA/controle-kimi.json" --url-relais http://127.0.0.1:$PORT_K \
  --max-sortie-court 4096 --sortie-min-jetons 1024 || { echo "contrôle Kimi en échec" >&2; exit 3; }
controle "$N/commande_argon_v56_nuit_v1.py" gemini-4-argon "$RA/controle-argon.json" appeler --url-relais http://127.0.0.1:$PORT_A \
  --max-sortie-court 1000 --sortie-min-jetons 256 || { echo "contrôle Argon en échec" >&2; exit 3; }
echo "contrôles conformes"

code=0
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 HOME="$RA" GO_ID=GO-2026-11-01-12 timeout 1800 "$PY" -I -B lancer_mini_course_v1.py lancer \
  --configuration "$CONF" --sortie "$RA/course" --registre-depense "$REG" --registre-go "$REPO/registres/go.md" \
  --confirmer-moteur-reel --preenregistrement "$S/preregistrement-repetition.md" --contre-lecture "$S/contre-lecture-repetition.md" \
  > "$RA/lanceur.log" 2>&1 || code=$?
echo "course : code $code"; tail -n 2 "$RA/lanceur.log" | cut -c1-600
arreter; trap - EXIT
"$PY" -I -B trace_agregee_mini_course_v1.py --run "$RA" --configuration "$CONF" --canari "$FICHE_FACTICE" || code=7
"$PY" -I -B trace_agregee_mini_course_v1.py --run "$RA" --configuration "$CONF" --canari "$FICHE_FACTICE" --artefacts-sur-run
for v in CLE_K CLE_A; do grep -rqF -- "${!v}" "$RA" 2>/dev/null && { echo "ALERTE : $v trouvée dans une sortie" >&2; code=6; }; done
echo "fin de la répétition, code $code"; exit $code
