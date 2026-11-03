#!/bin/bash
# Lance le relais Argon 8805 pour A1-v3 ; écrit le PID dans relais-argon.pid. La clé passe par l'environnement seulement.
D=/home/user/hors-clone-a1-v3
N=/home/user/controle-ia-travail/donnees/mini-course-kimi-argon-v1/orchestrateur/nuit
EXTRA=()
[ -n "${https_proxy+x}" ] && EXTRA+=("https_proxy=$https_proxy")
[ -n "${NO_PROXY+x}" ] && EXTRA+=("NO_PROXY=$NO_PROXY")
[ -n "${no_proxy+x}" ] && EXTRA+=("no_proxy=$no_proxy")
cd $D
nohup setsid env -i PATH=/usr/bin:/bin LANG=C.UTF-8 GEMINI_API_KEY="$GEMINI_API_KEY_2" HTTPS_PROXY="$HTTPS_PROXY" SSL_CERT_FILE=/root/.ccr/ca-bundle.crt "${EXTRA[@]}" \
  /usr/bin/python3 -I -B $N/commande_argon_v56_nuit_v2.py servir --port 8805 --plafond-usd 410 --max-appels 9000 \
  --journal $D/relais-argon-journal-a1-v3.jsonl >> $D/relais-argon-stdout-a1-v3.log 2>&1 < /dev/null &
echo $! > $D/relais-argon.pid
echo $!
