#!/usr/bin/env bash
# Filet indépendant v2 du serveur de la suite des tests (GO-2026-11-28-04 ; majeur 5 de la contre-lecture de classe B
# du lot v1). Lancé dès le démarrage par `systemd-run --on-active=<plafond + 45 min>` depuis les données de démarrage,
# indépendamment de l'amorce : si l'amorce n'a pas détruit le serveur (échec avant ses pièges, SIGKILL, panne mémoire,
# échec de systemd-run), ce filet le supprime par son identifiant numérique (R10, jamais par motif).
# Le jeton n'est lu que par curl, depuis un fichier d'en-tête 0600 ; il n'apparaît ni en argument ni au journal.
set -u
ENTETE="${1:-/opt/suite-tests/entete-filet}"
JOURNAL="${2:-/opt/suite-tests/journal-filet.txt}"
METADONNEES="${METADONNEES:-http://169.254.169.254/hetzner/v1/metadata}"
HCLOUD_API="${HCLOUD_API:-https://api.hetzner.cloud/v1}"
PAUSE="${PAUSE_FILET:-30}"
ID=""
for i in 1 2 3 4 5; do
  ID="$(curl -fsS --max-time 10 "$METADONNEES/instance-id" 2>/dev/null || true)"
  case "$ID" in ''|*[!0-9]*) ID=""; sleep 5 ;; *) break ;; esac
done
if [ -z "$ID" ]; then
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) filet : identifiant introuvable" >> "$JOURNAL"
  exit 1
fi
for i in 1 2 3 4 5 6; do
  CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 30 -X DELETE -H @"$ENTETE" "$HCLOUD_API/servers/$ID")"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) filet : DELETE servers/$ID -> $CODE" >> "$JOURNAL"
  case "$CODE" in 200|201|202|204|404) exit 0 ;; esac
  sleep "$PAUSE"
done
exit 1
