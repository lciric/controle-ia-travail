#!/bin/bash
# KIT COLOGNESE-WARD Q2, v1 (sous-agent de session-depot, 3 novembre 2026) : dérivé du kit Ibrahim v2 (outils/course-ibrahim-q1-v1, 965eb21b) par substitution de noms et par les changements de la course Colognese-Ward Q2 (deux pièces servies, trois variantes comme Ibrahim, garde lexicale sans « openai », juge du n° 419, marge d'appels 2 × plan + 5).
# RÉPÉTITION COLOGNESE-WARD Q2 v2 (sous-agent de session-depot, 3 novembre 2026) = repetition_complete_colognese_v1.sh (gardée, R12) appliquée au lanceur shell v2, aux configurations Colognese-Ward Q2 q1-v2, à la table v2 et au faux mandataire v2, qui rend 8 fiches par proposeur (plan : 6) ; l'essai 1 vérifie en plus les 8 fiches par proposeur dans la trace et imprime, par relais, les appels journalisés et le reste sous max_appels (contre-lecture CLI-01). Les lignes suivantes sont héritées.
# v2 = repetition_complete_colognese_v1.sh (gardée, R12) appliquée au lanceur shell v2 et aux configurations v2.
# Répétition complète de la course Colognese-Ward Q2 par le VRAI lanceur shell (mode `repeter`) et les VRAIS relais, SANS RÉSEAU ni
# dépense (sous-agent de session-depot, 3 novembre 2026), v3 = v2 (gardée, R12) appliquée au lanceur shell v3 et aux
# configurations v2 (pièces v2 de la contre-lecture ; table des pièces gelées v3) — sur le modèle de nuit/repetition/repetition_complete_v2.sh.
# - relais Claude réel (SDK anthropic, PY_RELAIS_CLAUDE) vers https://api.anthropic.com, relais Astra réel
#   (collisionneur_v8.appeler_openai) vers https://api.openai.com, relais Kimi réel (relais_kimi_v3.py) vers
#   https://api.moonshot.ai, relais Argon réel (collisionneur_v7.appeler_gemini) vers https://generativelanguage.googleapis.com,
#   tous par HTTPS_PROXY = faux mandataire TLS local (faux_mandataire_tls_colognese_v1.py), SSL_CERT_FILE = autorité FACTICE
#   (autorite_factice_colognese_v1.sh) : aucune connexion TLS réelle ne peut aboutir ; clés FACTICES ;
# - spécification de répétition : fiche et contre-lecture factices scellées dans DOSSIER, table des pièces gelées réelle ;
#   registre des GO de répétition (GO-2026-11-03-99, 244 USD, marqué RÉPÉTITION FACTICE) dans DOSSIER ;
# - cinq essais : (0) refus sans autorité factice ; (1) course complète, cinq espèces, comptes par étape et par modèle ;
#   (2) `kill -TERM` du lanceur en pleine course → arrêt propre, code 130 ; (3) contrôle d'un modèle en échec (modèle servi
#   différent) → aucune course, code 3 ; (4) plafond de session trop bas → refus avant tout appel, code 2.
# Les dossiers de run vont sous DOSSIER (hors du dépôt, comme l'exige le lanceur).
# Usage : PY_RELAIS_CLAUDE=/chemin/python-avec-anthropic bash repetition_complete_heimersheim_v1.sh DOSSIER_NEUF_HORS_DEPOT
set -uo pipefail; set +x
cd "$(dirname "$0")/.." || exit 2
H="$PWD"; O="$(cd .. && pwd)"; N="$O/nuit"; PY=/usr/bin/python3; E=(env -i PATH=/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1)
PYA="${PY_RELAIS_CLAUDE:?PY_RELAIS_CLAUDE (Python portant anthropic) exigé}"
X="${1:?dossier de répétition neuf}"; [ ! -e "$X" ] || { echo "$X existe déjà" >&2; exit 2; }
mkdir -p "$X" && X="$(cd "$X" && pwd -P)"
GO=GO-2026-11-03-99; T=$(date -u +%Y%m%d-%H%M%S)
CA_=cle-factice-anthropic-repetition-0123456789; CO=cle-factice-openai-repetition-0123456789
CK=cle-factice-kimi-repetition-0123456789; CG=cle-factice-argon-repetition-0123456789
bash repetition/autorite_factice_colognese_v1.sh "$X/ca" || exit 2
S17_REP="$("${E[@]}" "$PY" -I -c "import json,sys; print('%g' % json.load(open(sys.argv[1]))['budget']['plafond_usd'])" "$H/configuration-course-colognese-ward-q2-v1-cinq-especes.json")" || exit 2
printf '%s\n' "# Registre des GO — RÉPÉTITION FACTICE (aucun GO réel, aucune dépense)" "" \
  "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |" "|---|---|---|---|---|---|---|---|" \
  "| $GO | 2026-11-03 | calcul | RÉPÉTITION FACTICE de la course Colognese-Ward Q2 (faux amonts) | $S17_REP USD | 2026-11-30 | Lazar | répétition |" \
  > "$X/go-repetition.md"
