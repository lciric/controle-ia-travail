#!/bin/bash
# Poste Hetzner de REPRISE du témoin de Bailey, v1 (troisième série, addendum 4). Construit sur le poste v11 (sections 1 à
# 3 reprises : secrets, outils, dépôt, empreintes, garde du commit du code 8d1c541e, environnement Python), sans
# recherche d'offre ni conduite : il lance `lanceur_v17 reprendre` (lecture 38 de l'addendum 2 : redémarrage de
# l'instance arrêtée le temps du seul transfert, comparaison des empreintes, scellement, destruction par identifiant ;
# aucune reprise du calcul) sur l'instance 60417353 (étiquette temoin-bailey-c6-89bd4d5cb025406c), arrêtée « exited »
# le 13 novembre à ≈ 04:55Z avant un transfert qui fasse foi (bilan `sortie-conduite-v11/bilan-conduite-v5.json`).
# `--sortie` : le même chemin absolu que la conduite v11 (A-1 de la relecture v13). Il pousse `sortie-conduite-v11`
# (dont `reprise-v10*/`) et ses propres journaux toutes les 10 minutes, puis une dernière fois.
set -uo pipefail
DEPOT=/home/user/controle-ia-travail
BRANCHE=claude/compassionate-meitner-d4ryyk
BASE=$DEPOT/runs/temoin-bailey-v1-20261111
JOURNAL=/root/poste-hetzner-reprise-v1.log
exec >>"$JOURNAL" 2>&1
echo "début $(date -u +%FT%TZ)"

# 1. secrets (les blocs sont remplacés par le constructeur des données de démarrage)
umask 077
mkdir -p /root/.ssh
cat > /root/.ssh/deploiement <<'@@CLE_DEPLOIEMENT_FIN@@'
@@CLE_DEPLOIEMENT@@
@@CLE_DEPLOIEMENT_FIN@@
cat > /root/.ssh/id_ed25519 <<'@@CLE_VAST_FIN@@'
@@CLE_VAST@@
@@CLE_VAST_FIN@@
cat > /root/secrets.env <<'@@SECRETS_FIN@@'
@@SECRETS@@
@@SECRETS_FIN@@
chmod 600 /root/.ssh/deploiement /root/.ssh/id_ed25519 /root/secrets.env
umask 022

pousser() {  # $1 : message ; pousse les seuls fichiers de la sortie v5 et du poste
  cd "$DEPOT" || return 1
  local f
  for f in "$BASE/sortie-conduite-v11" "$BASE"/reprise-v1.out "$BASE"/reprise-v1.err "$BASE"/reprise-v1.pid \
    "$BASE"/poste-fini-reprise-v1.json "$BASE"/poste-hetzner-reprise-v1-etat.txt; do
    [ -e "$f" ] && git add -A "$f"
  done
  git diff --cached --quiet && return 0
  git commit -q -m "Témoin de Bailey, poste Hetzner : $1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XJ6MgnEhQMZteN9F8a1BST"
  for i in 1 2 3 4; do
    git pull -q --rebase origin "$BRANCHE" && git push -q origin "HEAD:$BRANCHE" && return 0
    git rebase --abort 2>/dev/null; sleep $((2 ** i))
  done
  echo "poussée en échec $(date -u +%FT%TZ)"
}
etat() { mkdir -p "$BASE"; echo "$(date -u +%FT%TZ) $1" >> "$BASE/poste-hetzner-reprise-v1-etat.txt"; echo "$1"; }

# 2. outils et dépôt
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq && apt-get install -y -qq git openssh-client python3-venv python3-pip ca-certificates curl \
  || { echo "installation apt en échec"; exit 3; }
ssh-keyscan -t ed25519 github.com >> /root/.ssh/known_hosts 2>/dev/null
export GIT_SSH_COMMAND="ssh -i /root/.ssh/deploiement -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes"
mkdir -p /home/user
git clone -q --single-branch --branch "$BRANCHE" git@github.com:lciric/controle-ia-travail.git "$DEPOT" \
  || { echo "clonage en échec"; exit 3; }
cd "$DEPOT"
git config user.name "Claude"; git config user.email "noreply@anthropic.com"
git fetch -q origin +refs/heads/main:refs/remotes/origin/main || { etat "récupération de main en échec"; pousser "main illisible"; exit 3; }
printf '%s\n' "$BASE/sortie-conduite-v11/*.battement" "$BASE/sortie-conduite-v11/**/*.battement" "*.battement" >> .git/info/exclude
etat "dépôt cloné : $(git rev-parse HEAD)"

