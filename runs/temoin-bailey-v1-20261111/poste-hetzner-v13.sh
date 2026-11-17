#!/bin/bash
# Poste Hetzner du témoin de Bailey, v13 — RUN DE CONFIRMATION (R12 ; v1 à v12 restent telles quelles ; addendum 7).
# v13 = v12 avec la conduite v15 (`lanceur_v21`, conduite normale, B = 85), le manifeste v7, la garde du commit du code
# a904aa39, et le filtre d'offre de l'addendum 7, § 2.4 : `cpu_cores_effective>=32 cpu_ghz>=2.4` à la recherche, et un
# coût (carte et 110 Go de stockage) d'au plus 1,6 USD/h au choix.
# v12 — RELANCE SEULE (R12 ; v1 à v11 restent telles quelles ; addendum 5).
# v12 = v11 avec la conduite de relance v13 (`lanceur_v20`, `relance_seule`), le manifeste v6 et la garde du commit du
# code v20 (f60c2620) au lieu de 8d1c541e.
# v11 (R12 ; v1 à v10 restent telles quelles). v11 = v10 avec la conduite v11
# (la conduite v10 avait un défaut de syntaxe ; le poste v10 n'a jamais tourné).
# v10 (R12 ; v1 à v9 restent telles quelles). v10 = v9 avec la conduite v10 (code v17 :
# lanceur_v17, instance_v16, execution_v4 ; addendum 4) et la garde du commit du code v17 (8d1c541e) au lieu de 91238a73.
# v9 (R12 ; v1 à v8 restent telles quelles). v9 = v8 avec la conduite v9 (envoi de
# fichier retenté).
# v8 (R12 ; v1 à v7 restent telles quelles). v8 = v7 + garde K-6 (c) de la
# contre-lecture de l'addendum 3 : avant la conduite, le code `src/` de la tête de branche doit être identique à celui du
# commit du code (91238a73), sinon rien ne tourne. La v7 n'a jamais tourné.
# v7 (R12 ; v1 à v6 restent telles quelles). v7 = v6 avec la conduite v8 (code v16 :
# lanceur_v16, instance_v15, commit 91238a73). La v6 (code v14) n'a jamais tourné.
# v6 (R12 ; v1 à v5 restent telles quelles). v6 = v5 avec la conduite v7 (code v14 :
# lanceur_v14, instance_v13 ; addendum 3) et la vérification du commit 4821ad7e au lieu de 4988f3f4.
# v5 (R12 ; v1 à v4 restent telles quelles). v5 = v4 avec la conduite v6 (disque
# demandé 110 Go) et le filtre de disque à 115 Go au lieu de 210 (aucune A100 80 Go à 200 Go louable à 14:57Z).
# v4 (R12 ; v1 à v3 restent telles quelles). v4 = v3 avec le filtre de mémoire vive
# allouée à 128,9 Go : les offres annoncées « 129 Go » ont 128 980 Mo et échouent à « >= 129 » (relevé de 14:53Z) ; mot de
# Lazar : « on loue ce qu'il y a now ». La garde du préenregistrement (128 × 10⁹ octets) est inchangée.
# v3 (R12 ; v1 et v2 restent telles quelles). v3 = v2 avec le filtre de mémoire vive
# allouée abaissé de 135 à 129 Go (mot de Lazar, 12 novembre, 14:42Z : « abaisse le filtre à 129 Go maintenant ») ; la garde
# du préenregistrement (128 × 10⁹ octets, à la mise en place) est inchangée.
# v2 (R12 ; la v1 reste telle quelle). v2 = v1 + attente d'une offre conforme : la v1
# s'est arrêtée à 14:34:42Z le 12 novembre faute d'offre conforme (« aucune offre conforme : rien ne tourne ») ; la v2
# relit les offres toutes les 600 s pendant 24 h au plus, et pousse son état toutes les heures pendant l'attente.
# Origine de la v1 : option (c) accordée par Lazar le 12 novembre 2026 : « go c »).
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
#   5. lance `lancer-conduite-v13.py` sous GO_ID=GO-2026-11-10-10 et DEPOT_URL, et pousse les petits journaux de la
#      sortie v5 sur la branche toutes les 10 minutes, puis une dernière fois quand la conduite a fini ;
#   6. écrit la marque `poste-fini-v1.json` et la pousse. La machine est détruite par la session (API Hetzner).
# Aucune note n'est lue ni imprimée ici ; rien n'est relancé ; aucune reprise automatique.
set -uo pipefail
DEPOT=/home/user/controle-ia-travail
BRANCHE=claude/compassionate-meitner-d4ryyk
BASE=$DEPOT/runs/temoin-bailey-v1-20261111
JOURNAL=/root/poste-hetzner-v13.log
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
  for f in "$BASE/sortie-conduite-v15" "$BASE"/lancement-v15.out "$BASE"/lancement-v15.err "$BASE"/lancement-v15.pid \
    "$BASE"/bilan-lancement-v15.json "$BASE"/offre-choisie-v13.json "$BASE"/poste-fini-v13.json \
    "$BASE"/poste-hetzner-v13-etat.txt "$BASE"/repertoires-sortie-conduite-v15-v1.txt "$BASE"/repertoires-sortie-conduite-v15-v1.txt.sha256; do
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
etat() { mkdir -p "$BASE"; echo "$(date -u +%FT%TZ) $1" >> "$BASE/poste-hetzner-v13-etat.txt"; echo "$1"; }

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
printf '%s\n' "$BASE/sortie-conduite-v15/*.battement" >> .git/info/exclude
etat "dépôt cloné : $(git rev-parse HEAD)"

