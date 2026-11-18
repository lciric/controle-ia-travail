#!/bin/bash
# Poste Hetzner de REPRISE du témoin de Bailey, v7 dit « v6 bis » (R12 ; v1 à v6 restent tels quels) — variante B′ du
# repli de la relance (conduite v16, instance 61170458 EN MARCHE) : `reprendre --arreter-en-cours`, sans redémarrage,
# après destruction du serveur du poste v14 (176575468) par la session et poussée de `arret-conduite-v16-poste-v14.json`.
# v7 = v6 dont changent seulement cette garde, l'inventaire (instance en marche), la garde de crédit (au moins 1,0 USD),
# l'option et les noms. Les lignes d'en-tête des versions antérieures, ci-dessous, restent telles quelles.
# Poste Hetzner de REPRISE du témoin de Bailey, v6 (R12 ; v1 à v5 restent tels quels) — reprise de la RELANCE de la
# confirmation (conduite v16, instance 61170458, étiquette temoin-bailey-c6-845f37c35eba4a3d), option B du plan de
# sauvegarde du 18 novembre (crédit épuisé, plus aucune recharge). v6 = v5 dont changent seulement la sortie
# (`sortie-conduite-v16`), l'instance et son étiquette, la garde « conduite v16 finie » (`poste-fini-v14.json`), les
# listes des répertoires et les noms ; garde de crédit au moins 2,0 USD (billing_failed non bloquant) ; inventaire avec
# statut voulu arrêté ; `reprendre` écrira `sortie-conduite-v16/reprise-v10/`. Les lignes d'en-tête des
# versions antérieures, ci-dessous, restent telles quelles (elles parlent de la conduite v15 et de 61049303).
# Poste Hetzner de REPRISE du témoin de Bailey, v5 (R12 ; v1 à v4 restent tels quels). v5 = v4 dont seuls changent
# les noms (journal, PID, sorties, marque de fin, état, script) : nouvel essai de la reprise après le refus de redémarrage
# de la v4 (18 novembre, 02:02Z) ; `reprendre` écrira `sortie-conduite-v15/reprise-v10-2/`.
# Poste Hetzner de REPRISE du témoin de Bailey, v4 — REPRISE DE LA CONFIRMATION (addendum 7 ; R12 : v1 à v3 restent telles
# quelles). v4 = v3 avec : sortie `sortie-conduite-v15`, `lanceur_v21 reprendre`, instance 61049303 (étiquette
# temoin-bailey-c6-40eb0b51dade4963, arrêtée par Vast faute de crédit le 17 novembre vers 17:12Z), GO-2026-11-17-07,
# manifeste v7, garde du commit du code a904aa39, noms neufs, garde « conduite v15 finie », liste des répertoires de
# chaque dossier de reprise écrite, scellée et poussée avant la marque de fin (addendum 7, § 3). `reprendre` écrit ici dans
# `sortie-conduite-v15/reprise-v10/` (ou `reprise-v10-<n>`), jamais d'écrasement. Étiquette et identifiant : relevé
# `vastai show instance 61049303` et ligne de création de `sortie-conduite-v15/conduite-v5.jsonl` (17 novembre).
# v4 (contre-lecture) : instance exigée arrêtée ; garde de crédit ; dossiers de reprise antérieurs non listés.
# Poste Hetzner de REPRISE du témoin de Bailey, v3 (R12 ; v1 et v2 restent telles quelles). v3 = v2 avec des noms
# neufs (la v2 a tourné le 13 novembre à 05:57Z : redémarrage refusé, compte Vast sans crédit) ; relancée après le crédit
# du compte par Lazar (« crédité, relance la reprise »). `reprendre` écrit dans `reprise-v10-2/` (jamais d'écrasement).
# v2 (R12 ; la v1 reste telle quelle). v2 = v1 sans le bloc repris du
# poste v11 (secrets attendus et garde « aucune instance du témoin avant la création »), contraire à une reprise : la v1
# s'est arrêtée à 05:52:54Z le 13 novembre sur cette garde, sans rien toucher.
# v1 (troisième série, addendum 4). Construit sur le poste v11 (sections 1 à
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
JOURNAL=/root/poste-hetzner-reprise-v7.log
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

