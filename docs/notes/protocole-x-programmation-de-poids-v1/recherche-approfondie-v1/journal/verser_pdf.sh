#!/usr/bin/env bash
# Usage : verser_pdf.sh IDENTIFIANT_ARXIV_AVEC_VERSION [...]
# Télécharge depuis export.arxiv.org vers sources/, écrit le compagnon .sha256, journalise. N'écrase jamais.
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"; SRC="$DIR/../sources"
J="$DIR/journal-des-versements-v1.tsv"
[ -f "$J" ] || printf 'heure_utc\tidentifiant\tcode_http\toctets\tpages\tsha256\n' > "$J"
for ID in "$@"; do
  F="$SRC/$ID.pdf"
  if [ -f "$F" ]; then echo "déjà versé : $ID"; continue; fi
  CODE=$(curl -sS -L --max-time 180 -A "generic-research-client/1.0" -o "$F.part" -w '%{http_code}' "https://export.arxiv.org/pdf/$ID" || echo ERR)
  if [ "$CODE" = "200" ] && head -c 5 "$F.part" | grep -q '%PDF'; then
    mv "$F.part" "$F"
    ( cd "$SRC" && sha256sum "$ID.pdf" > "$ID.pdf.sha256" )
    P=$(pdfinfo "$F" 2>/dev/null | awk '/^Pages:/{print $2}')
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$ID" "$CODE" "$(wc -c < "$F")" "$P" "$(cut -c1-64 "$SRC/$ID.pdf.sha256")" >> "$J"
    echo "versé : $ID ($P pages)"
  else
    echo "ÉCHEC : $ID code=$CODE"; mv "$F.part" "$F.echec" 2>/dev/null || true
    printf '%s\t%s\t%s\t-\t-\t-\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$ID" "$CODE" >> "$J"
  fi
  sleep 3
done