"${E[@]}" "$PY" -I -B - "$X/spec" "$H" "$O" <<'EOF' || exit 2
import os, subprocess, sys
d, h, o = sys.argv[1:4]
sys.path.insert(0, o)
from pole.outils import ecrire_scelle, sha256_fichier
cl = os.path.join(d, "contre-lecture-repetition-v1.md")
ecrire_scelle(cl, "# Contre-lecture FACTICE de répétition (aucune valeur réelle)\n")
table = subprocess.run([sys.executable, "-I", "-B", os.path.join(h, "table_pieces_gelees_colognese_v1.py"), "lignes"],
                       capture_output=True, text=True, check=True).stdout
fiche = ("# Fiche de lancement — RÉPÉTITION FACTICE de la course Colognese-Ward Q2\n\nContre-lecture : " + sha256_fichier(cl) + "\n\n"
         "### Pièces gelées\n\n| pièce | sha256 | rôle |\n|---|---|---|\n" + table + "\n## Fin\n")
ecrire_scelle(os.path.join(d, "fiche-repetition-v1.md"), fiche)
print("spécification de répétition :", d)
EOF
P="$X/spec/fiche-repetition-v1.md"; C="$X/spec/contre-lecture-repetition-v1.md"
MANDATAIRE=""
demarrer_mandataire() {  # $1 nom, puis options
  local nom="$1"; shift
  "${E[@]}" "$PY" -I -B "$H/repetition/faux_mandataire_tls_colognese_v1.py" --certificat "$X/ca/cert.pem" --cle "$X/ca/cle.pem" \
    --port-fichier "$X/port-$nom" --journal "$X/mandataire-$nom.jsonl" "$@" > "$X/mandataire-$nom.log" 2>&1 &
  MANDATAIRE=$!; local i=0; until [ -s "$X/port-$nom" ]; do i=$((i+1)); [ $i -lt 40 ] || return 1; sleep 0.25; done
  PORT_M=$(cat "$X/port-$nom")
}
arreter_mandataire() { [ -n "$MANDATAIRE" ] && kill "$MANDATAIRE" 2>/dev/null; wait "$MANDATAIRE" 2>/dev/null; MANDATAIRE=""; }
trap arreter_mandataire EXIT
lanceur() {  # $1 configuration, $2 run, puis variables en plus ; le vrai lanceur, environnement vide sauf clés FACTICES
  local conf="$1" run="$2"; shift 2
  "${E[@]}" HOME="$X" GO_ID=$GO PY_RELAIS_CLAUDE="$PYA" RR_ANTHROPIC_API_KEY_LUC="$CA_" OPENAI_API_KEY="$CO" KIMI_API_KEY="$CK" \
    GEMINI_API_KEY_2="$CG" HTTPS_PROXY="http://127.0.0.1:${PORT_M:-9}" SSL_CERT_FILE="$X/ca/ca.pem" REGISTRE_GO="$X/go-repetition.md" "$@" \
    bash "$H/lancer-course-colognese-v1.sh" repeter $GO "$conf" "$run" "$P" "$C"
}
ports_libres() { "${E[@]}" "$PY" -I -c "import socket,sys; sys.exit(any(socket.socket().connect_ex(('127.0.0.1',p))==0 for p in (8804,8805,8806,8807)))"; }
resume() {  # $1 dossier du run
  local R="$1" f
  for f in claude astra kimi argon; do [ -f "$R/relais-$f-journal.jsonl" ] && echo "  relais $f : $(wc -l < "$R/relais-$f-journal.jsonl") appels"; done
  [ -f "$R/registre-depense-cumulee-v1.jsonl" ] && "${E[@]}" "$PY" -I -B "$N/registre_depense_cumulee_v1.py" etat "$R/registre-depense-cumulee-v1.jsonl" \
    | "${E[@]}" "$PY" -I -c "import json,sys; o=json.load(sys.stdin); print('  registre : réglé', o['regle_usd'], '; engagé', o['engage_usd'], '; appels', o['appels'], {k: v['appels'] for k, v in o['par_etape'].items()}, '; dépassements', o['depassements_reserve'])"
  [ -f "$R/trace-agregee-course-colognese-v1.json" ] && "${E[@]}" "$PY" -I -c "import json; t=json.load(open('$R/trace-agregee-course-colognese-v1.json')); print('  trace : fin', t['l1']['fin'], t['l1']['motif_arret'], '; appels par étape', t['appels']['par_etape'], '; par modèle', t['appels']['par_modele'], '; fiches', t['fiches']['proposees_par_proposeur'], '; paires', t['paires_par_bras'], '; fusions', t['fusions_par_bras'], '; anti-fuite', t['controle_anti_fuite']['resultat'])"
  grep -E "épreuve anti-fuite|aucune clé|ALERTE|signal|SIGTERM|arrêté|fin, code|contrôle|scellé|refusée|non écrit" "$R/journal-lancement-course-colognese-v1.log" 2>/dev/null | sed 's/^/  journal : /' | cut -c1-240
}
bilan=0

