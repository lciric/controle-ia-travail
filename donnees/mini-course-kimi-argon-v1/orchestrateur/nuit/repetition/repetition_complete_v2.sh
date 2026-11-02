#!/bin/bash
# Répétition v2 de la mini-course par le VRAI lanceur shell v2 (mode `repeter`) et les VRAIS chemins réseau des relais, SANS RÉSEAU
# ni dépense (sous-agent de session-depot, 1er novembre 2026), v1 de ce script.
# - relais Kimi réel vers https://api.moonshot.ai et relais Argon réel (`servir`, donc collisionneur_v7.appeler_gemini) vers
#   https://generativelanguage.googleapis.com, tous deux par HTTPS_PROXY = faux mandataire TLS local (faux_mandataire_tls_v1.py),
#   SSL_CERT_FILE = autorité FACTICE (autorite_factice_v1.sh) : aucune connexion TLS réelle ne peut aboutir ; clés FACTICES ;
# - spécification : copie de répétition du préenregistrement v2 (table des pièces gelées remplie), scellée dans le bloc-notes ;
#   contre-lecture : le vrai rapport scellé (lecture seule) ;
# - quatre essais : (0) refus du mode `repeter` sans autorité factice ; (1) course complète ; (2) `kill -TERM` du lanceur en pleine
#   course (CLM-01) ; (3) contrôle d'Argon en échec (modèle servi faux) : aucune course.
# Les dossiers de run vont sous donnees/mini-course-kimi-argon-v1/repetitions-v2/ (le lanceur l'exige) ; le reste dans DOSSIER.
# Usage : bash repetition_complete_v2.sh DOSSIER_NEUF
set -uo pipefail; set +x
cd "$(dirname "$0")/.." || exit 2
N="$PWD"; REPO=/home/user/controle-ia-travail; PY=/usr/bin/python3; E=(env -i PATH=/usr/bin:/bin LANG=C.UTF-8)
X="${1:?dossier de répétition neuf}"; [ ! -e "$X" ] || { echo "$X existe déjà" >&2; exit 2; }
mkdir -p "$X" && X="$(cd "$X" && pwd)"
B=$REPO/donnees/mini-course-kimi-argon-v1/repetitions-v2; mkdir -p "$B"; T=$(date -u +%Y%m%d-%H%M%S)
CLE_K=cle-factice-kimi-repetition-v2-0123456789; CLE_A=cle-factice-argon-repetition-v2-0123456789
FICHE=MC1-FICHE-FACTICE-67b8c480
C=$REPO/docs/notes/mini-course-kimi-argon-v1/contre-lecture-mini-course-kimi-argon-v1.md
bash repetition/autorite_factice_v1.sh "$X/ca" || exit 2
mkdir -p "$X/spec"
"${E[@]}" "$PY" -I -B - "$X/spec" "$C" <<'EOF' || exit 2
import hashlib, os, sys
sys.path.insert(0, os.path.join(os.getcwd(), "repetition"))
import table_pieces_gelees_v2 as t
d, cl = sys.argv[1], sys.argv[2]
src = "/home/user/controle-ia-travail/docs/notes/mini-course-kimi-argon-v1/preregistrement-mini-course-kimi-argon-v2.md"
texte = open(src, encoding="utf-8").read()
if "TABLE_DES_PIECES" in texte:
    texte = texte.replace("TABLE_DES_PIECES", "\n".join(t.lignes()))
