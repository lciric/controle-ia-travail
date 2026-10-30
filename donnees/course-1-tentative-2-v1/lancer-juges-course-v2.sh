#!/bin/bash
# lancer-juges-course-v2.sh — mode « juges seulement » (orchestrateur v52) sur la course 1, tentative 2 (arrêtée le 30 octobre à
# 07:44 UTC sur un refus du juge Fable 5.1). Décision du directeur R-805 (≈ 08:00 UTC) : les 29 fiches validées sont notées par
# Opus 5.5 (juge-opus) et Argon (argon-juge), sans Fable ; si Opus 5.5 refuse, bascule DÉCLARÉE sur claude-opus-4-6 (option
# --bascule-declaree, jamais automatique, modèle servi consigné) ; toute autre bascule reste un arrêt (R-764).
# Préparé par le sous-agent ingénieur de conv-audit, 30 octobre 2026. JAMAIS LANCÉ ICI (aucun appel, aucune clé).
#
# Étapes : (0) gardes sans dépense (GO, clés, root, arbre v52, relais Gemini, commande d'Argon, ports, R12) ;
# (1) --verifier-seulement : empreintes de la course, reconstruction des consignes (celle de juge-fable, mise à l'écart, doit
#     être retrouvée octet pour octet), sommes, empreintes à attester — aucun appel, aucune écriture ;
# (2) essai à blanc, moteur simulé, sur les vraies fiches, SANS --commande-externe (aucun appel vers Argon) : code 4 attendu
#     (des juges simulés ne reconnaissent pas les témoins réels) ; tout autre code que 0 ou 4 arrête tout ;
# (3) attestation de lecture humaine exigée pour le juge externe (même contrat que le bras différé) : sans elle, arrêt AVANT les
#     relais (rien payé) ; elle porte fiches_validees_sha256 et consignes_en_attente_sha256.argon-juge imprimés à l'étape (1) ;
# (4) relais Claude v2 (pole/relais_reel_v2.py) : plafond 20 USD, réserve 4 par appel, --modeles-permis
#     claude-opus-5-5,claude-opus-4-6 (exactement les modèles Claude du mode) ; relais Gemini (8 appels au plus) ;
#     clés par variable sous env -i, jamais en argument ni en fichier ;
# (5) mode réel ; (6) état final des relais, arrêt des relais par leur PID (R10, sur tout chemin de sortie), scellement.
#
# DEVIS (plafonds, pire cas) — budgets des juges de la course, plus les contrôles :
#   Claude : contrôles 2 × 0,2 (Opus 5.5, Opus 4.6) + juge Opus 5.5 4,0 + session de repli Opus 4.6 4,0 (seulement sur refus)
#            = 8,4 ; total Claude du mode 10,0 (marge : une session refusée peut être comptée un peu au-delà de son plafond,
#            7,51 pour 7 chez Fable à la course) ; relais plafonné à 20 (Opus 4.6 compté au barème inconnu v2, borne haute).
#   Argon  : contrôle court 0,2 + juge 3,5 = 3,7 ; total externe 4,0.
#   Pire cas ≈ 12,1 USD facturés (Claude 8,4 + Argon 3,7), plafonds 10 + 4 = 14.
#   Attendu (SUPPOSÉ) : consigne du juge 824 298 caractères (≈ 210 000 jetons) — Opus 5.5 ≈ 1,0 à 1,5 ; Argon ≈ 2,3 à 2,7 (ses
#   passes de 686 000 à 758 000 caractères ont coûté 2,04 et 2,21) ; contrôles quelques centimes : ≈ 3,5 à 4,5 USD sans refus ;
#   avec un refus d'Opus 5.5 (session refusée jusqu'à 4,0) et la bascule (Opus 4.6 ≈ 1,5 à 2,0) : ≈ 8 à 9 USD.
#
# Usage (root) :
#   GO_ID=GO-AAAA-MM-JJ-NN ATTESTATION=/root/ideation-v1/attestation-lecture-juges-course-v2.json \
#     bash /root/ideation-v1/lancer-juges-course-v2.sh > /root/ideation-v1/lancement-juges-course-v2.out 2>&1
#   (RR_ANTHROPIC_API_KEY_3 et GEMINI_API_KEY_2 dans l'environnement du lanceur, jamais en argument.)
set -uo pipefail; set +x
DOS=/root/ideation-v1
. $DOS/args-course-v2.sh            # DOS, P, CORPUS (et ARGS de la course, non utilisé ici)
O=$DOS/orchestrateur-v52/arbre
EMPREINTES_V52=EMPREINTES-orchestrateur-pole-v7-v52.txt
EMPREINTE_LISTE_V52=13bc34c763a76ecf1e6b9867fa46e12d4e486458f3cde503909be5f0db94361f
COURSE=$DOS/sortie-course-v2
SORTIE=$DOS/sortie-juges-course-v2
BLANC=$DOS/sortie-juges-course-v2-essai-blanc
DEPOT=/home/user/controle-ia-travail
RELAIS_G=$DEPOT/docs/notes/ideation-organisme-v1/lancement-v2/relais_gemini_v1.py
CMD_ARGON="/usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v3.sh"
FIN_SHA=192b39807fa11faa23425d9279bb5a3a09cc03480ba0d6ce8a373fd7e9bb1343      # manifeste-fin.json de la course
FICHES_SHA=a7068ba41ec4929edaedf28a5669a6f7d34773445dfad7295b6652085ce3b7f9   # fiches-validees.json (29 fiches)

