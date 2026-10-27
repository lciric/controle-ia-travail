#!/usr/bin/env bash
# Contrôle du prix de l'instance créée, comparaison d'échelle v8 (lignée « session-depot », 27 octobre 2026 ; CLY-13,
# CLZ-03, CLZ-04), copie de `controler_prix_v7.sh` sous un nom nouveau (R12) après la contre-lecture n° 7, sans
# changement. Extrait du lanceur pour
# être testé (R5) : relit l'instance (champs de prix seulement, jamais la
# réponse brute dans un journal : elle porte l'environnement de l'instance), compare chaque prix relu à l'offre choisie
# par `choisir_offre_v8.py --prix-relu` (tolérance comptée dans le pire) ; s'il n'est pas conforme ou pas lisible :
# arrêt de l'instance par son identifiant (R10), puis état relu.
# Usage : VASTAI=<chemin de vastai 1.8.3> controler_prix_v8.sh ID OFFRE_JSON JOURNAL
# Chaque appel à vastai est borné à 60 s (CLW-08).
# Codes : 0 conforme ; 4 non conforme ou illisible, arrêt relu ; 6 non conforme ou illisible, arrêt non relu (vérifier
# l'instance à la main, champs filtrés) ; 2 usage.
# ATTENTE_ARRET_S ne sert qu'aux essais.
set -uo pipefail
[ $# -eq 3 ] || { echo "usage : controler_prix_v8.sh ID OFFRE_JSON JOURNAL"; exit 2; }
ID=$1; OFFRE=$2; J=$3
V=${VASTAI:?VASTAI : chemin de l outil vastai 1.8.3}
ICI=$(cd "$(dirname "$0")" && pwd)
ATTENTE_ARRET_S=${ATTENTE_ARRET_S:-20}
[[ "$ID" =~ ^[0-9]+$ ]] && [ -f "$OFFRE" ] || { echo "identifiant ou offre illisible"; exit 2; }
if timeout 60 "$V" show instance "$ID" --raw 2>/dev/null | python3 -I -B "$ICI/choisir_offre_v8.py" --prix-relu "$OFFRE" >> "$J" 2>&1; then
    echo "instance $ID : prix relu conforme" | tee -a "$J"
    exit 0
fi
echo "instance $ID : prix relu non conforme ou illisible : arrêt par son identifiant (R10)" | tee -a "$J"
timeout 60 "$V" stop instance "$ID" >> "$J" 2>&1
sleep "$ATTENTE_ARRET_S"
e=$(timeout 60 "$V" show instance "$ID" --raw 2>/dev/null | python3 -I -B -c '
import json, sys
try:
    i = json.load(sys.stdin)
    assert isinstance(i, dict)
    print(i.get("actual_status"), i.get("cur_state"))
except Exception:
    print("illisible")')
echo "instance $ID : état relu après l'arrêt : $e" | tee -a "$J"
case "$e" in
    *stopped*|*exited*) exit 4 ;;
    *) echo "arrêt non relu : vérifier l'instance $ID à la main (champs filtrés)" | tee -a "$J"; exit 6 ;;
esac