sha_cl = hashlib.sha256(open(cl, "rb").read()).hexdigest()
assert sha_cl in texte, "le préenregistrement v2 doit citer l'empreinte du rapport de contre-lecture"
p = os.path.join(d, "preregistrement-repetition-v2.md")
b = texte.encode("utf-8")
open(p, "wb").write(b)
open(p + ".sha256", "w").write(f"{hashlib.sha256(b).hexdigest()}  {os.path.basename(p)}\n")
print("spécification de répétition :", p)
EOF
P="$X/spec/preregistrement-repetition-v2.md"
MANDATAIRE=""
demarrer_mandataire() {  # $1 nom, puis options
  local nom="$1"; shift
  "${E[@]}" "$PY" -I -B "$N/repetition/faux_mandataire_tls_v1.py" --certificat "$X/ca/cert.pem" --cle "$X/ca/cle.pem" \
    --port-fichier "$X/port-$nom" --journal "$X/mandataire-$nom.jsonl" --fiche-factice "$FICHE" "$@" > "$X/mandataire-$nom.log" 2>&1 &
  MANDATAIRE=$!; local i=0; until [ -s "$X/port-$nom" ]; do i=$((i+1)); [ $i -lt 40 ] || return 1; sleep 0.25; done
  PORT_M=$(cat "$X/port-$nom")
}
arreter_mandataire() { [ -n "$MANDATAIRE" ] && kill "$MANDATAIRE" 2>/dev/null; wait "$MANDATAIRE" 2>/dev/null; MANDATAIRE=""; }
trap arreter_mandataire EXIT
sh_v2() {  # $1 dossier du run ; le vrai lanceur v2, environnement vide sauf clés FACTICES, faux mandataire, autorité factice
  "${E[@]}" HOME="$X" GO_ID=GO-2026-11-01-12 GEMINI_API_KEY_2="$CLE_A" KIMI_API_KEY="$CLE_K" HTTPS_PROXY="http://127.0.0.1:$PORT_M" \
    SSL_CERT_FILE="$X/ca/ca.pem" bash "$N/lancer-mini-course-v2.sh" repeter "$1" "$P" "$C"
}
ports_libres() { "${E[@]}" "$PY" -I -c "import socket,sys; sys.exit(any(socket.socket().connect_ex(('127.0.0.1',p))==0 for p in (8804,8805)))"; }
resume() {  # $1 dossier du run
  local R="$1"
  echo "  relais Kimi : $(wc -l < "$R/relais-kimi-journal.jsonl" 2>/dev/null || echo 0) appels ; relais Argon : $(wc -l < "$R/relais-argon-journal.jsonl" 2>/dev/null || echo 0) appels"
  [ -f "$R/registre-depense-cumulee-v1.jsonl" ] && "${E[@]}" "$PY" -I -B registre_depense_cumulee_v1.py etat "$R/registre-depense-cumulee-v1.jsonl" \
    | "${E[@]}" "$PY" -I -c "import json,sys; o=json.load(sys.stdin); print('  registre : réglé', o['regle_usd'], '; engagé', o['engage_usd'], '; appels', o['appels'], {k: v['appels'] for k, v in o['par_etape'].items()}, '; dépassements', o['depassements_reserve'])"
  [ -f "$R/trace-agregee-mini-course-v2.json" ] && "${E[@]}" "$PY" -I -c "import json; t=json.load(open('$R/trace-agregee-mini-course-v2.json')); print('  trace : L1', t['l1']['fin'], t['l1']['motif_arret'], t['l1']['l3_l4'], '; appels', t['appels']['par_role'], '; anti-fuite', t['controle_anti_fuite']['resultat'])"
  grep -E "épreuve anti-fuite|aucune clé|ALERTE|signal|SIGTERM|relais arrêtés|fin, code|contrôle" "$R/journal-lancement-mini-course-v2.log" | sed 's/^/  journal : /' | cut -c1-260
}
bilan=0

echo "== essai 0 : mode repeter refusé sans autorité factice"
R0=$B/$T-refus
"${E[@]}" HOME="$X" GO_ID=GO-2026-11-01-12 GEMINI_API_KEY_2="$CLE_A" KIMI_API_KEY="$CLE_K" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  bash "$N/lancer-mini-course-v2.sh" repeter "$R0" "$P" "$C" 2>&1 | sed 's/^/  /'
c0=${PIPESTATUS[0]}; echo "  code $c0 ; dossier créé : $([ -e "$R0" ] && echo oui || echo non)"; [ "$c0" = 2 ] && [ ! -e "$R0" ] || bilan=1

