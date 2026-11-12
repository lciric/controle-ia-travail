#!/bin/bash
# Sorties v2 (aucun réseau, aucune clé) ; PYTHONHASHSEED=0 fixé en plus des parcours triés (E-2) ; aucune sortie écrasée.
set -u
O="$1"; D="$(cd "$(dirname "$0")" && pwd)"; P="python3 -I -B"; export PYTHONHASHSEED=0
cd "$D"
j() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*" >> "$O/journal-sorties-v2.txt"; }
j "début ; python $(python3 -c 'import platform,numpy;print(platform.python_version(), numpy.__version__)') ; PYTHONHASHSEED=$PYTHONHASHSEED"
$P essais_v2.py > "$O/essais-v2.stdout" 2> "$O/essais-v2.stderr"; j "essais code $?"
$P devis_multi_generations_v2.py "$O/devis-v2.json" > "$O/devis-v2.stdout" 2>&1; j "devis code $?"
$P puissance_monde_riche_v2.py representant "$O/representant-w12-v2.json" --mondes 12 > "$O/representant-w12-v2.stdout" 2>&1; j "représentant code $?"
$P puissance_monde_riche_v2.py doublons "$O/doublons-w12-v2.json" --mondes 12 > "$O/doublons-w12-v2.stdout" 2>&1; j "doublons code $?"
$P puissance_monde_riche_v2.py attribution "$O/attribution-w12-v2.json" --mondes 12 > "$O/attribution-w12-v2.stdout" 2>&1; j "attribution code $?"
$P puissance_monde_riche_v2.py archive "$O/archive-w8-r30-v2.json" --mondes 8 --repetitions 30 > "$O/archive-w8-r30-v2.stdout" 2>&1; j "archive code $?"
$P puissance_monde_riche_v2.py detection "$O/detection-w12-r40-v2.json" --mondes 12 --repetitions 40 > "$O/detection-w12-r40-v2.stdout" 2>&1; j "détection code $?"
$P puissance_monde_riche_v2.py generations "$O/generations-w12-g3-n400-v2.json" --mondes 12 > "$O/generations-w12-g3-n400-v2.stdout" 2>&1; j "générations code $?"
PYTHONHASHSEED=1 $P puissance_monde_riche_v2.py generations "$O/reproductibilite-generations-w2-hash1-v2.json" --mondes 2 > /dev/null 2>&1; j "reproductibilité (graine de hachage 1, 2 mondes) code $?"
$P banc_generateur_v2.py "$O/banc-generateur-w12-v2.json" 12 > "$O/banc-generateur-w12-v2.stdout" 2>&1; j "banc générateur code $?"
j "fin"
