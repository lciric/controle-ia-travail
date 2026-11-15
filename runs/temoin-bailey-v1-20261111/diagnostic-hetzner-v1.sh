#!/bin/bash
# Diagnostic en lecture seule de l'instance Vast 60480302 (relance du témoin de Bailey), lancé au démarrage d'un serveur
# Hetzner jetable ; mot de Lazar « go Hetzner » (15 novembre 2026). Aucune note lue : processus, GPU, noms et dates des
# fichiers, nombre de lignes du journal des durées. Sortie poussée sur la branche, puis le serveur attend sa destruction
# (par son identifiant, depuis la session). Gabarit : les jetons @@…@@ sont remplacés par
# `construire-donnees-diagnostic-hetzner-v1.py` ; aucune clé n'est dans le dépôt.
set -uo pipefail
DEPOT=${DIAG_DEPOT:-/root/depot}
BRANCHE=claude/compassionate-meitner-d4ryyk
DISTANT=${DIAG_DISTANT:-git@github.com:lciric/controle-ia-travail.git}
SORTIE_REL=runs/temoin-bailey-v1-20261111/diagnostic-hetzner-v1-sortie.txt
HOTE=@@HOTE@@
PORT=@@PORT@@
RELAIS_HOTE=@@RELAIS_HOTE@@
RELAIS_PORT=@@RELAIS_PORT@@
SSH_BIN=${DIAG_SSH:-ssh}
TMP=${DIAG_TMP:-/root}
exec >>"$TMP/diagnostic-v1.log" 2>&1
echo "début $(date -u +%FT%TZ)"

if [ -z "${DIAG_ESSAI:-}" ]; then
  umask 077; mkdir -p /root/.ssh
  cat > /root/.ssh/deploiement <<'@@CLE_DEPLOIEMENT_FIN@@'
@@CLE_DEPLOIEMENT@@
@@CLE_DEPLOIEMENT_FIN@@
  cat > /root/.ssh/vast <<'@@CLE_VAST_FIN@@'
@@CLE_VAST@@
@@CLE_VAST_FIN@@
  chmod 600 /root/.ssh/deploiement /root/.ssh/vast; umask 022
  export DEBIAN_FRONTEND=noninteractive
  command -v git >/dev/null || { apt-get update -qq && apt-get install -y -qq git openssh-client; }
  ssh-keyscan -t ed25519 github.com >> /root/.ssh/known_hosts 2>/dev/null
  export GIT_SSH_COMMAND="ssh -i /root/.ssh/deploiement -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes"
fi

DIAG='date -u; uptime; echo "== GPU"; nvidia-smi --query-gpu=utilization.gpu,memory.used,temperature.gpu --format=csv; nvidia-smi --query-compute-apps=pid,used_memory --format=csv; echo "== PROCESSUS"; ps -eo pid,ppid,etimes,pcpu,pmem,stat,wchan:20,args --sort=-pcpu | cut -c1-220 | head -20; echo "== ETATS"; ls -l --time-style=full-iso /root/etats; echo "== FICHIERS RECENTS"; find /root/x -type f -printf "%TY-%Tm-%Td %TH:%TM %10s %p\n" 2>/dev/null | sort | tail -30; echo "== DUREES"; for f in $(find /root/x -name "sortie-durees*" 2>/dev/null); do echo "$f $(wc -l < "$f") lignes, modifié $(date -u -r "$f" +%FT%TZ)"; done; echo "== DISQUE"; df -h /root | tail -1; free -g | head -2'
OPTS=(-i /root/.ssh/vast -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=30 -o BatchMode=yes)

R="$TMP/diag-sortie.txt"
{
  echo "# Diagnostic en lecture seule de 60480302 — serveur Hetzner jetable — $(date -u +%FT%TZ)"
  echo "## direct $HOTE:$PORT"
  if "$SSH_BIN" "${OPTS[@]}" -p "$PORT" "root@$HOTE" "$DIAG"; then echo "## code 0 (direct)"
  else
    echo "## direct en échec (code $?) ; relais $RELAIS_HOTE:$RELAIS_PORT"
    "$SSH_BIN" "${OPTS[@]}" -p "$RELAIS_PORT" "root@$RELAIS_HOTE" "$DIAG"; echo "## code $? (relais)"
  fi
} > "$R" 2>&1

rm -rf "$DEPOT"
git clone -q --depth 5 --single-branch --branch "$BRANCHE" "$DISTANT" "$DEPOT" || { echo "clonage en échec"; exit 3; }
cd "$DEPOT" || exit 3
git config user.name "Claude"; git config user.email "noreply@anthropic.com"
[ -e "$SORTIE_REL" ] && { echo "sortie déjà présente (R12) : rien n'est poussé"; exit 3; }
cp "$R" "$SORTIE_REL"
sha256sum "$SORTIE_REL" | sed "s#  .*/#  #" > "$SORTIE_REL.sha256"
git add "$SORTIE_REL" "$SORTIE_REL.sha256"
git commit -q -m "Témoin de Bailey : diagnostic en lecture seule de 60480302 par serveur Hetzner jetable

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrudziqEQujXt4ofM8u"
for i in 1 2 3 4 5; do
  git pull -q --rebase origin "$BRANCHE" && git push -q origin "HEAD:$BRANCHE" && { echo "poussé $(date -u +%FT%TZ)"; break; }
  git rebase --abort 2>/dev/null; sleep $((2 ** i))
done
[ -z "${DIAG_ESSAI:-}" ] && shred -u /root/.ssh/vast /root/.ssh/deploiement 2>/dev/null
echo "fin $(date -u +%FT%TZ)"