echo "== essai 0 : mode repeter refusé sans autorité factice"
R0=$X/run-$T-refus
"${E[@]}" HOME="$X" GO_ID=$GO PY_RELAIS_CLAUDE="$PYA" RR_ANTHROPIC_API_KEY_LUC="$CA_" OPENAI_API_KEY="$CO" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  REGISTRE_GO="$X/go-repetition.md" bash "$H/lancer-course-colognese-v1.sh" repeter $GO configuration-course-colognese-ward-q2-v1-avec-kimi.json "$R0" "$P" "$C" 2>&1 | sed 's/^/  /'
c0=${PIPESTATUS[0]}; echo "  code $c0 ; dossier créé : $([ -e "$R0" ] && echo oui || echo non)"; [ "$c0" = 2 ] && [ ! -e "$R0" ] || bilan=1

echo "== essai 1 : course complète, variante cinq_especes"
demarrer_mandataire complet || exit 3
R1=$X/run-$T-complete; t0=$(date +%s); lanceur configuration-course-colognese-ward-q2-v1-cinq-especes.json "$R1"; c1=$?; t1=$(date +%s); arreter_mandataire
echo "  code $c1 en $((t1 - t0)) s ; ports 8804 à 8807 libres : $(ports_libres && echo oui || echo non)"; resume "$R1"
echo "  clé présente à l'amont (journal du mandataire) : $(grep -c '"cle": true' "$X/mandataire-complet.jsonl") appels sur $(grep -c '"hote"' "$X/mandataire-complet.jsonl") ; par hôte : $(grep -o '"hote": "[a-z.]*"' "$X/mandataire-complet.jsonl" | sort | uniq -c | tr -s ' ' | tr '\n' ';')"
"${E[@]}" "$PY" -I - "$R1" "$H/configuration-course-colognese-ward-q2-v1-cinq-especes.json" <<'EOF2' || bilan=1
import json, os, sys
r, c = sys.argv[1:3]
conf = json.load(open(c, encoding="utf-8"))
t = json.load(open(os.path.join(r, "trace-agregee-course-colognese-v1.json"), encoding="utf-8"))
fp = t["fiches"]["proposees_par_proposeur"]
ok = bool(fp) and all(v == 8 for v in fp.values())
print("  amont à 8 fiches par proposeur (plan : 6) :", fp, "->", "conforme" if ok else "ÉCART")
for f, x in sorted(conf["relais"].items()):
    p = os.path.join(r, "relais-%s-journal.jsonl" % f)
    n = sum(1 for _ in open(p, encoding="utf-8")) if os.path.exists(p) else 0
    print("  relais %s : %d lignes de journal, max_appels %d, reste %d" % (f, n, x["max_appels"], x["max_appels"] - n))
sys.exit(0 if ok else 1)
EOF2
[ "$c1" = 0 ] || bilan=1

echo "== essai 2 : kill -TERM du lanceur en pleine course (variante avec_kimi)"
demarrer_mandataire kill --pause-s 0.3 || exit 3
R2=$X/run-$T-kill
"${E[@]}" HOME="$X" GO_ID=$GO PY_RELAIS_CLAUDE="$PYA" RR_ANTHROPIC_API_KEY_LUC="$CA_" OPENAI_API_KEY="$CO" KIMI_API_KEY="$CK" \
  HTTPS_PROXY="http://127.0.0.1:$PORT_M" SSL_CERT_FILE="$X/ca/ca.pem" REGISTRE_GO="$X/go-repetition.md" \
  bash "$H/lancer-course-colognese-v1.sh" repeter $GO configuration-course-colognese-ward-q2-v1-avec-kimi.json "$R2" "$P" "$C" & PSH=$!
