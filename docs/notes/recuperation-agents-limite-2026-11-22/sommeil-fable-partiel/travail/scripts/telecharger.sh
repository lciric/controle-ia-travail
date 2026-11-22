#!/bin/bash
# usage: telecharger.sh NOM_FICHIER ADRESSE
# Télécharge dans sources/, relève l'heure (date -u), calcule l'empreinte, écrit le compagnon .sha256, journalise.
OUT=/tmp/claude-0/-home-user-controle-ia-travail/d69341ed-1da2-5804-bff1-02b01c73e5e7/scratchpad/sommeil-fable
nom="$1"; url="$2"
dest="$OUT/sources/$nom"
if [ -e "$dest" ]; then echo "EXISTE DEJA: $dest (non écrasé)"; exit 3; fi
code=$(curl -sS -L --max-time 180 -A "Mozilla/5.0 (X11; Linux x86_64) research-client" -o "$dest.part" -w "%{http_code}" "$url")
h=$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ "$code" != "200" ]; then echo "ECHEC code=$code url=$url"; rm -f "$dest.part"; printf '%s\t%s\t%s\t%s\n' "$h" "ECHEC-$code" "$nom" "$url" >> "$OUT/travail/journal/telechargements.tsv"; exit 1; fi
type=$(file -b "$dest.part" | cut -c1-60)
mv "$dest.part" "$dest"
e=$(sha256sum "$dest" | cut -d' ' -f1)
( cd "$OUT/sources" && sha256sum "$nom" > "$nom.sha256" )
taille=$(stat -c %s "$dest")
printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$h" "$e" "$nom" "$url" "$taille" "$type" >> "$OUT/travail/journal/telechargements.tsv"
echo "OK $nom $e $taille octets [$type] $h"