# (0) gardes sans dépense
[ -n "${GO_ID:-}" ] || { echo "GO_ID absent" >&2; exit 2; }
[ -n "${RR_ANTHROPIC_API_KEY_3:-}" ] || { echo "RR_ANTHROPIC_API_KEY_3 absente" >&2; exit 2; }
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ "$(id -u)" = 0 ] || { echo "root exigé (setpriv de la commande d'Argon)" >&2; exit 2; }
for f in $SORTIE $BLANC $DOS/juges-course-v2.log $DOS/verification-juges-course-v2.json $DOS/essai-blanc-juges-course-v2.log \
         $DOS/relais-juges-journal-v1.jsonl $DOS/relais-juges-v1.log $DOS/relais-gemini-juges-journal-v1.jsonl \
         $DOS/relais-gemini-juges-v1.log $DOS/relais-juges-etat-final-v1.txt; do
  [ ! -e "$f" ] || { echo "$f existe déjà (R12)" >&2; exit 2; }; done
[ "$(sha256sum $O/$EMPREINTES_V52 | cut -d' ' -f1)" = "$EMPREINTE_LISTE_V52" ] || { echo "liste d'empreintes v52 non conforme" >&2; exit 2; }
(cd $O && sha256sum -c --quiet $EMPREINTES_V52) || { echo "arbre v52 non conforme" >&2; exit 2; }
(cd $COURSE && sha256sum -c --quiet manifeste-depart.json.sha256 manifeste-fin.json.sha256 fiches-validees.json.sha256) \
  || { echo "course arrêtée : sceaux faux" >&2; exit 2; }
(cd "$(dirname $RELAIS_G)" && sha256sum -c --quiet relais_gemini_v1.py.sha256) || { echo "relais Gemini non conforme" >&2; exit 2; }
[ "$(sha256sum /opt/argon/appel-argon-v3.sh | cut -c1-16)" = 24d5d16c7cb4ee85 ] || { echo "enveloppe Argon non conforme" >&2; exit 2; }
[ "$(sha256sum /opt/argon/commande_argon_v2.py | cut -c1-16)" = 6905ac71f126bfd4 ] || { echo "commande Argon non conforme" >&2; exit 2; }
for port in 8787 8788; do  # au 30 octobre ≈ 08:30 UTC : pris par les relais de la course (PID 24293, 24295), à arrêter par PID d'abord
  python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',$port)) else 1)" || { echo "port $port déjà pris" >&2; exit 2; }; done

J=(--juges-seulement $COURSE --empreinte-manifeste-fin $FIN_SHA --empreinte-fiches-validees $FICHES_SHA
   --liste-blanche $DOS/liste-blanche-ideation-v4-session-depot-v1.json --question $P/question-collisionneur-priorites-sept-questions-v3.md
   --temoins $DOS/temoins/temoins-ideation-tiers-v1.json)
