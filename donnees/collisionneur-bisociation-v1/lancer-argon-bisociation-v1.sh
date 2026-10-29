#!/bin/sh
# lancer-argon-bisociation-v1.sh — pose la question « recombinaison bisociative à deux espaces » (conv-audit n° 217, `73a30ab7…`) à
# Argon seul (gemini-4-argon), consigne seule (sans les pièces), par la chaîne du 29 octobre : relais Gemini local v1
# (`docs/notes/ideation-organisme-v1/lancement-v2/relais_gemini_v1.py`, `5021021a…`) → enveloppe /opt/argon/appel-argon-v3.sh
# (`24d5d16c…`, aucune clé) → commande_argon_v2.py (`6905ac71…`) sous `setpriv --reuid=argon`.
# GO-2026-10-29-19 (mot direct de Lazar, ≈ 22:30 UTC) ; dépense demandée par Lazar (mot relayé, conv-audit R-514).
# Garde de pire cas (commande_argon_v2.py, avant tout envoi) : question de 6 996 octets, ≈ 1 750 jetons gardés ; avec
# --max-sortie-jetons 32000 et la provision de pensée 8 192 : ≈ 0,015 + (32 000 + 8 192) × 41,5 / 10^6 ≈ 1,68 USD < plafond 3 USD.
# Le relais Gemini (mort avec l'ancien conteneur) est relancé ici, clé passée par variable sous `env -i` (jamais en argument ni en
# fichier), borné à 4 appels, puis arrêté par son PID (R10). En root (setpriv l'exige). Sortie hors dépôt, dossier 700 ;
# elle sera versée sur la branche `donnees/collisionneur-bisociation-v1` ; l'avis d'Argon est « lu à côté » (critères gelés de la question).
set -eu
umask 077
ICI=$(cd "$(dirname "$0")" && pwd)
DEPOT=$(cd "$ICI/../.." && pwd)
QUESTION=question-bisociation-deux-espaces-v1.md
EMPREINTE_ATTENDUE=73a30ab727445969b7ecb8300ba0fef5efd7dfcf9c59cd93943d6ce77e1c4cc3
RELAIS="$DEPOT/docs/notes/ideation-organisme-v1/lancement-v2/relais_gemini_v1.py"
SORTIE=/root/ideation-v1/argon-bisociation-v1
GO_ID=GO-2026-10-29-19
export GO_ID
cd "$ICI"
[ -n "${GEMINI_API_KEY_2:-}" ] || { echo "GEMINI_API_KEY_2 absente" >&2; exit 2; }
[ "$(id -u)" = 0 ] || { echo "setpriv exige root" >&2; exit 11; }
EMPREINTE=$(sha256sum "$QUESTION" | cut -d' ' -f1)
[ "$EMPREINTE" = "$EMPREINTE_ATTENDUE" ] || { echo "empreinte de $QUESTION inattendue : $EMPREINTE" >&2; exit 10; }
sha256sum -c --quiet "$QUESTION.sha256" || { echo "compagnon $QUESTION.sha256 non conforme" >&2; exit 10; }
(cd "$(dirname "$RELAIS")" && sha256sum -c --quiet relais_gemini_v1.py.sha256) || { echo "relais non conforme" >&2; exit 10; }
[ "$(sha256sum /opt/argon/appel-argon-v3.sh | cut -c1-16)" = 24d5d16c7cb4ee85 ] || { echo "enveloppe non conforme" >&2; exit 10; }
[ "$(sha256sum /opt/argon/commande_argon_v2.py | cut -c1-16)" = 6905ac71f126bfd4 ] || { echo "commande non conforme" >&2; exit 10; }
mkdir -p "$SORTIE"; chmod 700 "$SORTIE"
for f in reponse-argon-v1.json reponse-argon-v1.err lancement.txt relais-gemini-journal-v1.jsonl relais-gemini-v1.log; do
    [ ! -e "$SORTIE/$f" ] || { echo "$SORTIE/$f existe déjà (R12)" >&2; exit 12; }
done
if python3 -I -c "import socket,sys; s=socket.socket(); sys.exit(0 if s.connect_ex(('127.0.0.1',8788)) else 1)"; then :; else
    echo "le port 8788 est déjà pris : un relais tourne ? arrêt" >&2; exit 13; fi
# (1) relais, clé par variable sous env -i ; PID consigné
setsid nohup env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" HTTPS_PROXY="${HTTPS_PROXY:-}" \
    SSL_CERT_FILE="${SSL_CERT_FILE:-/root/.ccr/ca-bundle.crt}" python3 -I -B "$RELAIS" --port 8788 --max-appels 4 \
    --journal "$SORTIE/relais-gemini-journal-v1.jsonl" > "$SORTIE/relais-gemini-v1.log" 2>&1 &
PID_RELAIS=$!
echo "$PID_RELAIS" > "$SORTIE/relais-gemini.pid"
arreter() { kill "$PID_RELAIS" 2>/dev/null || true; }
trap arreter EXIT
i=0; until python3 -I -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8788/relais/etat', timeout=2)" 2>/dev/null; do
    i=$((i+1)); [ $i -lt 30 ] || { echo "relais non prêt" >&2; exit 14; }; sleep 1; done
# (2) journal de lancement
{
    echo "go: $GO_ID"; echo "question: $ICI/$QUESTION"; echo "empreinte_question: $EMPREINTE"; echo "pid_relais: $PID_RELAIS"
    echo "commande: printf '%s' \"\$(cat $QUESTION)\" | PLAFOND_SESSION_USD=3 ROLE_POLE=proposeur_ideation /usr/bin/timeout 1900 /usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v3.sh --max-sortie-jetons 32000"
    echo "debut_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$SORTIE/lancement.txt"
# (3) envoi
code=0
printf '%s' "$(cat "$QUESTION")" | PLAFOND_SESSION_USD=3 ROLE_POLE=proposeur_ideation /usr/bin/timeout 1900 /usr/bin/setpriv --reuid=argon --regid=argon --init-groups /opt/argon/appel-argon-v3.sh --max-sortie-jetons 32000 > "$SORTIE/reponse-argon-v1.json" 2> "$SORTIE/reponse-argon-v1.err" || code=$?
# (4) fin, arrêt du relais par PID (R10), scellement
arreter; trap - EXIT
{ echo "fin_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"; echo "code_retour: $code"; echo "relais_arrete_pid: $PID_RELAIS"; } >> "$SORTIE/lancement.txt"
cd "$SORTIE"
for f in reponse-argon-v1.json reponse-argon-v1.err lancement.txt relais-gemini-journal-v1.jsonl relais-gemini-v1.log; do
    [ -e "$f" ] && sha256sum "$f" > "$f.sha256"
done
echo "fini : code $code ; sorties dans $SORTIE" >&2
exit "$code"
