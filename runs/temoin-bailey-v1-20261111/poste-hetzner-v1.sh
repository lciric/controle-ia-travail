#!/bin/bash
# Poste Hetzner du témoin de Bailey, v1 (option (c) accordée par Lazar le 12 novembre 2026 : « go c »).
# Script de démarrage (données de démarrage de la machine, exécuté une fois par cloud-init, en root). Il remplace le
# poste local, que la session ne peut pas tenir : elle n'ouvre aucune connexion `ssh` (port 22 refusé, 443 intercepté).
#
# Ce qu'il fait, dans l'ordre :
#   1. pose les secrets reçus dans les données de démarrage (jamais imprimés) : clé de déploiement GitHub, clé `ssh` de
#      session enregistrée sur Vast (1864483), VAST_API_KEY et HF_TOKEN dans un fichier 600 ;
#   2. installe git, ssh, python3-venv (Debian 12 : Python 3.11) ; clone la branche de travail dans le même chemin
#      absolu que la session (/home/user/controle-ia-travail) et récupère `main` (refspec explicite) ;
#   3. vérifie l'empreinte du script de conduite v5 contre son compagnon ; installe numpy et vastai 1.11.0 ;
#   4. choisit l'offre Vast la moins chère du filtre de l'ordre de lancement (carte et stockage de 200 Go), l'écrit ;
#   5. lance `lancer-conduite-v5.py` sous GO_ID=GO-2026-11-10-10 et DEPOT_URL, et pousse les petits journaux de la
#      sortie v5 sur la branche toutes les 10 minutes, puis une dernière fois quand la conduite a fini ;
#   6. écrit la marque `poste-fini-v1.json` et la pousse. La machine est détruite par la session (API Hetzner).
# Aucune note n'est lue ni imprimée ici ; rien n'est relancé ; aucune reprise automatique.
set -uo pipefail
DEPOT=/home/user/controle-ia-travail
BRANCHE=claude/compassionate-meitner-d4ryyk
BASE=$DEPOT/runs/temoin-bailey-v1-20261111
JOURNAL=/root/poste-hetzner-v1.log
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
  for f in "$BASE/sortie-conduite-v5" "$BASE"/lancement-v5.out "$BASE"/lancement-v5.err "$BASE"/lancement-v5.pid \
    "$BASE"/bilan-lancement-v5.json "$BASE"/offre-choisie-v5.json "$BASE"/poste-fini-v1.json \
    "$BASE"/poste-hetzner-v1-etat.txt; do
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
etat() { mkdir -p "$BASE"; echo "$(date -u +%FT%TZ) $1" >> "$BASE/poste-hetzner-v1-etat.txt"; echo "$1"; }

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
printf '%s\n' "$BASE/sortie-conduite-v5/*.battement" >> .git/info/exclude
etat "dépôt cloné : $(git rev-parse HEAD)"

# 3. empreintes et environnement Python
(cd "$BASE" && sha256sum -c --quiet lancer-conduite-v5.py.sha256 manifeste-local-v3.json.sha256) \
  || { etat "empreinte du script ou du manifeste différente : rien ne tourne"; pousser "empreinte en échec"; exit 3; }
git cat-file -e 4988f3f442c670887a0e8ad15ddfbac68a173d03^{commit} \
  || { etat "commit du code 4988f3f4 absent : rien ne tourne"; pousser "commit absent"; exit 3; }
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

# 4. offre : filtre de l'ordre de lancement, moins chère carte et 200 Go de stockage compris
vastai search offers 'gpu_name in [A100_SXM4,A100_PCIE] num_gpus=1 gpu_ram>=79 cpu_ram>=135 disk_space>=210 reliability>0.97 cuda_vers>=12.4 direct_port_count>=1 rentable=true' -o dph --raw > /root/offres.json \
  || { etat "recherche d'offres en échec : rien ne tourne"; pousser "offres illisibles"; exit 3; }
python3 - "$BASE/offre-choisie-v5.json" <<'EOF' || { etat "aucune offre conforme : rien ne tourne"; pousser "aucune offre"; exit 3; }
import json, sys, time
d = json.load(open("/root/offres.json"))
cout = lambda o: o["dph_total"] + o.get("storage_cost", 0) * 200 / 730
if not d:
    sys.exit(1)
o = min(d, key=cout)
choix = {"offre": str(o["id"]), "gpu": o["gpu_name"], "dph_total": o["dph_total"], "cout_avec_200_go": round(cout(o), 4),
         "cpu_ram_go": round(o["cpu_ram"] / 1000), "fiabilite": o.get("reliability2", o.get("reliability")),
         "verification": o.get("verification"), "cuda": o.get("cuda_max_good"), "lieu": o.get("geolocation"),
         "nombre_offres": len(d), "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
json.dump(choix, open(sys.argv[1], "w"), ensure_ascii=False, indent=2, sort_keys=True)
EOF
OFFRE=$(python3 -c "import json;print(json.load(open('$BASE/offre-choisie-v5.json'))['offre'])")
etat "offre choisie : $OFFRE"
pousser "offre choisie ($OFFRE)"

# 5. conduite, poussées régulières
export GO_ID=GO-2026-11-10-10 DEPOT_URL=https://github.com/lciric/controle-ia-travail.git PYTHONPATH=$DEPOT/src
nohup setsid python "$BASE/lancer-conduite-v5.py" --offre "$OFFRE" \
  --image runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04 \
  > "$BASE/lancement-v5.out" 2> "$BASE/lancement-v5.err" < /dev/null &
sleep 20
P=$(cat "$BASE/lancement-v5.pid" 2>/dev/null || true)
[ -n "$P" ] || { etat "conduite non lancée (PID absent)"; pousser "conduite non lancée"; exit 3; }
etat "conduite lancée, PID $P"
pousser "conduite lancée (PID $P)"
while kill -0 "$P" 2>/dev/null; do
  sleep 600
  pousser "journaux $(date -u +%H:%MZ)"
done
etat "conduite terminée"
printf '{"fini": "%s", "pid": %s}\n' "$(date -u +%FT%TZ)" "$P" > "$BASE/poste-fini-v1.json"
pousser "conduite terminée"
echo "fin $(date -u +%FT%TZ)"