echo "== essai 1 : course complète"
demarrer_mandataire complet || exit 3
R1=$B/$T-complete; sh_v2 "$R1"; c1=$?; arreter_mandataire
echo "  code $c1 ; ports 8804 et 8805 libres : $(ports_libres && echo oui || echo non)"; resume "$R1"
echo "  fiche factice dans fiches.json : $(grep -o "$FICHE" "$R1/course/generation-1/fiches.json" | wc -l) ; dans la trace : $(grep -c "MC1-" "$R1/trace-agregee-mini-course-v2.json")"
echo "  clé présente à l'amont (journal du mandataire) : $(grep -c '"cle": true' "$X/mandataire-complet.jsonl") appels sur $(grep -c '"hote"' "$X/mandataire-complet.jsonl")"
[ "$c1" = 0 ] || bilan=1

echo "== essai 2 : kill -TERM du lanceur en pleine course (CLM-01)"
demarrer_mandataire kill --pause-s 0.4 || exit 3
R2=$B/$T-kill
# lancé directement (pas par la fonction : `fonction &` crée un sous-shell, et `kill` n'atteindrait pas le lanceur)
"${E[@]}" HOME="$X" GO_ID=GO-2026-11-01-12 GEMINI_API_KEY_2="$CLE_A" KIMI_API_KEY="$CLE_K" HTTPS_PROXY="http://127.0.0.1:$PORT_M" \
  SSL_CERT_FILE="$X/ca/ca.pem" bash "$N/lancer-mini-course-v2.sh" repeter "$R2" "$P" "$C" & PSH=$!
i=0; until [ -f "$R2/registre-depense-cumulee-v1.jsonl" ] && [ "$(grep -c '"type": "debut"' "$R2/registre-depense-cumulee-v1.jsonl")" -ge 12 ]; do
  i=$((i+1)); [ $i -lt 600 ] || { echo "  la course n'a pas atteint 12 appels" >&2; break; }; sleep 0.2; done
echo "  PID du lanceur écrit au journal : $(grep -o "PID du lanceur [0-9]*" "$R2/journal-lancement-mini-course-v2.log" | grep -o "[0-9]*$") ; PID visé : $PSH"
PC=$(grep -o "course lancée en arrière-plan, PID [0-9]*" "$R2/journal-lancement-mini-course-v2.log" | grep -o "[0-9]*$")
echo "  $(date -u +%T) kill -TERM $PSH (lanceur) ; course PID $PC vivante : $(kill -0 "$PC" 2>/dev/null && echo oui || echo non) ; appels déjà partis : $(grep -c '"type": "debut"' "$R2/registre-depense-cumulee-v1.jsonl")"
t0=$(date +%s); kill -TERM "$PSH"; wait "$PSH"; c2=$?; t1=$(date +%s); arreter_mandataire
echo "  code $c2 en $((t1 - t0)) s ; course PID $PC vivante : $(kill -0 "$PC" 2>/dev/null && echo oui || echo non) ; ports libres : $(ports_libres && echo oui || echo non)"
for p in $(grep -o "PID [0-9]* (port" "$R2/journal-lancement-mini-course-v2.log" | grep -o "[0-9]*"); do echo "  relais PID $p vivant : $(kill -0 "$p" 2>/dev/null && echo oui || echo non)"; done
echo "  bilan de course : $("${E[@]}" "$PY" -I -c "import json; print(json.load(open('$R2/course/bilan-course.json'))['arret'])" 2>&1 | cut -c1-160)"
resume "$R2"
[ "$c2" = 130 ] || bilan=1

i=0; until ports_libres; do i=$((i+1)); [ $i -lt 60 ] || break; sleep 1; done
echo "== essai 3 : contrôle d'Argon en échec (modèle servi faux) : aucune course"
demarrer_mandataire controle --controle-modele-faux || exit 3
R3=$B/$T-controle; sh_v2 "$R3"; c3=$?; arreter_mandataire
echo "  code $c3 ; dossier course : $([ -e "$R3/course" ] && echo oui || echo non) ; ports libres : $(ports_libres && echo oui || echo non)"; resume "$R3"
[ "$c3" = 3 ] || bilan=1
echo "== fin de la répétition v2 : $([ $bilan = 0 ] && echo 'quatre essais conformes' || echo 'ÉCART (voir ci-dessus)')"; exit $bilan
