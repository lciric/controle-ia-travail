#!/usr/bin/env bash
# Téléchargement d'une source ouverte, avec heure (date -u), code de réponse, type et empreinte.
# Usage : telecharger_v1.sh DOSSIER_SOURCES NOM_DE_FICHIER ADRESSE
# Écrit une ligne dans DOSSIER_SOURCES/../travail/journal-telechargements-v1.tsv ; ne remplace jamais un fichier présent (R12).
set -u
dossier="$1"; nom="$2"; adresse="$3"
journal="$dossier/../travail/journal-telechargements-v1.tsv"
if [ -e "$dossier/$nom" ]; then echo "présent, non remplacé : $nom"; exit 0; fi
tmp="$(mktemp)"
rep="$(curl -sS -L --max-time 120 -A 'Mozilla/5.0 (compatible; client-generique)' -o "$tmp" -w '%{http_code}\t%{size_download}\t%{content_type}' "$adresse" 2>&1)"
heure="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
type="$(file -b "$tmp" | cut -c1-40)"
case "$type" in
  PDF*) mv "$tmp" "$dossier/$nom"; chmod 644 "$dossier/$nom"
        emp="$(sha256sum "$dossier/$nom" | cut -d' ' -f1)"
        pages="$(pdfinfo "$dossier/$nom" 2>/dev/null | awk '/^Pages:/{print $2}')"
        printf '%s\t%s\t%s\t%s\t%s\t%s p.\tgardé\n' "$heure" "$nom" "$adresse" "$rep" "$emp" "$pages" >> "$journal"
        echo "gardé : $nom ($pages p.) $emp" ;;
  *)    rm -f "$tmp"
        printf '%s\t%s\t%s\t%s\t-\t-\trefusé (%s)\n' "$heure" "$nom" "$adresse" "$rep" "$type" >> "$journal"
        echo "refusé : $nom [$rep] type=$type" ;;
esac
