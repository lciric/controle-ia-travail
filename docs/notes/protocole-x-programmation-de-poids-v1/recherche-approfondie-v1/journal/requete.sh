#!/usr/bin/env bash
# Journal des requêtes de la recherche approfondie (classe C).
# Usage : requete.sh CANAL "REQUETE EN CLAIR" URL [extension]
# Écrit la réponse brute sous journal/brut/ et une ligne au journal (heure UTC, canal, requête, code, octets, fichier, empreinte).
# Client générique : aucun nom de programme, de personne, ni chemin interne dans la requête.
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
CANAL="$1"; REQ="$2"; URL="$3"; EXT="${4:-txt}"
J="$DIR/journal-des-requetes-v1.tsv"
[ -f "$J" ] || printf 'rang\theure_utc\tcanal\trequete\tcode_http\toctets\tfichier_brut\tsha256\turl\n' > "$J"
N=$(( $(wc -l < "$J") ))
F=$(printf '%s/brut/%03d-%s.%s' "$DIR" "$N" "$CANAL" "$EXT")
CODE=$(curl -sS -L --max-time 90 -A "generic-research-client/1.0" -o "$F" -w '%{http_code}' "$URL" 2>"$F.err" || echo "ERR")
[ -s "$F.err" ] || rm -f "$F.err"
SZ=$( [ -f "$F" ] && wc -c < "$F" || echo 0 )
H=$( [ -f "$F" ] && sha256sum "$F" | cut -c1-64 || echo - )
printf '%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$N" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$CANAL" "$REQ" "$CODE" "$SZ" "$(basename "$F")" "$H" "$URL" >> "$J"
echo "$N $CODE $SZ $F"
