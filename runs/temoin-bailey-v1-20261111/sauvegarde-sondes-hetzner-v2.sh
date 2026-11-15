#!/bin/bash
# Sauvegarde en lecture seule des sondes et des paramètres de l'attaquant de la relance (instance Vast 60480302) vers le
# v2 (15 novembre, 08:31Z) : `ssh -n` ; en v1, `ssh` lisait l'entrée standard de la boucle de copie et avalait la liste (66 fichiers sur 67 non copiés, passage 1, serveur 176186695 détruit) ; essai factice v1 aveugle à ce défaut.
# disque d'un serveur Hetzner jetable, avant la destruction de l'instance par la garde à B − 2. But : garder possible une
# continuation au-delà du tour coupé (décision à venir de Lazar). Aucune note lue : seuls `sondes/` et `params/` sont
# copiés, fichier par fichier, avec l'empreinte calculée sur l'instance et sur le serveur. À chaque passage, la liste
# (noms, tailles, empreintes, accord) est poussée sur la branche ; les fichiers restent sur le serveur. Passages toutes les
# PERIODE secondes jusqu'à l'instance injoignable trois fois de suite ou l'heure FIN. Gabarit : jetons @@…@@ remplacés par
# `construire-donnees-sauvegarde-hetzner-v1.py` ; aucune clé dans le dépôt.
set -uo pipefail
DEPOT=${SV_DEPOT:-/root/depot}
BRANCHE=claude/compassionate-meitner-d4ryyk
DISTANT=${SV_DISTANT:-git@github.com:lciric/controle-ia-travail.git}
REL=runs/temoin-bailey-v1-20261111/sauvegarde-sondes-v2
HOTE=@@HOTE@@
PORT=@@PORT@@
SOURCE=${SV_SOURCE:-/root/x/principal-relance}
DEST=${SV_DEST:-/root/sauvegarde}
PERIODE=${SV_PERIODE:-1200}
FIN=@@FIN@@
SSH_BIN=${SV_SSH:-ssh}
TMP=${SV_TMP:-/root}
exec >>"$TMP/sauvegarde-v2.log" 2>&1
echo "début $(date -u +%FT%TZ)"

if [ -z "${SV_ESSAI:-}" ]; then
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
OPTS=(-n -i /root/.ssh/vast -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=30
      -o BatchMode=yes -o ServerAliveInterval=15 -p "$PORT")
distant() { "$SSH_BIN" "${OPTS[@]}" "root@$HOTE" "$1"; }

mkdir -p "$DEST"
rm -rf "$DEPOT"
git clone -q --depth 5 --single-branch --branch "$BRANCHE" "$DISTANT" "$DEPOT" || { echo "clonage en échec"; exit 3; }
git -C "$DEPOT" config user.name "Claude"; git -C "$DEPOT" config user.email "noreply@anthropic.com"

pousser() {  # $1 : fichier de liste du passage
  local nom; nom=$(basename "$1")
  mkdir -p "$DEPOT/$REL"
  [ -e "$DEPOT/$REL/$nom" ] && { echo "liste $nom déjà présente (R12)"; return 1; }
  cp "$1" "$DEPOT/$REL/$nom"
  (cd "$DEPOT/$REL" && sha256sum "$nom" > "$nom.sha256")
  git -C "$DEPOT" add "$REL/$nom" "$REL/$nom.sha256"
  git -C "$DEPOT" commit -q -m "Témoin de Bailey : sauvegarde des sondes et paramètres de 60480302, liste $nom

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_016QhUrudziqEQujXt4ofM8u"
  for i in 1 2 3 4 5; do
    git -C "$DEPOT" pull -q --rebase origin "$BRANCHE" && git -C "$DEPOT" push -q origin "HEAD:$BRANCHE" && return 0
    git -C "$DEPOT" rebase --abort 2>/dev/null; sleep $((2 ** i))
  done
  echo "poussée en échec $(date -u +%FT%TZ)"; return 1
}

n=0; echecs=0
while :; do
  n=$((n + 1)); L="$TMP/liste-passage-$(printf %02d $n).tsv"
  if distant "cd $SOURCE && find sondes params -type f -print0 | xargs -0 -r sha256sum" > "$TMP/distant.sha" 2>"$TMP/distant.err"; then
    echecs=0
    while read -r sha chemin; do
      [ -z "$chemin" ] && continue
      case "$chemin" in sondes/*|params/*) ;; *) echo "chemin refusé : $chemin"; continue;; esac
      loc="$DEST/$chemin"
      if [ ! -f "$loc" ] || [ "$(sha256sum "$loc" | cut -d' ' -f1)" != "$sha" ]; then
        mkdir -p "$(dirname "$loc")"
        distant "cat '$SOURCE/$chemin'" > "$loc.part" && mv "$loc.part" "$loc"
      fi
    done < "$TMP/distant.sha"
    {
      printf "# passage %s %s : fichier\ttaille\tempreinte_instance\tempreinte_serveur\taccord\n" "$n" "$(date -u +%FT%TZ)"
      while read -r sha chemin; do
        [ -z "$chemin" ] && continue
        loc="$DEST/$chemin"; s=$(sha256sum "$loc" 2>/dev/null | cut -d' ' -f1); t=$(stat -c %s "$loc" 2>/dev/null)
        printf "%s\t%s\t%s\t%s\t%s\n" "$chemin" "${t:-0}" "$sha" "${s:-absent}" "$([ "$s" = "$sha" ] && echo oui || echo non)"
      done < "$TMP/distant.sha"
    } > "$L"
    if [ -f "$TMP/derniere.tsv" ] && cmp -s <(tail -n +2 "$L") <(tail -n +2 "$TMP/derniere.tsv"); then
      echo "passage $n : liste inchangée, rien n'est poussé"; rm -f "$L"
    else
      pousser "$L" && cp "$L" "$TMP/derniere.tsv"
    fi
  else
    echecs=$((echecs + 1)); echo "passage $n : instance injoignable ($echecs) $(head -c 300 "$TMP/distant.err")"
    [ "$echecs" -ge 3 ] && { echo "instance injoignable trois fois : fin"; break; }
  fi
  [ "$(date -u +%s)" -ge "$FIN" ] && { echo "heure de fin atteinte"; break; }
  sleep "$PERIODE"
done
[ -z "${SV_ESSAI:-}" ] && shred -u /root/.ssh/vast /root/.ssh/deploiement 2>/dev/null
echo "fin $(date -u +%FT%TZ) ; fichiers gardés dans $DEST"
