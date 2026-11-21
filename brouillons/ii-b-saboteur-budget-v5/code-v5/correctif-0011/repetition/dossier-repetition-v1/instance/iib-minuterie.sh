ECH="$1"; DEP="$2"; R="$3"; API="$4"; J="$R/iib-minuterie.log"
PAS="${MINUTERIE_PAS_S:-5}"; REESSAI="${MINUTERIE_REESSAI_S:-60}"; MARGE="${MINUTERIE_MARGE_S:-1800}"
case "$PAS" in ''|*[!0-9]*) PAS=5;; esac; case "$REESSAI" in ''|*[!0-9]*) REESSAI=60;; esac
case "$MARGE" in ''|*[!0-9]*) MARGE=1800;; esac; case "$DEP" in ''|*[!0-9]*) DEP=0;; esac
echo "$(date -u +%FT%TZ) minuterie $$ : échéance $ECH, dépense épuisée à $DEP" >> "$J"
echo "$$" > "$R/iib-minuterie.pid"
case "${CONTAINER_ID:-}" in ''|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME : identifiant d'instance illisible : aucun geste" >> "$J"; exit 3;; esac
consigner() {  # C14, C08 : résultats partiels committés et poussés par le script écrit par l'amorce (git seul)
    if [ -f "$R/iib-consigner.sh" ]; then timeout -k 10 2400 bash "$R/iib-consigner.sh" "$1" >> "$J" 2>&1; echo "$(date -u +%FT%TZ) consigné ($1) : code $?" >> "$J"
    else echo "$(date -u +%FT%TZ) rien à consigner ($1) : dépôt non extrait" >> "$J"; fi; }
appel() {  # méthode, corps JSON (vide pour DELETE) ; écrit le code HTTP
    local c
    if command -v curl >/dev/null 2>&1; then
        if [ -n "$2" ]; then c=$(curl -sS -m 60 -o "$R/iib-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" -H 'Content-Type: application/json' -d "$2" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000
        else c=$(curl -sS -m 60 -o "$R/iib-api-corps.txt" -w '%{http_code}' -X "$1" -H "Authorization: Bearer ${CONTAINER_API_KEY:-}" "$API/instances/$CONTAINER_ID/" 2>/dev/null) || c=000; fi
    elif command -v python3 >/dev/null 2>&1; then
        c=$(python3 -I -B -c 'import os, sys, urllib.error, urllib.request
corps = sys.argv[3].encode() if sys.argv[3] else None
q = urllib.request.Request(sys.argv[1], data=corps, method=sys.argv[2], headers={"Authorization": "Bearer " + os.environ.get("CONTAINER_API_KEY", ""), "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(q, timeout=60) as r:
        code, corps = r.status, r.read()
except urllib.error.HTTPError as e:
    code, corps = e.code, e.read()
except Exception:
    code, corps = 0, b""
open(sys.argv[4], "wb").write(corps)
print("%03d" % code)' "$API/instances/$CONTAINER_ID/" "$1" "$2" "$R/iib-api-corps.txt" 2>/dev/null) || c=000
    else c=aucun; fi
    echo "$c"
}
while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/iib-detruire" ]; do
    if [ "$DEP" -gt 0 ] && [ "$(date +%s)" -ge "$DEP" ] && [ ! -e "$R/iib-depense-epuisee" ]; then
        echo "$(date -u +%FT%TZ) DÉPENSE ÉPUISÉE (C08, plafond de la configuration cumulé) : consignation, poussée, puis état « stopped »" >> "$J"
        echo "dépense épuisée $(date -u +%FT%TZ)" > "$R/iib-depense-epuisee"
        consigner "dépense épuisée"
        if [ -e "$R/iib-detruire" ]; then echo "$(date -u +%FT%TZ) PUT stopped non envoyé : ordre de destruction de l'amorce reçu pendant la consignation (R-1689)" >> "$J"
        else c=$(appel PUT '{"state": "stopped"}'); echo "$(date -u +%FT%TZ) PUT stopped (dépense épuisée) : HTTP $c" >> "$J"; fi
    fi
    sleep "$PAS"
done
raison="échéance"; [ -e "$R/iib-detruire" ] && raison="ordre de l'amorce"
if [ "$raison" = "échéance" ]; then echo "$(date -u +%FT%TZ) ÉCHÉANCE $ECH atteinte (C14) : consignation et poussée des résultats partiels avant la destruction" >> "$J"; consigner "échéance"; fi
FIN=$(( $(date +%s) + MARGE )); n=0
while :; do
    n=$((n + 1))
    if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then
        echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue avant la fin de la marge" >> "$J"; exit 4
    fi
    c=$(appel DELETE '')
    if [ "$c" = aucun ]; then echo "$(date -u +%FT%TZ) ALARME : ni curl ni python3 : aucune destruction possible" >> "$J"; exit 5; fi
    refus=non; grep -qiE '"success"[[:space:]]*:[[:space:]]*false' "$R/iib-api-corps.txt" 2>/dev/null && refus=oui
    echo "$(date -u +%FT%TZ) DELETE instance $CONTAINER_ID (essai $n, $raison) : HTTP $c, refus dans le corps : $refus" >> "$J"
    case "$c" in 2??) if [ "$refus" = non ]; then echo "$(date -u +%FT%TZ) instance $CONTAINER_ID détruite" >> "$J"; exit 0; fi;; esac
    [ "$(date +%s)" -lt "$FIN" ] || { echo "$(date -u +%FT%TZ) ALARME : destruction non obtenue" >> "$J"; exit 4; }
    sleep "$REESSAI"
done