# 3. empreintes et environnement Python
(cd "$BASE" && sha256sum -c --quiet poste-hetzner-reprise-v1.sh.sha256 manifeste-local-v5.json.sha256) \
  || { etat "empreinte du script ou du manifeste différente : rien ne tourne"; pousser "empreinte en échec"; exit 3; }
git cat-file -e 8d1c541ef7a3ac99f942e0b2f26567088f2cc503^{commit} \
  || { etat "commit du code 8d1c541e absent : rien ne tourne"; pousser "commit absent"; exit 3; }
git diff --quiet 8d1c541ef7a3ac99f942e0b2f26567088f2cc503 HEAD -- src/ \
  || { etat "code src/ de la tête différent du commit 8d1c541e : rien ne tourne"; pousser "code différent"; exit 3; }
python3 -m venv .venv && . .venv/bin/activate && pip install -q numpy==2.4.6 vastai==1.11.0 \
  || { etat "environnement Python en échec : rien ne tourne"; pousser "Python en échec"; exit 3; }
etat "Python $(python --version 2>&1) ; vastai $(vastai --version 2>&1 | tail -1)"

# secrets en variables (le fichier n'est jamais imprimé)
set -a; . /root/secrets.env; set +a
[ -n "${VAST_API_KEY:-}" ] && [ -n "${HF_TOKEN:-}" ] || { etat "clés absentes : rien ne tourne"; pousser "clés absentes"; exit 3; }

# inventaire R10 : aucune instance du poste ne doit exister avant la création
vastai show instances --raw > /root/inventaire-avant.json \
  || { etat "inventaire Vast illisible : rien ne tourne"; pousser "inventaire illisible"; exit 3; }
python3 - <<'EOF' || { etat "instance du poste déjà présente : rien ne tourne"; pousser "inventaire non vide"; exit 3; }
import json, sys
d = json.load(open("/root/inventaire-avant.json"))
sys.exit(1 if any(str(i.get("label") or "").startswith("temoin-bailey-c6-") for i in d) else 0)
EOF


# secrets en variables (le fichier n'est jamais imprimé)
set -a; . /root/secrets.env; set +a
[ -n "${VAST_API_KEY:-}" ] || { etat "clé Vast absente : rien ne tourne"; pousser "clé absente"; exit 3; }

# inventaire R10 : l'instance à reprendre doit exister, arrêtée ; aucune autre instance du témoin
vastai show instances --raw > /root/inventaire-avant.json \
  || { etat "inventaire Vast illisible : rien ne tourne"; pousser "inventaire illisible"; exit 3; }
python3 - <<'EOF2' || { etat "inventaire non conforme : rien ne tourne"; pousser "inventaire non conforme"; exit 3; }
import json, sys
d = json.load(open("/root/inventaire-avant.json"))
t = [i for i in d if str(i.get("label") or "").startswith("temoin-bailey-c6-")]
ok = len(t) == 1 and str(t[0]["id"]) == "60417353" and t[0].get("label") == "temoin-bailey-c6-89bd4d5cb025406c"
print("instances du témoin :", [(i["id"], i.get("actual_status")) for i in t])
sys.exit(0 if ok else 1)
EOF2
etat "inventaire conforme : 60417353 seule instance du témoin"

# 4. reprise (lecture 38), poussées régulières
export GO_ID=GO-2026-11-10-10 DEPOT_URL=https://github.com/lciric/controle-ia-travail.git PYTHONPATH=$DEPOT/src
[ -e "$BASE/reprise-v1.pid" ] && { etat "PID de reprise déjà présent (R12) : rien ne tourne"; pousser "PID présent"; exit 3; }
cd "$DEPOT"
nohup setsid python -m controle_ia.temoin_bailey.lanceur_v17 reprendre \
  --sortie "$BASE/sortie-conduite-v11" --etiquette temoin-bailey-c6-89bd4d5cb025406c \
  --go-id GO-2026-11-10-10 --depot "$DEPOT" \
  > "$BASE/reprise-v1.out" 2> "$BASE/reprise-v1.err" < /dev/null &
P=$!
echo "$P" > "$BASE/reprise-v1.pid"
etat "reprise lancée, PID $P"
pousser "reprise lancée (PID $P)"
while kill -0 "$P" 2>/dev/null; do
  sleep 600
  pousser "reprise : journaux $(date -u +%H:%MZ)"
done
wait "$P"; C=$?
etat "reprise terminée, code $C"
printf '{"fini": "%s", "pid": %s, "code": %s}\n' "$(date -u +%FT%TZ)" "$P" "$C" > "$BASE/poste-fini-reprise-v1.json"
pousser "reprise terminée (code $C)"
echo "fin $(date -u +%FT%TZ)"