pousser() {  # $1 : message ; pousse les seuls fichiers de la sortie de la conduite v16, des listes des répertoires de reprise et du poste
  cd "$DEPOT" || return 1
  local f
  for f in "$BASE/sortie-conduite-v16" "$BASE"/reprise-v7.out "$BASE"/reprise-v7.err "$BASE"/reprise-v7.pid \
    "$BASE"/poste-fini-reprise-v7.json "$BASE"/poste-hetzner-reprise-v7-etat.txt "$BASE"/repertoires-sortie-conduite-v16--reprise-v10*; do
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
etat() { mkdir -p "$BASE"; echo "$(date -u +%FT%TZ) $1" >> "$BASE/poste-hetzner-reprise-v7-etat.txt"; echo "$1"; }

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
printf '%s\n' "$BASE/sortie-conduite-v16/*.battement" "$BASE/sortie-conduite-v16/**/*.battement" "*.battement" >> .git/info/exclude
etat "dépôt cloné : $(git rev-parse HEAD)"

# 3. empreintes et environnement Python
(cd "$BASE" && sha256sum -c --quiet poste-hetzner-reprise-v7.sh.sha256 manifeste-local-v7.json.sha256) \
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
[ -n "${VAST_API_KEY:-}" ] || { etat "clé Vast absente : rien ne tourne"; pousser "clé absente"; exit 3; }

# v7 (B′) : la conduite v16 doit être arrêtée (serveur du poste v14 détruit par la session, marque poussée), sinon rien ne tourne
[ -s "$BASE/arret-conduite-v16-poste-v14.json" ] || { etat "conduite v16 non arrêtée (arret-conduite-v16-poste-v14.json absent) : rien ne tourne"; pousser "conduite non arrêtée"; exit 3; }
# v7 : crédit Vast au moins 1,0 USD (transfert en marche, sans redémarrage : environ 0,4 USD), sinon rien ne tourne ;
# billing_failed relevé, non bloquant (recharge interdite, GO-2026-11-18-07 : son échec est attendu)
vastai show user --raw > /root/compte-avant.json || { etat "compte Vast illisible : rien ne tourne"; pousser "compte illisible"; exit 3; }
python3 - <<'EOF3' || { etat "crédit Vast sous 1,0 USD : rien ne tourne"; pousser "crédit insuffisant"; exit 3; }
import json, sys
u = json.load(open('/root/compte-avant.json'))
print('compte :', {k: u.get(k) for k in ('credit', 'billing_failed', 'has_billing', 'autobill_threshold', 'autobill_amount')})
sys.exit(0 if float(u.get('credit') or 0) >= 1.0 else 1)
EOF3
# v4 : dossiers de reprise déjà présents avant ce poste (venus par git) : non listés ici
AVANT=" $(cd "$BASE/sortie-conduite-v16" 2>/dev/null && ls -d reprise-v10* 2>/dev/null | tr "\n" " ") "
# inventaire R10 (v7) : l'instance à reprendre doit exister, en marche ; aucune autre instance du témoin
vastai show instances --raw > /root/inventaire-avant.json \
  || { etat "inventaire Vast illisible : rien ne tourne"; pousser "inventaire illisible"; exit 3; }
python3 - <<'EOF2' || { etat "inventaire non conforme : rien ne tourne"; pousser "inventaire non conforme"; exit 3; }
import json, sys
d = json.load(open("/root/inventaire-avant.json"))
t = [i for i in d if str(i.get("label") or "").startswith("temoin-bailey-c6-")]
ok = len(t) == 1 and str(t[0]["id"]) == "61170458" and t[0].get("label") == "temoin-bailey-c6-845f37c35eba4a3d" and t[0].get("actual_status") == "running" and t[0].get("intended_status") == "running"
print("instances du témoin :", [(i["id"], i.get("actual_status")) for i in t])
sys.exit(0 if ok else 1)
EOF2
etat "inventaire conforme : 61170458 seule instance du témoin, en marche"

# 4. reprise (lecture 38), poussées régulières
export GO_ID=GO-2026-11-17-07 DEPOT_URL=https://github.com/lciric/controle-ia-travail.git PYTHONPATH=$DEPOT/src
[ -e "$BASE/reprise-v7.pid" ] && { etat "PID de reprise déjà présent (R12) : rien ne tourne"; pousser "PID présent"; exit 3; }
cd "$DEPOT"
nohup setsid python -m controle_ia.temoin_bailey.lanceur_v21 reprendre \
  --sortie "$BASE/sortie-conduite-v16" --etiquette temoin-bailey-c6-845f37c35eba4a3d \
  --go-id GO-2026-11-17-07 --depot "$DEPOT" --arreter-en-cours \
  > "$BASE/reprise-v7.out" 2> "$BASE/reprise-v7.err" < /dev/null &
P=$!
echo "$P" > "$BASE/reprise-v7.pid"
etat "reprise lancée, PID $P"
pousser "reprise lancée (PID $P)"
while kill -0 "$P" 2>/dev/null; do
  sleep 600
  pousser "reprise : journaux $(date -u +%H:%MZ)"
done
wait "$P"; C=$?
etat "reprise terminée, code $C"
# v4 : liste des répertoires de chaque dossier de reprise (addendum 7, § 3), hors du dossier, avant la marque de fin
N=0
for R in "$BASE"/sortie-conduite-v16/reprise-v10*; do
  [ -d "$R" ] || continue
  case "$AVANT" in *" $(basename "$R") "*) etat "dossier antérieur au poste, non listé : $(basename "$R")"; continue;; esac
  L="repertoires-sortie-conduite-v16--$(basename "$R")-v1.txt"
  [ -e "$BASE/$L" ] && { etat "liste déjà présente, laissée telle quelle : $L"; continue; }
  (cd "$R" && find . -mindepth 1 -type d -printf '%P\n' | LC_ALL=C sort > "$BASE/$L")
  (cd "$BASE" && [ -f "$L" ] && LC_ALL=C sha256sum "$L" > "$L.sha256")
  N=$((N+1)); etat "liste des répertoires : $L ($(wc -l < "$BASE/$L" 2>/dev/null || echo absente) entrées ; compagnon $([ -s "$BASE/$L.sha256" ] && echo écrit || echo absent))"
done
[ "$N" -gt 0 ] || etat "aucun dossier de reprise neuf : aucune liste des répertoires"
pousser "listes des répertoires de reprise"
printf '{"fini": "%s", "pid": %s, "code": %s}\n' "$(date -u +%FT%TZ)" "$P" "$C" > "$BASE/poste-fini-reprise-v7.json"
pousser "reprise terminée (code $C)"
echo "fin $(date -u +%FT%TZ)"
