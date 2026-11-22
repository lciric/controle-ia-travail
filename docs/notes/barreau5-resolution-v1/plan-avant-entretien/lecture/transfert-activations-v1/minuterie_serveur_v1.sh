#!/usr/bin/env bash
# Minuterie de destruction du serveur de transfert des activations du barreau 5 — v1 (22 novembre 2026, classe B).
# Procédure : ../procedure-transfert-activations-b5f-v1.md, § 4. Accord : GO-2026-11-22-117.
# Tenue HORS du serveur, dans la session qui l'a créé, lancée en arrière-plan ; son PID est consigné ; elle s'arrête par ce
# PID seul (R10). À l'échéance : DELETE /v1/servers/ID par l'identifiant, puis GET /v1/servers/ID jusqu'à 404 ; la
# destruction n'est jamais jugée par le code de la demande, seulement par le 404 relu (puis par la liste, à la main).
# Le jeton HCLOUD_TOKEN est lu par son nom et passé à curl par l'entrée standard (`-K -`) : jamais dans les arguments,
# jamais au journal. Le volume n'est jamais touché ici (protégé contre la suppression, détaché par la destruction).
# Usage : minuterie_serveur_v1.sh ID ECHEANCE_UTC_S JOURNAL
# Essai : MINUTERIE_PAS_S (pas de veille, 30 par défaut), MINUTERIE_ESSAIS_MAX (0 = sans fin), API_HETZNER (faux serveur).
set -uo pipefail
ID="${1:-}"; ECHEANCE="${2:-}"; J="${3:-}"
API="${API_HETZNER:-https://api.hetzner.cloud/v1}"
PAS="${MINUTERIE_PAS_S:-30}"
MAXI="${MINUTERIE_ESSAIS_MAX:-0}"
MAINTENANT=$(date +%s)
case "$ID" in ''|*[!0-9]*) echo "MINUTERIE REFUS : identifiant numérique attendu (R10)"; exit 2;; esac
case "$ECHEANCE" in ''|*[!0-9]*) echo "MINUTERIE REFUS : échéance (secondes UTC) illisible"; exit 2;; esac
[ -n "$J" ] || { echo "MINUTERIE REFUS : journal attendu"; exit 2; }
[ -n "${HCLOUD_TOKEN:-}" ] || { echo "MINUTERIE REFUS : HCLOUD_TOKEN absent (par le nom) : la minuterie ne détruirait rien"; exit 2; }
[ $((ECHEANCE - MAINTENANT)) -le $((24 * 3600)) ] || { echo "MINUTERIE REFUS : échéance au-delà de 24 heures (devis v2, § 3)"; exit 2; }
j() { printf '%s MINUTERIE %s\n' "$(date -u +%FT%TZ)" "$*" >> "$J"; }
appel() {  # $1 = méthode ; code HTTP sur la sortie, rien d'autre
    printf 'header = "Authorization: Bearer %s"\n' "$HCLOUD_TOKEN" \
        | curl -sS -m 60 -K - -o /dev/null -w '%{http_code}' -X "$1" "$API/servers/$ID" 2> /dev/null || echo 000; }
j "lancée (PID $$) pour le serveur $ID, échéance $(date -u -d "@$ECHEANCE" +%FT%TZ)"
while [ "$(date +%s)" -lt "$ECHEANCE" ]; do sleep "$PAS"; done
n=0
while :; do
    n=$((n + 1))
    c=$(appel GET)
    if [ "$c" = 404 ]; then j "serveur $ID absent (GET 404) : destruction prouvée par la relecture ; fin"; exit 0; fi
    d=$(appel DELETE)
    j "échéance atteinte : DELETE du serveur $ID par son identifiant, essai $n : HTTP $d (GET précédent : HTTP $c)"
    [ "$MAXI" != 0 ] && [ "$n" -ge "$MAXI" ] && { j "essais épuisés (essai seulement) : serveur non prouvé détruit"; exit 4; }
    sleep "$PAS"
done