# 3. empreintes et environnement Python
(cd "$BASE" && sha256sum -c --quiet lancer-conduite-v15.py.sha256 manifeste-local-v7.json.sha256) \
  || { etat "empreinte du script ou du manifeste différente : rien ne tourne"; pousser "empreinte en échec"; exit 3; }
git cat-file -e a904aa391cdcf2650b747fe64e48caa0ec8c5849^{commit} \
  || { etat "commit du code a904aa39 absent : rien ne tourne"; pousser "commit absent"; exit 3; }
git diff --quiet a904aa391cdcf2650b747fe64e48caa0ec8c5849 HEAD -- src/ \
  || { etat "code src/ de la tête différent du commit a904aa39 : rien ne tourne"; pousser "code différent"; exit 3; }
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
# v2 : attente bornée (144 essais × 600 s = 24 h) ; état poussé tous les 6 essais ; rien n'est loué pendant l'attente
cat > /root/choisir_offre.py <<'EOF'
import json, sys, time
d = json.load(open("/root/offres.json"))
cout = lambda o: o["dph_total"] + o.get("storage_cost", 0) * 110 / 730
d = [o for o in d if cout(o) <= 1.6]  # v13 : plafond de coût, carte et 110 Go (addendum 7, § 2.4)
if not d:
    sys.exit(1)
o = min(d, key=cout)
choix = {"offre": str(o["id"]), "gpu": o["gpu_name"], "dph_total": o["dph_total"], "cout_avec_200_go": round(cout(o), 4),
         "cpu_ram_go": round(o["cpu_ram"] / 1000), "fiabilite": o.get("reliability2", o.get("reliability")),
         "verification": o.get("verification"), "cuda": o.get("cuda_max_good"), "lieu": o.get("geolocation"),
         "nombre_offres": len(d), "heure": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
json.dump(choix, open(sys.argv[1], "w"), ensure_ascii=False, indent=2, sort_keys=True)
EOF
for n in $(seq 1 144); do
  if vastai search offers 'gpu_name in [A100_SXM4,A100_PCIE] num_gpus=1 gpu_ram>=79 cpu_ram>=128.9 disk_space>=115 reliability>0.97 cuda_vers>=12.4 direct_port_count>=1 rentable=true cpu_cores_effective>=32 cpu_ghz>=2.4' -o dph --raw > /root/offres.json; then
    python3 /root/choisir_offre.py "$BASE/offre-choisie-v13.json" && break
  else
    etat "recherche d'offres en échec (essai $n)"
  fi
  [ $((n % 6)) -eq 1 ] && { etat "aucune offre conforme (essai $n sur 144)"; pousser "attente d'une offre (essai $n)"; }
  sleep 600
done
[ -s "$BASE/offre-choisie-v13.json" ] || { etat "aucune offre conforme en 24 h : rien ne tourne"; pousser "aucune offre en 24 h"; exit 3; }
OFFRE=$(python3 -c "import json;print(json.load(open('$BASE/offre-choisie-v13.json'))['offre'])")
etat "offre choisie : $OFFRE"
pousser "offre choisie ($OFFRE)"

# 5. conduite, poussées régulières
export GO_ID=GO-2026-11-17-07 DEPOT_URL=https://github.com/lciric/controle-ia-travail.git PYTHONPATH=$DEPOT/src
nohup setsid python "$BASE/lancer-conduite-v15.py" --offre "$OFFRE" \
  --image runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04 \
  > "$BASE/lancement-v15.out" 2> "$BASE/lancement-v15.err" < /dev/null &
sleep 20
P=$(cat "$BASE/lancement-v15.pid" 2>/dev/null || true)
[ -n "$P" ] || { etat "conduite non lancée (PID absent)"; pousser "conduite non lancée"; exit 3; }
etat "conduite lancée, PID $P"
pousser "conduite lancée (PID $P)"
while kill -0 "$P" 2>/dev/null; do
  sleep 600
  pousser "journaux $(date -u +%H:%MZ)"
done
etat "conduite terminée"
# v13 : liste de tous les répertoires de la sortie (addendum 7, § 3), hors de la sortie, avant la marque de fin
if [ -d "$BASE/sortie-conduite-v15" ]; then
  (cd "$BASE/sortie-conduite-v15" && find . -mindepth 1 -type d -printf '%P\n' | LC_ALL=C sort > "$BASE/repertoires-sortie-conduite-v15-v1.txt")
  (cd "$BASE" && [ -f repertoires-sortie-conduite-v15-v1.txt ] && LC_ALL=C sha256sum repertoires-sortie-conduite-v15-v1.txt > repertoires-sortie-conduite-v15-v1.txt.sha256)
  etat "liste des répertoires écrite : $(wc -l < "$BASE/repertoires-sortie-conduite-v15-v1.txt" 2>/dev/null) entrées"
else
  etat "sortie de la conduite absente : aucune liste des répertoires"
fi
pousser "liste des répertoires de la sortie"
printf '{"fini": "%s", "pid": %s}\n' "$(date -u +%FT%TZ)" "$P" > "$BASE/poste-fini-v13.json"
pousser "conduite terminée"
echo "fin $(date -u +%FT%TZ)"