for f in extraits-v1/anteriorite-Q{1,2,3,4,5,6,7,pont}-sections-1-a-3-v1.md anteriorite-coevolution-et-boite-blanche-v1.md; do J+=(--piece-juge $P/$f); done
for f in $CORPUS; do J+=(--piece-juge $f); done
J+=(--juge juge-opus=claude-opus-5-5 --juge-externe argon-juge=gemini-4-argon --bascule-declaree claude-opus-5-5=claude-opus-4-6
    --budget 'juge_ideation|claude-opus-5-5=4' --budget 'juge_ideation|claude-opus-4-6=4' --budget 'juge_ideation|gemini-4-argon=3.5'
    --budget-total-usd 10 --budget-externe-usd 4 --budget-controle-usd 0.2 --prix-entree-usd-par-million-jetons 8.3
    --delai-session-s 3600 --delai-commande-s 1800 --racine-depot $DEPOT)

# (1) vérification sans appel ni écriture
cd $O && env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 python3 -I -B demonstrations/ideation_v3.py "${J[@]}" --verifier-seulement \
  > $DOS/verification-juges-course-v2.json 2>&1 || { echo "vérification en échec (rien payé)" >&2; exit 4; }
sha256sum $DOS/verification-juges-course-v2.json > $DOS/verification-juges-course-v2.json.sha256
python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); r=d['reconstruction_des_consignes_de_la_course']; \
assert d['fiches_servies']==29 and r and all(v['identique'] for v in r.values()), 'reconstruction'; print(json.dumps(d['attestation_a_signer']))" \
  $DOS/verification-juges-course-v2.json || { echo "vérification : 29 fiches et consignes reconstruites attendues" >&2; exit 4; }

# (2) essai à blanc : moteur simulé, vraies fiches, aucune commande externe (aucun appel vers Argon)
code=0
cd $O && env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 python3 -I -B demonstrations/ideation_v3.py $BLANC "${J[@]}" --moteur simule \
  --horodatage "$(date -u)" > $DOS/essai-blanc-juges-course-v2.log 2>&1 || code=$?
sha256sum $DOS/essai-blanc-juges-course-v2.log > $DOS/essai-blanc-juges-course-v2.log.sha256
[ "$code" = 0 ] || [ "$code" = 4 ] || { echo "essai à blanc : code $code (attendu 0 ou 4) : arrêt, rien payé" >&2; exit 4; }
(cd $BLANC && sha256sum -c --quiet empreintes-sortie.txt) || { echo "essai à blanc : sortie mal scellée" >&2; exit 4; }

# (3) attestation de lecture humaine (juge externe) : sans elle, arrêt avant les relais
[ -n "${ATTESTATION:-}" ] && [ -f "$ATTESTATION" ] && [ -f "$ATTESTATION.sha256" ] \
  || { echo "ATTESTATION absente : signer l'attestation (empreintes ci-dessus), la sceller, relancer ; rien payé" >&2; exit 5; }

# R10 : les relais sont lancés SANS setsid ni nohup, pour que $! soit le PID du processus python lui-même. Constaté le 30 octobre
# (≈ 08:30 UTC) : avec `setsid nohup …`, setsid a fourché ; lancer-course-v2.sh a arrêté 24291 et 24292 (les setsid), et les relais
# de la course (python, PID 24293 et 24295) sont restés vivants sur 8787 et 8788. Ici : PID vérifié par /proc/PID/cmdline, arrêt
# vérifié (kill, puis attente de la fin du processus, puis SIGKILL par le même PID s'il survit).
PID_C=""; PID_G=""
verifier_pid() { tr '\0' ' ' < /proc/$1/cmdline 2>/dev/null | grep -q -- "$2" || { echo "PID $1 n'est pas $2 (R10)" >&2; exit 3; }; }
arreter_pid() { local p=$1 i=0; [ -n "$p" ] || return 0; kill "$p" 2>/dev/null
  while kill -0 "$p" 2>/dev/null && [ $i -lt 20 ]; do sleep 0.5; i=$((i+1)); done
  kill -0 "$p" 2>/dev/null && kill -9 "$p" 2>/dev/null; kill -0 "$p" 2>/dev/null && echo "PID $p toujours vivant" >&2; true; }
