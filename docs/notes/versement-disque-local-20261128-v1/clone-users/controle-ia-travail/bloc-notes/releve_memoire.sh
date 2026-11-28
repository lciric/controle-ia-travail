#!/usr/bin/env bash
# Relevé de la mémoire résidente des processus « controle_ia.premier_test_ia.run » (lecture de /proc seulement), toutes
# les 30 s, et de la mémoire disponible de la machine, jusqu'à la fin de la répétition (fichier de durée écrit).
SORTIE=$1; FIN=$2
while [ ! -e "$FIN" ]; do
    t=$(date -u +%H:%M:%S)
    dispo=$(awk '/^MemAvailable:/ {print int($2/1024)}' /proc/meminfo)
    for p in /proc/[0-9]*; do
        c=$(tr '\0' ' ' < "$p/cmdline" 2>/dev/null) || continue
        case "$c" in
            python*controle_ia.premier_test_ia.run*)
                rss=$(awk '/^VmRSS:/ {print int($2/1024)}' "$p/status" 2>/dev/null)
                printf '%s pid %s rss %s Mo ; disponible %s Mo\n' "$t" "${p#/proc/}" "$rss" "$dispo" ;;
        esac
    done >> "$SORTIE"
    sleep 30
done