i=0; until [ -f "$R2/registre-depense-cumulee-v1.jsonl" ] && [ "$(grep -c '"type": "debut"' "$R2/registre-depense-cumulee-v1.jsonl")" -ge 15 ]; do
  i=$((i+1)); [ $i -lt 900 ] || { echo "  la course n'a pas atteint 15 appels" >&2; break; }; sleep 0.2; done
PC=$(grep -o "course lancée en arrière-plan, PID [0-9]*" "$R2/journal-lancement-course-colognese-v1.log" | grep -o "[0-9]*$")
echo "  $(date -u +%T) kill -TERM $PSH (lanceur) ; course PID $PC vivante : $(kill -0 "$PC" 2>/dev/null && echo oui || echo non) ; appels déjà partis : $(grep -c '"type": "debut"' "$R2/registre-depense-cumulee-v1.jsonl")"
t0=$(date +%s); kill -TERM "$PSH"; wait "$PSH"; c2=$?; t1=$(date +%s); arreter_mandataire
echo "  code $c2 en $((t1 - t0)) s ; course PID $PC vivante : $(kill -0 "$PC" 2>/dev/null && echo oui || echo non) ; ports libres : $(ports_libres && echo oui || echo non)"
for p in $(grep -o "PID [0-9]* (port" "$R2/journal-lancement-course-colognese-v1.log" | grep -o "[0-9]*"); do echo "  relais PID $p vivant : $(kill -0 "$p" 2>/dev/null && echo oui || echo non)"; done
echo "  bilan de course : $("${E[@]}" "$PY" -I -c "import json; print(json.load(open('$R2/course/bilan-course.json'))['arret'])" 2>&1 | cut -c1-160)"
resume "$R2"
[ "$c2" = 130 ] || bilan=1

i=0; until ports_libres; do i=$((i+1)); [ $i -lt 60 ] || break; sleep 1; done
echo "== essai 3 : contrôle d'un modèle en échec (Opus 5.5 servi sous un autre nom) : aucune course"
demarrer_mandataire controle --controle-modele-faux claude-opus-5-5 || exit 3
R3=$X/run-$T-controle; lanceur configuration-course-colognese-ward-q2-v1-avec-kimi.json "$R3"; c3=$?; arreter_mandataire
echo "  code $c3 ; dossier course : $([ -e "$R3/course" ] && echo oui || echo non) ; ports libres : $(ports_libres && echo oui || echo non)"; resume "$R3"
[ "$c3" = 3 ] && [ ! -e "$R3/course" ] || bilan=1

echo "== essai 4 : plafond de session trop bas (juge 0,5 USD < pire cas d'un appel d'Astra) : refus avant tout appel"
"${E[@]}" "$PY" -I -B - "$H/configuration-course-colognese-ward-q2-v1-avec-kimi.json" "$X/configuration-artefact-plafond-bas.json" "$H" <<'EOF' || exit 2
import json, os, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))
c["plafonds_session"]["juge"] = 0.5
for p in c["pieces"].values():
    p["chemin"] = os.path.join(sys.argv[3], p["chemin"])
c["bisociateur"]["gu_krenn"]["source"]["chemin"] = os.path.join(sys.argv[3], c["bisociateur"]["gu_krenn"]["source"]["chemin"])
json.dump(c, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
EOF
demarrer_mandataire plafond || exit 3
R4=$X/run-$T-plafond; lanceur configuration-course-colognese-ward-q2-v1-avec-kimi.json "$R4" CONFIGURATION_REPETITION="$X/configuration-artefact-plafond-bas.json"; c4=$?; arreter_mandataire
echo "  code $c4 ; registre de dépense : $([ -e "$R4/registre-depense-cumulee-v1.jsonl" ] && echo oui || echo non) ; relais lancés : $(ls "$R4"/relais-*.log 2>/dev/null | wc -l) ; appels à l'amont : $(grep -c '"hote"' "$X/mandataire-plafond.jsonl" 2>/dev/null || echo 0)"
grep -o "plafonds_session.juge[^\"]*" "$R4/journal-lancement-course-colognese-v1.log" | head -1 | sed 's/^/  motif : /' | cut -c1-200
[ "$c4" = 2 ] && [ ! -e "$R4/registre-depense-cumulee-v1.jsonl" ] || bilan=1
echo "== fin de la répétition : $([ $bilan = 0 ] && echo 'cinq essais conformes' || echo 'ÉCART (voir ci-dessus)')"; exit $bilan