arreter() { arreter_pid "$PID_C"; arreter_pid "$PID_G"; }
trap arreter EXIT
trap 'arreter; exit 130' INT TERM HUP

# (4) relais : Claude v2 (plafond 20, réserve 4, modèles permis exacts) ; Gemini (8 appels au plus) ; clés par variable sous env -i
cd $O  # commande simple en arrière-plan (pas de liste « a && b & ») : $! est le PID de python (env l'exécute)
env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 HTTPS_PROXY="${HTTPS_PROXY:-}" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt \
  ANTHROPIC_API_KEY="$RR_ANTHROPIC_API_KEY_3" python3 -I pole/relais_reel_v2.py --port 8787 --variable-cle ANTHROPIC_API_KEY \
  --plafond-usd 20 --reserve-par-appel 4 --modeles-permis claude-opus-5-5,claude-opus-4-6 \
  --journal $DOS/relais-juges-journal-v1.jsonl > $DOS/relais-juges-v1.log 2>&1 &
PID_C=$!; echo "$PID_C" > $DOS/relais-juges-v1.pid; sleep 0.5; verifier_pid $PID_C relais_reel_v2.py
cd $DOS
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" HTTPS_PROXY="${HTTPS_PROXY:-}" \
  SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 -I -B $RELAIS_G --port 8788 --max-appels 8 \
  --journal $DOS/relais-gemini-juges-journal-v1.jsonl > $DOS/relais-gemini-juges-v1.log 2>&1 &
PID_G=$!; echo "$PID_G" > $DOS/relais-gemini-juges-v1.pid; sleep 0.5; verifier_pid $PID_G relais_gemini_v1.py
for port in 8787 8788; do i=0
  until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:$port/relais/etat', timeout=2)" 2>/dev/null; do
    i=$((i+1)); [ $i -lt 30 ] || { echo "relais $port non prêt" >&2; exit 3; }; sleep 1; done; done
python3 -I -c "import json,urllib.request; d=json.load(urllib.request.urlopen('http://127.0.0.1:8787/relais/etat')); print('relais claude', d.get('version_relais'), d.get('modeles_permis'))"

# (5) mode réel (l'orchestrateur fait les appels de contrôle, vérifie relais, attestation et modèles servis)
echo "début des juges : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
code=0
cd $O && env -i PATH=/usr/bin:/bin HOME=$DOS LANG=C.UTF-8 GO_ID="$GO_ID" python3 -I -B demonstrations/ideation_v3.py $SORTIE "${J[@]}" \
  --moteur claude-sdk --url-relais http://127.0.0.1:8787 --confirmer-moteur-reel --commande-externe "$CMD_ARGON" \
  --attestation-lecture-humaine "$ATTESTATION" --horodatage "$(date -u)" > $DOS/juges-course-v2.log 2>&1 || code=$?
echo "fin des juges : $(date -u +%Y-%m-%dT%H:%M:%SZ), code $code"

# (6) état final des relais, arrêt par PID (R10), scellement des fichiers hors sortie
python3 -I -c "import json,urllib.request; print('claude', json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:8787/relais/etat')))[:900])" 2>/dev/null \
  > $DOS/relais-juges-etat-final-v1.txt || true
python3 -I -c "import json,urllib.request; print('gemini', json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:8788/relais/etat')))[:600])" 2>/dev/null \
  >> $DOS/relais-juges-etat-final-v1.txt || true
arreter; trap - EXIT; echo "relais arrêtés : $PID_C (claude), $PID_G (gemini)"
cd $DOS && for f in juges-course-v2.log relais-juges-journal-v1.jsonl relais-juges-v1.log relais-gemini-juges-journal-v1.jsonl \
                    relais-gemini-juges-v1.log relais-juges-etat-final-v1.txt; do
  [ -e "$f" ] && sha256sum "$f" > "$f.sha256"; done
exit $code
