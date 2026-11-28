#!/usr/bin/env bash
# Surveillance externe v1 du serveur de la suite des tests (GO-2026-11-28-04), jouée dans le conteneur de la mère.
# Toutes les 5 minutes : état et étiquettes du serveur par l'API Hetzner, présence de la branche de sortie.
# Suppression par identifiant numérique (R10, jamais par motif) dans deux cas seulement :
#   - 15 minutes après la première vue de la branche de sortie, si le serveur ne s'est pas détruit lui-même ;
#   - au-delà de la limite absolue LIMITE_EPOCH (rempart du plafond de durée).
# Sort dès que l'API répond 404 pour ce serveur. Le jeton n'apparaît ni en argument de commande ni au journal.
set -uo pipefail
ID="${1:?identifiant du serveur}"
BRANCHE="${2:?branche de sortie}"
LIMITE_EPOCH="${3:?limite absolue en secondes depuis 1970}"
JOURNAL="${4:?journal}"
DEPOT="${5:-/home/user/controle-ia-travail}"
API="${HCLOUD_API:-https://api.hetzner.cloud/v1}"
: "${HCLOUD_TOKEN:?HCLOUD_TOKEN absent}"
case "$ID" in ''|*[!0-9]*) echo "identifiant non numérique : $ID" >&2; exit 2 ;; esac
ENTETE="$(mktemp)"
chmod 600 "$ENTETE"
printf 'Authorization: Bearer %s\n' "$HCLOUD_TOKEN" > "$ENTETE"
trap 'rm -f "$ENTETE"' EXIT
VU_POUSSEE=""
while true; do
  MAINTENANT="$(date +%s)"
  REPONSE="$(curl -s --max-time 30 -H @"$ENTETE" -w '\n%{http_code}' "$API/servers/$ID")"
  CODE="$(tail -n1 <<<"$REPONSE")"
  CORPS="$(sed '$d' <<<"$REPONSE")"
  STATUT="$(jq -r '.server.status // "-"' <<<"$CORPS" 2>/dev/null)"
  ETIQ="$(jq -c '.server.labels // {}' <<<"$CORPS" 2>/dev/null)"
  SHA="$(git -C "$DEPOT" ls-remote origin "refs/heads/$BRANCHE" 2>/dev/null | cut -f1)"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) serveur=$ID http=$CODE statut=$STATUT etiquettes=$ETIQ branche=${SHA:-absente}" >> "$JOURNAL"
  if [ "$CODE" = 404 ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) serveur $ID absent de l'API : surveillance close" >> "$JOURNAL"
    exit 0
  fi
  if [ -n "$SHA" ] && [ -z "$VU_POUSSEE" ]; then VU_POUSSEE="$MAINTENANT"; fi
  if { [ -n "$VU_POUSSEE" ] && [ $((MAINTENANT - VU_POUSSEE)) -ge 900 ]; } || [ "$MAINTENANT" -ge "$LIMITE_EPOCH" ]; then
    C="$(curl -s -o /dev/null -w '%{http_code}' --max-time 30 -X DELETE -H @"$ENTETE" "$API/servers/$ID")"
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) DELETE servers/$ID -> $C (rempart externe)" >> "$JOURNAL"
  fi
  sleep 300
done
